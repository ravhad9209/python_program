# SampleTuples = ("vivek","vedant","mayur","anya","rohit")

# print("SampleTuples[1]:",SampleTuples[1])
# print("SampleTuples[4]:",SampleTuples[4])
# print("SampleTuples[-2]",SampleTuples[-2])
# print("SampleTuples[-3]",SampleTuples[-3])

# # Slicing in Tuple

# SampleTuples = ("vivek","vedant","mayur","anya","rohit","anand")

# print("SampleTuples 1 to 5:",SampleTuples[1:5])

# print("SampleTuple 0 to -3:",SampleTuples[0:-3])

# print("SampleTuple:",SampleTuples[:])

# # Deleting a Tuples
 
# SampleTuples = ("vivek","vedant","mayur","anya","rohit","anand")

# print("Given SampleTuples:",SampleTuples)

# try:
#     del SampleTuples[4]
#     print(SampleTuples)
# except Exception as e:
#     print(e)    

# # Changing the Elements in Tuple

SampleTuples = ("vivek","vedant","mayur","anya","rohit","anand")
print("SampleTuple:",SampleTuples)

NameTuple = list(SampleTuples)
print("NameTuple:",NameTuple)

NameTuple[1] = "sarvesh"
print("NameTuple second name change:",NameTuple)

# Adding Elements to a Tuple

NameTuple.append("sai")
print("NameTuple Adding Element:",NameTuple)

# Adding a Tuple to a Tuple

new_NameTuple = ("magic",)

NameTuple += new_NameTuple

print("Adding a NameTuple to a new_NameTuple:",NameTuple)