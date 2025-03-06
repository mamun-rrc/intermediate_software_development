from patterns.decorator import StudentDecorator

class VolunteerDecorator(StudentDecorator):
    """
    Decorator to be applied to student objects for students 
    who volunteer.
    Methods:
        grade_point_average: A grade point average accessor 
        which applies a gpa boost based on volunteering.
    """
    @property
    def grade_point_average(self) -> float:
        """
        Grade point average accessor.
        Returns:
            float: The value of the grade point average 
            with a boost applied.
        """  
        return super().grade_point_average + 0.25
    