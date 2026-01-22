#Фролов Владислав БЗ-ИСИТ-23

class Events:
    
        def Eat():
            return "Прием пищи"
        def Clothes():
             return "Переодеваюсь"
        def Trip():
             return "Еду"
        def Work():
             return "Работаю"
        def Shower():
             return "Принимаю душ"

class Day:
    def Daylist():
        print ("Мой распорядок дня: \n"
        "6:00 - Подъем \n"
        f"6:10 - {Events.Shower()} \n"
        f"6:20 - {Events.Eat()} (завтрак)\n"
        f"6:40 - Собираюсь на работу\n"
        f"6:50 - 7:30 - {Events.Trip()} на работу \n"
        f"7:35 - {Events.Clothes()} в рабочую одежду \n"
        f"7:40 - 12:00 - {Events.Work()} \n"
        f"12:00 - 12:40 - {Events.Eat()} (обед) \n"
        f"12:40 - 16:20 - {Events.Work()} \n"
        f"16:20 - {Events.Clothes()} в свою одежду \n"
        f"16:25 - 18:00 - {Events.Trip()} домой  \n"
        f"18:10 - {Events.Clothes()} в домашнюю одежду \n"
        f"18:20 - {Events.Eat()} (ужин) \n"
        "18:30 - 19:40 - Отдых с семьей \n"
        "19:40 - 21:15 - Играю в компухтер \n"
        f"21:15 - 21:30 - {Events.Shower()} \n"
        "21:30 - 23:30 - Просмотр видеороликов/фильмов \n"
        "23:30 - Ложусь спать \n"
        )


Day.Daylist()