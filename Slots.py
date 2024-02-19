import main
import config
import random
import time


specialCharacters = ["|$|", "|%|", "|#|", "|&|", "|@|", "|!|", "|?|", "|=|", "|*|"]
JackpotCombinations = ["|$||$||$|", "|%||%||%|", "|#||#||#|", "|&||&||&|", "|@||@||@|", "|!||!||!|", "|?||?||?|", "|=||=||=|", "|*||*||*|"]

def slots():
    config.bet = int(input("How much would you like to bet? (Input 0 to pick a different game) "))
    if (config.bet == 0):
        pickGame()
    else:
        if (config.bet > config.balance):
            print("You don't have enough money to bet that much!")
            slots()
        else:
            config.balance = config.balance - config.bet
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
                config.balance = config.balance + config.bet*10
                time.sleep(1)
                print("Your balance is now $" + str(config.balance))
            if (combo[1] == combo[4] or combo[1] == combo[7] or combo[4] == combo[7]):
                print("No jackpot, but you get your bet back!")
                config.balance = config.balance + config.bet
            else:
                print("You lost! :(")
            time.sleep(1)
            print("Your balance is now $" + str(config.balance))
            if (config.balance == 0):
                print("You lost all your money! Game over.")
                time.sleep(1)
                print("Thanks for playing!")
                time.sleep(1)
                exit()
            else:
                slots()

#robust input. Works like a hub to lead to each game and back to the hub.
def pickGame():
    config.game = "0"
    while (config.game != "1"):
        config.game = input("Select a game: 1. Slots ")
        if (config.game == "1"):
            break
        print("Invalid input. Please try again.")
    if (config.game == "1"):
        slots()