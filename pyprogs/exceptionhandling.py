#Florence King'ori
#SCT211-0063/2022
def  calc():
    name =input("Please input name:")
    print("Hello", name ,"\nYour calculator is ready.")
    try:
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
            if value2 == 0:
                raise ZeroDivisionError("Dividing by zero is invalid\n")
            ans = value1/value2
        else:
            raise ValueError("Invalid operation\n")
        print ("Answer", ans)
    except ValueError as Error:
        print(Error)  
        print("Try Again")   
    except ZeroDivisionError as Error:
        print(Error)
        print("Try Again")
calc()       