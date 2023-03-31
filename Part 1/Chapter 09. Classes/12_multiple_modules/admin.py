from user import User

class Admin(User):
    ''' A simple attempt to model the admin type of user. '''

    def __init__(self, first_name, last_name, username, privileges):
        ''' Initialize first and last name.
            Initialize the privileges attribute (list). '''

        super().__init__(first_name, last_name, username)
        self.privileges = Privileges(privileges)


class Privileges:
    ''' A simple attempt to model the privileges of an admin user. '''

    def __init__(self, privileges):
        ''' Initialize the privileges list attribute. '''

        self.privileges = privileges

    def show_privileges(self):
        ''' It just shows this admin's privileges. '''

        print("This admin's privileges are:")
        for privilege in self.privileges:
            print(f'- {privilege.capitalize()}')
