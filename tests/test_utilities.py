# path: tests/test_utilities.py

import pandas as pd
import pytest
from datetime import datetime
from src.scripts.utilities import (
    add_datetime_column,
    convert_fractional_date,
    parse_hdf_data,
    flag_occurrences,
)


# === Test add_datetime_column ===
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            {"year": [2020], "day": [1], "hr": [0]},
            {
                "datetime": [datetime(2020, 1, 1, 0)],
                "year": [2020],
                "day": [1],
                "hr": [0],
            },
        ),  # ID: HappyPath-SingleRow
        (
            {"year": [2020, 2020], "day": [1, 2], "hr": [0, 23]},
            {
                "datetime": [datetime(2020, 1, 1, 0), datetime(2020, 1, 2, 23)],
                "year": [2020, 2020],
                "day": [1, 2],
                "hr": [0, 23],
            },
        ),  # ID: HappyPath-MultipleRows
        (
            {"year": [], "day": [], "hr": []},
            {"datetime": [], "year": [], "day": [], "hr": []},
        ),  # ID: EdgeCase-EmptyDataFrame
    ],
)
def test_add_datetime_column(input_data, expected_output):
    # Arrange
    df_input = pd.DataFrame(input_data)
    df_expected = pd.DataFrame(expected_output)
    df_expected["datetime"] = pd.to_datetime(df_expected["datetime"])

    # Act
    df_result = add_datetime_column(df_input)

    # Assert
    pd.testing.assert_frame_equal(
        df_result.reset_index(drop=True), df_expected.reset_index(drop=True)
    )


# === Test convert_fractional_date ===
@pytest.mark.parametrize(
    "input_number, expected_date",
    [
        (2020.5, datetime(2020, 7, 2)),  # ID: HappyPath-MidYear
        (2020, datetime(2020, 1, 1)),  # ID: EdgeCase-StartOfYear
        (2020.9999, datetime(2020, 12, 31)),  # ID: EdgeCase-EndOfYearApprox
    ],
)
def test_convert_fractional_date(input_number, expected_date):
    # Act
    result_date = convert_fractional_date(input_number)

    # Assert
    assert result_date == expected_date


# === Test parse_hdf_data ===
@pytest.mark.parametrize(
    "file_content, expected_df",
    [
        (
            "BEGIN DATA\nCol1 Col2\n1.0 2.0\n3.0 4.0",
            pd.DataFrame({"Col1": [1.0, 3.0], "Col2": [2.0, 4.0]}),
        ),  # ID: HappyPath-SimpleData
        (
            "Col1 Col2\nBEGIN DATA\nCol1 Col2\n1.0 2.0\n3.0 4.0",
            pd.DataFrame({"Col1": [1.0, 3.0], "Col2": [2.0, 4.0]}),
        ),  # ID: EdgeCase-DataAfterHeader
        (
            "BEGIN DATA\nCol1 Col2",
            pd.DataFrame(columns=["Col1", "Col2"]),
        ),  # ID: EdgeCase-NoData
    ],
)
def test_parse_hdf_data(tmp_path, file_content, expected_df):
    # Arrange
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hdf_data.txt"
    p.write_text(file_content)

    # Act
    result_df = parse_hdf_data(p)

    # Assert
    pd.testing.assert_frame_equal(result_df, expected_df, check_dtype=False)


# === Test flag_occurrences ===
@pytest.mark.parametrize(
    "input_df, flag, expected_df",
    [
        (
            pd.DataFrame({"A": [1, 2, 3], "B": [3, 2, 1]}),
            2,
            pd.DataFrame(
                {
                    "A": [1, 2, 3],
                    "B": [3, 2, 1],
                    "Flag_Count": [0, 2, 0],
                    "Flag_Proportion": [0.0, 1.0, 0.0],
                }
            ),
        ),  # ID: HappyPath-IntegerFlag
        (
            pd.DataFrame({"A": [0.1, 0.2, 0.3], "B": [0.3, 0.2, 0.1]}),
            0.2,
            pd.DataFrame(
                {
                    "A": [0.1, 0.2, 0.3],
                    "B": [0.3, 0.2, 0.1],
                    "Flag_Count": [0, 2, 0],
                    "Flag_Proportion": [0.0, 1.0, 0.0],
                }
            ),
        ),  # ID: HappyPath-FloatFlag
        (
            pd.DataFrame({"A": [], "B": []}),
            1,
            pd.DataFrame({"A": [], "B": [], "Flag_Count": [], "Flag_Proportion": []}),
        ),  # ID: EdgeCase-EmptyDataFrame
    ],
)
def test_flag_occurrences(input_df, flag, expected_df):
    # Act
    result_df = flag_occurrences(input_df, flag)

    # Assert
    pd.testing.assert_frame_equal(result_df, expected_df)
