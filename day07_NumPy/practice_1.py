import pandas as pd
import numpy as np

data = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Leo'],
    'revenue': [10, 25, 35, 60, 15]
}

df = pd.DataFrame(data)

arr = np.array(df['revenue'])
df['revenue_flag'] = np.where(arr > 30, 'high', 'low')
print(df)
