
# ************* string 

name = "jhone"
print("His name is "+ name)
print(name[3])
print(name.upper())      # or     print(name.lower())
print(name.islower())    # or      name.isupper() 
print(len(name))
print(name.index("o"))
print(name.replace("j","S"))


# *************** Numbers
age = 20
print("His age is ", age)

print(15 + 5)

#****************************
num = 123
print(str(num))

#************* Input ***************

user = input("Enter your Name :")
age = int(input("Enter your age :"))
print(user)

post = input("Enter your post :")
changePost = input("Change post :")
print(post.replace(post,changePost))
