import speech_recognition as sp
import random
import datetime
import time
import re
import os

mic = sp.Microphone(device_index=1)

a = ""  # переменная в которой текст который говорит ползователь
c = []  # список в котором текст который говорит пользователь
stage = 0  # узнаем узнал ли гугл текс
stage2 = 0  # служит что то типо включением циклов
stage3 = 0  # нужная переменная которая сильно помогает
LastMessege = 0  # узнаем что последний раз сказал пользователь
Random = 1  # рандомим число
While = 1  # номер рабочего списка
debug = 0  # вкл/выкл отладку
Whiles = 0  # сколько дебагов написалось

S0 = ["1"]
S1 = ["привет", "ку", "приветики", "хай", "хаю-хай", "хаю хай"]
S2 = ["как дела?", "как дела", "как настроение", "как жизнь?", "как жизнь", "как настроение?", "как твои дела?", "как твои дела"]
S3 = ["время", "сколько времени?", "сколько времени", "сколько время", "сколько времени?"]
S4 = ["сброс", "сбросить"]
S5 = [""]
S6 = [""]
S7 = [""]
S8 = [""]
S9 = ["лучше всех", "все пучком", "афигенно", "прекрастно", "как в сказке", "превосходно", "классно", "супер", "просто супер"]
S10 = ["нормально", "хорошо", "все ок", "", "", ""]
S11 = [""]
S12 = [""]
S13 = [""]
S14 = ["консоль", "cmd", "открыть консоль", "запусти консоль", "включи консоль"]
S15 = ["/start", "запуск", "старт", "запустись"]
S16 = ["вкл спящий режим", "включить спящий режим", "спящий режим", "включи спящий режим", "пк сон", "пк-сон"]
S17 = ["блокнот", "открой блокнот"]
S18 = ["имя"]
S19 = ["пока", "досвидания", "пока-пока"]
#S20 = ["вкл/выкл отладку"]
S21 = ["выключись", "выкл", "выкл бота", "/stop", "стоп", "спи", "усни", "сон", "бот сон", "бот-сон"]
S22 = ["рестарт", "/restart", "перезагрузись", "перезапуск"]
S23 = ["так же", "аналогично", "тоже", "тоже самое"]
S24 = ["отмена", "нет", "отменить", "прекрати", "остановись", "выключись"]
S25 = ["да", "уверен", "выполни", "окей", "оке"]
S27 = ["что делаешь?", "что делаешь"]

