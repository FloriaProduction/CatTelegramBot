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
bot = telebot.TeleBot('1410812387:AAHeuGUmUDaGoeOgltlsGl8-E2mY_kJ6nRQ')
# -*- coding: utf-8 -*-
# системные
Namebot = "Cat-girl"
Password = "-419106290"  # пароль от бота
FirstStartBot = 1  # самый первый запуск бота
FirstStart = 2  # первый запуск бота
Enabled = 1  # вкл/выкл бот
OnOffBot = 1  # 1 - вкл, 0 - выкл
Stage1 = 0  # номер стадии1
Stage2 = 0  # номер стадии2
Stage3 = 0  # номер стадии3
Error = 0  # произошла ли ошибка, 0 - нет, 1 - да
Debug = "1"  # вкл/выкл отладку
WhileEnabled = 1  # вкл/выкл циклы в коде
# работа с файлами/папками
TxtFileUsers = ""
TxtFileSaves = ""
DiskC = os.path.dirname(os.path.abspath(__file__))
os.chdir(DiskC)
print(DiskC)
Notes = ""
NotesRead = ""
FileNumber = 0  # id фалов
# работа с тектом
LastMesseger = 0  # номер последнего предложения, 1 - доброе утро
Random = 1  # нужная фигня
index = 0  # нужна фигня
commands = []  # список со словами
TipMesseger = 0  # тип вопроса 0 - нету сообщения, 1 - сообщение которое начинается с "а", 2 - сообщение которое нужно загуглить
EndSign = 0  # знак в конце сообщения, 1 - точка, 2 - восклицательный знак, 3 - вопросительный знак, 4 - многоточие
StartSign = 0  # буква в начале сообщения, 1 - "а"
NumberTask = 1  # Чем занят бот, 0 - ничем, 1 - спала,
NumberNewTask = 0  # то чем бот будет делать после 0 - незнаю
response = ""  # ответ который состоит из всех команд
response2 = " "  # ответ на сообщение "поиск" или "открой"
# работа с аудио
AudioHello = ""
AudioNya = ""
# работа со временем
TimeOut = 18000  # сколько должно пройти времени с последнего сообщения
day = 0  # день, который должен ностать
hours = 0  # час, который должен ностать
minutes = 0  # минута, которая должна ностать
seconds = 0  # секунда, которая должна ностать
Time_1 = 0  # сколько время сейчас
Time_2 = 0  # сколько время сейчас без дня и месяца
Time1 = 0  # сколько время должно пройти (прибавление + 10 сек)
Time2 = "010000"  # 10 часов вечера
Time3 = "010001"  # 7 часов утра
# работа с доступок к боту
AccessTypeToBot = 1  # тип доступа к боту, 1 - по никнейму
UsersWithAccess = []  # имена тех кто имеет доступ к боту "NotQwicky" "MrMarlain"
UserIdWithAccess = [""]
# пользовательские
NameUser = ""  # имя пользователя
PrintedMessage = 0
MessegerUser = ""  # сообщение от пользователя
S1 = []  # список, где находится все слова из сообщения
S2 = []  # список, где находятся команды, для ответа на сообщения
CommandsForBot = ["/start", "/help", "/me", "/nya", "/notes"]  # команды которые будут в боте
MessegerForBot = ['доброе утро', 'привет', 'что делать', 'что будешь делать', 'как дела', 'кто ты', 'какие команды знаешь', 'какие сообщения знаешь']  # сообщения на которые бот может ответить# бота
BotMood = 3  # настроение бота, 0 - самое плохое игнор, 1 - злиться, 2 - нормальная, 3 - веселая
BotMoodState = 0  # состояние бота, 0 - нормальное, 1 - вспыльчатое, 2 - депрессия, 3 - невыспалась, 4 - без ума, 5 - холоднокровна,
TipMood = 0  # тип общения с человеком, 0 -
CommandMe = "Меня зовут - " + Namebot + "\nМеня создал - @MrMarlain" + "\nЭто бета версия" + "\nДля того чтобы узнать какие команды я умею выполнять, напишите /help" + "\nВерсия бота - 3.0.4 (дата последнего обновления - 17.01.2021)"
SendStickers = 1  # 0 - уже стикер отправлен, 1 - все еще можно отправить стикер
# сам код

filepath = DiskC + r"/Users.txt"
FileX = open(filepath, "rt", encoding='utf8')
TextFileX = FileX.read()
UsersWithAccess = []
UsersWithAccess = TextFileX.rsplit()
FileX.close()

print(time.strftime("%d") + ":" + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime(
                "%S") + "\n \033[33mБот запустился\033[0m")
