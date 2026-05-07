import pandas as pd

data = {
    'name': ['Ali', 'Sara', 'Jphn', 'Mona'],
    'age': [25, 30, 22, 28],
    'salary': [3000, 4000, 2500, 3500],
}
df = pd.DataFrame(data)

print('=== HEAD ===')
print(df.head())

print('\n=== INFO ===')
df.info()

print('\n=== SALARY COLUMN===')
print(df['salary'])
