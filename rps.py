import random
computer = ["rock", "paper", "scissors"]
userwin = 0
compwin = 0

print ("\nThis is a game of rock paper scissors, first to 3 points wins!\n")

while userwin or userwin < 3:
    print ("Enter your guess (rock, paper, scissors): ")
    userguess = input("You: ").lower()
    compguess = random.choice(computer)

    if not userguess.isalpha() or userguess not in computer:
        print ("Oops, try again!\n")
        continue

    if userguess == "rock" and compguess == "paper" or userguess == "paper" and compguess == "scissors" or userguess == "scissors" and compguess == "rock":
        print ("Computer: " + compguess)
        compwin += 1
    if userguess == "rock" and compguess == "scissors" or userguess == "paper" and compguess == "rock" or userguess == "scissors" and compguess == "paper":
        print ("Computer: " + compguess)
        userwin += 1
    if compguess == userguess:
        print ("Computer: " + compguess)

    print ("SCORE    Player: " + str(userwin) + '       ' + "Computer: " + str(compwin) + "\n")
    
    if userwin == 3:
        print ("\nYou win!")
        quit()
    if compwin == 3:
        print ("\nYou lose!")
        quit()