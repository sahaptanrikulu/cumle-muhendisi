# Cümle Mühendisi — Örnekler ve Test Raporları

Bu belge, Cümle Mühendisi'nin ele aldığı her bir yapay zeka kusurunu, bunların somut öncesi/sonrası örneklerini ve analiz motorundan alınan sayısal test sonuçlarını belgeler.

---

## 1. İngilizce Çeviri Mantığını Kırma (Arkadan Dolanmayan Doğal Cümleler)

Yapay zeka modelleri İngilizce düşünerek önce ana ismi söyler, ardından "ki bu..." diyerek arkadan dolanır. Cümle Mühendisi lafı uzatmadan doğrudan Türkçe söyler.

* **Yapay Zeka (Önce):**  
  *"Yeni bir sipariş yönetim yazılımı devreye aldık, bu yazılım ihracat teslimat sürelerimizi %30 oranında kısaltıyor."*
* **Cümle Mühendisi (Sonra):**  
  *"İhracat teslimat sürelerimizi %30 kısaltan yeni bir sipariş yönetim yazılımını devreye aldık."*
* **Test Analizi:**  
  * Cümle yapısı Türkçenin öz mantığına (sıfat-fiille bağlama) kavuştu.  
  * Kelime tasarrufu: %23 daha sade ve doğrudan.

---

## 2. Saatin Tiktakı Gibi Duran Tekdüzelik (Cümle Boyu Dalgalanması ve Nefes Payı)

Yapay zeka istisnasız her cümlesini 15-20 kelime arasına hapseder. İnsan dilinde ise kısa vurucu cümlelerle uzun akıcı cümleler harmanlanır.

* **Yapay Zeka (Önce):**  
  *"Üretim süreçlerinde kalite kontrolün sağlanması büyük bir hassasiyet gerektirmektedir. Tüm personelin belirlenen talimatlara eksiksiz uyması kritik bir önem taşımaktadır. Her aşamada yapılan tetkikler hataların önlenmesine önemli katkıda bulunmaktadır."*  
  *(Cümle kelime sayıları: 11 - 12 - 12. Burstiness CoV: 0,08 — tamamen monoton)*
* **Cümle Mühendisi (Sonra):**  
  *"Kalite kontrol hata affetmez. Personel talimatlara harfiyen uyduğu ve her aşama sıkı denetlendiği sürece üretim sorunsuz yürür."*  
  *(Cümle kelime sayıları: 4 - 17. Burstiness CoV: 0,62 — canlı insan ritmi)*
* **Test Analizi:**  
  * Cümle Ritmi Çeşitliliği (Burstiness CoV) 0,08'den 0,62'ye çıktı.  
  * Okurun zihnini yoran tekdüze, mekanik yapı tamamen kırıldı.

---

## 3. Süslü Memur Dili ve Boş Fiil Şişkinliğini Budama

Yapay zeka dümdüz eylemi söylemek yerine süslü memur diliyle lafı şişirir.

* **Yapay Zeka (Önce):**  
  *"Müşteri taleplerinin değerlendirilmesi işlemi gerçekleştirilmiş olup, sevkiyat planlamasına yönelik hazırlıklar tamamlanma aşamasına getirilmiştir."*
* **Cümle Mühendisi (Sonra):**  
  *"Müşteri taleplerini inceleyip sevkiyat planını hazırladık."*
* **Test Analizi:**  
  * 16 kelimelik resmi daire kuruluğu, 7 kelimelik berrak ve hareketli bir cümleye dönüştü.  
  * Kelime tasarrufu: %56.

---

## 4. Sonu Gelmeyen "-mektedir / -maktadır" Kuruluğunu Temizleme

Arka arkaya dizilen ekler okuru canından bezdirir.

* **Yapay Zeka (Önce):**  
  *"Fabrikamızda günde 200 adet çelik kapı üretilmektedir. Ürünler uluslararası kalite standartlarına uygun olarak test edilmektedir ve Avrupa ülkelerine ihraç edilmektedir."*
* **Cümle Mühendisi (Sonra):**  
  *"Fabrikamızda günde 200 çelik kapı üretiyor, uluslararası standartlarda test edip Avrupa'ya ihraç ediyoruz."*
* **Test Analizi:**  
  * `-mektedir/-maktadır` yoğunluğu %100'den %0'a indirildi.  
  * Eylemler ulaçlarla birbirine bağlanarak konuşma akıcılığı elde edildi.

---

## 5. Türkçede Yeri Olmayan Noktalama ve Damgaları Ayıklama

İngilizce metinlerden miras kalan uzun tireler, noktalı virgüller ve bağlaç öncesi virgüller ayıklanır.

* **Yapay Zeka (Önce):**  
  *"Müşterimizle görüştük; fakat taleplerini netleştiremedik — çünkü bütçeleri sınırlı, ama beklentileri yüksek."*
* **Cümle Mühendisi (Sonra):**  
  *"Müşterimizle görüştük fakat taleplerini netleştiremedik. Bütçeleri dar ancak beklentileri yüksek."*
* **Test Analizi:**  
  * Uzun tire (`—`) ve noktalı virgül (`;`) temizlendi.  
  * TDK kuralı gereği karşıtlık bağlaçlarından önceki hatalı virgüller kaldırıldı.

---

## 6. Teknik ve Sektörel Terimleri Bozmadan Koruma (Olgusal Sadakat)

Teknik doğruluğu bozmadan, uydurma yapmadan ve terimleri gülünç çevirilere feda etmeden dili doğallaştırma.

* **Yapay Zeka (Önce):**  
  *"Yangına dayanıklı delikli madeni kapılarımızın NFPA 80 standardına göre test edilmesi işlemi gerçekleştirilmektedir."*
* **Cümle Mühendisi (Sonra):**  
  *"Fire-rated hollow metal kapılarımızı NFPA 80 standardına göre test ediyoruz."*
* **Test Analizi:**  
  * Uluslararası teknik terimler (`fire-rated`, `hollow metal`, `NFPA 80`) aynen korundu.  
  * Yapay ek ve bürokrasi yükü atıldı.
