cities = [ "Istanbul","Nyu York","London","Paris",True,153]
values = list(("Istanbul","Nyu York","London","Paris",True,153))
print(cities[0])
print(cities[0][3])
print(cities[1:])
cities[1] = "Ankara"
print(cities)
print(len(cities))
print(values)
print(type(values))
print(type(cities))

#******************   List Methods ******************
list1 = [1,2,3]
list2 = ["Kanada","Australia","Norvec"]
list1.extend(list2)
print(list1)
list1.insert(1,155)
print(list1)

list2.append("Brazilia")
list2.reverse()
list2.remove("Norvec")
print(list2.index("Australia"))
#   list2.clear()
print(list2)
list2.pop()

list3 = list2.copy()
print(list3)


#****************** 2D lists *******************

my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for lists in my_list:
    for row in lists:
        print(row)

