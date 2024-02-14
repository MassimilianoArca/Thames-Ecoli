import os
import pandas as pd
import urllib.error


dates = (
    pd.date_range(start="2023-05-05", end="2023-09-09", freq="D")
    .strftime("%Y-%m-%d")
    .values
)

complete_df = pd.DataFrame()

for date in dates:
    url = f"https://environment.data.gov.uk/flood-monitoring/archive/readings-{date}.csv"
    try:
        df = pd.read_csv(url)

        # complete_df = pd.concat([complete_df, df])
        df.to_csv(
            os.path.join("thames", "data", "historical_archive", f"{date}.csv")
        )
    except (pd.errors.EmptyDataError, urllib.error.HTTPError):
        pass

# complete_df.to_csv(os.path.join('..', 'data', 'historical_archive', 'complete.csv'))
