import pandas as pd
import numpy as np

data = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Leo'],
    'revenue': [10, np.nan, 35, np.nan, 15]
}

df = pd.DataFrame(data)

df['status'] = np.where(pd.isna(df['revenue']), 'missing', 'ok')
print(df)
