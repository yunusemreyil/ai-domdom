import os
import json
import time
import subprocess

from trade_manager import run_trading_logic
from learn import train_model
from self_diagnostics import run_diagnostics


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def main():
    config = load_config()
    print("[AI-DOMDOM] Sistem baslatiliyor...")

    while True:
        print("[AI-DOMDOM] Islemler yapiliyor...")
        run_trading_logic(config)
        train_model(config)
        run_diagnostics(config)
        print("[AI-DOMDOM] 10 saniye bekleniyor...")
        time.sleep(10)


if __name__ == "__main__":
    main()