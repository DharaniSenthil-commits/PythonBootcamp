
class Student :
    def __init__(self, name, course, gpa, on_prohibtion):
        self.name=name
        self.course=course
        self.gpa=gpa
        self.on_prohibtion=on_prohibtion

    def honour_roll(self):
        if self.gpa > 3.5 :
            return True
        else:
            return False


