import json
from datetime import datetime

def mevzuati_guncelle():
    veri = {
        "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "yil": 2026,
        "vergi_oranlari": {
            "kdv": {
                "standart": 0.20,      # Genel KDV oranı (%20)
                "gida_temel": 0.01,    # Temel gıda ürünleri (%1)
                "tekstil_egitim": 0.10 # Giyim, tiyatro, eğitim (%10)
            },
            "stopaj": {
                "kira": 0.20,          # İşyeri kira stopajı (%20)
                "freelance_makbuz": 0.20 # Serbest meslek makbuzu stopajı (%20)
            },
            "sgk": {
                "isciler": 0.14,       # İşçi payı (%14)
                "issizlik_isci": 0.01, # İşçi işsizlik payı (%1)
                "isveren": 0.155       # İşveren payı (%5 teşvikli %15.5)
            }
        },
        "gelir_vergisi_dilimleri_2026": [
            {"limit_ust": 150000, "oran": 0.15, "aciklama": "150.000 TL'ye kadar"},
            {"limit_ust": 350000, "oran": 0.20, "aciklama": "150.000 TL - 350.000 TL arası"},
            {"limit_ust": 900000, "oran": 0.27, "aciklama": "350.000 TL - 900.000 TL arası"},
            {"limit_ust": 4000000, "oran": 0.35, "aciklama": "900.000 TL - 4.000.000 TL arası"},
            {"limit_ust": None, "oran": 0.40, "aciklama": "4.000.000 TL'den fazlası için"}
        ]
    }
    
    with open("mevzuat.json", "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)
        
    print("✅ Darphane Başarılı: 2026 Vergi ve Mevzuat sabitleri 'mevzuat.json' dosyasına kaydedildi!")

if __name__ == "__main__":
    mevzuati_guncelle()