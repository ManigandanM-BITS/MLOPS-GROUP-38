# src/model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_and_save_model():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    # Save the model
    joblib.dump(model, 'model.joblib')
    print("Model trained and saved as model.joblib")

if __name__ == "__main__":
    train_and_save_model()
