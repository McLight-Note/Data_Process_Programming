'''
import numpy as np
# Creating a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])
# Reshaping it into a 2D array with 3 rows
reshaped = arr.reshape(3, -1)

print(reshaped)
'''
'''
import numpy as np
import pandas as pd

array = np.random.rand(5, 5)
df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E']) 
h_m_c = df.mean().idxmax()

print(df)
print("Column with highest mean:", h_m_c)
'''

import pandas as pd

df = pd.read_csv('employees.csv')

df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])
df = df.dropna(subset=['Salary'])
salary_avarage = df.groupby('Department')['Salary'].mean()
dep_high_sal = salary_avarage.idxmax()

print("Department with h.average salary: ", dep_high_sal)