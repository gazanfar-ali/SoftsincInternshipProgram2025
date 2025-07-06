import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.metrics import classification_report, mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import joblib
import os

def load_data(file_path):
    """Loads CSV data from the given file path"""
    return pd.read_csv(file_path)

def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_and_tune_model(model, param_grid, X_train, y_train, cv_folds=5, scoring=None):
    """Train using GridSearchCV with cross-validation"""
    grid = GridSearchCV(model, param_grid, cv=KFold(n_splits=cv_folds), scoring=scoring, n_jobs=-1)
    grid.fit(X_train, y_train)
    return grid.best_estimator_, grid.best_params_, grid.best_score_

def evaluate_classification(model, X_test, y_test):
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print("Classification Report:\n", report)

def evaluate_regression(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"MAE: {mae}\nMSE: {mse}\nRMSE: {rmse}\nR² Score: {r2}")

def save_model(model, filename="trained_model.pkl"):
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

# Example usage template
if __name__ == "__main__":
    # Load data
    data = load_data("your_dataset.csv")  # Replace with actual file
    X = data.drop("target", axis=1)
    y = data["target"]

    # Split
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Select model and parameters
    model = RandomForestClassifier()  # or RandomForestRegressor()
    param_grid = {
        'n_estimators': [50, 100],
        'max_depth': [None, 10, 20]
    }

    # Train and tune
    best_model, best_params, best_score = train_and_tune_model(
        model, param_grid, X_train, y_train, scoring='accuracy'
    )
    print("Best Parameters:", best_params)
    print("Best Cross-Validation Score:", best_score)

    # Evaluate
    evaluate_classification(best_model, X_test, y_test)  # or evaluate_regression()

    # Save
    save_model(best_model)
