import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


import json


import sqlite3

app = Flask(__name__)
CORS(app)



@app.route('/')
def home():
  return render_template('index.html')



@app.route('/pessoas', methods=['GET'])
def pessoas():

  
  conn = sqlite3.connect('bd.py')

  
  conn.row_factory = sqlite3.Row


  cursor = conn.cursor()

 
  cursor.execute('''SELECT id,nome,sobrenome,telefone,email,idioma from pessoa''')

  
  result = cursor.fetchall()

  
  conn.close()


  return json.dumps([dict(ix) for ix in result])



@app.route('/pessoa/<telefone>', methods=['GET', 'DELETE'])
def pessoaPorTelefone(telefone):

 
  conn = sqlite3.connect('bd.py')

 
  conn.row_factory = sqlite3.Row

  
  cursor = conn.cursor()

  if request.method == 'GET':

    
    cursor.execute(
      '''SELECT id,nome,sobrenome,telefone,email,idioma from pessoa where telefone=?''',
      [telefone])

    
    result = cursor.fetchall()

    
    conn.close()

    
    return json.dumps([dict(ix) for ix in result])

  elif request.method == 'DELETE':

    cursor.execute('''SELECT id,nome,sobrenome,telefone,email,idioma from pessoa''')

    
    result = cursor.fetchall()

    for valor in [dict(ix) for ix in result]:
      if valor['CPF'] == cpf:
        cursor.execute('''delete from pessoa where telefone=?''', [telefone])
        conn.commit()
        content = {'delete': 'ok'}
        return jsonify(content)

    content = {'delete': 'not_found'}
    return jsonify(content)



@app.route('/pessoa', methods=['POST'])
def insereAtualizaPessoa():
  data = request.get_json()

  id = data['id']
  nome = data['nome']
  sobrenome = data['sobrenome']
  telefone = data['Telefone']
  email = data['email']
  idioma = data['idioma']

  
  conn = sqlite3.connect('bd.py')

  
  conn.row_factory = sqlite3.Row


  cursor = conn.cursor()

 
  cursor.execute('''SELECT id,nome,sobrenome,telefone,email,idioma from pessoa''')

  result = cursor.fetchall()

  for valor in [dict(ix) for ix in result]:
    if valor['Telefone'] == telefone:
      cursor.execute(
        '''UPDATE pessoa set id=?,nome=?,sobrenome=?,telefone=?,email=?,idioma=? where telefone=?''',
        [id,nome, sobrenome, telefone, email, idioma])
      conn.commit()
      content = {'update': 'ok'}
      return jsonify(content)

  
  cursor.execute(
    '''INSERT INTO pessoa (id,nome,sobrenome,telefone,email,idioma) values(?,?,?,?,?,?)''',
    [id, nome, sobrenome, telefone, email, idioma])

  
  conn.commit()


  conn.close()

  content = {'insert': 'ok'}
  return jsonify(content)


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run()
  
