# GIven Imports
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, Signal
from demo_superclasses.gpa_window import GPAWindow


class GradePointAverageCalculator(GPAWindow):
    """
    A window that allows for GradePointAverage to be calculated.
    Inherited from GPAWindow which provides the gui design.
    """
    ## Signal
    new_gpa = Signal(str, float)
    
    def __init__(self, student_number: str, name: str):
        """
        Initializes the window widgets and displays received data.
        args:
            student_number (str):  The student number of the student being displayed.
            name (str): The name of the student being displayed.
        """
        super().__init__()
        self.GRADE_LOOKUP = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, 
                            "C+": 2.5, "C": 2, "D": 1, "F": 0}
        
        self.name_label.setText(name)
        self.student_number_label.setText(student_number)

        # establish connections
        self.credit_edit_1.textChanged.connect(self.__enable_button)
        self.credit_edit_2.textChanged.connect(self.__enable_button)
        self.credit_edit_3.textChanged.connect(self.__enable_button)

        self.calculate_button.clicked.connect(self.__on_calculate_clicked)

    @Slot()
    def __enable_button(self):
        """
        Validates the input fields and if valid, enables the Calculate button.
        """
        try:
            if (self.credit_edit_1.text() and 
                self.credit_edit_2.text() and 
                self.credit_edit_3.text()):
                try:
                    float(self.credit_edit_1.text())
                except:
                    self.credit_edit_1.setFocus()
                    raise ValueError("Credit Hours must be numeric.")
                
                try:
                    float(self.credit_edit_2.text())
                except:
                    self.credit_edit_2.setFocus()
                    raise ValueError("Credit Hours  must be numeric.")
                
                try:
                    float(self.credit_edit_3.text())
                except:
                    self.credit_edit_3.setFocus()
                    raise ValueError("Credit Hours must be numeric.")
                self.calculate_button.setEnabled(True)
        except ValueError as e:
            QMessageBox.information(self, "Credit Hours", str(e))
            self.calculate_button.setEnabled(False)
        
       
    @Slot()
    def __on_calculate_clicked(self):
        """
        Calculates the grade point average based on the data provided.
        Emits a signal with the student number and calculated gpa when complete.
        Formula: ((grade1 * cr_hours1) + (grade2 * cr_hours2) + etc) / sum(cr_hours#)
        """
        credit_1 = float(self.credit_edit_1.text())
        credit_2 = float(self.credit_edit_2.text())
        credit_3 = float(self.credit_edit_3.text())

        grade_value_1 = self.GRADE_LOOKUP[self.grade_select_1.currentText()]
        grade_value_2 = self.GRADE_LOOKUP[self.grade_select_2.currentText()]
        grade_value_3 = self.GRADE_LOOKUP[self.grade_select_3.currentText()]

        grade_point_average = ((
            (grade_value_1 * credit_1) + 
            (grade_value_2 * credit_2) + 
            (grade_value_3 * credit_3)) /
            (credit_1 + credit_2 + credit_3))

        self.grade_point_average_label.setText(f"{grade_point_average:.2f}")

        self.new_gpa.emit(self.student_number_label.text(), 
                          grade_point_average)
        
        


