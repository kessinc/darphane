import json
from datetime import datetime
import holidays

def tatilleri_guncelle():
    mevcut_yil = datetime.now().year
    tr_tatilleri = holidays.country_holidays('TR', years=mevcut_yil, language="tr")

    veri = {
        "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "yil": mevcut_yil,
        "resmi_tatiller": []
    }
    
    for tarih, isim in sorted(tr_tatilleri.items()):
        veri["resmi_tatiller"].append({
            "tarih": tarih.strftime("%Y-%m-%d"),
            "isim": isim
        })
        
    with open("tatiller.json", "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)
        
    print(f"✅ Darphane Başarılı: {mevcut_yil} yılı resmi tatilleri TÜRKÇE olarak 'tatiller.json' dosyasına kaydedildi!")

if __name__ == "__main__":
    tatilleri_guncelle()