# import json

# with open('user.json', 'r', encoding='utf-8') as f:
#     json_file = json.load(f)
#
# print(f'{type(json_file) = }\n{json_file = }')
# print(f'{json_file["name"] = }')
# print(f'{json_file["address"]["geo"] = }')
# print(f'{json_file["email"] = }')

# json_text = """
# [
# {
# "userId": 1,
# 6
# "id": 9,
# "title": "nesciunt iure omnis dolorem tempora et
# accusantium",
# "body": "consectetur animi nesciunt iure dolore"
# },
# {
# "userId": 1,
# "id": 10,
# "title": "optio molestias id quia eum",
# "body": "quo et expedita modi cum officia vel magni"
# },
# {
# "userId": 2,
# "id": 11,
# "title": "et ea vero quia laudantium autem",
# "body": "delectus reiciendis molestiae occaecati non minima
# eveniet qui voluptatibus"
# },
# {
# "userId": 2,
# "id": 12,
# "title": "in quibusdam tempore odit est dolorem",
# "body": "praesentium quia et ea odit et ea voluptas et"
# }
# ]"""
#
# print(f'{type(json_text) = }\n{json_text = }')
# json_list = json.loads(json_text)
# print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list =}')

# my_dict = {
# "first_name": "Джон",
# "last_name": "Смит",
# "hobbies": ["кузнечное дело", "программирование",
# "путешествия"],
# "age": 35,
# "children": [
# {
# "first_name": "Алиса",
# "age": 5
# },
# {
# "first_name": "Маруся",
# "age": 3
# }
# ]
# }
# print(f'{type(my_dict) = }\n{my_dict = }')
# with open('new_user.json', 'w') as f:
#     json.dump(my_dict, f)

# with open('new_user.json', 'r', encoding='utf-8') as f:
#     new_dict = json.load(f)
# print(f'{new_dict =}')

# with open('new_user.json', 'w', encoding='utf-8') as f:
#     json.dump(my_dict, f, ensure_ascii=False)

# dict_to_json_text = json.dumps(my_dict)
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

# my_dict = {
# "id": 123,
# "name": "Clementine Bauche",
# "username": "Cleba",
# "email": "cleba@corp.mail.ru",
# "address": {
# "street": "Central",
# "city": "Metropolis",
# "zipcode": "123456"
# },
# "phone": "+7-999-123-45-67"
# }
# res = json.dumps(my_dict, indent=2, separators=(',', ':'),
# sort_keys=True)
# print(res)

# a = 'Hello world!'
# b = {key: value for key, value in enumerate(a)}
# c = json.dumps(b, indent=3, separators=('; ', '= '))
# print(c)

# import csv
#
# with open('biostats.csv', 'r', newline="") as f:
#     csv_file = csv.reader(f)
#     for line in csv_file:
#         print(line)
# print(type(line))

import csv

# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(line)
# print(type(line))

# with (
#     open('biostats_tab.csv', 'r', newline='') as f_read,
#     open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     all_data = []
#     for i, line in enumerate(csv_read):
#         if i == 0:
#             csv_write.writerow(line)
#         else:
#             line[2] += 1
#             for j in range(2, 4 + 1):
#                 line[j] = int(line[j])
#             all_data.append(line)
#     csv_write.writerows(all_data)

# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
#     restkey="new", restval="MainOffice", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
# print(f'{line["name"] = }\t{line["age"] = }')

# with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
#     csv_write = csv.DictWriter(f_write, fieldnames=["number",
# "name", "data"], restval='Hello world!', dialect='excel',
# delimiter='#', quotechar='=', quoting=csv.QUOTE_NONNUMERIC)
#     csv_write.writeheader()
#     dict_row = {}
#     for i in range(10):
#         dict_row['number'] = i
#         dict_row['name'] = str(i)
#         csv_write.writerow(dict_row)

# import pickle

# res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
# print(res)

# my_dict = {
# "first_name": "Джон",
# "last_name": "Смит",
# "hobbies": ["кузнечное дело", "программирование",
# "путешествия"],
# "age": 35,
# "children": [
# {
# "first_name": "Алиса",
# "age": 5
# },
# {
# "first_name": "Маруся",
# "age": 3
# }
# ]
# }
# print(my_dict)
# res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
# print(f'{res = }')


# def func(a, b, c):
#     return a + b + c
#
#
# my_dict = {
# "numbers": [42, 4.1415, 7+3j],
# "functions": (func, sum, max),
# "others": {True, False, 'Hello world!'},
# }
# with open('my_dict.pickle', 'wb') as f:
#     pickle.dump(my_dict, f)

# def func(a, b, c):
#     return a * b * c
#
#
# with open('my_dict.pickle', 'rb') as f:
#     new_dict = pickle.load(f)
# print(f'{new_dict = }')
# print(f'{new_dict["functions"][0](2, 3, 4) = }')

# import pickle
#
# my_dict = {'numbers': [42, 4.1415, (7 + 3j)],
# 'functions': (sum, max),
# 'others': {False, True, 'Hello world!'}
# }
# res = pickle.dumps(my_dict)
# with open('quest.pickle', 'wb') as f:
#     pickle.dump(f'{res = }', f)






