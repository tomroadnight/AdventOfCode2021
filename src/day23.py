import typing
import sys
from lib.importer import read_file

AMPHIPODS_COST = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

AMPHIPODS_TO_Y_IDX = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9
}

def run(lines: typing.List[str]) -> int:
    grid = {(x, y): lines[y][x] for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] in list(AMPHIPODS_COST) + ['.']}    

    def compute(grid: typing.Dict[typing.Tuple[int, int], str], prior_pos: typing.Dict[str, int] = {}, total: int = 0, _min: int = 0) -> int:
        grid = grid.copy()
        curr_repr = hash(tuple(grid.items()))
        if (_min and total >= _min) or prior_pos.get(curr_repr, sys.maxsize) <= total:
            return _min
        prior_pos[curr_repr] = total

        if all(elem == '.' for elem in grid.values()):
            return min(_min, total) if _min else total
        
        for (x, y), elem in grid.items():
            if elem in AMPHIPODS_COST and grid.get((x, y-1), '.') == '.':
                elem_dest_col, elem_dest_max_row = AMPHIPODS_TO_Y_IDX[elem], max([pnt[1] for pnt in grid.keys() if pnt[0] == AMPHIPODS_TO_Y_IDX[elem]])

                _grid = {(_x, _y): _elem for (_x, _y), _elem in grid.items() if _y == 0 or (y >= _y > 0 and _x == x) or (_x == elem_dest_col and all(grid[(_x, __y)] == '.' for __y in range(1, elem_dest_max_row + 1)))}

                elem_dest_max_pnt = (elem_dest_col, elem_dest_max_row)

                elem_dest = [(_x,0) for _x in range(1, len(lines[0]) - 1) if _x not in AMPHIPODS_TO_Y_IDX.values()] if y > 0 else [elem_dest_max_pnt]

                to_visit, visited, next_steps = [((x, y), total)], list(), list()

                while to_visit:
                    pnt, _total = to_visit.pop(0)
                    for _pnt in ((pnt[0]+1, pnt[1]), (pnt[0]-1, pnt[1]), (pnt[0], pnt[1]+1), (pnt[0], pnt[1]-1)):
                        if _pnt in _grid and _pnt not in visited and _grid[_pnt] == '.':
                            to_visit.extend([(pnt, _total), (_pnt, _total + AMPHIPODS_COST[elem])])
                            visited.append(_pnt)
                    if pnt in elem_dest:
                        next_steps.append((pnt, _total))
                
                for _pnt, _total in next_steps:
                    _grid = grid.copy()
                    _grid[(x, y)] = '.'
                    if _pnt == elem_dest_max_pnt:
                        _grid.pop(_pnt)
                    else:
                        _grid[_pnt] = elem
                    n_min = compute(_grid, prior_pos, _total, _min)
                    _min = min(_min, n_min) if _min else n_min
        return _min

    return compute(grid)


def part_a() -> int:
    return run(read_file('day23a')[1:])


def part_b() -> int:
    return run(read_file('day23b')[1:])


if __name__ == '__main__':
    print(part_a(), part_b())
