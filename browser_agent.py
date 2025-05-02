
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def init_browser(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver

def browse_and_collect(url, keyword_filter=None):
    driver = init_browser()
    try:
        print(f"[BROWSER] {url} sayfasina giriliyor...")
        driver.get(url)
        time.sleep(3)

        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        content = [p.text for p in paragraphs if p.text.strip() != ""]

        if keyword_filter:
            content = [c for c in content if keyword_filter.lower() in c.lower()]

        for line in content:
            print(f"[BROWSER][TEXT] {line[:150]}...")

        print(f"[BROWSER] {len(content)} paragraf bulundu.")
        return content
    except Exception as e:
        print(f"[BROWSER] Hata: {e}")
        return []
    finally:
        driver.quit()

# Örnek kullanım
if __name__ == "__main__":
    browse_and_collect("https://www.reuters.com/markets/", keyword_filter="fed")
