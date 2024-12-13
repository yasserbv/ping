
class data:
    data_list = {}

    def data_analysis(self, ip, ip_name):
        if ip == "" or ip_name == "":
            message = ("Campo IP o IP NAME está vacío")
            return message
        else:

            if ip in data.data_list:
                return ("esta ip ya fue ingresada")
            else:
                data.data_list[ip] = ip_name
                return data.data_list

    def retun_data(self):
        return data.data_list
