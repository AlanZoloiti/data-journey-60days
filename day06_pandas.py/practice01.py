import pandas as pd

data = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Leo'],
    'revenue': [10, 25, 35, 60, 15]
}

df = pd.DataFrame(data)
print(df)


def label_user(row):
    if row['revenue'] > 40:
        return 'high_value'
    elif 20 <= row['revenue'] <= 40:
        return 'mid_value'
    else:
        return 'low_value'


df['segment'] = df.apply(label_user, axis=1)
print(df)
