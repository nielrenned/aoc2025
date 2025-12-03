def parse_input(raw_input: str):
    input = []
    for line in raw_input.split('\n'):
        if line == '': continue
        input.append(list(map(int, line)))
    return input


def part1(input):
    return sum(maximize_bank(bank, 2) for bank in input)


def part2(input):
    return sum(maximize_bank(bank, 12) for bank in input)


def maximize_bank(bank: list[int], battery_count: int):
    joltage = 0
    i = -1
    for n in range(battery_count, 0, -1):
        # Make sure we always have at least n batteries left to turn on
        bank_left = bank[i+1:len(bank)-(n-1)]
        m = max(bank_left)
        i += bank_left.index(m) + 1
        joltage = joltage * 10 + m
    return joltage