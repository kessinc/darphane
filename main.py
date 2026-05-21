from tcmb_core import kurlari_guncelle
from tatiller_core import tatilleri_guncelle
from mevzuat_core import mevzuati_guncelle
from altin_core import altin_fiyatlarini_guncelle

if __name__ == "__main__":
    print("🚀 Darphane Tüm Motorlar Başlatılıyor...")
    kurlari_guncelle()
    altin_fiyatlarini_guncelle()
    tatilleri_guncelle()
    mevzuati_guncelle()
    print("✨ Tüm veriler başarıyla güncellendi!")