import pandas as pd
orders = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Ali', 'Sara', 'John'],
    'amount': [120, 80, 200, None, 90, 300, -50],
    'status': ['paid', 'pending', 'paid', 'paid', 'pending', 'paid', 'paid']
}

df = pd.DataFrame(orders)

filter_amount = (df['amount'].notna()) & (
    df['amount'] >= 0) & (df['status'] == 'paid')

group_by_user_paid = df[filter_amount].groupby('user')['amount'].sum()

descending_sort = group_by_user_paid.sort_values(ascending=False)
print(descending_sort)

# result = df[
#     (df['amount'].notna()) &
#     (df['amount'] >= 0) &
#     (df['status'] == 'paid')
# ]\
#     .groupby('user')['amount']\
#     .sum()\
#     .sort_values(ascending=False)

# print(result)
