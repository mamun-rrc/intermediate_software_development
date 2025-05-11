from course.course import Course
from department.department import Department

def main():
    # Create an instance of the Course class with valid inputs.
    # Print the instance.
    # If an exception occurs, print the exception instance.
    try:
        software_development_fundamentals = Course("Software Development Fundamentals", 
                                                   Department.COMPUTER_SCIENCE, 6)
        print(software_development_fundamentals)
    except ValueError as e:
        print(e)

    try:
        intermediate_software_development = Course("Intermediate Software Development", 
                                               Department.COMPUTER_SCIENCE, 6)
        print(intermediate_software_development)
    except ValueError as e:
        print(e)

    # Create an instance of the Course class with invalid inputs.
    # Print the instance.
    # If an exception occurs, print the exception instance.
    try:
        invalid_department = Course("Invalid Department", "Invalid Department", 6)
        print(invalid_department)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
    
    
    