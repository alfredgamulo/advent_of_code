import time as timer
start_time = timer.time()
import re

with open("input") as f:
    lines = f.read().splitlines()

class operand1(object):
    def __init__(self, data):
        self.data = data

    def __sub__(self, other):
        return operand1(self.data * other.data)

    def __add__(self, other):
        return operand1(self.data + other.data)

print("Part 1:", sum([eval(''.join([f'operand1({o})' if o.isdigit() else (o,"-")[o == "*"] for o in line])).data for line in lines]))

class operand2(object):
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return operand2(self.data * other.data)

    def __mul__(self, other):
        return operand2(self.data + other.data)

print("Part 2:", sum([eval(''.join([f'operand2({o})' if o.isdigit() else ("+","*","(",")"," ")[["*","+","(",")"," "].index(o)] for o in line])).data for line in lines]))

print("--- %s millis ---" % ((timer.time() - start_time)*1000))
