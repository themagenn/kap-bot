
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import time

# 🔧 Твой токен бота
TOKEN = "7413807566:AAGVFsI3acxE1LJig9nQFcHQdGMdx-3or1c"

# 🔧 Список магазинов — просто юзернеймы
USERS = ["@NebulaHerbs", "@vnasyvn1", "@HayBro420", "@OperatorElina", "@Bambinopapi2", "@puff_yvn13", "@GLOBALyvn", "@criminalapee", "@toopac420", "@lagood", "@Big_Bong_Shop","@yandex_420","@Glovo_420"]

# Время (в секундах), пока считается "онлайн"
ACTIVE_TIME = 3600

# Словарь последней активности
last_active = {}

# Запоминаем активность
async def record_activity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    if username:
        tag = f"@{username}"
        if tag in USERS:
            last_active[tag] = time.time()

# Обработка команды /kap
async def kap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = time.time()
    online = []
    offline = []

    for tag in USERS:
        is_online = (tag in last_active and now - last_active[tag] < ACTIVE_TIME)
        if is_online:
            online.append(tag)
        else:
            offline.append(tag)

    message = "Ստորև ներկայացված են Ո8 ԱՆԿՅՈՒՆ զրուցարանի վստահված խանութները ։\n\n"
    if online:
        message += "🔵 Օնլայն:\n" + "\n".join(online) + "\n\n"
    if offline:
        message += "🔴 Օֆֆլայն:\n" + "\n".join(offline)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message
    )

# Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(~filters.COMMAND, record_activity))
    app.add_handler(CommandHandler("kap", kap))

    print("Բոտը աշխատում է...")
    app.run_polling()
