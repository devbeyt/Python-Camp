#******************** 1 ***********************

def  productAdded(name):
    print("Added product :" + name)


productAdded("Notebook")

#********************** 2 ****************************

def getAll(id,name):
    print("Product id :",id, " / " + "Product Name :" + name)

getAll(1,"Phone")
getAll(2,"Table")

#******************** 3 ************************

def login(*values):
    print("Your name  :" + values[0] + " / " + "password :", values[1])

login("Jhone",123457)



#********************* 4 ******************


name = input("Enter your userName :")
password = input("Enter your password :")

def register(name,password):
    print("Your username and password is :" + name + " " + password)


register(name,password)