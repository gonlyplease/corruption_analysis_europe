if __name__ == "__main__":
    # Load data
    corruption_dataset = load_data()

    # Preprocess data
    X, y, X_train, X_test, y_train, y_test = preprocess(corruption_dataset)

    # Train and evaluate models
    results = train_models(X_train, y_train, X_test, y_test)
