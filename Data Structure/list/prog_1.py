l = [5,21,7,2,14,52,"two","one"]
new_list = ["five",12,9]

print("list:",l)

l.append("four")
print("append:",l)

l.extend(new_list)
print("extend:",l)

l.insert(3 , 19)
print("insert:",l)

l.remove(14)
print("remove:",l)

l.pop(-1)
print("pop:",l)

# l.clear()
# print('clear:',l)

del l (0)
print(l)