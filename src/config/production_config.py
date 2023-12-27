import os

class ProductionConfig:
    def __init__(self):
        self.ENV = "production"
        self.API_ENDPOINT = os.getenv("API_ENDPOINT")
        self.TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
        
