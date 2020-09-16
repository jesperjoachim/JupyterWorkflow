import os
from jupyter_workflow.data import read_csvdata_to_df_with_dateindex
import pytest
import pandas as pd

"""Raw data used for test"""


@pytest.fixture()
def csvForTest():
    csv_file = "/home/jesper/Work/ReprodcibleDA/JupyterWorkflow/tests/Fremont.csv"
    return csv_file


"""END Raw data used for test"""

# Testing Fremont data is available
def test_csv_testfile_is_available():
    # Setup
    desired = True
    # Exercise
    actual = os.path.exists("Fremont.csv")
    # Verify
    assert actual == desired


# Tests
def test_column_names_is_correct(csvForTest):
    # Setup
    desired = ["Total", "East", "West"]
    # Exercise
    csv_file = csvForTest
    dataframe = read_csvdata_to_df_with_dateindex(
        rawdata_filename=csv_file, column_names=["Total", "East", "West"]
    )
    actual = dataframe.columns
    # Verify
    actual == desired
