import time

WhileEnabled = 1
enabled = 1
TimeOut = 300
Debug = 1

Time_1 = 0  # сколько время сейчас
Time_2 = 0  # сколько время сейчас без дня и месяца
Time1 = 0  # сколько время должно пройти (прибавление + 10 сек)
Time2 = "220000"  # 10 часов вечера
Time3 = "070000"  # 7 часов утра
# + 2 сек
while WhileEnabled == 1:
    day = time.strftime("%d")
    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")

    seconds = int(seconds) + 2
    while int(seconds) >= 60:
        seconds = int(seconds) - 60
        minutes = int(minutes) + 1
    if int(seconds) < 10:
        seconds = "0" + str(seconds)
    while int(minutes) >= 60:
        minutes = int(minutes) - 60
        hours = int(hours) + 1
    while int(hours) >= 24:
        hours = int(hours) - 24
        day = int(day) + 1
    if int(day) < 10:
        day = "0" + str(day)
    while WhileEnabled == 1:
        time.sleep(1)
        Time_1 = str(time.strftime("%d")) + str(time.strftime("%H")) + str(time.strftime("%M") + str(time.strftime("%S")))
        Time1 = str(day) + str(hours) + str(minutes) + str(seconds)
        print(Time_1)
        print(Time1)
        if str(Time_1) >= str(Time1):
            if Debug == 1:
                #print(time.strftime("%d") + ":" + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
                print("\033[33mС последнего сообщения прошло - 2 секунды\033[0m")
            break
        elif str(Time_1) <= str(Time1):
            if Debug == 1:
                #print(time.strftime("%d") + ":" + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
                print("\033[31mС последнего сообщения не прошло - 2 секунды\033[0m")
            #break
    break

# Время - 7 утра, 10 вечера
while WhileEnabled == 1:
    time.sleep(1)
    Time_2 = str(time.strftime("%H")) + str(time.strftime("%M") + str(time.strftime("%S")))
    print(Time_2)
    print(Time2)
    print(Time3)
    if str(Time_2) == str(Time2):
        if Debug == 1:
            print("\033[33mСейчас 10 часов вечера\033[0m")
    elif str(Time_2) == str(Time3):
        if Debug == 1:
            print("\033[33mСейчас 7 часов утра\033[0m")
    elif str(Time_2) != str(Time2):
        if Debug == 1:
            print("\033[31mСейчас не 10 часов вечера\033[0m")
    elif str(Time_2) != str(Time3):
        if Debug == 1:
            print("\033[31mСейчас не 7 часов утра\033[0m")
    break
