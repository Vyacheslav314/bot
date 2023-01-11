from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters, Updater, ApplicationBuilder
import parser
from credits import bot_token
from Show_parse import show_weather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Приветcтвую {update.effective_user.first_name}\n'
                                    f'Я бот студента GB Вячеслава\n'
                                    f'Пока что я могу показывать только погоду\n'
                                    f'Вот список команд\n'
                                    f'/today Показывает прогноз на сегодня\n'
                                    f'/tomorrow Показывает прогноз на завтра\n'
                                    f'/week Показывает прогноз на следующие 5 дней')


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Прогноз на сегодня:\n {parser.weather_today}')


async def tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Прогноз на завтра:\n {show_weather(parser.data_weather_tomorrow)}')


async def week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Прогноз на неделю:\n {show_weather(parser.data_weather_week)}')



app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler("today", today))
app.add_handler(CommandHandler('tomorrow', tomorrow))
app.add_handler(CommandHandler('week', week))

app.run_polling()

