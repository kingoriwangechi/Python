a="Hello"
for x in a:
    print(x)
print("h" in a)
print("H" in a)
if "l" in a:
    print("present")
#slicing
print(a[2:3]) 
print(a[:3]) 
print(a[-4:-2]) 
   
print(a[0:]) 
name = "Flo, Shi"
print(name.split(","))
x=1
y=2
xy= "I want {} banana and {} apples"
new_xy = xy.format(x,y)
print(new_xy)
print("She said \"yikes\" to him")
print(len(a))
myDict={
    "name":"flo",
    "age":19,
    "gender": "female"
}
print(myDict)
print(myDict["gender"])
z = myDict.get("name")
print(z)
print(myDict.keys())
myDict["race"] = "black"
print(myDict.keys())
print(myDict.values())
print(myDict.items())
w=myDict.pop("gender")
print(myDict)
del myDict["name"]
print(myDict)

for c,d in myDict.items():
    print(c,d)





