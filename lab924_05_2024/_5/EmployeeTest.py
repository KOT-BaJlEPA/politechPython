from lab924_05_2024._4.Employee import Employee
import unittest

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.empl = Employee("Alla", "Pugacheva", 20000)
    def test_give_default_raise(self):
        self.assertEqual(self.empl.give_raise(), 25000)

    def test_give_custom_raise(self):
        self.assertEqual(self.empl.give_raise(10000), 30000)



if __name__ == '__main__':
    unittest.main()