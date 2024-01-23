CONTACT_ROLES = { 'Staff' : 0,
    'Student' : 1
}

class Capstone:
    def __init__(self, res):
        self.pic = res[0]
        self.role = res[1]
        self.nstudent =res[2]
        self.year =res[3]
        self.title =res[4]
        self.companyname =res[5]
        self.poc =res[6]
        self.description =res[7]