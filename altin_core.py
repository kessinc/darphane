import json
from datetime import datetime
import requests

def altin_fiyatlarini_guncelle():
    url = "https://finans.truncgil.com/today.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        veri = {
            "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "altin_ve_emtia": {}
        }
        
        # Elenecek birebir döviz kodları listesi
        doviz_kodlari = ["USD", "EUR", "GBP", "CHF", "CAD", "RUB", "AED", "AUD", "DKK", "SEK", "NOK", "JPY", "KWD", "ZAR", "BHD", "LYD", "SAR", "IQD", "ILS", "INR", "MXN", "HUF", "NZD", "BRL", "IDR", "CZK", "PLN", "RON", "CNY", "ARS", "ALL", "AZN", "BAM", "CLP", "COP", "CRC", "DZD", "EGP", "HKD", "ISK", "KRW", "KZT", "LBP", "LKR", "MAD", "MDL", "MKD", "MYR", "OMR", "PEN", "PHP", "PKR", "QAR", "RSD", "SGD", "SYP", "THB", "TWD", "UAH", "UYU", "GEL", "TND", "BGN"]
        
        for key, value in data.items():
            if isinstance(value, dict) and "Alış" in value and "Satış" in value:
                # Eğer gelen anahtar döviz listesindeyse burayı pas geçiyoruz
                if key in doviz_kodlari:
                    continue
                
                # Sadece altın ve emtialar kaldı, kodlarını düzeltip kaydediyoruz
                try:
                    alis_str = value.get("Alış", "0").replace('.', '').replace(',', '.')
                    satis_str = value.get("Satış", "0").replace('.', '').replace(',', '.')
                    
                    temiz_kod = key.upper().replace(' ', '_').replace('-', '_').replace('İ', 'I').replace('Ş', 'S').replace('Ğ', 'G').replace('Ç', 'C').replace('Ö', 'O').replace('Ü', 'U')
                    
                    veri["altin_ve_emtia"][temiz_kod] = {
                        "orijinal_isim": key,
                        "alis": float(alis_str) if alis_str != "0" else None,
                        "satis": float(satis_str) if satis_str != "0" else None
                    }
                except ValueError:
                    continue
                
        with open("altin.json", "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=4)
            
        print("✅ Darphane: altin.json tamamen temizlendi!")

    except Exception as e:
        print(f"❌ Altın hatası: {e}")

if __name__ == "__main__":
    altin_fiyatlarini_guncelle()