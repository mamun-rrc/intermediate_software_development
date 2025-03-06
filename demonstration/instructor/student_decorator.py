from patterns.decorator.student_decoratable import StudentDecoratable
class StudentDecorator(StudentDecoratable):
    """
    Student Decorator.
    Implements abstract superclass method.
    Methods:
        __init__: Defines the student to which decorator(s)
        may be applied.
        grade_point_average: Returns the grade_point_average.
    """
    def __init__(self, student: StudentDecoratable):
        """
        Identify the student to which decorations may apply.
        Args:
            student: StudentDecoratable.
        """
        self.__student = student

    @property
    def grade_point_average(self) -> float:
        """
        Grade point average accessor.
        Returns:
            float:  The grade point average belonging to the student.
        """
        return self.__student.grade_point_average
    
