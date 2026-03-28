"Szakácsképző Intézmény" FastAPI projektje

Ez egy FastAPi alkalmazás, amelyik egy Szakácsképző Intézmény kurzusait, oktatóit és hallgatóit tartja nyilván:
   Kurzusok: azonosítószám, név, típus (ea, gyak), évfolyam (1,2,3), nap-időpont, helyszín, oktató, hallgatók, max. létszám.
   Kurzus név: Levesek, Sültek, Köretek, Saláták, Desszertek, …
   Oktató: név, email
   Hallgató: azonosítószám, név, email

A kurzusok.json fájlban jelenleg egy példa szerepel. 
A modellek.py fájl tartalmazza az osztályok atribútumait és azok típusait.
A fajl_kezeles.py fájlban a kurzusok.json fájl olvasása és írása szerepel. Ezeket a metódusokat kell felhasználni az utvonalak.py hiányzó metódusainak megírásakor.

Az alkalmazás futtatása:
1. Nyisd meg a Beadandó_1 mappát 

2. Az uvicorn modul telepítése:
pip install uvicorn

3. Futtasd a kódot a terminálban a következő paranccsal:
python app_sz/main.py

4. A böngésző címsorába írd be a következő URL-t:
http://127.0.0.1:8000/docs

5. A kapott interaktív felületen tudod tesztelni az egyes API végpontokat.

6. Az utvonalak.py fájlban a pass utasítások helyére implementáld a megfelelő metódusokat. Alkalmazz mindenhol kivételkezelést a felmerülő exeption-ok esetén: 
pl. raise HTTPException(status_code=404, detail="Hallgató nem található.")

7. A FastAPI alkalmazás futtatásához szükséges csomagok és modulok telepítését végezd el a pip install package_név paranccsal Command line-ból. Ezek lehetnek a következők (verziószámmal): annotated-types (0.6.0), anyio (4.3.0), click (8.1.7), colorama (0.4.6), fastapi (0.110.0), h11 (0.14.0), idna (3.6), pydantic (2.6.3), pydantic_core (2.16.3), sniffio (1.3.1), starlette (0.36.3), typing_extensions (4.10.0), uvicorn (0.27.1).


Sikeres munkát kívánok!









