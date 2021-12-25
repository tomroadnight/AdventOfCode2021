from typing import Callable
import typing


def read_file(file_name: str, line_cb: Callable = None, line_filter_cb: Callable = None, post_cb_line_filter: Callable = None) -> typing.List:
    with open(f'src/data/{file_name}.txt') as file:
        lines = file.readlines()
        lines = [line_cb(line.rstrip()) if line_cb else line.rstrip() for line in lines if not line_filter_cb or line_filter_cb(line.rsplit())]
        if post_cb_line_filter:
            lines = list(filter(post_cb_line_filter, lines))
    return lines
