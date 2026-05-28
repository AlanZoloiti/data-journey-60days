# Day 6 — Pandas: apply() & Vectorization

# Goal:
# Learn how to apply custom logic using apply() and vectorization

# What I learned:
# - apply() → row-wise logic
# - axis=1 → work with rows
# - vectorization → column operations
# - np.select → if/elif in vectorized form

import pandas as pd
import numpy as np

data = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Leo'],
    'revenue': [10, 25, 35, 60, 15],
    'visits': [1, 5, 2, 10, 1]
}

df = pd.DataFrame(data)

# Approach 1 — apply()
def classify_user(row):
    if row['revenue'] > 40 and row['visits'] > 5:
        return 'vip'
    elif row['revenue'] > 20 and row['visits'] > 2:
        return 'loyal'
    else:
        return 'casual'

df['user_score_apply'] = df.apply(classify_user, axis=1)

# Approach 2 — vectorization
conditions = [
    (df['revenue'] > 40) & (df['visits'] > 5),
    (df['revenue'] > 20) & (df['visits'] > 2)
]

choices = ['vip', 'loyal']

df['user_score_vectorized'] = np.select(conditions, choices, default='casual')

print(df)

# Key insights:
# - apply = loop over rows (slow)
# - vectorization = operations on columns (fast)
# - np.select works top-down (like if/elif)
# - order of conditions matters