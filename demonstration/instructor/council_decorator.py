from patterns.decorator.student_decorator import StudentDecorator

class CouncilDecorator(StudentDecorator):
    """
    Decorator to be applied to student objects for students 
    who participate on student council.
    Methods:
        grade_point_average: A grade point average accessor 
        which applies a gpa boost based on student council
        partication.
    """
    @property
    def grade_point_average(self) -> float:
        """
        Grade point average accessor.
        Returns:
            float: The value of the grade point average 
            with a boost applied.
        """        
        grade_point_average = super().grade_point_average

        increases: dict[float, float] = {
            4.13: 0.35,
            3.67: 0.19,
            2.40: 0.04
        }

        boost = 0

        for key in increases:
            if grade_point_average >= key:
                boost = increases[key]
                break

        return grade_point_average + boost

