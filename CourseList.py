class CourseList:
    def __init__(self, list: list = None):
        if list:
            self.courses = list
        else:
            self.courses = []

    def append(self, course):
        self.courses.append(course)

    def __iter__(self):
        return iter(self.courses)

    @property
    def names(self):
        """
        Returns a list of course names.
        """
        return [course.name for course in self.courses]

    @property
    def subjects(self):
        """
        Returns a list of course names.
        """
        return [course.subject for course in self.courses]

    @property
    def sections(self):
        """
        Returns a list of course names.
        """
        return [course.section for course in self.courses]

    @property
    def years(self):
        """
        Returns a list of course names.
        """
        return [course.year for course in self.courses]

    @property
    def CRNs(self):
        """
        Returns a list of course names.
        """
        return [course.CRN for course in self.courses]

    @property
    def course_numbers(self):
        """
        Returns a list of course names.
        """
        return [course.course_number for course in self.courses]

    @property
    def credits(self):
        """
        Returns a list of course names.
        """
        return [course.credit for course in self.courses]

    @property
    def CGPA_points(self):
        """
        Returns a list of course names.
        """
        return [course.CGPA_points for course in self.courses]

    @property
    def semesters(self):
        """
        Returns a list of course names.
        """
        return [course.semester for course in self.courses]

    @property
    def grades(self):
        """
        Returns a list of course grades.
        """
        return [course.grade for course in self.courses]
    
    @property
    def in_major(self):
        """
        Returns a list of course names.
        """
        return [course.in_major for course in self.courses]

    @property
    def headers(self):
        columns = [
            ("Grade", 9),
            ("Credits", 17),
            ("Term", 8),
            ("Year", 8),
            ("Class", 31),
            ("In Major", 11)
        ]

        header_string = "".join([f"{title:<{width}}" for title, width in columns])
        return header_string

    def __repr__(self) -> str:
        return "\n".join(
            f"{course.grade:<8} {course.credit:<5.2f} {'Credits':<10} "
            f"{course.semester:<7} {course.year:<7} {course.name:<30} "
            f"{'Yes' if course.in_major else 'No'}"
            for course in self.courses
        )

    def filter_by_year(self, year: int):
        """
        Filters courses by the specified year.
        """
        return CourseList([course for course in self.courses if course.year == year])

    def filter_by_semester(self, semester):
        """
        Filters courses by the specified semester.
        """
        return CourseList([course for course in self.courses if course.semester == semester])

    def filter_by_year_and_semester(self, year: int, semester):
        """
        Filters courses by the specified year and semester.

        :param year: Integer of wanted year
        :param semester: String of wanted semester ('fall' or 'winter')
        :return: CourseList object containing courses that took place in that year and semester
        """
        return CourseList([course for course in self.courses if course.year == year and course.semester == semester])

    @property
    def total_credits(self):
        """
        Calculates the total credits of all courses.
        """
        return sum(course.credit for course in self.courses)

    @property
    def major_credits(self):
        """
        Calculates the total credits of all courses.
        """
        return sum(course.credit for course in self.courses if course.in_major)

    @property
    def total_grade_points_earned(self):
        """
        Calculates the total credits of all courses.
        """
        return sum(course.CGPA_points for course in self.courses)

    @property
    def major_grade_points_earned(self):
        """
        Calculates the total credits of all courses.
        """
        return sum(course.CGPA_points for course in self.courses if course.in_major)

    def calculate_CGPA(self):
        return self.total_grade_points_earned / self.total_credits

    def calculate_major_CGPA(self):
        return self.major_grade_points_earned / self.major_credits
