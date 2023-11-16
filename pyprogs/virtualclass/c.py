class Student(object):
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print("Hi , my name is:", self.name)
    
    def add_weight(self,weight):
        self.weight = weight
    
    def change_name(self,name):
        self.name = name
s1 = Student("Flo")
s1.speak()
s1.add_weight(23)
s1.change_name("Mary")
print(s1.name)
print(s1.weight)

class Lecturer(Student):
    def __init__(self,name,course):
        super().__init__(name)
        self.course = course
    def teach(self):
        print("He's teaching",self.course)

lecturer1 = Lecturer("Mwai","comp sci")
print(lecturer1.name)
print(lecturer1.course)
lecturer1.teach()
lecturer1.speak()

class Worker(Lecturer):
    def __init__(self,name,course,department):
        super().__init__(name,course)
        self.department = department

worker1 = Worker("Jun","hospitality","spark")
print(worker1.department)
worker1.speak()



