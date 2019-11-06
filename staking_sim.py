from random import randint

class StakingSimulation(object):
    # TODO make stake amount take a dict as well to allow for multiple outputs

    def __init__(self, stake_amount: int, sim_length: int = 10000):
        self.stake_amount = stake_amount
        self.sim_length = sim_length
        self.tax_rate = 0.99
        self.wins = 0
        self.losses = 0

    def _run_sim_helper(self, cash: int, target: int):
        if cash >= target:
            return True
        if cash <= 0:
            return False
        win = randint(0,1)
        if win:
            cash += (self.multiplier * self.stake_amount * self.tax_rate)
            self.multiplier = 1
        else:
            cash -= (self.multiplier * self.stake_amount)
            self.multiplier *= 2
        self.stake_num += 1  # TODO print avg stake count
        return self._run_sim_helper(cash, target)

    def run_sim(self, cash: int, target: int):
        for _ in range(self.sim_length):
            self.stake_num = 0
            self.multiplier = 1
            if self._run_sim_helper(cash, target):
                self.wins += 1
            else:
                self.losses += 1
        print (self.wins, self.losses)
        print (f"this yields a {self.wins/self.sim_length*100}% win rate")

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
        if stakes(500,3000):
            wins += 1
        else:
            losses += 1
    print (wins, losses)
    print (f"this yields a {wins/sim_length*100}% win rate")
    StakingSimulation(7).run_sim(500, 3000)

