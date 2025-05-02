
import os
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import subprocess
import whisper
from pytube import YouTube
import time

def fetch_news_headlines():
    urls = [
        "https://www.bloomberg.com/",
        "https://www.reuters.com/markets/",
        "https://www.cnbc.com/world/?region=world"
    ]
    headlines = []
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            for tag in soup.find_all(["h1", "h2", "h3"]):
                text = tag.get_text().strip()
                if 20 < len(text) < 150:
                    headlines.append(text)
        except Exception as e:
            print(f"[NEWS] {url} okunamadi: {e}")
    return headlines

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    return polarity

def analyze_news():
    headlines = fetch_news_headlines()
    if not headlines:
        print("[NEWS] Haber bulunamadi.")
        return
    scores = []
    for headline in headlines:
        score = analyze_sentiment(headline)
        scores.append(score)
        print(f"[NEWS] '{headline}' → Skor: {score:.2f}")
    avg = sum(scores)/len(scores) if scores else 0
    print(f"[NEWS] Ortalama duygu skoru: {avg:.2f}")
    return avg

def download_and_transcribe_youtube(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        out_file = audio_stream.download(filename="yt_audio.mp4")

        print("[YT] Ses indirildi. Whisper'a gönderiliyor...")
        model = whisper.load_model("base")
        result = model.transcribe("yt_audio.mp4")
        print("[YT] Metin:")
        print(result["text"])
        return result["text"]
    except Exception as e:
        print(f"[YT] YouTube indirilemedi: {e}")
        return ""

def run_full_analysis(youtube_url=None):
    print("\n--- [1] HABER ANALİZİ ---")
    analyze_news()

    if youtube_url:
        print("\n--- [2] YOUTUBE TRANSKRİPT ANALİZİ ---")
        text = download_and_transcribe_youtube(youtube_url)
        if text:
            sentiment = analyze_sentiment(text)
            print(f"[YT] Video duygu skoru: {sentiment:.2f}")
        else:
            print("[YT] Transkript bulunamadi.")
    else:
        print("[YT] Video URL verilmedi.")

if __name__ == "__main__":
    while True:
        run_full_analysis("https://www.youtube.com/watch?v=fx7_UwqPz7Y")  # Powell konuşması örnek
        print("[AI-WATCHER] 20 dakika bekleniyor...")
        time.sleep(1200)  # 20 dakika bekle
