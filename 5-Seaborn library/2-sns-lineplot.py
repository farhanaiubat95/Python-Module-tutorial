import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


x = [1, 2, 3, 4, 5, 6, 7]
y = [10, 20, 30, 20, 40, 50, 40]

dat = {
    "Days": x,
    "No of students": y}

df = pd.DataFrame(dat)

sns.lineplot(data=df, x="Days", y="No of students")


plt.show()
