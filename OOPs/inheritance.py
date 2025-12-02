# #single inheritance
# class clg:
#     def roll(self):
#         print("103")

# class tech(clg):
#     def sir(self):
#         print("Anand")

# c = tech()
# c.sir()
# c.roll()

# #muliple inheritance
# class Grand_Father:
#     def Abc(self):
#         print("Grand Father")

# class Father(Grand_Father):
#     def Pqr(self):
#         print("Father ")

# class child(Father):
#     def Xyz(self):
#         print("Child")

# F = child()
# F.Xyz()
# F.Pqr()
# F.Abc()                 

# (sub,sup)
class cal:
    def add(self, a, b):
        return a+b;
    
class cal_2:
    def mul(self, a, b):
        return a*b;

class divide(cal,cal_2):
    def div(self,a,b):
        return a/b;

d = divide()
# print(d.div(10,5))
# print(d.mul(2,4))
# print(d.add(10,10))    

# print(issubclass(divide,cal_2))  
# print(issubclass(cal,cal_2))      

print(isinstance(cal,divide))
print(isinstance(d,divide))