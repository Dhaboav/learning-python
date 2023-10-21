from datetime import datetime as time


def getWaktu():
    jam = time.now().hour
    menit = time.now().minute

    if menit >= 0 and menit <= 59:
        if (jam >= 0 and jam <= 10):
            return "Pagi"
        elif (jam > 10 and jam <= 14):
            return "Siang"
        elif (jam > 14 and jam <= 18):
            return "Sore"
        else:
            return "Malam"


def login(user, password):
    data_user = {
        "Admin": "0",
        "Miko": "121203",
        "Tissa": "Naga T3rbang",
        "Arthur": "Fantasy121203",
        "Keqing_fake": "Liyue00RexLapis",
        "Areka": "Aya2protect"
    }

    if user in data_user and password == data_user[user]:
        return "Accepted"
    else:
        return "Rejected"


# ======================== MAIN PROGRAM ============================================
id = input("Masukan ID: ")
password = input("Masukan Password: ")
statusLogin = login(id, password)
if statusLogin == "Accepted":
    print(f"Selamat {getWaktu()} {id}")
else:
    print(f"ID atau password anda salah!")
