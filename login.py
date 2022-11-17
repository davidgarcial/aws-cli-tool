from clear import clear
from user import User

tab = '   '

class LoginStore:
    def __init__(self):
        self.users = []
        self.get_users()

    def add_user(self, username, password, accessKey, secretAccessKey, userType):
        for user in self.users:
            if user.name in self.users:
                raise AssertionError('User already exists')

        with open("passwords.txt", "a+") as file:
            file.write(username + tab + password  + tab + accessKey  + tab + secretAccessKey + tab + userType + tab + '\n')
            file.close()
 
        self.users.append(User(username, password, accessKey, secretAccessKey, userType))

        print("Done. Try to login.")

    def check_user(self, username, password):
        for user in self.users:
            if username == user.name and password == user.pwd:
                return user
 
        return False

    def get_users(self):
        print('Registered Users Are:')
        with open("passwords.txt", "r+") as f:
            for line in f:
                dataSplited = line.split(tab)
                self.users.append(User(dataSplited[0], dataSplited[1], dataSplited[2], dataSplited[3], dataSplited[4]))
                print('\t | ' + dataSplited[0])
            f.close()

class Login:
    def __init__(self):
        self.store = LoginStore()

    def _ask_input_and_password(self):
        username = input("username: ")
        password = input("password: ")
        return username, password

    def _ask_aws_credentials(self):
        accessKey = input("aws access key: ")
        secretAccessKey = input("aws secret access key: ")
        return accessKey, secretAccessKey

    def login_check(self):
        if input("Are you a new user? (yes/no) ") == "yes":
            print("Starting registration process")
            username, password = self._ask_input_and_password()
            accessKey, secretAccessKey = self._ask_aws_credentials()
            userType = "regular"

            if input("The user is an admin? (yes/no) ") == "yes":
                userType = "admin"

            self.store.add_user(username, password, accessKey, secretAccessKey, userType)

        username, password  = self._ask_input_and_password()

        if not username and not password:
            return
        
        user = self.store.check_user(username, password)

        if not user:
            print("Wrong username or password")
            clear(1)
            self.users = []
            self.store.get_users()
            username, password  = self.login_check()

        return user
