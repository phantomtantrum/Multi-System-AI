from http.client import responses
from idlelib import history
from os import system

import anthropic
from anthropic import Anthropic
from config import *

client = Anthropic(api_key=ANTHROPIC_API_KEY)
MODEL = "claude-haiku-5-5"
MAX_TOKENS = 8192

def text_of(response) -> str:
    return "".join(b.text for b in response.content if b.type == "text")

class Agent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions
        self.history = []

    def run(self, message: str):
        if(sum(1 for item in self.history if item.get("role") == "user") <= 4):
            self.history.append({"role": "user", "content": message})
            responce = client.messages.create(
                model=MODEL, max_tokens=MAX_TOKENS, system = self.instructions,
                messages=self.history
            )
            self.history.append({"role": "assistant", "content": responce.content})
            return text_of(responce)
        else:
            self.history.clear()
            return "You had a limit, but you can continue"

    def reset(self):
        self.history = []