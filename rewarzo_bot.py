from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os

# Get the bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://rewarzorewardbot.onrender.com"  # Replace with your actual Render URL

# Define the /start command handler
async def start(update, context):
    await update.message.reply_text("🤖 Rewarzo Bot is now online! Send me anything!")

# Define a message handler for all text messages
async def echo(update, context):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

# Create the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler("start", start))

# Add message handler for any text message
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Set the webhook
app.run_webhook(
    listen="0.0.0.0",
    port=8000,
    url_path=TOKEN,
    webhook_url=f"{WEBHOOK_URL}/{TOKEN}",
)
