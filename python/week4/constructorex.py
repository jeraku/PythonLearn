class School():
    def __init__(self, student_name):
        self._name = student_name
    def get_stundent_name(self):
        return self._name
    def set_stundent_name(self, name):
        self._name = name

school= School("jegan")
print(school.get_stundent_name())
school.set_stundent_name("raj")
print(school.get_stundent_name())
