# uniq = [1,2,3,4,5]
# fifa = [10,5,3,17,4]
# uniq_and_fifa = dict(zip(uniq, fifa))
# print(uniq_and_fifa)
# print(dict(sorted(uniq_and_fifa.items(), key=lambda x: x[1])))

people = {'eac23': 67.10368240683194, 'lrd1': 115.57190983486902, 'ksk12': 117.21063081690606, 'avo19': 123.18892032246849, 'nvb16': 139.9711310547301, 'vve15': 158.97610543749013}
#         row = 0
#         print(dict_sort)
#         print(people)
#         self.tableWidget.setRowCount(len(people))
#         for person in people:
#             self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(dict_sort.keys()))
#             self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person.values()))
#             row += 1
print(list(people.keys())[0])
print(people.values())

# for person in people:
#     print(person)
#     print(people[person])