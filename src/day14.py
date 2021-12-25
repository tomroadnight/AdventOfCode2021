import typing

from collections import Counter, defaultdict

from lib.importer import read_file

    
def part_a_b_brute_force() -> typing.Tuple[int, int]:
    # Brute force approach not sustainable for larger counts therefore an alternate approach was developed under part_a_b.
    lines = dict(read_file('day14', line_cb=lambda x: x.split(' -> '), line_filter_cb=lambda x: bool(x) and len(x) > 1))
    polymer_template = read_file('day14', line_filter_cb=lambda x: bool(x) and len(x) == 1)[0]

    for cnt in range(40):
        polymer_template = ''.join((polymer_template[x] + lines[polymer_template[x] + polymer_template[x+1]] for x in range(len(polymer_template) - 1))) + polymer_template[len(polymer_template) - 1]
        if cnt == 9:
            iter_10_polymer_template = polymer_template

    iter_10_counter, iter_40_counter = Counter(iter_10_polymer_template), Counter(polymer_template)

    return max(iter_10_counter.values()) - min(iter_10_counter.values()), max(iter_40_counter.values()) - min(iter_40_counter.values())
    

def part_a_b() -> typing.Tuple[int, int]:
    lines = dict(read_file('day14', line_cb=lambda x: x.split(' -> '), line_filter_cb=lambda x: bool(x) and len(x) > 1))
    polymer_template = read_file('day14', line_filter_cb=lambda x: bool(x) and len(x) == 1)[0]
    char_counter = Counter(polymer_template)
    polymer_template = defaultdict(int, {polymer_template[y] + polymer_template[y+1]: 1 for y in range(len(polymer_template) - 1)})
    
    for cnt in range(40):
        for (a, b), freq in list(polymer_template.items()):
            insert_char = lines[a + b]
            char_counter[insert_char] += freq
            polymer_template[a + b] -= freq
            polymer_template[a + insert_char] += freq
            polymer_template[insert_char + b] += freq
        if cnt == 9:
            iter_10_char_count = max(char_counter.values()) - min(char_counter.values())

    return iter_10_char_count, max(char_counter.values()) - min(char_counter.values())


if __name__ == '__main__':
    print(part_a_b())
