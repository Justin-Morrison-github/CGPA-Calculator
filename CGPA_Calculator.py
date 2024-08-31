import csv

from Course import Course, Semester
from CourseList import CourseList
from Terminal import move_cursor_up, move_cursor_down, clear_line, clear_previous_line_back, clear_previous_lines, print_sleep


def main():
    filename = "courses.csv"
    course_list = load_courses(filename)

    filter_preference = get_filtering_preference()

    if filter_preference == "year":
        year = get_year()
        clear_previous_lines(1)

        print(f"{year} Classes:")
        filtered_courses = course_list.filter_by_year(year)

    elif filter_preference == "semester":
        semester = get_semester()
        clear_previous_lines(1)

        print(f"{semester.title()} Classes:")
        filtered_courses = course_list.filter_by_semester(semester)

    elif filter_preference == "both":
        semester = get_semester()
        year = get_year(semester)
        clear_previous_lines(2)

        print(f"{semester.title()} {year} Classes:")
        filtered_courses = course_list.filter_by_year_and_semester(year, semester)

    elif filter_preference == "all":
        filtered_courses = course_list

    print(f"\n{filtered_courses.headers}\n")
    print(f"{filtered_courses}")

    calc_cgpa(filtered_courses, check_major=True)


def get_filtering_preference() -> str:

    options = {
        "1": "year",
        "2": "semester",
        "3": "both",
        "4": "all"
    }

    print("\nHow would you like to filter your courses?")
    print("1. View all courses from a single year")
    print("2. View all semesters of a certain type across different years")
    print("3. View courses from a single semester in a single year")
    print("4. View all classes")
    choice = input("\nEnter 1, 2, 3, or 4: ").strip()

    while choice not in ["1", "2", "3", "4"]:
        if choice in ['q', 'Q']:
            raise SystemExit("Program terminated by user.")
        else:
            move_cursor_up()
            clear_line()
            choice = input("Enter 1, 2, 3, or 4: ").strip()

    clear_previous_lines(7)

    return options[choice]


def get_semester() -> str:
    """
    Prompts user to enter semester. Only accepts 'fall' or 'winter'

    :return: The semester returned as a string
    """
    semester = input("Enter Semester:  ").title()

    while semester not in Course.valid_semesters:
        if semester == 'Q':
            raise SystemExit("Program terminated by user.")
        else:
            move_cursor_up()
            clear_line()
            move_cursor_up()
            print(f"Please enter \'{Semester.FALL}\' or \'{Semester.WINTER} or \'{Semester.SUMMER}\'")

            semester = input("Enter Semester:  ").title()

    clear_previous_line_back(2)
    return semester


def get_year(semester: str = None) -> int:
    """
    Prompts user to enter a valid year for the given semester

    :param semester: The name of the semester ('fall' or 'winter')
    :return: The valid year entered as an integer
    """
    year = input("Enter Year:      ")

    valid_years = ["2023", "2024", "2025", "2026", "2027", "2028"]

    if semester:
        while year not in Course.valid_semesters[semester]:
            if year in ['q', "Q"]:
                raise SystemExit("Program terminated by user.")
            else:
                move_cursor_up()
                clear_line()
                move_cursor_up(2)

                print(f"Please enter any of the following: {Course.valid_semesters[semester]}")
                move_cursor_down()

                year = input("Enter Year:      ")

        clear_previous_line_back(3)
    else:
        while year not in valid_years:
            if year in ['q', "Q"]:
                raise SystemExit("Program terminated by user.")
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
    print_delay = 0.3

    if courses.total_credits != 0:
        print_sleep(f"Credits Earned: {courses.total_credits}", print_delay)

        cgpa = courses.total_grade_points_earned/courses.total_credits
        print_sleep(f"CGPA: {cgpa:.2f}\n", print_delay)
    else:
        print("0 Credits Earned. Cannot Calculate CGPA")

    if check_major:
        if courses.major_credits != 0:
            print_sleep(f"Major Credits Earned: {courses.major_credits}", print_delay)

            major_cgpa = courses.major_grade_points_earned/courses.major_credits
            print_sleep(f"Major CGPA: {major_cgpa:.2f}\n", print_delay)
        else:
            print("0 Major Credits Earned. Cannot Calculate Major CGPA")


if __name__ == "__main__":
    main()
