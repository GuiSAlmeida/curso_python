import sqlite3

conct = sqlite3.connect('modulo06/database.db')
cursor = conct.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clients ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'name TEXT,'
#                'weight REAL'
#                ')')

# cursor.execute(
#     'INSERT INTO clients (name, weight) VALUES (?, ?)',
#     ('Deia', 54)
# )

# cursor.execute(
#     'INSERT INTO clients (name, weight) VALUES (:name, :weight)',
#     {'name': 'Deia', 'weight': 54}
# )

# cursor.execute(
#     'INSERT INTO clients VALUES (:id, :name, :weight)',
#     {'id': None, 'name': 'Bulma', 'weight': 5})

# conct.commit()

# cursor.execute('UPDATE clients SET name = :name WHERE id = :id',
#                {'name': 'Chokito', 'id': 3})
# conct.commit()

# cursor.execute('DELETE FROM clients WHERE id = :id',
#                {'id': 2})
# conct.commit()

# cursor.execute('SELECT * FROM clients')

cursor.execute('SELECT name, weight FROM clients WHERE weight > :weight',
               {'weight': 50})

for linha in cursor.fetchall():
    # ident, name, weight = linha
    # print(ident, name, weight)
    print(linha)


cursor.close()
conct.close()
