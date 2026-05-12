import pandas as pd

orders = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Ali', 'Sara'],
    'amount': [120, 80, 200, 150, 90, 300],
    'status': ['paid', 'pending', 'paid', 'paid', 'pending', 'paid']
}
df = pd.DataFrame(orders)


result = df[(df['amount'] > 100) & (df['status'] == 'paid')]
print(result)


result_2 = df[(df['amount'] > 100) & (df['status'] == 'paid')]['user']
print(result_2)

result_3 = df.groupby('user')['amount'].sum()
print(result_3)
