
# Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy.stats import chi2_contingency
from statsmodels.stats.outliers_influence import variance_inflation_factor
#from sklearn.model_selection import train_test_split
#from sklearn.ensemble import RandomForestCLassifier
#from sklearn.metrics import accuracy_score, classification_report , precision_recall_fscore
import warnings
import os

# Load the Dataset
a1 = pd.read_excel("E:\Data Science\PythonForDS\Credit Risk Modelling\Credit Modeling\case_study1.xlsx")
a2 = pd.read_excel("E:\Data Science\PythonForDS\Credit Risk Modelling\Credit Modeling\case_study2.xlsx")

df1 = a1.copy()
df2 = a2.copy()

# Remove nulls




