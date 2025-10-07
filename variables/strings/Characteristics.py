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