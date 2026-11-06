# Cümle Mühendisi

Cümle Mühendisi, Türkçe metinlerdeki yapay zeka kokusunu, çeviri kuruluğunu ve metronomik tekdüzeliği temizleyip dili gerçek bir insanın elinden çıkmış gibi akıtan açık kaynaklı bir dil mimarisi ve redaksiyon motorudur.

Kelime seviyesinde eşanlamlı aramak yerine, cümlenin taşıyıcı kolonlarına odaklanır. İngilizceden miras kalan sağa dallı cümle iskeletini kırar, Türkçenin kendi kök kuralı olan sola dallanmayı ve zengin ulaç sistemini devreye alır.

---

## Neyi Çözer?

Yapay zeka modellerinin ürettiği Türkçe metinler genellikle ilk bakışta düzgün görünür fakat okunduğunda insanı yoran bir yapaylık taşır:

1. **Sağa Dallanan Cümle Kopyası:** Model, İngilizce düşünerek yan cümleyi ismin sağına ekler (*"Bir yazılım geliştirdik, bu yazılım verileri analiz ediyor"*). Cümle Mühendisi bunu sıfat-fiille sola toplar: *"Verileri analiz eden bir yazılım geliştirdik."*
2. **Metronomik Ritim:** Cümlelerin hemen hepsi 15-20 kelime arasına sıkışır. Bu makine ritmi, kısa ve ulaçlı uzun cümlelerin bir arada kullanılmasıyla kırılır.
3. **Kof Fiil Şişkinliği:** Tek bir güçlü eylemle söylenecek durumlar isim ve yardımcı fiil yığınına çevrilir (*"gerçekleştirmek", "sağlamak", "katkıda bulunmak", "rol oynamak"*). Cümle Mühendisi bu yükleri atıp doğrudan eylemi söyler.
4. **Bürokratik Ek Monotonluğu:** Her cümlenin sonuna yapışan *-mektedir/-maktadır* ekleri temizlenir, yüklem kipleri çeşitlendirilir.
5. **Yapay Noktalama ve Damgalar:** İngilizce metinlerden sızan uzun tireler, yapay üçlemeler ve uygunsuz bağlaç öncesi virgüller bütünüyle ayıklanır.

---

## Temel Mühendislik İlkeleri

* **Olgusal Sadakat Kilidi:** Metni insansı kılacağız diye kaynakta bulunmayan uydurma istatistik, isim, tarih ya da sahte hikaye eklenmez. Gerçek neyse dille o anlatılır.
* **Ulaç (Zarf-Fiil) Sistemi:** Düşünceler refleksif "ve" bağlaçlarıyla art arda dizilmek yerine Türkçenin ulaçlarıyla (`-ıp`, `-ince`, `-dıkça`, `-erek`, `-ken`) birbirine kaynaştırılır.
* **Vurgu Yuvası:** Cümlede öne çıkarılmak istenen fikir yapay vurgu kalıplarıyla değil, yüklemin hemen önüne yerleştirilerek verilir.
* **TDK Standartları:** Saat ve dakikalar iki noktayla değil tek noktayla ayrılır (`14.30`). Saat ekleri son basamağa göre gelir (`13.00'te`). Yüzde işareti sayıdan önce ve boşluksuz yazılır (`%25`). Karşıtlık bağlaçlarından (ama / fakat / ancak) önce veya sonra virgül konmaz.
* **Fonetik Ek Uyumu:** Sektörel yabancı terimler (*endpoint, deploy, cache, fire-rated, queue*) zoraki Türkçeleştirilmez. Terimlere gelen ekler yazılışa göre değil, Türkçedeki okunuşa göre getirilir (`cache'i`, `SQL'i`, `GitHub'da`).

---

## 3 Çalışma Modu

1. **Onarım (`rewrite`):** Mevcut bir Türkçe metni veya çeviriyi alır. Mesajı ve teknik doğruluğu eksiksiz koruyarak cümlenin iskeletini onarır ve yapay zeka damgalarını siler.
2. **Üretim (`write`):** Belirli bir konu veya taslaktan yola çıkarak baştan sona Türkçe cümle mantığıyla metin üretir.
3. **Denetim (`audit`):** Metne müdahale etmeden içindeki yapay zeka sinyallerini, sentaks bozukluklarını ve ritim değerlerini raporlar.

---

## CLI Analiz Aracı

Repo içerisinde bulunan deterministik analiz betiğiyle herhangi bir metin dosyasını terminalden doğrudan denetleyebilirsiniz:

```bash
python scripts/detect_tr_ai.py dosya.txt
```

JSON formatında ayrıntılı çıktı almak için:

```bash
python scripts/detect_tr_ai.py --json metin.md
```

Bu araç metindeki cümle uzunluğu çeşitliliğini (Burstiness CoV), *-mektedir* yoğunluğunu ve kof fiil kullanımlarını saniyeler içinde ölçüp raporlar.

---

## Teşekkür ve Atıf

Bu çalışma sıfırdan ve tek başına ortaya çıkmadı. Arkasında Türkçe dil işleme ve yapay zeka metin kalıpları üzerine kafa yoran üç değerli açık kaynak çalışmanın emeği ve birikimi yatıyor. Onların ortaya koyduğu araştırmalar, kalıp listeleri ve yapısal yaklaşımlar olmasaydı bu sentezi kurmak çok daha zor olurdu.

Kendilerine içtenlikle teşekkür ediyorum:

* **Tahir Yıldız ([tahiryildiz/insanca](https://github.com/tahiryildiz/insanca)):** Çıkardığı 48 içerik ve üslup kalıbı, 25 ritim kuralı ve dedektör tersine mühendisliği analizleriyle bu projenin temel taşını oluşturdu.
* **Büşra Beggi ([bushrabeg/turkce-humanizer](https://github.com/bushrabeg/turkce-humanizer)):** Geliştirdiği iki fazlı mimari, 5 mutlak yasak kuralı, register sınıflandırması ve yazar profili yaklaşımıyla sistemin çerçevesini zenginleştirdi.
* **Yüce Zerey ([yucezerey/turkish-anti-ai-skill](https://github.com/yucezerey/turkish-anti-ai-skill)):** Sola dallanma sentaksı, ulaç sistemi, TDK tipografi ilkeleri, fonetik ek kuralları ve deterministik CLI tarayıcısıyla projenin sentaks ve analiz omurgasını kurdu.

---

## Lisans

Bu proje MIT Lisansı altında sunulur. Ayrıntılar için `LICENSE` dosyasına bakabilirsiniz.
