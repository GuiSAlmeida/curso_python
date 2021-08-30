import sqlite3


class ScheduleDB:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def insert(self, name, phone):
        query = 'INSERT OR IGNORE INTO schedule (name, phone) VALUES (?, ?)'
        self.cursor.execute(query, (name, phone))
        self.conn.commit()

    def edit(self, name, phone, id):
        query = 'UPDATE OR IGNORE schedule SET name=?, phone=? WHERE id=?'
        self.cursor.execute(query, (name, phone, id))
        self.conn.commit()

    def delete(self, id):
        query = 'DELETE FROM schedule WHERE id = ?'
        self.cursor.execute(query, (id,))
        self.conn.commit()

    def list(self):
        query = 'SELECT * FROM schedule'
        self.cursor.execute(query)

        for line in self.cursor.fetchall():
            print(line)

    def search(self, term):
        query = 'SELECT * FROM schedule WHERE name LIKE ?'
        self.cursor.execute(query, (f'%{term}%',))

        for line in self.cursor.fetchall():
            print(line)

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    schedule = ScheduleDB('modulo06/schedule.db')
    # schedule.insert('Gui', '123456')
    # schedule.insert('Deia', '654321')
    # schedule.insert('Bulma', '123654')
    # schedule.edit('Deinha', '222222', 5)
    # schedule.delete(6)

    # schedule.list()

    # schedule.insert('Gui Almeida', '321654')
    # schedule.insert('Felipe Almeida', '321655')
    schedule.search('Almeida')
