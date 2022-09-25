from datetime import datetime

from src.services.whatsapp_service import Whatsapp
from src.services.database_service import Database


class ImoveisNatal:
    def step_1_question(self, number):
        print(number)
        text_1 = "Olá, seja bem vindo ao auto atendimento do Imoveis Natal!"
        text_2 = "Antes de começar seu atendimento preciso que você me diga seu nome em uma unica mensagem."

        Whatsapp().simple_message(number, text_1)
        Whatsapp().simple_message(number, text_2)

        log = {"number": number, "step": 1, "datetime": datetime.now()}
        Database().insert_object(log, "logs")

    def step_1_answer(self, message, number):
        Database().insert_object({"name": message, "number": number}, "clients")

    def step_2_question(self, number):
        text_1 = "Você está procurando aparamento de quantos quartos?"
        text_2 = "Quantos quartos?"
        options = ["1 quarto", "2 quartos", "3 quartos", "4 quartos", "5 quartos", "6 quartos ou mais"]
        Whatsapp().mensagem_lista(number, text_1, text_2, options)