print("программа запустилась")
while stage2 != -1 and While == 1:
    if debug == 1:
        Whiles = Whiles + 1
    if Whiles == 30 and debug == 1:
        os.system("cls")
    try:
        r = sp.Recognizer()
        with mic as source:
            audio = r.listen(source)
        a = r.recognize_google(audio, language="ru-RU")
        #print("вы сказали \"" + a + "\"")
        stage = 1
        stage2 = 0
        a = re.sub("[.|,|?|!|:|;|%|@|/|s|#|'|\"|(|)|=|_|&|*|+|~|^|<|>|{|}]", "", a)
        c = a.rsplit()
        #print(a)
        #print(c)
    except sp.UnknownValueError:
        #print("вы промолчали")
        stage = 2
        stage2 = 0
    except sp.RequestError:
        stage = 3
        #print("гугл не захотел понимать")
        stage2 = 0
    if "окей дом" in a.lower() and stage == 1 and a != "":
        While = 2
        stage2 = 0
        Random = random.randint(1, 3)
        if Random == 1:
            print("Я вас слушаю")
        elif Random == 2:
            print("Да-Да")
        elif Random == 3:
            print("Вы меня звали?")
        else:
            print("ошибка")
    elif "окей комната" in a.lower() and stage == 1 and a != "":
        While = 2
        stage2 = 0
        Random = random.randint(1, 3)
        if Random == 1:
            print("Я вас слушаю")
        elif Random == 2:
            print("Да-Да")
        elif Random == 3:
            print("Вы меня звали?")
        else:
            print("ошибка")
    elif "слушай дом" in a.lower() and stage == 1 and a != "":
        While = 2
        stage2 = 0
        Random = random.randint(1, 3)
        if Random == 1:
            print("Я вас слушаю")
        elif Random == 2:
            print("Да-Да")
        elif Random == 3:
            print("Вы меня звали?")
        else:
            print("ошибка")
    elif "слушай комната" in a.lower() and stage == 1 and a != "":
        While = 2
        stage2 = 0
        Random = random.randint(1, 3)
        if Random == 1:
            print("Я вас слушаю")
        elif Random == 2:
            print("Да-Да")
        elif Random == 3:
            print("Вы меня звали?")
        else:
            print("ошибка")
    #elif "бот" in c and stage == 1 and a != "":
        #While = 2
        #stage2 = 0
        #print("я вас слушаю")
    #if debug == 1:
        #print("a - \"" + a + "\"; c - " + str(c) + "; stage - " + str(stage) + "; stage2 - " + str(stage2) + "; LastMessege - " + str(LastMessege) + "; Random - " + str(Random) + "; debug - " + str(debug) + "; While - " + str(While) + "; Whiles - " + str(Whiles))

    # второй, исполняющий цикл
    while stage2 != -1 and While == 2:
        if debug == 1:
            Whiles = Whiles + 1
        if Whiles == 30 and debug == 1:
            os.system("cls")
        # print("слушаю")
        try:
            r = sp.Recognizer()
            with mic as source:
                audio = r.listen(source)
            a = r.recognize_google(audio, language="ru-RU")
            # print("вы сказали \"" + a + "\"")
            stage = 1
            stage2 = 0
            c = []
        except sp.UnknownValueError:
            # print("вы промолчали")
            stage = 2
            stage2 = 0
        except sp.RequestError:
            stage = 3
            # print("гугл не захотел понимать")
            stage2 = 0
        if debug == 1:
            print("a - \"" + a + "\"; c - " + str(c) + "; stage - " + str(stage) + "; stage2 - " + str(stage2) + "; LastMessege - " + str(LastMessege) + "; Random - " + str(Random) + "; debug - " + str(debug) + "; While - " + str(While) + "; Whiles - " + str(Whiles))

        # привет
        if a.lower() in S1 and stage == 1 and a != "":
            Random = random.randint(1, 3)
            LastMessege = 1
            if Random == 1:
                print("Вам тоже, " + a)
                stage2 = 0
                LastMessege = 1
            elif Random == 2:
                print("Приветствую вас")
                stage2 = 0
                LastMessege = 1
            elif Random == 3:
                print("Ку")
                stage2 = 0
                LastMessege = 1
            else:
                print("ошибка")
                stage2 = -1
        # пока
        elif a.lower() in S19 and stage == 1 and a != "":
            Random = random.randint(1, 3)
            LastMessege = 19
            stage2 = 0
            While = 1
            if Random == 1:
                print("досвидания")
            elif Random == 2:
                print("Скоро увидемся")
            elif Random == 3:
                print("Пока - пока")

            else:
                print("ошибка")
                stage2 = -1
        # сколько времени
        elif a.lower() in S3 and stage == 1 and a != "":
            print("Сейчас - " + time.strftime("%H") + " часов, " + time.strftime(
                "%M") + " минут, " + time.strftime("%S") + " секунд")
            LastMessege = 3
        # включи отладку
        elif "включи отладку" in a.lower() and stage == 1 and a != "":
            LastMessege = 20
            if debug == 0:
                print("Отладка включена")
                debug = 1
            elif debug == 1:
                print("Отладка уже включена")
        # выключи отладку
        elif "выключи отладку" in a.lower() and stage == 1 and a != "":
            LastMessege = 20
            if debug == 0:
                print("Отладка уже выключена")
            elif debug == 1:
                print("Отладка выключена")
                debug = 0
        elif a.lower() in S16 and stage == 1 and a != "" and stage3 == 0:
            print("вы уверены?")
            stage3 = 1
            LastMessege = 16
        elif a.lower() in S25 and stage == 1 and a != "" and stage3 == 1 and LastMessege == 16:
            print("выключаю пк")
            stage3 = 0
            LastMessege = 0
            os.startfile(r'C:/Windows/System32/cmd.exe')
            #os.system('rundll32 powrprof.dll,SetSuspendState 0,1,0')
        elif a.lower() in S24 and stage == 1 and a != "" and stage3 == 1 and LastMessege == 16:
            print("вы передумали")
            stage3 = 0
            LastMessege = 0
        # ошибки & отмена
        else:
            if a.lower() in S24:
                print("вы успешно отвенили операцию")
                stage2 = 0
                LastMessege = 0
                While = 1
                a = ""
            else:
                #print("что то пошло не так")
                LastMessege = 0
                a = ""