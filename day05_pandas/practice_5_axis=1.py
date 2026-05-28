import pandas as pd

df = pd.DataFrame({
    'A': [10, 20],
    'B': [20, 40],
    'C': [30, 60]
}, index=['base', 'experiment'])

print(df)

result = df.div(df.loc['base'], axis=1)
print(result)
