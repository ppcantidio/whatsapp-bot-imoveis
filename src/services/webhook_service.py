class Webhook:
    def get_number(self, request: dict):
        entry = request.get("entry", [])
        entry = entry[0]
        changes = entry.get("changes", [])
        changes = changes[0]
        value = changes.get("value", {})
        messages = value.get("messages", [])
        message = messages[0]
        number = message.get("from")
        text = message.get("text")
        body = text.get("body")

        return {"number": number, "message": body}

    def verifica_registro(self, request: dict):
        mensagem = self.get_number(request)
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
