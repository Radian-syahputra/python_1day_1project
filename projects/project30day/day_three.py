# Project Konverter Satuan 

class KonverterSatuan:
    def __init__(self, satuan_awal : str, satuan_akhir : str) -> None:
        self.satuan_awal = satuan_awal
        self.satuan_akhir = satuan_akhir


    def konversi(self, nilai  : float) -> float :
        if self.satuan_awal == 'cm' and self.satuan_akhir == 'mm' :
            return nilai * 10
        elif self.satuan_awal == 'mm' and self.satuan_akhir == 'cm' :
            return nilai * 0.1
        elif self.satuan_awal == 'cel' and self.satuan_akhir == 'fah' :
            return nilai * 9/5 + 32
        elif self.satuan_awal == 'kg' and self.satuan_akhir == 'lbs' :
            return nilai * 2.20462
        elif self.satuan_awal == 'lbs' and self.satuan_akhir == 'kg' :
            return nilai * 0.453592
        elif self.satuan_awal == 'cm' and self.satuan_akhir == 'inch' :
            return nilai * 0.393701
        elif self.satuan_awal == 'inch' and self.satuan_akhir == 'cm' :
            return nilai * 2.54
        else:
            return nilai

    def tampilkan(self, nilai : float) -> None:
        print(f"Hasil konversi: {nilai}")


satuan_awal : str = input("Masukkan satuan awal: ")
satuan_akhir : str = input("Masukkan satuan akhir: ")
nilai : float = float(input("Masukkan nilai: "))


konverter = KonverterSatuan(satuan_awal, satuan_akhir)
hasil = konverter.konversi(nilai)
konverter.tampilkan(hasil)
