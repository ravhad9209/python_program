#Accessing Characters
R = "tpoint tech"

print("Data Type:",type(R))

print("R[0]:", R[0])
print("R[8]:",R[8])

#Accessing String with Negative Indexing

print("R[-3]:",R[-3])
print("R[-7]:",R[-7])

#String Slicing
print("Number of Character:",len(R))
print("R[4:]", R[4:])
print("R[8:]:",R[8:])
print("R[:5]:",R[:5])
print("R[:9]:",R[:9])
print("R[:-1]",R[:-1])
print("R[::-1]",R[::-1])
print("R[2::6]",R[2::6])

#String Immutability
print("Given String:", R)
print("New String:","T"+R[1:7] + "T"+R[8:])

#Deleting a String
# del R
# print("Delete String:",R)

#Common String Methods
#len
Given_String = "Welcome"
print("Number of Character:",len(Given_String))

#upper() and lower()
print("UPPER:",Given_String.upper())
print("lower:",Given_String.lower())

#Strip

str_1 = "     Welcome To Disha    "

print("After removing space(Strip):", str_1.strip())

# Replasing
Str_2 = "Welcome to icon"

print("After Replasing 'icon' with 'Tpoint':",Str_2.replace("icon","Tpoint"))

#String Concatenation
x = "python"
y = "programming"
z = "language"

p = x +" " + y +" "+ z

print("Concatenation:", p)

#String Repetition

print("Repetition String:", x*5)

#F-String
Name = "String"
Language = "Python"
print(f'{Name} in {Language} is a sequence of characters.')

#String Membership Test
Given_String_1 = "Welcome"

print(f"'W' is exist in '{Given_String_1}'?", 'W'in Given_String_1)

print(f"'v' is not exist in '{Given_String_1}'? :", 'v'not in Given_String_1)