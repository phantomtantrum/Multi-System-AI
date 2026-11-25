from platform import system
from agent import Agent
import anthropic
from anthropic import Anthropic
from anthropic.resources.messages import messages

tutor = Agent("tutor", "Ти терплячий репетитор з математики. Пояснюй просто.")

while True:
    text = input("[~]phntmch: ")
    if text.lower() in ("exit", "quit"):
        break
    print("Agent: ", tutor.run(text))