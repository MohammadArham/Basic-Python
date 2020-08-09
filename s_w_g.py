# Snake Water Gun
import random
print("(Snake,Water,Gun) Game")
nam=input("Enter Your Name:")
nam1=nam.upper()
print(f"Welcome {nam1} to (Snake, Water, Gun) Game")
print("lets Play")
wil=1
x=0
y=0
z=0
while(wil<=10):
    ran=random.choice(["s","w","g"])
    print(f"\n****** Turn - {wil} ******")
    print(f"{nam1} Please choose: s for snake, w for water, g for gun")
    inp1=input("Enter your choice:")
    inp1=inp1.lower()
    if ran=="s":  # code for snake
        if ran==inp1:
            print("Match draw")
            print(f"Computer was choosed snake, and {nam} you also choosed snake")
            x+=1
        elif inp1=="w":
            print(f"You Loose {nam}")
            print(f"Computer was choosed snake, and {nam} you choosed water")
            y+=1
        elif inp1=="g":
            print(f"You Win {nam}")
            print(f"Computer was choosed snake, and {nam} you choosed gun")
            z+=1
        else:
            print(f"ohoo! {nam1} wrong input read carfully")
    elif ran=="w":  # code for water
        if ran==inp1:
            print("Match draw")
            print(f"Computer was choosed water, and {nam} you also choosed water")
            x+=1
        elif inp1=="g":
            print(f"You Loose {nam}")
            print(f"Computer was choosed water, and {nam} you choosed gun")
            y+=1
        elif inp1=="s":
            print(f"You Win {nam}")
            print(f"Computer was choosed water, and {nam} you choosed snake")
            z+=1
        else:
            print(f"ohoo! {nam1} wrong input read carfully")
    elif ran=="g":  # code for gun
        if ran==inp1:
            print("Match draw")
            print(f"Computer was choosed gun, and {nam} you also choosed gun")
            x+=1
        elif inp1=="s":
            print(f"You Loose {nam}")
            print(f"Computer was choosed gun, and {nam} you choosed snake")
            y+=1
        elif inp1=="w":
            print(f"You Win {nam}")
            print(f"Computer was choosed gun, and {nam} you choosed water")
            z+=1
        else:
            print(f"ohoo! {nam1} wrong input read carfully")
            break
    if wil<=9:
        print(f"{10-wil}  chances left")
    wil+=1
print(f"\n\n##### Game Summery #####")
print(f"{nam1} you wins {z} times and you loose {y} times")
if z>y:
    print(f"Congratulations {nam1} you are winner")
elif z<y:
    print("Oops, you loose the game")
else:
    print("Draw Match")