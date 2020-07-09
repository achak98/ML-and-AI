
import numpy as np
import pandas as pd
import seaborn as sns
import plotly
import chart_studio.plotly as py
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv("housingdata.csv",header = None)
print(df.head())

''' CRIM per capita crime rate by town

    ZN proportion of residential land zoned for lots over 25,000 sq.ft.

    INDUS proportion of non-retail business acres per town

    CHAS Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)

    NOX nitric oxides concentration (parts per 10 million)

    RM average number of rooms per dwelling

    AGE proportion of owner-occupied units built prior to 1940

    DIS weighted distances to five Boston employment centres

    RAD index of accessibility to radial highways

    TAX full-value property-tax rate per $10,000

    PTRATIO pupil-teacher ratio by town

    B [1000*(Bk - 0.63) ^ 2] where Bk is the proportion of blacks by town

    LSTAT percentage lower status of the population

    MEDV Median value of owner-occupied homes in $1000s'''



'''housing_colnames = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.columns = housing_colnames
print(df.info())

#print(df.head())

#print(df.shape)'''

'''def plotFeatures(col_list,title):
    plt.figure(figsize=(10, 14))
    i = 0
    print(len(col_list))
    for col in col_list:
        i+=1
        plt.subplot(7,2,i)
        plt.plot(df[col],df["MEDV"],marker='.',linestyle='none')
        plt.title(title % (col))   
        plt.tight_layout()'''