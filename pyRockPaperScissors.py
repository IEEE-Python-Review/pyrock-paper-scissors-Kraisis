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
    if 1 in sel:
        choice = "rock"

    if 2 in sel:
        choice = "paper"

    if 3 in sel:
        choice = "scissors"

    # print("The computer selected", choice)

    return choice


def Human():
    """
  This function should display a menu, prompting the player to select either rock, paper, or scissors and return what the player 
  selected IN LOWERCASE . If the player selects an invalid option, display the error message "Invalid Play"
  """

    print("1. Rock\n2. Papar\n3. Scissors\n\nChoose the number that corresponds with the move you want to make")
    sel = play()
    choice = "null"
    if sel is 1:
        choice = "Rock"
    if sel is 2:
        choice = "Papar"
    if sel is 3:
        choice = "Scissors"

    choice = sel.lower()
    return choice


def main():
    print("Welcome To PyRock Paper Scissors Best of 3\n")
    """
  This function should prompt the player to enter his/her name, get the player's and computer's play, displays what the player and the 
  computer played and displays who won. Remember this is a best of 3 match so this function should also keep track of who won each round 
  and displays the final scores and the overall winner.
  """

    player = input("Enter your name: ")

    for x in range(0, 50):
        hum = Human()
        print("Hum is: " + hum)
        comp = Computer()
        print(hum + "vs" + comp)

        compscore = 0
        humscore = 0

        if hum is "rock" and comp is "paper":
            compscore = compscore + 1
            print("Computer Won")
        if hum is "rock" and comp is "scissors":
            humscore = humscore + 1
            print("You Won")
        if hum is "rock" and comp is "rock":
            print("Tied, Try Again")

        if hum is "paper" and comp is "rock":
            humscore = humscore + 1
            print("You Won")
        if hum is "paper" and comp is "scissors":
            compscore = compscore + 1
            print("Computer Won")
        if hum is "paper" and comp is "paper":
            print("Tied, Try Again")

        if hum is "scissors" and comp is "paper":
            humscore = humscore + 1
            print("You Won")
        if hum is "scissors" and comp is "rock":
            compscore = compscore + 1
            print("You Won")
        if hum is "scissors" and comp is "scissors":
            print("Tied, Try Again")

        if humscore is 2:
            print(player + " score: " + str(humscore))
            print("Computer score: " + str(compscore))
            print(player + " won the best of 3 match")
            break

        if compscore is 2:
            print(player + " score: " + str(humscore))
            print("Computer score: " + str(compscore))
            print("Computer won the best of 3 match")
            break


if __name__ == '__main__':
    main()
