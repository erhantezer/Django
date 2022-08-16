import os
os.system('cls' if os.name == 'nt' else 'clear')

print("------------------------------------------------")
def print_types(data):
    for i in data:
        print(i, type(i))
        
test = [122, "victor", [1,2,3], (1,2,3), True, lambda x:x]
print_types(test)   



  

print("------------------------------------------------")




