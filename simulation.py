from itertools import permutations
from random import shuffle
from math import factorial
from copy import copy


def hamming_dist(employees, prev_perm):
    hamming_distance = 0
    for i, each in enumerate(employees):
        if each == prev_perm[i]:
            hamming_distance += 1
    return hamming_distance
    

num_trials = 1_000_000
numerator = 0
employees = list(range(1,10))
print(f'Original list: {employees}')
prev_perm = employees
shuffle(employees)
denominator = factorial(9)
for _ in range(num_trials):
    hamming_distance = hamming_dist(employees, prev_perm)
    if hamming_distance == 2:
        numerator += 1
    prev_perm = copy(employees)
    shuffle(employees)
print(numerator/ num_trials)
print(numerator)
