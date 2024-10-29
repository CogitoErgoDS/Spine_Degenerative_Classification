import os
import sys
import numpy as np
import pandas as pd

# Define the path
import sys
from pathlib import Path
import importlib

# Define the path to the project directory and add it to sys.path
project_dir = Path("c:/Users/HP1/Desktop/Spiced/capstone-project")
sys.path.append(str(project_dir)) 
 
 
with open("help_files/_0_definitions.py") as file:
    exec(file.read())


# some code here
# Load CSV files
X_train = pd.read_csv(data_path / "train.csv")
X_train_coor = pd.read_csv(data_path / "train_label_coordinates.csv")
X_train_des = pd.read_csv(data_path / "train_series_descriptions.csv")
X_test_des = pd.read_csv(data_path / "test_series_descriptions.csv")
submission_df = pd.read_csv(data_path / "sample_submission.csv")


## Filter the dataframes to keep only the study IDs that are in the list study_ids_to_keep


from help_files._0_definitions import keep_persons, study_ids_to_keep, all_persons
 
dataframes = [X_train, X_train_coor, X_train_des]

for i in range(len(dataframes)):
    dataframes[i] = keep_persons(dataframes[i], study_ids_to_keep, all_persons)
    print(f"df {i} ", dataframes[i].shape)

 
# Save the filtered dataframes to CSV files
file_names = ["X_train.csv", "X_train_coor.csv", "X_train_des.csv"]
for df, file_name in zip(dataframes, file_names):
    print(f"df ",df.shape)
    df.to_csv(data_path_vor / file_name, index=False)


 


    
