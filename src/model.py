"""
Model module for training a simple machine learning model.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)

if __name__ == "__main__":
    print(f"Model accuracy: {accuracy}")
