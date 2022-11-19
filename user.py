class User:
    name = ""
    pwd = ""
    accessKey = ""
    secretAccessKey = ""
    region = ""
    userType = ""

    def __init__(self, name, pwd, accessKey, secretAccessKey, region, userType):
        self.name = name
        self.pwd = pwd
        self.accessKey = accessKey
        self.secretAccessKey = secretAccessKey
        self.userType = userType
        self.region = region
