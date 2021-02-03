import re
import random

ResponseType = 0

b = input()
if b == "":
    b = "а у тебя как дела?"  # вводим уже заготовленный текст

c = ['']  # пустой список
c2 = []  # пустой список
# очищаем текст
b = re.sub("[.|,|?|!|:|;|%|@|/|s|#|'|\"|(|)|=|_|&|*|+|~|^|<|>|{|}|]", "", b)
# добавляем еще один объект чтобы пофиксить баг
b = b.lower() + " 1оаф3епф"
# добавляем в список "с" все слова из очищенного текста
c = b.rsplit()
# нужна фигня
index = 0
# сколько свободны команд осталось
freecommand = 5
# ответ на команду 1
command1 = ""
# ответ на команду 2
command2 = ""
# ответ на команду 3
command3 = ""
# ответ на команду 4
command4 = ""
# ответ на команду 5
command5 = ""
# тип вопроса 0 - нету сообщения, 1 - сообщение которое начинается с "а", 2 - сообщение которое нужно загуглить
TipMesseger = 0
# Чем занят бот, 0 - нечем
NumberTask = 0
# то чем бот будет делать после
NumberNewTask = 0
# ответ который состоит из всех команд
response = ""
# сколько прошло времени с последнего сообщения
TimeOut = 0
# если прошло 9 часов с последего сообщения то ставиться 1 ( бот должен поприветствовать ), иначе 0 ( бот уже поприветствовал )
FirstMesseger = 0
#
stage = 0

# добавляем в список с2 команды из текста
try:
    # узнаем
    if "найди" in c and c.index("найди") == 0:
        TipMesseger = 2
    # просто добавляем слова
    if "чд" in c:
        c2.append("как дела")
    else:
        TipMesseger = 1
    if "привет" in c or "ку" in c or "хай" in c or "здоров" in c or "qq" in c or "здарова" in c:
        c2.append("привет")
    if "пк" in c:
        c2.append("пк")
    if "пока" in c:
        c2.append("пока")
    # соединяем слова
    if "где" in c:
        index = c.index('где')
        c2.append(c[index] + " " + c[index + 1])
    if "где" in c:
        index = c.index('где')
        c2.append(c[index] + " " + c[index + 1] + " " + c[index + 2])
    if "ты" in c:
        index = c.index('ты')
        c2.append(c[index] + " " + c[index + 1])
    if "как" in c:
        index = c.index('как')
        c2.append(c[index] + " " + c[index + 1])
    if "как" in c:
        index = c.index('как')
        c2.append(c[index] + " " + c[index + 1] + " " + c[index + 2])
    if "как" in c:
        index = c.index('как')
        c2.append(c[index] + " " + c[index + 1] + " " + c[index + 2] + " " + c[index + 3])
    if "кто" in c:
        index = c.index('кто')
        c2.append(c[index] + " " + c[index + 1])
    if "чем" in c:
        index = c.index('чем')
        c2.append(c[index] + " " + c[index + 1])
    if "что" in c:
        index = c.index('что')
        c2.append(c[index] + " " + c[index + 1])
    if "что" in c:
        index = c.index('что')
        c2.append(c[index] + " " + c[index + 1] + " " + c[index + 2])
    if "че" in c:
        index = c.index('че')
        c2.append(c[index] + " " + c[index + 1])
    if "включи" in c or "вкл" in c or "запусти" in c:
        index = c.index('включи')
        c2.append(c[index] + " " + c[index + 1])
    if "выключи" in c or "выкл" in c or "закрой" in c:
        index = c.index('выключи')
        c2.append(c[index] + " " + c[index + 1])
    if "спокойной" in c:
        index = c.index("спокойной")
        c2.append(c[index] + " " + c[index + 1])
    if "приятной" in c:
        index = c.index("приятной")
        c2.append(c[index] + " " + c[index + 1])
    if "приятных" in c:
        index = c.index("приятных")
        c2.append(c[index] + " " + c[index + 1])
    if "доброе" in c:
        index = c.index("доброе")
        c2.append(c[index] + " " + c[index + 1])
    if "доброй" in c:
        index = c.index("доброй")
        c2.append(c[index] + " " + c[index + 1])
    if "утро" in c:
        index = c.index("утро")
        c2.append(c[index] + " " + c[index + 1])
except:
    print("капец коду1")
