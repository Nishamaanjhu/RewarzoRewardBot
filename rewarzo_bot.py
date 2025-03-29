from telegram.ext import ApplicationBuilder, CommandHandler
import os

# Get the bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://rewarzorewardbot.onrender.com"  # Replace with your actual Render URL

# Define the /start command handler
async def start(update, context):
    await update.message.reply_text("🤖 Rewarzo Bot is now online!")

# Create the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler("start", start))

# Set the webhook
app.run_webhook(
    listen="0.0.0.0",
    port=8000,
    url_path=TOKEN,
    webhook_url=WEBHOOK_URL,
)
