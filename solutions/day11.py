def parse_input(raw_input: str, is_test_input: bool):
    input = {}
    for line in raw_input.split('\n'):
        if line == '': continue
        source, sinks = line.split(': ')
        sinks = sinks.split(' ')
        input[source] = sinks
    return input


def count_paths(start, goal, graph, cache):
    if start in cache:       return cache[start]
    if start not in graph:   return 0
    if goal in graph[start]: return 1

    result = sum(count_paths(node, goal, graph, cache) for node in graph[start])
    cache[start] = result
    return result


def part1(input):
    return count_paths('you', 'out', input, {})


def part2(input):
    # We could do some cache sharing, but this is fast enough
    # on my machine, that I don't care to clutter up the code
    return (
        count_paths('svr', 'fft', input, {}) *
        count_paths('fft', 'dac', input, {}) *
        count_paths('dac', 'out', input, {})
        +
        count_paths('svr', 'dac', input, {}) *
        count_paths('dac', 'fft', input, {}) *
        count_paths('fft', 'out', input, {})
    )