# Example 11.3 - Employee
# Write a class called Employee. The __init__() method should take in a first
# name, last name and an annual salary and store each of these as attributes.
# Write a method called give_raise() that adds $5000 to the annual salary by
# default but also accepts a different raise amount

class Employee():
    """Collect detauls about an employee"""

    def __init__(self, f_name, l_name, salary):
        """Store a question, and prepare to store responses."""
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self, salary_raise=0):
        """Add $5000 to the annual salary by default but also accept
        another val"""
        if salary_raise:
            self.salary += salary_raise
        else:
            self.salary += 5000

    def show_results(self):
        """Show all details of an employee"""
        print("Employee name: " + self.f_name.title() + ' ' + self.l_name.title())
        print("Salary: " + str(self.salary))