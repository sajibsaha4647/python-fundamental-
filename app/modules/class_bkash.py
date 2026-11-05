from .class_abstract import Payment
from .class_interface import PaymentGetWay

class Bkash(Payment,PaymentGetWay):

    def pay(self, amount):
        totalAmount = amount
        print(f"Paid {amount} using Bkash")
        print(f"here new amount is {totalAmount}")

    def anotherPay(self,amount:float)->float:
        print(f"Another payment of {amount} using Bkash")
        return amount

    def newPayment(self,newValue):
            print(f"this was the new value here {newValue}")