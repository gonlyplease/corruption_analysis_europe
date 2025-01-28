# Metrics

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt


def get_metrics(y_train, y_train_pred, y_test, y_test_pred, X, y):
    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_mae = mean_absolute_error(y_train, y_train_pred)
    test_mae = mean_absolute_error(y_test, y_test_pred)
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    # Print results
    print("\nLinear Regression Baseline Metrics:")
    print(f"Training MSE: {train_mse:.3f}")
    print(f"Testing MSE: {test_mse:.3f}")
    print(f"Training MAE: {train_mae:.3f}")
    print(f"Testing MAE: {test_mae:.3f}")
    print(f"Training R²: {train_r2:.3f}")
    print(f"Testing R²: {test_r2:.3f}")

    # Visualize predictions vs actual values

    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_test_pred, alpha=0.6)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color="red", linestyle="--")
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Linear Regression: Actual vs Predicted")
    plt.show()
