import csv
from colorama import Fore

from Course import Course, Term
from CourseList import CourseList
from Terminal import move_cursor_up, move_cursor_down, clear_line, clear_previous_line_back, clear_previous_lines, print_sleep
from string_print import str_color


def main():
    filename = "courses.csv"
    course_list = load_courses(filename)

    filter_preference = get_filtering_preference()

    if filter_preference == "year":
        year = get_year()
        clear_previous_lines(1)

        print(f"{year} Classes:")
        filtered_courses = course_list.filter_by_year(year)

    elif filter_preference == "term":
        term = get_term()
        clear_previous_lines(1)

        print(f"{term.title()} Classes:")
        filtered_courses = course_list.filter_by_term(term)

    elif filter_preference == "both":
        term = get_term()
        year = get_year(term)
        clear_previous_lines(2)

        print(f"{term.title()} {year} Classes:")
        filtered_courses = course_list.filter_by_year_and_term(year, term)

    elif filter_preference == "all":
        print_sleep("All Classes:", 0.3)
        filtered_courses = course_list

    print(f"\n{filtered_courses.headers}")
    print(f"{filtered_courses}")

    calc_cgpa(filtered_courses, check_major=True)


def get_filtering_preference() -> str:

    options = {
        "1": "year",
        "2": "term",
        "3": "both",
        "4": "all"
    }

    print("\nHow would you like to filter your courses?")
    print("1. View all courses from a single year")
    print("2. View all terms of a certain type across different years")
    print("3. View courses from a single term in a single year")
    print("4. View all classes")
    choice = input("\nEnter 1, 2, 3, or 4: ").strip()

    while choice not in ["1", "2", "3", "4"]:
        if choice in ['q', 'Q']:
            raise SystemExit(str_color("Program terminated by user.", Fore.RED))
        else:
            move_cursor_up()
            clear_line()
            choice = input("Enter 1, 2, 3, or 4: ").strip()

    clear_previous_lines(7)

    return options[choice]


def get_term() -> str:
    """
    Prompts user to enter term. Only accepts 'fall' or 'winter'

    :return: The term returned as a string
    """
    term = input("Enter Term:  ").title()

    while term not in Course.valid_terms:
        if term == 'Q':
            raise SystemExit(str_color("Program terminated by user.", Fore.RED))
        else:
            move_cursor_up()
            clear_line()
            move_cursor_up()
            print(str_color(f"Please enter \'{Term.FALL}\' or \'{Term.WINTER} or \'{Term.SUMMER}\'", Fore.YELLOW))

            term = input("Enter Term:  ").title()

    clear_previous_line_back(2)
    return term


def get_year(term: str = None) -> int:
    """
    Prompts user to enter a valid year for the given term

    :param term: The name of the term ('fall' or 'winter')
    :return: The valid year entered as an integer
    """
    year = input("Enter Year:  ")

    valid_years = ["2023", "2024", "2025", "2026", "2027", "2028"]

    if term:
        while year not in Course.valid_terms[term]:
            if year in ['q', "Q"]:
                raise SystemExit(str_color("Program terminated by user.", Fore.RED))
            else:
                move_cursor_up()
                clear_line()
                move_cursor_up(2)

                print(str_color(f"Please enter any of the following: {Course.valid_terms[term]}", Fore.YELLOW))
                move_cursor_down()

                year = input("Enter Year:  ")

        clear_previous_line_back(3)
    else:
        while year not in valid_years:
            if year in ['q', "Q"]:
                raise SystemExit(str_color("Program terminated by user.", Fore.RED))
            else:
                move_cursor_up()
                clear_line()
                move_cursor_up()

                print(f'Please enter any of the following: {valid_years}')
                year = input("Enter Year:      ")

        clear_previous_line_back(2)

    return int(year)


def load_courses(filename: str) -> CourseList:
    """
    Loads courses from a CSV file and returns a CourseList object.

    :param filename: The path to the CSV file containing the course data.
    :return: A CourseList object containing the courses from the file.
    """
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            course_list = CourseList([Course(course_row) for course_row in csv_reader])

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return course_list


def calc_cgpa(courses: CourseList, check_major: bool = False) -> None:
    """
    Calculates the CGPA and optionally the major specific CGPA

    :param courses: CourseList object containing courses to have calculated
    :param check_major: Boolean whether to include major specific CGPA or not
    """
    print_delay = 0.4

    if courses.total_credits != 0:
        print(f"{str_color('Credits Earned:', Fore.CYAN)} {str_color(courses.total_credits, Fore.GREEN)}")

        cgpa = courses.total_grade_points_earned/courses.total_credits
        print_sleep(str_color("CGPA: ", Fore.CYAN) + str_color(f"{cgpa:.2f}\n", Fore.GREEN), print_delay)
    else:
        print("0 Credits Earned. Cannot Calculate CGPA")

    if check_major:
        if courses.major_credits != 0:
            print(f"{str_color('Major Credits Earned:', Fore.CYAN)} {str_color(courses.major_credits, Fore.GREEN)}")

            major_cgpa = courses.major_grade_points_earned/courses.major_credits
            print_sleep(
                str_color("Major CGPA: ", Fore.CYAN) + str_color(f"{major_cgpa:.2f}\n", Fore.GREEN),
                print_delay)
        else:
            print("0 Major Credits Earned. Cannot Calculate Major CGPA")


if __name__ == "__main__":
    main()
