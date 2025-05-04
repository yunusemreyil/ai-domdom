import json
import time
from datetime import datetime

with open("config.json", "r") as f:
    config = json.load(f)

# Binance API bilgisi eksikse al-sat işlemini tamamen devre dışı bırak
if "binance_api_key" not in config or "binance_api_secret" not in config:
    print("[trade_manager] Binance API bilgisi yok. Al-sat modülü devre dışı bırakıldı.")

    def run_trading_bot():
        print("[trade_manager] Al-sat modülü atlandı.")
        while True:
            time.sleep(60)

else:
    try:
        from binance.client import Client

        client = Client(config["binance_api_key"], config["binance_api_secret"])

        def run_trading_bot():
            print("[trade_manager] Binance bot başlatıldı.")
            while True:
                now = datetime.now()
                if now.month < 4:
                    print(f"[trade_manager] Şu an {now.month}. aydayız. Al-sat devre dışı.")
                    time.sleep(60)
                    continue

                try:
                    price = float(client.get_symbol_ticker(symbol="BTCUSDT")["price"])
                    print(f"[trade_manager] BTC fiyatı: {price}")

                    if price < 60000:
                        order = client.order_market_buy(symbol="BTCUSDT", quantity=0.001)
                        print("[trade_manager] ALIM YAPILDI", order)

                    elif price > 70000:
                        order = client.order_market_sell(symbol="BTCUSDT", quantity=0.001)
                        print("[trade_manager] SATIŞ YAPILDI", order)

                    time.sleep(60)
                except Exception as e:
                    print(f"[trade_manager] Binance işlem hatası: {e}")
                    time.sleep(60)

    except Exception as e:
        print(f"[trade_manager] Binance bağlantısı başarısız: {e}")

        def run_trading_bot():
            print("[trade_manager] Al-sat modülü hata nedeniyle devre dışı.")
            while True:
                time.sleep(60)
