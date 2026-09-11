#  Reminder Minum Obat 

import datetime
import time 


def reminder_minum_obat(target_minum: datetime.time, pesan : str) -> None:
    now= datetime.datetime.now()
    target_time = datetime.datetime.combine(now.date(), target_minum)

    if now >= target_time :
        print("Waktu sudah lewat")
        return

    print(f"Menunggu Sampai Jam {target_minum.strftime('%H:%M')}")
    while datetime.datetime.now() < target_time :
        time.sleep(1) # 1 detik

    print(pesan)


if __name__ == "__main__" :
    target_minum : datetime.time = datetime.time(22, 52)
    pesan : str = "Waktu minum obat sudah sampai!"
    reminder_minum_obat(target_minum, pesan)

    
        
