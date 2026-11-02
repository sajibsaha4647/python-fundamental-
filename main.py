print( "hi this was me")
from typing import Final
# int
age: int = 30
quentity:int = 50


# float

price = 44.4
height = 4.5

# string 

name ="sajib"

# bool

isData = True
 
dataType: bool = True

NewValue:None = ""

APP_NAME = "Ecommerce"
MAX_USERS: Final[int] = 1000

print(type(name))

# type convert 

print(float(age))
print(str(age))
print(bool(age))

number = list((2,5,5,5,5,5,55,))
# List to tuple
numbers = tuple([1, 2, 3])
# List to set (removes duplicates)
numbers = set([1, 2, 2, 3])
# List of pairs to dictionary
user = dict([("name", "Sajib"), ("age", 30)])
print(number)


# Integer list
numbers = [10, 20, 30, 40, 50]

# String list
names = ["Rahim", "Karim", "Sajib"]

# Float list
prices = [10.5, 20.5, 30.5]

# Mixed data types
data = [10, "Sajib", 25.5, True]



data.extend([2,3,5,6])
data.append("excused")
data.pop(len(data) - 1)

for data in data:
 print(data)




