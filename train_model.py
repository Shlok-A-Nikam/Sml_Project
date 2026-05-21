import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def load_data(train_path='artifact/train_data.csv', test_path='artifact/test_data.csv'):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test


def preprocess(df):
    df = df.copy()
    # target
    y = df['math score']
    X = df.drop(columns=['math score'])
    # One-hot encode categorical columns
    X = pd.get_dummies(X, drop_first=True)
    return X, y


def train_and_evaluate():
    train, test = load_data()
    X_train, y_train = preprocess(train)
    X_test, y_test = preprocess(test)

    # Align columns
    X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    print(f"Test MAE: {mae:.3f}")

    os.makedirs('artifact', exist_ok=True)
    model_path = os.path.join('artifact', 'model.pkl')
    joblib.dump(model, model_path)
    print('Saved model to', model_path)


if __name__ == '__main__':
    train_and_evaluate()