# добавляем в команды, команды которые нашли в с2
try:
    if "доброе утро" in c2:
        if freecommand == 5:
            command1 = "доброе утро"
        elif freecommand == 4:
            command2 = "доброе утро"
        elif freecommand == 3:
            command3 = "доброе утро"
        elif freecommand == 2:
            command4 = "доброе утро"
        elif freecommand == 1:
            command5 = "доброе утро"
        freecommand = freecommand - 1
    if "привет" in c2 and "доброе утро" not in c2 and "пока" not in c2:
        if freecommand == 5:
            command1 = "привет"
        elif freecommand == 4:
            command2 = "привет"
        elif freecommand == 3:
            command3 = "привет"
        elif freecommand == 2:
            command4 = "привет"
        elif freecommand == 1:
            command5 = "привет"
        freecommand = freecommand - 1
    if "привет" in c2 and "пока" in c2:
        if freecommand == 5:
            command1 = "пока"
        elif freecommand == 4:
            command2 = "пока"
        elif freecommand == 3:
            command3 = "пока"
        elif freecommand == 2:
            command4 = "пока"
        elif freecommand == 1:
            command5 = "пока"
        freecommand = freecommand - 1
    if "пока" in c2 and "привет" not in c2:
        if freecommand == 5:
            command1 = "пока"
        elif freecommand == 4:
            command2 = "пока"
        elif freecommand == 3:
            command3 = "пока"
        elif freecommand == 2:
            command4 = "пока"
        elif freecommand == 1:
            command5 = "пока"
        freecommand = freecommand - 1
    if "как дела" in c2 or "как жизнь" in c2 or "как спалось" in c2 or "как у тебя дела" in c2:
        if freecommand == 5:
            command1 = "нормально"
        elif freecommand == 4:
            command2 = "нормально"
        elif freecommand == 3:
            command3 = "нормально"
        elif freecommand == 2:
            command4 = "нормально"
        elif freecommand == 1:
            command5 = "нормально"
        freecommand = freecommand - 1
    if "как настроение" in c2:
        if freecommand == 5:
            command1 = "нормальное"
        elif freecommand == 4:
            command2 = "нормальное"
        elif freecommand == 3:
            command3 = "нормальное"
        elif freecommand == 2:
            command4 = "нормальное"
        elif freecommand == 1:
            command5 = "нормальное"
        freecommand = freecommand - 1
    if "где ты" in c2 or "ты где" in c2 or "ты сейчас где" in c2:
        if freecommand == 5:
            command1 = "я тута"
        elif freecommand == 4:
            command2 = "я тута"
        elif freecommand == 3:
            command3 = "я тута"
        elif freecommand == 2:
            command4 = "я тута"
        elif freecommand == 1:
            command5 = "я тута"
        freecommand = freecommand - 1
    if "че делаешь" in c2 or "что делаешь" in c2 or "чд" in c2:
        if NumberTask == 0 and freecommand == 5:
            command1 = "ничего"
        elif NumberTask == 0 and freecommand == 4:
            command2 = "ничего"
        elif NumberTask == 0 and freecommand == 3:
            command3 = "ничего"
        elif NumberTask == 0 and freecommand == 2:
            command4 = "ничего"
        elif NumberTask == 0 and freecommand == 1:
            command5 = "ничего"
        freecommand = freecommand - 1
    if "чем занята" in c2:
        if NumberTask == 0 and freecommand == 5:
            command1 = "ничем"
        elif NumberTask == 0 and freecommand == 4:
            command2 = "ничем"
        elif NumberTask == 0 and freecommand == 3:
            command3 = "ничем"
        elif NumberTask == 0 and freecommand == 2:
            command4 = "ничем"
        elif NumberTask == 0 and freecommand == 1:
            command5 = "ничем"
        freecommand = freecommand - 1
    if "что будешь делать" in c2 or "че будешь делать" in c2 or "чем займешься" in c2:
        if NumberNewTask == 0 and freecommand == 5:
            command1 = "незнаю"
        elif NumberNewTask == 0 and freecommand == 4:
            command2 = "незнаю"
        elif NumberNewTask == 0 and freecommand == 3:
            command3 = "незнаю"
        elif NumberNewTask == 0 and freecommand == 2:
            command4 = "незнаю"
        elif NumberNewTask == 0 and freecommand == 1:
            command5 = "незнаю"
        freecommand = freecommand - 1
    if "спокойной ночи" in c2 or "приятных снов" in c2 or "приятных сноведений" in c2 or "доброй ночи" in c2:
        if freecommand == 5:
            command1 = "и вам, спокойной ночи"
        elif freecommand == 4:
            command2 = "и вам, спокойной ночи"
        elif freecommand == 3:
            command3 = "и вам, спокойной ночи"
        elif freecommand == 2:
            command4 = "и вам, спокойной ночи"
        elif freecommand == 1:
            command5 = "и вам, спокойной ночи"
        freecommand = freecommand - 1
    if "выключи пк" in c2 and stage == 0 or "выкл пк" in c2 and stage == 0 or "выключи комьютер" in c2 and stage == 0 or "выкл помьютер" in c2 and stage == 0:
        print("вы уверены?")
        stage = 1
except:
    print("капец коду2")
# расставляем запятые и точки
try:
    if command1 != "" and command2 != "":
        command1 = command1 + ", "
    elif command1 != "" and command2 == "":
        command1 = command1 + ". "

    if command2 != "" and command3 != "":
        command2 = command2 + ", "
    elif command2 != "" and command3 == "":
        command2 = command2 + ". "

    if command3 != "" and command4 != "":
        command3 = command3 + ", "
    elif command3 != "" and command4 == "":
        command3 = command3 + ". "

    if command4 != "" and command5 != "":
        command4 = command4 + ", "
    elif command4 != "" and command5 == "":
        command4 = command4 + ". "

    if command5 != "":
        command5 = command5 + ". "
except:
    print("капец коду3")

# вывод всего
print("Вводимое, очищеное сообщение - " + "\"" + str(b) + "\"")
print("список 1 - " + str(c))
print("список 2 - " + str(c2))
print("c1 - " + command1)
print("c2 - " + command2)
print("c3 - " + command3)
print("c4 - " + command4)
print("c5 - " + command5)
print("сколько свободных команд осталось - " + str(freecommand))
print("TipMesseger - " + str(TipMesseger))
print("NumberTask - " + str(NumberTask))
print("NumberNewTask - " + str(NumberNewTask))
if TipMesseger == 0 or TipMesseger == 1:
    # складываем весь ответ
    response = response + command1 + command2 + command3 + command4 + command5
    print("\n r - " + response)
elif TipMesseger == 2:
    response2 = " "
    c.remove("найди")
    c.remove("1оаф3епф")
    response2 = response2.join(c)
    print("\n r - ищем \"" + response2 + "\"")