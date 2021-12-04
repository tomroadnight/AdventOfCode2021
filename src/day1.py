from lib.importer import read_file


def part_a() -> int:
    lines = read_file('day1', line_cb=lambda x: int(x))
    return sum([x > y for x, y in zip(lines[1:], lines[:-1])])


def part_b() -> int:
    lines = read_file('day1', line_cb=lambda x: int(x))
    lines = [sum(lines[i:i+3]) for i in range(len(lines) - 2)]
    return sum([x > y for x, y in zip(lines[1:], lines[:-1])])


if __name__ == '__main__':
    print(part_a())
    print(part_b())
