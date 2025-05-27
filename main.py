from fastapi import FastAPI
import feedparser
import openai

app = FastAPI()

# Важно: правильно передаем ключ
client = openai.OpenAI(api_key="sk-...")  # ← вставь сюда свой API-ключ

@app.get("/ateo-digest")
def ateo_digest():
    rss_url = "https://rsshub.app/telegram/channel/Ateobreaking"
    feed = feedparser.parse(rss_url)
    news_items = "\n\n".join([f"{e.title}\n{e.link}" for e in feed.entries[:10]])

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Сделай краткий, связный дайджест новостей."},
            {"role": "user", "content": news_items}
        ]
    )
    return {"digest": response.choices[0].message.content}
