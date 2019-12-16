def read_input(file):
    with open(file) as f:
        return [int(d) for d in f.readline().strip()]


def part1(loops):
    signal = read_input("input")
    base_pattern = (0, 1, 0, -1)
    
    phase = signal[:]
    
    for l in range(1, loops+1):
        new_phase = []
        for i in range(1, len(phase)+1):
            pattern = []
            for b in base_pattern:
                pattern.extend([b]*i)
            pattern = pattern * ((len(phase)//len(pattern)) + 1)
            pattern = pattern[1:]
            
            new_p = 0
            for j, p in enumerate(phase):
                if pattern[j] != 0:
                    new_p = new_p + (p * pattern[j])
            new_phase.append(abs(new_p) % 10)
        phase = new_phase
    return "".join(map(str,phase[:8]))


print("Part 1:", part1(100))


def part2(loops):
    signal = read_input("input")
    offset = int("".join(map(str, signal[:7])))
    print(offset)
    signal = signal*10000
    
    print(signal[offset:offset+8])
    return None


print("Part 2:", part2(100))