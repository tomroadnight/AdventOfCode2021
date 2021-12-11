
import typing
from itertools import count
from lib.importer import read_file
    

def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day11', line_cb=lambda x: list(map(int, x)))
    total_flashes = 0
    grid = {(x, y): val for y in range(len(lines)) for x, val in enumerate(lines[y])}

    for c in count(1):
        for elem in grid:
            grid[elem] += 1
        flashed = []
        ready_to_flash = [k for k, v in grid.items() if v > 9]

        while ready_to_flash:
            for x, y in ready_to_flash:
                grid[(x, y)] = 0
                adjs = set(grid.keys()).intersection(set((x + x1, y + y1) for x1, y1 in ((1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)) if (x + x1, y + y1) not in flashed + ready_to_flash))
                for adj in adjs:
                    grid[adj] += 1
            flashed += ready_to_flash
            ready_to_flash = [k for k, v in grid.items() if v > 9 and k not in flashed]
        
        if c < 101:
            total_flashes += len(flashed)
        if len(flashed) == len(grid):
            return total_flashes, c
        

if __name__ == '__main__':
    print(part_a_b())
