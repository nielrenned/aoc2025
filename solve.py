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
    parser.add_argument('-d', '--day', type=int, required=False)
    parser.add_argument('-t', '--test', action='store_true')
    args = parser.parse_args()

    days = [args.day] if args.day else range(1, 13)

    print()
    for day_number in days:
        try:
            day = importlib.import_module(f'solutions.day{day_number:02}')
        except:
            break
        raw_input = load_input(day_number, args.test)
        input = day.parse_input(raw_input, args.test)
        
        print(f'Day {day_number:02}')
        print('------')
        if (day1_result := day.part1(input)) is not None:
            print('PART 1:', day1_result)
        if (day2_result := day.part2(input)) is not None:
            print('PART 2:', day2_result)
        print()


if __name__ == '__main__': main()