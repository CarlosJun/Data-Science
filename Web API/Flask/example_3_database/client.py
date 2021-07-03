import requests

data = {"username": "Carlos", "secret":"@dmin456", "info":"salario", "value":5000}
response = requests.post('http://0.0.0.0:5000/informations', data=data)

# response = requests.get('http://0.0.0.0:5000/empregados/salario/5000')

if response.status_code == 200:
	message = response.json()
	print(message['empregados'])
else:
	print(response.status_code)



