import os
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # если ты локально тестируешь и используешь .env файл

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
app = FastAPI()


@app.get("/ateo-digest")
def ateo_digest():
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ты — новостной ассистент. Создавай краткий, актуальный дайджест."},
            {"role": "user", "content": "Сделай дайджест новостей из телеграм-канала ATEO."}
        ],
        temperature=0.7
    )
    return {"digest": response.choices[0].message.content}
