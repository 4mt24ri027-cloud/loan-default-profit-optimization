# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1️⃣ Load your dataset
df = pd.read_csv('data/processed_data/loan_processed_3.csv')

#7️⃣ Categorical feature exploration

print('\n========== 5. Categorical feature exploration ==========')

categorical_cols = ['grade', 'sub_grade', 'emp_length', 'home_ownership',

'verification_status', 'purpose', 'addr_state',

                'application_type', 'loan_status']

for col in categorical_cols:

    print(f'\n{col} value counts:\n', df[col].value_counts(normalize=True)*100)


