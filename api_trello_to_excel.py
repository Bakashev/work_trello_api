import json
import pandas
import settings


#----------------------------------------------------------------------------------------------------------------------
# Работа без файла используя API в Trello

json_list = json.loads(settings.response_lists.text)
json_members = json.loads(settings.response_members.text)
dict_cards = json.loads(settings.response_cards.text)
#print(json_members)
dict_excel = {'name': [], 'desc': [], 'date_create': [],'date_execution': [], 'status': [], 'users': []}
dict_list = {}

#Создание словоря со значениями ключ = id, value = ФИО
dict_users = {}
for element in json_members:
    dict_users[element['id']] = element['fullName']


#Создание словоря с id и наименованием пользователя
for elem in json_members:
    dict_users[elem['id']] = elem['fullName']


# Создание словоря с id и наисменованием колонок из Trello
for elem in json_list:
    dict_list[elem['id']] = elem['name']
#for elem in dict_list:
#print(dict_cards['cards'])
for elem in dict_cards['cards']:
    #print(elem)
    dict_excel['desc'].append(elem['desc'])
    dict_excel['name'].append(elem['name'])
    dict_excel['date_execution'].append(elem['due'])
    dict_excel['status'].append(elem['idList'])
    #заполнение списка ответсвенных, заменяя ID на имена из словоря dict_users
    dict_excel['users'].append(elem['idMembers'])
    # Проходим по спискам ответсвенных пользователей
for i in range(len(dict_excel['users'])):
    if len(dict_excel['users'][i]) != 0:
        # Проходим по списку ответсвенных пользователей за задачу
        for j in range(len(dict_excel['users'][i])):
            #print(dict_excel['users'][i][j])
            dict_excel['users'][i][j] = dict_users[dict_excel['users'][i][j]]

# print(dict_excel['users'])
# print(len(dict_excel['users']))
# print((len(dict_excel['desc'])))
#Установка имя статуса вместо ID
for i in range(len(dict_excel['status'])):
    dict_excel['status'][i] = dict_list[dict_excel['status'][i]]

data_to_excel = pandas.DataFrame.from_dict(dict_excel)
data_to_excel.to_excel('testAPI.xlsx')

# print(dict_excel)
# print(dict_list)
# print(dict_users)


