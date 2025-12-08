def parse_input(raw_input: str, is_test_input: bool):
    input = []
    for line in raw_input.split('\n'):
        if line == '': continue
        dir, clicks = line[:1], line[1:]
        input.append((dir, int(clicks)))
    return input


def part1(input):
    dial = 50
    count = 0
    for dir, clicks in input:
        sign = -1 if dir == 'R' else 1
        dial = (dial + sign*clicks) % 100
        if dial == 0: count += 1
    return count


def part2(input):
    dial = 50
    count = 0
    for dir, clicks in input:
        sign = -1 if dir == 'R' else 1
        for _ in range(clicks):
            dial = (dial + sign) % 100
            if dial == 0: count += 1
    return count
