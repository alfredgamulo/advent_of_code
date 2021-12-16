import sys
import math
from io import StringIO

hex = sys.stdin.readline().strip()
binary = StringIO("".join(format(int(h, 16), "04b") for h in hex))
versions = []
operators = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0,
}


def read_subpacket(binary):
    if binary.read(1) == "0":
        length = int(binary.read(15), 2)
        return read_packets(StringIO(binary.read(length)))
    else:
        length = int(binary.read(11), 2)
        return [read_packet(binary) for _ in range(length)]


def read_packet(binary):
    try:
        versions.append(int(binary.read(3), 2))
        type = int(binary.read(3), 2)
        if type == 4:
            end_packet = False
            packet = ""
            while not end_packet:
                chunk = binary.read(5)
                if chunk[0] == "0":
                    end_packet = True
                packet += chunk[1:]
            return int(packet, 2)
        else:
            return operators[type](read_subpacket(binary))
    except ValueError:
        pass


def read_packets(binary):
    packets = []
    while (packet := read_packet(binary)) is not None:
        packets.append(packet)
    return packets


part2 = read_packets(binary)[0]
print("Part 1:", sum(versions))
print("Part 2:", part2)
