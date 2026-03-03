import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix


df = pd.read_csv('data/processed_data/final_processed_data.csv')

#splitting the data as target and feature
x= df.drop('loan_status',axis=1) #features
y = df['loan_status'] #target

#split data
x_train ,x_test ,y_train,y_test = train_test_split(x,y,
test_size = 0.2,  # 20% data for testing
stratify = y,  # maintain 0/1 ratio
random_state = 42  # ensures reproducible results
)

#LogistricRegression  model training

# Create and train the model
lr_model = LogisticRegression(
max_iter=2000,
class_weight = 'balanced',  # pay more attention to minority class
random_state=42)
lr_model.fit(x_train, y_train)



# Predict on test data
y_pred = lr_model.predict(x_test)

#predict probabilities
y_proba = lr_model.predict_proba(x_test)[:,1]

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Recall (charged off):", recall_score(y_test, y_pred, pos_label=1))
print("Recall (fully paid):", recall_score(y_test, y_pred, pos_label=0))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

#saving result to csv for buissnes logic
df_result = x_test.copy()
df_result['loan_status'] = y_test.values
df_result['charged_off_probability'] = y_proba
df_result.to_csv('data/processed_data/test_prediction_with_prob')