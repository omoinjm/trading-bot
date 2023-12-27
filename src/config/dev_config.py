import os

class DevConfig:
    def __init__(self):
        self.PYTHON_ENV = "development"
        self.API_ENDPOINT = os.getenv("API_ENDPOINT")
        self.TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")