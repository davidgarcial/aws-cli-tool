import os

from user import User
from utils import clear

# This variable was created to just call a define var insted of write the tab each time
# For some reason \t was not working saving the text file
tab = '   '

class LoginStore:
    def __init__(self):
        self.users = []

    def add_user(self, username, password, accessKey, secretAccessKey, region, userType):
        for user in self.users:
            if user.name in self.users:
                raise AssertionError('User already exists')

        with open('passwords.txt', 'a+') as file:
            file.write(f'{username}{tab}{password}{tab}{accessKey}{tab}{secretAccessKey}{tab}{region}{tab}{userType}{tab}\n')
            file.close()
 
        self.users.append(User(username, password, accessKey, secretAccessKey, region, userType))

        print('Done. Try to login.')
        clear()

    def check_user(self, username, password):
        for user in self.users:
            if username == user.name and password == user.pwd:
                return user
 
        return False

    def get_users(self):
        if self.fileEmptyOrNull():
            print('There are not registered users')
            return

        print('Registered Users Are:')
        with open('passwords.txt', 'r+') as f:
            for line in f:
                dataSplited = line.split(tab)
                self.users.append(User(dataSplited[0], dataSplited[1], dataSplited[2], dataSplited[3], dataSplited[4]))
                print('\t | ' + dataSplited[0])
            f.close()

    def fileEmptyOrNull(self):
        if not os.path.exists("password.txt"):
            return True

        if os.stat('passwords.txt').st_size == 0:
            return True

        return False

class Login:
    def __init__(self):
        self.store = LoginStore()

    def _ask_input_and_password(self):
        username = input('username: ')
        password = input('password: ')
        return username, password

    def _ask_aws_credentials(self):
        accessKey = input('aws access key: ')
        secretAccessKey = input('aws secret access key: ')
        return accessKey, secretAccessKey

    def login_check(self):
        username, password  = self._ask_input_and_password()

        if not username and not password:
            quit()
        
        user = self.store.check_user(username, password)

        if not user:
            print('Wrong username or password')
            clear(1)
            self.users = []
            self.store.get_users()
            return

        return user
    
    def registerUser(self):
        print('Starting registration process')
        username, password = self._ask_input_and_password()
        accessKey, secretAccessKey = self._ask_aws_credentials()
        region = 'us-east-2'

        if input(f'Do you would like chage the default region "{region}" (yes/no) ') == 'yes':
            userType = input('Provide a valid region in aws: ')

        userType = 'regular'

        if input('The user is an admin? (yes/no) ') == 'yes':
            userType = 'admin'

        self.store.add_user(username, password, accessKey, secretAccessKey, region, userType)

    def main(self):
        if self.store.fileEmptyOrNull():
            print('There are not registred users, plese register one')
            self.registerUser()
        else:
            self.store.get_users()
            if input('Do you want add a new user? (yes/no) ') == 'yes':
                self.registerUser()

        user = self.login_check()

        while not user:
            user = self.login_check()

        return user