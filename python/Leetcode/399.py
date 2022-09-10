import collections
import itertools


def calcEquation(equations, values, queries):
    quot = collections.defaultdict(dict)
    print(quot)
    for (num, den), val in zip(equations, values):
        quot[num][num] = quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1 / val
        print(quot)
    for k, i, j in itertools.permutations(quot, 3):
        if k in quot[i] and j in quot[k]:
            quot[i][j] = quot[i][k] * quot[k][j]

        print("\n Second:", quot)
    return [quot[num].get(den, -1.0) for num, den in queries]

calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])