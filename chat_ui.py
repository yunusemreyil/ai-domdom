
import gradio as gr
from source_watcher import run_full_analysis

# Ana sohbet fonksiyonu
def ai_domdom_response(user_input):
    try:
        if "haber" in user_input.lower():
            run_full_analysis()
            return "Haber ve video analizleri tamamlandı."

        elif "video" in user_input.lower():
            # video linki yazıldıysa, analiz et
            if "https://" in user_input:
                link = user_input.split("https://")[1]
                link = "https://" + link
                run_full_analysis(youtube_url=link)
                return f"Video analiz edildi: {link}"
            else:
                return "Lütfen geçerli bir YouTube linki yaz."

        else:
            return "Komut tanınmadı. 'haber' veya 'video [link]' yazabilirsin."

    except Exception as e:
        return f"[HATA] {str(e)}"

# Gradio arayüzü
iface = gr.Interface(
    fn=ai_domdom_response,
    inputs=gr.Textbox(lines=2, placeholder="AI DOMDOM'a yaz: 'haber' veya 'video https://youtube.com/..."),
    outputs="text",
    title="AI DOMDOM - Web Chat (Gerçek Zeka)",
    description="Yapay zekana haber ve video analizi yaptırmak için yaz."
)

if __name__ == "__main__":
    iface.launch()
