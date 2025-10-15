class School():
    school_name = "test"
    def student(self):
        return f"test values i s {self.school_name}"
        pass

# different object will be created
school = School()
school1= School()
print( School.school_name)
print(school.school_name)
school.school_name = "test to be changed"
print(school.student())