import random
import math
import pr1testing
random.seed()


def roll(): #function that rolls 1 6-sided die, returning an integer between 0 and 5
    return random.randint(0,5)

def play():
    player1 = input("Name of Player 1?")
    player2 = input("Name of Player 2?")
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player1 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player2 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplayLoud(strat1, strat2):
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print("Player 1" + ": " + str(score1) + "   " + "Player 2" + ": " + str(score2))
        print('It is', "Player 1" + "'s turn.")
        numDice1 = strat1(score1, score2, False)
        diceTotal = 0
        diceString = ""
        i = numDice1
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print(str(numDice1), "dice chosen.")
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice1 == 0:
            last = True
        print()
        print("Player 1" + ": " + str(score1) + "   " + "Player 2" + ": " + str(score2))
        print('It is', "Player 2" + "'s turn.")
        numDice2 = strat2(score2, score1, False)
        diceTotal = 0
        diceString = ""
        i = numDice2
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print(str(numDice2), "dice chosen.")
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice2 == 0:
            last = True
    print("Player 1" + ": " + str(score1) + "   " + "Player 2" + ": " + str(score2))
    if score1 > 100:
        print("Player 2" + " wins.")
        return 2
    elif score2 > 100:
        print("Player 1" + " wins.")
        return 1
    elif score1 > score2:
        print("Player 1" + " wins.")
        return 1
    elif score2 > score1:
        print("Player 2" + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplay(strat1, strat2):
    score1 = 0
    score2 = 0
    last = False
    while True:
        numDice1 = strat1(score1, score2, last)
        diceTotal = 0
        i = numDice1
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice1 == 0:
            last = True
        numDice2 = strat2(score2, score1, last)
        diceTotal = 0
        i = numDice2
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice2 == 0:
            last = True
    if score1 > 100:
        return 2
    elif score2 > 100:
        return 1
    elif score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 3

def manyGames(strat1, strat2, n):
    num = n // 2
    player_1 = 0
    player_2 = 0
    tie = 0
    for _ in range(num):
        results_game = autoplay(strat1, strat2)
        if results_game == 1:
            player_1 += 1
        elif results_game ==2:
            player_2 += 1
        elif results_game == 3:
            tie += 1
    for _ in range(num, n):
        results_game = autoplay(strat2, strat1)
        if results_game == 1:
            player_2 += 1
        elif results_game ==2:
            player_1 += 1
        elif results_game == 3:
            tie += 1
    print("Player 1 wins: ", str(player_1) + "\n" + "Player 2 wins: ", str(player_2) + "\n" + "Ties:          ", str(tie))
    

def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
        return 12

def sample2(myscore, theirscore, last):
    if myscore <= 50:
        return 30
    elif myscore <= 80:
        return 10
    else:
        return 0

def improve(strat1):
    def new_strat(myscore, theirscore, last):
        if myscore == 100:
            return 0
        else:
            return strat1(myscore, theirscore, last)
    return new_strat

def myStrategy(myscore, theirscore, last):
    # I build my model based on expectation and probabilities
    # For the normal die, the expected value is 3.5 
    # For this die in question, the expected value is 2.5
    # The average of these two is 3
    # So I just played around these figures to scale the number of dies I roll
    # You'll realise that I've used 3.5 and 3.3 mostly, because 2.5 mostly get me above 100
    # My main concern in my strategy is my distance from 100 and how accurate I can get to it without going above it
    
    roll = 0
    if myscore == 0:
        roll = 33
    
    elif myscore == 100:
        roll = 0
    
    elif myscore >= 97:
        if theirscore > myscore:
            roll = (100 - myscore) // 3
        else:
            roll = (100 - myscore) // 3.5
    
    elif myscore >= 90:
        if myscore >= theirscore:
            if (myscore - theirscore) >= 7:
                roll = (100 - myscore) // 3.5
            elif (myscore - theirscore) >= 3:
                 roll = (100 - myscore) // 3.3
            elif (myscore - theirscore) >= 1:
                roll = (100 - myscore) // 3.3
            else:
                roll = (100 - myscore) // 3.5
        
        else:
            if (theirscore - myscore) >= 7:
                roll = (100 - myscore) // 3
            elif (theirscore - myscore) >= 4:
                roll = (100- myscore) // 3
            elif (theirscore - myscore) >= 1:
                roll = (100 - myscore) // 3.3
            else:
                roll = 3
    
    elif myscore >= 80:
        if myscore >= theirscore:
            if (myscore - theirscore) >= 7:
                roll = (100 - myscore) // 3.5
            elif (myscore - theirscore) >= 4:
                roll = (100-myscore) // 3.3
            else:
                roll = (100-myscore) // 3.3
        
        else:
            if (theirscore - myscore) >= 7:
                roll = (100 - myscore) // 3.3
            elif (theirscore - myscore) >= 3:
                roll = (100 - myscore) // 3.3
            else:
                roll = (100 - myscore) // 3.5
    
    elif myscore >= 70:
        if max(myscore, theirscore) == myscore:
            roll = (100 - myscore) // 3.5
        else:
            roll = (100 - myscore) // 3.5
    
    elif myscore >= 60:
        if max(myscore, theirscore) == myscore:
            roll = (100 - myscore) // 3.5
        else:
            roll = (100 - myscore) // 3.3
    
    elif myscore >= 50:
        if myscore >= theirscore:
            roll = (100 - myscore) // 3.3
        else:
            roll = (100 - myscore) // 3.1
    
    else:
        roll = (100 - myscore) // 2.5
    return int(roll)

