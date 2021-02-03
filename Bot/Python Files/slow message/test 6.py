import telebot  # Импортируем её (Да, импорт именно telebot, хотя устанавливаем PyTelegramBotApi)
from telebot import types  # Импортируем типы для клавиатуры
from requests import get  # Импортирует команду get для получения картинки из ссылки
import random
import time
import datetime
import os
import subprocess
import threading
import re
bot = telebot.TeleBot('1519141781:AAH2Eyd7Ce6H9Nz_t9-vNt0xcKIG1Z5Ldrk')
WhileEnabled = 1
idchat = ""
timesleep = ""
quantity = ""
messege = ""
TimeSay = ""
queue = 0
b = 0
c = 0
Time = ""
FileX = ""
TextFileX = ""
@bot.message_handler(content_types=['text'])
def Keyboard(message):
    global WhileEnabled
    global idchat
    global timesleep
    global quantity
    global messege
    global TimeSay
    global queue
    global b
    global c
    global Time
    global FileX
    global TextFileX
    while WhileEnabled == 1:
        FileX = open(r"C:\TelegramBot\Bot\Python Files\slow message\variables.txt", "rt", encoding='utf8')
        TextFileX = FileX.readlines()
        time.sleep(5)
        c = c + 1
        print("\033[42m\033[30mколичество кругов - " + str(c) + "\033[0m")
        try:
            while WhileEnabled == 1:
                Time = str(time.strftime("%Y")) + str(time.strftime("%m")) + str(time.strftime("%d")) + str(time.strftime("%H")) \
                       + str(time.strftime("%M")) + str(time.strftime("%S"))
                a = int(queue) * 5
                idchat = TextFileX[int(queue) + a + 1]
                idchat = re.sub(" |\n", "", idchat)
                timesleep = TextFileX[int(queue) + a + 2]
                timesleep = re.sub(" |\n", "", timesleep)
                quantity = TextFileX[int(queue) + a + 3]
                quantity = re.sub(" |\n", "", quantity)
                messege = TextFileX[int(queue) + a + 4]
                messege = re.sub("|\n", "", messege)
                TimeSay = TextFileX[int(queue) + a + 5]
                TimeSay = re.sub(" |\n", "", TimeSay)
                print("idchat = " + idchat)
                print("timesleep = " + timesleep)
                print("quantity = " + quantity)
                print("messege = \"" + messege + "\"")
                print("TimeSay = " + TimeSay + "\n")
                while b != int(quantity) and Time > TimeSay:
                    time.sleep(float(timesleep))
                    bot.send_message(idchat, messege)
                    print("\033[42m\033[30m" + idchat + " " + messege + "\033[0m")
                    b = int(b) + 1
                else:
                    print("\n")
                    b = 0
                queue = int(queue) + 1
        except:
            print("список закончился")
            idchat = ""
            timesleep = ""
            quantity = ""
            messege = ""
            TimeSay = ""
            queue = 0
            a = 0
            b = 0
        FileX.close()
bot.polling(none_stop=True)