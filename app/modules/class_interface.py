from typing import Protocol

class PaymentGetWay(Protocol):

    def anotherPay(self,amount:float)->float:
        ...