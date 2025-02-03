"""
Author: gk
Date: 29-01-2025
Name: create_correlation.py
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def correlation(df, target_corr):
    """Main function"""
    # Correlation matrix without the excluded features
    corr_matrix = df.corr(numeric_only=True)

    # Sort correlation of each feature with the target
    target_corr = corr_matrix[target_corr].sort_values(ascending=False)
    print("Correlation with CPI Score (Excluding Certain Features):\n", target_corr)

    # Visualize the full correlation heatmap
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=False, cmap="coolwarm", center=0)
    plt.title("Correlation Heatmap (Excluding Certain Features)")
    plt.show()
