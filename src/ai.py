import os

from typing import List

from decouple import config
from langchain_groq import ChatGroq

from components import Message

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:

    def __init__(self):
        self.__llm = ChatGroq(model='llama-3.2-90b-vision-preview')

    def __build_messages(self, user_message):
        messages = [
            (
                'system',
                'Você é um assistente responsável por tirar duvidas sobre programação'
                'Responda em Markdown.'
                ),
        ]
        messages.append(
            (
                'user',
                user_message,
            )
        )
        return messages

    

    def invoke(self, user_message):
        messages = self.__build_messages(
            user_message=user_message,
        )
        return self.__llm.invoke(messages).content