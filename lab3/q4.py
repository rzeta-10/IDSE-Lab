#CS22B1093 ROHAN G

tup = (("Khan", "Mahesh", "Sarath"), ("Yellow", "'Pink'", "Orange"), ("Watermelon", "'Mango'", "'Lemon'"))

print(f"The tuple is : {tup}")
search = input("Enter the element to be searched : ")
flag = False
for i in tup:
    for j in i:
        if j==search:
            flag = True
            print(True)
        
if(not flag):
    print(False)
    