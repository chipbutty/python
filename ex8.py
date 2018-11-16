#"Rock, Paper, Scissors - ex.8"
#"rock beats scissors, scissors beats paper, paper beats rock"
import random
choice = ['rock', 'paper', 'scissors']
a = int(input('Enter the number of game trials:'))
x= 0
while (a > 0):
   x += 1
   print("Game trial #" , x)
   play1 = random.choice(choice)
   play2 = random.choice(choice)
   print (play1, play2)
   def compare(play1, play2):
       if(play1 == play2):
           return ("It's a tie")
       elif play1 == 'rock':
           if play2 == 'scissors':
               return ("Rock wins!")
           else:
               return("Paper wins!")
       elif play1 == 'scissors':
           if play2 == 'paper':
               return("Scissors wins!")
           else:
               return("Paper wins!")
       elif play1 == 'paper':
           if play2 == 'rock':
              return("Paper wins!")
           else:
              return("Scissors wins!")
       else:
           return ("Invalid input! try again")
   print (compare(play1, play2), "\n")
   a -= 1
