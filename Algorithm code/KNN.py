import math
import operator

import numpy as np
import pandas as pd


# Tính toán khoảng cách giữa 2 vector
def E_distance(vector1,vector2):
    return math.sqrt((np.sum(vector1-vector2))**2)
# Tìm ra các neighbors gần nhất
def get_neighbors(z,X,k):
    distance = []   
    m = X.shape[0]
    for i in range (0,m):
        diff = E_distance(z,X[i,:])
        distance.append((X[i,:],diff,i))
    distance.sort(key = operator.itemgetter(1))
    neighbors = []
    for i in range (0,k):
        neighbors.append((distance[i][2]))
    print('nearest neighbors= ',neighbors)
    return neighbors
# dự đoán đầu ra dựa trên vote của y_train
def predict(neighbors,y_train):
    vote = {}
    for i in neighbors:
        if y_train[i] in vote:
            vote[y_train[i]] += 1
        else:
            vote[y_train[i]] = 1 
    max_vote = max(vote.items(), key=operator.itemgetter(1))[0]
    return max_vote
# tính toán phần trăm chính xác của tập dự đoán so với thực tế
def accuracy(list1,list2):
    s=  0
    for i,j in zip(list1,list2):
        if i == j:
            s+= 1
    result = s/len(list2) *100
    return result 
# Test thử với tập dataset Iris
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
df = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = iris['species']
X_train,X_test,y_train,y_test = df[:140].values,df[140:].values,y[:140],y[140:]
z = X_test # dùng X_test để dự báo 
pred = []
k_nearest = 7 # hệ số k nearest neighbors
for i in range (z.shape[0]):
    neighbors = get_neighbors(z[i,:],X_train,k_nearest)
    pred.append(predict(neighbors,y_train))
print('Prediction = ',pred)
print('y_test = ', y_test)
print("Accuracy = " + str(accuracy(pred,list(y_test)))+ '%')
