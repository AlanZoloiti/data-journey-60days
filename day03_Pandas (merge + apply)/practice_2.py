import pandas as pd

users = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Ali', 'Sara', 'John'],
    'country': ['UAE', 'KSA', 'USA', 'UAE', 'UAE', 'KSA', 'USA']
}

orders = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Ali', 'Sara', 'John'],
    'amount': [120, 80, 200, 150, 90, 300, 50],
    'status': ['paid', 'paid', 'paid', 'paid', 'pending', 'paid', 'paid']
}

df = pd.merge(pd.DataFrame(users).drop_duplicates(),
              pd.DataFrame(orders), on='user')

df = df[df['status'] == 'paid']
df['segment'] = df.apply(
    lambda row: 'VIP' if row['amount'] >= 200
    else 'mid' if row['amount'] >= 100
    else 'low',
    axis=1
)

result = df.groupby('segment')['amount'].sum().sort_values(ascending=False)

print(result)
