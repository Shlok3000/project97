num = 1
chances = 0


print("Guess a number 1-9")

while (chances < 5):
    chances + 1
    print("Guess")
if(guess == num):
    print("Congrats, you win")    
elif (chances > 5):
    print("Out of chances")
else:
    print("Incorrect number")

