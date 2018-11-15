import telebot, base64, json, requests

bot = telebot.TeleBot('706468679:AAHc55R6nUwf1AHbYRGPEmkoza9Mh49hXtY')

getupdates = types.InlineKeyboardMarkup(row_width=1)
getupdatesbutton = types.InlineKeyboardButton(text="Получать обновление", callback_data="getupdates")
getupdates.add(getupdatesbutton)

@bot.message_handler(commands=["start"])
def start(message):
     bot.send_message(message.chat.id, text="Начало работы!", reply_markup=getupdates)

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
     if c.data == 'getupdates':
          link = "https://api.github.com/repos/Stuffman/change/contents/Transaction.txt"
          F = requests.get(link)
          L = base64.b64decode(F.json()['content'])
          R = L.decode('utf-8')
          a = 0
          b = 0
          with open('Tr.txt', 'w') as TRW:
               TRW.write(R)
          TRW.close()
          with open('Tr.txt', 'r') as TR:
               for line in TR:
                    a = a + 1
          TR.close()
          with open('Lines.txt', 'r') as NL:
               b = int(NL.read())
          NL.close()
          if (a > b):
               n = a - b
               i = 0
               while i < n:
                    bot.send_message(message.chat.id, text="Одна новая транзакция")
                    i = i + 1
               with open('Lines.txt', 'w') as new:
                    new.write(b)
               new.close()

          bot.polling(none_stop=True)

if __name__ == '__main__':
     bot.polling(none_stop=True)
