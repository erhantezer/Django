import os
os.system('cls' if os.name == 'nt' else 'clear')

print("------------------------------------------------")
# def print_types(data):
#     for i in data:
#         print(i, type(i))
        
# test = [122, "victor", [1,2,3], (1,2,3), True, lambda x:x]
# print_types(test)   


# class Person:
#     name = "Victor"
#     age = 32

# person1 = Person()
# person2 = Person()

# person1.location = "Turkey"
#! Instance'larda yaptığımız değişiklikler diğer instance'ları etkilemez 👇
# print(person2.location) #* 'Person' object has no attribute 'location'

# person2.age = 25
# print(person1.age) # 32
# print(person2.age) # 25

#? İlk önce instance'a bakıyor. Orada yoksa class'a gidip bakıyor 👆



class Person:
    company = "clarusway"
    
    
    def test(self):
        print("test")
        
    
    def set_details(self, name, age):
        self.name = name
        self.age = age
        
    def get_details(self):
        print(self.name, self.age)
        
    @staticmethod
    def salute():
        print("hı there!")
        
        
person1 = Person()
person2 = Person()
    
# person1.test()
# Person.test()

person1.set_details("barry", 20)

person1.get_details()

print(person1.name) 

person1.salute()
# Person.test(person1)  python arkada bu şekle dönüştürüyor ve o yüzden üstteki çalışmıyor.(arguman gönderdin diyor) def tanımlamasına self ekleyerek sorunu çözebiliriz.


print("------------------------------------------------")




