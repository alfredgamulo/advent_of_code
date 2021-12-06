local io = io
local ipairs = ipairs
local print = print
local table = table
local tonumber = tonumber

local lines = {}
for line in io.lines() do
    table.insert(lines, line)
end


local function sum(t)
    local s = 0
    for _, x in ipairs(t) do
        s = s + x
    end
    return s
end


local function solve(days)
    local fish = {0, 0, 0, 0, 0, 0, 0, 0, 0}

    for _, line in ipairs(lines) do
        for l in line:gmatch("%d") do
            l = tonumber(l)
            fish[l] = fish[l] + 1
        end
    end

    for _=1,days-1 do
        local left = fish[1]
        for i, f in ipairs(fish) do
            if i > 1 then
                fish[i-1] = f
            end
        end
        fish[7] = fish[7] + left
        fish[9] = left
    end
    return sum(fish)
end


print("Part 1:", solve(80))
print("Part 2:", solve(256))
