from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os

# Get environment variables
TOKEN = os.getenv("BOT_TOKEN")  # Telegram Bot Token
WEBHOOK_URL = "https://rewarzorewardbot.onrender.com"  # Render URL

# Define FAQs for Rewarzo
faq_responses = {
    "how to earn coins": "You can earn coins by watching reward videos, playing HTML games, participating in surveys, and completing offers.",
    "how to redeem coins": "Go to the 'Redeem' section and choose between UPI, gift cards, or vouchers.",
    "minimum withdrawal limit": "The minimum withdrawal is 5000 coins.",
    "download rewarzo app": "You can download the Rewarzo app from this link: https://rewarzo.deepakchaudhary.dev/Rewarzo-App.apk",
    "contact support": "You can mail us on mail@deepakchaudhary.dev or visit our support page in the app.",
    "refer friends": "You can refer friends by sharing your referral link available in the app. When they sign up, you both earn coins.",
    "increase earnings": "To increase your earning potential, complete daily tasks, participate in events, and refer friends to earn bonuses.",
    "report issue": "You can mail us on mail@deepakchaudhary.dev or use the 'Report a Bug' feature in the app.",
    "check earnings history": "You can check your earnings history in the 'History' section of the app.",
    "update payment details": "You can update your payment details in the 'Redeem' section of the app.",
    "coins worth": "Coins are worth 0.01 INR each. 100 coins = 1 INR."
}

# Define the /start command handler
async def start(update, context):
    await update.message.reply_text("🤖 Welcome to Rewarzo! Ask me anything about earning and redeeming rewards. Use /help for available commands.")

# Define the /help command handler
async def help_command(update, context):
    help_text = """🤖 Rewarzo Bot Commands:
/start - Welcome message
/help - List of commands
/faq - Get common FAQs
/contact - Contact support
/redeem - How to redeem coins
/earn - How to earn coins
/download - Download Rewarzo App
/value - Coin value
"""
    await update.message.reply_text(help_text)

# Define command handlers for FAQs
async def faq(update, context):
    faq_text = "\n".join([f"- {q}" for q in faq_responses.keys()])
    await update.message.reply_text(f"🤖 Here are some common FAQs:
{faq_text}\n\nType any of these questions to get an answer.")

# Generic FAQ response handler
async def handle_message(update, context):
    user_message = update.message.text.lower()
    response = faq_responses.get(user_message, "Sorry, I don't have information on that. Try /faq for common questions.")
    await update.message.reply_text(response)

# Create the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("faq", faq))

# Add message handler for FAQs
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Set the webhook
app.run_webhook(
    listen="0.0.0.0",
    port=8000,
    url_path=TOKEN,
    webhook_url=f"{WEBHOOK_URL}/{TOKEN}",
)
