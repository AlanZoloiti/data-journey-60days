import pandas as pd

data = {
    'user': ['Ali', 'Ali', 'Sara', 'Sara', 'John', 'John', 'Mona', 'Mona', 'Leo'],
    'day':  [1, 2, 1, 3, 2, 3, 2, 3, 3],
    'revenue': [10, 20, 15, 25, 30, 40, 50, 60, 70]
}

df = pd.DataFrame(data)
print(df)

# 1. Когда пользователь появился?
cohort = df.groupby('user')['day'].min().reset_index()
print(cohort)

# 2. Переименовываем столбец 'day' в 'cohort'
cohort_df = cohort.rename(columns={'day': 'cohort'})
print(cohort_df)

# 3. Merging df and cohort_df
df_mer_cohort_df = pd.merge(df, cohort_df, on='user')
df_mer_cohort_df['day_number'] = df_mer_cohort_df['day'] - \
    df_mer_cohort_df['cohort']
print(df_mer_cohort_df)

# 4. Колисество пользоватиелей из каждой когорты было в каждый день
users_per_day = df_mer_cohort_df.groupby(['cohort', 'day_number'])[
    'user'].nunique().reset_index()
print(users_per_day)

# 5. Pivot - меняем ориентацию таблицы(меяем столбцы и колонки местами)
df_pivot = users_per_day.pivot(
    index='cohort',
    columns='day_number',
    values='user'
)
print(df_pivot)

# 6. Retention - удержание пользователей
# (df_pivot[1], axis=0) почему совершается деление имеено в порядке насиная с первого числа в строке делением на это число и далее осталных на это же число ?
retention = df_pivot.div(df_pivot[0], axis=0)
print(retention)

# 6. Колисество пользоватиелей из каждой когорты было в каждый день
revenue_per_day = df_mer_cohort_df.groupby(['cohort', 'day_number'])[
    'revenue'].sum().reset_index()
print(revenue_per_day)

# 7. Pivot - меняем ориентацию таблицы(меяем столбцы и колонки местами)
revenue_pivot = revenue_per_day.pivot(
    index='cohort',
    columns='day_number',
    values='revenue'
)
print(revenue_pivot)

# 8. Revenue Retention - сколько выручки осталось
revenue_retention = revenue_pivot.div(revenue_pivot[0], axis=0)
print(revenue_retention)
