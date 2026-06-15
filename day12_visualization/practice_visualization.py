import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'revenue': [5, 10, 15, 20, 1000]
})

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
sns.histplot(df['revenue'], bins=5)
plt.title('Histplot')

plt.subplot(1, 2, 2)
sns.boxplot(x=df['revenue'])
plt.title('Boxplot')

plt.show()
