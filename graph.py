import pandas as pd
from api_trello_to_excel import dict_excel
import matplotlib.pyplot as plt
import settings


#df = pd.DataFrame(dict_excel.items(), columns=['name', 'desc', 'date_create', 'date_execution', 'status','users'])
diagram = zip(dict_excel['date_execution'], dict_excel['status'])
diagram_for_graph = {}
for elem in diagram:
    if elem[0] is None:
        diagram_for_graph['01/01/2020'] = elem[1]
    else:
       diagram_for_graph[elem[0]] = elem[1]

df = pd.DataFrame(diagram_for_graph.items(), columns=['status', 'date_execution',])
fig, ax =plt.subplots(figsize=(8, 8))
#bars = plt.bar(df['name'], df['desc'], df['date_create'], df['date_execution'], df['status'], df['users'])
bars = plt.bar( df['date_execution'], df['status'])
plt.show()