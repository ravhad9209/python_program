# Creating Dictionary
Dict_0 = {}
Dict_1 = {'name':'vedant','no':91,'age':21}
Dict_2 = dict(name = 'rushi',age = 20 , city = 'pune')

print("empty Dictionary:",Dict_0)
print("Dictionary 1 (using{}):",Dict_1)
print("Dictionary 2 (using dict()):",Dict_2)

#Accessing Dictionary Items
print("------Accessing Dictionary Items------")
print("Dictionary 1 access name :",Dict_1["name"])
print("Dict 1 access name using (get);",Dict_1.get("name"))

#Adding Item Dictionery 
print("-----Adding Item Dictionery-----")
Dict_1["County"] = "India"
print("Updated Dictionary :", Dict_1)

#Removing Items from a Dictionary
print("-----Removing Items from a Dictionary-----")
del Dict_1["age"]
print("Delete Items from a Dictionary (age):",Dict_1)
Dict_1.pop("name")
print("pop Items from a Dictionary (name):",Dict_1)
Dict_1.popitem()
print("PopItem Items from a Dictionary:",Dict_1)
Dict_1.clear()
print("Clear Items from a Dictionary:",Dict_1)

#Changing Dictionary Items
print("-----Changing Dictionary Items-----")
Dict_2["city"] = "pune"
Dict_2["age"] = 25
print("Changing Dictionary Items (City):",Dict_2)

#Iterating Through a Dictionary
for key in Dict_2:
    value = Dict_2[key]
    print(key," -> ",value)

#Finding legth of Dictionary item
print("legth of item:",len(Dict_2))    