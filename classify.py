#to train and test classifiers
# to print classification report
# and make colorbar matrix of confusion matrix

#

import pandas as pd
import Xtest,ytest
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.

def make_report():
    dfx=pd.read_csv('Xtest.csv') # read Xtest and save in DataFrame
    dfy=pd.read_csv('ytest.csv') # read ytest and save in DataFrame
    df=pd.concat([dfx,dfy],axis=1) # concat both DataFrames
    
