from mixinex import  MixinLogin,TimeStampex
class Student(MixinLogin, TimeStampex):
    def __init__(self,name):
        print("I am in")
        self.student = []
        self.student_name = name

    def get_stud(self):
        return self.student_name

    def create(self, name):
        self.log("start creating the log")
        self.student.append(self.student_name)

studn = Student("hegan")