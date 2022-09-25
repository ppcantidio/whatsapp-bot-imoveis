from src.services.database_service import Database
from datetime import datetime
import re


class Webhook:
    def get_message(self, data: dict):
        entry = data.get("entry", [])

        if entry is not None:
            entry = entry[0]
            changes = entry.get("changes")
            changes = changes[0]
            value = changes.get("value")

            messages = value.get("messages")

            if messages is None:
                return False

            messages = messages[0]

            number_format = re.search(r"(\d{2})(\d{2})(\d{8,9})", messages["from"])

            if len(number_format.group(3)) == 8:
                new_number = f"{number_format.group(1)}{number_format.group(2)}9{number_format.group(3)}"
            else:
                new_number = f"{number_format.group(1)}{number_format.group(2)}{number_format.group(3)}"

            contacts = value.get("contacts")

            if contacts is None:
                return False

            contacts = contacts[0]

            profile = contacts.get("profile")
            name = profile.get("name")
            number = new_number
            timestamp = messages.get("timestamp")
            type_menssage = messages.get("type")
            body = messages.get(type_menssage)

        response = {
            "number": number,
            "name": name,
            "timestamp": timestamp,
            "body": body,
            "type_menssage": type_menssage,
            "created_at": datetime.now(),
            "read": False,
            "step": None,
        }

        return response

    def verifica_registro(self, request: dict):
        mensagem = self.get_message(request)
        numero = mensagem.get("number")
        message = mensagem.get("message")

    def verifica_tipo_webhook(self, request: dict):
        entry = request.get("entry", [])
        entry = entry[0]
        changes = entry.get("changes", [])
        changes = changes[0]
        value = changes.get("value", {})
        messages = value.get("messages")
        if messages:
            return True
        return False

    def verifica_cliente(self, request: dict):
        message = self.get_message(request)
        number = message.get("number")

        client = Database().select_one_object("clients", {"number": number})
        if client:
            return True

        return False

    def verify_step(self, number):
        log = list(Database().select_col("logs", where={"number": number}).sort("datetime", -1))
        if not log:
            return None
        return log[0].get("step")
