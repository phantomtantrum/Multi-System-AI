# lesson3.py
from agent import Agent, tool


@tool("Повертає поточну погоду в місті", city="Назва міста")
def get_weather(city: str) -> str:
    fake = {"київ": "+3°C, хмарно", "львів": "+1°C, дощ"}
    return fake.get(city.lower(), "немає даних")


@tool("Обчислює арифметичний вираз", expression="Наприклад (2+3)*4")
def calculate(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        raise ValueError("недопустимі символи")
    return str(eval(expression))


assistant = Agent("assistant", "Ти помічник. Використовуй інструменти, не вигадуй дані.",
                  tools=[get_weather, calculate])

print(assistant.run("Яка погода у Києві й Львові? І скільки буде 17*23?"))