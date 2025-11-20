
import calculator_1 as c

print("plese select your opration")
print("1.add")
print("2.sub")
print("3.milti")
print("4.divide")

select =int(input("select opration 1-4 "))
x= int(input("Enter the number 1 :"))
y = int(input("Enter the number 2 :"))


if select == 1:
    print(c.add(x,y))

elif select == 2:
    print(c.sub(x,y))

elif select == 3 :
    print(c.multi(x,y))

elif select == 4 :
    print(c.divide(x,y))

else:
    print("invalid input")
