# GIven Imports
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt, Slot

from student.student import Student
from department.department import Department

# Required
from demo_superclasses.listing import Listing
from user_interface.grade_point_average_calculator import GradePointAverageCalculator


class StudentListing(Listing):
    """
    A window which displays student data.
    Inherited from Listing which provides the gui design.
    """
    def __init__(self):
        """
        Initialize the window.
        """
        super().__init__()
        #Given
        self.students = []
        self.students.append(Student("Janine Wharton", Department.COMPUTER_SCIENCE))
        self.students.append(Student("Freddie Jeffries", Department.MEDICINE))
        self.students.append(Student("Paul Thompson", Department.COMPUTER_SCIENCE))
        self.students.append(Student("Suzanne Marchand", Department.EDUCATION))

        self.student_table.setRowCount(len(self.students))

        row = 0

        for student in self.students:
            # Create qtablewidgetitems
            student_number_item = QTableWidgetItem(str(student.student_number))
            name_item = QTableWidgetItem(student.name)
            grade_point_average_item = QTableWidgetItem(f"{student.grade_point_average:.2f}")

            # Align text
            grade_point_average_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

            # Place items in table
            self.student_table.setItem(row, 0, student_number_item)
            self.student_table.setItem(row, 1, name_item)
            self.student_table.setItem(row, 2, grade_point_average_item)

            # advance the row
            row += 1
        self.student_table.resizeColumnsToContents()

        # connect signal to slot:
        self.student_table.cellClicked.connect(self.__on_select_student)

        

        


    @Slot(int, int)
    def __on_select_student(self, row: int, column: int):
        """
        Obtain values from a clicked row.
        Connected to the cellClicked event of a QTable and therefore has row/column arguments.
        args:
            row (int): Row that has been clicked on.
            column(int): Column that has been clicked on.
        """
        # obtain values of name and student number
        student_number = self.student_table.item(row, 0).text()
        name = self.student_table.item(row, 1).text()

        calculator = GradePointAverageCalculator(student_number, name)

        # receive signal from other window
        calculator.new_gpa.connect(self.__update_gpa)

        calculator.exec()

    @Slot(str, float)
    def __update_gpa(self, student_number: str, gpa: float):
        """
        Updates the GPA value based on updates made in another window. The 
        other window sends a signal upon updating, and this slot receives the signal.
        args:
            student_number (str): The impacted student number.
            gpa (float): The updated gpa value.
        """
        for row in range(self.student_table.rowCount()):
            if self.student_table.item(row, 0).text() == student_number:
                self.student_table.item(row, 2).setText(f"{gpa:.2f}")
        
