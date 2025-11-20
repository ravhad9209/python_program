# # ex
# n = lambda a : a + 13
# print("adding 7 ",n(7))

# #two number multiply

# m = lambda x , y : x*y
# print("multiply two numbers :",m(5,8))

# #check number even or odd 
# r = lambda x : "zero" if x == 0 else "even" if x % 2 == 0 else "odd" 
# print("check number even or odd :", r (12))


# n = [lambda x = a : x * 5 for a in range(1, 6)]

# for i in n :
#     print(i())

# n = lambda x:"Even" if x % 2 == 0 else "odd"

# print(n(15))
# print(n(2))
# print(n(0))

# factorial = lambda n: 1 if n==0 else n * factorial(n-1)

# num = int(input("Enter number:"))
# print(factorial(num))   


# #calculate multiple statement

# v = lambda x,y:(x+y,x-y,x*y,x/y)
# print(v(5,3))

#using lambda with filter

num = [2,7,4,3,8]
is_new = filter(lambda x : x % 2 == 0 ,num)
print(list(is_new))