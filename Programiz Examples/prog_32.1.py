import prog_32 as a
a1 = int(input("Enter the number :"))

if a1 <= 0:
    print("positive intiger ")

else :
    print("Fibonacci Sequence" )
    for i in range(a1):
        print(a.fibo_rec(i))

