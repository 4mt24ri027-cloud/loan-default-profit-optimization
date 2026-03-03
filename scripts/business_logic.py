import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# 1️⃣ Load CSV with model predictions
# --------------------------
df = pd.read_csv('data/processed_data/test_prediction_with_prob')

# True labels and predicted probability of charged off
y_test = df['loan_status']
y_proba = df['charged_off_probability']

# --------------------------
# 2️⃣ Business assumptions
# --------------------------
profit_if_paid = 10000  # Bank earns $10k if loan fully paid
loss_if_default = -20000  # Bank loses $20k if loan defaults

# --------------------------
# 3️⃣ Simulate profit for multiple thresholds
# --------------------------
thresholds = np.arange(0.1, 0.91, 0.05)  # 0.1 to 0.9
total_profit = []

for t in thresholds:
    # Convert probability to approve/reject decision
    y_pred = (y_proba >= t).astype(int)  # 1 = reject, 0 = approve

    # Only consider approved loans
    approved_idx = np.where(y_pred == 0)[0]
    approved_actual = y_test.iloc[approved_idx]

    # Calculate profit
    profit = np.sum(np.where(approved_actual == 0, profit_if_paid, loss_if_default))
    total_profit.append(profit)

# --------------------------
# 4️⃣ Find threshold with maximum profit
# --------------------------
max_profit_idx = np.argmax(total_profit)
best_threshold = thresholds[max_profit_idx]
print(f"Best threshold for maximum profit: {best_threshold}")
print(f"Maximum profit: ${total_profit[max_profit_idx]}")

# --------------------------
# 5️⃣ Optional: visualize profit vs threshold
# --------------------------
plt.figure(figsize=(8, 5))
plt.plot(thresholds, total_profit, marker='o')
plt.xlabel("Approval Threshold (Probability of Default)")
plt.ylabel("Total Profit")
plt.title("Profit Optimization by Threshold")
plt.grid(True)
plt.savefig('plots/Profit_Optimization_by_Threshold')
plt.show()

# --------------------------
# 6️⃣ Optional: add 'approve' column and save
# --------------------------
df['approve'] = (df['charged_off_probability'] < best_threshold).astype(int)  # 1 = approve, 0 = reject
df.to_csv('data/final_predicted_data/test_predictions_with_approval.csv', index=False)
print("✅ CSV with approval decisions saved: data/processed_data/test_predictions_with_approval.csv")