from telegram.ext import ContextTypes
from telegram import Update
import requests

class Bot:
    # Define the class variable
    api_endpoint = None

    def __init__(self, api_endpoint):
        # Set the class variable when an instance is created
        Bot.api_endpoint = api_endpoint

    # Define the command handler
    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('Hello! Send me a payload, and I will forward it to the API.')

    # Define the function to handle messages
    @staticmethod
    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Get the user's message
        user_message = update.message.text

        # Send the payload to the API with the custom Cookie headers
        response = requests.get(Bot.api_endpoint)

        # Check the API response
        if response.status_code == 200 or response.status_code == 201:
            await update.message.reply_text('Payload sent successfully!')
            await update.message.reply_text(response.text)  # Use response.text to get the response content
        else:
            await update.message.reply_text('Failed to send payload to the API.')
