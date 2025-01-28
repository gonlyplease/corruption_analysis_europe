##linear.regression.py

from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer


# Initialize and train Linear Regression model


def linear_reg(
    X_train,
    y_train,
    X_test,
):
    lin_reg = LinearRegression()

    imputer = SimpleImputer(strategy="mean")  # or 'median', 'most_frequent'
    X_train_imputed = imputer.fit_transform(X_train)
    X_test_imputed = imputer.transform(X_test)

    lin_reg.fit(X_train_imputed, y_train)

    # Predictions
    y_train_pred = lin_reg.predict(X_train_imputed)  # Training predictions
    y_test_pred = lin_reg.predict(X_test_imputed)  # Testing predictions

    return y_train_pred, y_test_pred
