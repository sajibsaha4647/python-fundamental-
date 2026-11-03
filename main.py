# print( "hi this was me")
from typing import Final
from itertools import zip_longest
from pathlib import Path
import json
import csv
# import copy
# # int
# age: int = 30
# quentity:int = 50


# # float

# price = 44.4
# height = 4.5

# # string 

# name ="sajib"

# # bool

# isData = True
 
# dataType: bool = True

# NewValue:None = ""

# APP_NAME = "Ecommerce"
# MAX_USERS: Final[int] = 1000

# print(type(name))

# # type convert 

# print(float(age))
# print(str(age))
# print(bool(age))

# number = list((2,5,5,5,5,5,55,))
# # List to tuple
# numbers = tuple([1, 2, 3])
# # List to set (removes duplicates)
# numbers = set([1, 2, 2, 3])
# # List of pairs to dictionary
# user = dict([("name", "Sajib"), ("age", 30)])
# print(number)


# # Integer list
# numbers = [10, 20, 30, 40, 50]

# # String list
# names = ["Rahim", "Karim", "Sajib"]

# # Float list
# prices = [10.5, 20.5, 30.5]

# # Mixed data types
# data = [10, "Sajib", 25.5, True]



# data.extend([2,3,5,6])
# data.append("excused")
# data.pop(len(data) - 1)

# for data in data:
#  print(data)


# #  Collections I: lists and tuples Store and update records. Practice indexing, slicing, append, remove, sorting and tuple
# # unpacking.

# students = ["Rahim", "Karim", "Sajib", "Hasan"]

# print(students[0])
# print(students[-4])

# # Slicing so its always print start value 

# print(students[1:2])

# numbers2 =  [10, 20, 30, 40, 50, 60]

# print(numbers2[:3])   # [10, 20, 30]
# print(numbers2[2:])   # [30, 40, 50, 60]
# print(numbers2[-3:])  # [40, 50, 60]
# print(numbers2[:])    # Complete list
# print(numbers2[::2])  # [10, 30, 50]

# numbers3 =  [10, 20, 70, 40, 50, 60]

# numbers3.sort()
# result = sorted(numbers3)

# print(numbers3)
# print(result)

# students6 = [
#   ("Rahim", 80),
#     ("Karim", 75),
#     ("Sajib", 90),
#     ("Hasan", 85)
# ]

# # Display all students
# for name, marks in students6:
#     print(name, marks)

# # students6.append(("sajib saha", 78))
# # students6.pop((1))

# # students.sort(key=lambda students6: students6[1], reverse=True)

# students6.sort(key=lambda students6: students6[1])

# print("\nSorted student records:")

# for name, marks in students6:
#     print(name, marks)


# print(students6)


# # Collections II: dictionaries and
# # sets
# # Represent JSON-like user/product records with dictionaries. Use sets to remove duplicates
# # and test membership.

# user = {
#     "id": 101,
#     "name": "Sajib",
#     "age": 30,
#     "email": "sajib@gmail.com",
#     "is_active": True
# }

# print(user["id"])
# print(user.get("name"))
# print(user.get("age"))
# user["email"] = "sajib55@gmail.com"

# print(user["email"])


# user.update({
#     "age": 31,
#     "city": "Comilla"
# })


# user.pop("age")

# del user["name"]

# print(user)

# user.clear()
# for key,value in user.items():
#    print(value)

#    numbers.discard(100)  # No error if 100 doesn't exist

# # user.clear()


# product = {
#     "id": 101,
#     "name": "Laptop",
#     "price": 75000,
#     "category": {
#         "id": 1,
#         "name": "Electronics"
#     },
#     "stock": {
#         "quantity": 15,
#         "available": True
#     }
# }

# products = [
#     {
#         "id": 101,
#         "name": "Laptop",
#         "price": 75000,
#         "category": "Electronics"
#     },
#     {
#         "id": 102,
#         "name": "Mobile",
#         "price": 25000,
#         "category": "Electronics"
#     },
#     {
#         "id": 103,
#         "name": "Chair",
#         "price": 5000,
#         "category": "Furniture"
#     },
#     {
#         "id": 104,
#         "name": "Table",
#         "price": 12000,
#         "category": "Furniture"
#     }
# ]

# # print(product["category"]["name"])

# users = [
#     {
#         "id": 1,
#         "name": "Rahim",
#         "age": 25
#     },
#     {
#         "id": 2,
#         "name": "Karim",
#         "age": 28
#     },
#     {
#         "id": 3,
#         "name": "Sajib",
#         "age": 30
#     }
# ]

# # # Display all products
# # for product in products:
# #     print(product["name"], product["price"])

# # Add a product
# products.append({
#     "id": 105,
#     "name": "Keyboard",
#     "price": 1500,
#     "category": "Electronics"
# })

# # Update product price
# products[0]["price"] = 70000

# # Remove product by ID
# products = [
#     product for product in products
#     if product["id"] != 102
# ]

# # Get unique categories
# categories = {
#     product["category"]
#     for product in products
# }

# print("\nUnique categories:")
# print(categories)

# # Check product existence
# product_ids = {product["id"] for product in products}

