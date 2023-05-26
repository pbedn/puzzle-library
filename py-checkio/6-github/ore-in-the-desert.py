from functools import reduce


def my_checkio(previous):
    if not previous:
        return 0, 0

    def dist(x, y):
        return round(((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5)

    def func(px, py, D):
        return [
            (j, i) for i in range(10) for j in range(10) if dist((px, py), (j, i)) == D
        ]

    res = reduce(lambda a, b: a.intersection(b), [set(func(*x)) for x in previous])
    return res.pop()


"""
Line 9 can be improved in two ways: math.hypot instead of manual calculation, and round instead of int(…+0.5).

Double for in line 12 can be written using itertools.product. But not essential.

Line 5 is not pythonic. “if not data” (or even better: if data, and reversing branches) is much better.

First parameter of reduce is probably nicer written as set.intersection. That way, you don’t need to convert other elements with set, only the first one.

Speaking of which, why do you return list from candidates, just to convert it to set where it matters? Python has set comprehensions, just replace [] with {} in line 9.

And yeah, second argument on line 14 could really use itertools.starmap.

HTH,
"""
from math import hypot


def checkio(previous):
    """my_checkio_improved"""
    if not previous:
        return 0, 0

    def func(x, y, D):
        return {
            (i, j)
            for i in range(10)
            for j in range(10)
            if round(hypot(x - i, y - j)) == D
        }

    res = reduce(lambda a, b: a.intersection(b), [func(*x) for x in previous])
    return res.pop()


def checkio(previous):
    """my_checkio_improved - even better"""
    if not previous:
        return 0, 0

    def func(x, y, D):
        return {
            (i, j)
            for i in range(10)
            for j in range(10)
            if round(hypot(x - i, y - j)) == D
        }

    res = reduce(lambda a, b: a.intersection(b), [func(*x) for x in previous])
    return res.pop()


# - CLEAR 1 ---------------------------------
from math import hypot

cells = [[i, j] for i in range(10) for j in range(10)]


def checkio22(data):
    global cells
    for x, y, d in data[-1:]:
        cells = [[i, j] for i, j in cells if round(hypot(x - i, y - j), 0) == d]
    return cells[0]


# ---- clear random
import math
from functools import reduce


def intdist(f, t):
    h = f[0] - t[0]
    w = f[1] - t[1]
    return int(math.sqrt(h**2 + w**2) + 0.5)


def candidates(py, px, r):
    return [
        (y, x) for x in range(10) for y in range(10) if intdist((py, px), (y, x)) == r
    ]


def checkio4324(data):
    if len(data) == 0:
        return [0, 0]
    cs = reduce(lambda a, b: a & b, [set(candidates(*x)) for x in data])
    return cs.pop()


# ------- clear 3
from math import hypot

COOR = {(x, y) for x in range(10) for y in range(10)}


def checkio2123(prev):
    target = COOR
    for x, y, d in prev:
        target &= {(u, v) for u, v in COOR if round(hypot(x - u, y - v)) == d}
    return sorted(target)[0]


if __name__ == "__main__":
    # This part is using only for self-testing.
    def check_solution(func, ore):
        recent_data = []
        for step in range(4):
            row, col = func([d[:] for d in recent_data])  # copy the list
            if row < 0 or row > 9 or col < 0 or col > 9:
                print("Where is our probe?")
                return False
            if (row, col) == ore:
                return True
            dist = round(((row - ore[0]) ** 2 + (col - ore[1]) ** 2) ** 0.5)
            recent_data.append([row, col, dist])
        print("It was the last probe.")
        return False

    assert check_solution(checkio, (1, 1)), "Example"
    print("-----------------------------------------")
    assert check_solution(checkio, (9, 9)), "Bottom right"
    print("-----------------------------------------")
    assert check_solution(checkio, (6, 6)), "Center"

"""
During their adventure, the Robo-trio came across a desert, and the ships sensors have registered ore in the region. The desert has a size of 10x10 cells and can be represented as a 2D array. The ship has four probes which can be used to help us find the ore. At each step you will need to return the coordinates of a cell (as [row, column]) for the probe to travel to. If the cell contains ore, then you can finish; else the probe will give a distance to the location of the ore cell (it will be the Euclidean distance between cells' centers). The perception of probe is not very good and it will give you a result rounded to the closest integer (1.41 ≈ 1; 2.83 ≈ 3). At each step you receive information from the previous probes as a list of list. Each list will be in the following format: [row, column, distance]. At the beginning of the mission, you will only receive an empty list.

Input: Information of the previous probes as a list of lists. Each list contains three integers.

Output: The coordinate of the next probe as a list of two integers.

Precondition: 
len(desert) == 10
all(len(row) == 10 for row in desert)
There is always exist an ore cell in the desert.
"""
