def tambah_pasien(data: list[dict], nama: str, umur: int, riwayat: str) -> None:
    new_id = max((p["id"] for p in data), default=0) + 1
    new_pasien = {"id": new_id, "nama": nama, "umur": umur, "riwayat": riwayat}
    data.append(new_pasien)


def tampilkan_semua_pasien(data: list[dict]) -> None:
    if not data:
        print("pasien kosong")
        return
    for p in data:
        print(p)


def cari_pasien(data: list[dict], id: int) -> dict | None:
    for p in data:
        if p["id"] == id:
            return p
    return None


def main_program(data : list[dict]) -> None :
    while True :
        print("====== Rumah Sakit ======")
        print("1. Tambah Pasien")
        print("2. Tampilkan Semua Pasien")
        print("3. Cari Pasien")
        print("4. keluar")

        pilihan = int(input("Masukkan Pilihan : "))

        match pilihan :
            case 1 :
                nama = str(input("masukkan nama : "))
                umur = int(input("masukkan umur: "))
                riwayat = str(input("masukkan riwayat: "))
                tambah_pasien(data, nama, umur, riwayat)
                print("Pasien berhasil ditambahkan")
                
            case 2 :
                semua_pasien = tampilkan_semua_pasien(data)
                print(semua_pasien)

            case 3 :
                id = int(input("Masukkan ID Passien : "))
                pasien = cari_pasien(data, id)
                print(pasien)

            case 4 :
                break


        # Besok Bikin Update

if __name__ == "__main__":
    data = [
        {"id": 1, "nama": "Budi", "umur": 25, "riwayat": "Batuk"},
        {"id": 2, "nama": "Andi", "umur": 30, "riwayat": "Flu"},
    ]
    main_program(data)
