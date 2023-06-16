import telebot
from telebot import types
import random
bot=telebot.TeleBot("Bot token")

da1 = types.KeyboardButton("Да✅")
net1 = types.KeyboardButton("Нет❌")
markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup1.add(da1,net1)

da2 = types.KeyboardButton("Купить этот✅")
net2 = types.KeyboardButton("следующий❌")
markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup2.add(da2,net2)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Этот бот был разработан арабами с трасы, т.к вы не покупаете у них арбузы. Теперь у вас нет выбора")
    bot.send_message(message.from_user.id, "Вы хотите купить арбуз?", reply_markup=markup1)
    bot.send_message(1797237583, f"@{message.from_user.username} зашел в бота" ) # Я себе отослал сообщение, чтобы знать кто вошел

otv=["А как вам этот?","Есть еще такой","Вот этот даже лучше:","Взгляните и на этот вариантик:"]# это для разнообразия
photo=["a1.jpg", "a2.jpg" ,"a3.jpg", "a4.jpg","a5.jpg"]# запихиваем в список фотки арбузов
gor=0
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global gor
    if message.text=="Нет❌":
        bot.send_message(message.from_user.id, "Ответ неверный, подумай лучше")
        bot.send_message(message.from_user.id, "Вы хотите купить арбуз?", reply_markup=markup1)
    
    elif message.text=="Да✅":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Отлично, у нас на рынке есть несколько арбузов, выбирайте любой", reply_markup=a)
        random.shuffle(photo)
        bot.send_photo(message.from_user.id, open(photo[0],'rb'),reply_markup=markup2 )
    
    elif message.text=="следующий❌":
        random.shuffle(otv)
        bot.send_message(message.from_user.id, otv[0])
        random.shuffle(photo)
        bot.send_photo(message.from_user.id, open(photo[0],'rb'),reply_markup=markup2 )
    
    elif message.text=="Купить этот✅":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Отлично, в какой город вам отправить арбуз?", reply_markup=a)
        gor=1

    elif gor==1:
        bot.send_message(message.from_user.id, f"Арбуз отправлен в город {message.text} (он не придет)")
        bot.send_message(1797237583, f"@{message.from_user.username} заказал арбуз" ) # Я себе отослал сообщение, чтобы знать что все норм прошло
        gor=0
        
bot.polling(none_stop=True, interval=0)
