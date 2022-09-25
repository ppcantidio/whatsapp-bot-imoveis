from flask import Flask, jsonify

from flask import request
from clients.imoveis_natal.service import ImoveisNatal
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
    if Webhook().verifica_tipo_webhook(response):
        message = Webhook().get_message(response)
        number = message.get("number")
        msg = message.get("message")

        step = Webhook().verify_step(number)
        print(f"step: {step}")

        if step == None and Webhook().verifica_cliente(response) is False:
            ImoveisNatal().step_1_question(number)
        elif step == 1:
            ImoveisNatal().step_1_answer(msg, number)
            ImoveisNatal().step_2_question(number)
    return jsonify({"sucesso": True})


if __name__ == "__main__":
    app.run(host="localhost", port=8000)
