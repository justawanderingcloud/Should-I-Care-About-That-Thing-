# Should I Care About This Thing That You Are Presenting me?
# Might be biased towars saying "no", dunno why, works on my machine

import random

choices = ["Yes", "No"]

make_weighted_choice = random.choices(choices, weights=[0.1, 0.9], k=1)[0]

print("Should I Care About This Thing That You Are Presenting Me?")
print("The answer is:", make_weighted_choice)
