# Pengecek Apakah Berat Badan nya obesitas

def is_obesitas(berat_badan: float, tinggi_badan_cm: float) -> str:
    tinggi_meter = tinggi_badan_cm / 100
    imt: float = berat_badan / (tinggi_meter ** 2)

    if imt >= 30:
        return "Obesitas"
    elif imt >= 25:
        return "Overweight"
    else:
        return "Normal"


berat_badan: float = float(input("Masukkan Berat Badan Anda (kg): "))
tinggi_badan: float = float(input("Masukkan Tinggi Badan Anda (cm): "))

if __name__ == "__main__":
    print(is_obesitas(berat_badan, tinggi_badan))