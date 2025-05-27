#Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

# Subclass: Student
class Student(Person):
    def __init__(self,name,age,student_id,course):
        super().__init__(name,age,)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"STUDENT ID:{self.student_id}")
        print(f"Course:{self.course}")
# Subclass: Lecturer

class Lecturer(Person):
     def __init__(self, name, age, lecturer_id, department):
                super().__init__(name, age, )
                self.lecturer_id = lecturer_id
                self.department = department

     def display_info(self):
                super().display_info()
                print(f"LECTURER ID:{self.lecturer_id}")
                print(f"Department:{self.department}")

# Subclass: Staff
class Staff(Person):
    def __init__(self,name,age,staff_id,role):
        super().__init__(name,age)
        self.staff_id = staff_id
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"STAFF ID:{self.staff_id}")

# DEMo
if __name__ == "__main__":
    print("---Student Info---")
    student = Student("Sandra",22,"2300707270","BSSE")
    student.display_info()

    print("\n---Lecturer info---")
    lecturer = Lecturer("Dr Ruth", 40,"l4567","Networks")
    lecturer.display_info()

    print("\n---Staff Info---")
    staff = Staff("Mr Mike", 35,"ST9101","Librarian")
    staff.display_info()