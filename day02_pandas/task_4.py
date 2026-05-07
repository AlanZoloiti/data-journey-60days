import pandas as pd
orders = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Ali', 'Sara', 'John', 'Mona'],
    'amount': [120, 80, 200, 150, 90, 300, 50, 400],
    'status': ['paid', 'paid', 'paid', 'paid', 'paid', 'paid', 'paid', 'paid'],
    'month': ['Jan', 'Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Feb']
}

df = pd.DataFrame(orders)

revenue_by_month = df.groupby('month')['amount'].sum()
print(revenue_by_month)

revenue_by_month_by_user = df.groupby(['month', 'user'])['amount'].sum()
print(revenue_by_month_by_user)