# если пользователь написал
@bot.message_handler(content_types=['text'])
def Keyboard(message):
    global Password
    global FirstStart
    global Enabled
    global Stage1
    global Stage2
    global Stage3
    global LastMesseger
    global MessegerUser
    global Random
    global index
    global freecommand
    global commands
    global EndSign
    global TipMesseger
    global NumberTask
    global NumberNewTask
    global response
    global response2
    global TimeOut
    global UserGoodNatured
    global UserAggressive
    global UserMood
    global BotCharacter
    global BotMood
    global NameUser
    global S1
    global S2
    global Error
    global seconds
    global minutes
    global hours
    global day
    global seconds2
    global minutes2
    global hours2
    global day2
    global WhileEnabled
    global AccessTypeToBot
    global UsersWithAccess
    global UserIdWithAccess
    global seconds3
    global minutes3
    global hours3
    global day3
    global Time_1
    global Time_2
    global Time1
    global Time2
    global Time3
    global PrintedMessage
    global OnOffBot
    global TxtFileUsers
    global TxtFileSaves
    global DiskC
    global SendStickers
    global CommandMe
    global CommandsForBot
    global MessegerForBot
    global Debug
    global Notes
    global NotesRead
    if OnOffBot == 1:
        # проверка на пользователя
        FileX = open(DiskC + r"/Users.txt", "rt", encoding='utf8')
        TextFileX = FileX.read()
        UsersWithAccess = []
        UsersWithAccess = TextFileX.rsplit()
        FileX.close()
        # проверяем на доступность по UserName
        # если UserName нету в списке UsersWithAccess
        if AccessTypeToBot == 1 and (message.chat.username not in UsersWithAccess):
            bot.send_message(message.chat.id, "Вы не имеете доступ к этому боту")
            try:
                bot.send_message(message.chat.id, "Попросите @MrMarlain добавить вас в список доступа\nСообщите ему свое имя - \"" + message.chat.username + "\"")
            except:
                bot.send_message(message.chat.id, "Поставьте себе UserName и попросите @MrMarlain добавить вас в список доступа\nСообщите ему свой новый UserName ")
                bot.send_message(message.chat.id, str(message.chat))
            # по чату
        # если UserName есть в списке UsersWithAccess
        if AccessTypeToBot == 1 and (message.chat.username in UsersWithAccess):
            # узнаем что написал пользователь
            print(time.strftime("%d") + "д:" + time.strftime("%H") + "ч:" + time.strftime("%M") + "мин:" + time.strftime(
                "%S") + "сек\n " + str(message.chat.username) + " написал \"" + '\033[33m' + message.text.lower() + '\033[0m' + "\"")
            while WhileEnabled == 1:
                try:
                    FileX = open(DiskC + r"/FilesUsers/" + message.chat.username + "/Notes.txt", "rt", encoding='utf8')
                    TextFileX = FileX.read()
                    Notes = ""
                    Notes = str(TextFileX)
                    FileX.close()
                    if Debug == "1":
                        print("-список прочитан успешно")
                    break
                except:
                    
                    FileX = open(DiskC + r"/FilesUsers/" + message.chat.username + '/Notes.txt', 'w+', encoding='utf8')
                    FileX.close()
                    if Debug == "1":
                        bot.send_message(message.chat.id, 'Заметки успешно были созданы')
                        print("-список создан успешно")
            # команды
            if message.text.lower() == "/start":
                if Enabled == 0:
                    Enabled = 1
                    bot.send_message(message.chat.id, "бот включен")
                elif Enabled == 1:
                    bot.send_message(message.chat.id, "бот уже включен")
            elif message.text.lower() and Enabled == 0:
                Error = 0
                bot.send_message(message.chat.id, "включити бота командой /start")
            if message.text.lower() == "/help" and Enabled == 1:
                i = ', '.join(CommandsForBot)
                i2 = ', '.join(MessegerForBot)
                bot.send_message(message.chat.id, "В этом боте есть комманды - \n" +
                                 i + '\n' +
                                 "А так же он может ответить тебе на сообщения - \n" +
                                 i2)
            if message.text.lower() == "/me" and Enabled == 1:
                bot.send_message(message.chat.id, CommandMe)
            if message.text.lower() == "/nya" and Enabled == 1:
                AudioNya = open("C:/TelegramBot/FilesForBot/AudioMesseger/nya.mp3", "rb")
                bot.send_voice(message.chat.id, AudioNya)
                AudioNya.close()
            if message.text.lower() == "/notes" and Enabled == 1:
                FileX = open(DiskC + r"/FilesUsers/" + message.chat.username + '/Notes.txt', "rt", encoding='utf8')
                TextFileX = FileX.read()
                Notes = ""
                Notes = str(TextFileX)
                FileX.close()
                if len(Notes) == 0:
                    print("в заметках пусто")
                    bot.send_message(message.chat.id, 'В заметках пусто')
                else:
                    bot.send_message(message.chat.id, Notes)
            elif message.text.lower() == "/notes удалить" and Enabled == 1:
                try:
                    os.remove(DiskC + r"FilesUsers/" + message.chat.username + '/Notes.txt')
                    bot.send_message(message.chat.id, "Заметки удалены")
                    Error = "-1"
                except:
                    bot.send_message(message.chat.id, "Заметки уже удалены")
                    Error = "-1"
            # обработка сообщений
            if message.text.lower() and Enabled == 1 and message.text.lower() not in CommandsForBot:
                MessegerUser = message.text.lower()
                MessegerUser = re.sub("[.|,|?|!|:|;|%|@|/|#|'|\"|(|)|=|_|&|*|+|~|^|<|>|{|}|]", "", MessegerUser)
                MessegerUser = MessegerUser.lower() + " 1оаф3епф" + " 1оаф3епф"
                S1 = MessegerUser.rsplit()
                # проверяем чтобы сообщенияе не содержало больше 15 слов и не больше 255 символов
                if len(S1) < 18 and len(MessegerUser) <= 257:
                    # ищем, добавляем команды из S1 в S2
                    try:
                        # узнаем
                        if "поиск" in S1:
                            if S1.index("поиск") == 0:
                                TipMesseger = 2
                        if "открой" in S1:
                            if S1.index("открой") == 0:
                                TipMesseger = 3
                        if "notes" in S1:
                            if S1.index("notes") == 0:
                                    TipMesseger = 4
                        # просто добавляем слова
                        if "чд" in S1:
                            S2.append("что делаешь")
                        if "команды" in S1:
                            S2.append("команды")
                        if "привет" in S1 or "ку" in S1 or "хай" in S1 or "здоров" in S1 or "qq" in S1 or "здарова" in S1 or "приветик" in S1 or "приветики" in S1:
                            S2.append("привет")
                        if "пк" in S1:
                            S2.append("пк")
                        if "пока" in S1:
                            S2.append("пока")
                        # соединяем слова
                        if "на" in S1:
                            index = S1.index('на')
                            S2.append(S1[index] + " " + S1[index + 1] + " " + S1[index + 2] + " " + S1[index + 3])
                        if "твое" in S1:
                            index = S1.index('твое')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "чд" in S1:
                            index = S1.index('чд')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "давай" in S1:
                            index = S1.index('давай')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "где" in S1:
                            index = S1.index('где')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "где" in S1:
                            index = S1.index('где')
                            S2.append(S1[index] + " " + S1[index + 1] + " " + S1[index + 2])
                        if "какие" in S1:
                            index = S1.index('какие')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "какие" in S1:
                            index = S1.index('какие')
                            S2.append(S1[index] + " " + S1[index + 1] + " " + S1[index + 2])
                        if "ты" in S1:
                            index = S1.index('ты')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "как" in S1:
                            index = S1.index('как')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "как" in S1:
                            index = S1.index('как')
                            S2.append(S1[index] + " " + S1[index + 1] + " " + S1[index + 2])
                        if "как" in S1:
                            index = S1.index('как')
                            S2.append(S1[index] + " " + S1[index + 1] + " " + S1[index + 2] + " " + S1[index + 3])
                        if "кто" in S1:
                            index = S1.index('кто')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "чем" in S1:
                            index = S1.index('чем')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "что" in S1:
                            index = S1.index('что')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "что" in S1:
                            index = S1.index('что')
                            S2.append(S1[index] + " " + S1[index + 1] + " " + S1[index + 2])
                        if "че" in S1:
                            index = S1.index('че')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "включи" in S1 or "вкл" in S1:
                            index = S1.index('включи')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "выключи" in S1 or "выкл" in S1 or "закрой" in S1:
                            index = S1.index('выключи')
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "спокойной" in S1:
                            index = S1.index("спокойной")
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "приятной" in S1:
                            index = S1.index("приятной")
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "приятных" in S1:
                            index = S1.index("приятных")
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "доброе" in S1:
                            index = S1.index("доброе")
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "доброй" in S1:
                            index = S1.index("доброй")
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "утро" in S1:
                            index = S1.index("утро")
                            S2.append(S1[index] + " " + S1[index + 1])
                        if "чем" in S1:
                            index = S1.index('чем')
                            S2.append(S1[index] + " " + S1[index + 1] + " " + S1[index + 2])
                    # капец коду 1 (не распознал комманду)
                    except:
                        print('\033[31mкапец коду 1 (не распознал комманду)\033[0m' + '\n')
                        Error = 1
                    # добавляем в "commands" команды из S2
                    try:
                        if TipMesseger == 0 or TipMesseger == 1:
                            # приветствие
                            if ("доброе утро" in S2 or "утро доброе" in S2 or "доброе 1оаф3епф" in S2):
                                if FirstStart != int(-1):
                                    if BotMood == 3:
                                        if NumberTask == 1:
                                            Random = random.randint(1, 3)
                                            if Random == 1:
                                                commands.append("и вам тоже доброе утро")
                                                if SendStickers == 1:
                                                    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt91_HMz3MU_a6vwbPzd15F-UthiTMAAKvPQAC4KOCBymhyixxL3LvHgQ')
                                                    SendStickers = 0
                                            if Random == 2:
                                                commands.append("доброе утро")
                                                if SendStickers == 1:
                                                    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt91_HMz3MU_a6vwbPzd15F-UthiTMAAKvPQAC4KOCBymhyixxL3LvHgQ')
                                                    SendStickers = 0
                                            if Random == 3:
                                                commands.append("утро доброе")
                                                if SendStickers == 1:
                                                    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt91_HMz3MU_a6vwbPzd15F-UthiTMAAKvPQAC4KOCBymhyixxL3LvHgQ')
                                                    SendStickers = 0
                                        if NumberTask == 0:
                                            Random = random.randint(1, 2)
                                            if Random == 1:
                                                commands.append("как то уже поздновато")
                                                if SendStickers == 1:
                                                    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJxq1_KcaXjXQABadOHQj3UsZDRUbo7NQAC7z0AAuCjggeapj0tpd2DUB4E')
                                                    SendStickers = 0
                                            if Random == 2:
                                                commands.append("здравствуйте - здравствуйте")
                                                if SendStickers == 1:
                                                    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJxq1_KcaXjXQABadOHQj3UsZDRUbo7NQAC7z0AAuCjggeapj0tpd2DUB4E')
                                                    SendStickers = 0
                            if ("привет" in S2) and "доброе утро" not in S2:
                                if BotMood == 3:
                                    Random = random.randint(1, 3)
                                    if Random == 1:
                                        commands.append("ку")
                                        if SendStickers == 1:
                                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt9F_HMAZo0vQSNTEMs6y1xXph4ApmAAKqPQAC4KOCB8tspMmwoiOcHgQ')
                                            SendStickers = 0
                                    if Random == 2:
                                        commands.append("приветики")
                                        if SendStickers == 1:
                                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt9F_HMAZo0vQSNTEMs6y1xXph4ApmAAKqPQAC4KOCB8tspMmwoiOcHgQ')
                                            SendStickers = 0
                                    if Random == 3:
                                        commands.append("и вам тоже привет")
                                        if SendStickers == 1:
                                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt9F_HMAZo0vQSNTEMs6y1xXph4ApmAAKqPQAC4KOCB8tspMmwoiOcHgQ')
                                            SendStickers = 0
                            # прощание
                            if ("пока" in S2) and "привет" not in S2 and "доброе утро" not in S2:
                                if BotMood == 3:
                                    Random = random.randint(1, 3)
                                    if Random == 1:
                                        commands.append("и вам пока")
                                        if SendStickers == 1:
                                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt-l_HM7JuaW0Sm83h-Gcfju9ogybKAALJPQAC4KOCB2B3I2U3caRoHgQ')
                                            SendStickers = 0
                                    if Random == 2:
                                        commands.append("вы уже уходите?")
                                        if SendStickers == 1:
                                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt_V_HM9Oa4tNzDp9r1C3Imi9nbj_vAAKuPQAC4KOCB-p8k8NFHUIbHgQ')
                                            SendStickers = 0
                                    if Random == 3:
                                        commands.append("пока - пока")
                                        if SendStickers == 1:
                                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt-l_HM7JuaW0Sm83h-Gcfju9ogybKAALJPQAC4KOCB2B3I2U3caRoHgQ')
                                            SendStickers = 0
                            # вопросы
                            if ("что делаешь" in S2 or "что сейчас делаешь" in S2 or "чем занята" in S2 or "че делаешь" in S2
                                    or "что ты делаешь" in S2 or "чем ты занята" in S2):
                                if BotMood == 3:
                                    if NumberTask == 0:
                                        Random = random.randint(1, 2)
                                        if Random == 1:
                                            commands.append("я сейчас ничем не занята")
                                            if SendStickers == 1:
                                                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJxhF_KaZ7ScKwRZJz3cRRnSDnztiaAAALTPQAC4KOCBx8CDogOMcd_HgQ')
                                                SendStickers = 0
                                        if Random == 2:
                                            commands.append("ничего")
                                            if SendStickers == 1:
                                                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJxhF_KaZ7ScKwRZJz3cRRnSDnztiaAAALTPQAC4KOCBx8CDogOMcd_HgQ')
                                                SendStickers = 0
                                    elif NumberTask == 1:
                                        Random = random.randint(1, 2)
                                        if Random == 1:
                                            commands.append("я сейчас спала")
                                            if SendStickers == 1:
                                                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ_zV_V24ctMccAAUg-RW9JKmIlLhMYKQACxD0AAuCjggesAurmhyWk8B4E')
                                                SendStickers = 0
                                        if Random == 2:
                                            commands.append("я спала")
                                            if SendStickers == 1:
                                                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ_zV_V24ctMccAAUg-RW9JKmIlLhMYKQACxD0AAuCjggesAurmhyWk8B4E')
                                                SendStickers = 0
                                    elif NumberTask == 2:
                                        Random = random.randint(1, 2)
                                        if Random == 1:
                                            commands.append("я выпоолняла запрос")
                                            if SendStickers == 1:
                                                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALGXWAZY0oX7Qr1mPtsA2o7dS--Pr8sAAK_PQAC4KOCB-I53PwAAR0bOR4E')
                                                SendStickers = 0
                                        if Random == 2:
                                            commands.append("я выполняла команду \"поиск\"")
                                            if SendStickers == 1:
                                                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALGYGAZY3v3le-hj0xhVhagldFtmPovAAKqPQAC4KOCB8tspMmwoiOcHgQ')
                                                SendStickers = 0
                            if ("что будешь делать" in S2 or "чд будешь" in S2 or "делать что будешь" in S2 or "что делать будешь" in S2
                                    or "что ты собираешься" in S2):
                                if BotMood == 3:
                                    Random = random.randint(1, 2)
                                    if NumberNewTask == 0:
                                        if Random == 1:
                                            commands.append("незнаю")
                                            if SendStickers == 1:
                                                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJxt1_Kc5y3Kcip5hvEkwAB7sK9zTPj9gACwT0AAuCjggdePfK-o2Tihh4E')
                                                SendStickers = 0
                                        if Random == 2:
                                            commands.append("точно не знаю")
                                            if SendStickers == 1:
                                                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJxt1_Kc5y3Kcip5hvEkwAB7sK9zTPj9gACwT0AAuCjggdePfK-o2Tihh4E')
                                                SendStickers = 0
                            if ("как дела" in S2):
                                if BotMood == 3:
                                    Random = random.randint(1, 3)
                                    if Random == 1:
                                        commands.append("у меня все замечательно")
                                        if SendStickers == 1:
                                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJxh1_KbCUzrHmkls9wMVHTPNNjnsM5AAKrPQAC4KOCB5PKWhfZ4HLjHgQ')
                                            SendStickers = 0
                                    if Random == 2:
                                        commands.append("все прекрастно")
                                        if SendStickers == 1:
                                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJxh1_KbCUzrHmkls9wMVHTPNNjnsM5AAKrPQAC4KOCB5PKWhfZ4HLjHgQ')
                                            SendStickers = 0
                                    if Random == 3:
                                        commands.append("у меня лучше всех")
                                        if SendStickers == 1:
                                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJxh1_KbCUzrHmkls9wMVHTPNNjnsM5AAKrPQAC4KOCB5PKWhfZ4HLjHgQ')
                                            SendStickers = 0
                            if ("кто ты" in S2 or "ты кто" in S2):
                                if BotMood == 3:
                                    commands.append("я - бот помощник, который должен служить ради моих хозяев\nБольше информации - /me")
                                    if SendStickers == 1:
                                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJuA1_HNHuqvY-SdMIeyBUAAXPtFhaLBQAC2j0AAuCjggclRwdAEwABKcoeBA')
                                        SendStickers = 0
                            if ("какие команды знаешь" in S2 or "какие команды отвечаешь" in S2 or "команды" in S2 or "что ты умеешь" in S2):
                                if BotMood == 3:
                                    commands.append("команды которыя я знаю - " + ', '.join(CommandsForBot))
                                    if SendStickers == 1:
                                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ-hl_U1PPFOzkybMWR99Jqbx-NT-LMAAK_PQAC4KOCB-I53PwAAR0bOR4E')
                                        SendStickers = 0
                            if ("какие сообщения знаешь" in S2 or "какие сообщения отвечаешь" in S2 or "на что ты отвечаешь" in S2 or "на какие сообщения ты" in S2):
                                if BotMood == 3:
                                    commands.append("на какие сообщения я отвечаю - " + ', '.join(MessegerForBot))
                                    if SendStickers == 1:
                                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ-hl_U1PPFOzkybMWR99Jqbx-NT-LMAAK_PQAC4KOCB-I53PwAAR0bOR4E')
                                        SendStickers = 0
                            if ("твое имя" in S2 or "как тебя зовут" in S2):
                                if BotMood == 3:
                                    commands.append("меня звать - " + Namebot)
                                    if SendStickers == 1:
                                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ-iV_U2akTaH6-BEh--spS7t5NAz0jAALBPQAC4KOCB1498r6jZOKGHgQ')
                                        SendStickers = 0
                            # вежливые слова

                            # команды в сообщениях

                            # if "выключи пк" in S2 and stage == 0 or "выкл пк" in S2 and stage == 0 or "выключи комьютер" in S2 and stage == 0 or "выкл помьютер" in S2 and stage == 0:
                            # print("вы уверены?")
                            # stage1 = 1

                    # капец коду 2 (не смог добавить команду в список)
                    except:
                        print('\033[31mкапец коду 2 (не смог добавить команду в список)\033[0m' + '\n')
                        Error = 1
                    # выводим текст
                    try:
                        # time.sleep(0.25)
                        response = ', '.join(commands)
                        if Debug == "1":
                            print("-ошибка - " + str(Error))
                            print("-FirstStart - " + str(FirstStart))
                            print("-BotMood - " + str(BotMood))
                            print("-WhileEnabled - " + str(WhileEnabled))
                            print("-Вводимое, очищеное сообщение - " + "\"" + str(MessegerUser) + "\"")
                            print("-список 1 - " + str(S1))
                            print("-список 2 - " + str(S2))
                            print("-commands - " + str(commands))
                            print("-response - " + str(response))
                            print("-TipMesseger - " + str(TipMesseger))
                            print("-EndSign - " + str(EndSign))
                            print("-NumberTask - " + str(NumberTask))
                            print("-NumberNewTask - " + str(NumberNewTask))
                            print("-ответ - \"" + str(response) + "\"")
                        if Error == 0:
                            try:
                                if len(S2) != 0 and EndSign == 0:
                                    if BotMood == 3:
                                        EndSign = 2
                                    if BotMood == 2:
                                        EndSign = 1
                                    if BotMood == 1:
                                        EndSign = 1
                                    if BotMood == 0:
                                        EndSign = 4
                                if EndSign == 1:
                                    response = response + "."
                                elif EndSign == 2:
                                    response = response + "!"
                                elif EndSign == 3:
                                    response = response + "?"
                                elif EndSign == 4:
                                    response = response + "..."
                            except:
                                print('\033[31mкапец коду4(не удалось поставить знак)\033[0m' + '\n')
                                Error = 1
                            # просто отвечаем
                            if TipMesseger == 0 and len(commands) != 0 or TipMesseger == 1 and len(commands) != 0:
                                print('\033[33m' + ' r - ' + str(response) + '\033[0m')
                                #if len(commands) > 0:
                                    #for item in commands:
                                        #time.sleep(0.3)
                                        #bot.send_message(message.chat.id, item)
                                #else:
                                    #bot.send_message(message.chat.id, str(response.capitalize()))
                                for item in commands:
                                    time.sleep(0.20)
                                    bot.send_message(message.chat.id, item)
                            # ищем в инете
                            if TipMesseger == 2:
                                NumberTask = 2
                                S1.remove("поиск")
                                S1.remove("1оаф3епф")
                                S1.remove("1оаф3епф")
                                response2 = ' '.join(S1)
                                if len(response2) == 0:
                                    if BotMood == 3:
                                        Random = random.randint(1, 3)
                                        if Random == 1:
                                            bot.send_message(message.chat.id, "Вы забыли сказать что искать")
                                        elif Random == 2:
                                            bot.send_message(message.chat.id, "Вы не ввели запрос")
                                        elif Random == 3:
                                            bot.send_message(message.chat.id, "Скажите что вам нужно найти")
                                else:
                                    bot.send_message(message.chat.id, "Ищу \"" + str(response2.capitalize()) + "\"")
                                    if response2 == "vk" or response2 == "вк" or response2 == "vkontakte" or response2 == "вконтакте":
                                        bot.send_message(message.chat.id, "https://vk.com")
                                    elif response2 == "ютуб" or response2 == "youtube":
                                        bot.send_message(message.chat.id, "https://www.youtube.com/?gl=RU&hl=ru")
                                    elif response2 == "одноклассники" or response2 == "ok" or response2 == "ок":
                                        bot.send_message(message.chat.id, "https://ok.ru")
                                    else:
                                        bot.send_message(message.chat.id, "https://yandex.ru/search/?text=" + '%20'.join(S1) + "&lr=11279&clid=2358536")
                                        print(" r - ищем \"" + str(response2) + "\"")
                            # запускаем приложения
                            elif TipMesseger == 3:
                                NumberTask = 3
                                S1.remove("открой")
                                S1.remove("1оаф3епф")
                                S1.remove("1оаф3епф")
                                response2 = ' '.join(S1)
                                if len(response2) == 0:
                                    if BotMood == 3:
                                        Random = random.randint(1, 3)
                                        if Random == 1:
                                            bot.send_message(message.chat.id, "Вы забыли сказать что нужно открыть")
                                        elif Random == 2:
                                            bot.send_message(message.chat.id, "Вы не ввели то что вам нужно откыть")
                                        elif Random == 3:
                                            bot.send_message(message.chat.id, "Скажите что вам нужно открыть")
                                elif response2 == "кс":
                                    bot.send_message(message.chat.id, "открываю " + response2)

                                else:
                                    bot.send_message(message.chat.id, "Я не смогла запустить \"" + str(response2.capitalize()) + "\"")
                                    print(" r - Я не смогла запустить \"" + str(response2) + "\"")
                            # запись в заметки
                            elif TipMesseger == 4:
                                NumberTask = 4
                                S1.remove("notes")
                                S1.remove("1оаф3епф")
                                S1.remove("1оаф3епф")
                                response2 = ' '.join(S1)
                                MessegerUser = message.text.lower()
                                S1 = MessegerUser.rsplit()
                                try:
                                    S1.remove("/notes")
                                except:
                                    S1.remove("notes")
                                FileX = open(DiskC +r"/FilesUsers/" + message.chat.username + '/Notes.txt', "rt", encoding='utf8')
                                NotesRead = FileX.read()
                                FileX.close()
                                bot.send_message(message.chat.id, "\"" + str(' '.join(S1)) + "\" - в заметки было успешно добавлено")
                                FileX = open(DiskC + r'/FilesUsers/' + message.chat.username + '/Notes.txt', 'w', encoding='utf8')
                                FileX.write(str(NotesRead) + str(' '.join(S1)) + "\n")
                        # обнуляем переменные
                        S1 = []
                        S2 = []
                        commands = []
                        TipMesseger = 0
                        response = ""
                        response2 = ""
                        EndSign = 0
                        SendStickers = 1
                        #NumberTask = 0
                    # капец коду 3 (не смог вывести ответ)
                    except:
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJt61_HLJwsqZRTe-YJmZgr1j37w9pKAALTPQAC4KOCBx8CDogOMcd_HgQ')
                        bot.send_message(message.chat.id, "Я тя не поняла")
                        print('\033[31mкапец коду 3 (не смог вывести ответ)\033[0m')
                        Error = 1
                    Error = 0
                # если в сообщении много слов
                elif len(S1) >= 18:
                    bot.send_message(message.chat.id, "А~а~а~а, слишком много слов \n>-<")
                # если в сообщении много букв
                elif len(MessegerUser) > 257:
                    bot.send_message(message.chat.id, "А~а~а~а, слишком много букв \n>-<")
                # если какая то ошибка ,например ты >:(
                else:
                    print("капец коду5 (что то с распознованием ответа)")
    # если пользователь впервые запустил бота
    if FirstStart != 0:
        FirstStart = FirstStart - 1
