import numpy as np
from sklearn import svm
import json
import matplotlib.pyplot as plt

with open(
        'C:/Users/ozarg/Downloads/Telegram Desktop/Modeling/Modeling/Modeling/bin/Debug/stats/u94.json',
        encoding='utf-8-sig') as f:
    patterns = json.load(f)
# шаблоны пользователей и ожидаемые значения
patterns_users = []
expected_values = []
for i in patterns:
    patterns_users.append(i['Login'])
    expected_values.append(i['Letters'])

with open('C:/Users/ozarg/Downloads/Telegram Desktop/Modeling/Modeling/Modeling/bin/Debug/stats/u92.json', encoding='utf-8') as f:
    sessions = json.load(f)
# пользователи и значения
session_users = []
session_letters = []
for i in sessions:
    session_users.append(i['Login'])
    session_letters.append(i['Letters'])




x = expected_values
y_train = [1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
session_letters = session_letters[1]
# print(session_letters)
# print(patterns_users)
x_train = []
train = []
for i in x:
    for j in i:
        k = j.get('Value')
        train.append(k)
    x_train.append(train)
    train = []
y_pr = []
for i in x:
    for j in i:
        k = j.get('Value')
        train.append(k)
    y_pr.append(train)
    train = []

x_train += y_pr
x_train_data = []
p = 0
for i in x_train:
    p += 1
    a = sum(i)
    k = [p, a]
    x_train_data.append(k)

clf = svm.SVC(kernel='linear')
clf.fit(x_train_data, y_train)
v = clf.support_vectors_
w = clf.coef_[0]


x_train_data = np.array(x_train_data)
y_train = np.array(y_train)

x_0 = x_train_data[y_train == 1]
x_1 = x_train_data[y_train == -1]
print(w)
print(v)
line_x = list(range((int(10))))
line_y = [-x*w[0]/w[1] for x in line_x]
# print(line_y)

plt.scatter(x_0[:, 0], x_0[:, 1], color='red')
plt.scatter(x_1[:, 0], x_1[:, 1], color='blue')
plt.scatter(v[:, 0], v[:, 1], s=70, edgecolors=None, linewidths=0, marker='s')
# plt.plot(line_x, line_y, color='green')

plt.grid(True)
plt.show()
# print(x_train_data[:, 1])
