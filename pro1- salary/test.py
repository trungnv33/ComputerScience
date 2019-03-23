import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split,KFold
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
from sklearn import preprocessing
X= np.random.rand(10,1)
print('X = ',X)
y = X[-7:]
print('y= ',y)
