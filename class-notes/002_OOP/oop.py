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



# class Person:
#     company = "clarusway"
    
    
#     def test(self):
#         print("test")
        
    
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
        
#     def get_details(self):
#         print(self.name, self.age)
        
#     @staticmethod
#     def salute():
#         print("hı there!")
        
        
# person1 = Person()
# person2 = Person()
    
# person1.test()
# Person.test()

# person1.set_details("barry", 20)

# person1.get_details()

# print(person1.name) 

# person1.salute()
# Person.test(person1)  python arkada bu şekle dönüştürüyor ve o yüzden üstteki çalışmıyor.(arguman gönderdin diyor) def tanımlamasına self ekleyerek sorunu çözebiliriz.




#! special methods (init, str)

# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     def __str__(self):    #  print(person1) yaparsak ve str yoksa bize adresini ve nereden türedildiğini döndürür ama str varsa buradakileri döndürür. arka planda print(person1.__str__) çalışıyor.
        # return f"{self.name} - {self.age}"

# person1 = Person("victor", 32)   # init methodu sayesinde arguman gönderip direk oluşturabiliriz.
# person1.get_details()

# person2 = Person("selcuk", 22)
# person2.get_details()

# print(person1)



class Person:
    company = "clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def get_details(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, path):
        # self.name = name
        # self.age = age

        #! parent'taki attribute'ları super() metoduyla alabiliyoruz👇

        super().__init__(name, age)
        self.path = path

    #? Parent'taki metodu ihtiyacımız doğrultusunda overwrite ederek tekrardan tanımlamış olduk 👇
    def get_details(self):
        print(self.name, self.age, self.path)

emp1 = Employee("Victor", 32, "FS")

print(emp1) # Victor - 32

emp1.get_details() # Victor 32 FS






print("------------------------------------------------")




