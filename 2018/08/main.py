import sys
from collections import deque
from contextlib import suppress
from dataclasses import dataclass


@dataclass
class Node:
    children: []
    header: ()
    metadata: []


def process(tree):
    n = Node([], (), [])
    header = (tree.popleft(), tree.popleft())
    n.header = header
    for _ in range(header[0]):
        child = process(tree)
        n.children.append(child)
    metadata = []
    for _ in range(header[1]):
        metadata.append(tree.popleft())
    n.metadata = metadata
    return n


def part1(node):
    total = 0
    if node.children:
        for c in node.children:
            total += part1(c)
    total += sum(node.metadata)
    return total


def part2(node):
    total = 0
    if node.children:
        for i in node.metadata:
            with suppress(IndexError):
                total += part2(node.children[i - 1])
    else:
        total += sum(node.metadata)
    return total


if __name__ == "__main__":
    lines = sys.stdin.read()
    tree = deque(map(int, lines.split()))
    node = process(tree)

    print("Part 1:", part1(node))
    print("Part 2:", part2(node))
