#CS22B1093 ROHAN G

x = [] #forward declaration of list of students

def Physics_Excellent(x):
    count = 0
    for i in x:
        if i[1][0]=="Excellent":
            count+=1
        
    print(f"The count of students who got Excellent in Physics is : {count}")

def Chemistry_Good(x):
    count = 0
    for i in x:
        if i[1][1]=="Good":
            count+=1
        
    print(f"The count of students who got Good in Chemistry is : {count}")

def CS_Average(x):
    count = 0
    for i in x:
        if i[1][2]=="Average":
            count+=1
        
    print(f"The count of students who got Average in CS is : {count}")


def Physics_Excellent_Roll(x):
    print(f"The roll numbers of students who got Excellent in Physics is : ")
    for i in x:
        if i[1][0] == 'Excellent':
            print(f"{i[0]}")

print(f"Enter the student details : ")
for i in range(10):
    roll = input(f"Enter the roll number of the student {i+1} : ")
    grade = [i for i in input("Enter the grade in Physics, Chemistry, and CS (separated by comma) : ").split(',')[:3]]
    
    y = [roll,grade]
    x.append(y)

Physics_Excellent(x)
Chemistry_Good(x)
CS_Average(x)
Physics_Excellent_Roll(x)