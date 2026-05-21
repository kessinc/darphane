# 🏦 Darphane

> Türkiye finans, piyasa ve mevzuat verilerini sıfır sunucu maliyeti, sınırsız istek limiti ve %100 ulaşılan süre (uptime) ile sunan ölümsüz, sunucusuz (Serverless/GitOps) açık kaynaklı veri altyapısı.

[![Darphane Otomatik Veri Güncelleyici](https://github.com/kessinc/darphane/actions/workflows/update.yml/badge.svg)](https://github.com/kessinc/darphane/actions/workflows/update.yml)

⭐ **Projeyi beğendiyseniz star atarak destek olabilirsiniz!**

---

## 🎯 Neden Darphane?

Türkiye'deki yazılımcıların en büyük dertlerinden biri; resmi kurumlardan (TCMB vb.) döviz çekmek, serbest piyasa altın fiyatlarını takip etmek veya her yıl değişen resmi tatilleri sisteme entegre etmektir. Ücretli API'ler pahalıdır, ücretsiz sunucular ise uyku moduna geçer veya çöker.

**Darphane bu sorunu GitOps mimarisiyle çözer:**
*   **Sıfır Gecikme (Milisaniyeler):** Veriler doğrudan GitHub CDN altyapısından düz JSON dosyası olarak servis edilir. Sunucu uyanmasını beklemezsiniz.
*   **Sonsuz Limit (No Rate-Limit):** Dakikada kaç bin istek atarsanız atın asla engellenmezsiniz.
*   **Her Gün Güncel:** GitHub Actions her gün TSİ 15:45'te otomatik olarak uyanır, resmi kaynakları tarar, JSON dosyalarını günceller ve yeniden uyur.

---

## 📦 Sağlanan Veri Setleri (JSON API)

Projelerinizde herhangi bir kütüphane indirmeden, doğrudan aşağıdaki ham URL'lere `GET` isteği atarak veya tarayıcınızdan açarak verileri anında kullanabilirsiniz:

| Veri Seti | Açıklama | Canlı JSON Linki |
| :--- | :--- | :--- |
| 💵 **Döviz Kurları** | Resmi TCMB Kurları + Serbest Piyasa (Kapalıçarşı) Kurları bir arada. | [https://raw.githubusercontent.com/kessinc/darphane/main/kurlar.json](https://raw.githubusercontent.com/kessinc/darphane/main/kurlar.json) |
| 🟡 **Altın & Emtia** | Serbest piyasadaki tüm altın (Gram, Çeyrek, Ata vb.) ve emtia (Gümüş, Platin) fiyatları. | [https://raw.githubusercontent.com/kessinc/darphane/main/altin.json](https://raw.githubusercontent.com/kessinc/darphane/main/altin.json) |
| 📅 **Resmi Tatiller** | İçinde bulunulan yılın tüm dini/resmi tatil günleri ve Türkçe isimleri. | [https://raw.githubusercontent.com/kessinc/darphane/main/tatiller.json](https://raw.githubusercontent.com/kessinc/darphane/main/tatiller.json) |
| ⚖️ **Mevzuat & Vergi** | Güncel KDV oranları, stopajlar, SGK payları ve Gelir Vergisi dilimleri. | [https://raw.githubusercontent.com/kessinc/darphane/main/mevzuat.json](https://raw.githubusercontent.com/kessinc/darphane/main/mevzuat.json) |

---

## 🐍 Python SDK ile Kullanım (Pip Paketi)

Darphane verilerini ham JSON olarak çekmek yerine, projenize resmi Python kütüphanesini dahil ederek nesne tabanlı (Object Oriented) bir şekilde çok daha temiz kullanabilirsiniz.

### 1. Kurulum
Terminalinizden kütüphaneyi hızlıca yükleyin:
```bash
pip install darphane
```

### 2. Kod Örnekleri

```python
import json
from darphane import Darphane

# Kütüphaneyi başlatıyoruz
dp = Darphane()

# ---------------------------------------------------------
# 1. 💵 DÖVİZ KURLARI ÖRNEĞİ
# ---------------------------------------------------------
guncel_kurlar = dp.kurlar()
print(f"Son Güncelleme: {guncel_kurlar['son_guncelleme']}")

# 🏛️ Resmi TCMB Kurları Piyasası
resmi_usd_tcmb = guncel_kurlar['resmi_tcmb_kurlari']['USD']
print(f"TCMB USD Alış: {resmi_usd_tcmb['alis']} TL | Satış: {resmi_usd_tcmb['satis']} TL")

# 🏪 Serbest Döviz Piyasası (Kapalıçarşı)
serbest_usd_piyasa = guncel_kurlar['serbest_piyasa_kurlari']['USD']
print(f"Serbest Piyasa USD Alış: {serbest_usd_piyasa['alis']} TL\n")


# ---------------------------------------------------------
# 2. 🟡 ALTIN & EMTİA ÖRNEĞİ
# ---------------------------------------------------------
guncel_altin = dp.altin()

# Gram Altın fiyatına erişim
gram_altin = guncel_altin['altin_ve_emtia']['GRAM_ALTIN'] # 'GRAM_ALTIN' veya verideki kısaltma anahtarı
print(f"Gram Altın Alış: {gram_altin['alis']} TL | Satış: {gram_altin['satis']} TL")

# Çeyrek Altın fiyatına erişim
ceyrek_altin = guncel_altin['altin_ve_emtia']['CEYREK_ALTIN']
print(f"Çeyrek Altın Satış: {ceyrek_altin['satis']} TL\n")


# ---------------------------------------------------------
# 3. 📅 RESMİ TATİLLER ÖRNEĞİ
# ---------------------------------------------------------
resmi_tatiller = dp.tatiller()

print("--- Türkiye Resmi Tatil Takvimi ---")
# Listeyi dönüyoruz ve her bir sözlükten verileri çekiyoruz
for tatil in resmi_tatiller['resmi_tatiller']:
    print(f"📅 {tatil['tarih']} -> {tatil['isim']}")
print("\n")


# ---------------------------------------------------------
# 4. ⚖️ MEVZUAT & VERGİ ÖRNEĞİ
# ---------------------------------------------------------
mevzuat_verileri = dp.mevzuat()

# Güncel standart KDV oranına erişim (%20 için 0.2 döner)
standart_kdv = mevzuat_verileri['vergi_oranlari']['kdv']['standart']
print(f"Güncel Standart KDV Oranı: %{standart_kdv * 100}")

# Gelir vergisi dilimlerini listeleme (Liste yapısında olduğu için döngüyle basıyoruz)
print("--- Gelir Vergisi Dilimleri ---")
for dilim in mevzuat_verileri['gelir_vergisi_dilimleri']:
    print(f"💰 Oran: %{dilim['oran'] * 100} -> {dilim['aciklama']}")
```

> *Not: Yukarıdaki veri içindeki `['GRAM_ALTIN']`, `['vergi_oranlari']` gibi sözlük (dict) anahtarları, `altin.json` ve `mevzuat.json` dosyalarınızın tam şemasına göre küçük değişiklikler gösterebilir. Kendi JSON şemanıza göre bu kelimeleri güncelleyebilirsiniz.*

### 📚 SDK Fonksiyon Listesi

| Fonksiyon | Dönüş Tipi | Açıklama |
| :--- | :--- | :--- |
| `dp.kurlar()` | `dict` | İçerisinde **resmi_tcmb_kurlari** ve **serbest_piyasa_kurlari** olmak üzere iki farklı piyasanın güncel döviz kurlarını döner. |
| `dp.altin()` | `dict` | Güncel serbest piyasa altın ve emtia fiyatlarını döner. |
| `dp.tatiller()` | `dict` | Türkiye resmi ve dini tatil takvimini döner. |
| `dp.mevzuat()` | `dict` | Güncel vergi oranları, SGK payları ve gelir vergisi dilimlerini döner. |

---

## 🚀 Yerel Geliştirme (Local Setup)

Projeyi kendi bilgisayarınızda çalıştırmak veya katkıda bulunmak isterseniz:

```bash
# 1. Projeyi klonlayın
git clone https://github.com/kessinc/darphane.git
cd darphane

# 2. Sanal ortam oluşturun ve aktif edin
python3 -m venv .venv
source .venv/bin/activate  # Windows için: .venv\Scripts\activate

# 3. Bağımlılıkları yükleyin
pip install requests holidays

# 4. Tüm motorları tetikleyin
python main.py
```

---

## 🤝 Katkıda Bulunma (Contributing)

Darphane tamamen topluluğun ihtiyaçlarına göre genişletilebilir bir projedir. Türkiye finans altyapısına eklenmesini istediğiniz bir veri seti (örn: BIST hisseleri, kripto paralar veya yeni vergi mevzuatları) varsa:
1. Projeyi Fork'layın.
2. Yeni bir core dosyası açıp `main.py`'a bağlayın.
3. Pull Request (PR) gönderin!

## 📄 Lisans

Bu proje **MIT** lisansı altında tamamen ücretsiz ve açık kaynaklı olarak yayınlanmıştır. Ticari veya bireysel projelerinizde dilediğiniz gibi kullanabilirsiniz.
