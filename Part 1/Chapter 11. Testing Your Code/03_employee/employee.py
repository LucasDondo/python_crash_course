class Employee:
    ''' A simple attempt to represent an employee. '''

    def __init__(self, first_name, last_name, annual_salary):
        ''' Initializes some attributes of the employee. '''

        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5_000):
        ''' Simulates the employee receives a raise. '''

        self.annual_salary += salary_raise
