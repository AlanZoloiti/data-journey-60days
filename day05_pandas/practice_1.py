import pandas as pd

data = {
    'user': ['Ali', 'Ali', 'Sara', 'Sara', 'John', 'Mona'],
    'day': [1, 2, 1, 3, 1, 1]
}

df = pd.DataFrame(data)
print(df)

df_day1 = df[df['day'] == 1]
print(df_day1)

df_returned = df[df['day'] > 1]
print(df_returned)
