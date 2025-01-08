from department.department import Department

class Course:
    """
    Course class.  Represents a course in a school.
    """
    def __init__(self, name: str, department: Department, credit_hours: int):
        """
        Initializes a course object based on received arguments (if valid).
        args:
            name (str): The name of the course.
            department (Department): The name of the department in which the course belongs.
            credit_hours(int): The number of credit hours assigned to the course.
        raises:
            ValueError: if any of the arguments are invalid.
        """
        if len(name.strip()) > 0:
            self.__name = name
        else:
            raise ValueError("Name cannot be blank.")

        if isinstance(department, Department):
            self.__department = department
        else:
            raise ValueError("Department must be one of the predefined Departments.")

        if isinstance(credit_hours, int):
            self.__credit_hours = credit_hours
        else:
            raise ValueError("Credit Hours must be a whole number.")


    @property
    def name(self) -> str:
        """
        Accessor for the name attribute.
        Returns: str - The name of the Course instance.
        """
        return self.__name

    @property
    def department(self) -> Department:
        """
        Accessor for the department attribute.
        Returns: Department - A specific Department enum value associated with the Course instance.
        """
        return self.__department
    

    @property
    def credit_hours(self) -> int:
        """
        Accessor for the credit_hours attribute.
        Returns: int - The number of credit hours associated with the Course instance.
        """
        return self.__credit_hours
    
    def __str__(self) ->str:
        """
        Returns a string representation of the Course instance.
        Returns: str - The Course instance as a formatted string.
        """
        # Note: For departments containing more than one word
        # replace the _ with a blank.
        return (f"Course: {self.name}"
                + f"\nDepartment: {self.__department.name.replace('_', ' ').title()}"
                + f"\nCredit Hours: {self.__credit_hours}")