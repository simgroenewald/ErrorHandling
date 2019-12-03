import random

game = True

while game == True:

    coinHeads = False
    coinTails = False

    for count in range (1,10):
        coinFlip = random.randint(1,2)

        if coinFlip == 1:
            coinHeads = True
        if coinFlip == 2:
            coinTails = True

        if coinFlip == True:
            print ("I win!")
            break
        if coinFlip == True:
            print ("You win!")
            break

