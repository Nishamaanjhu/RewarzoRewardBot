from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os

# Get environment variables
TOKEN = os.getenv("BOT_TOKEN")  # Telegram Bot Token
WEBHOOK_URL = "https://rewarzorewardbot.onrender.com"  # Render URL

# Define FAQs
FAQ_TEXT = """
🤖 Here are some common FAQs:

Q: How can I earn coins on Rewarzo?
A: You can earn coins by watching reward videos, playing games, taking surveys, and completing offers.

Q: How do I redeem coins?
A: Go to the "Redeem" section and choose between UPI, gift cards, or vouchers.

Q: Is there a minimum withdrawal limit?
A: Yes, the minimum withdrawal is 5000 coins.

Q: How to contact support?
A: You can email us at mail@deepakchaudhary.dev or visit the support page in the app.

For more queries, ask me directly!
"""

# Define the /start command handler
async def start(update, context):
    await update.message.reply_text("🤖 Welcome to Rewarzo! Type /help to see available commands.")

# Define the /help command handler
async def help_command(update, context):
    await update.message.reply_text("""
🛠 Available Commands:
/start - Start the bot
/help - Show available commands
/faq - Get common FAQs
""")

# Define the /faq command handler
async def faq(update, context):
    await update.message.reply_text(FAQ_TEXT)

# Handle general messages
async def unknown(update, context):
    await update.message.reply_text("❓ I didn't understand that. Type /faq to see common queries.")

# Create the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("faq", faq))

# Add a fallback message handler
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))

# Set the webhook
app.run_webhook(
    listen="0.0.0.0",
    port=8000,
    url_path=TOKEN,
    webhook_url=f"{WEBHOOK_URL}/{TOKEN}",
)
