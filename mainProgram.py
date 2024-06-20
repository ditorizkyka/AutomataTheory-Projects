from parserCode import kalimatValid, splitKalimat

print("====================================================")
print("|                                                  |")
print("|    TUGAS BESAR TEORI BAHASA DAN AUTOMATA         |")
print("|    Program Detektsi Kalimat                      |")
print("|    Anggota Kelompok :                            |")
print("|     1. Andito Rizkyka - 1301220016               |")
print("|     2. Farizsyach Razif Januar - 1301220439      |")
print("|     3. Imam Wijayanto - 1301223117               |")
print("|                                                  |")
print("====================================================")

user = 'Y'

while (user != 'N'):
    kalimat = input("Masukan Kalimat SP/SPO/SPK/SPOK! ")
    print()
    subjek, predikat, objek, keterangan = splitKalimat(kalimat)
    kalimatValid(subjek, predikat, objek, keterangan, kalimat)  
    user = input('Cek kalimat lain (Y/N)? ')
    print()
