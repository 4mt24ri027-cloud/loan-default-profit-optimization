import pandas as pd

df = pd.read_csv('data/processed_data/loan_processed.csv')

# 3️⃣ Missing values

print('\n========== 2. Missing values ==========')
missing_count = df.isnull().sum()
missing_count_perc = (missing_count / len(df)) * 100
print("Missing count per column:\n", missing_count.sort_values(ascending=False))
print("\nMissing percentage per column:\n", missing_count_perc.sort_values(ascending=False))

# When emp_length is present → 19.5% default
# When emp_length is missing → 26.9% default so create new column 'emp_length_missing'
df['emp_length_missing'] = df['emp_length'].isnull().astype(int)

df.to_csv('data/processed_data/loan_processed_2.csv',index=False)

# The emp length missing percentage is 6% and the when map with loan status the'
#other three revol_util,dti,inq_last_6mths has less 1% missing count per so replce median


#loading new file
df['emp_length'] = df['emp_length'].fillna(df['emp_length'].median())
df['revol_util'] = df['revol_util'].fillna(df['revol_util'].median())
df['dti'] = df['dti'].fillna(df['dti'].median())
df['inq_last_6mths'] = df['inq_last_6mths'].fillna(df['inq_last_6mths'].median())

df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
df.to_csv('data/processed_data/loan_processed_2.csv', index=False)

df = pd.read_csv('data/processed_data/loan_processed_2.csv')
print("==========After the update======")
# 3️⃣ Missing values

print('\n========== 2. Missing values ==========')
missing_count = df.isnull().sum()
missing_count_perc = (missing_count / len(df)) * 100
print("Missing count per column:\n", missing_count.sort_values(ascending=False))
print("\nMissing percentage per column:\n", missing_count_perc.sort_values(ascending=False))
