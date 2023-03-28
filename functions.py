import json
import operator
from sklearn import svm


def frequency():
    with open(
            'C:/Users/ozarg/Downloads/Telegram Desktop/Recognition/Recognition/Recognition/bin/Debug/stats/letterFrequency30.json',
            encoding='utf-8-sig') as f:
        frequency = json.load(f)
    frequency.sort(key=operator.itemgetter('key'))
    return frequency

def patterns():
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
    return patterns_users, expected_values


def sessions(path):
    with open(path, encoding='utf-8') as f:
        sessions = json.load(f)
    # пользователи и значения
    session_users = []
    session_letters = []
    for i in sessions:
        session_users.append(i['Login'])
        session_letters.append(i['Letters'])
    return session_users, session_letters


def Eucliadian_dist(expected_values, session_letters, n_session):
    result = []
    for i in expected_values:
        dist_eucliadian = 0
        for j in range(len(i)):
            if i[j]['Key'] == session_letters[n_session][j]['Key']:
                dist_eucliadian += pow(float(i[j]['Value']) - session_letters[n_session][j]['Value'], 2)
                k = pow(dist_eucliadian, 0.5)
        result.append(k)
    return result


def Eucliadian_freq_dist(expected_values, session_letters, n_session, frequency):
    result = []
    for i in expected_values:
        dist_eucliadian = 0
        for j in range(len(i)):
            if i[j]['Key'] == session_letters[n_session][j]['Key'] == frequency[j]['key']:
                dist_eucliadian += pow(float(i[j]['Value']) - session_letters[n_session][j]['Value'], 2) * float(frequency[j]['value'])
                k = pow(dist_eucliadian, 0.5)
        result.append(k)
    return result


def Manhattan_dist(expected_values, session_letters, n_session):
    result = []
    for i in expected_values:
        dist_manhattan = 0
        for j in range(len(i)):
            if i[j]['Key'] == session_letters[n_session][j]['Key']:
                dist_manhattan += abs(float(i[j]['Value']) - session_letters[n_session][j]['Value'])
                k = dist_manhattan
        result.append(k)
    return result


def Manhattan_freq_dist(expected_values, session_letters, n_session, frequency):
    result = []
    for i in expected_values:
        dist_manhattan_freq = 0
        for j in range(len(i)):
            if i[j]['Key'] == session_letters[n_session][j]['Key'] == frequency[j]['key']:
                dist_manhattan_freq += abs(float(i[j]['Value']) - session_letters[n_session][j]['Value']) * float(frequency[j]['value'])
                k = dist_manhattan_freq
        result.append(k)
    return result

def SVM(expected_values, patterns_users,session_letters, n_session):
    x = expected_values
    y_train = patterns_users
    session_letters = session_letters[n_session]
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
    # print(len(x[2]))
    # print(len(x_train[2]))
    # print((x_train[0]))
    # print(len(y_train))
    # print(x_train)
    # print(y_pr)
    clf = svm.SVC()
    clf.fit(x_train, y_train)
    result = clf.predict([y_pr])
    return result