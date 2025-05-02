
import os
import json
import time
import subprocess

from trade_manager import run_trading_logic
from learn import train_model
from self_diagnostics import run_diagnostics
from source_watcher import run_full_analysis

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def main():
    config = load_config()
    loop_counter = 0
    print("[AI-DOMDOM] Sistem baslatiliyor...")

    while True:
        print("[AI-DOMDOM] Islemler yapiliyor...")
        run_trading_logic(config)
        train_model(config)
        run_diagnostics(config)

        if loop_counter % 6 == 0:  # Her saat başı bir medya analizi (10s x 6 = 60s x 20 = 20 dakika)
            print("[AI-DOMDOM] Medya analiz modulu calistiriliyor...")
            run_full_analysis("https://www.youtube.com/watch?v=fx7_UwqPz7Y")

        print("[AI-DOMDOM] 10 saniye bekleniyor...")
        time.sleep(10)
        loop_counter += 1

if __name__ == "__main__":
    main()
