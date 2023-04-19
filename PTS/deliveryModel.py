import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load the delivery dataset
df = pd.read_csv('delivery_dataset.csv')

# Convert categorical variables to numerical variables using label encoding
le = LabelEncoder()
df['Source_Pincode'] = le.fit_transform(df['Source_Pincode'])
df['Destination_Pincode'] = le.fit_transform(df['Destination_Pincode'])

# Split the data into training and testing sets
X = df.drop(['Number_of_Days'], axis=1)
y = df['Number_of_Days']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest regressor on the training data
rf = RandomForestRegressor(n_estimators=20, random_state=42)
rf.fit(X_train, y_train)

# Predict the number of days for the testing data and calculate the mean squared error
y_pred = rf.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)

# dump the model to a file using pickle
joblib.dump(rf, 'model.joblib')
joblib.dump(le, 'encoder.joblib')
# with open('delivery_model.pkl', 'wb') as f:
#     pickle.dump((rf, le), f)

# # Convert the source and destination pin codes to numerical values using the label encoder
# source_pincode = '560068'
# destination_pincode = '465669'
# source_pincode_encoded = le.transform([source_pincode])[0]
# destination_pincode_encoded = le.transform([destination_pincode])[0]

# # Use the trained random forest regressor to predict the number of days
# num_days = rf.predict([[source_pincode_encoded, destination_pincode_encoded]])
# print('Predicted number of days:', num_days[0])
