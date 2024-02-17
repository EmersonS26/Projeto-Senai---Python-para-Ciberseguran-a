import pandas as pd 

data = {"Nome" : ["Fulano1","Fulano2","Fulano3","Fulano4"],
        "Recorde": [99,98,95,90],
        "Pontos": [218,215,213,212]}

print(data)

df=pd.DataFrame(data)
print(df)
df

print(df.loc[0])

print(df.loc[[0,1]])

df=pd.DataFrame(data, index = ["Rank1","Rank2","Rank3","Rank4"])

print(df.info())

print(df)
df

df.describe()