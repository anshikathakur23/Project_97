import random

guess = input ("Enter your number")

def randint ():

    chances = 1
    number = random.randint (1,5)

#While loop to count the number of chances
    while chances < 5:

     if guess == number:
        print ("Congratulations. You won!!!")
        break

     if chances == 0:
        print ("You lose. The number is", number)
    
    chances = chances + 1

randint ()