from sklearn.ensemble import IsolationForest


def detect_anomaly(logs):
    """
    Simple AI anomaly detection using log length
    """

    # Convert logs to numeric feature (length of log)
    X = [[len(log)] for log in logs]

    # Train model
    model = IsolationForest(contamination=0.1)
    model.fit(X)

    # Predict
    predictions = model.predict(X)

    return predictions