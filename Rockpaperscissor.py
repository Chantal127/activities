from random import randint

t = ["Rock", "Paper", "Scissors"]
computer1 = 0
player1 = 0


while True:

    player = input("Rock, Paper, Scissors?\n")
    computer = t[randint(0, 2)]
    if player == computer:
        print("Tie!")
        print("Computer = " + str(computer1))
        print("Player= " + str(player1))
        continue
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer1 += 1
            print("Computer = " + str(computer1))
            print("Player = " + str(player1))
        else:
            print("You win!", player, "Smashes", computer)
            player1 += 1
            print("Computer = " + str(computer1))
            print("Player = " + str(player1))
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computer1 += 1
            print("Computer = " + str(computer1))
            print("Player = " + str(player1))
        else:
            print("You win!", player, "cut", computer)
            player1 += 1
            print("Computer = " + str(computer1))
            print("Player = " + str(player1))
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computer1 += 1
            print("Computer = " + str(computer1))
            print("Player = " + str(player1))
        else:
            print("You win!", player, "smashes", computer)
            player1 += 1
            print("Computer = " + str(computer1))
            print("Player = " + str(player1))
    else:
        print("Invalid. Check your spelling!")
    computer = t[randint(0, 2)]
    Quit = (input("Do you want to play again?"))
    if Quit in ["Yes", "y", "Y", "yes"]:
        pass
    elif Quit in ["No", "no", "n", "N"]:
        break
    else:
        b