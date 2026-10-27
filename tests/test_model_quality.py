# tests/test_model_quality.py
"""
Test the trained model quality on the processed Iris dataset.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
MIN_ACCEPTABLE_ACCURACY = 0.90


def test_model_quality():
    # Load processed feature data
    df = pd.read_csv("data/processed/iris_features.csv")

    # Encode target labels
    encoder = LabelEncoder()
    y = encoder.fit_transform(df["species"])

    # Select model features
    feature_cols = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "sepal_area",
        "petal_area",
        "sepal_to_petal_length_ratio",
    ]

    X = df[feature_cols]

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    # Create and train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42,
    )

    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)

    # Check prediction labels
    assert set(predictions).issubset(set(y))

    # Model should achieve at least 90% accuracy
    assert accuracy >= MIN_ACCEPTABLE_ACCURACY