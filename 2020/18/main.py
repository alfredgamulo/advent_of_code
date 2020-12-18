import time as timer
start_time = timer.time()

with open("input") as f:
    lines = f.read().splitlines()

class operand(object):
    def __init__(self, data):
        self.data = data

    def __mul__(self, other):
        return operand(self.data * other.data)

    def __mod__(self, other):
        return operand(self.data + other.data)

    def __pow__(self, other):
        return operand(self.data + other.data)

print("Part 1:", sum([eval(''.join([f'operand({o})' if o.isdigit() else (o,"%")[o == "+"] for o in line])).data for line in lines]))

print("Part 2:", sum([eval(''.join([f'operand({o})' if o.isdigit() else (o,"**")[o == "+"] for o in line])).data for line in lines]))

print("--- %s millis ---" % ((timer.time() - start_time)*1000))
