local io = io
local ipairs = ipairs
local print = print
local table = table
local tonumber = tonumber

local lines = {}
for line in io.lines() do
    table.insert(lines, tonumber(line))
end

local count = 0
for i, l in ipairs(lines) do
    if lines[i-1] and l > lines[i-1] then
        count = count + 1
    end
end

print("Part 1: ", count)

local function sum(t)
    local s = 0
    for _, x in ipairs(t) do
        s = s + x
    end
    return s
end

local window_count = 0
for i, _ in ipairs(lines) do
    if lines[i-3] then
        if sum({table.unpack(lines, i-3, i-1)}) < sum({table.unpack(lines, i-2, i)}) then
            window_count = window_count + 1
        end
    end
end

print("Part 2: ", window_count)
