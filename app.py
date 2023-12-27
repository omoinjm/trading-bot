import inspect
import logging
from src import app, config
from src.bot_commands import Bot
from telegram.ext import CommandHandler, MessageHandler, filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main() -> None:
    bot = Bot(config.API_ENDPOINT)

    # Check if bot.start is a coroutine function
    if inspect.iscoroutinefunction(bot.start):
        print("bot.start is a coroutine function")
    
    # Check if bot.handle_message is a coroutine function
    if inspect.iscoroutinefunction(bot.handle_message):
        print("bot.handle_message is a coroutine function")

    if inspect.iscoroutinefunction(app):
        print("app is a coroutine function")

    app.add_handler(CommandHandler("start", bot.start))
    app.add_handler(MessageHandler(filters.TEXT, bot.handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()

