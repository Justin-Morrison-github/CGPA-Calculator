from colorama import Fore


def sub_str_color(str: str, substr: str, color: str, start: str = "", end: str = "") -> str:
    valid, str_len, substr_len = sub_str_valid(str, substr)

    if valid:
        num = str.lower().find(substr.lower())

        f_string = f"{start}{str[0: num]}{color}{str[num: num + substr_len]}{Fore.RESET}{str[num + substr_len: str_len]}{end}"
        return f_string
    else:
        return str


def print_sub_str_color(str: str, substr: str, color: str, start: str = "", end: str = "") -> None:
    print(sub_str_color(str, substr, color, start, end))


def sub_str_valid(main_string: str, sub_string: str) -> bool:
    if sub_string == "" or sub_string not in main_string:
        return (False, 0, 0)
    else:
        return (True, len(main_string), len(sub_string))


def str_color(str: str, color: str, start: str = "", end: str = ""):
    return f"{start}{color}{str}{Fore.RESET}{end}"


def print_str_color(str: str, color: str, start: str = "", end: str = ""):
    print(str_color(str, color, start, end))
