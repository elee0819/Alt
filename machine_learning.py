#machine_learning.py
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Define the dataset file name
dataset_file = 'dataset.csv'

# Get the current directory
current_dir = os.getcwd()

# Construct the dataset file path
dataset_path = os.path.join(current_dir, dataset_file)

# Check if the dataset file exists
if not os.path.isfile(dataset_path):
    # Dataset file does not exist, generate a synthetic dataset
    num_samples = 1000
    num_features = 10
    num_classes = 2

    # Generate synthetic dataset
    X = np.random.randn(num_samples, num_features).astype(np.float32)
    y = np.random.randint(num_classes, size=num_samples)

    # Create a DataFrame from the generated data
    dataset = pd.DataFrame(X, columns=[f'feature{i}' for i in range(num_features)], dtype=np.float32)
    dataset['target'] = y.astype(np.int32)

    # Save the synthetic dataset to the specified path
    dataset.to_csv(dataset_path, index=False)
    print(f"Dataset file not found. Created a synthetic dataset at: {dataset_path}")

# Load the dataset
dataset = pd.read_csv(dataset_path)

# Split the dataset into features and target
X = dataset.drop('target', axis=1)
y = dataset['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a dictionary to store model names and corresponding instances
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier()
}

# Train and evaluate the models using cross-validation
results = {}
for model_name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5)
    accuracy = scores.mean()
    results[model_name] = accuracy

# Sort the models based on accuracy in descending order
sorted_results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}

# Print the model performance results
for model_name, accuracy in sorted_results.items():
    print(f"{model_name} Accuracy: {accuracy}")

# Train the best performing model on the full training set
best_model_name = next(iter(sorted_results))
best_model = models[best_model_name]
best_model.fit(X_train, y_train)

# Make predictions on the test set
predictions = best_model.predict(X_test)

# Calculate accuracy on the test set
test_accuracy = accuracy_score(y_test, predictions)
print(f"Best Model Test Accuracy: {test_accuracy}")