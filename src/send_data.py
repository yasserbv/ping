import requests


class data_ping:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def sending_data(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        params = {
            "chat_id": self.chat_id,
            "text": message
        }
        response = requests.get(url, params=params)
        return response.json
