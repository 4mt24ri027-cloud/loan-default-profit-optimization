# 5% reecall on  charged of so i prefer using the logistic reggression model
#if want you can work on this
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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

# Create RF model
rf_model = RandomForestClassifier(
    n_estimators=200,          # number of trees
    class_weight='balanced',   # handle imbalanced classes
    random_state=42,
    n_jobs=-1                  # use all cores for speed
)

# Fit model
rf_model.fit(x_train, y_train)

# Predict
y_pred = rf_model.predict(x_test)


# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Recall (charged off):", recall_score(y_test, y_pred, pos_label=1))
print("Recall (fully paid):", recall_score(y_test, y_pred, pos_label=0))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))