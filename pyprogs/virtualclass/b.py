class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

dog1 =Dog("Rex", 6)

print(dog1.name)
print(dog1.age)

class Cat:
  def __init__(self, species, color):
    self.species = species
    self.color = color

cat1 = Cat("Ragdoll","black")

print(cat1.species)
print(cat1.color)

class Husky(Dog):
  def __init__(self,origin,color):
    super().__init__(origin,color)
    self.sound = "woof"

husky = Husky("german","black","woof")
print(husky.age)
print(husky.origin)
print(husky.sound)