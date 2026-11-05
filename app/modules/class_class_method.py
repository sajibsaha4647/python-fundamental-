class ClassMethod:
    school = "ABC School"

    def __init__(self):
       pass

    @classmethod
    def get_school(cls):
        return cls.school