class student:
    def __init__(self , name, major, grade, is_on_probation):
        self.name = name
        self.major = major
        self.grade = grade
        self.is_on_probation = is_on_probation
    def on_honor_roll(self):
        if self.grade >=2.0 :
            return True
        else:
            return False

