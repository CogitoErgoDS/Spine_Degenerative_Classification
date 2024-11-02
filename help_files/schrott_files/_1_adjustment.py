
# Define the path
from pathlib import Path
# Define the path
path = Path('C:/Users/HP1/Desktop/Spiced/capstone-project/data')

def load_frames():
    """
    This function is to load frames from the dataset
    """
    # some code here
    # Load CSV files
    X_train = pd.read_csv(path / "train.csv")
    X_train_coor = pd.read_csv(path / "train_label_coordinates.csv")
    X_train_des = pd.read_csv(path / "train_series_descriptions.csv")
    X_test_des = pd.read_csv(path / "test_series_descriptions.csv")
    submission_df = pd.read_csv(path / "sample_submission.csv")
 


def some_cases():
    """
    This function is to pick some cases from the dataset
    """
    # some code here
 
