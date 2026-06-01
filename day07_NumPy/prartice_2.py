import pandas as pd
import numpy as np
data = {
    'user': ['Ali', 'Sara', 'John', 'Mona', 'Leo'],
    'revenue': [10, 25, 35, 60, 15]
}

df = pd.DataFrame(data)

df['vip_flag'] = np.where(df['revenue'] >= 50, 'vip', 'normal')
print(df)
