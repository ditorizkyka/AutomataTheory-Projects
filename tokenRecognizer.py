def ceksubjek(subjek):
    state = 0
    i = 0
    while i < len(subjek):
        if state == 0:
            if subjek[i] == 'a':
                state = 15
            elif subjek[i] == 'k':
                state = 14
            elif subjek[i] == 'd':
                state = 12
            elif subjek[i] == 'm':
                state = 13
        elif state == 15:
            if subjek[i] == 'k':
                state = 11
        elif state == 14:
            if subjek[i] == 'a':
                state = 10
            elif subjek[i] == 'i':
                state = 8
        elif state == 12:
            if subjek[i] == 'i':
                state = 7
        elif state == 13:
            if subjek[i] == 'e':
                state = 5
        elif state == 11:
            if subjek[i] == 'u':
                state = 1
        elif state == 10:
            if subjek[i] == 'm':
                state = 9
        elif state == 9:
            if subjek[i] == 'i':
                state = 1
        elif state == 8:
            if subjek[i] == 't':
                state = 2
        elif state == 7:
            if subjek[i] == 't':
                state = 6
        elif state == 6:
            if subjek[i] == 'o':
                state = 1
        elif state == 5:
            if subjek[i] == 'r':
                state = 4
        elif state == 4:
            if subjek[i] == 'e':
                state = 3
        elif state == 3:
            if subjek[i] == 'k':
                state = 2
        elif state == 2:
            if subjek[i] == 'a':
                state = 1
        elif state == 1:
            break
        i += 1
    # print(subjek, state,i)
    return state == 1


def cekpredikat(predikat):
    state = 0
    i = 0
    while i < len(predikat):
        if state == 0:
            if predikat[i] == 'm':
                state = 22
        elif state == 25:
            if predikat[i] == 'p':
                state = 21  
            elif predikat[i] == 'b':
                state = 14  
        elif state == 24:
            if predikat[i] == 'c':
                state = 9  
            elif predikat[i] == 'u':
                state = 11  
            elif predikat[i] == 'g':
                state = 5  
        elif state == 23:
            if predikat[i] == 'm':
                state = 25  
            elif predikat[i] == 'n':
                state = 24  
        elif state == 22:
            if predikat[i] == 'e':
                state = 23
        elif state == 21:
            if predikat[i] == 'e':
                state = 20  
        elif state == 20:
            if predikat[i] == 'l':
                state = 19  
        elif state == 19:
            if predikat[i] == 'a':
                state = 18  
        elif state == 18:
            if predikat[i] == 'j':
                state = 17  
        elif state == 17:
            if predikat[i] == 'a':
                state = 16  
        elif state == 16:
            if predikat[i] == 'r':
                state = 15  
        elif state == 15:
            if predikat[i] == 'i':
                state = 1  
        elif state == 14:
            if predikat[i] == 'a':
                state = 13 
        elif state == 13:
            if predikat[i] == 'c':
                state = 12
        elif state == 12:
            if predikat[i] == 'a':
                state = 1  
        elif state == 11:
            if predikat[i] == 'l':
                state =  10
        elif state == 10:
            if predikat[i] == 'i':
                state = 2
        elif state == 9:
            if predikat[i] == 'a':
                state = 8
        elif state == 8:
            if predikat[i] == 't':
                state = 7
        elif state == 7:
            if predikat[i] == 'a':
                state = 6
        elif state == 6:
            if predikat[i] == 't':
                state = 1
        elif state == 5:
            if predikat[i] == 'u':
                state = 4
        elif state == 4:
            if predikat[i] == 'l':
                state = 3
        elif state == 3:
            if predikat[i] == 'a':
                state = 2
        elif state == 2:
            if predikat[i]== 's':
                state = 1
        elif state == 1:
            break
        i += 1
    # print(predikat, state, i)
    return state == 1

def cekobjek(objek):
    state = 0
    i = 0
    while i < len(objek):
        if state == 0:
            if objek[i] == 'm':
                state = 20
            elif objek[i] == 'k':
                state = 17
            elif objek[i] == 'b':
                state = 18
            elif objek[i] == 't':
                state = 19
        elif state == 21:
            if objek[i] == 't':
                state = 16 
            elif objek[i] == 'j':
                state = 5 
        elif state == 20:
            if objek[i] == 'a':
                state = 21  
        elif state == 19:
            if objek[i] == 'u':
                state = 13  
        elif state == 18:
            if objek[i] == 'u':
                state = 10  
        elif state == 17:
            if objek[i] == 'o':
                state = 8
        elif state == 16:
            if objek[i] == 'e':
                state = 15
        elif state == 15:
            if objek[i] == 'r':
                state = 14   
        elif state == 14:
            if objek[i] == 'i':
                state = 1 
        elif state == 13:
            if objek[i] == 'g':
                state = 12
        elif state == 12:
            if objek[i] == 'a':
                state = 11
        elif state == 11:
            if objek[i] == 's':
                state = 1 
        elif state == 10:
            if objek[i] == 'k':
                state = 9
        elif state == 9:
            if objek[i] == 'u':
                state = 1
        elif state == 8:
            if objek[i] == 'm':
                state = 7
        elif state == 7:
            if objek[i] == 'i':
                state = 6
        elif state == 6:
            if objek[i] == 'k':
                state = 1   
        elif state == 5:
            if objek[i] == 'a':
                state = 4
        elif state == 4:
            if objek[i] == 'l':
                state = 3
        elif state == 3:
            if objek[i] == 'a':
                state = 2
        elif state == 2:
            if objek[i] == 'h':
                state = 1  
        elif state == 1:
            break
        i += 1
    # print(objek, state, i)
    return state == 1

