import pandas as pd
import numpy as np

data = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Leo'],
    'revenue': [10, 25, 35, 60, 5]
}

df = pd.DataFrame(data)

conditions = [
    (df['revenue'] > 50),
    (df['revenue'] > 30),
    (df['revenue'] > 10)
]

choices = ['high', 'medium', 'low']
df['spending_level'] = np.select(conditions, choices, default=None)
print(df)
