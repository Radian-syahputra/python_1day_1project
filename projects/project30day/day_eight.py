#  Kalkulator Kebutuhan Kaori Harian (BMR dan TDEE)


def hitung_bmr(berat : float,tinggi : float, umur : int, jenis_kelamin : str) -> float :
    rumus_dasar = 10 * berat + 6.25 * tinggi - 5 * umur
    if jenis_kelamin.lower() == "pria" :
        return rumus_dasar + 5
    return rumus_dasar - 161

FAKTOR_AKTIVITAS = {    
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9,
}

def hitung_tdee(bmr : float, level_aktifitas : int) -> float | None :
    faktor = FAKTOR_AKTIVITAS.get(level_aktifitas)
    if faktor is None :
        return None
    return bmr * faktor


def main_program() -> None :
    berat : float = float(input("Masukkan Berat Badan : "))
    tinggi : float = float(input("Masukkan Tinggi Badan : "))
    umur : int = int(input("Masukkan Umur : "))
    jenis_kelamin : str = str(input("Masukkan Jenis Kelamin Anda : "))

    hasil_bmr = hitung_bmr(berat, tinggi, umur, jenis_kelamin)

    level_aktifitas = int(input("Pilih Level Aktifitas Anda : "))
    hasil_tdee = hitung_tdee(hasil_bmr, level_aktifitas)

    print(f"Hasil BMR : {hasil_bmr}")
    print("====================")
    print(f"hasil TDEE : {hasil_tdee}")
    


if __name__ == "__main__" :
    main_program()