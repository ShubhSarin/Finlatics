import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Employee_Name': ['em1', 'em2', 'em3', 'em4', 'em5'],
    'Income': [1000, 2000, 3000, 4000, 5000],
}, index = ['a','b','c','d','e'])
print(df)