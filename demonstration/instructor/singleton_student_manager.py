class SingletonStudentManager:
    __instance = None
    __next_student_number = 20240000

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(SingletonStudentManager, cls).__new__(cls)
        return cls.__instance
    
    def get_next_student_number(self):
        student_number = self.__next_student_number
        self.__next_student_number += 1
        return student_number