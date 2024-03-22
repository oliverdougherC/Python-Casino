import Slots
import Blackjack
import config
import random
import time

# Functions------------------------------------------------------------------------------------#

#Bugs:
# If user inputs a non-int for the bet value, the program will crash
#pickgame function ends program if user inputs random value (????)
#Dealer still wont 'hit' itself properly (>=17) and if player wins, program ends


#slot machine for initial gabmle balance if user chooses to do so
def initializeBalance():
    combination = (random.choice(config.specialCharacters) + random.choice(config.specialCharacters) + random.choice(config.specialCharacters))
    for n in range (30):
        print(random.choice(config.specialCharacters) + random.choice(config.specialCharacters) + random.choice(config.specialCharacters))
        time.sleep(0.01+n/100)
    time.sleep(1)
    print(combination)
    combo = list(combination)
    time.sleep(1)
    if (combination in config.JackpotCombinations):
        print("You won the jackpot!")
        config.balance = config.GWinIAmount
        time.sleep(1)
        print("Your balance is now $" + str(config.balance))
    if (combo[1] == combo[4] or combo[1] == combo[7] or combo[4] == combo[7]):
        print("No jackpot, but you won $1000!")
        config.balance = config.GNeutralIAmount
    else:
        print("You lost! You only get $300 :(")
        config.balance = config.GLoseIAmount


#----------------------------------------------------------------------------------------------#

print("Welcome to the Python Casino!")
time.sleep(1)
if (input("Would you like to [g]amble for you starting cash, or start with [$]800?") == "g"):
    print("Off to the races already I see!")
    time.sleep(1.5)
    print("Here we go!")
    time.sleep(1)
    initializeBalance()
    time.sleep(1)
    print("Your balance is now $" + str(config.balance))
else:
    config.balance = config.defaultIAmount
    print("Your balance is now $" + str(config.balance))

time.sleep(2)
print("Let's get started!")
time.sleep(1.5)
Slots.pickGame()
 







