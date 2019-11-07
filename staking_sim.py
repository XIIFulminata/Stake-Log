import sys

from random import randint

class StakingSimulation(object):

    def __init__(self):
        try:
            self.stake_amount = int(input('Enter your base stake? (Default 10M): '))
        except ValueError:
            self.stake_amount = 10
            print("Using default value of 10")
        
        try:
            self.sim_length = int(input('How many simulations should be run? (Default 10,000): '))
        except ValueError:
            self.sim_length = 10000
            print("Using default value of 10,000")

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

    def run_sim(self):
        # TODO make this error out better
        cash = int(input('Starting cash (in million gp): '))
        assert cash, "Please enter a number for cash"
        target = int(input('Target cash (in million gp): '))
        assert target, "Please enter a number for target"
        
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
    sim = StakingSimulation().run_sim()
