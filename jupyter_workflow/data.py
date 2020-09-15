import pandas as pd
import os
from urllib.request import urlretrieve


def get_url_rawdata(name_rawdata_file=None, url=None, force_url_download=False):
    """Download and cache data
    
    PARAMETERS
    ----------
    name_rawdata_file : string
        location and name to save the data file
    url : string
        loacation to download the data
    force_url_download : boolean (optional)
        option to force downloading the raw data
    
    Returns
    -------
    rawdata : file, type as input in name_rawdata_file (e.g. .csv etc)
    """
    if force_url_download or not os.path.exists(name_rawdata_file):
        rawdata, _ = urlretrieve(url, name_rawdata_file)
    else:
        rawdata = name_rawdata_file
    return rawdata


def read_csvdata_to_df_with_dateindex(
    rawdata_filename, column_names=None, parse_dates=True
):
    """Reading a rawdata file into pandas dataframe

    OPTIONINAL
    ----------
    column_names :
        Pass a list of column names to substitute the current names (from left to right)
    parse_dates :
        Transforming the string dates in raw data to pandas DateIndex type
    
    PARAMETERS
    ----------
    name_rawdata_file : string
        location and name to save the data file
    url : string
        loacation to download the data
    force_url_download : boolean (optional)
        option to force downloading the raw data
    
    Returns
    -------
    data : pandas.Dataframe
    """
    data = pd.read_csv(
        rawdata_filename, index_col="Date", parse_dates=parse_dates
    )  # Note the parse_dates=True 'magically' convert the date format to pandas datetime
    if column_names:
        data.columns = column_names
    return data


# Testing
# test_rawdata = get_url_rawdata(
#     name_rawdata_file="fremont.csv",
#     url="https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD",
# )

# df = read_csvdata_to_df_with_dateindex(
#     rawdata_filename=test_rawdata, column_names=["Total", "East", "West"]
# )
# print(df)
