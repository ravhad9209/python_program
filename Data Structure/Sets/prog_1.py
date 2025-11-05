simple_set = {2001,2002,2003,2004,2005,2006,2007}

print("Given set = ", simple_set)

# for num in simple_set:
#     print(num)

simple_set.add(2008)
print("add a single element :",simple_set)

simple_set.update({'num9','num10'})
print("add a multiple element :",simple_set)

# Removing Elements from the Set

simple_set.remove("num9")
print("remove element :", simple_set)

simple_set.discard("num11")
print("discard element :", simple_set)

simple_set.pop()
print("pop element:" , simple_set)

simple_set.clear()
print("clear element :" , simple_set)