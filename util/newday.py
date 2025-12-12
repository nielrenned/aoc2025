import argparse
import os

TEMPLATE = """def parse_input(raw_input: str, is_test_input: bool):
    input = []
    for line in raw_input.split('\\n'):
        if line == '': continue
        input.append(line)
    return input


def part1(input):
    pass


def part2(input):
    pass
"""


def main():
    parser = argparse.ArgumentParser(prog='python newday.py', description='My Advent of Code solution template generator')
    parser.add_argument('day', type=int)
    args = parser.parse_args()
    
    solution_filename = f'solutions/day{args.day:02}.py'
    if os.path.exists(solution_filename):
        print(f'Error: {solution_filename} already exists.')
        return
    
    with open(solution_filename, 'w') as f:
        f.write(TEMPLATE)

    test_input_filename = f'inputs/test/day{args.day:02}.txt'
    if not os.path.exists(test_input_filename):
        with open(test_input_filename, 'w') as f:
            f.write('')

    print('Files created!')


if __name__ == "__main__":
    main()