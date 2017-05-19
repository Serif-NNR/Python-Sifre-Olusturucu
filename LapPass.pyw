##
##  LapPass - Parola Oluşturucu
##
##  Copyright (C) 2017 - Şerif İnanır
##  e-mail: sheriffnnr[at]gmail.com
##
##  LapPass is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by the
## Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## LapPass is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program.  If not, see <http://www.gnu.org/licenses/>.
#####################################################################################



#  PROGRAM ANLATIMI
#
#  Oluşturulacak şifrenin kaç haneli olduğu girilir.
#  O hane sayısında WHİLE döngüsü döner ve işaretlenen
#  özellikler (Büyük, Küçük, Sayı, Özel) rasgele olarak
#  seçmeye başlar ve bunları birleştirerek ekrana basar.



#-*- coding:utf-8 -*-
from tkinter import*
import random
pnc=Tk()
pnc.title("LapPass")
pnc.resizable(width=False,height=False)
pnc.geometry("400x120+300+100")
oluşanParola=[]

# ŞİFRE ÖZELLİKLERİ
yazıK=list("qwertyuıopğüişlkjhgfdsazxcvbnmöç")
yazıB=list("QWERTYUIOPĞÜİŞLKJHGFDSAZXCVBNMÖÇ")
sayı=list("1234567890")
özel=list(".,+/*-?$%&=!")

tanım=Label(text="Parola Oluşturucu @ Ctrl+C ile Kopyala",fg="red")
tanım.grid(columnspan=10)

# İŞARET BUTONLARI
Balpha2=IntVar(0)
Balpha=Checkbutton(text="Büyük Harfler",variable=Balpha2)
Balpha.grid(row=1,column=0)
Kalpha2=IntVar(0)
Kalpha2.set(1)
Kalpha=Checkbutton(text="Küçük Harfler",variable=Kalpha2)
Kalpha.grid(row=1,column=1)
Num2=IntVar(0)
Num2.set(1)
Num=Checkbutton(text="Rakamlar",variable=Num2)
Num.grid(row=1,column=2)
spec2=IntVar(0)
spec=Checkbutton(text="Özel Karakterler",variable=spec2)
spec.grid(row=1,column=3)

# ŞİFRE HANESİ
basm=Label(text="Basamak Sayısı:")
basm.grid(row=2,column=1)
basmS=Entry(width=5)
basmS.grid(row=2,column=2)


basmS.insert(0,8)
uyarı=Label(text="(max 32)")
uyarı.place(x=260,y=45)

# ŞİFREYİ OLUŞTURAN ANA FONKSİYON
def yap():
    global oluşanParola
    parola.delete(0,END)
    toplam=0
    liste=[]
    yazı2B=Balpha2.get()
    yazı2K=Kalpha2.get()
    sayı2=Num2.get()
    özel2=spec2.get()
    if yazı2B==1:
        for i in yazıB:
            liste.append(i)
        toplam+=32
    if yazı2K==1:
        for i in yazıK:
            liste.append(i)
        toplam+=32
    if sayı2==1:
        for i in sayı:
            liste.append(i)
        toplam+=10
    if özel2==1:
        for i in özel:
            liste.append(i)
        toplam+=12
    ana_toplam=toplam-1
    basamak=basmS.get()
    basamak=int(basamak)
    ilk=0
    oluşanParola=[]
    krkter=""
    while ilk<basamak:
        ilk+=1
        krkter+=liste[random.randint(0,ana_toplam)]
    parola.insert(0,krkter)

# BUTON İŞLEMLERİ
oluştur=Button(text="Oluştur",command=yap)
oluştur.grid(row=3,column=0)
parola=Entry(width=40)
parola.place(x=80,y=70)
durum=Label(text="Şerif İnanır ~~ ")
durum.place(x=310,y=100)
mainloop()