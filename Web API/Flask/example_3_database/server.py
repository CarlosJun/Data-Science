# conda install flask
from flask import Flask, request, Response, g
import sqlite3

DB_URL = "enterprise.db"

# Criar o aplicativo
app = Flask(__name__)

users = [
			{"username":"Carlos", "secret":"@dmin456"}
		]

@app.before_request
def before_request():
	print("Conectando ao banco")
	conn = sqlite3.connect(DB_URL)
	g.conn = conn

@app.after_request
def after_request(response):
	if g.conn is not None:
		g.conn.close()
		print("Desconectando do banco")
	return response

def query_employers_to_dict(conn, query):
    # definindo um cursor
    cursor = conn.cursor()
    # lendo os dados
    cursor.execute(query)
    # construindo dicionário da consulta
    employers_dict = [{'nome':row[0], 'cargo':row[1], 'salario':row[2]} 
                       for row in cursor.fetchall()]
    return employers_dict

def check_user(username, secret):
	for user in users:
		if (user["username"] == username) and (user["secret"] == secret):
			return True
	return False

@app.route("/")
def home():
	return "<h1>Home Page</h1>"

@app.route("/empregados")
def get_empregados():

	# consturindo a consulta SQL
	query = """
				SELECT nome, cargo, salario 
				FROM empregados;
			"""
	# cria a lista em formato json
	employers = query_employers_to_dict(g.conn, query)

	return {'empregados':employers}

@app.route("/empregados/<cargo>")
def get_empregados_cargo(cargo):


	# consturindo a consulta
	query = """
				SELECT nome, cargo, salario 
				FROM empregados
				WHERE "cargo" LIKE "{}";
			""".format(cargo)

	# cria a lista em formato json
	employers = query_employers_to_dict(g.conn, query)

	return {'empregados': employers}

@app.route("/empregados/<info>/<value>")
def get_empregados_info(info, value):
	
	if value.isnumeric():
		value = float(value)
    
	# construir a consulta
	query = """SELECT nome, cargo, salario 
				FROM empregados
				WHERE "{}" LIKE "{}";
			""".format(info, value)

	# cria a lista em formato json
	employers = query_employers_to_dict(g.conn, query)
					
	return {'empregados': employers}

@app.route("/informations", methods=['POST'])
def get_empregados_post():
		
	username = request.form['username']
	secret = request.form['secret']

	if not check_user(username, secret):
		# 401 HTTP Unauthorized
		return Response("Unauthorized", status=401)

	info = request.form['info']
	value = request.form['value']
	
	if value.isnumeric():
		value = float(value)
    
	# construir a consulta
	query = """SELECT nome, cargo, salario
			   FROM empregados
			   WHERE "{}" LIKE "{}";
			""".format(info, value)

	# cria a lista em formato json
	employers = query_employers_to_dict(g.conn, query)
					
	return {'empregados': employers}

if __name__ == "__main__":
	app.run(debug=True)
