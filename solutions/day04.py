DIRECTIONS = [
    (1, 0), (-1, 0), (0, 1), (0, -1), 
    (1, 1), (-1, 1), (1, -1), (-1, -1), 
]

def parse_input(raw_input: str, is_test_input: bool):
    input = set()
    for y, line in enumerate(raw_input.split('\n')):
        if line == '': continue
        for x, c in enumerate(line):
            if c == '@': input.add((x, y))
    return input


def part1(input):
    return sum(
        1 for x, y in input
        if sum(1 for dx, dy in DIRECTIONS if (x+dx, y+dy) in input) < 4
    )


def part2(input):
    rolls = input
    while True:
        new_rolls = set(
            (x, y) for x, y in rolls
            if sum(1 for dx, dy in DIRECTIONS if (x+dx, y+dy) in rolls) >= 4       
        )
        
        if len(rolls) == len(new_rolls): break
        rolls = new_rolls
    
    return len(input) - len(rolls)
