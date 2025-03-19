#Rock paper scissor

import random

print("Winning rules for the game :- \n"
      + " Rock vs Paper = Paper wins\n"
      + " Paper vs Scissor = Scissor wins\n"
      + " Scissor vs Rock = Rock wins\n")

while True:
   print ("Select any of your hand \n 1) Rock\n 2) Paper\n 3) Scissor")
   choice = int(input("Enter your choice:- " ))

   while choice > 3 or choice < 1:
      choice = int(input("Enter a valid hand choice:- "))

   if choice == 1:
        choice_name = "Rock"
   if choice == 2:
        choice_name = "Paper"
   if choice == 3:
       choice_name = "Scissor"

   print("User choice is :\n", choice_name)
   print("Now it's computer's turn...\n")

   comp_choice = random.randint(1, 3)

   if comp_choice == 1:
      comp_choice_name = "Rock"
   if comp_choice == 2:
      comp_choice_name = "Paper"
   if comp_choice == 3:
      comp_choice_name = "Scissor"

   print("Computer choice is :", comp_choice)
   print(choice_name, 'vs' ,comp_choice_name)

   if choice == comp_choice:
      result = "DRAW"
   elif(choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
      result = "PAPER"
   elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
      result = "SCISSOR"
   elif (choice == 3 and comp_choice == 1) or (choice == 1 and comp_choice == 3):
      result = "ROCK"

   if result=="DRAW":
       print("---TIE---")
   elif result == choice_name:
       print("---You Wins")
   else:
       print("---Computer Wins---")

   print("Do you want to play again? : (Y/N)")
   ans=input().lower()
   if ans=='n':
        break


print("Thanks For Playing")
