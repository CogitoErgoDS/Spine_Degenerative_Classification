import numpy as np
import pandas as pd
# Define the path
from pathlib import Path
# Define the path
full_sample = False

path = Path('C:/Users/HP1/Desktop/Spiced/capstone-project/data')
path_vor = Path('C:/Users/HP1/Desktop/Spiced/capstone-project/data/vorlauf')
 
# some code here
# Load CSV files
X_train = pd.read_csv(path / "train.csv")
X_train_coor = pd.read_csv(path / "train_label_coordinates.csv")
X_train_des = pd.read_csv(path / "train_series_descriptions.csv")
X_test_des = pd.read_csv(path / "test_series_descriptions.csv")
submission_df = pd.read_csv(path / "sample_submission.csv")

study_ids_to_keep = [4003253]
def keep_persons(X_train, X_train_coor, X_train_des, study_ids_to_keep, all_studies=full_sample):
    if all_studies == True:
        return X_train, X_train_coor, X_train_des
    else:
        
        X_train = X_train[X_train['study_id'].isin(study_ids_to_keep)]
        X_train_coor = X_train_coor[X_train_coor['study_id'].isin(study_ids_to_keep)]
        X_train_des = X_train_des[X_train_des['study_id'].isin(study_ids_to_keep)]
    return X_train, X_train_coor, X_train_des

X_train, X_train_coor, X_train_des = keep_persons(
    X_train, X_train_coor, X_train_des, study_ids_to_keep, all_studies=full_sample 
)

# Save the filtered dataframes to CSV files
file_names = ["X_train.csv", "X_train_coor.csv", "X_train_des.csv"]
dataframes = [X_train, X_train_coor, X_train_des]

for df, file_name in zip(dataframes, file_names):
    df.to_csv(path_vor / file_name, index=False)


 


    
