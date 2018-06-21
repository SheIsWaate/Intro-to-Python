from random import randint
print("Let's Play Rock Paper Sciccors")
userchoice = raw_input("Choose rock, paper, scissors")
choice = randint(1,3)
if (choice == 1):
    computer = "rock"
elif (choice == 2):
    computer = "paper"
else:
    computer = "scisssors"
if(userchoice == computer):
    print("It's a tie")
elif(userchoice == "rock" and computer == "scissors"):
    print("You win!")
elif(userchoice == "rock" and computer == "paper"):
    print("Haha! I win!")
elif(userchoice == "paper" and computer == "scissors"):
    print("Haha! I win!")
elif(userchoice == "paper" and computer == "rock"):
    print("You win!")
elif(userchoice == "scissors" and computer == "paper"):
    print("You win!")
elif(userchoice == "scissors" and computer == "rock"):
    print("Haha! I win!")



