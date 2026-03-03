import pandas as pd

df = pd.read_csv('data/raw_data/accepted_2007_to_2018Q4.csv')

target = 'loan_status'
features = [
    'loan_amnt', 'term', 'int_rate', 'installment', 'grade', 'sub_grade',
    'emp_length', 'home_ownership', 'annual_inc', 'verification_status',
    'purpose', 'addr_state', 'dti', 'delinq_2yrs', 'earliest_cr_line',
    'fico_range_low', 'fico_range_high', 'inq_last_6mths', 'open_acc',
    'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'application_type'
]

df_model = df[features + [target]]


df_model.to_csv("data/processed_data/loan_cleaned.csv", index=False)