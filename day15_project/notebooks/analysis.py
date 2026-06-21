import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    'ads': [100, 200, 300, 400, 500],
    'revenue': [1000, 1800, 2600, 3200, 4000],
    'users': [1000, 1500, 2000, 3000, 5000],
    'time_spent': [5, 7, 10, 13, 15]
})

sns.heatmap(df.corr(), annot=True)
plt.show()

df.describe()
sns.histplot(df['revenue'])
