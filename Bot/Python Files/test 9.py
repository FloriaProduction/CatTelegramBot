import os
WhileEnabled = 1
Debug = "1"

while WhileEnabled == 1:
    try:
        FileX = open(r'C:/TelegramBot/FilesUsers/MrMarlain/Notes.txt', "rt", encoding='utf8')
        TextFileX = FileX.read()
        Notes = ""
        Notes = str(TextFileX)
        FileX.close()
        if Debug == "1":
            print("-список прочитан успешно")
        break
    except:
        FileX = open('C:/TelegramBot/FilesUsers/MrMarlain/Notes.txt', 'w', encoding='utf8')
        FileX.close()
        if Debug == "1":
            print("-список создан успешно")
if len(Notes) == 0:
    print("в списке пусто")
else:
    print(Notes)