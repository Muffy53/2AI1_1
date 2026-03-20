import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv('insurance_data_linear.csv')
df.head()
df.info()

#This creates a tool that converts labels - numbers
df = pd.get_dummies(df,columns = ['sex','smoker','region'], drop_first=True)

# fit_transform(): learns categories and converts them into numbers
print("Categorical variables encoded successsfully ")
print(df.head())