# если пользователь отправил документ/фото
@bot.message_handler(content_types=['document', 'photo'])
def handle_docs_photo(message):
    global WhileEnabled
    global AccessTypeToBot
    global UsersWithAccess
    global OnOffBot
    global Debug
    global Random
    # проверка на пользователя
    FileX = open(DiskC + r"\Users.txt", "rt", encoding='utf8')
    TextFileX = FileX.read()
    UsersWithAccess = []
    UsersWithAccess = TextFileX.rsplit()
    FileX.close()
    Error = 0
    # проверяем, спит бот или нет
    if WhileEnabled == 1:
        Time_2 = str(time.strftime("%H")) + str(time.strftime("%M") + str(time.strftime("%S")))
        if Time_2 >= Time3 and Time_2 <= Time2:
            OnOffBot = 1
            # Debug
            FileX = open(DiskC + r"\Bot\Variables.txt", "rt", encoding='utf8')
            TextFileX = FileX.readlines()
            Debug = TextFileX[0]
            FileX.close()
            Debug = re.sub(" |\n", "", Debug)

            if Debug == "1":
                print("\033[42m\033[30mСейчас бот вкл\033[0m")
        else:
            bot.send_message(message.chat.id, "*сплю*")
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAJxe1_KZ6KYEiJ6rps4TQf3DAzh-TXyAAKwPQAC4KOCB9Hlip3uzqVUHgQ")
            OnOffBot = 0
            FirstStart = 2
            if Debug == "1":
                print(message.chat.username + "(отправка файла): \033[41m\033[30mСейчас бот выкл\033[0m")
    # сохранение файлов
    if OnOffBot == 1:
        # проверка на пользователя
        if AccessTypeToBot == 1 and (message.chat.username not in UsersWithAccess):
            bot.send_message(message.chat.id, "Вы не имеете доступ к этому боту")
            try:
                bot.send_message(message.chat.id, "Попросите @MrMarlain добавить вас в список доступа\nСообщите ему свое имя - \"" + message.chat.username + "\"")
            except:
                bot.send_message(message.chat.id, "Поставьте себе UserName и попросите @MrMarlain добавить вас в список доступа\nСообщите ему свой новый UserName")
            if Debug == "1":
                print(message.chat.username + " отправил боту файл")
                print(time.strftime("%d") + ":" + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime(
                    "%S") + "\n " + str(message.chat.username) + " отправил боту файл")
        # если все ок
        else:
            # создание всех нужных папок
            if WhileEnabled == 1:
                if not os.path.isdir(DiskC + r"/FilesUsers/" + message.chat.username + "/Document"):
                    os.makedirs(DiskC + r"/FilesUsers/" + message.chat.username + "/Document")
                    print("папка FilesUsers/Document создана успешно")
                if not os.path.isdir(DiskC + r"/FilesUsers/" + message.chat.username + "/Photo"):
                    os.makedirs(DiskC + r"/FilesUsers/" + message.chat.username + "/Photo")
                    print("папка FilesUsers/Photo создана успешно")
            # сохранение фалов
            if AccessTypeToBot == 1 and message.chat.username in UsersWithAccess:
                try:
                    file_info = bot.get_file(message.document.file_id)
                    downloaded_file = bot.download_file(file_info.file_path)

                    src = DiskC + r"/FilesUsers/" + str(message.chat.username) + "/Document/" + message.document.file_name
                    with open(src, 'wb') as new_file:
                        new_file.write(downloaded_file)
                    #if BotMood == 3:
                        #Random = random.randint(1, 2)
                        #if Random == 1:
                            #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ_vl_V2z6GoYvOV4lhgSiaUGj5J0D0AALlPQAC4KOCB900OeGYB8JAHgQ')
                        #if Random == 2:
                            #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJ_6F_V3EoVB8iI0NremSQd6Jd2kwjZAALaPQAC4KOCByVHB0ATAAEpyh4E')
                    bot.reply_to(message, "документ - \n" + "\"" + message.document.file_name + "\"" + "\nуспешно сохранен")
                    print(time.strftime("%d") + ":" + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime(
                        "%S") + "\n " + str(message.chat.username) + " документ сохранен")
                except:
                    Error = 1
            if AccessTypeToBot == 1 and message.chat.username in UsersWithAccess:
                try:
                    Random = random.randint(100, 999)
                    file_info = bot.get_file(message.photo[0].file_id)
                    downloaded_file = bot.download_file(file_info.file_path)

                    src = DiskC + r"/FilesUsers/" + str(message.chat.username) + "/Photo/" + " Y-" + time.strftime("%Y") + " m-" + time.strftime("%m") + \
                          " d-" + time.strftime("%d") + " H-" + time.strftime("%H") + " M-" + time.strftime("%M") + " S-" + time.strftime("%S") + \
                          " - " + Random + ".png"
                    with open(src, 'wb') as new_file:
                        new_file.write(downloaded_file)
                    bot.reply_to(message, "фото - \n" + "\"" + message.photo[0].file_id + "\"" + "\nуспешно сохранено")
                    print(time.strftime("%d") + ":" + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime(
                        "%S") + "\n " + str(message.chat.username) + " фото сохранено")
                except:
                    #print("ошибка в сохранении")
                    Error = 1
                # по чату
# не даем боту выключаться
while True:
    bot.polling(none_stop=True)
    input()
