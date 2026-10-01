import mlflow
import pandas as pd

# Connect to MLflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Load model from Staging
model_uri = "models:/iris-classifier/Staging"

model = mlflow.sklearn.load_model(model_uri)

print("=" * 60)
print("REGISTERED MODEL LOADED SUCCESSFULLY")
print("=" * 60)

# Load test data
df = pd.read_csv("data/processed/iris_features.csv")

# Features used during training
FEATURE_COLS = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "sepal_area",
    "petal_area",
    "sepal_to_petal_length_ratio"
]

X_test = df[FEATURE_COLS].head(5)

# Make predictions
predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)

print("\nModel URI:")
print(model_uri)

print("\nTest completed successfully!")