a=[1,3,4,2,6,0,4,2,1]

players={1:0,2:0}

on_strike=1
off_strike=2
balls=0
for i in a:
    ball=True
    if i==0:
        pass
    players[on_strike] +=i  
    if i%2==1:
        on_strike,off_strike=off_strike,on_strike
    if ball:
        balls+=1
    if balls==6:
        balls=0
        on_strike,off_strike=off_strike,on_strike
        
print('batsmen 1: ',players[on_strike])
print('batsmen 2: ',players[off_strike])
