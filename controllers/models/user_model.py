class User:
    def __init__(self, res):
        self.username =res[0]
        self.password =res[1]
        self.role_id =res[2]

    def serialize(self):
        return { \
            'username' : self.username, \
            'password' : self.password, \
            'role_id' : self.role_id \
        }