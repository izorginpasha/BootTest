import telebot
from config import TOKEN, keys
from extensions import CryptoConverter, ConvertionException

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ("Чтобы начать работу введите комманду боту в следующем формате: \n <имя валюты> \
<в какую валюту перевести> \
<количество переводимои валюты> \n  Увидеть весь список валют: /values")
    bot.reply_to(message, text)


# Обрабатываются все сообщения, содержащие команды '/values'.
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = ("Доступные валюты: ")
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(massage: telebot.types.Message):
    try:
        values = massage.text.split(' ')
        if len(values) > 3:
            raise ConvertionException("Слишком много параметров")

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(massage,f"Ошибка пользователя.\n {e}")
    except Exception as e:
        bot.reply_to(massage, f"Не удалось обработать команду\n{e}")
    else:
        text = f"Цена {amount} {quote} в {base} - {total_base}"
        bot.send_message(massage.chat.id, text)


bot.polling()
