
import typing
from collections import defaultdict
from lib.importer import read_file
    
def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day12', line_cb=lambda x: x.split('-'))
    caves = defaultdict(list)
    for l, r in lines:
        caves[l] += [r]
        caves[r] += [l]

    def traverse_tree(cave: str, seen: set, routes: int = 0, second_visit: bool = False):
        if cave == 'end':
            return 1
        
        if cave[0].islower():
            seen = seen | set((cave,))

        for next_cave in caves[cave]:
            if next_cave == 'start':
                continue

            if next_cave in seen and not second_visit: 
                routes += traverse_tree(next_cave, seen, second_visit=True)
            elif next_cave not in seen:
                routes += traverse_tree(next_cave, seen, second_visit=second_visit)
        
        return routes

    return traverse_tree('start', set(), second_visit=True), traverse_tree('start', set())


if __name__ == '__main__':
    print(part_a_b())
