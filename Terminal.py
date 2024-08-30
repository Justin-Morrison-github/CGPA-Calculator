import sys


def move_cursor_down(lines_down: int = 1):
    for _ in range(lines_down):
        sys.stdout.write("\033[E")  # down to next line


def move_cursor_up(lines_up: int = 1):
    for _ in range(lines_up):
        sys.stdout.write("\033[F")  # back to previous line


def clear_line(lines_cleared: int = 1):
    for _ in range(lines_cleared):
        sys.stdout.write("\033[K")  # clear line


def clear_previous_line(lines_back: int):
    for _ in range(lines_back):
        sys.stdout.write("\033[F")  # back to previous line

    sys.stdout.write("\033[K")  # clear line

    for _ in range(lines_back):
        sys.stdout.write("\033[E")  # down to next line
