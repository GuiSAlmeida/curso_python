import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def connect_mariadb():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conn
    finally:
        print('Conexão fechada!')
        conn.close()


# CREATE
# with connect_mariadb() as connection:
#     with connection.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso)' \
#             ' VALUES (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Bilu', 30, 98))
#         connection.commit()


# with connect_mariadb() as connection:
#     with connection.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso)' \
#             ' VALUES (%s, %s, %s, %s)'

#         data = [
#             ('DEIA', 'Almeida', 30, 54),
#             ('BULMA', 'Almeida', 1, 5),
#             ('CHOKITO', 'Almeida', 3, 6)
#         ]
#         cursor.executemany(sql, data)  # executa vários INSERTs
#         connection.commit()

# DELETE
# with connect_mariadb() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         connection.commit()

# with connect_mariadb() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         connection.commit()

# with connect_mariadb() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         connection.commit()


# UPDATE
# with connect_mariadb() as connection:
#     with connection.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('Joana', 5))
#         connection.commit()


# READ
with connect_mariadb() as connection:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY nome LIMIT 100')
        result = cursor.fetchall()

        for line in result:
            print(line)
