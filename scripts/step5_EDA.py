# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1️⃣ Load your dataset
df = pd.read_csv('data/processed_data/loan_processed_3.csv')

# 2️⃣ Select numeric columns
numeric_cols = df.select_dtypes(include=['int64','float64']).columns

# 3️⃣ Sample the dataset to avoid freezing (optional)
df_sample = df.sample(100000, random_state=42)  # 100k rows for speed

# 4️⃣ Create folder to save plots
os.makedirs("plots", exist_ok=True)

# 5️⃣ Loop through numeric columns and save histograms
for col in numeric_cols:
    plt.figure(figsize=(8,5))
    df_sample[col].hist(bins=50)
    plt.title(f'{col} distribution (sampled 100k)')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'plots/{col}_hist.png')  # Save instead of showing
    plt.close()  # Close figure to avoid memory issues