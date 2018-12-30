import psycopg2
from psycopg2.extensions import AsIs

class DatabaseConnection:
    def __init__(self):
        self.connecion = psycopg2.connect(
            database='ktsdb2', user='user144', host='localhost', password='user')
        self.connecion.autocommit = True
        self.cursor = self.connecion.cursor()


    def create_table(self):
        try:
            query = "CREATE TABLE users(id serial PRIMARY KEY, name VARCHAR(32) UNIQUE , state integer, value text[] )"
            self.cursor.execute(query)
        except:
            pass

    def create_table_subject(self, subject):
        try:
            query = "CREATE TABLE {}(id serial PRIMARY KEY, question VARCHAR(300), variants VARCHAR(300), answer VARCHAR(50) )".format(subject)
            self.cursor.execute(query)
            print(subject, " table is created")
            return True
        except:
            return False

    def get_tests(self, subject):
        query = "SELECT * FROM {}".format(subject)
        self.cursor.execute(query)
        table = self.cursor.fetchall()
        return table

    def save_question(self, subj, que, var, ans):
        print(subj, que, var, ans)
        #query = "INSERT INTO {} (question, variants, answer) VALUES ({}, {}, {})".format(subj, que, var, ans)
        self.cursor.execute("INSERT INTO %s (question, variants, answer) VALUES (%s, %s, %s)", (AsIs(subj), que, var, ans))

    # def add_device(self, device_name):

    #     query = "SELECT state FROM users WHERE name = %s"
    #     self.cursor.execute(query, (device_name,))
    #     state = self.cursor.fetchall()

    #     # if device already exist in table
    #     if state:
    #         query = "UPDATE users SET state = 1 WHERE name = %s"
    #         self.cursor.execute(query, (device_name,))
    #         return

    #     query = "INSERT INTO users (name, state) VALUES (%s, 1)"
    #     self.cursor.execute(query, (device_name,))

    # def estabilish_connections(self):
    #     query = "UPDATE users SET state=0 WHERE state=1"
    #     self.cursor.execute(query)

    # def take_table(self):
    #     self.cursor.execute("SELECT * FROM users")
    #     table = self.cursor.fetchall()
    #     return table

    # def save(self, data, device_name):
    #     query = "UPDATE users SET value = value || %s WHERE name = %s"
    #     self.cursor.execute(query, (data, device_name))

    # def quit(self, device_name):
    #     query = "UPDATE users SET state = 0 WHERE name = %s"
    #     self.cursor.execute(query, (device_name,))

    # def take_data(self, device_name):
    #     query = "SELECT value FROM users WHERE name = %s"
    #     self.cursor.execute(query, (device_name,))
    #     val = self.cursor.fetchall()
    #     return val

    def drop_table(self, name):
        try:
            self.cursor.execute("DROP TABLE {}".format(name))
        except:
            pass



if __name__ == '__main__':
    database_connection = DatabaseConnection()
    database_connection.create_table()
