# Health Management System
def getdate():
    import datetime
    return datetime.datetime.now()
print("Are you want to retrieve or log the plan")
print("1. for log")
print("2. for retrieve")
inp3=int(input("Enter you choice:"))
print("Select Name")
print("1. for Harry")
print("2. for Jarry")
print("3. for Marry")
inp1=int(input("Enter S.no.:"))
print("Select your Plan")
print("1. for Exercise")
print("2. for Diet")
inp2=int(input("Enter S.no.:"))
if inp3==1:
    if inp1==1:
        if inp2==1:
            w=input("Enter Exercise:")
            f=open("harry_exer.txt","a")
            f.write(str(getdate()))
            try:
                f.write(w)
                print("Successfully Writen")
            except Exception as ex:
                print(ex)
            f.close()
        elif inp2==2:
            w=input("Enter Diet:")
            f=open("harry_dit.txt","a")
            f.write(str(getdate()))
            f.write(w)
            print("Successfully Writen")
            f.close()
        else:
            print("sorry, you can only lock exercise or diet")
    elif inp1==2:
        if inp2==1:
            w=input("Enter Exercise:")
            f=open("jarry_exer.txt","a")
            f.write(str(getdate()))
            f.write(w)
            print("Successfully Writen")
            f.close()
        elif inp2==2:
            w=input("Enter Diet:")
            f=open("jarry_dit.txt","a")
            f.write(str(getdate()))
            f.write(w)
            print("Successfully Writen")
            f.close()
        else:
            print("sorry, you can only lock exercise or diet")
    elif inp1==3:
        if inp2==1:
            w=input("Enter Exercise:")
            f=open("marry_exer.txt","a")
            f.write(str(getdate()))
            f.write(w)
            print("Successfully Writen")
            f.close()
        elif inp2==2:
            w=input("Enter Diet:")
            f=open("marry_dit.txt","a")
            f.write(str(getdate()))
            f.write(w)
            print("Successfully Writen")
            f.close()
        else:
            print("sorry, you can only lock exercise or diet")
    else:
        print("Sorry, this is not in a list")
elif inp3==2:
    if inp1==1:
        if inp2==1:
            f=open("harry_exer.txt")
            re=f.read()
            print(re,"\n")
            print(f)
            f.close()
        elif inp2==2:
            f=open("harry_dit.txt")
            re=f.read()
            print(re,"\n")
            f.close()
        else:
            print("Sorry, this is not in the list")
    if inp1==2:
        if inp2==1:
            f=open("jarry_exer.txt")
            re=f.read()
            print(re,"\n")
            print(f)
            f.close()
        elif inp2==2:
            f=open("jarry_dit.txt")
            re=f.read()
            print(re,"\n")
            print(f)
            f.close()
        else:
            print("Sorry, this is not in the list")
    if inp1==3:
        if inp2==1:
            f=open("marry_exer.txt")
            re=f.read()
            print(re,"\n")
            print(f)
            f.close()
        elif inp2==2:
            f=open("marry_dit.txt")
            re=f.read()
            print(re,"\n")
            print(f)
            f.close()
        else:
            print("Sorry, this is not in the list")
else:
    print("Thanks for using") 