"""Social media data analysis and regression model example.

This script loads a CSV file containing metrics for social media posts, performs
simple feature engineering, trains a linear regression model to predict views,
and evaluates its performance. The goal is to illustrate the process of
turning raw engagement metrics into actionable insights.

Author: Ahmet Tanık
Date: 2024
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load the CSV dataset into a pandas DataFrame."""
    df = pd.read_csv(path)
    # Convert posting_time (HH:MM) into an hour of day as numeric feature
    df['hour'] = df['posting_time'].str.split(':').str[0].astype(int)
    return df


def build_model(df: pd.DataFrame):
    """Build and train a regression model to predict views from features."""
    X = df[['hour', 'hashtags', 'content_type']]
    y = df['views']
    # Preprocess categorical features
    preprocessor = ColumnTransformer(
        transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), ['content_type'])],
        remainder='passthrough',
    )
    model = Pipeline(steps=[('preprocess', preprocessor), ('regressor', LinearRegression())])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    print(f"R² score: {score:.2f}")
    return model, X_test, y_test, y_pred


def plot_results(y_true, y_pred):
    """Plot actual vs. predicted views."""
    plt.scatter(y_true, y_pred)
    plt.xlabel('Actual views')
    plt.ylabel('Predicted views')
    plt.title('Actual vs. Predicted Views')
    # Add diagonal line
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--')
    plt.show()


def main():
    df = load_data('sample_data.csv')
    model, X_test, y_test, y_pred = build_model(df)
    plot_results(y_test, y_pred)


if __name__ == '__main__':
    main()