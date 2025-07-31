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
<h3 class="code-line" data-line-start=45 data-line-end=46 ><a id="Senaryo_1_Insider_Ana_Sayfasnn_Ald_Dorulanmal_45"></a>Senaryo 1: Insider Ana Sayfasının Açıldığı Doğrulanmalı</h3>
<ol>
<li class="has-line-data" data-line-start="46" data-line-end="47">Tarayıcıda <a href="https://useinsider.com/">https://useinsider.com/</a> adresine gidilir.</li>
<li class="has-line-data" data-line-start="47" data-line-end="49">Sayfa başlığında “Insider” kelimesi geçip geçmediği doğrulanır.</li>
</ol>
<hr>
<h3 class="code-line" data-line-start=51 data-line-end=52 ><a id="Senaryo_2_Kariyer_Sayfas_ve_Ana_Blmlerinin_Grnd_Dorulanmal_51"></a>Senaryo 2: Kariyer Sayfası ve Ana Bölümlerinin Göründüğü Doğrulanmalı</h3>
<ol>
<li class="has-line-data" data-line-start="52" data-line-end="53">Üst menüden <code>Company</code> üzerine hover yapılır.</li>
<li class="has-line-data" data-line-start="53" data-line-end="54">Açılan alt menüden <code>Careers</code> tıklanır.</li>
<li class="has-line-data" data-line-start="54" data-line-end="60">Kariyer sayfasında aşağıdaki bölümlerin görünür olduğu kontrol edilir:
<ul>
<li class="has-line-data" data-line-start="55" data-line-end="56">Locations (Lokasyonlar)</li>
<li class="has-line-data" data-line-start="56" data-line-end="57">Teams (Takımlar)</li>
<li class="has-line-data" data-line-start="57" data-line-end="58">Life at Insider (Insider’da Yaşam)</li>
</ul>
</li>
</ol>
<hr>
<h3 class="code-line" data-line-start=62 data-line-end=63 ><a id="Senaryo_3_QA__lanlar_Lokasyon_ve_Departmana_Gre_Filtrelenmeli_62"></a>Senaryo 3: QA İş İlanları Lokasyon ve Departmana Göre Filtrelenmeli</h3>
<ol>
<li class="has-line-data" data-line-start="63" data-line-end="64"><a href="https://useinsider.com/careers/quality-assurance/">https://useinsider.com/careers/quality-assurance/</a> sayfasına gidilir.</li>
<li class="has-line-data" data-line-start="64" data-line-end="65">“See all QA jobs” butonuna tıklanır.</li>
<li class="has-line-data" data-line-start="65" data-line-end="68">Filtreler uygulanır:
<ul>
<li class="has-line-data" data-line-start="66" data-line-end="67">Location: Istanbul, Turkey</li>
<li class="has-line-data" data-line-start="67" data-line-end="68">Department: Quality Assurance</li>
</ul>
</li>
<li class="has-line-data" data-line-start="68" data-line-end="70">Listelenen tüm iş ilanlarının seçilen lokasyon ve departman bilgisine uygun olduğu doğrulanır.</li>
</ol>
<hr>
<h3 class="code-line" data-line-start=72 data-line-end=73 ><a id="Senaryo_4_Filtre_Sonras__lanlarnn_Detaylar_Dorulanmal_72"></a>Senaryo 4: Filtre Sonrası İş İlanlarının Detayları Doğrulanmalı</h3>
<ol>
<li class="has-line-data" data-line-start="73" data-line-end="74"><a href="https://useinsider.com/careers/quality-assurance/">https://useinsider.com/careers/quality-assurance/</a> sayfasına gidilir.</li>
<li class="has-line-data" data-line-start="74" data-line-end="75">“See all QA jobs” butonuna tıklanır.</li>
<li class="has-line-data" data-line-start="75" data-line-end="78">Filtreler uygulanır:
<ul>
<li class="has-line-data" data-line-start="76" data-line-end="77">Location: All (Tüm Lokasyonlar)</li>
<li class="has-line-data" data-line-start="77" data-line-end="78">Department: Quality Assurance</li>
</ul>
</li>
<li class="has-line-data" data-line-start="78" data-line-end="82">Listelenen her bir iş ilanında:
<ul>
<li class="has-line-data" data-line-start="79" data-line-end="80">Departmanın “Quality Assurance” olduğu,</li>
<li class="has-line-data" data-line-start="80" data-line-end="82">Lokasyonun “Istanbul, Turkey” olduğu doğrulanır.</li>
</ul>
</li>
</ol>
<hr>
<h3 class="code-line" data-line-start=84 data-line-end=85 ><a id="Senaryo_5_Lever__Bavuru_Formuna_Ynlendirme_Dorulanmal_84"></a>Senaryo 5: Lever İş Başvuru Formuna Yönlendirme Doğrulanmalı</h3>
<ol>
<li class="has-line-data" data-line-start="85" data-line-end="86"><a href="https://useinsider.com/careers/quality-assurance/">https://useinsider.com/careers/quality-assurance/</a> sayfasına gidilir.</li>
<li class="has-line-data" data-line-start="86" data-line-end="87">“See all QA jobs” butonuna tıklanır.</li>
<li class="has-line-data" data-line-start="87" data-line-end="90">Filtreler uygulanır:
<ul>
<li class="has-line-data" data-line-start="88" data-line-end="89">Location: All (Tüm Lokasyonlar)</li>
<li class="has-line-data" data-line-start="89" data-line-end="90">Department: Quality Assurance</li>
</ul>
</li>
<li class="has-line-data" data-line-start="90" data-line-end="91">İkinci iş ilanındaki “View Role” butonuna tıklanır.</li>
<li class="has-line-data" data-line-start="91" data-line-end="93">Yeni sekmenin açıldığı ve URL’nin <code>https://jobs.lever.co/useinsider</code> ile başladığı doğrulanır.</li>
</ol>
<p class="has-line-data" data-line-start="93" data-line-end="95">Ekran Görüntüleri<br>
Test sırasında hata oluşursa, screenshots/ klasörüne otomatik olarak ekran görüntüsü kaydedilir.</p>
