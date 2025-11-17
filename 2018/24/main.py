import copy
import os
import re
import string
import sys
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from functools import cache, cmp_to_key, reduce
from heapq import heappop, heappush
from io import StringIO
from itertools import (batched, chain, combinations, count, groupby,
                       permutations, product, zip_longest)
from math import ceil, floor, lcm, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter
from typing import List, Optional, Set, Tuple


@dataclass
class Group:
    id: int
    team: str
    units: int
    hp: int
    weaknesses: Set[str]
    immunities: Set[str]
    attack_damage: int
    attack_type: str
    initiative: int

    def effective_power(self) -> int:
        return self.units * self.attack_damage


def parse(lines: List[str]) -> List[Group]:
    groups: List[Group] = []
    team = None
    gid = 1
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.endswith(':'):
            team = line[:-1]
            continue
        # parse line
        # example: 18 units each with 729 hit points (weak to fire; immune to cold, slashing) with an attack that does 8 radiation damage at initiative 10
        units_part, rest = line.split(' units each with ')
        units = int(units_part)
        hp_part, rest = rest.split(' hit points')
        hp = int(hp_part)

        weaknesses = set()
        immunities = set()
        rest = rest.strip()
        if rest.startswith('('):
            paren_end = rest.find(')')
            inside = rest[1:paren_end]
            rest = rest[paren_end+1:].strip()
            # clauses separated by ';'
            for clause in inside.split(';'):
                clause = clause.strip()
                if clause.startswith('weak to '):
                    types = clause[len('weak to '):].split(',')
                    for t in types:
                        weaknesses.add(t.strip())
                elif clause.startswith('immune to '):
                    types = clause[len('immune to '):].split(',')
                    for t in types:
                        immunities.add(t.strip())

        # rest should contain: with an attack that does 8 radiation damage at initiative 10
        # remove leading 'with '
        rest = rest.lstrip()
        # find 'with an attack that does '
        aidx = rest.find('with an attack that does ')
        if aidx >= 0:
            rest2 = rest[aidx+len('with an attack that does '):]
        else:
            # some inputs may use 'with an attack that does'
            rest2 = rest
        dmg_part, rest3 = rest2.split(' damage at initiative ')
        # dmg_part like '8 bludgeoning' or '525 slashing'
        parts = dmg_part.strip().split()
        attack_damage = int(parts[0])
        attack_type = parts[1]
        initiative = int(rest3.strip())

        groups.append(Group(gid, team, units, hp, weaknesses, immunities, attack_damage, attack_type, initiative))
        gid += 1

    return groups


def simulate(orig_groups: List[Group], boost: int = 0) -> Tuple[Optional[str], int]:
    # deep copy groups
    groups = [Group(g.id, g.team, g.units, g.hp, set(g.weaknesses), set(g.immunities), g.attack_damage, g.attack_type, g.initiative) for g in orig_groups]
    # apply boost to Immune System
    for g in groups:
        if g.team == 'Immune System':
            g.attack_damage += boost

    while True:
        # remove dead groups
        groups = [g for g in groups if g.units > 0]
        teams = set(g.team for g in groups)
        if len(teams) == 1:
            # someone won
            total = sum(g.units for g in groups)
            return (next(iter(teams)), total)

        # target selection
        # attackers sorted by effective power then initiative
        selection_order = sorted(groups, key=lambda g: (g.effective_power(), g.initiative), reverse=True)
        targets = {}
        chosen = set()
        for attacker in selection_order:
            enemies = [g for g in groups if g.team != attacker.team and g.id not in chosen and g.units > 0]
            # pick target maximizing damage
            best = None
            best_damage = 0
            for e in enemies:
                if attacker.attack_type in e.immunities:
                    dmg = 0
                elif attacker.attack_type in e.weaknesses:
                    dmg = attacker.effective_power() * 2
                else:
                    dmg = attacker.effective_power()
                if dmg <= 0:
                    continue
                # tie-breaker: highest damage, then effective power, then initiative
                key = (dmg, e.effective_power(), e.initiative)
                if best is None or key > best[0]:
                    best = (key, e)
            if best:
                targets[attacker.id] = best[1].id
                chosen.add(best[1].id)

        # attacking phase: order by initiative desc
        attack_order = sorted(groups, key=lambda g: g.initiative, reverse=True)
        total_killed = 0
        id_to_group = {g.id: g for g in groups}
        for attacker in attack_order:
            if attacker.units <= 0:
                continue
            if attacker.id not in targets:
                continue
            defender = id_to_group.get(targets[attacker.id])
            if defender is None or defender.units <= 0:
                continue
            # compute damage
            if attacker.attack_type in defender.immunities:
                dmg = 0
            elif attacker.attack_type in defender.weaknesses:
                dmg = attacker.effective_power() * 2
            else:
                dmg = attacker.effective_power()
            killed = min(defender.units, dmg // defender.hp)
            if killed > 0:
                defender.units -= killed
                total_killed += killed

        if total_killed == 0:
            # stalemate
            return (None, 0)


def part1(lines: List[str]) -> int:
    groups = parse(lines)
    winner, total = simulate(groups, boost=0)
    return total


def part2(lines: List[str]) -> int:
    groups = parse(lines)
    boost = 1
    # incrementally search for minimal boost where Immune System wins
    while True:
        winner, total = simulate(groups, boost=boost)
        if winner == 'Immune System':
            return total
        boost += 1


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
