import pandas as pd
import numpy as np

data = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Leo'],
    'revenue': [10, 25, 35, 60, 15],
    'visits': [1, 5, 2, 10, 1]
}

df = pd.DataFrame(data)

conditions = [
    (df['visits'] >= 8),
    (df['visits'] >= 3) & (df['visits'] <= 7)
]

choices = ['heavy', 'medium']

df['activity_level'] = np.select(conditions, choices, default='low')
print(df)
