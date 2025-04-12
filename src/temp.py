import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/df.csv")
cols = df.columns
g = sns.displot(data=df,
                x=cols[2],
                y=cols[3],
                bins=30,
                hue=cols[0],
                legend=True,
                height=8,
                aspect=1,
                col=cols[0],
                col_wrap=2)
plt.show()
