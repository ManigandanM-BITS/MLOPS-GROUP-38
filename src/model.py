"""
This module contains the model training code.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data():
    """Load the Iris dataset."""
    data = load_iris()
    return data.data, data.target

def train_model():
    """Train a RandomForest model on the Iris dataset."""
    x_data, y_data = load_data()
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    print(f"Model accuracy: {accuracy}")
    joblib.dump(model, 'model.joblib')

if __name__ == "__main__":
    train_model()
