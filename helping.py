import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def Clean_Data(df):
    # Convert numerical columns to numeric types, handling errors and coercing to NaN
    numerical_columns = df.select_dtypes(include='number').columns
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')

    # Impute missing values with the median for numerical columns
    df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].median())

    # Impute missing values with the mode for categorical columns
    categorical_columns = df.select_dtypes(exclude='number').columns
    df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])

    return df



def plot_bar_chart(df, x_col, title=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x=x_col, data=df, ax=ax)
    ax.set_title(title if title else f'Distribution of {x_col}')
    return fig, ax

def plot_histogram(df, numeric_col, bins=20, kde=True, title=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df[numeric_col], bins=bins, kde=kde, ax=ax)
    ax.set_title(title if title else f'Distribution of {numeric_col}')
    return fig, ax

def plot_box_plot(df, x_col, y_col, title=None):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(x=x_col, y=y_col, data=df, ax=ax)
    ax.set_title(title if title else f'Box Plot of {y_col} by {x_col}')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    return fig, ax

def plot_scatter(df, x_col, y_col, title=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=df, ax=ax)
    ax.set_title(title if title else f'Scatter Plot of {y_col} vs. {x_col}')
    return fig, ax

def plot_time_series(df, time_col, numeric_col, ci=None, title=None):
    df[time_col] = pd.to_datetime(df[time_col])
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=time_col, y=numeric_col, data=df, ci=ci, ax=ax)
    ax.set_title(title if title else f'Time Series Plot of {numeric_col} Over Time')
    return fig, ax

def plot_corr_matrix_heatmap(df):
    correlation_matrix = df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Correlation Matrix Heatmap')
    return fig, ax




