from random import randint

def stakes(cash: int, target: int, stake_num: int = 0, stake_amount: int = 7, multiplier: int = 1) -> bool:
    """
    Returns whether a "player" hits the target gold value in the simulation

    Args:
    cash -- amount of gold in Mgp that the player has to stake
    target -- minimum amount of gold in Mgp that the player wants to leave with
    stake_num -- (user shouldn't access)
    stake_amount -- base value of a stake in Mgp
    multiplier -- (user shouldn't access)
    """

    # TODO turn this into a class
    # TODO make stake amount take a dict as well to allow for multiple outputs

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
    return stakes(cash, target, stake_num+1, stake_amount, multiplier)

if __name__ == "__main__": 
    wins = losses = 0
    sim_length=10000
    for _ in range(sim_length):
        if stakes(1500,3000):
            wins += 1
        else:
            losses += 1
    print (wins, losses)
    print (f"this yields a {wins/sim_length*100}% win rate")
