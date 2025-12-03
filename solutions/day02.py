def parse_input(raw_input: str):
    input = []
    for range in raw_input.strip().split(','):
        lower, upper = range.split('-')
        input.append((int(lower), int(upper)))
    return input


def part1(input):
    total = 0
    for lower, upper in input:
        for i in range(lower, upper+1):
            s = str(i)
            if test(s, 2):
                total += i
    return total


# We could do something much more complicated here,
# but this code runs quick enough on my machine
def part2(input):
    total = 0
    for lower, upper in input:
        for i in range(lower, upper+1):
            s = str(i)
            if any(test(s, n) for n in range(2, len(s)+1)):
                total += i
    return total


def test(s: str, n: int):
    '''returns True if n >= 2 and s == t repeated n times, where t is any non-empty string.'''
    if n <= 1 or len(s) % n != 0 or len(s) == 0: return False
    
    l = len(s) // n
    piece = s[:l]
    for i in range(l, len(s), l):
        if s[i:i+l] != piece:
            return False
    return True
