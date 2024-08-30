class Semester():
    FALL = "Fall"
    WINTER = "Winter"
    SUMMER = "Summer"


class Course():
    grades = {
        "A+": 12.0,
        "A": 11.0,
        "A-": 10.0,
        "B+": 9.0,
        "B": 8.0,
        "B-": 7.0,
        "C+": 6.0,
        "C": 5.0,
        "C-": 4.0,
        "D+": 3.0,
        "D": 2.0,
        "D-": 1.0,
        "F": 0.0,
        "SAT": 0.0
    }

    valid_semesters = {
        Semester.FALL: ["2023"],
        Semester.WINTER: ["2024"],
        Semester.SUMMER: []
    }

    def __init__(self, course_dict: dict):
        self.name = course_dict['Course Title']
        self.subject = course_dict['Subject']
        self.section = course_dict['Section']

        self.year = int(course_dict['Year'])
        self.CRN = int(course_dict['CRN'])
        self.course_number = int(course_dict['Course Number'])

        self.credit = float(course_dict['Credit'])
        self.CGPA_points = float(course_dict['CGPA Points'])

        if course_dict['Semester'] in Course.valid_semesters:
            self.semester = course_dict['Semester']
        else:
            raise ValueError(f"Invalid semester: {course_dict['Semester']}")

        if course_dict["Final Grade"] in Course.grades:
            self.grade = course_dict['Final Grade']
        else:
            raise ValueError(f"Invalid grade: {course_dict['Final Grade']}")

        self.in_major = course_dict["Major"].strip().lower() in ['true', '1', 'yes']

    def __repr__(self) -> str:
        return f"""{
            self.grade: <8} {
            self.credit: <5.2f} {
            'Credits': <10} {
            self.semester: <7} {
            self.year: <7} {
            self.name: <30}"""
