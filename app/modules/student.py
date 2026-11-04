class Student:
    name:str = "sajib"
    _age:int = 25 #protected
    __years:int = 2030 #private

    def __init__(self,name:str,age:int,years:int):
        print("constractor called")
        self.name = name
        # self._age = age
        # self.__years = years

    #getter
    @property
    def age(self) -> int:
        return self._age

    #setter
    @age.setter
    def age(self,value)->int:
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    #getter
    @property
    def years(self) -> int:
        return self.__years

    #setter
    @years.setter
    def years(self,value)->int:
        self.__years = value

    


    def getFunctionClass(self,other: "Student"):
        print(f"hi i am {self.name} from  student class")
        print(f"my friend is {other.name}, age {other.age}, year {other.years}")
