import pandas as pd
df = pd.read_csv('data/processed_data/loan_processed_3.csv')

pd.set_option('display.max_rows',None)

# 4️⃣ Target column distribution

print('\n========== 3. Target column distribution ==========')

print(df['loan_amnt'].value_counts())

print('\nPercentage:\n', df['loan_amnt'].value_counts(normalize=True) * 100)