
import os
import datetime
from textblob import TextBlob
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def save_journal_entry(user: str, entry_time: str, content: str) -> str:
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%B")
    day = now.strftime("%d")

    blob = TextBlob(content)
    mood_score = blob.sentiment.polarity
    mood_tag = (
        "Positive" if mood_score > 0.2 else "Negative" if mood_score < -0.2 else "Neutral"
    )

    try:
        summary_result = summarizer(content, max_length=50, min_length=15, do_sample=False)
        summary = summary_result[0]["summary_text"]
    except:
        summary = "Summary not available."

    user_folder = os.path.join("journal_logs", user, year, month, day)
    os.makedirs(user_folder, exist_ok=True)

    timestamp = now.strftime("%I-%M%p").lower()
    filename = f"{mood_tag.lower()}_log_{timestamp}.txt"
    path = os.path.join(user_folder, filename)

    with open(path, "w") as f:
        f.write(f"🕒 Entry Time: {entry_time}\n")
        f.write(f"😊 Mood: {mood_tag}\n")
        f.write("📝 Entry:\n")
        f.write(content + "\n")
        f.write(f"\n📋 Summary:\n{summary}\n")

    return f"Journal saved: {filename}"

def analyze_mood(text: str) -> str:
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    if score > 0.2:
        return "Positive"
    elif score < -0.2:
        return "Negative"
    return "Neutral"

def summarize_entry(text: str) -> str:
    try:
        result = summarizer(text, max_length=50, min_length=15, do_sample=False)
        return result[0]["summary_text"]
    except:
        return "Summary not available."

def read_entry(path: str) -> str:
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return "Entry not found."
