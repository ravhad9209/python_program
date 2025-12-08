# class animal:
#     def __init__(self,cat,dog):
#         self.cat = cat
#         self.dog = dog 

#     def display(self):
#         print(f"animal{self.cat} {self.dog}")   

# a = animal("small", "big")
# print(a.cat) 
# a.display()       

class car:
    def __init__(self,brand,model,):
        self.brand = brand
        self._model = model

    def display(self):
        print(f"brand:{self.brand},model:{self._model}")

class electricCar(car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def Show(self):
        print(f"battery_capacity:{self.battery_capacity} kWH")

C = electricCar("tata","Top^",5000 )
C.Show()
print(C.brand)
print(C._model)

