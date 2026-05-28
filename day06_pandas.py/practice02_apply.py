import pandas as pd

data = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Leo'],
    'revenue': [10, 25, 35, 60, 15],
    'visits': [1, 5, 2, 10, 1]
}

df = pd.DataFrame(data)
print(df)


def classify_user(row):
    if row['revenue'] > 40 and row['visits'] > 5:
        return 'vip'
    elif row['revenue'] > 20 and row['visits'] > 2:
        return 'loyal'
    else:
        return 'casual'


df['user_score'] = df.apply(classify_user, axis=1)
print(df)
