import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'ads': [10, 20, 30, 40, 50],
    'revenue': [100, 200, 300, 400, 500],
    'users': [200, 180, 220, 210, 205],
    'time_spent': [5, 10, 15, 20, 25]
})

sns.heatmap(df.corr(), annot=True)
plt.show()
