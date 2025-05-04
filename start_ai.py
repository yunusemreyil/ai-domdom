from trade_manager import run_trading_bot
from learn import run_learning_cycle
from self_diagnostics import run_diagnostics
from source_watcher import watch_sources
from chat_ui import start_chat_interface
from ai_update import check_for_updates

if __name__ == "__main__":
    run_diagnostics()
    check_for_updates()
    watch_sources()
    run_learning_cycle()
    run_trading_bot()
    start_chat_interface()
