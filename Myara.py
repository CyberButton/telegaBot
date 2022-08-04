import telebot

from apscheduler.schedulers.blocking import BlockingScheduler

bot = telebot.TeleBot('5326250099:AAEWi-VcjkA8F-bqp0yO_FA1mKqTOnquUXE')


@bot.message_handler()
def start():
    bot.send_message(864119119, '1h just passed')


# bot.polling(non_stop=True)
scheduler = BlockingScheduler()
scheduler.add_job(start, 'interval', seconds=5)
scheduler.start()
