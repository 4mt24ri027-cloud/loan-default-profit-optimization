import pandas as pd

df = pd.read_csv('data/processed_data/loan_processed_2.csv')

# 5️⃣ Numeric feature summary

print('\n========== 4. Numeric feature summary ==========')
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)


df.loc[df['dti']<0,'dti'] = df['dti'].median()
upper = df['dti'].quantile(.99)
df['dti'] = df['dti'].clip(upper=upper)
df = df.drop_duplicates()

df.to_csv('data/processed_data/loan_processed_3.csv',index=False)
print(df.describe())
