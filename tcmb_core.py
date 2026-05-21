import xml.etree.ElementTree as ET
import json
from datetime import datetime
import requests

def kurlari_guncelle():
    tcmb_url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    serbest_url = "https://finans.truncgil.com/today.json"
    
    veri = {
        "son_guncelleme": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "resmi_tcmb_kurlari": {},
        "serbest_piyasa_kurlari": {}
    }
    
    # 1. KISIM: RESMİ TCMB KURLARI
    try:
        tcmb_response = requests.get(tcmb_url)
        tcmb_response.raise_for_status()
        root = ET.fromstring(tcmb_response.content)
        
        for currency in root.findall('Currency'):
            kod = currency.get('CurrencyCode')
            if kod:
                alis_element = currency.find('ForexBuying')
                satis_element = currency.find('ForexSelling')
                isim_element = currency.find('Isim')
                
                if alis_element is not None and satis_element is not None and alis_element.text and satis_element.text:
                    veri["resmi_tcmb_kurlari"][kod] = {
                        "isim": isim_element.text.strip() if isim_element is not None else kod,
                        "alis": float(alis_element.text.replace(',', '.')),
                        "satis": float(satis_element.text.replace(',', '.'))
                    }
        print("✅ Darphane: Resmi TCMB kurları alındı.")
    except Exception as e:
        print(f"⚠️ TCMB Hatası: {e}")

    # 2. KISIM: SERBEST PİYASA KURLARI (Tam Eşleşme)
    try:
        serbest_response = requests.get(serbest_url)
        serbest_response.raise_for_status()
        serbest_data = serbest_response.json()
        
        # JSON çıktından gördüğümüz net döviz kodları
        hedef_dovizler = ["USD", "EUR", "GBP", "CHF", "CAD", "RUB", "AED", "AUD", "DKK", "SEK", "NOK", "JPY", "KWD", "SAR", "AZN", "PKR", "QAR", "KRW", "KZT"]
        
        for kod in hedef_dovizler:
            if kod in serbest_data:
                item = serbest_data[kod]
                alis_str = item.get("Alış", "0").replace('.', '').replace(',', '.')
                satis_str = item.get("Satış", "0").replace('.', '').replace(',', '.')
                
                veri["serbest_piyasa_kurlari"][kod] = {
                    "isim": f"Serbest Piyasa {kod}",
                    "alis": float(alis_str) if alis_str != "0" else None,
                    "satis": float(satis_str) if satis_str != "0" else None
                }
        print("✅ Darphane: Serbest piyasa (Kapalıçarşı) kurları alındı.")
    except Exception as e:
        print(f"⚠️ Serbest Piyasa Hatası: {e}")

    with open("kurlar.json", "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    kurlari_guncelle()