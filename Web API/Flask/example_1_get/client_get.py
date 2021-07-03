import requests

response = requests.get('http://0.0.0.0:5000/empregados/cargo/analista')

# parte 1
print(response.text)

# parte 2
#print(response.text['empregados'])

# # parte 3
# print(response.json()['empregados'])

# # parte 4
# message = response.json()
# print(message['empregados'])

# if response.status_code == 200:
# 	message = response.json()
# 	print(message['empregados'])
# else:
# 	print(response.status_code)
