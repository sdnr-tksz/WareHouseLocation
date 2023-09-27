import math

# Dosya okuma işlemi
def FileOpen(txt):
    dizi,depo,dc,tcw=[],[],[],[]
    f = open(txt, 'r')
    for satir in f:
        dizi.append(satir.strip())

    
    # txt deki ilk satır depo sayısı
    deposayisi=dizi[0].split(" ")[0]
    dizi.pop(0)
    depo=dizi[0:int(deposayisi)]
    del dizi[0:int(deposayisi)]
    i=0
    for indis in depo:
        depo[i]=[float(indis.split(" ")[0]),float(indis.split(" ")[1])]
        depo[i].append(i)
        i+=1
    depo.sort()

    # Talep kapasitesi ve seyehat maliyeti çekilir.
    for indis in range(len(dizi)):
        if(indis%2!=0):
            tcw.append(dizi[indis].split(" "))
        else:
            dc.append(dizi[indis])
            dc= [float(i) for i in dc]
    for indis in range(len(tcw)):
        tcw[indis] = [float(i) for i in tcw[indis]]
    optimalMaliyet(depo,dc,tcw)


def optimalMaliyet(depo,dc,tcw):
    count,aw,optimalmaliyet=0,[],0
    for musteri in dc:
        for satir in depo:
            if(satir[0]<musteri):
                continue
            else:
                tut=satir[2]
                aw.append(tut)
                break
        optimalmaliyet+=tcw[count][tut]
        count+=1
    for indis in range(len(aw)):
        if indis==0:
            tut=indis
            optimalmaliyet+=depo[indis][1]
        else:
            if tut!=aw[indis]:
                optimalmaliyet+=depo[indis][1]
                tut=indis
    print("Optimal Maliyet:",optimalmaliyet)
    print("Depoya Atanan Müşteriler:",aw)

FileOpen('wl_3_0.txt')
FileOpen('wl_16_1.txt')
FileOpen('wl_200_2.txt')
FileOpen('wl_500_3.txt')