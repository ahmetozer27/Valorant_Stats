# Valorant Stats Python Client

Bu proje, Riot Games'in Valorant API'lerini kullanarak oyuncu maç geçmişi, maç detayları ve oyuncu bilgilerini çekmek amacıyla geliştirilmiş modüler bir Python kütüphanesidir.

---

## 🚀 Proje Amacı

Bu proje, **mobil uygulama geliştirme sürecinde test ve prototip aşaması** için hazırlanmıştır.  
Mobil uygulama Valorant oyuncularına; maç analizleri, performans takibi ve oyuncu eşleştirme gibi özellikler sunmayı hedeflemektedir.  
Python tarafı ise Riot API'lerinden veri çekme ve işleme görevlerini üstlenmektedir.

---

## 📁 Proje Klasör ve Dosya Yapısı

```plaintext
valorant_stats/
├── main.py                  # Uygulamanın ana giriş noktası, kullanıcıdan Riot ID alıp maç detaylarını gösterir
├── config.py                # API anahtarı ve genel konfigürasyon ayarları
├── services/                # Riot API isteklerini gerçekleştiren modüller
│   ├── __init__.py          # Paket tanımlama dosyası (boş bırakılabilir)
│   ├── riot_account.py      # Riot ID'den PUUID alma işlemleri
│   ├── match_history.py     # PUUID ile maç listesi çekme fonksiyonları
│   └── match_detail.py      # Belirli maç ID'si ile maç detaylarını getiren fonksiyonlar
└── utils/                   # Yardımcı genel fonksiyon ve HTTP istek modülleri
    ├── __init__.py          # Paket tanımlama dosyası (boş bırakılabilir)
    └── http_client.py       # requests ile HTTP GET istekleri yapmayı sağlayan genel fonksiyon
