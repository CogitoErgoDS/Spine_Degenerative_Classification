"""TODO 
    Make predictions with the linear regression trained model (model_penguins.pkl). 
    The model predicts the body_mass_g given the input features: flipper_length_mm, species and sex
    1. Set the value of flipper_length to a number between 160 and 240
    2. Set the value of species to one of the possible options 'Adelie','Chinstrap','Gentoo'
    3. Set the value of sex to 'Female' or 'Male'
    4. Let's create a dictionary having as keys the input features 
    5. create a dataframe from the input_dict_X 
    6. Make predictions
"""

### Import libraries
import pickle
import streamlit as st
import pandas as pd
