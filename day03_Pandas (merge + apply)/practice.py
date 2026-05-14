import pandas as pd

users = {
    'user': ['Ali', 'Sara', 'John', 'Mona'],
    'country': ['UAE', 'KSA', 'USA', 'UAE']
}

orders = {
    'user': ['Ali', 'Sara', 'John', 'Mona'],
    'amount': [100, 200, 150, 300]
}

df = pd.merge(pd.DataFrame(users), pd.DataFrame(orders))

df['category'] = df['amount'].apply(lambda x: 'high' if x > 150 else 'low')
df['final_amount'] = df.apply(
    lambda row: row['amount'] * 1.2 if row['category'] == 'high' else row['amount'] * 1.1, axis=1
)

print(df)
