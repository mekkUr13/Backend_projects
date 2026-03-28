import json

class KurzusFajlKezelo:
    utvonal = "kurzusok.json"

    def kurzusok_olvasas(self):
        try:
            with open(self.utvonal, "r", encoding='utf-8') as be:
                kurzusok = json.load(be)
        except FileNotFoundError:
            print("Nem található a kurzusok fájl!")
            return []
        return kurzusok

    def kurzusok_iras(self, kurzusok):
        with open(self.utvonal, "w", encoding='utf-8') as ki:
            json.dump(kurzusok, ki, indent=4)
