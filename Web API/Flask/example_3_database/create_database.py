import sqlite3

# conectando ao banco de dados
conn = sqlite3.connect('enterprise.db')

# definindo um cursor
cursor = conn.cursor()

# criando a tabela
cursor.execute("""
	CREATE TABLE empregados (
	    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	    nome TEXT NOT NULL,
	    cargo TEXT,
	    salario REAL
	);
""")

print('Tabela criada com sucesso.')

# desconectando do banco
conn.close()