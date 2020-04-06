import datetime as date

if __name__ == "__main__":

    now = date.datetime.now()
    last_update = date.datetime.strptime("06/04/2020 00:00:00", "%d/%m/%Y %H:%M:%S") #24

    delta = now - date.timedelta(minutes=30)

    print(last_update)
    print(now)
    print(delta)

    if delta >= last_update:
        print("Han pasado 30 mins :d")

    #tct = DT.datetime.strptime("05/04/2021 01:4:40", "%d/%m/%Y %H:%M:%S") #24

