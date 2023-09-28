name =input("Please input name:")
print("Hello", name ,"\nYour calculator is ready")
value1 =float( input("Input value 1: "))
value2 =float( input("Input value 2: "))
operator = input("Input operator (+ - *  / ): ")
if operator == "+":
    ans = value1 + value2

elif operator == "-":
    ans = value1 - value2

elif   operator == "*":
    ans = value1 * value2

elif operator == "/": 
    ans = value1 / value2

print("The result is: ",ans)


