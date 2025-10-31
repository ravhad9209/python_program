# Find the Factorial of a Number

num = int(input("enter the number:"))

fact = 1

if num < 0:
    print("fact are does not exist")

if num == 0:
    print("fact 0 is ",1)

if num > 0:
    for i in range(1 , num+1):
        fact = fact*i

print(fact)
