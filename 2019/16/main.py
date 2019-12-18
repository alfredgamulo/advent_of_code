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
    signal = signal*10000
    working_signal = signal[offset:]
    phase = working_signal[::-1]
    
    for l in range(loops):
        # print(l)
        new_phase = []
        new_p = 0
        for p in phase:
            new_p = (p + new_p) % 10
            new_phase.append(new_p)
        phase = new_phase
    return "".join(map(str,phase[-1:-9:-1]))


print("Part 2:", part2(100))