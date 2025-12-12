from queue import Queue
from sympy import Matrix, floor, ceiling
from itertools import product

def parse_input(raw_input: str, is_test_input: bool):
    input = []
    for line in raw_input.split('\n'):
        if line == '': continue
        pieces = line.split(' ')
        lights = list(map(lambda c: True if c == '#' else False, pieces[0][1:-1]))
        buttons = [tuple(map(int, piece[1:-1].split(','))) for piece in pieces[1:-1]]
        joltage = list(map(int, pieces[-1][1:-1].split(',')))
        input.append((lights, buttons, joltage))
    return input


def part1(input):
    return sum(get_min_pushes_lights(lights, buttons) for lights, buttons, _ in input)


def part2(input):
    return sum(get_min_pushes_joltage(joltage, buttons) for i, (_, buttons, joltage) in enumerate(input))


def get_min_pushes_lights(lights_goal, buttons):
    # We can BFS until we find a solution
    q = Queue()
    q.put((0, [0]*len(lights_goal)))
    while not q.empty():
        depth, old_lights = q.get()
        for button in buttons:
            lights = old_lights[:]
            for light in button:
                lights[light] = not lights[light]
            if lights == lights_goal:
                return depth+1
            q.put((depth+1, lights))


def get_push_bounds(inequalities):
    # Each element of `inequalities` is a list of rationals of the form [a_1, a_2, ..., a_n, c],
    # which implies that a_1*x_1 + a_2*x_2 + .... + a_n*x_n <= c, for non-negative integers x_i.
    # This function iterates over these inequalities to find tighter bounds for the x_i.
    # The iteration is repeated until the bounds converge.
    var_count = len(inequalities[0])-1
    bounds = [[0, float('inf')] for i in range(var_count)]
    old_bounds = None
    while old_bounds != bounds:
        old_bounds = bounds
        bounds = [l[:] for l in bounds]
        for ineq in inequalities:
            for i, a_i in enumerate(ineq[:-1]):
                if a_i == 0: continue
                
                bound = ineq[-1]
                for j, a_j in enumerate(ineq[:-1]):
                    if i == j: continue
                    if a_j > 0:
                        # Then a_i*x_i <= c - a_j*x_j <= c - a_j*(lower bound for x_j)
                        bound -= bounds[j][0]*a_j
                    elif a_j < 0: 
                        # Then a_i*x_i <= c - a_j*x_j <= c + (-a_j)*(upper bound for x_j)
                        bound -= bounds[j][1]*a_j

                if a_i < 0:
                    # x_i is bounded below by value/a_i
                    bounds[i][0] = max(bounds[i][0], ceiling(bound/a_i))
                elif a_i > 0:
                    # x_i is bounded above by value/a_i
                    bounds[i][1] = min(bounds[i][1], floor(bound/a_i))
    return bounds


def get_min_pushes_joltage(goal, buttons):
    cols = [[1 if j in buttons[i] else 0 for j in range(len(goal))] for i in range(len(buttons))]
    M, pivots = Matrix(cols).col_join(Matrix([goal])).transpose().rref()
    non_pivots = [i for i in range(len(buttons)) if i not in pivots]

    # We can extract the inequalities from the matrix by choosing the columns corresponding to the non-pivots
    inequalities = M[:, non_pivots + [len(buttons)]]
    bounds = get_push_bounds([inequalities.row(r) for r in range(inequalities.rows)])

    min_sum = float('inf')
    for non_pivot_values in product(*[range(a, b+1) for a,b in bounds]):
        this_sum = sum(non_pivot_values)
        # Calculate the values for the pivots (we only need to use non-pivot values because M is in RREF)
        for r in range(len(pivots)):
            value = M[r, -1] - sum(M[r, n] * non_pivot_values[i] for i, n in enumerate(non_pivots))
            if not value.is_Integer or value < 0: # All values need to be positive integers
                break
            this_sum += value if value.is_Integer and value >= 0 else float('inf')
        else:
            # We didn't break, so this_sum is valid
            min_sum = min(min_sum, this_sum)
    return min_sum
