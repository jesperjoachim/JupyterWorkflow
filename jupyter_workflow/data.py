import pandas as pd
import os
from urllib.request import urlretrieve


def get_url_data(rawdata_filename=None, url=None, force_url_download=False):
    """Download and cache data
    
    PARAMETERS
    ----------
    rawdata_filename : string
        location to save the date
    url : string
        loacation to download the data
    force_url_download : boolean (optional)
        option to force downloading the raw data
    
    Returns
    -------
    data : pandas.Dataframe
    """
    if force_url_download or not os.path.exists(rawdata_filename):
        urlretrieve(url, rawdata_filename)
    data = pd.read_csv(
        rawdata_filename, index_col="Date", parse_dates=False
    )  # Note the parse_dates=True 'magically' convert the date format to pandas datetime
    data.columns = ["Total", "East", "West"]
    return data
