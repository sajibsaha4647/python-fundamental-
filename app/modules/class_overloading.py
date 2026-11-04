from functools import singledispatchmethod

class Printer :

    @singledispatchmethod
    def display(self,value):
        print(f"other value {value}")

    @display.register
    def _(self,value:int):
        print(f"integer {value}")

    @display.register
    def _(self,value:str):
        print(f"string value {value}")
    