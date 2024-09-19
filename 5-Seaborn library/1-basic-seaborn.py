# Seaborn is an amazing visualization library for statistical graphics plotting in Python.
# default styles and color palettes to make statistical plots more attractive
# It is built on top (matplotlib library) &
# also closely integrated with the data structures from (pandas).
# It provides dataset-oriented APIs so that we can switch between different visual representations for
# the same variables for a better understanding of the dataset.

# Seaborn divides the plot into the below categories
# Relational plots:   This plot is used to understand the relation between two variables.
# Categorical plots:  This plot deals with categorical variables and how they can be visualized.
# Distribution plots: This plot is used for examining univariate and bivariate distributions
# Regression plots:   The regression plots in Seaborn are primarily intended to add a visual guide that helps to emphasize patterns in a dataset during exploratory data analyses.
# Matrix plots:       A matrix plot is an array of scatterplots.
# Multi-plot grids:   It is a useful approach to draw multiple instances of the same plot on different subsets of the dataset.
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)

# Plot a simple histogram and kde
sns.histplot(d, kde=True, color="m")


plt.show()