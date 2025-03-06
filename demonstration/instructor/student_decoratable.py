from abc import ABC, abstractmethod

class StudentDecoratable(ABC):
    """
    Interface to be applied to the Student class.
    Methods:
        grade_point_average:  Abstract method which must
        be implemented in subclasses.
    """
    @abstractmethod
    def grade_point_average(self) -> float:
        """
        Abstract grade_point_average accessor.
        returns:
            float
        """
        pass