from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    malzemeler = [
        {"isim": "Domates", "resim": "domates.png"},
        {"isim": "Patates", "resim": "patates.png"},
        {"isim": "Soğan", "resim": "sogan.png"},
        {"isim": "Biber", "resim": "biber.png"},
    ]
    return render_template("index.html", malzemeler=malzemeler)

if __name__ == "__main__":
    app.run(debug=True)
    # 🍽️ Yemek Tarifi Sitesi

<div class="malzeme-container">
  {% for m in malzemeler %}
    <div class="malzeme-kart">
      <img src="{{ url_for('static', filename='images/' + m.resim) }}" alt="{{ m.isim }}">
      <p>{{ m.isim }}</p>
    </div>
  {% endfor %}
</div>

<style>
.malzeme-container {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: center;
}

.malzeme-kart {
  width: 120px;
  text-align: center;
  cursor: pointer;
}

.malzeme-kart img {
  width: 100px;
  height: 100px;
  object-fit: cover;
}
</style>

Bu projede farklı kategorilerde yemek tarifleri bulunmaktadır.

## 📚 Tarifler

### 🍲 Çorbalar
- [Mercimek Çorbası](recipes/corbalar/mercimek-corbasi.md)
- [Domates Çorbası](recipes/corbalar/domates-corbasi.md)
- [Yayla Çorbası](recipes/corbalar/yayla-corbasi.md)
- [Ezogelin Çorbası](recipes/corbalar/ezogelin-corbasi.md)

### 🍲 Ana Yemekler
- [Karnıyarık](recipes/ana-yemekler/karniyarik.md)
- [Kuru Fasulye](recipes/ana-yemekler/kuru-fasulye.md)
- [Tas Kebabı](recipes/ana-yemekler/tas-kebabi.md)
- [Fırında Tavuk Patates](recipes/ana-yemekler/firinda-tavuk-patates.md)
- [Zeytinyağlı Taze Fasulye](recipes/ana-yemekler/zeytinyagli-taze-fasulye.md)
- [Kremalı Mantarlı Makarna (Hızlı Tarif)](recipes/ana-yemekler/kremali-mantarli-makarna.md)
- [Domates Soslu Makarna (Vegan)](recipes/ana-yemekler/domates-soslu-makarna.md)

### Tatlılar
- [Sütlaç](recipes/tatlilar/sutlac.md)
- [Islak Kek](recipes/tatlilar/islak-kek.md)
- [Cheesecake](recipes/tatlilar/cheesecake.md)
- [Magnolia](recipes/tatlilar/magnolia.md)
- [Bisküvili Soğuk Pasta](recipes/tatlilar/biskuvili-soguk-pasta.md)
- [Vegan Çikolatalı Puding](recipes/tatlilar/vegan-cikolatali-puding.md)


    # 🍝 Domates Soslu Makarna (Vegan)

## 📝 Tarif Bilgileri
- **Kategori:** Spesiyal / Hızlı / Vegan
- **Hazırlık Süresi:** 5 dakika
- **Pişirme Süresi:** 15 dakika
- **Porsiyon:** 2 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 1 paket makarna
- 3 adet domates (rendelenmiş)
- 2 yemek kaşığı zeytinyağı
- 1 diş sarımsak
- 1 çay kaşığı tuz
- 1 çay kaşığı kekik

## 👨‍🍳 Yapılışı
1. Makarnayı tuzlu suda haşlayın.
2. Sarımsağı zeytinyağında kavurun.
3. Rendelenmiş domatesleri ekleyin.
4. Sos koyulaşınca baharatları ekleyin.
5. Makarnayı sosla karıştırıp 2–3 dakika pişirin.

## 💡 Servis Önerisi
Taze fesleğen ile servis edebilirsiniz.

# 🍗 Fırında Tavuk Patates

## 📝 Tarif Bilgileri
- **Kategori:** Ana Yemek
- **Hazırlık Süresi:** 15 dakika
- **Pişirme Süresi:** 45 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 1 kg tavuk but veya baget
- 4 adet patates
- 2 yemek kaşığı zeytinyağı
- 1 tatlı kaşığı tuz
- 1 çay kaşığı karabiber
- 1 çay kaşığı kırmızı toz biber

## 👨‍🍳 Yapılışı
1. Tavukları ve patatesleri doğrayın.
2. Baharatlar ve zeytinyağı ile harmanlayın.
3. Fırın tepsisine dizin.
4. 180°C fırında 45 dakika pişirin.

