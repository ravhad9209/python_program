# class animal:
#     def dog(self):
#         pass

# class animals2:
#     def dog(self):
#         return 'abc'

# A = animals2()
# print(A.dog())

class vehical:
    def start(self):
        pass

    def end(self):
        pass

class car(vehical):
    def start(self):
        return "go Abc"
    
    def end(self):
        return "stop"
    
V = car()
print(V.start())
print(V.end())