Services
Documents
InsiderAutomation.md
Preview as 
Export as 
Save to 
Import from 
Document Name
InsiderAutomation.md
MarkdownPreviewToggle Mode
  
<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="InsiderAutomation_0"></a>InsiderAutomation</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2">Test Otomasyon Projesi</p>
<h1 class="code-line" data-line-start=3 data-line-end=4 ><a id="InsiderAutomation_3"></a>InsiderAutomation</h1>
<p class="has-line-data" data-line-start="5" data-line-end="6">Bu proje, <a href="https://useinsider.com">useinsider.com</a> sitesinin Kariyer ve QA İş ilanları sayfalarının UI test otomasyonunu içermektedir. Python, Selenium WebDriver ve unittest framework ile geliştirilmiştir.</p>
<hr>
<h2 class="code-line" data-line-start=9 data-line-end=10 ><a id="Proje_Yaps_9"></a>Proje Yapısı</h2>
<p class="has-line-data" data-line-start="11" data-line-end="24">InsiderAutomation/<br>
├── pages/ # Sayfa objeleri (Page Objects)<br>
│ ├── base_page.py<br>
│ ├── home_page.py<br>
│ ├── careers_page.py<br>
│ ├── department_page.py<br>
│ └── joblist_page.py<br>
├── tests/ # Test senaryoları<br>
└── base_test.py<br>
│ └── test_check_insider_career_qa_jobs.py<br>
├──utils<br>
│    ├── screenshots/ # Test başarısız olursa ekran görüntüleri<br>
└── <a href="http://README.md">README.md</a> # Proje açıklaması</p>
<hr>
<h2 class="code-line" data-line-start=28 data-line-end=29 ><a id="Teknolojiler_28"></a>Teknolojiler</h2>
<ul>
<li class="has-line-data" data-line-start="30" data-line-end="31">Python 3.x</li>
<li class="has-line-data" data-line-start="31" data-line-end="32">Selenium WebDriver</li>
<li class="has-line-data" data-line-start="32" data-line-end="33">unittest (Python’un standart test framework’ü)</li>
<li class="has-line-data" data-line-start="33" data-line-end="35">ChromeDriver</li>
</ul>
<hr>
<h2 class="code-line" data-line-start=37 data-line-end=38 ><a id="Kurulum_37"></a>Kurulum</h2>
<ol>
<li class="has-line-data" data-line-start="39" data-line-end="40">Python 3 yüklü olmalı.</li>
<li class="has-line-data" data-line-start="40" data-line-end="43">Gerekli paketleri yükle:<pre><code class="has-line-data" data-line-start="42" data-line-end="43" class="language-bash">pip install -r requirements.txt
</code></pre>
</li>
</ol>
<p class="has-line-data" data-line-start="43" data-line-end="44">ChromeDriver sistemde PATH içinde olmalı veya sürücünün yolu testlerde belirtilmeli.</p>
<p class="has-line-data" data-line-start="45" data-line-end="48">Test Senaryoları<br>
Senaryo 1: Ana Sayfa Açılışı<br>
<a href="https://useinsider.com/">https://useinsider.com/</a> adresine gidilir</p>
<p class="has-line-data" data-line-start="49" data-line-end="50">Ana sayfanın açıldığı doğrulanır</p>
<p class="has-line-data" data-line-start="51" data-line-end="53">Senaryo 2: Kariyer Sayfasındaki Ana Bölümler Kontrolü<br>
Menüden Company &gt; Careers tıklanır</p>
<p class="has-line-data" data-line-start="54" data-line-end="55">Location, Teams, Life at Insider bloklarının görünürlüğü kontrol edilir</p>
<p class="has-line-data" data-line-start="56" data-line-end="58">Senaryo 3: QA İş İlanları Filtreleme<br>
QA kariyer sayfasına gidilir</p>
<p class="has-line-data" data-line-start="59" data-line-end="60">“See all QA jobs” tıklanır</p>
<p class="has-line-data" data-line-start="61" data-line-end="62">Lokasyon olarak “Istanbul, Turkiye” seçilir</p>
<p class="has-line-data" data-line-start="63" data-line-end="64">Departman olarak “Quality Assurance” seçildiği doğrulanır</p>
<p class="has-line-data" data-line-start="65" data-line-end="67">Senaryo 4: İş İlanı Detayları Doğrulama<br>
Filtre uygulandıktan sonra</p>
<p class="has-line-data" data-line-start="68" data-line-end="69">Her bir iş ilanının başlık, departman ve lokasyon bilgilerinde doğru değerler olduğu kontrol edilir</p>
<p class="has-line-data" data-line-start="70" data-line-end="72">Senaryo 5: Başvuru Sayfasına Yönlendirme<br>
“View Role” butonuna tıklanır</p>
<p class="has-line-data" data-line-start="73" data-line-end="74">Yeni sekmede URL’nin <a href="https://jobs.lever.co">https://jobs.lever.co</a> ile başladığı doğrulanır</p>
<p class="has-line-data" data-line-start="75" data-line-end="77">Ekran Görüntüleri<br>
Test sırasında hata oluşursa, screenshots/ klasörüne otomatik olarak ekran görüntüsü kaydedilir.</p>
