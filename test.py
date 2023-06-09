import json

import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt


with open(
        'km.json',
        encoding='utf-8-sig') as f:
    patterns = json.load(f)
# шаблоны пользователей и ожидаемые значения
patterns_users = []
expected_values = []
for i in patterns:
    patterns_users.append(i['login'])
    expected_values.append(i['expectedValues'])

with open('C:/Users/ozarg/Downloads/Telegram Desktop/Modeling/Modeling/Modeling/bin/Debug/stats/u94.json', encoding='utf-8') as f:
    sessions = json.load(f)
# пользователи и значения
session_users = []
session_letters = []
for i in sessions:
    session_users.append(i['Login'])
    session_letters.append(i['Letters'])


x = expected_values
y_train = patterns_users
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
for i in session_letters:
    p = i.get('Value')
    y_pr.append(p)

x_train = [list(map(float, i)) for i in x_train]

x_train_data = []
for i in x_train:
    a = sum(i)
    x_train_data.append(a)
print(x_train_data[0])
print(len(x_train[0]))

clf = svm.SVC(probability=True)
clf.fit(x_train, y_train)
# y_pr = clf.predict([y_pr])
# y_pr_str = y_pr[0]
v = clf.support_vectors_
print(y_pr)

x_train = np.array(x_train)
y_train = np.array(y_train)
print(x_train_data[0])
print(y_train)
x_0 = x_train[y_train == 'User19']
print(x_0)
x_1 = x_train[y_train != 'User19']


plt.scatter(x_0[:, 0], x_0[:, 1], color='red')
plt.scatter(x_1[:, 0], x_1[:, 1], color='blue')
plt.scatter(v[:, 0], v[:, 1], s=70, edgecolors=None, linewidths=0, marker='s')
# plt.plot(line_x, line_y, color='green')

plt.grid(True)
plt.show()
