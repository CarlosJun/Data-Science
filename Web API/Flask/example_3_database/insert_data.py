import sqlite3

# acrescentar os dados existentes ao banco
empregados = [
    {"nome":"Valentina", "cargo":"Analista", "salario":5000},
    {"nome":"Enzo", "cargo":"Analista", "salario":4000},
    {"nome":"Maria", "cargo":"Desenvolvedor", "salario":5000}
]

# conectando ao banco de dados
conn = sqlite3.connect('enterprise.db')

# definindo um cursor
cursor = conn.cursor()

# inserindo dados na tabela
for empregado in empregados:
    cursor.execute("""
        INSERT INTO empregados (nome, cargo, salario)
        VALUES (?, ?, ?)
    """, (empregado['nome'], empregado['cargo'], empregado['salario']))


print('Dados inseridos com sucesso.')

# salvando os dados no banco
conn.commit()
# desconectando do banco
conn.close()