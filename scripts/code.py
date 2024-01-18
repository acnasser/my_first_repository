import random
import itertools

letters = "difhqwf"
perms = list(itertools.permutations(letters))
random.shuffle(perms)

for i in range(1000):
    print("".join(perms[i]))
