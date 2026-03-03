import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1️⃣ Load dataset
df = pd.read_csv('data/processed_data/loan_cleaned.csv')

#removing the current loan status records we need only bool value
df = df[df['loan_status' ].isin(['Charged Off','Fully Paid'])].copy()

df['term'] = df['term'].str.replace('months','').astype(float)
df['emp_length'] = df['emp_length'].str.replace({'<1 year':'0','10+ years':'10'})
df['emp_length'] = df['emp_length'].str.extract(r'(\d+)').astype(float)
#df['loan_status'] = pd.Categorical(df['loan_status'],categories=['Charged Off','Fully Paid'], ordered=True)

#creating new csv file and loading value
df.to_csv('data/processed_data/loan_processed.csv',index=False)
df = pd.read_csv('data/processed_data/loan_processed.csv')

# 2️⃣ Dataset size and types
print("========== 1. Dataset size and types ==========")
print('Shape:', df.shape)
print('\nData types:\n', df.dtypes)


