"""
This module trains a simple machine learning model and saves it.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_model():
    """
    Train a Logistic Regression model on the Iris dataset.
    """
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    joblib.dump(model, 'model.pkl')

def add(a, b):
    """
    Add two numbers.
    """
    return a + b

if __name__ == "__main__":
    train_model()
