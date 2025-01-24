from database import database


class data:
    data_list = {}

    def __init__(self):

        self.host_in = database()

    def data_analysis(self, ip, ip_name):

        if ip == "" or ip_name == "":
            message = ("Campo IP o IP NAME está vacío")
            return message
        else:

            if ip in data.data_list:
                return ("esta ip ya fue ingresada")
            else:
                data.data_list[ip] = ip_name
            message = self.host_in.insert_data(ip_name, ip, 1)
            if message == 1:
                return f"Se ingreso el host:{ip_name} con la IP:{ip}"
            else:
                return "Estos datos estan repetidos"
