import logging
from src import app, config
from src.bot_commands import Bot
from telegram.ext import CommandHandler, MessageHandler, filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main() -> None:
    bot = Bot(config.API_ENDPOINT)

    app.add_handler(CommandHandler("start", bot.start))

     # Add message handler for handling all messages
    app.add_handler(MessageHandler(filters.TEXT, bot.handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()

