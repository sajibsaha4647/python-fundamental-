from dataclasses import dataclass

@dataclass
class Order:
    id:int
    product:str
    price:float

@dataclass
class UserData:
    name:str
    age:float
    address:str
    salary:float
    email:str
    profile:dict
    skills:list[str]
    marks:list[list[int]]
    orders:list[Order]