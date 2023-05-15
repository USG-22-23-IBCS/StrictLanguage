import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Class to store prediction data
class Prediction:
    def __init__(self, index, animal_type, probabilities):
        self.index = index
        self.animal_type = animal_type
        self.probabilities = probabilities
    
    
# Load the training data
train_data = pd.read_csv('PuffinandPenguin.csv')

# Drop the "animal" column from the training data
X_train = train_data.drop('Animal', axis=1)
y_train = train_data['Animal']

# Fit the classifier to the training data
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# Load the new data
new_data = pd.read_csv('PuffinandPenguin1.csv')

# Separate the features from the target variable
X_new = new_data[['Length', 'Mass']]

# Make predictions on the new data
pred_animal = clf.predict(X_new)
probs = clf.predict_proba(X_new)


predictions = []
for i in range(len(pred_animal)):
    animal_type = pred_animal[i]
    probabilities = probs[i]
    predictions.append(Prediction(i, animal_type, probabilities))

# Print the predicted species and corresponding probabilities
# for i, animal in enumerate(pred_animal):
#    print(f"Sample {i+1}: {animal}, Probabilities: {probs[i]}")

for prediction in predictions:
    print(f"Sample: {prediction.index}: {prediction.animal_type}, Probabilities: {prediction.probabilities}")
