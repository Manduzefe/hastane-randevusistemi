# hastane-randevusistemi

1. Temel Tanım
Bu proje, hastaların uygun doktorlardan randevu almasını ve bu randevuları yönetmesini sağlayan bir sistemdir. Python programlama dili ve tkinter arayüz kütüphanesi kullanılarak geliştirilecektir.
2. Temel Sınıfların Tanımlanması
Hasta Sınıfı: Hasta bilgilerini ve geçmiş randevularını tutar.
- Özellikler: isim (str), tc (str), randevu_gecmisi (list)
Doktor Sınıfı: Doktor bilgilerini ve uygunluk durumunu saklar.
- Özellikler: isim (str), uzmanlik (str), musaitlik (list)
Randevu Sınıfı: Bir hasta ile doktor arasında oluşturulan randevuyu temsil eder.
- Özellikler: tarih (str), doktor (Doktor), hasta (Hasta)
3. Randevu Sistemi Fonksiyonları
randevu_al(hasta, doktor, tarih): Hasta için doktorun uygunluk durumuna göre randevu oluşturur.
randevu_iptal(hasta, randevu): Mevcut bir randevuyu iptal eder ve doktorun müsaitlik listesini günceller.
4. Veri Yapıları
- Liste (list): Hasta ve doktor nesnelerini saklamak için.
- Sözlük (dict): TC ile hasta erişimi sağlamak için.
- JSON: Verilerin dosyada kalıcı olarak saklanması.
- datetime/str: Tarih ve saat bilgileri için.
5. Kullanıcı Arayüzü (GUI)
Araçlar: tkinter, customtkinter
Tema: Mavi tonlar, tıbbi ikonlar (steteskop, iğne)
Ekranlar: Giriş, doktor seçimi, randevu takvimi, randevu iptali
6. Kodlama Aşamaları
1. Sınıfların tanımlanması
2. Fonksiyonların yazılması
3. JSON veri kaydetme/yükleme
4. GUI oluşturulması
5. Kullanıcı girdisi ve işlem mantığı
6. Ana döngünün yönetimi
7. Test Etme
- TC ile hasta girişi
- Aynı saate iki randevu alınamaması
- Randevu alındıktan sonra doktorun uygunluk güncellemesi
- Randevu iptali sonrası zaman diliminin serbest kalması
- JSON veri kaydının test edilmesi
8. Kullanım Kılavuzu
1. Programı başlatın: python main.py
2. TC ile giriş yapın: Yeni hasta otomatik eklenir.
3. Doktor ve tarih seçin, Randevu Al butonuna basın.
4. Randevu geçmişi üzerinden iptal işlemi yapılabilir.
