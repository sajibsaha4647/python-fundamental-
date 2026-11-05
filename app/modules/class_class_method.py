class ClassMethod:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_name(cls, name):
        return cls(name, 0)

    @classmethod
    def from_dictionary(cls, data):
        print("speak from dictionary")
        return cls(data["name"], data["age"])

    @classmethod
    def get_school(cls):
        return cls.school