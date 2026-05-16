from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8542343376:AAEo_vHYY1HDv3CtD5McvHSRABSz8pkFWGc"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [" Diamond Prices"],
        [" Buy Account"],
        [" Admin"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        " Mythic Vault မှ ကြိုဆိုပါတယ်!",
        reply_markup=reply_markup
    )


async def message_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == " Diamond Prices":
        await update.message.reply_text(
            " Diamond Prices\n\n86  =  2000 Ks\n172  = 4000 Ks"
        )

    elif text == " Buy Account":
        await update.message.reply_text(
            " Available MLBB Accounts\n\nEpic / Legend / Mythic Accounts"
        )

    elif text == " Admin":
        await update.message.reply_text(
            " Admin - @YourTelegramName"
        )

    elif text == "Hi" or text == "Hello" or text == "Hey":
        await update.message.reply_text(
            "Hello  Welcome to Mythic Vault!"
        )   
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message_reply))

print("Bot running...")

app.run_polling()
