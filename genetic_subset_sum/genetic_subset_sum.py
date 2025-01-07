import math

def sum_p(x: list[int], W: list[int]):
    multiset_size = len(x)
    result = 0
    for i in range(multiset_size):
        result += x[i] * W[i]
    return result

def fitness(x: list[int], W: list[int], c: int):
    s = 0
    px = sum_p(x)
    if c - px >= 0:
        s = 1
    return s * (c - px) + (1 - s) * px


def crossover():

def mutate():

def selection():

def genetic_subset_sum():