# print(105 in product_ids)

# # Conditions and loops Use if/elif/else, for and while. Practice break, continue, enumerate and zip with real data.


# ager = 25
# is_active = True

# if ager <= 25:
#    print("you are elligiable")
# else:
#     print("You are not eligible")

#     markes:int = 85

#     if markes>=90:
#        print("you get golden A+")
#     elif markes>=80:
#        print("you get A+")
#     else :
#        print("sorry for failed")

# if age >= 18 and is_active:
#     print("User can access the system")

# if  not is_active:
#     print("Account is inactive")


# for i in range(5):
#     print(i)

# range(1, 6)       # 1, 2, 3, 4, 5
# range(2, 11, 2)   # 2, 4, 6, 8, 10

# count = 1

# while count <= 5:
#     print(count)
#     count += 1

# # get unique numbers
# numbersNew = [10, 20, 30, 20, 10, 40, 50]

# unique_numbers = list(dict.fromkeys(numbersNew))

# print(unique_numbers)

# studentsNew = ["Rahim", "Karim", "Sajib", "Hasan"]
# for student in studentsNew:
#     print(student)


# for i in range(len(students)):
#     print(i, students[i])

# for index, student in enumerate(students):
#     print(index, student)

# for index, student in enumerate(students, start=1):
#     print(index, student)

#     names = ["Rahim", "Karim", "Sajib"]

# marks = [80, 75, 90]

# for name, mark in zip(names, marks):
#     print(name, mark)

#     student_records = dict(zip(names, marks))

# print(student_records)


# result = list(zip_longest(names, marks, fillvalue="N/A"))

# print(result)

# day =2

# day = 2

# match day:
#     case 2:
#         print("Found the day")

#     case _:
#         print("Invalid day")

# number = 15

# match number:
#     case n if n > 10 or is_active == True and is_active == "True" :
#         print("Greater than 10")

#     case _:
#         print("10 or less")

# age = 16
# is_student = True

# match age:
#     case n if n >= 18 and is_student:
#         print("Adult student")

#     case n if n < 18 or not is_student:
#         print("Not an adult student")

#     case _:
#         print("Unknown")

# #  Functions Write small reusable functions. Understand parameters, return values, default arguments,
# # keyword arguments and local/global scope

# a: int = 20

# b:int = 30
# c:float = 30

# print(a+b+c)

# def addSum(a:int, b:int)->int:
#     result = a+b
#     print(a+b)
#     return result

# addSum(20,55.55)


# def calculate(a: int, b: int) -> float:
#     return a / b

# result = calculate(10, 2)

# print(type(result))


# # Mutable and immutable objects Understand references, object identity and why changing a list inside a function can affect
# # the caller. Practice shallow and deep copy.


# name2 = "Sajib"

# name2 = "Rahim"

# print(name2)


# a = "Hello"
# a = "World"
# print(a)

# newVal = (["sajib","saha",23])

# newVal[0] = "rana"

# print(newVal)

# nameTwo = "test new"
# ageTwo = "34"

# newResultTwo = dict(name=nameTwo, age=ageTwo)

# print(newResultTwo)

# newListTwo = [20,30,50,60]

# copyList =  newListTwo.copy()

# newListTwo[0] = 500

# print(copyList)
# print(newListTwo)

# data:int = 50
# data = 50.60

# print(data)


# a = 100
# b = a

# a = 200

# print(a)
# print(b)

# MAX_USERS: Final[int] = 100

# MAX_USERS = 200

# print(MAX_USERS)


# newListTwoDeep = [20, 30, 50, 60]

# resT = copy.deepcopy(newListTwoDeep)



# resT.insert(1, 100)
# resT.insert(2, 700)

# resTwo = resT.copy()

# print(newListTwoDeep)
# print(resT)
# print(resTwo)


# #  Comprehensions and sorting Use list/dict/set comprehensions, sorted, key functions and lambda. Rewrite repetitive loops
# # clearly.


numbers = [1, 2, 3, 4, 5]

# squares = []

# for number in numbers:
#      squares.append(number * number)


# print(squares)


# squares = [number * number for number in numbers]

# print(squares)

# evenNumbers = []

# for number in numbers:
#     if number % 2 == 0:
#         evenNumbers.append(number)

# evenNumbers = [number 
#                for number in numbers
#                 if number % 2 == 0
            
#                ]
# even_numbers = [
#     number
#     for number in numbers
#     if number % 2 == 0
# ]


# print(evenNumbers)
# print(even_numbers)



# names = ["Sajib", "Rahim", "Karim"]

# name_lengths = {
#     name: len(name)
#     for name in names
# }

# print(name_lengths)


# numbers = [50, 10, 40, 20, 30]

# result = sorted(numbers)

# print(result)
# print(numbers)

# numbers.sort()

# print(numbers)


# numbers = [50, 10, 40, 20, 30]

# ascending = sorted(numbers)
# descending = sorted(numbers, reverse=True)

# print(ascending)
# print(descending)



# students = [
#     ("Rahim", 75),
#     ("Karim", 90),
#     ("Sajib", 85),
#     ("Hasan", 60)
# ]