## 💡 Servis Önerisi
Yanında mevsim salatası ile servis edebilirsiniz.

# 🍆 Karnıyarık

## 📝 Tarif Bilgileri
- **Kategori:** Ana Yemek
- **Hazırlık Süresi:** 20 dakika
- **Pişirme Süresi:** 30 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Orta

## 🛒 Malzemeler
- 4 adet patlıcan
- 200 g kıyma
- 1 adet soğan
- 2 adet yeşil biber
- 1 adet domates
- 2 yemek kaşığı sıvı yağ
- 1 tatlı kaşığı tuz
- 1 çay kaşığı karabiber

## 👨‍🍳 Yapılışı
1. Patlıcanları alacalı soyup kızartın.
2. Soğanı ve biberi yağda kavurun.
3. Kıymayı ekleyip pişirin.
4. Domates ve baharatları ekleyin.
5. Patlıcanların içine harcı doldurun.
6. Fırında 180°C’de 30 dakika pişirin.

## 💡 Servis Önerisi
Pirinç pilavı ve cacık ile servis edebilirsiniz.

# 🍝 Kremalı Mantarlı Makarna

## 📝 Tarif Bilgileri
- **Kategori:** Spesiyal / Hızlı Yemek
- **Hazırlık Süresi:** 5 dakika
- **Pişirme Süresi:** 15 dakika
- **Porsiyon:** 2 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 1 paket makarna
- 200 ml krema
- 200 g mantar
- 1 yemek kaşığı zeytinyağı
- 1 çay kaşığı tuz
- 1 çay kaşığı karabiber

## 👨‍🍳 Yapılışı
1. Makarnayı tuzlu suda haşlayın.
2. Mantarları zeytinyağında soteleyin.
3. Kremayı ekleyip karıştırın.
4. Haşlanan makarnayı sosun içine alın.
5. 2–3 dakika birlikte pişirin.

## 💡 Servis Önerisi
Üzerine parmesan peyniri ekleyebilirsiniz.

# 🫘 Kuru Fasulye

## 📝 Tarif Bilgileri
- **Kategori:** Ana Yemek
- **Hazırlık Süresi:** 15 dakika
- **Pişirme Süresi:** 40 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Orta

## 🛒 Malzemeler
- 2 su bardağı kuru fasulye
- 1 adet soğan
- 1 yemek kaşığı domates salçası
- 2 yemek kaşığı sıvı yağ
- 1 tatlı kaşığı tuz
- 6 su bardağı su

## 👨‍🍳 Yapılışı
1. Kuru fasulyeyi bir gece önceden ıslatın.
2. Soğanı yağda kavurun.
3. Salçayı ekleyip karıştırın.
4. Fasulyeleri ve suyu ekleyin.
5. Yumuşayana kadar pişirin.

## 💡 Servis Önerisi
Pilav ve turşu ile servis edebilirsiniz.

## 📝 Tarif Bilgileri
- **Kategori:** Ana Yemek
- **Hazırlık Süresi:** 20 dakika
- **Pişirme Süresi:** 45 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Orta

## 🛒 Malzemeler
- 500 g kuşbaşı et
- 1 adet soğan
- 2 yemek kaşığı sıvı yağ
- 1 tatlı kaşığı tuz
- 5 su bardağı su

## 👨‍🍳 Yapılışı
1. Etleri yağda kavurun.
2. Soğanı ekleyip kavurmaya devam edin.
3. Suyunu ekleyip kısık ateşte pişirin.
4. Etler yumuşayınca ocaktan alın.

## 💡 Servis Önerisi
Pilav veya bulgur pilavı ile servis edebilirsiniz.

# 🫒 Zeytinyağlı Taze Fasulye

## 📝 Tarif Bilgileri
- **Kategori:** Ana Yemek (Zeytinyağlı)
- **Hazırlık Süresi:** 20 dakika
- **Pişirme Süresi:** 35 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 500 g taze fasulye
- 2 adet domates
- 1 adet soğan
- 3 yemek kaşığı zeytinyağı
- 1 çay kaşığı tuz
- 1 su bardağı su

## 👨‍🍳 Yapılışı
1. Taze fasulyelerin uçlarını alıp doğrayın.
2. Soğanı zeytinyağında kavurun.
3. Domatesleri ekleyip pişirin.
4. Fasulyeleri ve suyu ekleyin.
5. Kısık ateşte 30–35 dakika pişirin.

## 💡 Servis Önerisi
Ilık veya soğuk olarak servis edebilirsiniz.

# 🍅 Domates Çorbası

