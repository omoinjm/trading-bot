import os
from dotenv import load_dotenv
from src.config.config import Config
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# loading environment variables
load_dotenv()

# calling the environment configuration
python_env = os.getenv("PYTHON_ENV")

if python_env == "DEV":
    config = Config().dev_config
elif python_env == "PROD":
    config = Config().production_config
else:
    raise ValueError("Invalid value for PYTHON_ENV")

# making our application to use dev env
app = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()