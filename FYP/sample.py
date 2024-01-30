import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset with latitude, longitude, and ocean basin labels
values = pd.read_csv('myvalues.csv')

# Split dataset into features and labels
X = values[['Latitude', 'Longitude']]
y = values['ocean_basin']

# Create decision tree classifier and fit it to the data
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Predict the ocean basin for a new set of coordinates
new_coords = [[30.5, -70.2]]
predicted_basin = clf.predict(new_coords)

print("Predicted ocean basin: ", predicted_basin)