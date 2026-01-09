import pandas as pd


print("Extract Data")

data={
    "Id":[101,102,103],
    "name":['komal','nikita','payal'],
    "age":[26,27,25]
}

df=pd.DataFrame(data)
print(df)