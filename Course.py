class Term():
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

    valid_terms = {
        Term.FALL: ["2023"],
        Term.WINTER: ["2024"],
        Term.SUMMER: []
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

        if course_dict['Term'] in Course.valid_terms:
            self.term = course_dict['Term']
        else:
            raise ValueError(f"Invalid term: {course_dict['Term']}")

        if course_dict["Final Grade"] in Course.grades:
            self.grade = course_dict['Final Grade']
        else:
            raise ValueError(f"Invalid grade: {course_dict['Final Grade']}")

        self.in_major = course_dict["Major"].strip().lower() in ['true', '1', 'yes']

    def __repr__(self) -> str:
        return f"""{
            self.grade: <8}{
            self.credit: <10.2f}{
            self.term: <8}{
            self.year: <8}{
            self.name: <30}{
            'Yes' if self.in_major else 'No'}"""
