print('HELLO WORLD')
import tkinter as tk
from tkinter import messagebox

doktorlar = []
randevular = []

class Hasta:
    def __init__(self, isim, tc):
        self.isim = isim
        self.tc = tc
        self.randevu_gecmisi = []

class Doktor:
    def __init__(self, isim, uzmanlik):
        self.isim = isim
        self.uzmanlik = uzmanlik
        self.musait = True

class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta


def giris_ekrani():
    giris = tk.Tk()
    giris.title("Giriş Seçimi")
    giris.geometry("300x200")
    giris.configure(bg="#cce6ff")

    tk.Label(giris, text="Giriş Türü Seçin", font=("Arial", 14, "bold"), bg="#cce6ff").pack(pady=20)
    tk.Button(giris, text="Hasta Girişi", width=20, command=lambda: [giris.destroy(), hasta_ekrani()]).pack(pady=10)
    tk.Button(giris, text="Doktor Girişi", width=20, command=lambda: [giris.destroy(), doktor_ekrani()]).pack(pady=10)
    giris.mainloop()

def hasta_ekrani():
    pencere = tk.Tk()
    pencere.title("Hastane Randevu Sistemi")
    pencere.geometry("500x550")
    pencere.configure(bg="#cce6ff")

    try:
        stetoskop_img = ImageTk.PhotoImage(Image.open("steteskop.png").resize((100, 100)))
        igne_img = ImageTk.PhotoImage(Image.open("igne.png").resize((80, 80)))
    except:
        stetoskop_img = igne_img = None

    if stetoskop_img:
        tk.Label(pencere, image=stetoskop_img, bg="#cce6ff").pack(pady=5)

    tk.Label(pencere, text="Hasta Randevu Paneli", font=("Helvetica", 16, "bold"), bg="#cce6ff", fg="#003366").pack(pady=5)

    tk.Label(pencere, text="Hasta İsmi:", bg="#cce6ff").pack()
    entry_isim = tk.Entry(pencere)
    entry_isim.pack()

    tk.Label(pencere, text="TC Kimlik No:", bg="#cce6ff").pack()
    entry_tc = tk.Entry(pencere)
    entry_tc.pack()

    tk.Label(pencere, text="Randevu Tarihi (GG/AA/YYYY):", bg="#cce6ff").pack()
    entry_tarih = tk.Entry(pencere)
    entry_tarih.pack()

    tk.Label(pencere, text="Doktor Seçin:", bg="#cce6ff").pack()
    doktor_var = tk.StringVar(pencere)
    doktor_menu = tk.OptionMenu(pencere, doktor_var, *[d.isim for d in doktorlar])
    doktor_var.set(doktorlar[0].isim)
    doktor_menu.pack()

    def randevu_al():
        isim = entry_isim.get()
        tc = entry_tc.get()
        tarih = entry_tarih.get()
        secilen_doktor = doktor_var.get()

        if not isim or not tc or not tarih:
            messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
            return

        doktor = next((d for d in doktorlar if d.isim == secilen_doktor), None)

        if doktor and doktor.musait:
            hasta = Hasta(isim, tc)
            randevu = Randevu(tarih, doktor, hasta)
            randevular.append(randevu)
            doktor.musait = False
            messagebox.showinfo("Başarılı", f"{doktor.isim} ile {tarih} tarihinde randevu alındı.")
        else:
            messagebox.showerror("Meşgul", "Doktor şu an müsait değil.")

    def randevu_iptal():
        secilen_doktor = doktor_var.get()
        randevu = next((r for r in randevular if r.doktor.isim == secilen_doktor), None)

        if randevu:
            randevular.remove(randevu)
            randevu.doktor.musait = True
            messagebox.showinfo("İptal Edildi", "Randevu iptal edildi.")
        else:
            messagebox.showwarning("Bulunamadı", "İptal edilecek randevu yok.")

    tk.Button(pencere, text="Randevu Al", command=randevu_al, bg="#004080", fg="white", width=20).pack(pady=5)
    tk.Button(pencere, text="Randevu İptal Et", command=randevu_iptal, bg="#800000", fg="white", width=20).pack(pady=5)

    if igne_img:
        tk.Label(pencere, image=igne_img, bg="#cce6ff").pack(pady=10)

    pencere.mainloop()

def doktor_ekrani():
    pencere = tk.Tk()
    pencere.title("Doktor Paneli")
    pencere.geometry("400x300")
    pencere.configure(bg="#e6f2ff")

    tk.Label(pencere, text="Doktor Paneli", font=("Helvetica", 14, "bold"), bg="#e6f2ff", fg="#003366").pack(pady=10)

    for doktor in doktorlar:
        durum = "Müsait" if doktor.musait else "Meşgul"
        tk.Label(pencere, text=f"{doktor.isim} - {doktor.uzmanlik} - {durum}", bg="#e6f2ff").pack()

    tk.Button(pencere, text="Çık", command=pencere.destroy, bg="#003366", fg="white").pack(pady=20)

    pencere.mainloop()

doktorlar.append(Doktor("Dr. Ayşe Yılmaz", "Kardiyoloji"))
doktorlar.append(Doktor("Dr. Mehmet Demir", "Dahiliye"))
doktorlar.append(Doktor('DR.İhsan Özyavuz','Kulak burun boğaz'))
doktorlar.append(Doktor('DR.Ali Kaya','Beyin cerhhasi'))
giris_ekrani()
