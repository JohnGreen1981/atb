from fastapi import FastAPI
import feedparser
import openai

app = FastAPI()
openai.api_key = "sk-..."  # ← вставь свой API-ключ

@app.get("/ateo-digest")
def ateo_digest():
    rss_url = "https://rsshub.app/telegram/channel/Ateobreaking"
    feed = feedparser.parse(rss_url)
    news = "\n\n".join([f"{e.title}\n{e.link}" for e in feed.entries[:10]])
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Сделай краткий, связный дайджест из новостей."},
            {"role": "user", "content": news}
        ]
    )
    return {"digest": response.choices[0].message.content}
