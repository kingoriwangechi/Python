#Florence King'ori
#SCT211-0063/2022
name =input("Please input name:")
print("Hello", name ,"\nYour calculator is ready.")
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

from datetime import date
today = date.today()
print(today)
year = int(input("Input your year of birth:"))
month =int( input("Input your month of birth:"))
day = int(input("Input your date of birth:"))
current_day = date.today().day
current_month = date.today().month
current_year = date.today().year
Age_day = current_day - day
Age_month = current_month - month
Age_year = current_year - year
date.today().year
date.today().month
date.today().day
print("year:",Age_year, "Month:",Age_month,"Day:", Age_day)




