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


#  Collections I: lists and tuples Store and update records. Practice indexing, slicing, append, remove, sorting and tuple
# unpacking.

students = ["Rahim", "Karim", "Sajib", "Hasan"]

print(students[0])
print(students[-4])

# Slicing so its always print start value 

print(students[1:2])

numbers2 =  [10, 20, 30, 40, 50, 60]

print(numbers2[:3])   # [10, 20, 30]
print(numbers2[2:])   # [30, 40, 50, 60]
print(numbers2[-3:])  # [40, 50, 60]
print(numbers2[:])    # Complete list
print(numbers2[::2])  # [10, 30, 50]

numbers3 =  [10, 20, 70, 40, 50, 60]

numbers3.sort()
result = sorted(numbers3)

print(numbers3)
print(result)

students6 = [
  ("Rahim", 80),
    ("Karim", 75),
    ("Sajib", 90),
    ("Hasan", 85)
]

# Display all students
for name, marks in students6:
    print(name, marks)

# students6.append(("sajib saha", 78))
# students6.pop((1))

# students.sort(key=lambda students6: students6[1], reverse=True)

students6.sort(key=lambda students6: students6[1])

print("\nSorted student records:")

for name, marks in students6:
    print(name, marks)


print(students6)


# Collections II: dictionaries and
# sets
# Represent JSON-like user/product records with dictionaries. Use sets to remove duplicates
# and test membership.

user = {
    "id": 101,
    "name": "Sajib",
    "age": 30,
    "email": "sajib@gmail.com",
    "is_active": True
}

print(user["id"])
print(user.get("name"))
print(user.get("age"))
user["email"] = "sajib55@gmail.com"

print(user["email"])


user.update({
    "age": 31,
    "city": "Comilla"
})


user.pop("age")

del user["name"]

print(user)

user.clear()
for key,value in user.items():
   print(value)

# user.clear()


product = {
    "id": 101,
    "name": "Laptop",
    "price": 75000,
    "category": {
        "id": 1,
        "name": "Electronics"
    },
    "stock": {
        "quantity": 15,
        "available": True
    }
}

products = [
    {
        "id": 101,
        "name": "Laptop",
        "price": 75000,
        "category": "Electronics"
    },
    {
        "id": 102,
        "name": "Mobile",
        "price": 25000,
        "category": "Electronics"
    },
    {
        "id": 103,
        "name": "Chair",
        "price": 5000,
        "category": "Furniture"
    },
    {
        "id": 104,
        "name": "Table",
        "price": 12000,
        "category": "Furniture"
    }
]

# print(product["category"]["name"])

users = [
    {
        "id": 1,
        "name": "Rahim",
        "age": 25
    },
    {
        "id": 2,
        "name": "Karim",
        "age": 28
    },
    {
        "id": 3,
        "name": "Sajib",
        "age": 30
    }
]

# # Display all products
# for product in products:
#     print(product["name"], product["price"])

# Add a product
products.append({
    "id": 105,
    "name": "Keyboard",
    "price": 1500,
    "category": "Electronics"
})

# Update product price
products[0]["price"] = 70000

# Remove product by ID
products = [
    product for product in products
    if product["id"] != 102
]

# Get unique categories
categories = {
    product["category"]
    for product in products
}

print("\nUnique categories:")
print(categories)

# Check product existence
product_ids = {product["id"] for product in products}

print(105 in product_ids)