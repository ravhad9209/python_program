# class student:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def display(self,roll , city):
#         print(roll ,city)   

# a1 = student("abc",100)
# a1.display(101, "pune")         

class employer:
    def __init__(self,employe_count, name):
        self.employe_count = employe_count
        self.name = name 

    def new_employe_count(self):
        return self.employe_count  

    def new1_employe_count(self):
        return self.name 

e1 = employer(32 , "abcd")        
print(e1.new_employe_count())
print(e1.new1_employe_count())