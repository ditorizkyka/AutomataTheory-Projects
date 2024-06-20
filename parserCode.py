from tokenRecognizer import cekketerangan, cekobjek, cekpredikat, ceksubjek

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def splitKalimat(kalimat):
    kalimatspok = kalimat.split()
    subjek = kalimatspok[0]
    
    if (len(kalimatspok) == 5) :
        predikat = kalimatspok[1]
        objek = kalimatspok[2]
        keterangan = kalimatspok[3] + kalimatspok[4]
    elif (len(kalimatspok) == 4) :
        predikat = kalimatspok[1]
        objek = ""
        keterangan = kalimatspok[-2] + kalimatspok[-1]
    elif (len(kalimatspok) == 3) :
        predikat = kalimatspok[1]
        objek = kalimatspok[2]
        keterangan = ""
    elif (len(kalimatspok) == 2) :
        predikat = kalimatspok[1]
        objek = ""
        keterangan = ""
    elif(len(kalimatspok) == 1):
        predikat = ""
        objek = ""
        keterangan = ""

    
    return subjek, predikat, objek, keterangan

def kalimatValid(sub,pred,obj,ket, kalimat):
    i = 0
    stack = Stack()
    validate = []
    state = 'i'
    cek = True
    idx = 0
    stack.push('#')
    state = 'p'
    stack.push('S')
    state = 'q'

    while(stack.top() != '#' and cek == True) :

        if stack.top() == 'S' :
            if (pred != ""):
                stack.pop()
                stack.push('P')
                stack.push('s')
            else :
                cek = False

        if stack.top() == 'P' :
            if (obj == "" and ket == "") :
                stack.pop()
                stack.push('p')
            elif(obj == "" and ket != ""):
                stack.pop()
                stack.push('K')
                stack.push('p')
            else :
                stack.pop()
                stack.push('O')
                stack.push('p')
        
        if stack.top() == 'O':
            if (ket == "") :
                stack.pop()
                stack.push('o')
            else :
                stack.pop()
                stack.push('K')
                stack.push('o')

        if stack.top() == 'K':
            stack.pop()
            stack.push('k')
        
        if stack.top() == 's':
            if (ceksubjek(sub) == True):
                stack.pop()
                validate.append('S')
                idx+= 1
            else :
                cek = False

        if stack.top() == 'p':
            if (cekpredikat(pred) == True):
                stack.pop()
                validate.append('P')
                idx+= 1
            else :
                cek = False
        
        if stack.top() == 'o':
            if (cekobjek(obj) == True) :
                stack.pop()
                validate.append('O')
                idx+= 1
            else :
                cek = False

        if stack.top() == 'k':
            if (cekketerangan(ket) == True) :
                stack.pop()
                validate.append('K')
                idx+= 1
            else :
                cek = False
    

    if (stack.top() == "#") :
        stack.pop()
        state = 'r'
        print(f"-- KALIMAT {kalimat} VALID --\n")
        print(f"Struktur Kalimat terbaca : ")
        while (i < len(validate) ):
            if (validate[i] == 'S') :
                print(f'{sub} sebagai Subjek')
            elif (validate[i]== 'P') :
                print(f'{pred} sebagai Predikat')
            elif (validate[i]== 'O') :
                print(f'{obj} sebagai Objek')
            elif (validate[i]== 'K') :
                print(f'{ket} sebagai Keterangan')
            
            print()
            i+= 1 

    else:
        print(f"-- KALIMAT {kalimat} INVALID --\n")
        print(f'Program Tidak mengenali salah satu dari unsur kata dan stack berhenti pada {stack.top()}')
    

    


