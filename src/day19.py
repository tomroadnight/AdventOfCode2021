import typing

from collections import defaultdict
from itertools import permutations

from lib.importer import read_file


def grid_transformations(a: typing.List[typing.Tuple[int, int, int]], b_orig: typing.List[typing.Tuple[int, int, int]]) -> typing.Tuple[bool, typing.Optional[typing.List[typing.Tuple[int,int, int]]], typing.Optional[typing.Tuple[int,int, int]]]:
    for axis, flip in ((axis, flip) for axis in permutations((0, 1, 2)) for flip in ((-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1), (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1))):
        b = [(_b[axis[0]] * flip[0], _b[axis[1]] * flip[1], _b[axis[2]] * flip[2]) for _b in b_orig]
        for pos_a in a:
            for pos_b in b:
                delta = (pos_b[0] - pos_a[0], pos_b[1]-pos_a[1], pos_b[2]-pos_a[2])

                succ_maps = [(pos_revert_b[0] - delta[0], pos_revert_b[1] - delta[1], pos_revert_b[2] - delta[2]) for pos_revert_b in b]

                if sum([x in a for x in succ_maps]) >= 12:
                    return True, succ_maps, delta
                    
    return False, None, None
    

def part_a_b() -> typing.Tuple[int, int]:
    lines = read_file('day19', line_cb=lambda x: int(''.join(filter(str.isdigit, x))) if 'scanner' in x else tuple(map(int, x.split(','))), line_filter_cb=bool)

    grids, curr_scanner = defaultdict(list), 0
    for l in lines:
        if isinstance(l, int):
            curr_scanner = l
        else:
            grids[curr_scanner].append(l)

    scanner_pos = {
        0: grids[0]
    }

    beacons, origin_dists, max_dist, seen = set(grids[0]), [(0, 0, 0)], 0, set()

    while len(scanner_pos) < len(grids):
        for k, v in grids.items():
            if k not in scanner_pos:
                for k1, v1 in tuple(scanner_pos.items()):
                    if (k, k1) not in seen or (k1, k) not in seen:
                        seen.add((k, k1))
                        aligned, succ_maps, delta = grid_transformations(v1, v)
                        if aligned:
                            scanner_pos[k] = succ_maps
                            beacons.update(succ_maps)
                            max_dist = max(max_dist, max([abs(delta[0]-a[0]) + abs(delta[1]-a[1]) + abs(delta[2]-a[2]) for a in origin_dists]))
                            origin_dists.append(delta)
                            break

    return len(beacons), max_dist


if __name__ == '__main__':
    print(part_a_b())
