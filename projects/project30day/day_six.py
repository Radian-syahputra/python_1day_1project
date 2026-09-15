#  Konversi Suhu


def celsius_to_fahrenheit(celsius : float) -> float:
    return (celsius * 9/5) + 32

def fahreheit_to_celsius(fahrenheit : float) -> float :
    return (fahrenheit - 32) * 5/9

def celsius_to_reamur(celsius : float) -> float :
    return celsius * 4/5

def main_fuction(pilihan : int) -> None :
    match pilihan :
        case 1 : 
            print("Konversi Dari Celsius Ke Fahrenheit")
            celsius = float(input("Masukkan Suhu Dalam Celcius: "))
            print(f"Nilai Fahrenheit : {celsius_to_fahrenheit(celsius)}")
        case 2 :
            print("konversi Dari Fahrenheit ke Celsius")
            fahrenheit = float(input("Masukkan Suhu Dalam Fahrenheit: "))
            print(f"Nilai Celsius : {fahreheit_to_celsius(fahrenheit)}")
        case 3 :
            print("Konversi Dari Celsius ke Reamur")
            celsius = float(input("Masukkan Nilai Celcius: "))
            print(f"Nilai Reamur : {celsius_to_reamur(celsius)}")


if __name__ == "__main__":
    print("Pilih Operasi: ")
    print("===================================")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Celsius ke Reamur")
    print("===================================")
    pilihan = int(input("Masukkan Pilihan: "))
    main_fuction(pilihan)