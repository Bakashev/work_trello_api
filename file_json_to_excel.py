import json
import pandas
import settings

# -------рабочая версия с выгрузкой в Excel, используюя для источника двнных стандартный выгруженный в формате json
# -------файл из меню печати доски Trello. В блок with необходимо задать имя создоваемого файла и сохранить сам файл в
#-------папку где лежит проект
with open('22anUFBN (1).json', encoding='utf8') as file:
#with open('test.json', encoding='utf8') as file:

    json_data = json.load(file)
    #print(json_data)
    #создание списка карточек из Трелло
    json_cards = json_data['cards']

    #Создание списка словоре с перечнем колонок
    json_lists = json_data['lists']

    #Создание списка словорей с пользователями
    json_users = json_data['members']
print(len(json_cards))
# print(json_lists)
print(json_users[0])
#Создание словоря с id и статусами
dict_list = {}
for elem in json_lists:
    print(elem['name'])
    dict_list[elem['id']]  = elem['name']

#создание словоря с id и пользователями
dict_users = {}
for elem in json_users:
    dict_users[elem['id']] = elem['fullName']

print(dict_users)
print(dict_list)
for elem in json_cards:
    print(elem['name'])

#Импорт в excel
#print('!!!!!!!!!!!!!' + json_cards[5]['idList'])
dict_test={'name': [], 'status': [], 'desc': [], 'end_date': [], 'users': [], 'Url':[]}
for elem in json_cards:
    # Добавление заголовка карточки
    dict_test['name'].append(elem["name"])

    #Добавление описание карточки
    try:
        print(elem['desc'])
        dict_test['desc'].append(elem['desc'])
    except ValueError:
        dict_test['desc'].append('-')

    # Добавление местонахождения карточки
    try:
        print(elem['idList'])
        if elem['idList'] in dict_list:
            id_value = dict_list[elem['idList']]
            # print('-----')
            # print(dict_list)
            #
            # print(id_value)
            # print('-')
            #print(dict_list[id_value])
            dict_test['status'].append(id_value)

    except KeyError:
         dict_test['status'].append('Архив')

    # Добавление даты выполнения
    try:
        dict_test['end_date'].append(elem["due"])
    except ValueError:
        dict_test['end_date'].append('No date')

    # Добавление пользователей
    if elem['idMembers']:
        dict_test['users'].append(elem['idMembers'])

    else:
        dict_test['users'].append([])

    # Добавляем ссылку на карточку

    if elem['shortUrl']:
        dict_test['Url'].append(elem['shortUrl'])
    else:
        dict_test['Url'] = ''
#Замена Id на имя пользователя в итоговом словоре dict_test['users']
for us_list in dict_test['users']:

    for i in range(len(us_list)):
        us_list[i]=dict_users[us_list[i]]

print(dict_test)
for key, val in dict_test.items():
    print(len(val))

data_to_excel = pandas.DataFrame.from_dict(dict_test)
data_to_excel.to_excel('test.xlsx')
#----------------------------------------------------------------------------------------------------------------------