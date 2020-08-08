"""
Exercist,4- Pattern Printing
input = integer n
Boolean = True or False
True n=4            False n=4
*                   ****
**                  ***
***                 **
****                *  
"""

"""
#Code developed by me 
inp=int(input("Enter a number:"))
boo=input("Enter \'0\' or \'1\':")
i=1
if(boo=='1'):
    while(i<=inp):
        print(i*"*")
        i+=1
if(boo=='0'):
    while(inp>=i):
        print(inp*"*")
        inp-=1
"""

try: # created  by taking hint
    fir=int(input("Enter a number:")) # Starting point without using try_except
    sec=int(input("Enter \'0\' or \'1\':"))
    new=bool(sec)
    if new==True:
        for i in range(1,fir+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    elif new==False:
        for i in range(fir,0,-1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    else:
        print("invalid Pattern") # ending point without using try_except
except Exception as e:
    print(e)
    print("Invalid value")