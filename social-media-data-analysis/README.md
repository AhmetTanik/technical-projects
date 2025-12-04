# Social Media Data Analysis & ML Model

This project demonstrates how to collect, preprocess, and analyse engagement metrics from social media posts (such as TikTok videos) and build a regression model to predict future performance. The goal of the original project was to provide data‑driven recommendations that increased average views per post by **20 %**【423963862728788†L65-L66】.

## Overview

In 2024 I analysed metrics from two TikTok channels with over **160 k followers** to understand how posting time, hashtags, and content type influence engagement【423963862728788†L57-L63】. Using Python libraries like `pandas` and `scikit‑learn`, I engineered features, trained multiple regression models, and achieved an **R² score of 0.82** on the best model【423963862728788†L61-L63】.

This repository provides a simplified example you can run locally. It includes a small synthetic dataset, a Python script to train and evaluate a regression model, and instructions for extending the analysis.

## Structure

```text
social-media-data-analysis/
├── README.md            ← Project documentation (this file)
├── sample_data.csv      ← Synthetic dataset with posting metrics and engagement
└── data_analysis.py      ← Python script for data loading, feature engineering, model training, and evaluation
```

## Getting Started

1. **Install dependencies**: Ensure you have Python 3.8+ installed. You can install the required libraries with:

   ```bash
   pip install pandas scikit-learn matplotlib
   ```

2. **Inspect the data**: Open `sample_data.csv` to see the structure of the dataset. Each row includes posting time, number of hashtags, content type encoded as a categorical variable, views, and likes.

3. **Run the analysis**: Execute the script:

   ```bash
   python data_analysis.py
   ```

   The script will load the dataset, preprocess the features (including one‑hot encoding for categorical variables), train a linear regression model, report the R² score, and plot actual vs. predicted views.

## Extending This Project

To adapt this example to your own data:

* Replace `sample_data.csv` with your dataset exported from your social media platform (e.g., TikTok, Instagram). Ensure that the CSV contains numeric and categorical variables.
* Experiment with different models (Random Forests, Gradient Boosting, Neural Networks) using `scikit‑learn`.
* Split the data into training and testing sets to avoid overfitting.
* Use advanced feature engineering (e.g., text sentiment, trending topics) to improve predictions.

## License

This example is provided for educational purposes under the MIT License. Feel free to modify and adapt it for your own analyses.