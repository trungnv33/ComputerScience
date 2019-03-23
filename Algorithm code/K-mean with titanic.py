import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans
df = pd.read_excel('titanic.xls')
df.drop(['body','name'],1,inplace = True)
df.convert_objects(convert_numeric= True)
df.fillna(0, inplace = True)
# print(df.columns.values)
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
            # print(list(map(convert_to_int,df[column])))
            df[column] = list(map(convert_to_int,df[column])) 
    return df
df = handle_non_numerical_data(df)
X = np.array(df.drop(['survived'],1).astype(float))
y = np.array(df['survived'])
print(X)
print(y)
clf = KMeans(n_clusters=2)
clf.fit(X)