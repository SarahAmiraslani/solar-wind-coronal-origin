# path: src/scripts/utilities.py

"""
utilities.py
------------
This module provides utility functions for date and time manipulation.
"""
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt


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


# === Data Quality Functions ===
def flag_occurrences(df, flag):
    """
    Counts the occurrences of a specific flag in each row of a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to count flag occurrences in.
        flag: The flag to count occurrences of.

    Returns:
        pandas.DataFrame: The input DataFrame with an additional column "Flag_Count" that contains the count of flag occurrences in each row.
    """
    df["Flag_Count"] = df.apply(lambda row: row.tolist().count(flag), axis=1)
    numeric_columns = df.select_dtypes(include=["float", "int"]).columns
    df["Flag_Proportion"] = df["Flag_Count"] / df[numeric_columns].shape[1]
    return df


def visualize_flag(flag_df):
    """
    Visualizes the distribution of flag occurrences in a DataFrame.

    Parameters:
        flag_df (pandas.DataFrame): The DataFrame with flag occurrences.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.hist(flag_df["Flag_Count"], bins=10, color="skyblue", edgecolor="black")
    plt.xlabel("Flag Count")
    plt.ylabel("Frequency")
    plt.title("Distribution of Flag Occurrences")
    plt.show()
