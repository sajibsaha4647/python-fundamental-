class Teacher:
    def __init__(self,name):
        self.name = name 
        print(f"the name from teacher {self.name}")

    # after pass ing teacher object then this method conver it to string then the agregation two file run the name what i have pass 
    def __str__(self):
        return self.name