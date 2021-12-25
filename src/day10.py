import typing

from functools import reduce
from statistics import median

from lib.importer import read_file

CLOSURE_POINTS= {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

CHAR_RELATION = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day10')
    corrupt, autocomplete = 0, list()

    for l in lines:
        stack = list()
        for char in l:
            if char_points := CLOSURE_POINTS.get(char):
                if (stack.pop() != CHAR_RELATION[char]):
                    corrupt += char_points
                    stack.clear()
                    break
            else:
                stack.append(char)
        if stack:
            autocomplete.append(reduce(lambda acc, x: acc * 5 + (list(CHAR_RELATION.values()).index(x) + 1), reversed(stack), 0))

    return corrupt, median(autocomplete)


if __name__ == '__main__':
    print(part_a_b())
