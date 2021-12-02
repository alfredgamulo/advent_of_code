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

local function travel(position, operations)
    for _, line in ipairs(lines) do
        local instructions = {}
        for l in string.gmatch(line, "[^%s]+") do
            table.insert(instructions, l)
        end
        position = operations[instructions[1]](position, tonumber(instructions[2]))
    end
    return position[1]*position[2]
end

local operations = {
    up      = function(p, n) return { p[1], p[2] - n} end,
    down    = function(p, n) return { p[1], p[2] + n} end,
    forward = function(p, n) return { p[1] + n, p[2]} end,
}
print("Part 1: ", travel({0, 0}, operations))

operations = {
    up      = function(p, n) return { p[1], p[2], p[3] - n} end,
    down    = function(p, n) return { p[1], p[2], p[3] + n} end,
    forward = function(p, n) return { p[1] + n, p[2] + n*p[3], p[3]} end,
}
print("Part 2: ", travel({0, 0, 0}, operations))