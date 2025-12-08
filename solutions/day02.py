import re

def parse_input(raw_input: str, is_test_input: bool):
    input = []
    for range in raw_input.strip().split(','):
        lower, upper = range.split('-')
        input.append((int(lower), int(upper)))
    return input


def part1(input):
    pattern = re.compile(r'(\d+)\1')
    return sum(i for l, u in input for i in range(l, u) if pattern.fullmatch(str(i)))


def part2(input):
    pattern = re.compile(r'(\d+)\1+')
    return sum(i for l, u in input for i in range(l, u) if pattern.fullmatch(str(i)))
