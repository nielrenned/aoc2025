from itertools import combinations, product

def parse_input(raw_input: str, is_test_input: bool):
    input = []
    for line in raw_input.split('\n'):
        if line == '': continue
        input.append(tuple(map(int, line.split(','))))
    return input


def part1(input):
    return max(rect_area(p1, p2) for p1, p2 in combinations(input, 2))


def part2(input):
    poly_segments = list(zip(input, input[1:] + input[:1]))
    return max(
        rect_area(p1, p2)
        for p1, p2 in combinations(input, 2)
        if rect_inside_polygon(p1, p2, poly_segments)
    )


def rect_area(p1, p2):
    return (abs(p1[0] - p2[0])+1)*(abs(p1[1] - p2[1])+1)


def rect_inside_polygon(rect_p1, rect_p2, poly_segments):
    rect_segments = shrunken_rect_segments(rect_p1, rect_p2)
    return not any(segments_intersect(r, p) for r, p in product(rect_segments, poly_segments))


def shrunken_rect_segments(p1, p2):
    (x1, y1), (x2, y2) = sorted((p1, p2))
    return [
        ((x1+1, y1+1), (x1+1,y2-1)),
        ((x1+1, y1+1), (x2-1,y1+1)),
        ((x2-1, y2-1), (x1+1,y2-1)),
        ((x2-1, y2-1), (x2-1,y1+1)),
    ]

def segments_intersect(l1, l2):
    (x1, y1), (x2, y2) = l1
    (x3, y3), (x4, y4) = l2

    if y1 == y2 and y3 == y4:
        # Both horizontal at same y-value, so x-ranges must overlap
        return y1 == y3 and ranges_overlap(x1, x2, x3, x4)
    elif x1 == x2 and x3 == x4:
        # Both vertical at same x-value, so y-ranges must overlap
        return x1 == x3 and ranges_overlap(y1, y2, y3, y4)
    else:
        return ranges_overlap(x1, x2, x3, x4) and ranges_overlap(y1, y2, y3, y4)


def ranges_overlap(a, b, c, d):
    # Returns True if there exists an integer that is 
    # between a and b (inclusive) and between c and d (inclusive)
    return not (max(a, b) < min(c, d) or max(c, d) < min(a, b))




