#Florence King'ori
#SCT211-0063/2022
totalbill = float(input("Total Bill: "))
tip =int(input("Tip percentage (10,12,15) of the bill: "))
diners=int(input("Number of customers: "))

tipamt = (tip * totalbill)/100
bill= totalbill + tipamt
individualbill = (bill)/diners
print("Each customer pays:",round (individualbill,2))