def cekketerangan(keterangan):
    state = 0
    i = 0
    while i < len(keterangan):
        char = keterangan[i]
        if state == 0:
            if char == 'd':
                state = 30        
        elif state == 30:
            if char == 'i':
                state = 32
        elif state == 31:
            if char == ' ':
                state = 32           
        elif state == 32:
            if char == 'k':
                state = 29
            elif char == 'r':
                state = 25
            elif char == 'b':
                state = 23
            elif char == 'p':
                state = 18
            elif char == 's':
                state = 7
        elif state == 29:
            if char == 'e':
                state = 28
        elif state == 28:
            if char == 'l':
                state = 27
        elif state == 27:
            if char == 'a':
                state = 26 
        elif state == 26:
            if char == 's':
                state = 1    
        elif state == 25:
            if char == 'u':
                state = 24      
        elif state == 24:
            if char == 'm':
                state = 3       
        elif state == 23:
            if char == 'a':
                state = 22   
        elif state == 22:
            if char == 'n':
                state = 21   
        elif state == 21:
            if char == 'g':
                state = 20    
        elif state == 20:
            if char == 'k':
                state = 19   
        elif state == 19:
            if char == 'u':
                state = 1   
        elif state == 18:
            if char == 'e':
                state = 17  
        elif state == 17:
            if char == 'r':
                state = 16      
        elif state == 16:
            if char == 'p':
                state = 15     
        elif state == 15:
            if char == 'u':
                state = 14     
        elif state == 14:
            if char == 's':
                state = 13 
        elif state == 13:
            if char == 't':
                state = 12
        elif state == 12:
            if char == 'a':
                state = 11
        elif state == 11:
            if char == 'k':
                state = 10
        elif state == 10:
            if char == 'a':
                state = 9
        elif state == 9:
            if char == 'a':
                state = 8
        elif state == 8:
            if char == 'n':
                state = 1
        elif state == 7:
            if char == 'e':
                state = 6
        elif state == 6:
            if char == 'k':
                state = 5
        elif state == 5:
            if char == 'o':
                state = 4
        elif state == 4:
            if char == 'l':
                state = 3
        elif state == 3:
            if char == 'a':
                state = 2
        elif state == 2:
            if char == 'h':
                state = 1
        if state == 1:
            break
        i += 1
    # print(keterangan, state,i)
    return state == 1




# # Test subjek
# print("Cek Subjek:")
# print(ceksubjek("aku"))       # Expected output: True
# print(ceksubjek("kami"))      # Expected output: True
# print(ceksubjek("kita"))      # Expected output: True
# print(ceksubjek("dito"))      # Expected output: True
# print(ceksubjek("mereka"))    # Expected output: True
# print(ceksubjek("diti"),f'\n\n\n')    # fail
# # Test predikat
# print("Cek Predikat:")
# print(cekpredikat("mempelajari"))  # Expected output: True
# print(cekpredikat("membaca"))      # Expected output: T6rue
# print(cekpredikat("menulis"))      # Expected output: True
# print(cekpredikat("mencatat"))     # Expected output: True
# print(cekpredikat("mengulas"))     # Expected output: True
# print(cekpredikat("menggambar"),f'\n\n\n')   # fail


# # Test objek
# print("Cek Objek:")
# print(cekobjek("materi"))  # Expected output: True
# print(cekobjek("tugas"))   # Expected output: True
# print(cekobjek("buku"))    # Expected output: True
# print(cekobjek("komik"))   # Expected output: True
# print(cekobjek("majalah")) # Expected output: True
# print(cekobjek("kunci"),f'\n\n\n')   # fail

# # Test keterangan
# print(cekketerangan("di kelas"))  # Expected output: True
# print(cekketerangan("di rumah"))  # Expected output: True
# print(cekketerangan("di bangku"))  # Expected output: True
# print(cekketerangan("di perpustakaan"))  # Expected output: True
# print(cekketerangan("di sekolah"))  # Expected output: True
# print(cekketerangan("di pasar"))  # Expected output: False