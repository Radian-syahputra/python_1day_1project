import random

SOAL = [
    {
        "pertanyaan": "Organ apa yang menghasilkan hormon insulin?",
        "pilihan": ["Hati", "Pankreas", "Ginjal", "Lambung"],
        "jawaban": "Pankreas",
    },
    {
        "pertanyaan": "Vitamin apa yang dibentuk kulit dengan bantuan sinar matahari?",
        "pilihan": ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin K"],
        "jawaban": "Vitamin D",
    },
]

def minta_pilihan(jumlah_pilihan : int) -> int :
    while True :
        try :
            nomor = int(input("Masukkan Pilihan Anda : "))
        except ValueError : 
            print("Masukkan Pilihan Berupa Angka")
            continue

        if nomor >= 1 and nomor <= jumlah_pilihan :
            return nomor
        else :
            print(f"Pilih Angka 1 Sampai {jumlah_pilihan}")


def ajukan_soal(soal : dict, nomor : int) -> bool:
    pilihan = soal["pilihan"].copy()
    random.shuffle(pilihan)

    # Tampilkan Nomor Dan Pertanyaan
    print(f"\n{nomor}. {soal['pertanyaan']}")
    for i , teks in enumerate(pilihan, start=1) :
        print(f"{i}. {teks}")

    # Input User
    nomor_pilihan : int = minta_pilihan(len(pilihan))
    hitung_index : int = nomor_pilihan - 1

    # Ambil List
    jawaban_user = pilihan[hitung_index]
    return jawaban_user == soal['jawaban']


def jalankan_kuis(bank_soal : list[dict], jumlah_soal : int) -> int :
    skor : int = 0
    jumlah_ambil : int = min(jumlah_soal, len(bank_soal))

    soal_terpilih : list[dict] = random.sample(bank_soal, jumlah_ambil)

    for nomor , soal in enumerate(soal_terpilih, start=1 ) :
        if  ajukan_soal(soal, nomor) is True :
            skor = skor + 1
            
    return skor
    

def tampilkan_hasil(skor : int, jumlah_soal:int) -> None :

    if jumlah_soal == 0 :
        print("Tidak Ada Soal Yang Di Jawab")
        return
    
    presentase : float = skor / jumlah_soal * 100

    print(f"Skor : {skor} Jumlah Soal : {jumlah_soal}")
    print(f"Presentase : {presentase}")

    if presentase >= 80 :
        print("Sangat Baik")
    elif presentase >= 60 :
        print("Baik")
    elif presentase >= 40 :
        print("Perlu Belajar Lagi")
    else :
        print("Pelajari Lagi Dasar-Dasar nya dek :)")

    