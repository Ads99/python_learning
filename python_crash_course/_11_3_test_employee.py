# Example 11.3 - Employee Test
# Write a test case for Employee. Write two test methods, test_give_default_raise()
# and test_give_custom_raise(). Use the setUp() method so you don't have to
# create a new employee instance in each test method. Run your test case and
# make sure both tests pass

import unittest
from _11_3_example_employee_class import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Create an Employee and some details  for use in all test methods."""
        self.my_employee = Employee('adam', 'baker', 78000)

    def test_give_default_raise(self):
        """Test that the default 5000 raise is given."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 83000)

    def test_give_custom_raise(self):
        """Test that a custom $ raise works."""
        self.my_employee.give_raise(6000)
        self.assertEqual(self.my_employee.salary, 84000)


unittest.main()