#change string
p = str.upper("welcome to disha class")
q = str.lower("WELCOME TO DISHA CLASS")
r = str.title("tpoint")
s = str.capitalize("the following table shows the different methods")
t = str.swapcase("python is programming lang")

print("Upper case:",p)
print("Lower case:",q)
print("Title case:",r)
print("capitalize:",s)
print("Swapcase:", t)

#search and find subtring

text = """Python offers a wide range of built-in
 string methods in order for us to manipulate and process strings efficiently. 
 string in Python, is an immutable data type, therefore,
 all of these methods return a new string,
 keeping the original string unchanged."""

index = text.find("string")
print(f"find 'string': {index}")

index = text.rfind("string")
print(f"rfind 'string': {index}")

index = text.rindex("Python")
print(f"rindex 'Python':{index}")

index = text.count("string")
print(f"count 'string':{index}")

index = text.startswith("Python")
print(f"startswith 'Python': {index}") 

index = text.endswith("Python")
print(f"endswith 'Python': {index}") 

#split and join string
text_1 = "This method splits the string into a list"

