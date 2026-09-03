#  Project 30 Day | Day 1 -> Kalkulator with class


class Kalkulator : 
    def __init__(self, angka1 : int, angka2 : int) -> None:
        self.angka1 : int = angka1
        self.angka2 : int = angka2
        
    def tambah(self) -> int :
        return self.angka1 + self.angka2

    def kurang(self) -> int :
        return self.angka1 - self.angka2

    def kali(self) -> int :
        return self.angka1 * self.angka2

    def bagi(self) -> float :
        return self.angka1 / self.angka2

    def pangkat(self) -> int :
        return self.angka1 ** self.angka2

    def modulus(self) -> int :
        return self.angka1 % self.angka2


if __name__ == "__main__" :
    kalkulator = Kalkulator(12, 2)

    print(kalkulator.tambah())
    print(kalkulator.kurang())
    print(kalkulator.kali())
    print(kalkulator.bagi())
    print(kalkulator.pangkat())
    print(kalkulator.modulus())




# Build Calculator
class Calculator :
    def __init__(self) -> None:
        pass

    def tambah(self, angka1 : int, angka2 : int) -> None :
        self.angka1 : int = angka1
        self.angka2 : int = angka2

        print(self.angka1 + self.angka2)



calculator = Calculator()

calculator.tambah(21, 7)