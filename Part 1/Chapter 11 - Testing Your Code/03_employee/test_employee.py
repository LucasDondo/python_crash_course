import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    ''' Tests the Employee class. '''

    def setUp(self):
        ''' Creates an Employee class to use among the other tests. '''

        self.employee = Employee('Delfina', 'Dondo', 1_000_000)

    def test_give_default_raise(self):
        ''' Does giving the default raise work? '''

        self.employee.give_raise()

    def test_give_custom_raise(self):
        ''' Does giving a custom raise work? '''

        self.employee.give_raise(12_000)


if __name__ == '__main__':
    unittest.main()
