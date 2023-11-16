#FLORENCE KING'ORI
#SCT211-0063/2022
class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def Add(self):
        print("Sum:", self.num1 + self.num2)
    def Subtraction(self):
        print("Subtraction:", self.num1 - self.num2)    
    def Multiplication(self):
        print("Multiplication:", self.num1 * self.num2)  
    def Division(self):
        print("Division:", self.num1 / self.num2) 
    def Answer(self):
        print("Answer is:",self.ans)
num1 =float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
operator = input("Please insert operator:")

value = Calculator(num1,num2)
if operator == "+":
    ans = value.Add()

elif operator == "-":
    ans = value.Subtraction()

elif   operator == "*":
    ans = value.Multiplication()

elif operator == "/": 
    ans =value.Division