## 📝 Tarif Bilgileri
- **Kategori:** Çorba
- **Hazırlık Süresi:** 10 dakika
- **Pişirme Süresi:** 20 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 4 adet domates (rendelenmiş)
- 1 yemek kaşığı tereyağı
- 1 yemek kaşığı un
- 4 su bardağı su
- 1 çay kaşığı tuz
- 1 çay bardağı süt

## 👨‍🍳 Yapılışı
1. Tereyağını tencerede eritin.
2. Unu ekleyip kokusu çıkana kadar kavurun.
3. Rendelenmiş domatesleri ekleyin.
4. Suyu ilave edip 15–20 dakika pişirin.
5. Sütü ekleyip karıştırın.

## 💡 Servis Önerisi
Üzerine rendelenmiş kaşar peyniri serperek servis edebilirsiniz.

# 🍲 Ezogelin Çorbası

## 📝 Tarif Bilgileri
- **Kategori:** Çorba
- **Hazırlık Süresi:** 15 dakika
- **Pişirme Süresi:** 25 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Orta

## 🛒 Malzemeler
- 1 çay bardağı kırmızı mercimek
- 1 çay bardağı ince bulgur
- 1 çay bardağı pirinç
- 1 adet soğan
- 1 yemek kaşığı domates salçası
- 1 tatlı kaşığı biber salçası
- 2 yemek kaşığı zeytinyağı
- 6 su bardağı su
- 1 çay kaşığı tuz
- 1 çay kaşığı pul biber
- 1 çay kaşığı nane

## 👨‍🍳 Yapılışı
1. Soğanı küçük doğrayıp zeytinyağında kavurun.
2. Salçaları ekleyip karıştırın.
3. Yıkanmış mercimek, bulgur ve pirinci ekleyin.
4. Suyu ilave edip orta ateşte pişirin.
5. Malzemeler yumuşayınca tuz ve baharatları ekleyin.
6. 5 dakika daha kaynatıp ocaktan alın.

## 💡 Servis Önerisi
Üzerine limon sıkarak sıcak servis edebilirsiniz.

# Mercimek Çorbası




## 📋 Tarif Bilgileri

- **Kategori:** Çorba
- **Hazırlık Süresi:** 10 dakika
- **Pişirme Süresi:** 25 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 1 su bardağı kırmızı mercimek
- 1 adet soğan
- 1 adet havuç
- 1 yemek kaşığı salça
- 1 tatlı kaşığı tuz
- 5 su bardağı su
- 2 yemek kaşığı sıvı yağ

## 👩‍🍳 Yapılışı
1. Soğanı ve havucu küçük küçük doğrayın.
2. Tencereye sıvı yağı alın ve soğanları kavurun.
3. Salçayı ekleyip karıştırın.
4. Mercimek, havuç ve suyu ekleyin.
5. Kaynadıktan sonra kısık ateşte 20-25 dakika pişirin.
6. Blenderdan geçirip sıcak servis edin.

## 💡 Püf Noktaları
- Blenderdan sonra kıvam koyu gelirse sıcak su ekleyebilirsiniz.
- Üzerine tereyağlı pul biber sosu çok yakışır.

# 🥣 Yayla Çorbası

## 📝 Tarif Bilgileri
- **Kategori:** Çorba
- **Hazırlık Süresi:** 10 dakika
- **Pişirme Süresi:** 20 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 1 su bardağı yoğurt
- 1 yemek kaşığı un
- 1 adet yumurta sarısı
- 3 su bardağı su
- 1 çay bardağı haşlanmış pirinç
- 1 çay kaşığı tuz

### 🔥 Üzeri için
- 1 yemek kaşığı tereyağı
- 1 çay kaşığı nane

## 👨‍🍳 Yapılışı
1. Yoğurt, un ve yumurta sarısını bir kapta çırpın.
2. Suyu yavaş yavaş ekleyerek karıştırın.
3. Karışımı tencereye alıp kısık ateşte sürekli karıştırarak pişirin.
4. Kaynayınca pirinci ve tuzu ekleyin.
5. Ayrı tavada tereyağını eritip naneyi ekleyin.
6. Çorbanın üzerine gezdirerek servis edin.

## 💡 Servis Önerisi
Sıcak olarak, limon dilimiyle servis edebilirsiniz.

# ❄️ Bisküvili Soğuk Pasta

## 📝 Tarif Bilgileri
- **Kategori:** Soğuk Tatlı
- **Hazırlık Süresi:** 20 dakika
- **Pişirme Süresi:** Yok
- **Porsiyon:** 6 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 1 paket petibör bisküvi
- 2 su bardağı süt
- 1 paket kakaolu puding
- 1 paket krem şanti

