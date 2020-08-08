# Snake Water Gun
import random
print("(Snake,Water,Gun) Game")
wil=1
x=0
y=0
z=0
while(wil<=10):
    ran=random.choice(["s","w","g"])
    print(f"\n****** Turn - {wil} ******")
    print("Please, choose: s for snake, w for water, g for gun")
    inp1=input("Enter your choice:")
    inp1=inp1.lower()
    if ran=="s":  # code for snake
        if ran==inp1:
            print("Match draw")
            print("Computer was choosed snake, and you also choosed snake")
            x+=1
        elif inp1=="w":
            print("You Loose")
            print("Computer was choosed snake, and you choosed water")
            y+=1
        elif inp1=="g":
            print("You Win")
            print("Computer was choosed snake, and you choosed gun")
            z+=1
        else:
            print("ohoo! wrong input read carfully")
    elif ran=="w":  # code for water
        if ran==inp1:
            print("Match draw")
            print("Computer was choosed water, and you also choosed water")
            x+=1
        elif inp1=="g":
            print("You Loose")
            print("Computer was choosed water, and you choosed gun")
            y+=1
        elif inp1=="s":
            print("You Win")
            print("Computer was choosed water, and you choosed snake")
            z+=1
        else:
            print("ohoo! wrong input read carfully")
    elif ran=="g":  # code for gun
        if ran==inp1:
            print("Match draw")
            print("Computer was choosed gun, and you also choosed gun")
            x+=1
        elif inp1=="s":
            print("You Loose")
            print("Computer was choosed gun, and you choosed snake")
            y+=1
        elif inp1=="w":
            print("You Win")
            print("Computer was choosed gun, and you choosed water")
            z+=1
        else:
            print("ohoo! wrong input read carfully")
    print(f"{10-wil}  chances left")
    wil+=1
print(f"Draw:{x}  Loose:{y}   Win:{z}")