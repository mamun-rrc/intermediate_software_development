__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from user_interface.student_listing import StudentListing

# GIVEN:
from PySide6.QtWidgets import QApplication

# GIVEN:
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = StudentListing()
    mainWindow.show()
    sys.exit(app.exec())