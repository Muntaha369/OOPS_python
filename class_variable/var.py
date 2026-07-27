class Person:
    status = "Unemployed (NEET)"   # This is the calss variable which mentioned in the class and is the part of the every instance
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def stud_details(self):
        print(self.name, self.age)

student1 = Person("Osomatsu", 20)
student2 = Person("Karamatsu", 19)

student1.stud_details()
student2.stud_details()

print(student2.status) # Status is the part of evey instance 
print(student1.status) # it can be student 1 2 3 .... n
print(Person.status) # So its better to represent by the class like this