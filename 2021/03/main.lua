local io = io
local ipairs = ipairs
local print = print
local table = table
local tonumber = tonumber

local lines = {}
local count = 0
for line in io.lines() do
    table.insert(lines, line)
    count = count + 1
end
local half  = count / 2

local vbits = {}
for _, line in ipairs(lines) do
    local i = 1
    for b in line:gmatch("%d") do
        if not vbits[i] then
            vbits[i] = {}
        end
        table.insert(vbits[i], b)
        i = i + 1
    end
end

local function sum(t)
    local s = 0
    for _, x in ipairs(t) do
        s = s + x
    end
    return s
end

local g = ""
local e = ""
for _, b in ipairs(vbits) do
    if sum(b) > half then
        g = g.."1"
        e = e.."0"
    else
        g = g.."0"
        e = e.."1"
    end
end

print("Part 1:", tonumber(g,2)*tonumber(e,2))