import os
os.system('cls' if os.name == 'nt' else 'clear')

print("------------------------------------------------")
# def print_types(data):
#     for i in data:
#         print(i, type(i))
        
# test = [122, "victor", [1,2,3], (1,2,3), True, lambda x:x]
# print_types(test)   


class Person:
    name = "Victor"
    age = 32

person1 = Person()
person2 = Person()

# person1.location = "Turkey"
#! Instance'larda yaptığımız değişiklikler diğer instance'ları etkilemez 👇
# print(person2.location) #* 'Person' object has no attribute 'location'

person2.age = 25
print(person1.age) # 32
print(person2.age) # 25

#? İlk önce instance'a bakıyor. Orada yoksa class'a gidip bakıyor 👆

print("------------------------------------------------")




