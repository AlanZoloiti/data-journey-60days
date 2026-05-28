import pandas as pd

data = {
    'user': ['Ali', 'Ali', 'Sara', 'Sara', 'John', 'John', 'Mona', 'Mona', 'Leo'],
    'day':  [1, 2, 1, 3, 2, 3, 2, 3, 3]
}

df = pd.DataFrame(data)

cohort = df.groupby('user')['day'].min().reset_index()

cohort = cohort.rename(columns={'day': 'cohort'})
print(cohort)
df = pd.merge(df, cohort, on='user')
print(df)

users_of_cohort_by_day = df.groupby(['cohort', 'day'])[
    'user'].nunique().reset_index()
print(users_of_cohort_by_day)

df_pivot = users_of_cohort_by_day.pivot(
    index='cohort',
    columns='day',
    values='user'
)
print(df_pivot)

df_retention = df_pivot.div(df_pivot[1], axis=0)
print(df_retention)
