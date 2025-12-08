from collections import defaultdict
from itertools import combinations

def parse_input(raw_input: str, is_test_input: bool):
    points = []
    for line in raw_input.split('\n'):
        if line == '': continue
        points.append(tuple(map(int, line.split(','))))
    
    # Pre-calculate the distances
    distances = []
    for p1, p2 in combinations(points,2):
        d = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
        distances.append((d, (p1, p2)))
    distances.sort()

    num_connections = 10 if is_test_input else 1000

    return num_connections, points, distances


def part1(input):
    num_connections, points, distances = input
    
    circuits = {p: c for c, p in enumerate(points)}
    for _, (p1, p2) in distances[:num_connections]:
        c1 = circuits[p1]
        c2 = circuits[p2]
        if c1 == c2: continue

        min_id = min(c1, c2)
        max_id = max(c1, c2)
        for p, id in circuits.items():
            if id == max_id:
                circuits[p] = min_id
    
    sizes = defaultdict(int)
    for id in circuits.values():
        sizes[id] += 1
    a, b, c = sorted(sizes.values())[-3:]

    return a * b * c


def part2(input):
    _, points, distances = input

    circuits = {p: c for c, p in enumerate(points)}
    circuit_count = len(points)
    for _, (p1, p2) in distances:
        c1 = circuits[p1]
        c2 = circuits[p2]
        if c1 == c2: continue

        # Connecting two _different_ circuits reduces the total circuit count by 1
        circuit_count -= 1
        if circuit_count == 1:
            return p1[0] * p2[0]

        min_id = min(c1, c2)
        max_id = max(c1, c2)
        for p, id in circuits.items():
            if id == max_id:
                circuits[p] = min_id
        