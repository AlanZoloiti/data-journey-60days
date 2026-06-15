import pandas as pd

df = pd.DataFrame({
    'ads': [1, 2, 3, 4, 5],
    'revenue': [10, 20, 30, 40, 50],
    'users': [5, 3, 6, 2, 7]
})
correlaton = df.corr()
print(correlaton)
