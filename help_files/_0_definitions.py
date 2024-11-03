### overal globals that are used in the project
## different paths setting
# Define the paths to the data
# Define the path
import sys
from pathlib import Path
import importlib
data_path = Path('C:/Users/HP1/Desktop/Spiced/capstone-project/data')
data_path_vor = Path('C:/Users/HP1/Desktop/Spiced/capstone-project/data/vorlauf')
all_persons = True
study_ids_to_keep = [4003253] 
number_persons_train = 30

 


def keep_persons(df, study_ids_to_keep, all_persons):
    if all_persons:
        return df  # Return all DataFrames if all_studies is True
    else:
        df = df[df['study_id'].isin(study_ids_to_keep)]
    return df


RSEED = 42
# put True if full sample and False if not
full_sample = True
frac = 0.5


 
## take a sample of the data 
def generate_sample(df):
    if df.isnull().values.any():
        print("DataFrame contains missing values.")
    else:
        print("DataFrame does not contain any missing values.")
        
    if not full_sample:
        df_sample = df.sample(frac=frac, random_state=RSEED)
        df = df_sample
        print(f"Only {frac * 100}% sample", df.shape)
        print(10 * "#")
    else:
        print("No changes", df.shape)
        print(10 * "#")
        
    return df  # Return the modified DataFrame


def dummies(list_dum):
    # Check if there are any object type columns to create dummy variables for
    if df.select_dtypes(include=['object']).shape[1] > 0:
        df_dummies = pd.get_dummies(df, drop_first=True)
    df = df_dummies
    df.head() # display first 5 rows of dataframe
    return ()
 

# check how many duplicated rows exist in the data frame
def check_duplicates(df):
    duplicates_count = df.duplicated().value_counts()
    duplicates = df[df.duplicated()]
    sorted_duplicates = duplicates.sort_values(by=list(duplicates.columns))
    print(duplicates)
    print("Number of duplicate rows:", duplicates.shape[0])

def count_severity_by_condition_level(X_train):
    # Drop duplicates to ensure each 'study_id' is only counted once per 'condition' and 'level'
    unique_data = X_train.drop_duplicates(subset=['study_id', 'condition', 'level', 'severity'])
    
    # Group by 'condition', 'level', and 'severity' and count occurrences
    severity_counts = unique_data.groupby(['condition', 'level', 'severity']).size().reset_index(name='count')

    shape_df = X_train.shape
    # Display the result
    print(f"Shape of the DataFrame: {shape_df}")
    print(severity_counts)
    return severity_counts

# IMpute missing data using KNN method
import pandas as pd
from sklearn.impute import KNNImputer

def impute_missing_data_knn(df, n_neighbors=5):
    """
    Impute missing data in a DataFrame using K-Nearest Neighbors.

    Parameters:
    df (pd.DataFrame): The DataFrame containing missing data.
    n_neighbors (int): Number of neighboring samples to use for imputation.

    Returns:
    pd.DataFrame: DataFrame with missing data imputed.
    """
    imputer = KNNImputer(n_neighbors=n_neighbors)
    df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    # Create a new column 'miss_val' to indicate if any value is missing in the row
    df['miss_val'] = df.isnull().any(axis=1).apply(lambda x: not x)
    missing_values = df.isnull().sum()
    if missing_values.any():
        raise ValueError("There are missing values in the dataframe. Please handle them before proceeding.")
    df = df.drop(columns=['miss_val'])
    return df


drop_missings = True
how_many_percent = 10

def get_columns_to_drop(df):
    if drop_missings == True:
        shape_1 = df.shape
        print("Before dropping ", shape_1)  
        missing_values = df.isnull().sum()
        # Drop columns with missing data percentage higher than 10% 
        missing_values = df.isnull().sum()
        missing_in_column_percent = (missing_values / shape_1[0]) * 100
        missing_in_column_percent = missing_in_column_percent.sort_values(ascending=False)
        # Drop columns with missing data percentage higher than 10%
        columns_to_drop = missing_in_column_percent[missing_in_column_percent > how_many_percent].index
        # see definition file
        
        print('Columns with missing values dropped.')
        df = df.drop(columns=columns_to_drop)

        shape_2 = df.shape
        diff_shape = shape_1[1] - shape_2[1]
        print("After dropping ", shape_2)
        print("number of coolumsn dropped: ", diff_shape)
    else:
        print('Columns with missing values are not dropped. ')
        # shape_1 = df.shape
        # shape_2 = df.shape
        # print("Before dropping ", shape_1) 
        # print("After dropping ", shape_2)
    return (df)    

def describe_target(df, target):
    # - Total number of records
    n_records = len(df)
    # - Number of records passed
    passed = len(df[df[target] == True])
    # - Number of records not passed
    not_passed = len(df[df[target] == False])
    # - Percentage of individuals who passed
    greater_percent = 100 * passed / n_records

    # Print the results
    print("Total number of records: {}".format(n_records))
    print("Y numbers: {} ".format(passed))
    print("(1-Y): {}".format(not_passed))
    print("Percentage of Y to all records : {:.2f}%".format(greater_percent))
    return df