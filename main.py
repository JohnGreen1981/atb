import os
from fastapi import FastAPI
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
app = FastAPI()


@app.get("/ateo-digest")
def ateo_digest():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Ты — новостной ассистент. Создавай краткий, актуальный дайджест."},
            {"role": "user", "content": "Вот список новостей за сегодня. Составь по ним короткий дайджест для тех, кто хочет быстро понять, что произошло. Не пиши источники, просто выдели суть:\n\n1. [заголовок] — [описание]\n2. ..."}

        ],
        temperature=0.7
    )
    return {"digest": response.choices[0].message.content}