## 👨‍🍳 Yapılışı
1. Puding ve sütü pişirip soğumaya bırakın.
2. Krem şantiyi hazırlayın.
3. Bisküvi, puding ve krem şantiyi kat kat dizin.
4. Buzdolabında 2 saat dinlendirin.

## 💡 Servis Önerisi
Üzerine kakao serpebilirsiniz.

    # 🍰 Cheesecake

## 📝 Tarif Bilgileri
- **Kategori:** Tatlı
- **Hazırlık Süresi:** 20 dakika
- **Pişirme Süresi:** 50 dakika
- **Porsiyon:** 8 kişilik
- **Zorluk:** Orta

## 🛒 Malzemeler
- 200 g yulaflı bisküvi
- 100 g tereyağı
- 400 g labne peyniri
- 1 su bardağı şeker
- 2 adet yumurta
- 1 paket vanilin

## 👨‍🍳 Yapılışı
1. Bisküvileri rondodan geçirin.
2. Eritilmiş tereyağı ile karıştırıp kalıba bastırın.
3. Labne, şeker, yumurta ve vanilini karıştırın.
4. Karışımı kalıba dökün.
5. 160°C fırında 50 dakika pişirin.

## 💡 Servis Önerisi
Üzerine frambuaz sosu ile servis edebilirsiniz.

# 🍫 Islak Kek

## 📝 Tarif Bilgileri
- **Kategori:** Tatlı
- **Hazırlık Süresi:** 15 dakika
- **Pişirme Süresi:** 30 dakika
- **Porsiyon:** 6 kişilik
- **Zorluk:** Orta

## 🛒 Malzemeler
- 3 adet yumurta
- 1 su bardağı şeker
- 1 su bardağı süt
- 2 yemek kaşığı kakao
- 1 paket kabartma tozu
- 1,5 su bardağı un

## 👨‍🍳 Yapılışı
1. Yumurta ve şekeri çırpın.
2. Diğer malzemeleri ekleyin.
3. Fırında 180°C’de 30 dakika pişirin.

## 💡 Servis Önerisi
Üzerine çikolata sosu dökebilirsiniz.

# 🍓 Magnolia

## 📝 Tarif Bilgileri
- **Kategori:** Tatlı
- **Hazırlık Süresi:** 15 dakika
- **Pişirme Süresi:** 10 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 1 litre süt
- 1 su bardağı şeker
- 2 yemek kaşığı nişasta
- 1 paket vanilin
- 1 paket bebe bisküvisi
- Çilek veya muz

## 👨‍🍳 Yapılışı
1. Süt, şeker ve nişastayı pişirin.
2. Vanilini ekleyip soğumaya bırakın.
3. Bisküvi ve meyvelerle kat kat dizin.

## 💡 Servis Önerisi
Soğuk servis ediniz.

# 🍮 Sütlaç

## 📝 Tarif Bilgileri
- **Kategori:** Tatlı
- **Hazırlık Süresi:** 10 dakika
- **Pişirme Süresi:** 25 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 1 litre süt
- 1 çay bardağı pirinç
- 1 su bardağı toz şeker
- 1 paket vanilin

## 👨‍🍳 Yapılışı
1. Pirinci haşlayın.
2. Sütü ekleyip kaynatın.
3. Şekeri ekleyip karıştırın.
4. Vanilini ekleyip ocaktan alın.

## 💡 Servis Önerisi
Üzerine tarçın serpebilirsiniz.

# 🌱 Vegan Çikolatalı Puding

## 📝 Tarif Bilgileri
- **Kategori:** Tatlı / Vegan / Soğuk
- **Hazırlık Süresi:** 5 dakika
- **Pişirme Süresi:** 10 dakika
- **Porsiyon:** 4 kişilik
- **Zorluk:** Kolay

## 🛒 Malzemeler
- 1 litre badem sütü (veya soya sütü)
- 2 yemek kaşığı kakao
- 3 yemek kaşığı mısır nişastası
- 4 yemek kaşığı toz şeker

## 👨‍🍳 Yapılışı
1. Tüm malzemeleri tencereye alın.
2. Sürekli karıştırarak pişirin.
3. Koyulaşınca kaselere paylaştırın.
4. Soğuduktan sonra buzdolabına koyun.

## 💡 Servis Önerisi
Üzerine meyve dilimleri ekleyebilirsiniz.


