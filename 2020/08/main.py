with open("input") as f:
    code = [(x, int(y)) for x, y in (line.split() for line in f.readlines())]
    
class AssMachine():
    def __init__(self, ass):
        self.ass = ass
        self.accumulator = 0
        
    def run(self):
        pos = 0
        vis = set()
        clean = True
        while pos < len(self.ass):
            if pos in vis:
                clean = False
                break
            op = self.ass[pos][0]
            val = self.ass[pos][1]
            vis.add(pos)
            if op == "nop":
                pos += 1
                continue
            if op == "acc":
                self.accumulator += val
                pos += 1
                continue
            if op == "jmp":
                pos += val
                continue
        
        return (clean, self.accumulator)

# part 1
a = AssMachine(code)
print(a.run())

# part 2
for i in range(len(code)):
    a = AssMachine([c for c in code])
    if 'jmp' == code[i][0]:
        a.ass[i] = ("nop", a.ass[i][1])
    elif 'nop' == code[i][0]:
        a.ass[i] = ("jmp", a.ass[i][1])
    rc = a.run()
    if rc[0]:
        print(rc[1])
        break