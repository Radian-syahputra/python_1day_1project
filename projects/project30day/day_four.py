#  Reminder Minum Obat 

import datetime as dt
import time as tm


def reminder_minum_obat(target_minum: dt.time, pesan : str) -> None:
    now= dt.datetime.now()
    target_time = dt.datetime.combine(now.date(), target_minum)

    if now >= target_time :
        print("Waktu sudah lewat")
        return

    print(f"Menunggu Sampai Jam {target_minum.strftime('%H:%M')}")
    while dt.datetime.now() < target_time :
        tm.sleep(1) # 1 detik

    print(pesan)


if __name__ == "__main__" :
    target_minum : dt.time = dt.time(22, 52)
    pesan : str = "Waktu minum obat sudah sampai!"
    reminder_minum_obat(target_minum, pesan)

    
        
