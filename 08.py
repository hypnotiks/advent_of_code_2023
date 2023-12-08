import math

f = open('08-input', 'r')
lines = f.read().split("\n")

class Instruction:
    def __init__(self, line):
        self.key = line.split('=')[0].strip()
        self.starting_key = self.key[-1] == 'A'
        self.left = line.split('=')[1].strip().split(',')[0].strip()[1:]
        self.right = line.split('=')[1].strip().split(',')[1].strip()[:-1]

    def next_instruction(self, direction):
        if direction == "L":
            return self.left
        elif direction == "R":
            return self.right

input_instructions = dict() 
current_instructions = []
for line in lines[2:]:
    i = Instruction(line)
    input_instructions[i.key] = i
    if i.starting_key:
        current_instructions.append(i)

found = True
steps_to_end = []
for instruction in current_instructions:
    found = len(steps_to_end) == len(current_instructions)
    steps = 0
    current_instruction = input_instructions[instruction.key]
    while not found:
        for direction in lines[:1][0]:
            next_location = input_instructions[current_instruction.next_instruction(direction)]
            steps += 1
            if next_location.key[-1] == 'Z':
                found = True
                steps_to_end.append(steps)
                break

            current_instruction = next_location

print("total steps: {0}".format(math.lcm(*steps_to_end)))