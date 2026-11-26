class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        return f"I am {self.name}, a student in grade {self.grade}."


student = Student("Bob", 10)
print(student.introduce())