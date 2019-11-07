import sys

from random import randint
from typing import Optional

class StakingSimulation(object):

    @staticmethod
    def _get_input_or_default(input_message: str, default_value: Optional[int] = None) -> int:
        """
        Returns a user input or default value.
        Retry until an appropriate value is given (unless a default is provided)
        """
        while True:
            try:
                return int(input(input_message))
            except ValueError:
                if default_value != None:
                    print(f"Using default value of {default_value}")
                    return default_value
                else:
                    print("Please provide a valid integer input")


    def __init__(self):
        self.stake_amount = StakingSimulation._get_input_or_default(
            input_message='Enter your base stake? (Default 10M): ',
            default_value=10
        )
        self.sim_length = StakingSimulation._get_input_or_default(
            input_message='How many simulations should be run? (Default 10,000): ',
            default_value=10000
        )

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
        if cash >= target:
            self.stake_count += self.stake_num
            return True
        if cash <= 0:
            return False
        win = randint(0,1)  # TODO account for X's, maybe w/ dps in each scenario
        if win:
            cash += (self.multiplier * self.stake_amount * self.tax_rate)
            self.multiplier = 1
        else:
            cash -= (self.multiplier * self.stake_amount)
            self.multiplier *= 2
        self.stake_num += 1
        return self._run_sim_helper(cash, target)

    def run_sim(self):
        cash = StakingSimulation._get_input_or_default('Starting cash (in million gp): ')
        target = StakingSimulation._get_input_or_default('Target cash (in million gp): ')
        
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
