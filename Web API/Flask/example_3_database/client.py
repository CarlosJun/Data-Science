import requests

# # requisição simples com get
# response = requests.get('http://0.0.0.0:5000/empregados/salario/5000')

# requisição com usuário e senha usando post
data = {"username": "Carlos", "secret":"@dmin456", "info":"salario", "value":5000}
response = requests.post('http://0.0.0.0:5000/informations', data=data)

# # inserção de dados com usuário e senha usando post
# data = {"username": "Carlos", "secret":"@dmin456", "nome":"Gabriel", "cargo":"Engenheiro", "salario":"6000"}
# response = requests.post('http://0.0.0.0:5000/register', data=data)

if response.status_code == 200:
	message = response.json()
	print(message['empregados'])
else:
	print(response.status_code)



