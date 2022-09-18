import os
import json
import requests


class Whatsapp:
    def __init__(self):
        self.from_number = os.environ.get("WHATSAPP_NUMBER")
        self.version = os.environ.get("WHATSAPP_VERSION")
        self.token = os.environ.get("WHATSAPP_TOKEN")
        self.url = f"https://graph.facebook.com/{self.version}/{self.from_number}/messages"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }

    def menssagem_simples(self, to_number, menssagem):

        payload = json.dumps({"messaging_product": "whatsapp", "to": to_number, "text": {"body": menssagem}})

        response = requests.request("POST", self.url, headers=self.headers, data=payload)

        print(response.text)

    def menssagem_lista(self, data, pergunta, titulo, opcoes):
        to_number = data.get("number")

        payload = json.dumps(
            {
                "messaging_product": "whatsapp",
                "to": to_number,
                "recipient_type": "individual",
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {"text": pergunta},
                    "action": {
                        "button": "opções",
                        "sections": [
                            {
                                "title": titulo,
                                "rows": [opcoes],
                            }
                        ],
                    },
                },
            }
        )

        response = requests.request("POST", self.url, headers=self.headers, data=payload)

        print(response.text)
