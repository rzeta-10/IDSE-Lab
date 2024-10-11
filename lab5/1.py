#CS22B1093 ROHAN G
import pandas as pd

print("--------------------------")
value = [(10,27,32),(52,65,89),(10,55,74)]
var1 = pd.Series(value)
print(var1)

print("--------------------------")
marks = {"Raja": (550,624), "Fazil" : (380,526), "John" : (390,)}
var2 = pd.Series(marks)
print(var2)
print('\n')
print(var2[0:2])

print("--------------------------")
dataset = {
    'company': ["Maruti","Hyundai","Ford"],
    'car_name' : ["Baleno","Creta", "Ecosport"]
}

var3 = pd.DataFrame(dataset)
print(var3)
print(var3[0:2])
print(var3.loc[0:2])
print(var3.loc[1])
print("--------------------------")

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'Safetyranking': [3, 7, 2],
    'yearofmanufacutring':(2005,2001,1995)
}

var4 = pd.DataFrame(mydataset,index=["Car1","Car2",'Car3'])
print(var4)
print(var4.loc["Car1":"Car3"])
print(var4.to_string())
print("--------------------------")



