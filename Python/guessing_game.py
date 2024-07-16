import random
range=int(input("Enter the range number : "))
guess=int(input("Enter a number between 1 to {} : ".format(range)))
answer = random.randint(1,range)
if(guess==answer):
    print("congo....you made it on the first guess")
else:
    while(guess!=answer):
        guess=int(input("guess again : "))
        if guess == answer:
            print("you got the correct guess finally")
        elif guess < answer:
            print("guess higher")
        else :
            print("guess lower")