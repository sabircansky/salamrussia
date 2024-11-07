from telegram import Update
from telegram.ext import ContextTypes
from utils.language_codes import LANGUAGE_CODES

async def handle_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    language_buttons = [[lang] for lang in LANGUAGE_CODES.keys()]
    await update.message.reply_text("Выберите язык:", reply_markup={"keyboard": language_buttons})
