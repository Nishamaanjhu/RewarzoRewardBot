from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import openai
import os

# Get environment variables
TOKEN = os.getenv("BOT_TOKEN")  # Telegram Bot Token
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # OpenAI API Key
WEBHOOK_URL = "https://rewarzorewardbot.onrender.com"  # Render URL

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

# Define the system prompt for Rewarzo context
SYSTEM_PROMPT = """
You are RewarzoRewardBot, the official support bot for the Rewarzo app.
Rewarzo is a reward-based gaming app where users earn coins by watching videos, playing games, taking surveys, and more.
Coins can be redeemed for UPI payments, gift cards, and vouchers.
Here are some common FAQs for Rewarzo:

{faq}

Use this data to answer relevant user queries. If unsure, politely redirect.
Answer only Rewarzo-related queries. For unrelated questions, politely redirect the user.
"""

faq = """
Q: How can I earn coins on Rewarzo?
A: You can earn coins by watching reward videos, playing HTML games, participating in surveys, and completing offers.

Q: How do I redeem coins?
A: Go to the "Redeem" section and choose between UPI, gift cards, or vouchers.

Q: Is there a minimum withdrawal limit?
A: Yes, the minimum withdrawal is 5000 coins.

Q: How to download the Rewarzo app?
A: You can download the Rewarzo app from this link: https://rewarzo.deepakchaudhary.dev/Rewarzo-App.apk

Q: How to contact support?
A: You can mail us on mail@deepakchaudhary.dev or visit our support page in the app.

Q: How to refer friends?
A: You can refer friends by sharing your referral link available in the app. When they sign up, you both earn coins.

Q: How to increase my earning potential?
A: To increase your earning potential, complete daily tasks, participate in events, and refer friends to earn bonuses.

Q: How to report a bug or issue?
A: You can mail us on mail@deepakchaudhary.dev or use the "Report a Bug" feature in the app.

Q: How to change my account settings?
A: You can change your account settings in the "Profile" section of the app.

Q: How to delete my account?
A: To delete your account, go to "Settings" > "Account" > "Delete Account". Please note that this action is irreversible.

Q: How to check my earnings history?
A: You can check your earnings history in the "History" section of the app.

Q: How to update my payment details?
A: You can update your payment details in the "Reedem" section of the app.

Q: How to change my password?
A: To change your password, go to "login" > "forgot password" > "Change Password".

Q: How to change my email address?
A: To change your email address, go to "Profile" > "Change Email".

Q: How to change my phone number?
A: To change your phone number, go to "Profile" > "Change Phone Number".

Q: How to change my profile picture?
A: To change your profile picture, go to "Profile" > "Change Profile Picture".

Q: How to change my username?
A: To change your username, go to "Profile" > "Change Username".

Q: How to change my notification settings?
A: To change your notification settings, go to "Settings" > "Notifications". Notifications is recommended to be on.

Q : How to change my language settings?
A: To change your language settings, go to "Profile" > "Choose Language".

Q : what are my coins worth?
A: Coins are worth 0.01 INR each. 100 coins = 1 INR.

"""


# Define the /start command handler
async def start(update, context):
    await update.message.reply_text("🤖 Welcome to Rewarzo! Ask me anything about earning and redeeming rewards.")

# Function to get response from OpenAI
async def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# Handle messages and respond using OpenAI
async def chat(update, context):
    user_message = update.message.text
    # Get response from OpenAI with system prompt
    ai_response = await get_ai_response(user_message)
    # Send the response back to the user
    await update.message.reply_text(ai_response)

# Create the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler("start", start))

# Add message handler for any text message
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

# Set the webhook
app.run_webhook(
    listen="0.0.0.0",
    port=8000,
    url_path=TOKEN,
    webhook_url=f"{WEBHOOK_URL}/{TOKEN}",
)
