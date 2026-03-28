from fastapi import APIRouter, HTTPException
from typing import List
from .modellek import Kurzus, Valasz
from .fajl_kezeles import KurzusFajlKezelo


utvonal = APIRouter()

fajl_kezelo = KurzusFajlKezelo()

@utvonal.get("/kurzusok", response_model=List[Kurzus])
async def get_osszes_kurzus():
    json_kurzusok = fajl_kezelo.kurzusok_olvasas()
    if not json_kurzusok:
        raise HTTPException(status_code=404, detail="Nincsenek kurzusok!")
    kurzusok = [Kurzus(**kurzus) for kurzus in json_kurzusok]
    return kurzusok

@utvonal.post("/kurzusok", response_model=Valasz)
async def uj_kurzus(kurzus: Kurzus):
    if kurzus.id <= 0:
        raise HTTPException(status_code=400, detail="Az id egy pozitív egész szám kell legyen!")
    if kurzus.tipus not in ['ea', 'gyak']:
        raise HTTPException(status_code=400, detail="A kurzus tipusa ea vagy gyak lehet!")
    if kurzus.evfolyam not in [1, 2, 3]:
        raise HTTPException(status_code=400, detail="Az évfolyam csak 1, 2 vagy 3 lehet!")
    if kurzus.max_letszam <= 0:
        raise HTTPException(status_code=400, detail="A max létszám egy pozitív egész szám kell legyen!")
    hallgato_ids = [hallgato.id for hallgato in kurzus.hallgatok]
    if any([i <= 0 for i in hallgato_ids]):
        raise HTTPException(status_code=400, detail="A hallgató id-je egy pozitív egész szám kell legyen!")
    if len(hallgato_ids) != len(set(hallgato_ids)):
        raise HTTPException(status_code=400, detail="Nem lehetnek azonos id-jű hallgatók!")
    json_kurzusok = fajl_kezelo.kurzusok_olvasas()
    kurzusok = [Kurzus(**kurzus) for kurzus in json_kurzusok]
    for k in kurzusok:
        if k.id == kurzus.id:
            # raise HTTPException(status_code=400, detail="Ez a kurzus id már foglalt") # Nem volt világos, hogy exception kell-e ide, ezért kikommenteztem
            return Valasz(**{"uzenet" : "Ez a kurzus id már foglalt"})
    kurzusok.append(kurzus)
    fajl_kezelo.kurzusok_iras([kurzus.dict() for kurzus in kurzusok])
    return Valasz(**{"uzenet": "Sikeres felvétel"})

# Az evfolyam paramétert stringről int-re változtattam, mert a Kurzus modellben az evfolyam int típusú
@utvonal.get("/kurzusok/filter", response_model=List[Kurzus])
async def get_kurzusok_filter(nap_idopont: str = None, oktato_email: str = None, tipus: str = None, evfolyam: int = None, helyszin: str = None, max_letszam: int = None):
    filters = locals()
    filter_set = {x for x in filters.values()} - {None}
    filters.pop("oktato_email")
    if len(filter_set) != 1:
        raise HTTPException(status_code=400, detail="Pontosan egy szűrő lehet!")
    kurzusok = fajl_kezelo.kurzusok_olvasas()
    return [k for k in kurzusok if all([k[key] == value for key, value in filters.items() if value is not None]) and (not oktato_email or k["oktato"]["email"] == oktato_email)]


# Az evfolyam paramétert stringről int-re változtattam, mert a Kurzus modellben az evfolyam int típusú
@utvonal.get("/kurzusok/filters", response_model=List[Kurzus])
async def get_kurzusok_filters(nap_idopont: str = None, oktato_email: str = None, tipus: str = None, evfolyam: int = None, helyszin: str = None, max_letszam: int = None):
    filters = locals()
    filter_set = {x for x in filters.values()} - {None}
    filters.pop("oktato_email")
    if len(filter_set) != 2:
        raise HTTPException(status_code=400, detail="Pontosan két szűrő lehet!")
    kurzusok = fajl_kezelo.kurzusok_olvasas()
    return [k for k in kurzusok if all([k[key] == value for key, value in filters.items() if value is not None]) and (
                not oktato_email or k["oktato"]["email"] == oktato_email)]


@utvonal.put("/kurzusok/{kurzus_id}", response_model=Kurzus)
async def update_kurzus(kurzus_id: int, kurzus: Kurzus):
    if kurzus.id <= 0:
        raise HTTPException(status_code=400, detail="Az id egy pozitív egész szám kell legyen!")
    if kurzus.tipus not in ['ea', 'gyak']:
        raise HTTPException(status_code=400, detail="A kurzus tipusa ea vagy gyak lehet!")
    if kurzus.evfolyam not in [1, 2, 3]:
        raise HTTPException(status_code=400, detail="Az évfolyam csak 1, 2 vagy 3 lehet!")
    if kurzus.max_letszam <= 0:
        raise HTTPException(status_code=400, detail="A max létszám egy pozitív egész szám kell legyen!")
    hallgato_ids = [hallgato.id for hallgato in kurzus.hallgatok]
    if any([i <= 0 for i in hallgato_ids]):
        raise HTTPException(status_code=400, detail="A hallgató id-je egy pozitív egész szám kell legyen!")
    if len(hallgato_ids) != len(set(hallgato_ids)):
        raise HTTPException(status_code=400, detail="Nem lehetnek azonos id-jű hallgatók!")
    json_kurzusok = fajl_kezelo.kurzusok_olvasas()
    kurzusok = [Kurzus(**kurzus) for kurzus in json_kurzusok]
    for i,k in enumerate(kurzusok):
        if k.id == kurzus_id:
            kurzusok[i] = kurzus
            fajl_kezelo.kurzusok_iras([kurzus.dict() for kurzus in kurzusok])
            return kurzus
    raise HTTPException(status_code=404, detail="Nem található a kurzus!")


@utvonal.get("/kurzusok/hallgatok/{hallgato_id}", response_model=List[Kurzus])
async def get_hallgato_kurzusai(hallgato_id: int):
    if hallgato_id <= 0:
        raise HTTPException(status_code=400, detail="Az id egy pozitív egész szám kell legyen!")
    kurzusok = fajl_kezelo.kurzusok_olvasas()
    return [k for k in kurzusok if any([h["id"] == hallgato_id for h in k["hallgatok"]])]

@utvonal.delete("/kurzusok/{kurzus_id}")
async def delete_kurzus(kurzus_id: int):
    json_kurzusok = fajl_kezelo.kurzusok_olvasas()
    kurzusok = [Kurzus(**kurzus) for kurzus in json_kurzusok]
    for k in kurzusok:
        if k.id == kurzus_id:
            kurzusok.remove(k)
            fajl_kezelo.kurzusok_iras([kurzus.dict() for kurzus in kurzusok])
            return "Sikeres törlés"
    raise HTTPException(status_code=404, detail="Nem található a kurzus!")

@utvonal.get("/kurzusok/{kurzus_id}/hallgatok/{hallgato_id}", response_model=Valasz)
async def get_hallgato_kurzuson(kurzus_id: int, hallgato_id: int):
    if hallgato_id <= 0 or kurzus_id <= 0:
        raise HTTPException(status_code=400, detail="Az id egy pozitív egész szám kell legyen!")
    kurzusok = fajl_kezelo.kurzusok_olvasas()
    for k in kurzusok:
        if k["id"] == kurzus_id and any([h["id"] == hallgato_id for h in k["hallgatok"]]):
            return Valasz(**{"uzenet": "Igen"})
    return Valasz(**{"uzenet": "Nem"})
