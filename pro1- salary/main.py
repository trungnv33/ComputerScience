import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split,KFold
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
from sklearn import preprocessing
df = pd.read_csv('dataset\data.csv')
def handle_non_numerical_data(df):
    columns = df.columns.values
    for column in columns:
        x = 0
        digit_dict = {}
        def convert_to_int(val):
            return digit_dict[val]
        if df[column].dtype != np.float64 and df[column].dtype != np.int64:
            df_val = list(set(df[column]))
            for val in df_val:
                if val not in digit_dict:
                    digit_dict[val] = x
                    x += 1 
            df[column] = list(map(convert_to_int,df[column])) 
    return df
df=  handle_non_numerical_data(df)
#--------Visualization---------------------#
# sns.pairplot(df)
# plt.show()
#-------------------------------------------#
X = np.array(df.drop(['X5','X6','X7','Y'],1))
X2_X3 = np.array(X[:,1]*X[:,2]).reshape(-1,1)
X4_X5 = np.array(X[:,3]*X[:,4]).reshape(-1,1)
# print('X2_X3= ', X2_X3)
X = np.concatenate((X,X2_X3),axis = 1)
X = preprocessing.scale(X)
y = np.array(df['Y'])
# print('X = ',X)
# X_train,X_test,y_train,y_test = X[:20,:],X[20:,:],y[:20],y[20:]
X_train,X_test,y_train,y_test  = train_test_split(X,y,test_size = 0.2)
model = LinearRegression().fit(X_train,y_train)
# co_eff = model.coef_
# print('co_eff = ' ,co_eff)
# predictions = model.predict(X_test)
# accuracy = model.score(X_test,y_test)
# print('predict = ', predictions.astype(int))
# print('y_test = ',y_test)
# print('accuracy = ', accuracy)
# print('error',mean_squared_error(predictions,y))
#_----------------------------#
kf = KFold(n_splits= 4)
kf.get_n_splits(X)
print(kf)
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    predictions = model.predict(X_test)
    co_eff = model.coef_
    print('-------------------------------------------------')
    print('co_eff = ' ,co_eff)
    print('predict = ', predictions.astype(int))
    print('y_test = ',y_test)
    accuracy = model.score(X_test,y_test)
    print("accuracy ",accuracy)

    