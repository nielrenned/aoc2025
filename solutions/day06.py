from functools import reduce
from operator import __add__, __mul__


product = lambda l: reduce(__mul__, l, 1)
concat = lambda l: reduce(__add__, l, '')


def parse_input(raw_input: str):
    lines = list(filter(lambda s: s != '', raw_input.split('\n')))
    op_line = lines[-1]

    problems = []
    op_indices = [i for i, c in enumerate(op_line) if c in ['+', '*']] + [len(op_line) + 1]
    for x in range(len(op_indices)-1):
        i, j = op_indices[x:x+2]
        padded_num_strings = [row[i:j-1] for row in lines[:-1]]
        problems.append((op_line[i], padded_num_strings))

    return problems


def part1(input):
    total = 0
    for op, num_strings in input:
        numbers = map(int, num_strings)
        if op == '+': total += sum(numbers)
        if op == '*': total += product(numbers)
    
    return total


def part2(input):
    total = 0
    for op, num_strings in input:
        width = len(num_strings[0])
        numbers = [int(concat(s[i] for s in num_strings)) for i in range(width)]

        if op == '+': total += sum(numbers)
        if op == '*': total += product(numbers)

    return total