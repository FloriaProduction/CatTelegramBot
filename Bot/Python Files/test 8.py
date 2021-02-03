import re
import random

Random = 0

Text = ""  # вводимое сообщение
S1 = []  # разбор сообщения на слова
S2 = []  # команды на которые нужно ответить

NumberTask = 0  # Чем занят бот, 0 - ничем, 1 - спала,
NumberNewTask = []  # то чем бот будет делать после

BotMood = 0  # настроение бота, 0 - высокое, 1 - среднее, 2 - грустное
BotEmotion = 0  # эмоция бота, 0 - обычное, 1 - застенчивое,

Conclusion = []  # сообщение, собираемое из слов
DoneMessege = ""  # вывод собраного сообщения

while True:
    Text = input()

    print("Text (вводимое) - " + Text)
    Text = re.sub("[.|,|?|!|:|;|%|@|/|s|#|'|\"|(|)|=|_|&|*|+|~|^|<|>|{|}|]", "", Text)  # очищаем сообщение от знаков
    print("Text (очищенное) - " + Text)
    Text = Text.lower()  # ставим текст в нижний ригистр
    S1 = Text.rsplit()  # добавляем по словно текст в список
    print("S1 - " + str(S1))

    if "привет" in S1 or "ку" in S1:
        S2.append("привет")

    print("S2 - " + str(S2))

    if "привет" in S2:
        Random = random.randint(1, 3)
        if BotEmotion == 0:
            if BotMood == 0:
                if Random == 1:
                    Conclusion.append(" приветик")
                elif Random == 2:
                    Conclusion.append(" приветики")
                elif Random == 3:
                    Conclusion.append(" кукусики")
            elif BotMood == 2:
                if Random == 1:
                    Conclusion.append(" привет")
                elif Random == 2:
                    Conclusion.append(" ку")
                elif Random == 3:
                    Conclusion.append(" здравствуй")
            elif BotMood == 3:
                if Random == 1:
                    Conclusion.append(" ага")
                elif Random == 2:
                    Conclusion.append(" те тож")
                elif Random == 3:
                    Conclusion.append(" угу")

    print("Conclusion - " + str(Conclusion))
    DoneMessege = ''.join(Conclusion)  # собираем ответ
    if len(S1) == 0:  # если ответ оказался пустым то
        print("DoneMessege - \"\033[33mсообщение пустое\033[0m\"")  # выводим ответ о том что сообщение было пустым
    elif len(S1) > 0 and DoneMessege == "":
        print("DoneMessege - \"\033[33mнепонятное сообщение\033[0m\"")
    else:  # если ответ не оказался пустым то
        print("DoneMessege - \033[33m" + DoneMessege + "\033[0m")  # выводим готовое сообщение
    DoneMessege = []
    Conclusion = []
    S2 = []
    S1 = []



