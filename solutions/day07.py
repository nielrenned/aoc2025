from collections import defaultdict

def parse_input(raw_input: str, is_test_input: bool):
    lines = list(filter(lambda s: s != '', raw_input.split('\n')))

    start = None
    splitters = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S': start = (x, y)
            if c == '^': splitters.add((x, y))
    
    return start, splitters


def part1(input):
    (start_x, start_y), splitters = input
    max_y = max(y for _, y in splitters) + 1

    split_count = 0
    beams = {start_x}
    for y in range(start_y + 1, max_y + 1, 2):
        new_beams = set()
        for x in beams:
            if (x, y+1) in splitters:
                split_count += 1
                new_beams.add(x - 1)
                new_beams.add(x + 1)
            else:
                new_beams.add(x)
        beams = new_beams
    
    return split_count


def part2(input):
    (start_x, start_y), splitters = input
    max_y = max(y for _, y in splitters) + 1

    beam_counts = {start_x: 1}
    for y in range(start_y + 1, max_y + 1, 2):
        new_counts = defaultdict(int)
        for x in beam_counts:
            if (x, y+1) in splitters:
                new_counts[x - 1] += beam_counts[x]
                new_counts[x + 1] += beam_counts[x]
            else:
                new_counts[x] += beam_counts[x]
        beam_counts = new_counts
    
    return sum(beam_counts[x] for x in beam_counts)