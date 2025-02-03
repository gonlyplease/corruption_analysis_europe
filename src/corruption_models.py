##corruption.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# Sklearn libraries for modeling
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
import shap
import xgboost as xgb

# Own Functions

from linear_regression import linear_reg
from metrics import get_metrics
from load_data import load_data
from create_correlation import correlation

path = "../data/processed/corruption_dataset.csv"

corruption_dataset = load_data(path=path)

corruption_dataset.head()

# Exclude the specified features from the correlation matrix


## 5. Model the Data

columns_to_remove = [
    "iso3_code",
    "country",
    "corruption_perceptions_index_score",
    "control_of_corruption",
    "rule_of_law",
    "gov_effectiveness",
    "year",
]

filtered_dataset = corruption_dataset.drop(columns=columns_to_remove)

correlation(filtered_dataset, "corruption_perceptions_index_score")

# Create feature set X and target y
X = corruption_dataset.drop(
    columns=columns_to_remove, errors="ignore"
)  # 'errors=ignore' handles columns that may not exist
y = corruption_dataset["corruption_perceptions_index_score"].values  # Our target

print(X.columns)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_test.shape
X_train.shape


y_train_pred, y_test_pred = linear_reg(X_train=X_train, y_train=y_train, X_test=X_test)

get_metrics(
    y_train=y_train,
    y_train_pred=y_train_pred,
    y_test=y_test,
    y_test_pred=y_test_pred,
    X=X,
    y=y,
)
