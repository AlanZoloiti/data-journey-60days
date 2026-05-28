import pandas as pd

data = {
    'user': ['Ali', 'Ali', 'Ali', 'Sara', 'Sara', 'John', 'John', 'Mona'],
    'day':  [1, 2, 3, 1, 3, 1, 2, 1]
}

df = pd.DataFrame(data)

# Day 1 cohort
users_day1 = df[df['day'] == 1]['user'].unique()

# Day 2 и Day 3
users_day2 = df[df['day'] == 2]['user'].unique()
users_day3 = df[df['day'] == 3]['user'].unique()

# пересечения
returned_users_day2 = set(users_day1) & set(users_day2)
returned_users_day3 = set(users_day1) & set(users_day3)

# retention
retention_day2 = len(returned_users_day2) / len(users_day1)
retention_day3 = len(returned_users_day3) / len(users_day1)

print({
    'retention_day2': retention_day2,
    'retention_day3': retention_day3
})
