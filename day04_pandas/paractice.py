import pandas as pd

# --- данные ---
users = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Ali', 'Sara', 'John'],
    'country': ['UAE', 'KSA', 'USA', 'UAE', 'UAE', 'KSA', 'USA']
}

orders = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Ali', 'Sara', 'John'],
    'amount': [120, 80, 200, 150, 90, 300, 50],
    'status': ['paid', 'paid', 'paid', 'paid', 'pending', 'paid', 'paid']
}

# --- подготовка данных ---
df_users = pd.DataFrame(users).drop_duplicates()
df_orders = pd.DataFrame(orders)

df = pd.merge(df_users, df_orders, on='user')

# оставляем только оплаченные
df = df[df['status'] == 'paid']

# сегментация
df['segment'] = df.apply(
    lambda row: 'VIP' if row['amount'] >= 200
    else 'mid' if row['amount'] >= 100
    else 'low',
    axis=1
)

# --- ВАЖНО ---
# дальше ты работаешь с df
print(df)

country_rev = df.groupby('country')[
    'amount'].sum().sort_values(ascending=False).reset_index()


country_segment_rev = df.groupby(['country', 'segment'])[
    'amount'].sum().reset_index()

user_mean_check = df.groupby('user')['amount'].mean().reset_index()


print("\n=== Revenue by Country ===\n")
print(country_rev)

print("\n=== Revenue by Coutry and Segment ===\n")
print(country_segment_rev)


print("\n=== Average Check per User ===\n")
print(user_mean_check)
