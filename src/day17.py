import math, typing
from lib.importer import read_file

def part_a_b() -> typing.Tuple[int, int]:
    (x_min, x_max), (y_min, y_max) = read_file('day17', line_cb=lambda x: map(lambda y: (int(x) for x in y.replace(',', '').replace('x=', '').replace('y=', '').split('..')), x.split(' ')[2:]))[0]
    
    max_height, target_hits = 0, 0

    for velo_x_init in range(0, x_max + 1):
        for velo_y_init in range(-abs(y_min), abs(y_min) + 1):
            curr_x, curr_y, curr_height, curr_vel_x, curr_vel_y = 0, 0, -abs(y_min), velo_x_init, velo_y_init
            for _ in range(x_max * abs(y_min)):
                if curr_x <= x_max and curr_x >= x_min and curr_y >= y_min and curr_y <= y_max:
                    max_height = max(max_height, curr_height)
                    target_hits += 1
                    break

                curr_y += curr_vel_y
                curr_x += curr_vel_x
                curr_height = max(curr_height, curr_y)

                curr_vel_x += 1 if curr_vel_x < 0 else -1 if curr_vel_x > 0 else 0
                curr_vel_y -= 1

                if curr_y < y_min or curr_x > x_max:
                    break

    return max_height, target_hits


if __name__ == '__main__':
    print(part_a_b())
