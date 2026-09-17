# Data Pipeline Documentation

## 1. Overview

This project implements an automated data pipeline for the Iris dataset using DVC.

The pipeline contains four stages:

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Data Validation

The pipeline is defined in `dvc.yaml` and the pipeline state is stored in `dvc.lock`.

## 2. Data Collection

The collection stage uses the Iris dataset and saves the raw data to:

`data/raw/iris_raw.csv`

The dataset contains 150 rows.

## 3. Data Preprocessing

The preprocessing stage:

- Removes duplicate rows
- Converts numeric columns to numeric values
- Handles missing numeric values using median imputation
- Removes rows with missing species
- Removes the `collected_at` column

The processed data is saved to:

`data/processed/iris_preprocessed.csv`

After preprocessing, 149 rows were obtained.

## 4. Feature Engineering

The feature engineering stage creates additional features:

- `sepal_area`
- `petal_area`
- `sepal_to_petal_length_ratio`
- `petal_length_bin`

The final feature dataset contains 9 columns.

Output:

`data/processed/iris_features.csv`

## 5. Data Validation

The validation stage checks:

- Expected columns
- Missing values
- Valid species values
- Valid ranges for Iris measurements

Validation result:

`Validation PASSED: 149 rows, 9 columns, all checks satisfied`

## 6. DVC Pipeline

The pipeline execution order is:

Collection → Preprocessing → Feature Engineering → Validation

The pipeline is automated using DVC.

Command used:

`dvc repro`

A second execution skipped unchanged stages, showing that DVC caching is working.

## 7. DVC Remote

A DVC remote named `myremote` is configured at:

`C:/Users/jaysh/dvc-remote-storage`

The command:

`dvc push`

successfully pushed 3 files to the remote storage.

## 8. Git Version Control

The pipeline files were committed to Git with the commit message:

`Add automated data pipeline`

The commit was pushed to the `conflict-demo-b` branch.

## 9. Pipeline Verification

The following commands were used to verify the pipeline:

`python src\pipeline\collect.py`

`python src\pipeline\preprocess.py`

`python src\pipeline\features.py`

`python src\pipeline\validate.py`

`dvc repro`

`dvc dag`

`dvc push`

The complete pipeline executed successfully and the validation stage passed.