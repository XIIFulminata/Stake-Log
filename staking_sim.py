from random import randint

def stakes(cash, target, stake_num=0, stake_amount=7, multiplier=1):
    if cash >= target:
        return True
    if cash <= 0:
        return False
    win = randint(0,1)
    if win:
        cash += (multiplier * stake_amount * .99)
        multiplier = 1
    else:
        cash -= (multiplier * stake_amount)
        multiplier *= 2
#     print (f"stake number {stake_num}")
    return stakes(cash, target, stake_num+1, stake_amount, multiplier)

wins = losses = 0
sim_length=10000
for _ in range(sim_length):
    if stakes(500,3000):
        wins += 1
    else:
        losses += 1
print (wins, losses)
print (f"this yields a {wins/sim_length*100}% win rate")
