import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/processed_data/loan_processed_3.csv')
#Correlatoion / relationship

print("=========== 6.Correlatoion / relationship=======")
corr = df.select_dtypes(include=['float64','int64']).corr()

print(corr['loan_amnt'].sort_values(ascending=False))
plt.figure(figsize =(12,10))
sns.heatmap(corr,annot=True,fmt='.2f',cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('plots/Correlation_heatmap.png')
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
df = df.drop(['installment', 'fico_range_high','grade '], axis=1)
df.to_csv('data/processed_data/loan_processed_4.csv')