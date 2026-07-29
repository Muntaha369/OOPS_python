class Student:
    allStudent = []
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        Student.allStudent.append(self)
        
    def __str__(self):
        return f"Student is {self.name}, age is {self.age} and {self.marks}"

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __add__(self, other):
        return self.marks + other.marks

    def __div__(self, other):
        return self.marks / other.marks

    def __sub__(self, other):
        return self.marks - other.marks
    
    def __contains__(self, keyword):
        return keyword in self.name

    def __getitem__(self, keyword):
        if keyword == "name":
            return self.name
        if keyword == "age":
            return self.age
        if keyword == "marks":
            return self.marks

student1 = Student("Usop", 21, 75)
student2 = Student("Chopper", 19, 83)
student3 = Student("Nami", 21, 88)
student4 = Student("Robin", 29, 96)
student5 = Student("Franky", 30, 93)
student6 = Student("Brook", 99, 14)
student7 = Student("Sanji", 22, 75)
student8 = Student("Zoro", 22, 0)
student9 = Student("Luffy", 22, -10)

for student in Student.allStudent:
    print(student)

print('\n')

print(student1 == student7)
print(student1 == student4)

print('\n')

print(student4 < student9)
print(student2 < student3)

print('\n')

print(student4 > student9)
print(student2 > student3)

print('\n')

print(student4 + student9)
print(student2 + student3)
print('\n')

print(student4 - student9)
print(student2 - student3)
print('\n')

print("Usop" in student1)
print("Luffy" in student9)

print('\n')

print(student1["name"])
print(student1["age"])
print(student1["marks"])
