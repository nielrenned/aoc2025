from queue import Queue
from functools import cache

def parse_input(raw_input: str, is_test_input: bool):
    input = {}
    for line in raw_input.split('\n'):
        if line == '': continue
        source, sinks = line.split(': ')
        sinks = sinks.split(' ')
        input[source] = sinks
    return input


def subgraph_before(v, graph):
    subgraph = {}
    q = Queue()
    q.put(v)
    while not q.empty():
        node = q.get()
        for source, sinks in graph.items():
            if node not in sinks: continue
            if source not in subgraph:
                subgraph[source] = sinks
                q.put(source)
    return subgraph


def count_paths(start, goal, graph):
    subgraph = subgraph_before(goal, graph)
    q = Queue()
    q.put(start)
    count = 0
    while not q.empty():
        node = q.get()
        if node not in subgraph: continue
        for sink in subgraph[node]:
            if sink == goal:
                count += 1
            else:
                q.put(sink)
    return count


def part1(input):
    return count_paths('you', 'out', input)


def part2(input):
    if 'fft' in subgraph_before('dac', input):
        return (
            count_paths('svr', 'fft', input) *
            count_paths('fft', 'dac', input) *
            count_paths('dac', 'out', input)
        )
    else:
        return (
            count_paths('svr', 'dac', input) *
            count_paths('dac', 'fft', input) *
            count_paths('fft', 'out', input)
        )