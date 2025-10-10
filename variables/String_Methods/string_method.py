#change string
print("change string:")

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
print("-" * 30) 

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
print("-" * 30) 

#split and join string
text_1 = "This method splits the string into a list"
Split_str = text_1.split()
print("String Split:",Split_str)

rsplit_str = text_1.rsplit(" ", 2)

print("rstring String:", rsplit_str)

partition_str = text_1.partition("simple")
print("partition String:", partition_str)

list_str = ["Tpoint", "Tech", "offers", "best", "tutorials", "to", "learn", "Python"] 
joinded_str = " ".join(list_str)
print("joinded String:", joinded_str)
 
joinded_str_underscore = " _ ".join(list_str)
print("joinded_str_underscore:",joinded_str_underscore)
print("-" * 30) 

#Validate Strings
validate_string = "Welcome"

print(f"Given String: {validate_string}")

a = str.isalpha(validate_string)
print("Is alphabetic :" ,a)  

b = str.isdigit(validate_string)
print("Is digit:",b)  

c = str.isalnum(validate_string)
print("Is alphanumeric:",c)  

d = str.isspace(validate_string)
print("Is space :", d)  

e = str.islower(validate_string)
print("Is lowercase:",e) 

f = str.isupper(validate_string)
print("Is uppercase :", f)  

g = str.istitle(validate_string)
print("Is titlecase:",g)  
print("-" * 30)  

# #Alignment and Formatting
str_5 = "Avhad anvlljj"

print("rjust:",str_5.rjust(10,"+"))
print("ljust:",str_5.ljust(10, '-'))      
print("center:",str_5.center(10, '-'))






