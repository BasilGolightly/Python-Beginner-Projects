from random import randint

#game start boolean
game = True

#game while loop
while game == True:

    # choice array
    choice_array = ["Rock", "Paper", "Scissors"]

    # computer random choice
    computer = choice_array[randint(0, 2)]

    #player choice input
    player = input("Rock, Paper, Scissors? (You can also type 'exit' to quit the program)")

    #player choice is 'paper'
    if player == "Paper" :
        #computer choice is scissors
        if computer == "Scissors":
            print("You lost )= ; " + computer + " beat " + "Paper")
            continue

        #computer choice is 'Rock'
        elif computer == "Rock":
            print("You Won (= ; " + player + " beats " + "Rock")
            continue

        #computer choice is paper
        else:
            print("No one wins! Tie!")
            continue

    #player choice is same as computer choice
    elif player == computer:
        print("No one wins! Tie!")
        continue

    #player choice is rock
    elif player == "Rock":
        #computer choice is scissors
        if computer == "Scissors":
            print("You Won (= ; Rock beats " + computer)
            continue

        #computer choice is Paper
        elif computer == "Paper":
            print("You Lost )= ; " + computer + " beats Rock")
            continue

        #computer choice is rock
        else:
            print("No one wins! Tie!")
            continue

    #player choice is scissors
    elif player == "Scissors":
        #computer choice is rock
        if computer == "Rock":
            print("You lose )= ; " + computer + " beats Scissors")
            continue

        #computer choice is paper
        elif computer == "Paper":
            print("You win (= ; " + "Scissors beat " + computer )

        #computer choice is scissors
        else:
            print("No one wins! Tie!")
            continue

    #player input is exit
    elif player == "exit" or player == "Exit" or player == "EXIT" or player == "eXIT":
        print("Ok, have a nice day!")
        game = False

    #player input is not understood
    else:
        print("Did not understand input. Check for uppercase and lowercase letters (for example; Rock or Paper or Scissors)")
        continue