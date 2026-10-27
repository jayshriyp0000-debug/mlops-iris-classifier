# Testing Strategy

## 1. Introduction
The purpose of this testing strategy is to verify the correctness and reliability of the Iris machine learning project. Unit tests are used to check data preprocessing, feature engineering, data validation, the training pipeline, and model quality.

## 2. Testing Objectives
- Verify that duplicate records are removed correctly.
- Check handling of missing values and empty data.
- Verify that engineered features are calculated correctly.
- Check data validation rules, including missing columns, invalid species, and out-of-range values.
- Ensure the training pipeline runs successfully and produces valid predictions.
- Check the quality of the trained model.

## 3. Testing Tools
- **Python 3.11.3:** Programming language.
- **pytest:** Unit testing framework.
- **pytest-cov:** Code coverage measurement.
- **scikit-learn:** Machine learning model development and evaluation.

## 4. Testing Approach
The project uses unit tests to test individual functions and integration-style tests to check the training pipeline. Model quality is checked using a separate model quality test.

The test modules are:
- `test_preprocess.py`
- `test_features.py`
- `test_validate.py`
- `test_training_pipeline.py`
- `test_model_quality.py`

## 5. Test Execution
The tests were executed using pytest. The following command was used to run the complete test suite and generate coverage and XML reports:

`pytest --cov=src --cov-report=term-missing --junitxml=test-results.xml`

## 6. Test Results
A total of 15 tests were collected and executed.

- Tests passed: 15
- Tests failed: 0
- Execution time: 4.65 seconds
- Overall code coverage: 19%
- XML report: `test-results.xml`

All 15 tests passed successfully. The overall coverage is 19% because the coverage report includes additional source files that are not exercised by the current test suite.

## 7. Conclusion
The unit testing process verified the main data processing functions, validation rules, training pipeline, and model quality checks. All 15 tests passed successfully. Further tests can be added to improve coverage of the remaining source files.
