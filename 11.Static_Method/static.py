# Instance Method
# ----------------
# - Works with a specific object (instance).
# - Has 'self' as the first parameter.
# - Can access and modify instance variables.
#
# Static Method
# -------------
# - Belongs to the class.
# - Does NOT use 'self'.
# - Cannot access instance variables directly.
# - Used for utility/helper functions.

class Employee:
    def __init__(self, employee, position):
        self.employee = employee
        self.position = position

    def info(self):
        print(f"{self.employee} is a {self.position}")

    @staticmethod
    def valid_pos(position):
        valid_positions = ["Developer", "Infra manager", "DBA", "QA"]

        return position in valid_positions

print(Employee.valid_pos("DBA"))
print(Employee.valid_pos("Api caller"))


employee1 = Employee("Khalid Kashmiri", "Developer")
employee2 = Employee("Muhammad Sumbul", "Infra manager")

employee1.info()
employee2.info()