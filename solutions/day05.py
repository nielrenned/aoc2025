from itertools import product

def parse_input(raw_input: str, is_test_input: bool):
    lines = raw_input.split('\n')
    blank_line = lines.index('')

    ranges = {tuple(map(int, line.split('-'))) for line in lines[:blank_line]}
    ids = [int(line) for line in lines[blank_line+1:] if line != '']
    return (ranges, ids)


def part1(input):
    ranges, ids = input
    return len({id for id in ids for a, b in ranges if a <= id <= b})


def part2(input):
    ranges, _ = input

    # Combine all overlapping intervals
    while True:
        for (a, b), (c, d) in product(ranges, ranges):
            if a == c and b == d: continue
            if a <= c <= b or c <= a <= d:
                ranges -= {(a, b), (c, d)}
                ranges.add((min(a, c), max(b, d)))
                break
        else:
            break
    
    return sum(b - a + 1 for a, b in ranges)
