def parse_input(raw_input: str, is_test_input: bool):
    chunks = raw_input.split('\n\n')
    presents = []
    for diagram in chunks[:-1]:
        presents.append(tuple(
            (x-1, y-2) # centered coordinates
            for y, line in enumerate(diagram.split('\n'))
            for x, c in enumerate(line)
            if c == '#'
        ))
    
    regions = []
    for line in chunks[-1].split('\n'):
        if line == '': continue
        dims, counts = line.split(': ')
        dims = tuple(map(int, dims.split('x')))
        counts = tuple(map(int, counts.split(' ')))
        regions.append((dims, counts))
    
    return presents, regions


def part1(input):
    presents, regions = input
    # The inputs for this particular problem are designed in such a way
    # that just comparing sizes gives a correct answer. Except this doesn't 
    # work for the test input!! I guess that would be too obvious...
    return sum(
        1 for (w, h), counts in regions 
        if sum(c*len(p) for c, p in zip(counts, presents)) <= w*h
    )


def part2(input):
    # No puzzle for part 2 on the last day :)
    return 'Merry Christmas!'
