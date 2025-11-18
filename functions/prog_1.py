# # abs functions
# integer = -29
# print("remove negetive sign",abs(integer))

# integer_2 = 36
# print(abs(integer_2))
# print("_"*30)

# # all functions

# new_value = [0,False, 23]
# print(all(new_value))

# new_1 = [False , 54]
# print(all(new_1))

# new = [34, -32]
# print(all(new))

# #bin function
# a = 54
# print(bin(a))

# # bool function
# print("--- give values true or false ---")
# abc = []
# print(bool(abc))

# abcd = [23]
# print(bool(abcd))

# # callable function 

# a = 12
# print("check fuction or not = ",callable(a))

#compile code
code_str = 'a=7\nb=5\nprint("sum = ",a+b)'
code = compile(code_str,'sum.py','exec')
print(type(code))
exec(code)
# exec(a)

#exec() function
y = 13
exec('print(y==13)')
exec('print(y+5)')

#sum() function 
x = sum([3,2,5])
print(x)

z = sum([4,3,5],15)
print(z)

