import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# with open("i11price.csv") as f:
#     dic = csv.DictReader(f)
#     li = []
#     sex = []
#     own = []
#     price = []
#     for row in dic:
#         if row["sex"]:
#             li.append(row)
#             sex.append(int(row["sex"]))
#             own.append(int(row["own"]))
#             price.append(int(row["price"]))

# https://fstd.com.tw/victory/2019/04/03/%E5%A4%A7%E5%AE%B6%E4%B8%80%E8%B5%B7%E4%BE%86%E5%AD%B8python%EF%BC%884%EF%BC%89%EF%BC%9A%E6%95%B8%E5%80%BC%E5%88%86%E6%9E%90/
# x = men()

# l1 = []
# for i in range(0, len(sex)):
#     l2 = []
#     l2.append(sex[i])
#     l2.append(own[i])
#     l2 = np.asarray(l2)
#     l1.append(l2)
#
# print(l1)

from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(l1, [np.newaxis], price)
# print('intercept:', model.intercept_)
# print('coefficient:', model.coef_)

data = pd.read_csv("i11price.csv")
X_1 = data.iloc[3:, 1].values.reshape(-1, 1)
X_2 = data.iloc[3:, 2].values.reshape(-1, 1)
X_3 = data.iloc[3:, 3].values.reshape(-1, 1)
X_4 = data.iloc[3:, 4].values.reshape(-1, 1)
X_5 = data.iloc[3:, 5].values.reshape(-1, 1)
Y = data.iloc[3:, 6].values.reshape(-1, 1)
lr = LinearRegression()
X = X_3
print(type(X))
lr.fit(X, Y)
Y_pred = lr.predict(X)

plt.scatter(X, Y)
plt.plot(X, Y_pred, color="red")
plt.show()