#Cameron Chromiak
#11-8
#simulates a bias die
import random

def rollDie(pseudoList):
    diceRoll = pseudoList[random.randint(0,10)] #or len(pseudoList)
    return diceRoll


def calcInfluence(infl, outcome):
    values = []
    for i in range(0,infl):
        values.append(outcome)
    remainingListLen = 10 - len(values)
    for i in range(0, remainingListLen):
        values.append(random.randint(1,7))
##    print(values) #for testing
    return values
        
def main():
    try:
        outcome = int(input("Die outcome (1-6): "))
        influence = int(input("Proabability 1-10: "))
    except ValueError:
        print("Must be positive integer")
        main()
        
    if influence in range(1,11):
        pseudoList = calcInfluence(influence, outcome)
    else:
        print("Probability must be between 1 and 10")
        main()
        
    if outcome in range(1,7):
        diceResult = rollDie(pseudoList)
    else:
        print("Die must be between 1 and 6")
        main()
    print(pseudoList)
    print(diceResult)
main()
