import importlib
import argparse


def load_input(day, use_test_input):
    path = f'inputs/actual/day{day:02}.txt'
    if use_test_input:
        path = f'inputs/test/day{day:02}.txt'
    with open(path) as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser(prog='python solve.py', description='Advent of Code 2025 solutions')
    parser.add_argument('day_number', type=int)
    parser.add_argument('-t', '--test', action='store_true')
    args = parser.parse_args()

    day = importlib.import_module(f'solutions.day{args.day_number:02}')
    raw_input = load_input(args.day_number, args.test)
    input = day.parse_input(raw_input)
    
    if day1_result := day.part1(input):
        print('PART 1:', day1_result)
    if day2_result := day.part2(input):
        print('PART 2:', day2_result)


if __name__ == '__main__': main()