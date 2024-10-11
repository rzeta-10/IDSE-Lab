#CS22B1093 ROHAN G

import pandas as pd

df = pd.read_csv('file2.csv')
print(df.head()) #print the first 5 entries in the dataframe
print('\n')
print(df.info()) #print the info about the data present in the csv file
print('\n')
print(df.to_string()) #converts the dataframe into string
print('\n')

# df1 = pd.read_csv('file2.csv')

df.drop_duplicates(inplace=True)#removes duplicate entries
df1 = df.copy()
print(df.to_string()) #no duplicates in the given csv file

df.dropna(subset=['Maths','Physics','Computerscience','Dept'],inplace=True) #drops rows with NaN values
print(df.to_string())
print(f"The number of rows after droping NaN value containing rows is : {df.shape[0]}")
print('\n')

#calculating mean of the df after dropping all rows with NaN values
x = df['Maths'].mean()
print(f"The mean of maths marks after removing NaN values : {x}")
y = df['Physics'].mean()
print(f"The mean of maths marks : {y}")
z = df['Computerscience'].mean()
print(f"The mean of maths marks : {z}")

print('\n')

#filling the NaN values with calculated mean (expected value)
df1['Maths'].fillna(x,inplace=True)
df1['Physics'].fillna(y,inplace=True)
df1['Computerscience'].fillna(z,inplace=True)

print(df1.to_string())

print('\n')
x = df1['Maths'].mean()
print(f"The mean of Maths marks after filling NaN values : {x}")
y = df1['Physics'].median()
print(f"The median of Physics marks after filling NaN values : {y}")
z = df1['Computerscience'].mode()
print(f"The mode of ComputerScience marks after filling NaN values : {z}")