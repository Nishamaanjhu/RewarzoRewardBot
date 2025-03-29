from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import random

# Replace with your actual BotFather Token
TOKEN = "7541385041:AAGdRa3BntxsUB_8sOnybUV2zAUeNMpE7xM"

# Function to handle /start command
async def start(update, context):
    await update.message.reply_text("🎉 Welcome to Rewarzo! I'm your friendly chatbot. Ask me anything!")

# Function to handle /help command
async def help_command(update, context):
    await update.message.reply_text("🤖 I can chat with you! Try asking me about Rewarzo rewards or just say hi!")

# Function for intelligent replies
async def handle_message(update, context):
    text = update.message.text.lower()

    # Define possible responses
    responses = {
        "hi": ["Hey there! 👋", "Hello! How can I help you today?", "Hi! 😊"],
        "hello": ["Hello! 😊", "Hey! Need help with Rewarzo?", "Hi there! How's it going?"],
        "rewards": ["You can earn rewards by playing games, watching videos, and completing offers! 🎮🎁"],
        "how are you": ["I'm just a bot, but I'm feeling chatty today! 😄", "Doing great! How about you?"],
        "bye": ["Goodbye! See you soon! 👋", "Take care! Come back anytime! 😊"],
    }

    # Check if message matches any key
    for key, replies in responses.items():
        if key in text:
            await update.message.reply_text(random.choice(replies))
            return

    # Default response if no keyword matches
    await update.message.reply_text("I didn't quite get that. 🤔 Try asking about rewards or just say hi!")

# Create the Application
app = ApplicationBuilder().token(TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Run the bot
print("🤖 Rewarzo Chatbot is running...")
app.run_polling()
