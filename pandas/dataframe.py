# import pandas as pd 

# x = [ 'a' , 'b' , 'c' , 'd' ]

# abcd = pd.Series(x,index = [1,2,3,4])
# print(abcd[4])

import pandas as pd 
data = {
    "abcs" : ["x","Y","z"],
    "pqrs" : ["E","F","G"]

}

df = pd.DataFrame(data)
print(df.loc[2])