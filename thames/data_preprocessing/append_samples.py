import os
import sys
import pandas as pd


"""
Usage: python main.py "<dir_new_samples_path>" "<dir_store_path>" "<filename_new_samples>" "<file_old_samples_path>"
    where
        <dir_new_samples_path>: path to the folder containing the new samples EXCEL files
        <dir_store_path>: path to the folder to store the CSV file  
        <filename_new_samples>: name of the new CSV file to store the samples
        <file_old_samples_path>: [optional] path to the EXCEL or CSV file containing the old samples 
"""


# function to concatenate all the new samples excel files in a folder
def new_samples_loop(path):
    dataframe = pd.DataFrame()
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            data = pd.read_excel(f)
            dataframe = pd.concat([dataframe, data], ignore_index=True)
    return dataframe


if __name__ == "__main__":
    # path to the folder containing the new samples excel files
    dir_new_samples_path = sys.argv[1]
    if not os.path.isdir(dir_new_samples_path):
        raise ValueError(
            "The path to the folder containing the new samples excel files is not a directory"
        )

    # path to the folder store the concatenated excel file
    dir_store_path = sys.argv[2]
    if not os.path.isdir(dir_store_path):
        raise ValueError(
            "The path to store the concatenated excel file is not a directory"
        )

    # concatenate all the new samples excel files in a folder
    df = new_samples_loop(dir_new_samples_path)

    # path to the file containing the old samples excel file
    if len(sys.argv) > 4:
        file_old_samples_path = sys.argv[4]
        if not os.path.isfile(file_old_samples_path):
            raise ValueError(
                "The path to the file containing the old samples excel file is not a file"
            )

        # check file extension
        if file_old_samples_path.endswith(".xlsx"):
            old_samples_df = pd.read_excel(file_old_samples_path)
        elif file_old_samples_path.endswith(".csv"):
            old_samples_df = pd.read_csv(file_old_samples_path)
        else:
            raise ValueError("The file extension is not supported")

        # concatenate the old samples and new samples
        df = pd.concat([old_samples_df, df], ignore_index=True)

    # store the concatenated file
    new_filename = (
        sys.argv[3] if sys.argv[3] is not None else "historical_samples.csv"
    )
    df.to_csv(os.path.join(dir_store_path, new_filename), index=False)
