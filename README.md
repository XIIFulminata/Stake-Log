# Stake-Log (WIP) ![alt text](http://vignette3.wikia.nocookie.net/runescape2/images/1/1a/Polypore_staff.png/revision/latest?cb=20160502063510 "Polypore Staff")
Logging and Projecting Stakes, Martingale

## Background

I wanted an excuse to play Runescape, so I decided to record and plan stakes (bets) to get used to matplotlib and d3.js. Staking is a (virtually) 50/50 game of chance. Many gambling addi- I mean Runescape players swear by the [Martingale betting system](https://en.wikipedia.org/wiki/Martingale_(betting_system)), but those who do just haven't used it long enough. I will be recording stakes until I get cleaned or my assumption is proven wrong and I become infintely wealthy.




## Notebook

I'm recording each session of stakes as its own graph with a restricted window to better visualize how much money I'll be losing. I also created a Martingale Planner that would tell me how much o bet in each scenario, depending on how conservatively I'd like to play.

## Next Steps
-> Martingale Simulator (random path for the program to plot)

-> Overall Graph

-> Turn notebook into a dashboard

## Martingale System
### How it Works 

A player will bet a fractional amount of their net worth, maybe 1-4 Million Gold Pieces [M] which may be a few hours’ work, but is a drop in the bucket when compared to the average high level player's bank. Should the player win, they repeat the process. If they lose however, the Martingale betting system has them double the bet, and repeat until a victory is achieved. No matter how many times you lose, if you win the last bet, you've profited the same amount as your initial bet of 1-4M. For a user who started out betting 1% of their net worth, to lose they would have to lose the following stakes in a row:

[1% (stake 1), 2% , 4% , 8% , 16% , 32% (stake6)]

6 stakes in a row? On a 50/50 game? No way you could lose, that's like a 1/2^6 chance!

### Problems
1) Exponential Growth: When you have to double your bets after each loss, they get too high too rapidly. You could literally bet half as much on your initial bet, and still get to the same loss very quickly. This in part is why the planner doesn't work. Being conservative means starting low to increasae the number of stakes between you and bankruptcy. Starting low won't save you from exponential growth.

2) Probability Hates You: Forget the 1/2^6 chance. Each event is its own 50/50 chance, so as you progressively lose, you are no closer to the promise of recovery. 

3) Probablilty Really Hates You: The main point is, this system only works for people with infinite capital. You would think, "There's no way I could be unlucky enough to lose 6 matches in a row," until it happens. You only need to hit one "streak" of losses to undo every win you've had up to that point. 
