import json
import operator
from scipy.spatial import distance

with open(
        'C:/Users/ozarg/Downloads/Telegram Desktop/Recognition/Recognition/Recognition/bin/'
        'Debug/stats/sessions 10.json',
        encoding='utf-8') as f:
    sessions = json.load(f)
    # print(d)

with open(
        'C:/Users/ozarg/Downloads/Telegram Desktop/Recognition/Recognition/Recognition/bin/Debug/stats/patterns.json',
        encoding='utf-8-sig') as f:
    patterns = json.load(f)
    # print(p)
with open(
        'C:/Users/ozarg/Downloads/Telegram Desktop/Recognition/Recognition/Recognition/bin/Debug/stats/letterFrequency30.json',
        encoding='utf-8-sig') as f:
    frequency = json.load(f)

    # print(frequency)


patterns_users = []
expected_values = []
for i in patterns:
    patterns_users.append(i['login'])
    expected_values.append(i['expectedValues'])
session_users = []
session_letters = []
for i in sessions:
    session_users.append(i['Login'])
    session_letters.append(i['Letters'])

frequency.sort(key=operator.itemgetter('key'))
print(frequency)
print(expected_values[0][21]['Key'])
print(expected_values[0][0]['Key'] == frequency[0]['key'])

# key_ex = []
# for i in expected_values:
#     for j in range(len(i)):
#         key_ex.append(i[j]['Key'])
#     break
#
# key_fr = []
# for i in range(len(frequency)):
#     key_fr.append(frequency[i]['key'])
#
# print(key_ex)
# print(key_fr)


# print(type(session_letters[0][0]['Value']))
# print(type(expected_values[0][0]['Value']))
t = []
for i in expected_values:
        dist_euklead = 0
        for j in range(len(i)):
            if i[j]['Key'] == session_letters[0][j]['Key'] == frequency[j]['key']:
                dist_euklead += pow(float(i[j]['Value']) - session_letters[0][j]['Value'], 2) * float(frequency[j]['value'])
                k = (pow(dist_euklead, 0.5))
        t.append(k)
print(t)

# t = []
# test = []
# for i in expected_values:
#         dist_mathetn = 0
#         for j in range(len(i)):
#             if i[j]['Key'] == session_letters[0][j]['Key'] == frequency[j]['key']:
#                 dist_mathetn += abs(float(i[j]['Value']) - session_letters[0][j]['Value']) * float(frequency[j]['value'])
#                 # print(frequency[j]['value'])
#                 test.append(frequency[j]['key'])
#                 # test.append(session_letters[0][j]['Key'])
#                 k = dist_mathetn
#         t.append(k)
# print(t)
# print(len(test))
# print(test)

# expectedValues = []
# values = []
# for i in range(len(list1)):
#     values.append(list1[i].get('Value'))
#
# for i in range(len(list2)):
#     expectedValues.append(float(list2[i].get('Value')))

# print(values)
# print(expectedValues)
# distEucledian = distance.euclidean(values, expectedValues)
# distmath = distance.cityblock(values, expectedValues)
# print(distEucledian)
# print(distmath)
