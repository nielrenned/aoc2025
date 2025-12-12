from z3.z3 import *
from queue import Queue

def parse_input(raw_input: str, is_test_input: bool):
    input = []
    for line in raw_input.split('\n'):
        if line == '': continue
        pieces = line.split(' ')
        lights = list(map(lambda c: True if c == '#' else False, pieces[0][1:-1]))
        buttons = [tuple(map(int, piece[1:-1].split(','))) for piece in pieces[1:-1]]
        joltage = list(map(int, pieces[-1][1:-1].split(',')))
        input.append((lights, buttons, joltage))
    return input


def part1(input):
    return sum(get_min_pushes_lights(lights, buttons) for lights, buttons, _ in input)


def part2(input):
    return sum(get_min_pushes_joltage(joltages, buttons) for i, (_, buttons, joltages) in enumerate(input))


def get_min_pushes_lights(lights_goal, buttons):
    # We can BFS until we find a solution
    q = Queue()
    q.put((0, [0]*len(lights_goal)))
    while not q.empty():
        depth, old_lights = q.get()
        for button in buttons:
            lights = old_lights[:]
            for light in button:
                lights[light] = not lights[light]
            if lights == lights_goal:
                return depth+1
            q.put((depth+1, lights))


def get_min_pushes_joltage(joltages, buttons):
    solver = Optimize()
    presses = [Int(f'p{i}') for i in range(len(buttons))]
    for p in presses:
        solver.add(p >= 0)
    for joltage_index, joltage in enumerate(joltages):
        expr = sum(press for j, press in enumerate(presses) if joltage_index in buttons[j])
        solver.add(expr == joltage)
    solver.minimize(sum(presses))
    
    solver.check()
    result = solver.model()
    return sum(result[p].py_value() for p in presses)
