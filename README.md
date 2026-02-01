# Hareketli Hava Aracı Takip ve Otomatik Anten Yönlendirme Sistemi

Bu repo, **havada hareket eden bir aracı (İHA / drone / hava platformu)** sürekli takip ederek, **yer istasyonu ile araç arasındaki haberleşme bağlantısının kopmasını önlemeyi** amaçlayan bir sistemin geliştirilmesini içermektedir.

Sistem, **araçtan gerçek zamanlı olarak alınan konum verilerini** kullanarak, yer istasyonundaki **antenin otomatik olarak aracın bulunduğu yöne dönmesini** sağlar.
Bu sayede **kesintisiz veri akışı**, uzun menzilli ve kararlı haberleşme mümkün hale gelmiştir.

## Problemin Tanımı

Hareketli hava araçlarında:
- Araç yön değiştirdikçe anten görüş açısı kaybolabilir
- Özellikle yönlü antenlerde:
 - Bağlantı zayıflar
 - Paket kayıpları artar
 - Telemetri ve veri akışı kesintiye uğrar

Bu durum:

- Otonom görevleri
- Canlı video aktarımını
- Kritik telemetri verilerini

doğrudan riske sokmaktadır.

## Geliştirilen Çözüm

Bu projede, Python kullanılarak geliştirilen bir takip sistemi ile:

- Araçtan sürekli konum bilgisi alınır
- Araç–yer istasyonu arasındaki göreceli yön (bearing) hesaplanır
- Anten, aracın hareket yönüne gerçek zamanlı olarak döndürülür
- Bağlantı hattı sürekli aktif tutulur

Sistem, aracın manevralarına dinamik olarak adapte olur ve manuel müdahale gerektirmez.

## Sistem Mimarisi

Genel yapı aşağıdaki adımlardan oluşur:

1. Hava aracından:

- Enlem (Latitude)

- Boylam (Longitude)

- İrtifa (opsiyonel)
bilgileri alınır

2. Yer istasyonunun sabit konumu referans alınır

3. Araç ile yer istasyonu arasındaki:

- Yön açısı (azimuth)

- Gerekirse yükseklik açısı (elevation) hesaplanır

4. Anten:

- Hesaplanan açıya doğru otomatik olarak yönlendirilir

5. Veri bağlantısı:

- Sürekli ve kararlı şekilde korunur


## Öne Çıkan Özellikler

- 📡 Otomatik anten yönlendirme

- 🛰️ Gerçek zamanlı konum takibi

- 🔄 Araç yön değiştirdikçe dinamik güncelleme

- 📶 Bağlantı kopmalarının önlenmesi

- 🐍 Python tabanlı, modüler yapı

- 🔧 Donanımdan bağımsız algoritma yapısı


## Kullanım Senaryoları

Bu sistem özellikle aşağıdaki alanlarda kullanılabilir:

- İHA yer kontrol istasyonları

- Uzun menzilli telemetri sistemleri

- Canlı video aktarımı (FPV / ISR)

- Otonom görev ve takip sistemleri

- Savunma & havacılık haberleşme çözümleri

## Neden Python?

Python tercih edilme sebepleri:

- Hızlı prototipleme

- Matematiksel ve trigonometrik hesaplarda esneklik

- Donanım ve haberleşme kütüphaneleriyle kolay entegrasyon

- Görüntü işleme ve otonomi sistemleriyle uyumluluk

## Sistem Davranışı (Özet)

- Araç ileri yönde hareket ettiğinde anten aynı doğrultuda döner

- Araç yön değiştirirse:

 - Anten yeni yönü takip eder

- Araç sabitlenirse:

 - Anten konumunu korur

- Veri akışı:

 - Kopmadan devam eder

Bu yapı sayesinde manuel anten ayarlama ihtiyacı tamamen ortadan kaldırılmıştır.

## Teknik Notlar

- Sistem, araçtan gelen konum verisinin sürekliliğine bağlıdır

- Yüksek güncelleme frekansı, daha hassas takip sağlar

- Anten mekanik sınırları yazılımsal olarak dikkate alınabilir

- Simülasyon ortamında test edilmesi önerilir

## Geliştirilebilir Alanlar

- Filtreleme (Kalman / düşük geçiren filtre)

- Anten dönüş hızına ivme sınırlaması

- Çoklu araç takibi

- VTOL / sabit kanat senaryoları için optimizasyon

- Görsel arayüz (GUI) entegrasyonu


