# A class method belongs to the CLASS,
# not to individual objects.
#
# It receives 'cls' (the class itself)
# as the first parameter instead of 'self'.
#
# Syntax:
#
# @classmethod
# def method_name(cls):
#     ...
#
# Class methods are commonly used to:
# 1. Access or modify class variables.
# 2. Create alternative constructors.


class Student:

    # ============================================
    # Class Variable
    # ============================================
    #
    # Shared by every Student object.
    #
    school = "ABC Public School"

    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # ============================================
    # Instance Method
    # ============================================
    #
    # Uses 'self'
    # Can access both instance and class variables.
    #
    def display(self):
        print(f"Name   : {self.name}")
        print(f"Marks  : {self.marks}")
        print(f"School : {Student.school}")

    # ============================================
    # Class Method
    # ============================================
    #
    # Uses 'cls' instead of 'self'.
    #
    # It modifies the class variable,
    # so the change affects ALL objects.
    #
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


# ============================================
# Creating Objects
# ============================================

student1 = Student("Alice", 90)
student2 = Student("Bob", 75)

print("===== Before Changing School =====")
student1.display()
print()
student2.display()

# Calling the class method
Student.change_school("XYZ International School")

print("\n===== After Changing School =====")
student1.display()
print()
student2.display()