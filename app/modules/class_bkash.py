from .class_abstract import Payment
from .class_interface import PaymentGetWay
from .class_final import FinalClass
from .class_context_manager_gc import Database

class Bkash(Payment,PaymentGetWay,FinalClass):

    def pay(self, amount):
        totalAmount = amount
        print(f"Paid {amount} using Bkash")
        print(f"here new amount is {totalAmount}")

    def anotherPay(self,amount:float)->float:
        print(f"Another payment of {amount} using Bkash")
        return amount

    def newPayment(self,newValue):
            print(f"this was the new value here {newValue}")

    def save(self):
        with Database() as db:
            print("Saving student to the database")
    
    def __del__(self):
        print("Object finalized")