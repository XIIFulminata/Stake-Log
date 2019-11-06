import sys

from random import randint

class StakingSimulation(object):

    def __init__(self, stake_amount: int, sim_length: int = 10000):
        self.stake_amount = stake_amount
        self.sim_length = sim_length
        self.tax_rate = 0.99
        self.wins = 0
        self.losses = 0
        self.stake_count = 0

    def _run_sim_helper(self, cash: int, target: int) -> bool:
        """
        Returns whether a "player" hits the target gold value in the simulation

        Args:
        cash -- amount of gold in Mgp that the player has to stake
        target -- minimum amount of gold in Mgp that the player wants to leave with
        """
        # print(f"tried to run helper with these params cash: {cash}, target: {target}")
        if cash >= target:
            self.stake_count += self.stake_num
            return True
        if cash <= 0:
            return False
        win = randint(0,1)  # TODO account for X's w/ dps in each scenario
        if win:
            cash += (self.multiplier * self.stake_amount * self.tax_rate)
            self.multiplier = 1
        else:
            cash -= (self.multiplier * self.stake_amount)
            self.multiplier *= 2
        self.stake_num += 1
        return self._run_sim_helper(cash, target)

    def run_sim(self, cash: int, target: int):
        print (f"Starting cash: {cash}M gp")
        print (f"Target cash: {target}M gp")
        print (f"Running sim {self.sim_length} times with a base stake of {self.stake_amount}")
        for _ in range(self.sim_length):
            self.stake_num = 0
            self.multiplier = 1
            if self._run_sim_helper(cash, target):
                self.wins += 1
            else:
                self.losses += 1
        print (f"{self.wins} Wins, {self.losses} Losses")
        print (f"Win rate: {round(self.wins/self.sim_length*100, 2)}%")
        print (f"Average stakes to win: {round(self.stake_count/self.wins)} stakes")

if __name__ == "__main__":
    stake_amount, cash, target = [int(x) for x in sys.argv[1:4]]  # TODO use inputs instead
    sim = StakingSimulation(stake_amount).run_sim(cash, target)