# def markets(students):
#     print(students)
#     return students[1]

# student = sorted(students, key=markets)

# print(student)



# Python: Errors and Exceptions


# number = 10
# result = number / 0

# print(result)


# try:
#     number = 10 / 0
#     print(number)

# except ZeroDivisionError:
#     print("You cannot divide by zero")


# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number

# except ValueError:
#     print("Invalid number.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# else:
#     print("Calculation successful!")
#     print("Result:", result)


# try:   
#    number = int(input("enter number"))
#    result = 100/numbers
# except : ValueError
# except: ZeroDivisionError
#  print("can not works with this value")

# else :
# print("Calculation successful!")

# finally :
#   print("Calculation process finished.")


# try:
#     number = int(input("Enter number: "))
#     result = 100 / number

# except ValueError:
#     print("Invalid number.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# else:
#     print("Calculation successful!")
#     print("Result:", result)

# finally:
#     print("Calculation process finished.")


# try: 
#     number = int(input("enter a number here"))
# except ValueError :
#     print("invalid value")

# except ZeroDivisionError:
#     print("dividation error")

# else :
#     print("calculation successfull")

# finally :
#     print("calculatin finished")



# user = {
#     "name": "sajib",
#     "age": 19,
#     "email": "sajib@example.com"
# }

# def register_user(user):
#     try:
#         name = user["name"]
#         age = user["age"]
#         email = user["email"]
#         if not name or not age or not email:
#             raise ValueError("All fields are required")
#         if not isinstance(name,str) or not name.strip():
#             raise ValueError("Name is required")
#         if age<=17:
#             raise ValueError("age must be at least 18")
#         if '@' not in email :
#             raise ValueError("invalid email address")
#     except KeyError as error :
#         print("Missing required field:", error)
#     except (ValueError, TypeError) as error:
#         print("Registration failed:", error)
#     else :
#         print("registration successfull")
#     finally:
#         print("Registration process completed.")


# register_user(user)



BASE_DIR = Path(__file__).resolve().parent

# file_path = BASE_DIR / "data" / "user.txt"

# file_path.parent.mkdir(exist_ok=True,parents=True)
# with file_path.open("w", encoding="utf-8") as file:
#     file.write("Name: Sajib\n")
#     file.write("Age: 30\n")
#     file.write("Country: Bangladesh\n")

# # The write block has ended, so the file is closed and saved

# print(file_path)




# with file_path.open("a", encoding="utf-8") as file:
#     file.write("City: Comilla\n")
#     # lines = file.readlines()
    
#     # print(lines)


# with file_path.open("r", encoding="utf-8") as file:
#     content = file.read()
   

# print(content)

# user = {
#     "id": 101,
#     "name": "Sajib",
#     "age": 30,
#     "country": "Bangladesh"
# }


# with file_path.open("w", encoding="utf-8") as file:
#     json.dump(user, file, indent=4)
#     try:
#         with file_path.open("r", encoding="utf-8") as file:
#             user = json.load(file)
#     except FileNotFoundError:
#          print("Users file does not exist.")
#     except PermissionError:
#         print("You don't have permission to read this file.")

# print(user)
# print(user["name"])
# print(user["age"])


# try:
#     # Your code
#     number = int(input("Enter number: "))
#     result = 100 / number

# except Exception as error:
#     print("Exception:", type(error).__name__)
#     print("Message:", error)

# JSON, CSV and dates Parse API-style JSON, read CSV, work with datetime and timezone-aware timestamps.

# {
#     "id": 101,
#     "name": "Sajib",
#     "age": 30,
#     "is_active": true,
#     "skills": ["Python", "Go", "Flutter"]
# }



response = '''
{
    "id": 101,
    "name": "Sajib",
    "age": 30,
    "is_active": true
}
'''


# response = requests.get(url).text
# user = json.loads(response)


# print(repr(response))
# user = json.loads(response)


# print(user)
# print(user["name"])
# print(user["age"])



# user = {
#     "id": 101,
#     "name": "Sajib",
#     "age": 30,
#     "is_active": True
# }

# response = json.dumps(user)

# print(response)




# response = '''
# {
#     "success": true,
#     "data": [
#         {
#             "id": 1,
#             "name": "Rahim",
#             "age": 25
#         },
#         {
#             "id": 2,
#             "name": "Sajib",
#             "age": 30
#         }
#     ],
#     "message": "Users retrieved successfully"
# }
# '''

# result = json.loads(response)

# for user in result["data"]:
#     print(user["id"], user["name"], user["age"])
users = [
    ["id", "name", "age"],
    [1, "Sajib", 30],
    [2, "Rahim", 25],
    [3, "Karim", 28]
]
file_path = BASE_DIR /"json" /"json.csv"
file_path.parent.mkdir(exist_ok=True,parents=True)

headers = users[0]
rows = [dict(zip(headers, row)) for row in users[1:]]

with file_path.open("w", encoding="utf-8", newline="") as file:
   # writer = csv.writer(file)
   # writer.writerows(users)
   writer = csv.DictWriter(file, fieldnames=headers)
   writer.writeheader()
   writer.writerows(rows)

with file_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)