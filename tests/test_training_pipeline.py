 
import numpy as np
from sklearn.ensemble import RandomForestClassifier


def make_synthetic_dataset():
    """Create a small synthetic dataset for testing."""
    rng = np.random.default_rng(42)

    X = rng.normal(size=(30, 4))
    y = np.array([0, 1, 2] * 10)

    return X, y


def test_training_pipeline_runs_without_error():
    """Test that the model can be trained successfully."""
    X, y = make_synthetic_dataset()

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )

    model.fit(X, y)

    assert hasattr(model, "predict")


def test_training_pipeline_prediction_shape():
    """Test that predictions have the correct shape."""
    X, y = make_synthetic_dataset()

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )

    model.fit(X, y)

    preds = model.predict(X)

    assert preds.shape == (len(X),)


def test_training_pipeline_prediction_probabilities():
    """Test that prediction probabilities sum to 1."""
    X, y = make_synthetic_dataset()

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )

    model.fit(X, y)

    probabilities = model.predict_proba(X)

    row_sums = probabilities.sum(axis=1)

    assert np.allclose(row_sums, 1.0, atol=1e-6)