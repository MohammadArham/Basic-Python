# Snake Water Gun
import random

def speech(massege):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(massege)
    
def choice(chois):
    if chois=="s":
        return "snake"
    elif chois=="w":
        return "water" 
    elif chois=="g":
        return "gun"
    
print("   $$$$$$ Mohammad Arham $$$$$$")
speech("Presented By MOHAMMAD ARHAM")
print("      (Snake,Water,Gun) Game")
speech("Welcome to snake water gun game")
speech("Enter your name")
player_name=input("   Enter Your Name:").upper()
print(f"## Welcome {player_name} to (Snake, Water, Gun) Game ##")
print("   lets Play")
speech(f"let's play {player_name}")
game_turn=1
draw_count=0
loose_count=0
win_count=0
while(game_turn<=10):
    cmputr_chois=random.choice(["s","w","g"])
    cmputr_choose=choice(cmputr_chois)
    print(f"\n    ****** Turn - {game_turn} ******")
    speech(f"turn {game_turn}")
    print(f"{player_name} Please choose: (s,w,g) for (snake,water,gun)")
    speech("choose")
    user_choice=input("  Enter your choice:").lower()
    user_choose=choice(user_choice)
    if user_choice=="s" or user_choice=="w" or user_choice=="g":  # code for snake
        if cmputr_chois==user_choice:
            print("  Match draw")
            speech("Draw")
            print(f"Computer was choosed {cmputr_choose}, and {player_name} you also choosed {user_choose}")
            draw_count+=1
        elif cmputr_chois=="s" and user_choice=="w" or cmputr_chois=="w" and user_choice=="g" or cmputr_chois=="g" and user_choice=="s":
            print(f"  You Loose {player_name}")
            speech("you loose")
            print(f"Computer was choosed {cmputr_choose}, and {player_name} you choosed {user_choose}")
            loose_count+=1
        elif cmputr_chois=="s" and user_choice=="g" or cmputr_chois=="w" and user_choice=="s" or cmputr_chois=="g" and user_choice=="w":
            print(f"  You Win {player_name}")
            speech("you win")
            print(f"Computer was choosed {cmputr_choose}, and {player_name} you choosed {user_choose}")
            win_count+=1         
    else:
        print(f" OOPS! {player_name} you entered wrong input, read carfully.")
        speech("oops, careful")
    if game_turn<=9:
        print(f"  {10-game_turn}  chances left")
    game_turn+=1
print(f"\n\n        ##### Game Summery #####")
print(f"{player_name} you wins {win_count} times and you loose {loose_count} times")
print(f"       And {draw_count} times match was draw")
print(f"    Your score is: {win_count*10} out of 100. and,")
print(f"     Computer score is: {loose_count*10} out of 100")
if win_count>loose_count:
    print(f"           ***** HURREY *****")
    speech("Congratulations")
    print(f"        {player_name} you are the winner")
elif win_count<loose_count:
    print("      Oops, you loose the game")
else:
    print("      Draw Match")
print("      Game Over")
speech("game over")    