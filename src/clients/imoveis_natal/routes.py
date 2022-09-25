from flask.views import MethodView
from flask import Blueprint, request, jsonify

from clients.imoveis_natal.service import ImoveisNatal
from src.services.webhook_service import Webhook


imoveis_natal_route = Blueprint("imoveis_natal_route", __name__)


class ImoveisNatalRoutes(MethodView):
    def get(self):
        param = request.args.get("hub.challenge")
        if param is not None:
            return param

    def post(self):
        data = request.json

        message = Webhook().get_message(data)

        if message:
            self.db.insert("cb_menssage", message)

            response = list(self.db.find_object("cb_menssage", message))

            number = message.get("number")
            msg = message.get("message")

            step = Webhook().verify_step(number)
            print(f"step: {step}")

            if step == None and Webhook().verifica_cliente(response) is False:
                ImoveisNatal().step_1_question(number)
            elif step == 1:
                ImoveisNatal().step_1_answer(msg, number)
                ImoveisNatal().step_2_question(number)

        return jsonify({"mensagem": "Mensagem recebida com sucesso!"}), 200


imoveis_natal_view = ImoveisNatalRoutes.as_view("webhook_view")
imoveis_natal_route.add_url_rule("/", view_func=imoveis_natal_view, methods=["POST", "GET"])
