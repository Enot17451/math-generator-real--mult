from random import *

class RealNumber:

    def __init__(self):
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])
        number = randint(1, 11)
        mantissa = randint(0,2)
        self.number = f"0.{"0"*mantissa}{number}"

    def __str__(self):
        return f"{self.number}"

    def printMinusOnly(self):
        if self.sign == "+":
            return f"{self.number}"
        else:
            return f"{self.sign}{self.number}"

    def printWithSign(self):
        return f"{self.sign}{self.number}"

    def printNoSign(self):
        return f"{self.number}"


class RealMult:

    def __init__(self):
        self.a = RealNumber()
        self.b = RealNumber()

    def __str__(self):
        return f"{self.a} * {self.b}"

def nicePrint(str,needLen):
    needAdd = needLen - len(str)
    str += needAdd*" "
    print(str,end="")

n = 10
for i in range(n):
    for j in range(3):
        nicePrint(RealMult().__str__(),20)
    print()
