with open("input") as f:
    code = [(x, int(y)) for x, y in (line.split() for line in f.readlines())]
    
class Machine():
    def __init__(self, code):
        self.code = code

    def run(self):
        pos = 0
        acc = 0
        vis = set()
        while pos < len(self.code):
            if pos in vis:
                return (False, acc)
            op = self.code[pos][0]
            jmp = 1
            vis.add(pos)
            if op == "acc":
                acc += self.code[pos][1]
            elif op == "jmp":
                jmp = self.code[pos][1]
            pos += jmp
        
        return (True, acc)

# part 1
m = Machine(code)
print("part 1:", m.run()[1])

# part 2
for i in range(len(code)):
    if 'acc' == code[i][0]:
        continue
    m.code = code[:]
    if 'jmp' == code[i][0]:
        m.code[i] = ("nop", code[i][1])
    elif 'nop' == code[i][0]:
        m.code[i] = ("jmp", code[i][1])
    rc, acc = m.run()
    if rc:
        print("part 2:", acc)
        break
