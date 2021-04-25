# conda install flask
from flask import Flask, request, Response

# Criar o aplicativo
app = Flask(__name__)

# Dados em formato JSON
empregados = [
			 	{"nome":"Valentina", "cargo":"Analista", "salario":5000},
			 	{"nome":"Enzo", "cargo":"Analista", "salario":4000},
			 	{"nome":"Maria", "cargo":"Desenvolvedor", "salario":5000}
			 ]

users = [
			{"username":"Carlos", "secret":"@dmin456"}
		]

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
	return {'empregados':empregados}

@app.route("/empregados/<cargo>")
def get_empregados_cargo(cargo):
	out_empregados = []
	for empregado in empregados:
		if cargo == empregado['cargo'].lower():
			out_empregados.append(empregado)
	return {'empregados': out_empregados}

@app.route("/empregados/<info>/<value>")
def get_empregados_info(info, value):
	out_empregados = []
	for empregado in empregados:
		if info in empregado.keys():

			value_empregado = empregado[info]

			if type(value_empregado) == str:
				if value == value_empregado.lower():
					out_empregados.append(empregado)
			elif type(value_empregado) == int:
				if int(value) == value_empregado:
					out_empregados.append(empregado)
					
	return {'empregados': out_empregados}

@app.route("/informations", methods=['POST'])
def get_empregados_post():
		
	username = request.form['username']
	secret = request.form['secret']

	if not check_user(username, secret):
		# 401 HTTP Unauthorized
		return Response("Unauthorized", status=401)

	info = request.form['info']
	value = request.form['value']

	out_empregados = []
	for empregado in empregados:
		if info in empregado.keys():

			value_empregado = empregado[info]

			if type(value_empregado) == str:
				if value == value_empregado.lower():
					out_empregados.append(empregado)
			elif type(value_empregado) == int:
				if int(value) == value_empregado:
					out_empregados.append(empregado)
					
	return {'empregados': out_empregados}

if __name__ == "__main__":
	app.run(debug=True)
