#Florence King'ori
#SCT211-0063/2022
year = int(input("Year:"))
if( (year % 4 == 0) and
    (year % 100 != 0) or
        (year % 400 == 0)) :
             print(year,"is a leap year")
        
else:
    print(year,"is not a leap year")