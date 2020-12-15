import time as timer
start_time = timer.time()

with open("input") as f:
    line = [int(l) for l in f.readline().strip().split(',')]

def play_memory(turns):
    memory = {v:i+1 for i,v in enumerate(line[:])}
    last = line[-1]
    for i in range(len(memory), turns):
        try:
            last_spoken = i - memory[last]
        except KeyError:
            last_spoken = 0
        memory[last] = i
        last = last_spoken
    return last

print("Part 1:", play_memory(2020))
print("Part 2:", play_memory(30000000))

print("--- %s millis ---" % ((timer.time() - start_time)*1000))
