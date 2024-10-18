# CS22B1093 ROHAN G

import pandas as pd
import numpy as np

df = pd.read_csv('Fitness.csv')

print(df.head())
print(df.info())
print(df.describe())

def pearson_coefficient(a,b):
    x = np.array(a)
    y = np.array(b)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = np.sum((y - y_mean) * (x - x_mean))
    denominator = np.sqrt(np.sum((x - x_mean) ** 2) * np.sum((y - y_mean) ** 2))
    return (numerator/denominator)
    # n = len(x)
    # x_mean = (x.sum())/n
    # y_mean = (y.sum())/n
    
    # r = 0
    # num = 0
    # deno = 0
    # for i in range(n):
    #     num += (x[i]-x_mean)*(y[i]-y_mean)
    #     deno += 
        
df_numeric = df.select_dtypes(include='int64')
print(df_numeric)

corr_matrix = df_numeric.corr()

for i in range(df_numeric.shape[1]):
    for j in range(df_numeric.shape[1]):
        c1 = df_numeric.columns[i]
        c2 = df_numeric.columns[j]
        x = df[c1]
        y = df[c2]
        r = pearson_coefficient(x,y)
        r_fn = corr_matrix[c1][c2]
        
        if r<0:
            print(f"Correlation between {c1} and {c2} is : {r:.2f} , -ve corr")
        elif r>0:
            print(f"Correlation between {c1} and {c2} is : {r:.2f} , +ve corr")
        else:
            print(f"Correlation between {c1} and {c2} is : {r:.2f} , no corr")
            
        if r_fn<0:
            print(f"Correlation between {c1} and {c2} is : {r:.2f} , -ve corr")
        elif r_fn>0:
            print(f"Correlation between {c1} and {c2} is : {r:.2f} , +ve corr")
        else:
            print(f"Correlation between {c1} and {c2} is : {r:.2f} , no corr")
        
        print("--------------------------------------------------------------")