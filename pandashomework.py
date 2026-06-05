import pandas as pd
import numpy as np

employeedata = {
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", "", "", ""],
    "Salary": [100, 200, np.nan, np.nan]
}
df = pd.DataFrame(employeedata)
print(df)
print("\n")
print(df.head(2))
print("\n")
print(df.tail(2))
print("\n")
print(df.isnull().sum().sum())
df.info()
df_rows = df.dropna()
print(df_rows)
df_cols = df.dropna(axis=1)
print(df_cols)
filled_salary = df.fillna({"Salary": 300})
print(filled_salary)
filled_role = df.fillna({"Role": "CEO"})
print(filled_role)
