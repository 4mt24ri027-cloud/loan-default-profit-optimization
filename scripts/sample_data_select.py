import pandas as pd

# Load your full dataset
df = pd.read_csv('data/processed_data/final_processed_data.csv')

sample_size = 100000

# Calculate exact number of rows per class
class_counts = df['loan_status'].value_counts()
total_rows = len(df)

# Determine how many rows from each class to keep
n0 = int(sample_size * class_counts[0] / total_rows)  # Fully Paid
n1 = sample_size - n0  # Charged Off (ensure total = 100k)

# Sample each class separately
df_0 = df[df['loan_status'] == 0].sample(n=n0, random_state=42)
df_1 = df[df['loan_status'] == 1].sample(n=n1, random_state=42)

# Combine and shuffle
df_sample = pd.concat([df_0, df_1]).sample(frac=1, random_state=42).reset_index(drop=True)

# Check
print("Sample shape:", df_sample.shape)
print("Target distribution (%):")
print(df_sample['loan_status'].value_counts(normalize=True) * 100)

# Save sample
df_sample.to_csv("data/processed_data/final_sample_100k.csv", index=False)