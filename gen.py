import json, os
CFG=json.load(open("config.json")) if os.path.exists("config.json") else {}
OWN,REPO=CFG.get("owner",""),CFG.get("repo","programma-immigrazione")
BASE=f"https://raw.githubusercontent.com/{OWN}/{REPO}/main/" if OWN else ""
STORICO=json.load(open("storico.json",encoding="utf-8"))
from dati_a import PERMESSI_A
from dati_b import PERMESSI_B, NORME, GENERALI, FAQ, ESEMPI, RICONG
try:
    from dati_c import PERMESSI_C, RICONG_C, FAQ_C
except ImportError:
    PERMESSI_C, RICONG_C, FAQ_C = [], {}, []
PERMESSI_B = PERMESSI_B + PERMESSI_C
RICONG = {**RICONG, **RICONG_C}
FAQ = FAQ + FAQ_C
for p in PERMESSI_A+PERMESSI_B:
    p.setdefault("conversioni", [])
    if p["id"] in RICONG: p["ricong"]=RICONG[p["id"]]
data = dict(
 revisione=STORICO[-1]["revisione"], dataISO=STORICO[-1]["data"], aggiornamento=STORICO[-1]["data"], appMinima=2, storico=STORICO,
 aggiornamenti=dict(url=[BASE+"dist/banca-dati.json", f"https://cdn.jsdelivr.net/gh/{OWN}/{REPO}@main/dist/banca-dati.json"] if OWN else [], programma=BASE+"dist/Programma%20Immigrazione.html" if OWN else ""),
 avvertenza="Strumento di supporto alla consultazione. Le schede sintetizzano la normativa vigente al 30/10/2026 sulla base di fonti consolidate non ufficiali e dossier istituzionali: prima di adottare un provvedimento verifica sempre il testo vigente (Normattiva/Gazzetta Ufficiale) e le circolari del Ministero dell'Interno. I punti indicati 'da verificare' non hanno conferma testuale certa.",
 permessi=PERMESSI_A+PERMESSI_B, norme=NORME, generali=GENERALI, faq=FAQ, esempi=ESEMPI,
 matriceColonne=["lav_sub","lav_aut","famiglia","studio","attesa_occ","lungo_periodo"],
 reddito=dict(assegnoSocialeAnnuo=7101.12, nota="Assegno sociale 2026: 546,24 € × 13 mensilità = 7.101,12 € (circ. INPS n. 153/2025). Aggiorna l'importo ogni anno. Concorre il reddito dei familiari conviventi; i titolari dello status di rifugiato sono esonerati dal requisito per il ricongiungimento (art. 29-bis).", norme=["art. 29 TU 286/1998","art. 9 TU 286/1998","art. 29-bis TU 286/1998"]))
json.dump(data, open("data.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
os.makedirs("dist",exist_ok=True)
json.dump(data, open("dist/banca-dati.json","w",encoding="utf-8"), ensure_ascii=False)
