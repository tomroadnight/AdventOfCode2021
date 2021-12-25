import typing

from lib.importer import read_file


def board_num_index(ball: int, board: typing.List[typing.List[int]]) -> typing.Optional[typing.Tuple[int, int]]:
    for row_num, row in enumerate(board):
        if ball in row:
            return (row_num, row.index(ball))


def part_a_b() -> typing.Tuple[int, int]:
    board_size = 5
    lines = read_file('day4', line_filter_cb=bool)
    balls = list(map(int, lines[0].split(',')))
    boards = [[list(map(int, y.split())) for y in lines[(1+x):(1+board_size+x)]] for x in range(0, len(lines)-1, board_size)]

    board_completion_summary = []

    for ball in balls:
        boards_to_pop = []
        for board_idx, board in enumerate(boards):
            if idx := board_num_index(ball, board):
                board[idx[0]][idx[1]] = -1
                if (sum(board[idx[0]]) == -board_size) or (sum(x[idx[1]] for x in board) == -board_size):
                    board_completion_summary.append(sum(max(y, 0) for x in board for y in x) * ball)
                    boards_to_pop.append(board_idx)
        if not (len(boards) - len(boards_to_pop)):
            return board_completion_summary[0], board_completion_summary[-1]
        for b_idx, to_pop in enumerate(boards_to_pop):
            boards.pop(to_pop - b_idx)                    
    

if __name__ == '__main__':
    print(part_a_b())
