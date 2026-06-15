import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'ads': [1, 2, 3, 4, 5],
    'revenue': [10, 20, 30, 40, 50],
    'users': [5, 3, 6, 2, 7]
})

sns.heatmap(df.corr(), annot=True)
plt.title('Correlation Heatmap')
plt.show()
