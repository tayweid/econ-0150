-- Translate reveal.js-flavored constructs into native pandoc elements so the
-- PowerPoint writer keeps them. Pandoc drops raw HTML in pptx; this converts
-- it instead of losing it.

local function attr_of(html, name)
  return html:match(name .. '%s*=%s*"([^"]*)"') or html:match(name .. "%s*=%s*'([^']*)'")
end

-- <img src=... height=...>  ->  Image  (height carried as a pandoc attribute)
local function img_to_image(html)
  local src = attr_of(html, 'src')
  if not src then return nil end
  local attrs = {}
  local h = attr_of(html, 'height')
  if h then
    if not h:match('%a') then h = h .. 'px' end
    attrs['height'] = h
  end
  return pandoc.Image({}, src, '', pandoc.Attr('', {}, attrs))
end

function RawInline(el)
  if el.format ~= 'html' then return nil end
  local t = el.text
  if t:match('^%s*<img') then
    local im = img_to_image(t)
    if im then return im end
    return {}
  end
  -- structural/styling-only inline HTML carries nothing in pptx
  if t:match('^%s*</?%s*br') or t:match('^%s*</?%s*center')
     or t:match('^%s*</?%s*span') or t:match('^%s*</?%s*p[%s>]') then
    return {}
  end
  return nil
end

function RawBlock(el)
  if el.format ~= 'html' then return nil end
  local t = el.text

  -- <p class="subheader">text</p>  ->  italic paragraph
  local cls = attr_of(t, 'class')
  local inner = t:match('<p[^>]*>(.-)</p>')
  if inner and cls and cls:match('subheader') then
    inner = inner:gsub('<[^>]+>', '')
    if inner:match('%S') then
      return pandoc.Para({ pandoc.Emph(pandoc.Str(inner)) })
    end
    return {}
  end

  -- a raw block that is (or contains) images -> real Image blocks
  if t:match('<img') then
    local imgs = {}
    for tag in t:gmatch('<img[^>]*>') do
      local im = img_to_image(tag)
      if im then table.insert(imgs, im) end
    end
    if #imgs > 0 then return pandoc.Para(imgs) end
  end

  return {}   -- any other raw HTML block would be dropped anyway
end

-- Reveal's .columns/.column: pandoc's pptx writer honors at most two columns,
-- so discard the empty spacer columns reveal uses for centering. A slide with
-- spacer/Card/spacer/Krueger/spacer then becomes a real two-column slide.
function Div(el)
  if el.classes:includes('columns') then
    local kept = {}
    for _, blk in ipairs(el.content) do
      if blk.t == 'Div' and blk.classes:includes('column') then
        local txt = pandoc.utils.stringify(blk)
        local has_img = false
        pandoc.walk_block(blk, { Image = function() has_img = true end })
        if txt:match('%S') or has_img then table.insert(kept, blk) end
      else
        table.insert(kept, blk)
      end
    end
    if #kept > 2 then                  -- more real columns than pptx supports
      local flat = {}
      for _, blk in ipairs(kept) do
        for _, inner in ipairs(blk.content or { blk }) do table.insert(flat, inner) end
      end
      return flat
    end
    el.content = kept
    return el
  end
  -- incremental/fragment reveals are meaningless in pptx; keep contents
  if el.classes:includes('incremental') or el.classes:includes('fragment')
     or el.classes:includes('fragments') then
    return el.content
  end
  return nil
end

-- Reveal's ". . ." pause marker is literal text to the pptx writer. Drop it
-- both as a standalone paragraph and where a missing blank line in the source
-- made pandoc glue it onto the end of the preceding paragraph.
local function is_dots(inline)
  return inline.t == 'Str' and inline.text:match('^%.+$') ~= nil
end

function Para(el)
  local flat = pandoc.utils.stringify(el):gsub('%s', '')
  if flat ~= '' and flat:match('^%.+$') then return {} end

  -- count the trailing run of dot-words (". . ." is three separate Strs)
  local i, dots = #el.content, 0
  while i > 0 do
    local it = el.content[i]
    if is_dots(it) then dots = dots + 1
    elseif it.t ~= 'Space' and it.t ~= 'SoftBreak' then break end
    i = i - 1
  end
  if dots >= 3 then                     -- distinctive enough not to hit prose ellipses
    local kept = {}
    for j = 1, i do kept[j] = el.content[j] end
    if #kept == 0 then return {} end
    el.content = kept
    return el
  end
  return nil
end
