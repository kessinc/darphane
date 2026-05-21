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

## 🛠️ Mimari ve Klasör Yapısı

Proje tamamen modüler bir çekirdek (core) mimarisi üzerine kurulmuştur:

```text
darphane/
├── .github/workflows/
│   └── update.yml          # Her gün 15:45'te çalışan otomasyon motoru
├── tcmb_core.py            # Resmi ve serbest döviz kurlarını toplayan motor
├── altin_core.py           # Serbest piyasa altın ve emtiaları süzen motor
├── tatiller_core.py        # Türkiye resmi tatillerini Türkçeleştiren motor
├── mevzuat_core.py         # Güncel vergi ve yasal sabitleri basan motor
├── main.py                 # Tüm motorları sırayla çalıştıran orkestra şefi
├── kurlar.json             # Çıktı: Canlı Döviz Verisi
├── altin.json              # Çıktı: Canlı Altın Verisi
├── tatiller.json           # Çıktı: Canlı Tatil Takvimi
└── mevzuat.json            # Çıktı: Canlı Vergi Oranları
```

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
