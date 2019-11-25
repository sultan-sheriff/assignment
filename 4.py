a=['2','4','0','3','1','1','2','6','1']

players={1:0,2:0}

on_strike=1
off_strike=2
balls=0
for i in a:
    ball=True
    if i=='0':
        pass
    elif i.isdigit():
        players[on_strike] +=int(i)
        if int(i)%2==1:
            on_strike,off_strike=off_strike,on_strike
    if ball:
        balls+=1
    if balls==6:
        balls=0
        on_strike,off_strike=off_strike,on_strike
        
print(players[on_strike])
print(players[off_strike])
