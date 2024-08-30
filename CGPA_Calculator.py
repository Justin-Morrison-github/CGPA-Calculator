import csv
from Course import Course, Semester
from CourseList import CourseList
from Terminal import move_cursor_up, move_cursor_down, clear_line, clear_previous_line


def main():
    filename = "courses.csv"
    course_list = load_courses(filename)

    filter_preference = get_filtering_preference()

    if filter_preference == "both":
        semester = get_semester()
        year = get_year(semester)
        filtered_courses = course_list.filter_by_year_and_semester(year, semester)

    elif filter_preference == "year":
        year = get_year(None)
        filtered_courses = course_list.filter_by_year(year)

    elif filter_preference == "semester":
        semester = get_semester()
        filtered_courses = course_list.filter_by_semester(semester)

    elif filter_preference == "all":
        filtered_courses = course_list

    print(filtered_courses.headers)
    print(f"\n{filtered_courses}")

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
    choice = input("Enter 1, 2, 3, or 4: ").strip()

    while choice not in ["1", "2", "3", "4"]:
        move_cursor_up()
        clear_line()
        move_cursor_up()
        print("Please enter 1, 2, 3, 4.")
        choice = input("Enter 1, 2, 3, or 4: ").strip()

    clear_previous_line(2)

    return options[choice]


def get_semester() -> str:
    """
    Prompts user to enter semester. Only accepts 'fall' or 'winter'

    :return: The semester returned as a string
    """
    semester = input("\nEnter Semester:  ").title()

    while semester not in Course.valid_semesters:
        if semester == 'Q':
            raise SystemExit("Program terminated by user.")
        else:
            move_cursor_up()
            clear_line()
            move_cursor_up()
            print(f"Please enter \'{Semester.FALL}\' or \'{Semester.WINTER} or \'{Semester.SUMMER}\'")

            semester = input("Enter Semester:  ").title()

    clear_previous_line(2)
    return semester


def get_year(semester: str) -> int:
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
    else:
        while year not in valid_years:
            if year in ['q', "Q"]:
                raise SystemExit("Program terminated by user.")
            else:
                move_cursor_up()
                clear_line()
                move_cursor_up(2)

                print(f'Please enter any of the following: {valid_years}')
                move_cursor_down()

                year = input("Enter Year:      ")

    clear_previous_line(3)

    return int(year)


def load_courses(filename: str) -> CourseList:
    """
    Loads courses from a CSV file and returns a CourseList object.

    :param filename: The path to the CSV file containing the course data.
    :return: A CourseList object containing the courses from the file.
    """
    course_list = CourseList()
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for course_row in csv_reader:
                course = Course(course_row)
                course_list.append(course)
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

    if courses.total_credits != 0:
        print(f"\nCredits Earned: {courses.total_credits}")

        cgpa = courses.total_grade_points_earned/courses.total_credits
        print(f"CGPA: {cgpa:.2f}\n")
    else:
        print("0 Credits Earned. Cannot Calculate CGPA")

    if check_major:
        if courses.major_credits != 0:
            print(f"Major Credits Earned: {courses.major_credits}")

            major_cgpa = courses.major_grade_points_earned/courses.major_credits
            print(f"Major CGPA: {major_cgpa:.2f}\n")
        else:
            print("0 Major Credits Earned. Cannot Calculate Major CGPA")


if __name__ == "__main__":
    main()
