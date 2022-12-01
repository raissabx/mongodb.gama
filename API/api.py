from flask import Flask, redirect, request, url_for, jsonify
from pymongo import MongoClient

app = Flask(__name__)
conn = MongoClient('mongodb+srv://cluster0.x45vtu2.mongodb.net/test', username='rai_xavier', password='201295')
db = conn['magalu']

#Create
## FROM
@app.route('/')
def home():
    return redirect(url_for('static', filename='cadastro.html'))

@app.route('/cadastro', methods=['GET'])
def cadastro():
    produto = request.args.to_dict()
    db.produtos.insert_one(produto)
    del produto['_id']
    return produto

if __name__ == '__main__':
    app.run(debug=True)