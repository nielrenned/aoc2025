import sys
import os

template = """def parse_input(raw_input: str):
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
    if len(sys.argv) != 2:
        print('Usage: python newday.py <day_num>')
        return
    
    try:
        day_num = int(sys.argv[1])
    except ValueError:
        print(f'Error: {sys.argv[1]} is not an integer.')
        return
    
    solution_filename = f'solutions/day{day_num:02}.py'
    if os.path.exists(solution_filename):
        print(f'Error: {solution_filename} already exists.')
        return
    
    with open(solution_filename, 'w') as f:
        f.write(template.format(day=day_num))

    test_input_filename = f'inputs/test/day{day_num:02}.txt'
    if not os.path.exists(test_input_filename):
        with open(test_input_filename, 'w') as f:
            f.write('')

    print('Files created!')


if __name__ == "__main__":
    main()