from platform import system
from agent import Agent
from config import *
import anthropic
from anthropic import Anthropic
from anthropic.resources.messages import messages

sceptik = Agent("Sceptik", "Ти скептик — людина, яка схильна сумніватися в загальноприйнятих істинах або неперевірених фактах. Пиши короткі відповіді")

while True:
    text = input("[~]phntmch: ")
    if text.lower() in ("exit", "quit"):
        break
    print("Agent: ", sceptik.run(text))