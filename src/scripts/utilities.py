# path: src/scripts/utilities.py

"""
utilities.py
------------
This module provides utility functions for date and time manipulation.
"""
# Standard library imports
from datetime import datetime, timedelta

# Third-party imports
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce


# === Date Formatting Functions ===
def add_datetime_column(df):
    """
    Adds a datetime column to the DataFrame based on the year, day, and hour columns.

    Parameters:
    df (pandas.DataFrame): The DataFrame to which the datetime column will be added.

    Returns:
    pandas.DataFrame: The DataFrame with the datetime column added.
    """
    # Apply get_datetime() function to year, day, and hour columns
    datetime_column = pd.to_datetime(
        df[["year", "day", "hr"]].astype(str).agg("-".join, axis=1), format="%Y-%j-%H"
    )

    # Insert the new datetime column as the first column of the DataFrame
    df.insert(0, "datetime", datetime_column)

    return df


def convert_fractional_date(number):
    """
    Converts a fractional date to a datetime object.

    Parameters:
        number (float)

    Returns:
        date (datetime)
    """
    year = int(number)
    d = timedelta(days=(number - year) * 365)
    day_one = datetime(year, 1, 1)
    return d + day_one


# === Data Parsing Functions ===
def parse_hdf_data(path):
    """
    Parses the data from an HDF file saved as a text file located at the given path.

    Parameters:
        path (str)

    Returns:
        pandas.DataFrame
    """
    with open(path, "r", encoding="utf-8") as file:

        # find the line with 'BEGIN DATA', skip to next line
        lines = file.readlines()
        begin_data_index = lines.index("BEGIN DATA\n") + 1

        # Define the data and columns starting from begin_data_index
        col_names = lines[begin_data_index].split()
        data = [line.split() for line in lines[begin_data_index + 1 :]]

    return pd.DataFrame(data, columns=col_names, dtype=float)


def merge_dataframes(dataframes, key):
    """
    Merge multiple pandas DataFrames on a common key.

    Args:
    dataframes (list of pd.DataFrame): List of DataFrames to merge.
    key (str): Column name to merge on.

    Returns:
    pd.DataFrame: Merged DataFrame.
    """
    # Reduce function to merge two DataFrames on the specified key
    return reduce(
        lambda left, right: pd.merge(
            left, right, on=key, how="inner", validate="one_to_one"
        ),
        dataframes,
    )


def sort_columns_except_key(df, key_column):
    """
    Sort all columns of the DataFrame alphabetically except the specified key column.

    Args:
    df (pd.DataFrame): The DataFrame to sort.
    key_column (str): The name of the column to keep fixed.

    Returns:
    pd.DataFrame: DataFrame with sorted columns, keeping the key column as is.
    """
    if key_column not in df.columns:
        raise ValueError(f"Key column '{key_column}' not found in DataFrame.")

    # Get all columns except the key column
    columns_to_sort = [col for col in df.columns if col != key_column]
    # Sort these columns
    sorted_columns = sorted(columns_to_sort)
    # Combine the key column with the sorted remaining columns
    new_column_order = [key_column] + sorted_columns
    # Reindex the DataFrame with the new column order
    return df[new_column_order]


# === Data Quality Functions ===
def missing_occurrences(df, flag):
    """
    Counts the occurrences of a specific flag in each row of a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to count flag occurrences in.
        flag: The flag to count occurrences of.

    Returns:
        pandas.DataFrame: The input DataFrame with an additional column
        "Missing_Count" that contains the count of flag occurrences in each row.
    """
    df["Missing_Count"] = df.apply(lambda row: row.tolist().count(flag), axis=1)
    numeric_columns = df.select_dtypes(include=["float", "int"]).columns
    df["Missing_Proportion"] = df["Missing_Count"] / df[numeric_columns].shape[1]
    return df


def visualize_flag(  # The `flag_` prefix is commonly used to indicate variables or
    # columns that represent flags or indicators in a dataset.
    # These flags are typically binary variables that denote the
    # presence or absence of a certain condition, event, or status.
    flag_df,
):
    """
    Visualizes the distribution of flag occurrences in a DataFrame.

    Parameters:
        flag_df (pandas.DataFrame): The DataFrame with flag occurrences.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.hist(
        flag_df["Missing_Count"],
        bins=10,
        color="skyblue",
        edgecolor="black",
    )
    plt.xlabel("Missing Count")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Missing Occurrences Per Timestamp")
    plt.show()


# === Machine Learning Functions ===
