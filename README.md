# InsiderAutomation
Test Otomasyon Projesi

# InsiderAutomation

Bu proje, [useinsider.com](https://useinsider.com) sitesinin Kariyer ve QA İş ilanları sayfalarının UI test otomasyonunu içermektedir. Python, Selenium WebDriver ve unittest framework ile geliştirilmiştir.

---

## Proje Yapısı

InsiderAutomation/
├── pages/ # Sayfa objeleri (Page Objects)
│ ├── base_page.py
│ ├── home_page.py
│ ├── careers_page.py
│ ├── department_page.py
│ └── joblist_page.py
├── tests/ # Test senaryoları
  └── base_test.py
│ └── test_check_insider_career_qa_jobs.py
├──utils
│    ├── screenshots/ # Test başarısız olursa ekran görüntüleri
└── README.md # Proje açıklaması


---

## Teknolojiler

- Python 3.x  
- Selenium WebDriver  
- unittest (Python'un standart test framework'ü)  
- ChromeDriver  

---

## Kurulum

1. Python 3 yüklü olmalı.  
2. Gerekli paketleri yükle:  
   ```bash
   pip install -r requirements.txt
ChromeDriver sistemde PATH içinde olmalı veya sürücünün yolu testlerde belirtilmeli.

Test Senaryoları
Senaryo 1: Ana Sayfa Açılışı
https://useinsider.com/ adresine gidilir

Ana sayfanın açıldığı doğrulanır

Senaryo 2: Kariyer Sayfasındaki Ana Bölümler Kontrolü
Menüden Company > Careers tıklanır

Location, Teams, Life at Insider bloklarının görünürlüğü kontrol edilir

Senaryo 3: QA İş İlanları Filtreleme
QA kariyer sayfasına gidilir

"See all QA jobs" tıklanır

Lokasyon olarak "Istanbul, Turkiye" seçilir

Departman olarak "Quality Assurance" seçildiği doğrulanır

Senaryo 4: İş İlanı Detayları Doğrulama
Filtre uygulandıktan sonra

Her bir iş ilanının başlık, departman ve lokasyon bilgilerinde doğru değerler olduğu kontrol edilir

Senaryo 5: Başvuru Sayfasına Yönlendirme
"View Role" butonuna tıklanır

Yeni sekmede URL'nin https://jobs.lever.co ile başladığı doğrulanır

Ekran Görüntüleri
Test sırasında hata oluşursa, screenshots/ klasörüne otomatik olarak ekran görüntüsü kaydedilir.


