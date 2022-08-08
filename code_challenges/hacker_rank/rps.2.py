import random


def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    r = random.randint(0,2)
    if r == 0:
        return "rock"
    elif r == 1:
        return "scissors"
    else:
        return "paper"


def rps():
    print("Welcome to Rock, Paper, Scissors!\n\n-----")
    
    play = True
    while play:
        player1 = choose_rps()
        player2 = choose_rps()
        print(f"\n\nplayer1 chose {player1}")
        print(f"player2 chose {player2}")
        
        if player1 == player2:
            print("\nit's a tie!\n\n-----")
        elif player1 == "rock" and player2 == "scissors":
            print("\nplayer1 WINS\n\n-----")
        elif player1 == "paper" and player2 == "rock":
            print("\nplayer1 WINS\n\n-----")
        elif player1 == "scissors" and player2 == "paper":
            print("\nplayer1 WINS\n\n-----")
        else:
            print("\nplayer 2 WINS\n\n-----")
        play = random.randint(0,1)
        
        
    print("\nThank you for playing!")
    

rps()