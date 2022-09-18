from flask import Flask, jsonify

from flask import request
from src.services.whatsapp_service import Whatsapp
from src.services.webhook_service import Webhook


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route("/", methods=["POST", "GET"])
def imoveis_natal():
    param = request.args.get("hub.challenge")
    if param is not None:
        return param

    response = request.get_json()
    print(response)

    if Webhook().verifica_tipo_webhook(response):
        Whatsapp().menssagem_simples("5584981631800", "Qual seu nome?")

    return response


if __name__ == "__main__":
    app.run(host="localhost", port=8000)
