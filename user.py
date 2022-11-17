class User:
    name = ""
    pwd = ""
    accessKey = ""
    secretAccessKey = ""
    region_name = "us-east-2"
    userType = ""

    def __init__(self, name, pwd, accessKey, secretAccessKey, userType):
        self.name = name
        self.pwd = pwd
        self.accessKey = accessKey
        self.secretAccessKey = secretAccessKey
        self.userType = userType
        self.region_name = "us-east-2"
