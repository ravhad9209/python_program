def print_factors(x):
    print(x)

    for i in range(1 , x + 1):
        if i % x == 0:
            print(i)

x = int(input("Enter the number :"))
print(print_factors(x))