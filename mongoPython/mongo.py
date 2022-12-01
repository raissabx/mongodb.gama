from pymongo import MongoClient
from pprint import pprint
from pandas import pandas as pd

#conexão
cliente = MongoClient('mongodb+srv://rai_xavier:201295@cluster0.x45vtu2.mongodb.net/test')
db = cliente['test']

#consulta
cursor = db.alunos.find({})
resultado = list(cursor)
pprint(resultado)

#Pandas
df = pd.DataFrame(resultado).set_index('_id')
print(df)

#Arquivo
df.to_json('mongo.json', orient='records')

#Update

db.alunos.update_many(
    {'idade': {'$gt':40}},
    {'$set':
        {'idade': 30}
    }
)

cursor = db.alunos.find({'idade': 30})
resultado = list(cursor)
pprint(resultado)