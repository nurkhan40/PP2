class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa 

    def info(self):
        print(f"Sudent {self.name} and there is his gpa: {self.gpa}")

p1 = Student("John", 3.0)

p1.info()