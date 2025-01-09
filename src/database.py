import sqlite3 as sql


class database():

    def insert_data(self, nombre, host, state):
        try:
            conn = sql.connect("hosts.db")
            cursor = conn.cursor()
            data = f"INSERT INTO HOSTS (host_name,host, state) VALUES ('{nombre}', '{host}', {state})"
            cursor.execute(data)
            conn.commit()
            conn.close()
            return 1
        except sql.IntegrityError:
            return 0

    def read_data(self):
        conn = sql.connect("hosts.db")
        cursor = conn.cursor()
        data = "SELECT * FROM HOSTS"
        cursor.execute(data)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        list_hosts = {ip: nombre for _, nombre, ip, _ in datos}
        return datos, list_hosts

    def search(self, host):
        conn = sql.connect("hosts.db")
        cursor = conn.cursor()
        data = f"SELECT * FROM HOSTS WHERE host='{host}'"
        cursor.execute(data)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos

    def update_data(self, nombre, host, estado):
        conn = sql.connect("hosts.db")
        cursor = conn.cursor()
        data = f"UPDATE HOSTS SET host='{host}',estado={estado} WHERE name ='{nombre}'"
        cursor.execute(data)
        conn.commit()
        conn.close()

    def update_state(self, host, state):
        conn = sql.connect("hosts.db")
        cursor = conn.cursor()
        data = f"UPDATE HOSTS SET state={state} WHERE host ='{host}'"
        cursor.execute(data)
        conn.commit()
        conn.close()

    def delete_data(self):
        conn = sql.connect("hosts.db")
        cursor = conn.cursor()
        data = "DELETE FROM HOSTS"
        cursor.execute(data)
        conn.commit()
        conn.close()


host_1 = database()
# host_1.insert_data("antena selva 1", "192.168.1.23", 1)
# host_1.read_data()
# host_1.delete_data()
# host_1.update_state("192.168.110.239", 1)
# host_1.search("192.168.110.117")
