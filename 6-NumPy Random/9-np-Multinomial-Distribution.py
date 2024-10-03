# Multinomial distribution is a generalization of binomial distribution.
# It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.
# It has three parameters:
# n - number of possible outcomes (e.g. 6 for dice roll).
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.

from numpy import random

# array = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
array = random.multinomial(n=7, pvals=[1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7])
print("1. Multinomial Distribution : \n", array)

#  As they are generalization of binomial distribution their visual representation and similarity of 
# normal distribution is same as that of multiple binomial distributions.

# Multinomial samples will NOT produce a single value! They will produce one value for each pval.