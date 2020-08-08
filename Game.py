"""
Taking any number from user in can be (+ve)integer
no. of guesses
print no. of guesses left
No of guesses he took to finish
print the no. choosen by user is greater or smaller
At the end show the no.
Game Over
"""
import random
lo=1
n=random.randint(0,99)
while(lo<=10):
    a=int(input("Guess the number:"))
    if a<n:
        print(a," is smaller, please guess a greater one")
    elif a>n:
        print(a," is greater, please guess a smaller one")
    else:
        print("You choosed a correct one")
        break
    z=lo;
    y=10-z;
    print("you left",y,"chances")
    lo=lo+1
if z<10:
    print("congrats, you complete in",z+1,"chances")
else:
    print("You loose, ",n," is the correct answer")
print("Game Over")