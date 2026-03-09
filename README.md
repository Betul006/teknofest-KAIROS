## **Drone Engelden Kaçış Sistemi (Autonomous Obstacle Avoidance)**
Bu proje, otonom hava araçlarının (İHA) çevresel farkındalığını artırarak, dinamik engelleri gerçek zamanlı algılamasını ve bu engellerden güvenli manevralarla kaçmasını sağlayan uçtan uca bir Yazılım Mimarisi geliştirme sürecini kapsamaktadır. Proje, fiziksel riskleri minimize etmek adına Gazebo 3D Simülasyon ve SITL (Software In The Loop) ortamlarında test edilmektedir.

# Katmanlı Mimari (Layered Architecture)
Proje, modülerliği ve sürdürülebilirliği sağlamak amacıyla 4 ana katman üzerine inşa edilmiştir:

**Infrastructure:** Video kaynaklarının yönetimi (Gazebo & ESP32-CAM), YOLOv8 ve MiDaS entegrasyonu ile uçuş kontrol kartı (MAVLink) iletişimini sağlar.

**Domain:** Nesne tespiti çıktılarının normalize edilmesi, derinlik haritası (Depth Map) füzyonu ve risk analizi gibi projenin temel mantıksal hesaplamalarını içerir.

**Business:** Tüm katmanların koordinasyonunu sağlayan Pipeline Manager, durum makinesi (State Machine) ve hata yönetim mekanizmalarını barındırır.

**Presentation:** Sistemin anlık telemetri verilerini, tespit edilen nesneleri ve risk skorlarını gösteren Tkinter tabanlı bir kontrol panelinden oluşur.

#  Teknik Yetenekler ve İş Akışı
Gerçek Zamanlı Algılama: OpenCV ile yakalanan kareler YOLOv8 modeline aktarılarak engeller tespit edilir.

**Yapay Zeka Destekli Nesne Takibi:** Harici bir kütüphane kullanılmadan, yerleşik takip mekanizmalarıyla nesnelere benzersiz kimlikler (ID) atanır.

**Derinlik Kestirimi (MiDaS):** Tek bir kamera görüntüsü üzerinden MiDaS modeli kullanılarak nesnelerin uzaklık bilgisi (Depth Map) üretilir.

**Matematiksel Risk Analizi:** NumPy tabanlı lineer cebir algoritmalarıyla nesne yaklaşma hızı ve çarpışma olasılığı hesaplanır.

**Otonom Manevra:** Risk eşik değerini aşarsa, PyMavlink üzerinden sanal otopilota kaçış komutları (sağ, sol, orta) gönderilir.

# 👥 Takım ve Görev Dağılımı

**👩‍💻 BETÜL**

Klasör yapısının oluşturulması ve Repo yönetimi.

MiDaS Derinlik Kestirimi ve Derinlik + BBox Füzyonu.

Risk Hesaplama algoritmaları.

State Machine ve Hata Yönetimi (Exception Handling).

Tkinter Kontrol Paneli tasarımı ve Parametre Tuning.

**👩‍💻 ASLIHAN**

Katman sorumluluk matrisinin yazılması ve mimari diyagramın çizilmesi.

Veri Modellerinin oluşturulması.

Mimari Kontrol ve SITL Bağlantı süreçleri.

**👩‍💻 RAVZA**

Pipeline akış dokümanının ve akış şemalarının hazırlanması.

OpenCV & YOLOv8 Entegrasyonu.

Kaçış Yönü Planlama ve Pipeline Manager yönetimi.

Overlay Gösterimi ve Sözleşme Doğrulaması.

Demo senaryoları, engel testleri ve video kayıt süreçleri.

**👨‍💻 YUŞA**

Veri nesnesi sözleşmelerinin belirlenmesi ve örnek veri yapılarının (JSON/Class) oluşturulması.

Nesne Takibi algoritmaları.

Kaçış Yönü Optimizasyonu ve UI Veri Akışı.

Telemetri Verilerinin Okunması.

**👨‍💻 ABDURRAHİM**

Veri Akışı Yönetimi (Gazebo & ESP32-CAM).

Config (Yapılandırma) Yönetimi ve Okuma Fonksiyonları.

Kurtarma Stratejisi geliştirme.

MAVLink → SITL entegrasyonu.

**🛠️ Kurulum ve Kullanım**
Bash
pip install -r requirements.txt






