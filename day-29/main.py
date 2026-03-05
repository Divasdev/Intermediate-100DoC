import numpy as np

# 1. Define the possible outcomes of our die
outcomes = [1, 2, 3, 4, 5, 6]

# 2. "Roll" the die 10,000 times
# size=10000 tells it how many times to repeat the experiment
trials = np.random.choice(outcomes, size=10000)

# 3. Calculate the simulated expected value
simulated_EV = np.mean(trials)

