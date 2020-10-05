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
ply_chns=1
rndm_nmbr=random.randint(0,99)
print("    $$$$$$ Mohammad  Arham $$$$$$")
print("          Number Guess Game")

while(ply_chns<=10):
    print(f"\n         ##### Turn  {ply_chns} #####")
    usr_guess_input=(input("   Guess the number:"))
    try:
        usr_guess=int(usr_guess_input)
        if usr_guess<rndm_nmbr:
            if ply_chns<10:
                print(f"   {usr_guess} is smaller, please guess a greater one")
            else:
                pass
        elif usr_guess>rndm_nmbr:
            if ply_chns<10:
                print(f"   {usr_guess} is greater, please guess a smaller one")
            else:
                pass
        else:
            print("         ****** HURREY *****")
            break
        try:
            lft_chns_logic=ply_chns;
            lft_chns=10-lft_chns_logic;
            if ply_chns<10:
                if ply_chns==9:
                    print(f"   you left {lft_chns} chance")
                else:
                    print(f"   you left {lft_chns} chances")
            else:
                pass
        except Exception as f:
            pass
    except Exception as input_error:
        print("   OOPS!!!")
    ply_chns+=1
    
if ply_chns<=10:
    if ply_chns==1:
        print(f"   You complete in {ply_chns} chance")
    else:
        print(f"   You complete in {ply_chns} chances")
else:
    print(f"You loose, {rndm_nmbr} is the correct answer")
print("   Game Over")