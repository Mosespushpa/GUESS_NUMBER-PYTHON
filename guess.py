from art import logo
import random
import os
n = random.randint(1,100)
def restart():
    
    ch = input("Do you want to continue type 'y' or to exit 'n' : ")
    if(ch=='y'):
            os.system('cls')
            start()
    else:
            exit(0)
def guess(guess):
    if guess=='easy':
        att=10
        for i in range(1,att+1):
          if(i==1):
              print(f"you have {att} attempts to guess the number.")
          elif(i>1):
              print(f"you have {att} attempts remaining to guess the number.")
          m = int(input("make a guess: "))
          if(m==n):
              print(f"you guessed it {m}")
              att=att-1
              break
          elif(m>n):
              att=att-1
              print("too high")
              if(i==10):
                  print("Run-out of attempts")
          elif(m<n):
              att=att-1
              print("too loo")
              if(i==10):
                  print("Run-out of attempts")
        restart()
        
    elif guess=='hard':
        att=5
        for i in range(1,att+1):
          if(i==1):
              print(f"you have {att} attempts to guess the number.")
          elif(i>1):
              print(f"you have {att} attempts remaining to guess the number.")
          m = int(input("make a guess: "))
          if(m==n):
              print(f"you guessed it {m}")
              att=att-1
              break
          elif(m>n):
              att=att-1
              print("too high")
              if(i==5):
                  print("Run-out of attempts")
          elif(m<n):
              att=att-1
              print("too loo")
              if(i==5):
                  print("Run-out of attempts")
        restart()
    else:
        print("Please enter correct input")
        restart()

        
def start():
    print(logo)
    print("Guess the number from 1 to 100")
    diff = input("choose the diffculty type 'easy'or 'hard' : ")
    guess(diff)

start()
