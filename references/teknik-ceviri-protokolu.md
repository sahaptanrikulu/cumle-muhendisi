# Teknik Çeviri ve Sektörel Terminoloji Protokolü

Teknik metinleri veya yabancı dilden yapılan çevirileri doğallaştırırken en sık düşülen tuzak, sektörde yerleşik teknik terimleri zorla Türkçeleştirmeye çalışmaktır. Bu protokol, dilin akıcılığını sağlarken teknik doğruluğu ve terim bütünlüğünü tavizsiz koruma kurallarını belirler.

---

## 1. Temel İlke

Teknik dilde amaç edebi süsleme yapmak değil; bilgiyi en açık, doğrudan ve standartlara uygun biçimde aktarmaktır. Yapay zeka kalıplarını temizlerken sektörel standart isimleri, test kodları, mühendislik kavramları ve şartname terimleri aynen korunur.

---

## 2. Dokunulmayacak ve Aynen Korunacak Terminoloji

Aşağıdaki ve benzeri uluslararası teknik terimler, standartlar ve kısaltmalar değiştirilemez, kısaltılamaz veya Türkçeleştirilemez:

* **Standart ve Teşkilat Kodları:** SDI, HMMA, ANSI, NFPA (NFPA 80, NFPA 101), IBC, ASTM (ASTM E119, ASTM F1233, ASTM F3038), UL (UL 10C, UL 263, UL 752), ICC 500, FEMA (FEMA 320, FEMA 361), Intertek-ATI, Warnock Hersey.
* **Mühendislik ve İmalat Terimleri:** *fire-rated*, *fire door assembly*, *hollow metal*, *steel door*, *steel frame*, *KD (knock-down) frame*, *welded frame*, *specifier*, *architect*, *egress*, *compartmentalization*, *gasketing*, *thermal break*, *blast-resistant*, *bullet-resistant*, *STC*, *OITC*, *LEED*, *label(ed)*, *listed*, *masonry*, *stud wall*, *drywall*, *glazing*, *sidelight*, *transom*, *shim*, *strike*, *hinge*, *3/4 rule*.
* **Yazılım ve Altyapı Terimleri:** *endpoint*, *deploy*, *middleware*, *queue*, *cache*, *payload*, *pipeline*, *token*, *query*.

> **Açıklama Kuralı:** Eğer terimin Türkçesinin verilmesi şartsa, yalnızca metinde geçtiği ilk yerde parantez içinde kısa bir açıklama eklenir: `fire-rated (yangına dayanıklı)`. Metnin geri kalanında doğrudan orijinal teknik terim kullanılır.

---

## 3. Fonetik Ek Kuralı

Yabancı terimlere gelen çekim ve yapım ekleri, kelimenin yazılışına göre değil, Türkçedeki okunuşuna (fonetiğine) göre kesme işaretiyle ayrılır:

* `cache'i` (keş'i — `cache'ı` değil)
* `queue'yu` (kü'yü — `queue'ya` değil)
* `SQL'i` (es-kü-el'i — `SQL'da` değil)
* `JSON'ı` (ceyson'ı — `JSON'i` değil)
* `GitHub'da` (git-hab'da — `GitHub'de` değil)
* `Node.js'i` (nod-cey-es'i)
* `React'i` (ri-ekt'i)

---

## 4. Cümle İçi Temizlik Kuralları

1. **`-mektedir/-maktadır` Tekdüzeliğini Kır:** Teknik fiillerin doğruluğunu korurken kip çeşitliliği sağla. *"Kapı 3 saat boyunca yangına dayanmaktadır"* yerine *"Kapı 3 saat boyunca yangına dayanır"* ifadesini kullan.
2. **Kof Fiilleri Tasfiye Et:** *"Gerçekleştirmek, sağlamak, katkıda bulunmak, hizmet vermek"* gibi şişkinlikleri at. *"Test işlemi gerçekleştirildi"* yerine *"Test yapıldı"* de.
3. **Metronomik Ritmi Kır:** Teknik şartnamelerde bile art arda 18-20 kelimelik mekanik cümleler yerine, kısa hüküm cümleleriyle ulaçlı teknik bağlamları birlikte kur.
4. **Çeviri Kokusunu Sil:** İngilizce `a/an` kalıntısı olan soyut isim önündeki `"bir"` kelimelerini ve gereksiz `"biz/siz"` zamirlerini temizle.
5. **Tire ve Noktalı Virgül Yasağı:** Gövde metninde uzun tire (`—`) ve noktalı virgül (`;`) kullanma. Standart numaralarında veya aralıklarda TDK standardı kısa tire (`-`) kullan (`A250.8-2017`, `14.00-15.30`).
