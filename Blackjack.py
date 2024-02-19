import main
import Slots
import config
import random
import time

def Blackjack():
    config.bet = int(input("How much would you like to bet? (Input 0 to pick a different game) "))
    if (config.bet == 0):
        Slots.pickGame()
    else:
        if (config.bet > config.balance):
            print("You don't have enough money to bet that much!")
            Blackjack()
        else:
            config.balance = config.balance - config.bet
            print("Your balance is now $" + str(config.balance))
            time.sleep(1)
            print("Dealing cards...")
            time.sleep(1)
            playerHand = [random.choice(config.cards), random.choice(config.cards)]
            dealerHand = [random.choice(config.cards), random.choice(config.cards)]
            print("Your hand: " + str(playerHand))
            time.sleep(1)
            print("Dealer's hand: " + str(dealerHand[0]) + ", ?")
            time.sleep(1)
            playerTurn = True
        while (playerTurn == True):
            if (input("Would you like to [h]it or [s]tay? ") == "h"):
                playerHand.append(random.choice(config.cards))
                print("Your hand: " + str(playerHand))
                time.sleep(1)
                if (sum(playerHand) > 21):
                    print("You busted! You lose.")
                    time.sleep(1)
                    print("Your balance is now $" + str(config.balance))
                    if (config.balance == 0):
                        print("You lost all your money! Game over.")
                        time.sleep(1)
                        print("Thanks for playing!")
                        time.sleep(1)
                        exit()
                    else:
                        Blackjack()
            else:
                playerTurn = False
        print("Dealer's hand: " + str(dealerHand))
        time.sleep(1)
        if (sum(dealerHand) > sum(playerHand) and sum(dealerHand) <= 21):
                print("Dealer wins.")
                time.sleep(1)
                print("Your balance is now $" + str(config.balance/2))
                if (config.balance == 0):
                    print("You lost all your money! Game over.")
                    time.sleep(1)
                    print("Thanks for playing!")
                    time.sleep(1)
                    exit()
                else:
                    Blackjack()
        else:
            while (sum(dealerHand) < 17):
                dealerHand.append(random.choice(config.cards))
                print("Dealer's hand: " + str(dealerHand))
                time.sleep(1)
                if (sum(dealerHand) > 21):
                    print("Dealer busted! You win.")
                    config.balance = config.balance + config.bet*2
                    time.sleep(1)
                    print("Your balance is now $" + str(config.balance))
                    if (config.balance == 0):
                        print("You lost all your money! Game over.")
                        time.sleep(1)
                if (sum(dealerHand) > sum(playerHand) and sum(dealerHand) <= 21):
                    print("Dealer wins.")
                    time.sleep(1)
                    print("Your balance is now $" + str(config.balance/2))
                    if (config.balance == 0):
                        print("You lost all your money! Game over.")
                        time.sleep(1)
                        print("Thanks for playing!")
                        time.sleep(1)
                        exit()
                    else:
                        Blackjack()