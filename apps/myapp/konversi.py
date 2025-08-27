def teks_dari_angka(angka: int) -> str:
    satuan: list[str] = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    belasan: list[str] = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]

    def puluhan(i):
        puluh: int = int(i / 10)
        sisa: int = i % 10
        match i:
            case i if i < 10:
                return f"{satuan[i]}"
            case i if i < 20:
                return f"{belasan[i - 10]}"
            case i if i < 100:
                if (sisa) == 0:
                    return f"{satuan[puluh]} puluh" 
                else:
                    return f"{satuan[puluh]} puluh {satuan[sisa]}"
    def ratusan(i):
        ratus: int = int(i / 100)
        sisa: int = i % 100
        match i:
            case i if i < 200:
                if (sisa) == 0:
                    return "seratus"
                else:
                    return f"seratus {puluhan(sisa)}"
            case i if i < 1000:
                if (sisa) == 0:
                    return f"{satuan[ratus]} ratus"  
                else:
                    return f"{satuan[ratus]} ratus {puluhan(sisa)}"

    # if angka == 0:
    #     return "Nol"
    # elif angka <= 99:
    #     return puluhan(angka)
    # elif angka <= 999:
    #     return ratusan(angka)
    # else:
    #     return "Error!: Harus masukan angka 0-999"

# def main():
#     try:
#         nomer: int = int(input("Masukin angka: "))
#         hasil = teks_dari_angka(nomer)
#         print(hasil)
#     except:
#         ValueError
#         print("Error! Harus masukan angka")
#         main()

# if __name__ == "__main__":
#     main()
