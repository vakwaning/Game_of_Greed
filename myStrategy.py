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
