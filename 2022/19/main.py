import re
import sys
from functools import cache


@cache
def dig(
    step,
    ore,
    clay,
    obs,
    ore_bots,
    clay_bots,
    obs_bots,
    ore_bot_ore,
    clay_bot_ore,
    obs_bot_ore,
    obs_bot_clay,
    geo_bot_ore,
    geo_bot_obs,
):
    if step <= 1:
        return 0

    geodes = []

    if ore >= geo_bot_ore and obs >= geo_bot_obs:
        geodes.append(
            dig(
                step - 1,
                ore + ore_bots - geo_bot_ore,
                clay + clay_bots,
                obs + obs_bots - geo_bot_obs,
                ore_bots,
                clay_bots,
                obs_bots,
                ore_bot_ore,
                clay_bot_ore,
                obs_bot_ore,
                obs_bot_clay,
                geo_bot_ore,
                geo_bot_obs,
            )
            + step
            - 1
        )
    if ore >= obs_bot_ore and clay >= obs_bot_clay and obs_bots < geo_bot_obs:
        geodes.append(
            dig(
                step - 1,
                ore + ore_bots - obs_bot_ore,
                clay + clay_bots - obs_bot_clay,
                obs + obs_bots,
                ore_bots,
                clay_bots,
                obs_bots + 1,
                ore_bot_ore,
                clay_bot_ore,
                obs_bot_ore,
                obs_bot_clay,
                geo_bot_ore,
                geo_bot_obs,
            )
        )
    geodes.append(
        dig(
            step - 1,
            ore + ore_bots,
            clay + clay_bots,
            obs + obs_bots,
            ore_bots,
            clay_bots,
            obs_bots,
            ore_bot_ore,
            clay_bot_ore,
            obs_bot_ore,
            obs_bot_clay,
            geo_bot_ore,
            geo_bot_obs,
        )
    )
    if ore >= ore_bot_ore and ore_bots < max(clay_bot_ore, obs_bot_ore, geo_bot_ore):
        geodes.append(
            dig(
                step - 1,
                ore + ore_bots - ore_bot_ore,
                clay + clay_bots,
                obs + obs_bots,
                ore_bots + 1,
                clay_bots,
                obs_bots,
                ore_bot_ore,
                clay_bot_ore,
                obs_bot_ore,
                obs_bot_clay,
                geo_bot_ore,
                geo_bot_obs,
            ),
        )

    if ore >= clay_bot_ore and clay_bots < obs_bot_clay:
        geodes.append(
            dig(
                step - 1,
                ore + ore_bots - clay_bot_ore,
                clay + clay_bots,
                obs + obs_bots,
                ore_bots,
                clay_bots + 1,
                obs_bots,
                ore_bot_ore,
                clay_bot_ore,
                obs_bot_ore,
                obs_bot_clay,
                geo_bot_ore,
                geo_bot_obs,
            ),
        )

    return max(geodes)


def part1(blueprints):
    dig.cache_clear()
    res = 0
    for b in blueprints:
        g = dig(24, 0, 0, 0, 1, 0, 0, *b[1:7])
        res += b[0] * g
    return res


def part2(blueprints):
    dig.cache_clear()
    res = 1
    for b in blueprints[:3]:
        g = dig(32, 0, 0, 0, 1, 0, 0, *b[1:7])
        res = res * g
    return res


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    blueprints = []
    for line in lines:
        # id, ore bot cost, clay bot cost, obsidian bot cost (ore, clay), geode bot cost (ore, obsidian)
        blueprints.append(list(map(int, re.findall(r"\d+", line))))

    print("Part 1:", part1(blueprints))
    print("Part 2:", part2(blueprints))
