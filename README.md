# Programma Immigrazione

Programma offline di consultazione per l'Ufficio Immigrazione: permessi di soggiorno, requisiti, conversioni, normativa.

- **Programma da usare:** `dist/Programma Immigrazione.html` (doppio clic, funziona senza internet).
- **Banca dati online:** `dist/banca-dati.json`. Il programma la controlla a ogni avvio e, se è più recente, la applica da solo.

## Come si aggiorna (per chi mantiene la banca dati)
1. Modificare le schede in `dati_a.py` / `dati_b.py`.
2. Aggiungere in coda a `storico.json` una voce con `revisione` = ultima + 1, `data` (AAAA-MM-GG) e l'elenco `novita` in italiano semplice.
3. Eseguire `python3 gen.py && python3 build.py`.
4. Fare commit e push di tutto (compresa la cartella `dist/`).

Se si modifica `template.html` in modo che i dati nuovi richiedano il programma nuovo, aumentare `APP_VERSIONE` nel template e `appMinima` in `gen.py`: i PC con il programma vecchio vedranno l'avviso per scaricare la nuova versione.

Le fonti delle ricerche sono in `ricerca/`.
