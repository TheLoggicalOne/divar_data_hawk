from datasets import load_dataset
import pyarrow.parquet as pq
import pandas as pd
import os
from pathlib import Path
import json

# local_directory = '/home/ali/ProgrammingProjects/divar_data_hawk'
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# how many levels up is the root from current file? 0 if we are in the root
CURRENT_REL_DEPTH = 0

ROOT_DIR = str(Path(CURRENT_DIR).parents[CURRENT_REL_DEPTH])

DATA_DIR = ROOT_DIR

RAW_DATA_DIR_NAME = "train"
RAW_DATA_PATH = os.path.join(DATA_DIR,RAW_DATA_DIR_NAME)

def download_data_if_not_exist(data_path_name_to_check=RAW_DATA_PATH):
    #TODO improve the check
    if not os.path.exists(data_path_name_to_check):
        if (confirmation:=input("Are you sure you want to download data?")) in {"yes","y","Y","YES"}:
            dataset = load_dataset('divaroffical/real_estate_ads')
            dataset.save_to_disk(DATA_DIR)
            print(f"Dataset saved to {DATA_DIR}")



# Define the path to the train folder
train_folder = "/home/ali/ProgrammingProjects/divar_data_hawk/train"





# Load the state.json file to get the data file names
with open(os.path.join(train_folder, "state.json"), "r") as f:
    state = json.load(f)

# Iterate through the data files and convert them to CSV
data_files = state["_data_files"]
for i, data_file in enumerate(data_files):
    file_path = os.path.join(train_folder, data_file["filename"])
    
    # Read the Arrow table
    table = pq.read_table(file_path)
    
    # Convert to pandas DataFrame
    df = table.to_pandas()
    
    # Save to CSV
    csv_file_path = os.path.join(train_folder, f"data_part_{i}.csv")
    df.to_csv(csv_file_path, index=False)
    print(f"Saved: {csv_file_path}")



