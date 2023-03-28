import json
from sklearn import svm


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
    clf = svm.SVC(probability=True)
    clf.fit(x_train, y_train)
    y_pr = clf.predict([y_pr])
    y_pr_str = y_pr[0]
    print(len(clf.support_vectors_))

    return y_pr_str


# user = 'User19'
fr = 0      # Ложный отказ в допуске законного пользователя
fa = 0      # Ложный доступ незаконного пользователя
ta = 0      # Верный допуск в систему законного пользователя
tr = 0      # Верный отказ в доступе незаконному пользователю

# for i in range(10):
#     a = SVM(expected_values, patterns_users, session_letters, i)
#     print(a)

    # print(type(a))

def borderReg(real_user, expected_values, n_session, border):
    a = expected_values
    session_users = []
    session_letters = []
    n_pattern = 0
    for i in range(len(patterns_users)):
        if patterns_users[i] == real_user:
            n_pattern = i

    letters_sum = 0


    for i in sessions:
        session_users.append(i['Login'])
        session_letters.append(i['Letters'])
    for i in session_letters[n_session]:
        p = i.get('Value')
        letters_sum += p


    pattern_sum = 0
    for i in expected_values[n_pattern]:
        k = float(i.get('Value'))
        pattern_sum += k
    result = abs(letters_sum - pattern_sum) < 0.01 * border * pattern_sum   # если true то пользователь прошел проверку
    # print(result)
    # print(pattern_sum)
    # print((letters_sum))
    return result
# print(borderReg('User19',expected_values, 0, 10))


for i in range(10):
    a = SVM(expected_values, patterns_users, session_letters, i)
    # print(a)
    regognized_user = a
    real_user = 'User19'
    b = borderReg(real_user, expected_values, i, 100)
    # print(a)
    if regognized_user == real_user and b:
        ta += 1
    elif regognized_user != real_user and b:
        fa += 1
    elif regognized_user == real_user and not b:
        fr += 1
    else:
        tr += 1

print(f'{ta} ta')
print(f'{fa} fa')
print(f'{fr} fr')
print(f'{tr} tr')
print(patterns_users)