require("inspect")
local io = io
local ipairs = ipairs
local math = math
local print = print
local table = table
local tonumber = tonumber

local lines = {}
for line in io.lines() do
    table.insert(lines, line)
end

local crabs = {}
for _, line in ipairs(lines) do
    for l in line:gmatch("([^,]+)") do
        l = tonumber(l)
        table.insert(crabs, l)
    end
end

local function findmedian (numlist)
    local copy = {}
    for j,x in ipairs(numlist) do copy[j] = x end
    if type(copy) ~= 'table' then return copy end
    table.sort(copy)
    if #copy %2 == 0 then return (copy[#copy/2] + copy[#copy/2+1]) / 2 end
    return copy[math.ceil(#copy/2)]
end

local function sum(t)
    local s = 0
    for _, x in ipairs(t) do
        s = s + x
    end
    return s
end

local median = findmedian(crabs)
local fuel = {}
for _, c in ipairs(crabs) do
    table.insert(fuel, math.abs(median - c))
end

print("Part 1:", sum(fuel))

local average = math.floor(sum(crabs) / #crabs) -- but also ceil??
fuel = {}
for _, c in ipairs(crabs) do
    local f = {}
    for i=1,math.abs(average-c) do
        table.insert(f, i)
    end
    table.insert(fuel, sum(f))
end

print("Part 2:", sum(fuel))
