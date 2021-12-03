local io = io
local ipairs = ipairs
local print = print
local string = string
local table = table
local tonumber = tonumber

local lines = {}
for line in io.lines() do
    table.insert(lines, line)
end