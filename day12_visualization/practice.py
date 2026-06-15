# 1
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.DataFrame({
    'revenue': [10, 20, 30, 40, 500]
})
q1 = df['revenue'].quantile(0.25)
median = df['revenue'].quantile(0.5)
q3 = df['revenue'].quantile(0.75)

print(q1, median, q3)

# 2

df = pd.DataFrame({
    'revenue': [10, 20, 30, 40, 50]
})
q1 = df['revenue'].quantile(0.25)
median = df['revenue'].quantile(0.5)
q3 = df['revenue'].quantile(0.75)

iqr = q3 - q3
lower_bound = q1 - iqr
upper_bound = q3 + iqr

outliers = df[(df['revenue'] < lower_bound) | (df['revenue'] > upper_bound)]

print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("Outliers:")
print(outliers)


sns.histplot(df['revenue'], bins=5)
plt.title('Revenue Distribution')
plt.show()
