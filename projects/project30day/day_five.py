# Project cek Tegangan Darah

def cek_tekanan_darah(sistol: int, diastol: int) -> str:
    if sistol >= 180 or diastol >= 120:
        return "Krisis Hipertensi: Segera cari bantuan medis!!"
    elif sistol >= 140 or diastol >= 90:
        return "Hipertensi Tahap 2"
    elif (130 <= sistol <= 139) or (80 <= diastol <= 89):
        return "Hipertensi Tahap 1"
    elif (120 <= sistol <= 129) and diastol < 80:
        return "Elevated"
    else:
        return "Normal"


sistol_input = int(input("Masukkan tekanan darah sistol: "))
diastol_input = int(input("Masukkan tekanan darah diastol: "))

print(cek_tekanan_darah(sistol_input, diastol_input))

