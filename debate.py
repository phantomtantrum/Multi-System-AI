# debate.py
import json
from agent import Agent

TOPIC = "Чи варто вчити програмування у 2026 році, якщо є AI-агенти?"
ROUNDS = 3

RULES = ("Відповідай 3–4 реченнями. Обов'язково відповідай на останній аргумент "
         "суперника, а потім додай свій новий. Не повторюй уже сказане.")

pro = Agent("pro", verbose=False, instructions=
    f"Ти учасник дебатів. Тема: «{TOPIC}». Ти захищаєш позицію ЗА. {RULES}")

con = Agent("con", verbose=False, instructions=
    f"Ти учасник дебатів. Тема: «{TOPIC}». Ти захищаєш позицію ПРОТИ. {RULES}")

judge = Agent("judge", verbose=False, instructions=
    "Ти неупереджений суддя дебатів. Оцінюй силу аргументів і те, наскільки "
    "учасники відповідали один одному, а не власну думку щодо теми. "
    'Відповідай ЛИШЕ JSON: {"winner": "pro" або "con", "pro_score": 1-10, '
    '"con_score": 1-10, "best_argument": "...", "reason": "..."}')


def parse_json(text: str) -> dict:
    """Модель іноді обгортає JSON у ```json ... ``` — беремо від першої { до останньої }."""
    start, end = text.find("{"), text.rfind("}")
    return json.loads(text[start:end + 1])


transcript = []
last_speech = "Відкрий дебати своїм найсильнішим аргументом."

for round_no in range(1, ROUNDS + 1):
    for label, speaker in (("ЗА", pro), ("ПРОТИ", con)):
        prompt = (last_speech if not transcript
                  else f"Суперник сказав:\n«{last_speech}»\n\nТвоя відповідь:")
        speech = speaker.run(prompt)
        transcript.append(f"{label}: {speech}")
        print(f"\n--- Раунд {round_no} · {label} ---\n{speech}")
        last_speech = speech

print("\n=== Суддя радиться... ===")
raw = judge.run(f"Тема: {TOPIC}\n\nСтенограма:\n\n" + "\n\n".join(transcript))

try:
    v = parse_json(raw)
    winner = "ЗА" if v["winner"] == "pro" else "ПРОТИ"
    print(f"Переможець: {winner}  (ЗА {v['pro_score']}/10 · ПРОТИ {v['con_score']}/10)")
    print(f"Найкращий аргумент: {v['best_argument']}")
    print(f"Чому: {v['reason']}")
except (ValueError, KeyError):
    print("Суддя відповів не у форматі JSON:\n", raw)   # запасний варіант