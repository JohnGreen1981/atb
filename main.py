from fastapi import FastAPI
import feedparser
from openai import OpenAI  # ⚠️ именно так

app = FastAPI()

client = OpenAI(api_key="sk-...")  # вставь свой ключ

@app.get("/ateo-digest")
def ateo_digest():
    rss_url = "https://rsshub.app/telegram/channel/Ateobreaking"
    feed = feedparser.parse(rss_url)
    news = "\n\n".join([f"{entry.title}\n{entry.link}" for entry in feed.entries[:10]])

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ты — новостной помощник. Сделай короткий, связный дайджест:"},
            {"role": "user", "content": news}
        ]
    )
    return {"digest": response.choices[0].message.content}
