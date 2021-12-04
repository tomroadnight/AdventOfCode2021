import typing
from lib.importer import read_file

def board_num_index(ball: int, board: typing.List[typing.List[int]]) -> typing.Optional[typing.Tuple[int, int]]:
    for row_num, row in enumerate(board):
        if ball in row:
            return (row_num, row.index(ball))


def part_a() -> int:
    board_size = 5
    lines = read_file('day4', line_filter_cb=lambda x: x)
    balls = list(map(int, lines[0].split(',')))
    boards = [[list(map(int, y.split())) for y in lines[(1+x):(1+board_size+x)]] for x in range(0, len(lines)-1, 5)]

    for ball in balls:
        for board in boards:
            if idx := board_num_index(ball, board):
                board[idx[0]][idx[1]] = -1
                if (sum(board[idx[0]]) == -5) or (sum(x[idx[1]] for x in board) == -5):
                    return sum(max(y, 0) for x in board for y in x) * ball


def part_b() -> int:
    board_size = 5
    lines = read_file('day4', line_filter_cb=lambda x: x)
    balls = list(map(int, lines[0].split(',')))
    boards = [[list(map(int, y.split())) for y in lines[(1+x):(1+board_size+x)]] for x in range(0, len(lines)-1, 5)]

    for ball in balls:
        boards_to_pop = []
        for board_idx, board in enumerate(boards):
            if idx := board_num_index(ball, board):
                board[idx[0]][idx[1]] = -1
                if len(boards) == 1 and board_idx == 0:
                    return sum(max(y, 0) for x in board for y in x) * ball
                if (sum(board[idx[0]]) == -5) or (sum(x[idx[1]] for x in board) == -5):
                    boards_to_pop.append(board_idx)
        for b_idx, to_pop in enumerate(boards_to_pop):
            boards.pop(to_pop - b_idx)
                    
    

if __name__ == '__main__':
    print(part_a())
    print(part_b())
