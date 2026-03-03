import pandas as pd
df = pd.read_csv('data/processed_data/loan_processed_4.csv')
df['loan_status'] = df['loan_status'].map({'Fully Paid':0,'Charged Off':1})

#coverting str into number order
#dropping state column because for simple model it not need if you get better model include this
df = df.drop('addr_state',axis=1)

#applying ordeal encoding to sub_grade
df['grade_letter'] = df['sub_grade'].str[0]
df['grade_number'] = df['sub_grade'].str[1].astype(int)
grade_mapping = {
'A':1,
'B':2,
'C':3,
'D':4,
'E':5,
'F':6,
'G':7
}

df['grade_letter'] = df['grade_letter'].map(grade_mapping)
df['sub_grade_encoded'] = (df['grade_letter'] - 1) * 5 + df['grade_number']
df.drop(['sub_grade','grade_letter','grade_number'], axis=1, inplace=True)

#converting earliest_cr_line to number of year
df['earliest_cr_line'] = pd.to_datetime(df['earliest_cr_line'],format='%b-%Y',errors='coerce')
df['credit_history_years'] = (pd.Timestamp('today') - df['earliest_cr_line']).dt.days / 365
df.drop('earliest_cr_line', axis=1, inplace=True)

#applying hot encoding to ['home_ownership','verification_status','purpose','application_type']
df = pd.get_dummies(
    df,
    columns=['home_ownership','verification_status','purpose','application_type'],
    drop_first=True

)
if 'Unnamed: 0' in df.columns:
    df.drop('Unnamed: 0', axis=1, inplace=True)

#i don't how but i missed one empty data in loan amnt i found at model phase
df = df.dropna(subset=['loan_amnt'])
df.to_csv("data/processed_data/final_processed_data.csv", index=False)
