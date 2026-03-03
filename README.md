

# 📌 Loan Default Prediction & Profit Optimization

## 🚀 Project Overview

This project builds a Machine Learning system to predict loan default probability and optimize loan approval decisions using business-driven profit simulation.

Unlike traditional ML projects that focus only on accuracy, this project converts predictions into financial decisions by selecting an optimal approval threshold that maximizes profit.

### Core Objectives

* Predict loan default probability
* Handle imbalanced dataset (~80:20 ratio)
* Compare Logistic Regression and Random Forest
* Perform threshold optimization
* Convert ML output into a profit-based decision engine

---

## 📂 Dataset

⚠️ **Important Notice**

This repository includes only a **100,000 record sample dataset** for demonstration.

The full dataset is not included due to size limitations.

To reproduce complete results:

1. Download the LendingClub dataset from
   **Kaggle**

2. Place the downloaded CSV file inside:

```
data/raw_data/
```

3. Run preprocessing to generate cleaned data.

---

## 📁 Project Structure

```
Loan-Default-Profit-Optimization/
│
├── data/
│   ├── raw_data/                 # Full dataset (not included)
│   ├── processed_data/
│   │   └── final_sample_100k.csv
│   └── final_predicted_data/
│
├── scripts/
│   ├── final_EDA_Cleaning.py
│   ├── logistic_model.py
│   ├── random_forest_model.py
│   ├── business_logic.py
│
├── plots/
├── requirements.txt
└── README.md
```

---

## 🧠 Models Implemented

### 1️⃣ Logistic Regression (Primary Model)

* Baseline interpretable model
* Probability-based output
* Suitable for financial risk modeling

### 2️⃣ Random Forest

* Non-linear ensemble comparison
* Used to benchmark performance

---

## 📊 Evaluation Metrics

* Accuracy
* Recall (Default / Charged-Off class)
* Confusion Matrix
* Probability distribution analysis

Special focus is placed on **recall for defaulters**, since missing risky borrowers increases financial loss.

---

## 💰 Business Logic & Profit Optimization

Instead of using the default probability threshold (0.5), this project:

1. Predicts probability of default
2. Tests multiple probability thresholds
3. Simulates profit/loss for each threshold
4. Selects the threshold that maximizes total profit

This transforms a classification model into a **financial decision optimization system**.

---

## 🛠 How To Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train Logistic Regression Model

```bash
python scripts/logistic_model.py
```

### 3️⃣ Run Profit Optimization

```bash
python scripts/business_logic.py
```

---

## 📈 Future Enhancements

* Cross-validation
* ROC-AUC comparison
* Hyperparameter tuning
* SHAP-based model explainability
* Deployment using FastAPI or Streamlit
* Real-time loan approval simulation

---

## 🎯 Key Takeaways

* Imbalanced classification handling
* Probability-based decision systems
* Business-oriented ML modeling
* Threshold optimization strategy
* Risk modeling for financial applications

---

##👨‍💻 Author

**Prajnesh Shetty**  

This project was built as part of my Machine Learning practice to explore:
- Imbalanced classification
- Probability-based modeling
- Business-driven threshold optimization