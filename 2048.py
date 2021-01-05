import random
global matris
global puan
puan=0

global matris
matris=[[0 for j in range(4)] for i in range(4)]
x=random.randint(0,3)
y=random.randint(0,3)
matris[i][j]=2

def kayit(isim):
    global puan
    kayitpuan=str(puan)
    dosya = open("score.txt", "a")
    dosya.write(isim)
    dosya.write("\t")
    dosya.write(":")
    dosya.write(kayitpuan)
    dosya.write(":")
    dosya.write("\n")

    dosya.close()

def scoretablo():
    dosya=open("score.txt","r")
    veriliste=dosya.read()
    dosyalistesi=veriliste.split(":")
    for i in range(len(dosyalistesi)):
        for j in range(1,((len(dosyalistesi)-1)/2)):
            if int(dosyalistesi[(2*j)+1])>int(dosyalistesi[(2*j)-1]):
                aktarma=dosyalistesi[(2*j)+1]
                aktarma2=dosyalistesi[(2*j)]
                dosyalistesi[(2*j)+1]=dosyalistesi[(2*j)-1]
                dosyalistesi[(2*j)]=dosyalistesi[(2*j)-2]
                dosyalistesi[(2*j)-1]=aktarma
                dosyalistesi[(2*j)-2]=aktarma2
    print "\nSCORE TABLOSU"            
    for i in range(0,20,2):
        if len(dosyalistesi)<20:
            for j in range(dosyalistesi):
                print dosyalistesi[j]
        else:
            print dosyalistesi[i]+dosyalistesi[i+1]
                

    dosya.close()


def olustur():
    global puan
    global matris
    puan=0
    matris=[[0 for j in range(4)] for i in range(4)]
    x=random.randint(0,3)
    y=random.randint(0,3)

    


def boskontrol():
    kontrol=0
    while kontrol==0:
        for j in range(4):
            for i in range(4):
                if matris[i][j]==0:
                    kontrol=1
                    return kontrol
        return kontrol
    

def rastgele():
    anahtar=True
    while anahtar==True:
        x=random.randint(0,3)
        y=random.randint(0,3)
        if matris[x][y]==0:

            if puan<750:
                matris[x][y]=2
                
            elif puan>750:
                atama=random.randint(0,1)
                if atama==0:
                    matris[x][y]=2
                else:
                    matris[x][y]=4
            elif puan>2000:
                atama=random.randint(0,2)
                if atama==0:
                    matris[x][y]=2
                elif atama==1:
                    matris[x][y]=4
                else:
                    matris[x][y]=8
            else:
                pass
            
            anahtar=False
        else:
            anahtar=True

    
def toplama(yon):
    global puan
    if yon=='s':
        for j in range(4):
            i=2
            while i>=0:
                if (matris[i][j]==matris[i+1][j]):
                    matris[i+1][j]=matris[i][j] + matris[i+1][j]
                    matris[i][j]=0
                    puan=puan+matris[i+1][j]
                    i=i-1
                i=i-1
                
    elif yon=='w':
        for j in range(4):
            i=1
            while i<=3:
                if (matris[i][j]==matris[i-1][j]):
                    matris[i-1][j]=matris[i][j] + matris[i-1][j]
                    matris[i][j]=0
                    puan=puan+matris[i-1][j]
                    i=i+1
                i=i+1


    elif yon=='d':
        for i in range(4):
            j=2
            while j>=0:
                if (matris[i][j]==matris[i][j+1]):
                    matris[i][j+1]=matris[i][j] + matris[i][j+1]
                    matris[i][j]=0
                    puan=puan+matris[i][j+1]
                    j=j-1
                j=j-1


    elif yon=='a':
        for i in range(4):
            j=1
            while j<=3:
                if (matris[i][j]==matris[i][j-1]):
                    matris[i][j-1]=matris[i][j] + matris[i][j-1]
                    matris[i][j]=0
                    puan=puan+matris[i][j-1]
                    j=j+1
                j=j+1

                    

def kaydirma(yon):
    if yon=='w':
        for x in range(4):
            for j in range(4):
                for i in range(2,-1,-1):
                    if matris[i][j]==0:
                        matris[i][j]=matris[i+1][j]
                        matris[i+1][j]=0

    elif yon=='s':
        for x in range(4):
            for j in range(4):
                for i in range(1,4,1):
                    if matris[i][j]==0:
                        matris[i][j]=matris[i-1][j]
                        matris[i-1][j]=0

    elif yon=='a':
        for x in range(4):
            for i in range(4):
                for j in range(2,-1,-1):
                    if matris[i][j]==0:
                        matris[i][j]=matris[i][j+1]
                        matris[i][j+1]=0

    elif yon=='d':
        for x in range(4):
            for i in range(4):
                for j in range(1,4,1):
                    if matris[i][j]==0:
                        matris[i][j]=matris[i][j-1]
                        matris[i][j-1]=0


    

def yazdirma():
    global puan
    for i in range(4):
        for j in range(4):
            print matris[i][j],'\t',
        print '\n'
    print '\n','puan=',puan


def oyun():
    
    while boskontrol()==1:
        rastgele()
        yazdirma()
        yon=raw_input('yon girin(w,a,s,d):')
        kaydirma(yon)
        toplama(yon)
        kaydirma(yon)
        boskontrol()
    if boskontrol()==0:
        anayer()
        
def anayer():
    global isim
    global baslama
    if boskontrol()==0:
        kayit(isim)
        print "oyun bitti"
        baslama=raw_input("tekrar baslamak icin 'r'ye basin:")
        
    else:
        isim=raw_input('isim girin:')
        oyun()
        
    if baslama=='r':
        olustur()
        oyun()
    else:
        pass
    
anayer()
scoretablo()                
                

