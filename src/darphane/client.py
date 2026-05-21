import requests

class Darphane:
    def __init__(self, github_username="kessinc"):
        # Verilerin çekileceği temel GitHub URL'i
        self.base_url = f"https://raw.githubusercontent.com/{github_username}/darphane/main"

    def _fetch_json(self, filename):
        url = f"{self.base_url}/{filename}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Darphane verisi çekilirken hata oluştu ({filename}): {e}")

    def kurlar(self):
        """Güncel resmi TCMB ve serbest piyasa döviz kurlarını döner."""
        return self._fetch_json("kurlar.json")

    def altin(self):
        """Güncel serbest piyasa altın ve emtila fiyatlarını döner."""
        return self._fetch_json("altin.json")

    def tatiller(self):
        """Türkiye resmi ve dini tatil takvimini döner."""
        return self._fetch_json("tatiller.json")

    def mevzuat(self):
        """Güncel vergi oranları, SGK payları ve gelir vergisi dilimlerini döner."""
        return self._fetch_json("mevzuat.json") 