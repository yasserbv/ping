import subprocess
from send_data import data_ping
from database import database


class connected_hosts:
    def __init__(self, hosts, token, chat_id):
        self.hosts = hosts
        self.token = token
        self.chat_id = chat_id

        # Estado inicial de las IPs con un metodo que me llama comprecion de listas
        self.previous_status = {ip: "activa" for ip in self.hosts.keys()}
        # print(self.previous_status)

    def ping_hosts(self):
        # Instancia para enviar datos a Telegram
        data_1 = data_ping(self.token, self.chat_id)
        updata_state = database()

        for ip, ip_name in zip(self.hosts.keys(), self.hosts.values()):
            command = ["ping", "-n", "1", ip]
            ping = subprocess.run(
                command, capture_output=True, text=True)

            # Verificar si el host responde al ping
            if "TTL=" in ping.stdout:
                # Solo "notificar si el estado cambió
                if self.previous_status[ip] == "inactiva":
                    data_1.sending_data(f"{ip_name} ahora responde.")
                self.previous_status[ip] = "activa"
                updata_state.update_state(ip, 1)

            else:
                # Solo notificar si el estado cambió
                if self.previous_status[ip] == "activa":
                    data_1.sending_data(f"{ip_name} no responde.")
                self.previous_status[ip] = "inactiva"
                updata_state.update_state(ip, 0)
