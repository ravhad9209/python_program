## Set Operations in Python

set_A = {1,2,3,4,5}
set_B = {8,7,6,5,4}

#Union of Sets
print("Union method 1 = ",set_A|set_B)
print("Union method 2 =",set_A.union(set_B))
print("-" * 30)

#Intersection of Sets
print("Intersection method 1 = ",set_A & set_B)
print("Intersection method 2 = ",set_A.intersection(set_B))
print("-"*30)

#Difference of Sets
print("Difference method 1 = ", set_A - set_B)
print("Difference method 2 =", set_A.difference(set_B))
print("-"*30)

#Set Comprehension
set_1 = {i**3 for i in range (8)}
print("Set Comprehension method 1 = ", set_1)

set_2 = {r**2 for r in range (4)}
print("Set Comprehension method 2 = ", set_2)
print("-"*30)


#Frozenset in Python
set_z = frozenset(['one','two','three','four'])
print("Frozenset  =",set_z)
print("Frozenset Type = ",type(set_z))
print("-"*30)