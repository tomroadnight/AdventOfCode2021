from typing import Callable

def read_file(file_name: str, line_cb: Callable = None, line_filter_cb: Callable = None) -> list:
    with open(f'src/data/{file_name}.txt') as file:
        lines = file.readlines()
        lines = [line_cb(line.rstrip()) if line_cb else line.rstrip() for line in lines if not line_filter_cb or line_filter_cb(line.rsplit())]
    return lines
