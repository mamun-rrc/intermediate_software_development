"""
Description: Unit tests for the Course class.
Author: ACE Faculty
Modified by: {Mamun}
Date: {08/01/2025}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_course.py
"""
import unittest
from course.course import Course
from department.department import Department

class TestCourse(unittest.TestCase):


    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and 
        # provides initial values for the class attributes.
         self.course = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE, 6)  


    def test_init_valid(self):
        # Arrange & Act
        course = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE, 6)  
        
        # Assert (uses name mangling to obtain private attribute)
        self.assertEqual("Intermediate Software Development", course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, course._Course__department)
        self.assertEqual(6, course._Course__credit_hours)


    def test_init_invalid_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            course = Course("   ", Department.COMPUTER_SCIENCE, 6)
  
    def test_init_invalid_department_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            course = Course("Intermediate Software Development", "Invalid", 6)  
        
    def test_init_invalid_credit_hours_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            course = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE, "six")  

        
    def test_name_accessor(self):
        # Arrange done by setUp above...
        # Act and Assert 
        self.assertEqual("Intermediate Software Development", self.course.name)

    def test_department_accessor(self):
        # Arrange done by setUp above

         # Act and Assert 
        self.assertEqual(Department.COMPUTER_SCIENCE, self.course.department)

    def test_credit_hours_accessor(self):
        # Arrange done by setUp above

         # Act and Assert 
        self.assertEqual(6, self.course.credit_hours)


    def test_str(self):
        # Arrange done by setUp above
        expected = ("Course: Intermediate Software Development\n"
                    + "Department: Computer Science\n"
                    + "Credit Hours: 6")

        # Act and Assert
        self.assertEqual(expected, str(self.course))




