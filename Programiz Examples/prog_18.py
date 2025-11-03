#  Print the Fibonacci sequence

a = 0 
b = 1
num = int(input("enter the number of fibonacci:"))
if num == 1:
    print(a)

else:
    print(a)
    print(b)
    for num in range(2, num):
        c = a+b
        a = b
        b = c
        print(c)