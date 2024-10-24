import random
Option = ["Rock" , "Paper" , "Scissors"]


user =  input(f"Choose only one!{Option}\n ").capitalize()
input2 = print("Your Choose :", user)

Computer_choice = random.choice(Option)
print("The Computer chose :",Computer_choice)

if user == Computer_choice:
 print("Game Tied!")
elif user == "Rock" and Computer_choice == "Scissors":
 print("You won the Game!")
elif user == "Paper" and Computer_choice == "Rock":
 print("You Won the Game!")
elif user == "Scissors" and Computer_choice == "Paper":
 print("You Won the Game!")
else:
 print("Computer !")

