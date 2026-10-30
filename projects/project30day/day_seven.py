import json

NAMA_FILE : str  = "data_pasien.json"

def simpan_data(data : list[dict], nama_file : str = NAMA_FILE) -> None :
    with open(nama_file, "w", encoding="utf-8") as file :
        json.dump(data, file, ensure_ascii=False, indent=4)


def muat_data(nama_file : str = NAMA_FILE) -> list[dict] :
    try : 
        with open(nama_file, "r", encoding="utf-8") as file :
            return json.load(file)
    except FileNotFoundError : 
        return []


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
    
def update_pasien(data : list[dict], id_pasient : int, riwayat_baru : str) -> bool :
    pasien = cari_pasien(data, id_pasient)
    if pasien is None :
        return False
    pasien['riwayat'] = riwayat_baru
    return True

def hapus_pasien(data : list[dict], id_pasient : int) -> bool :
    pasien = cari_pasien(data, id_pasient)
    if pasien is None :
        return False
    data.remove(pasien);
    return True

def main_program(data : list[dict]) -> None :
    while True :
        print("====== Rumah Sakit ======")
        print("1. Tambah Pasien")
        print("2. Tampilkan Semua Pasien")
        print("3. Cari Pasien")
        print("4. Update Riwayat Pasien")
        print("5. Hapus Pasien")
        print("6. Keluar")

        pilihan = int(input("Masukkan Pilihan : "))

        match pilihan :
            case 1 :
                nama = str(input("masukkan nama : "))
                umur = int(input("masukkan umur: "))
                riwayat = str(input("masukkan riwayat: "))
                tambah_pasien(data, nama, umur, riwayat)
                print("Pasien berhasil ditambahkan")
                
            case 2 :
                tampilkan_semua_pasien(data)

            case 3 :
                id = int(input("Masukkan ID Passien : "))
                pasien = cari_pasien(data, id)

                if pasien is None :
                    print("Pasien Tidak Ada")
                    
                print(pasien)
            case 4 :
                id_pasien = int(input("Masukkan Id Pasien : "))
                riwayat_baru : str = str(input("Masukkan Riwayat Penyakit Baru : "))
                if update_pasien(data, id_pasien, riwayat_baru) :
                    simpan_data(data);
                    print("Riwayat Baru Berhasil Di Tambahkan")
                else : 
                    print("Pasient Tidak Di Temukan")

            case 5 :
                id_pasien : int = int(input("Masukkan Id Pasien : "))
                if hapus_pasien(data, id_pasien) :
                    simpan_data(data)
                    print("Data Pasien Berhasil Di Hapus")
                else : 
                    print("Pasien Tidak Di Temukan")
            case 6 :
                break
                    
                
                


        # Besok Bikin Update
        
if __name__ == "__main__":
    data = muat_data()
    main_program(data)
