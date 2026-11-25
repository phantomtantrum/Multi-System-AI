from platform import system
from agent import Agent
import anthropic
from anthropic import Anthropic
from anthropic.resources.messages import messages
from config import ANTHROPIC_API_KEY

optimist = Agent("Optimist", "Ти людина з позитивною життєвою позицією, яка вірить у краще майбутнє, очікує успіху своїх починань і вмієш знаходити рішення або позитивні сторони навіть у складних обставинах. Пиши коротко.")

while True:
    text = input("[~]phntmch: ")
    if text.lower() in ("exit", "quit"):
        break
    print("Agent: ", optimist.run(text))