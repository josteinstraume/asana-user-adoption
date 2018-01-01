import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import statistics as st
import csv as csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load in the datasets
filepath_users = "/Users/Jostein/stories/asana-user-adoption/data/takehome_users-intern.csv"
filepath_engagement = "/Users/Jostein/stories/asana-user-adoption/data/takehome_user_engagement-intern.csv"
users = pd.read_csv(filepath_users, header='infer', delimiter=',', encoding='latin-1')
engagement = pd.read_csv(filepath_engagement, header='infer', delimiter=',')

# Snapshot of the data / verify loaded in correctly
users.head()
users.describe()

# Transform time_stamp into datetime object
# in order to discern which users are adopted
engagement['times'] = pd.to_datetime(engagement['time_stamp'])
engagement.describe()
engagement.head()

for user in engagement['user_id']:
    for time in engagement['times']:
        print(time)