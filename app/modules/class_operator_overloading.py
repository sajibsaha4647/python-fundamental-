class OperatorOverloading:
    def __init__(self,value):
        self.value  = value

    def __mul__(self, other):
        print("__mul__ is running")
        if isinstance(other, OperatorOverloading):
            return OperatorOverloading(self.value * other.value)
        return OperatorOverloading(self.value * other)

    def __add__(self, other):
        print("__add__ is running")
        if isinstance(other, OperatorOverloading):
            return OperatorOverloading(self.value + other.value)
        return OperatorOverloading(self.value + other)


    # Optional: Helps print the object nicely instead of <__main__.OperatorOverloading object...>
    def __str__(self):
        return f"OperatorOverloading({self.value})"