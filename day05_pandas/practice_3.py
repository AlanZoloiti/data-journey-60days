import pandas as pd

data = {
    'user': ['Ali', 'Ali', 'Ali', 'Sara', 'Sara', 'John', 'John', 'Mona'],
    'day':  [1, 2, 3, 1, 3, 1, 2, 1]
}

df = pd.DataFrame(data)

users_day1 = df[df['day'] == 1]['user'].unique()

results = {}

for day in df['day'].unique():
    users_dayX = df[df['day'] == day]['user'].unique()
    returned = set(users_day1) & set(users_dayX)
    retention = len(returned) / len(users_day1)

    results[day] = retention
print(results)

df_retention = pd.DataFrame(list(results.items()),
                            columns=['day', 'retention'])
print(df_retention)

df_cohort = df_retention.set_index('day').T
print(df_cohort)
