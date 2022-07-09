# class Person:
#     id = 1
#     name = "Jhone"

# info = Person()
# print(info.name)



#******************* _init_ ***************

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is " + self.name)
        
p1 = Person("Jhone",30)
print(p1.name)
print(p1.age)

p1.myfunc()

#**********************

