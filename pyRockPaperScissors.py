import random


def play():
    """
  This function simply returns the option the player selected.
  """

    selected = input()
    return selected


def Computer():
    """
  This function should simply return the computers SINGLE choice of rock, paper, or scissors IN LOWERCASE
  """
    choice = "null"
    sel = random.randint(1, 3)
    if sel is 1:
        choice = "rock"

    if sel is 2:
        choice = "paper"

    if sel is 3:
        choice = "scissors"

    # print("The computer selected", choice)

    return choice


def Human():
    """
  This function should display a menu, prompting the player to select either rock, paper, or scissors and return what the player 
  selected IN LOWERCASE . If the player selects an invalid option, display the error message "Invalid Play"
  """
    sel = 1
    choice = "null"

    while sel is 1 or 2 or 3:

        print("1. Rock\n2. Paper\n3. Scissors\n\nChoose the number that corresponds with the move you want to make")
        sel = play()

        if sel is '1':
            choice = "Rock"
            break

        if sel is '2':
            choice = "Paper"
            break

        if sel is '3':
            choice = "Scissors"
            break

        if sel is not 1 or 2 or 3:
            nope = "Invalid Play"
            print(nope)
            return nope

    choice = choice.lower()

    return choice


def main():
    print("Welcome To PyRock Paper Scissors Best of 3\n")
    """
  This function should prompt the player to enter his/her name, get the player's and computer's play, displays what the player and the 
  computer played and displays who won. Remember this is a best of 3 match so this function should also keep track of who won each round 
  and displays the final scores and the overall winner.
  """

    player = input("Enter your name: ")
    compscore = 0
    humscore = 0

    for x in range(0, 50):
        hum = Human()
        if hum == "Invalid Play":
            exit(0)

        comp = Computer()
        print("\n" + hum + " vs " + comp + "\n")

        if hum == "rock" and comp == "paper":
            compscore = compscore + 1
            print("Computer Won\n")
        if hum == "rock" and comp == "scissors":
            humscore = humscore + 1
            print("You Won\n")
        if hum == "rock" and comp == "rock":
            print("Tied, Try Again\n")

        if hum == "paper" and comp == "rock":
            humscore = humscore + 1
            print("You Won\n")
        if hum == "paper" and comp == "scissors":
            compscore = compscore + 1
            print("Computer Won\n")
        if hum == "paper" and comp == "paper":
            print("Tied, Try Again\n")

        if hum == "scissors" and comp == "paper":
            humscore = humscore + 1
            print("You Won\n")
        if hum == "scissors" and comp == "rock":
            compscore = compscore + 1
            print("Computer Won\n")
        if hum == "scissors" and comp == "scissors":
            print("Tied, Try Again\n")

        if humscore == 2:
            print(player + "'s score: " + str(humscore))
            print("Computer score: " + str(compscore))
            print(player + " won the best of 3 match")
            break

        if compscore == 2:
            print(player + "'s score: " + str(humscore))
            print("Computer score: " + str(compscore))
            print("Computer won the best of 3 match")
            break


if __name__ == '__main__':
    main()
