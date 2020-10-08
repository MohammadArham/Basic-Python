import random
def spk(massege):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(massege)
ply_chns=1
rndm_nmbr=random.randint(0,99)
print("    $$$$$$ Mohammad  Arham $$$$$$")
spk("Presented By MOHAMMAD ARHAM")
print("          Number Guess Game")
spk("Number Guess Game")

while(ply_chns<=10):
    print(f"\n         ##### Turn  {ply_chns} #####")
    spk(f"turn {ply_chns}")
    spk("Guess")
    usr_guess_input=(input("   Guess the number:"))
    try:
        usr_guess=int(usr_guess_input)
        if usr_guess<rndm_nmbr:
            if ply_chns<10:
                print(f"   {usr_guess} is smaller, please guess a greater one")
                spk(f"{usr_guess} is smaller")
        elif usr_guess>rndm_nmbr:
            if ply_chns<10:
                print(f"   {usr_guess} is greater, please guess a smaller one")
                spk(f"{usr_guess} is greater")
        else:
            print("         ****** HURREY *****")
            spk("Congratulations")
            break
        try:
            lft_chns_logic=ply_chns;
            lft_chns=10-lft_chns_logic;
            if ply_chns<10:
                if ply_chns==9:
                    spk(f"You left {lft_chns} chance")
                else:
                    spk(f"   you left {lft_chns} chances")
        except Exception as f:
            pass
    except Exception as input_error:
        spk("oops!!!")
    ply_chns+=1
if ply_chns<=10:
    if ply_chns==1:
        print(f"   You complete in {ply_chns} chance")
        spk(f"Oh Nice, you complete in just {ply_chns} chance")
    else:
        print(f"   You complete in {ply_chns} chances")
        spk(f"Nice, you complete in {ply_chns} chances")
else:
    print(f"You loose, {rndm_nmbr} is the correct answer")
    spk(f"ooh, o! you loose, {rndm_nmbr} is the correct answer")
print("   Game Over")
spk("game over")
