#CS22B1093 ROHAN G

dic = {} #forward declaration of dictionary


while True:
    choice = int(input("Choose one of the following options : \n1.Insert \n2.Delete \n3.Search \n4.Exit \n"))
    if(choice == 1):
        roll = input("Enter the roll number of the student : ")
        details = [i for i in input("Enter the name, CGPA and the mobile number of student (separated by comma) : ").split(',')[:3]]
        dic[roll] = details
    elif(choice == 2):
        roll = input("Enter the roll number of the student who should be removed from the database : ")
        if roll in dic.keys():
            dic.pop(roll)
            print(f"Successfully removed the roll number from database")
        else:
            print(f"Roll number not present in the database")
    elif(choice == 3):
        roll = input("Enter the roll number of the student whose details to be searched in database : ")
        if roll in dic.keys():
            print(f"The details of the student with roll number {roll} is :")
            print(f"Name : {dic[roll][0]}")
            print(f"CGPA : {dic[roll][1]}")
            print(f"Mobile Number : {dic[roll][2]}")
        else:
            print(f"Roll number not present in the database")
    elif(choice == 4):
        print(f"Exiting the program")
        break
    else:
        print(f"Invalid input. Try Again!")
    