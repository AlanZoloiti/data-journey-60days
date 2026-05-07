import pandas as pd

orders = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Ali', 'Sara'],
    'amount': [120, 80, 200, 150, 90, 300],
    'status': ['paid', 'pending', 'paid', 'paid', 'pending', 'paid']
}
df = pd.DataFrame(orders)

filter_status = df['status'] == 'paid'
print(filter_status)

group_by_user_paid = df[filter_status].groupby('user')['amount'].sum()
print(group_by_user_paid)


descending_sort = group_by_user_paid.sort_values(ascending=False)
print(descending_sort)
