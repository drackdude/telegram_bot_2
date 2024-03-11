from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler ,filters , ContextTypes
import download_from_youtube
import os

TOKEN = os.environ.get("TOKEN")


# commands

async def help_commant(update : Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        this is bot for video and audio downloading
        for cuting add /cut comment
        """
        )


async def cut_commant(update : Update , context : ContextTypes.DEFAULT_TYPE):
    print(context.args)


# responses
async def message_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text
        file = download_from_youtube.download_audio(text)
        if file:  
            with open(file, 'rb') as audio_file:
                await update.message.reply_document(audio_file)
                print("send succes")
            os.remove(file)  
        else:
            await update.message.reply_text("Failed to download audio.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")


# error 
async def error(update : Update , context : ContextTypes.DEFAULT_TYPE):
    print(f"error : {context.error}")


#main logic
if __name__ == "__main__":
    print("bot working ...")
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler("help",help_commant))
    app.add_handler(CommandHandler("cut",cut_commant))


    app.add_handler(MessageHandler(filters.TEXT , message_handle))


    app.add_error_handler(error)


    app.run_polling(poll_interval=3)
    print("polling ...")
