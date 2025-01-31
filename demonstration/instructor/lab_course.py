from course.course import Course
from department.department import Department
from student.student import Student

class LabCourse(Course):
    def __init__(self, name: str, department: Department, 
                 credit_hours: int, capacity: int, 
                 current_enrollment: int, lab_equipment: str):
        """
        __init__:  initializes class members to passed parameters.
        """
        super().__init__(name, department, credit_hours, capacity, current_enrollment)

        if len(lab_equipment.strip()) == 0:
            self.__lab_equipment = "None"
        else:
            self.__lab_equipment = lab_equipment

    
    def __str__(self)-> str:
        return super().__str__() + f"\nRequired Equipment: {self.__lab_equipment}"


    def enroll_student(self, student: Student)-> bool:
        message = f"{student.name}"
        if self._current_enrollment < (self._capacity / 2):
            self._current_enrollment += 1
            message += f" has been successfully enrolled in {self.name}."
        else:
            message += f" has NOT been enrolled in lab: {self.name} due to insufficient capacity."
        return message
