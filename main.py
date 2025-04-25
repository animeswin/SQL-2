import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produtos (
        ProdutoID INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeProduto TEXT NOT NULL,
        Quantidade INTEGER NOT NULL,
        Preco REAL NOT NULL
    )
''')

produtos = [
    ('Notebook Dell', 15, 3500.00),
    ('Teclado Mecânico', 50, 450.00),
    ('Mouse Sem Fio', 30, 200.00)
]

cursor.executemany('''
    INSERT INTO Produtos (NomeProduto, Quantidade, Preco)
    VALUES (?, ?, ?)
''', produtos)

conn.commit()
print("Tabela Produtos criada e registros inseridos com sucesso!")
conn.close()