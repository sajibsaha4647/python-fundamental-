from .class_father import Father
from .class_mother import Mother

class Child(Father,Mother):
    def __init__(self, name, breed, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.name = name
        self.breed = breed

 

    def whereFrom(self):
        print(f"i am {self.breed} from child class")