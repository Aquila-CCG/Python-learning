class Student():
    
    currentYear = 2024
    
    def __init__(self, firstName, lastName, enrolledYear, major, stuID):
        self.firstName = firstName
        self.lastName = lastName
        self.enrolledYear = enrolledYear
        self.major = major
        self.stuID = stuID
        
    def showEmail(self):
        print(str(self.stuID) + self.firstName + self.lastName + "@uic.edu.cn")
        
    def showGradeLevel(self):
        return Student.currentYear - self.enrolledYear
    
    def showMajor(self):
        print("%s %s is in the %s program." %(self.firstName, self.lastName, self.major))
        