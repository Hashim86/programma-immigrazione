# Revisione indipendente della banca dati (dati_a.py, dati_b.py)

Data della revisione: 30/10/2026. I file non sono stati modificati.

Metodo: ho letto entrambi i file per intero. Ho verificato sul web le affermazioni ad alto impatto. Normattiva non era raggiungibile, quindi il testo consolidato del TU l'ho controllato su Brocardi.it (pagine "aggiornato al 16/07/2026") e su altre fonti secondarie. Quando una fonte primaria non era disponibile, l'ho indicato.

Livelli di gravità:
- **ALTA**: l'errore può portare a rilasciare o negare un titolo in modo sbagliato.
- **MEDIA**: dato errato o incompleto che può fuorviare l'operatore.
- **BASSA**: forma, coerenza o completezza.

Livelli di certezza:
- **certo**: testo di legge riscontrato.
- **probabile**: fonte secondaria attendibile oppure sintesi del testo.
- **da verificare**: nessuna conferma trovata, quindi nessuna correzione proposta.

---

## Gravità ALTA

### A1. `rifugiato` e `sussidiaria`: conversione in `lungo_periodo`, calcolo dei 5 anni sbagliato
- **Testo attuale** (rifugiato, condizioni): "5 anni di soggiorno (metà del periodo di attesa della decisione, o tutto se oltre 18 mesi)".
- **Problema:** è la regola facoltativa della dir. 2011/51/UE, non quella italiana. L'art. 9 c.5-bis TU fa decorrere il periodo dalla data di presentazione della domanda di protezione su cui si fonda il riconoscimento e conta l'intero periodo, senza dimezzamenti. Con la regola attuale si rischia di negare il permesso UE di lungo periodo a chi ne ha diritto. La scheda `sussidiaria` non indica alcun calcolo.
- **Correzione proposta** (rifugiato; aggiungere lo stesso testo anche in sussidiaria):
  `C("lungo_periodo", "si", "Permesso UE di lungo periodo dopo 5 anni, calcolati per intero dalla data di presentazione della domanda di protezione internazionale (art. 9 c.5-bis). Esonero dal test di italiano (c.2-ter) e dalla documentazione sull'alloggio (c.1-ter).", ["art. 9 c.1, c.1-ter, c.2-ter, c.5-bis TU 286/1998"], ["5 anni dalla data della domanda di protezione", "Reddito non inferiore all'assegno sociale (per i vulnerabili, l'alloggio gratuito vale figurativamente il 15%)", "Indicazione del luogo di residenza"], "Nel permesso va annotato 'protezione internazionale riconosciuta da [Stato] il [data]' (art. 9 c.1-bis).")`
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art9.html (commi 1-bis, 1-ter, 2-ter, 5-bis)
- **Certezza:** certo

### A2. Permesso UE di lungo periodo: elenco dei permessi esclusi incompleto (protezione speciale e art. 42-bis)
- **Testo attuale:**
  - `lungo_periodo`, requisiti: "Non rientrare tra i permessi esclusi (studio, protezione temporanea, cure mediche, casi speciali, breve durata, ecc.)".
  - NORME art. 9: "Esclusi (c.3): studio, protezione temporanea, cure mediche, casi speciali, calamità, domanda di asilo pendente, permessi di breve durata, diplomatici".
  - FAQ sul lungo periodo: elenco analogo.
- **Problema:** l'art. 9 c.3 lett. b esclude espressamente anche i titolari del permesso art. 42-bis (valore civile) e del permesso ex art. 32 c.3 D.Lgs. 25/2008 (protezione speciale), e chi ha chiesto questi titoli ed è in attesa della decisione. La scheda `valore_civile` non ha alcuna voce `lungo_periodo`. Un operatore potrebbe quindi rilasciare il permesso UE di lungo periodo a un titolare di permesso art. 42-bis.
- **Correzione proposta:**
  - NORME art. 9, sostituire la frase degli esclusi con: "Esclusi (c.3): studio e formazione; protezione temporanea, cure mediche, artt. 18, 18-bis, 20-bis, 22 c.12-quater, 42-bis, protezione speciale (art. 32 c.3 D.Lgs. 25/2008), anche se la domanda per questi titoli è solo pendente; domanda di protezione internazionale pendente; permessi di breve durata; diplomatici."
  - `lungo_periodo`, requisito: "Non rientrare tra i permessi esclusi dall'art. 9 c.3: studio, protezione temporanea, cure mediche, artt. 18, 18-bis, 20-bis, 22 c.12-quater, 42-bis, protezione speciale, asilo pendente, breve durata, diplomatici".
  - Aggiungere in `valore_civile`: `C("lungo_periodo", "no", "Escluso dal permesso UE di lungo periodo.", ["art. 9 c.3 lett. b TU 286/1998"])`.
  - Nella FAQ aggiungere "protezione speciale, valore civile (art. 42-bis)".
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art9.html
- **Certezza:** certo

### A3. Coesione familiare (art. 30 c.1 lett. c): mancano due regole decisive
- **Testo attuale** (`famiglia`, requisito): "Coesione (art. 30 c.1 lett. c): familiare già regolarmente soggiornante con altro titolo, in possesso dei requisiti per il ricongiungimento". Nelle conversioni verso `famiglia` (da lav_sub, lav_aut, attesa_occ, studio, assist_fam) non compare nessun termine.
- **Problema:** la norma prevede due regole che la banca dati non riporta.
  - La conversione può essere chiesta entro 1 anno dalla scadenza del titolo originario. Se l'operatore pretende un titolo ancora valido, rischia di negare la coesione a chi ne ha diritto.
  - Se il familiare di riferimento è un rifugiato, non serve un permesso valido.
- **Correzione proposta** (requisito di `famiglia`): "Coesione (art. 30 c.1 lett. c): familiare regolarmente soggiornante con altro titolo, in possesso dei requisiti per il ricongiungimento. La conversione si può chiedere anche entro 1 anno dalla scadenza del titolo originario. Se il familiare di riferimento è rifugiato, non serve un permesso valido." Aggiungere la stessa condizione ("Domanda entro 1 anno dalla scadenza del titolo posseduto") nelle C("famiglia", …) delle schede lav_sub, lav_aut, attesa_occ, studio e assist_fam.
- **Fonte:** https://brocardi.it/testo-unico-immigrazione/titolo-iv/art30.html
- **Certezza:** certo

### A4. `attesa_citt`: manca il requisito del permesso già posseduto
- **Testo attuale:** requisiti "Documentazione dell'avvio del procedimento di cittadinanza", "Alloggio e mezzi di sussistenza".
- **Problema:** l'art. 11 c.1 lett. c DPR 394/1999 prevede il permesso "per acquisto della cittadinanza o dello stato di apolide" a favore dello straniero "già in possesso del permesso di soggiorno per altri motivi", per la durata del procedimento. Senza questo requisito si rischia di rilasciarlo a chi è irregolare o entrato per turismo. Per i riconoscimenti iure sanguinis la prassi consolidata era diversa; dopo il DL 36/2025 va verificata.
- **Correzione proposta:** aggiungere in testa ai requisiti `R("Essere già in possesso di permesso di soggiorno per altri motivi", "art. 11 c.1 lett. c DPR 394/1999")`. Sostituire la durata con "Per la durata del procedimento di concessione o riconoscimento (art. 11 c.1 lett. c DPR 394)". In nota: "Prassi per i richiedenti iure sanguinis entrati con visto turistico: verificare le circolari vigenti dopo il DL 36/2025."
- **Fonte:** https://trentininelmondo.it/attachments/article/52/art.11_reg.att._dicembre_2018.pdf (testo dell'art. 11 al 2018). Testo vigente da confrontare su Normattiva.
- **Certezza:** probabile

### A5. `minore_eta`: requisiti dell'art. 32 c.1-ter incompleti
- **Testo attuale:** "Al compimento dei 18 anni (MSNA): parere positivo della DG Immigrazione del Ministero del Lavoro, oppure 3 anni di presenza e 2 di progetto di integrazione". Il testo è uguale nelle conversioni e nella FAQ.
- **Problema:** per la seconda via l'art. 32 c.1-ter chiede che l'ente gestore documenti, oltre ai 3 anni di presenza e ai 2 di progetto, anche:
  - la disponibilità di un alloggio;
  - la frequenza di corsi di studio o lo svolgimento di un lavoro retribuito, oppure un contratto di lavoro anche non ancora iniziato.

  I requisiti sono cumulativi. Così come è scritto, il testo può far rilasciare il permesso senza alloggio e senza studio o lavoro. Inoltre l'art. 32 c.1 prevede anche il permesso per "esigenze sanitarie o di cura".
- **Correzione proposta:**
  - Requisito: "Al compimento dei 18 anni (MSNA): a) se affidato o in tutela, parere positivo della DG Immigrazione del Ministero del Lavoro; oppure b) ammissione da almeno 2 anni a un progetto di integrazione di un ente iscritto, con presenza in Italia da almeno 3 anni, alloggio e frequenza di corsi di studio o lavoro retribuito o contratto di lavoro (requisiti cumulativi, documentati dall'ente: art. 32 c.1-ter)."
  - Durata: "Il permesso ex art. 32 c.1-bis (studio, accesso al lavoro, lavoro) dura al massimo 1 anno."
  - Aggiungere la voce "esigenze sanitarie o di cura (art. 32 c.1)".
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-iv/art32.html
- **Certezza:** certo

### A6. `lav_sub`: la durata al rinnovo è indicata in modo generico (incoerenza interna)
- **Testo attuale:**
  - durata: "Rinnovo: fino a 3 anni.";
  - rinnovo: "Il rinnovo dei permessi a tempo indeterminato può avere durata fino a 3 anni";
  - NORME art. 5: "rinnovi fino a 3 anni (c.3-bis, 3-quater)";
  - nota: "Durata massima del rinnovo per il tempo determinato: le fonti non sono univoche".
- **Problema:** l'art. 5 c.3-bis prevede rinnovi fino a 3 anni solo per il tempo indeterminato (lett. c). Per il lavoro autonomo vale il c.3-quater. Per il tempo determinato restano il limite di 1 anno e il c.4 (il rinnovo non supera la durata del rilascio iniziale). La riga "Rinnovo: fino a 3 anni" può far rilasciare un permesso di 3 anni con un contratto a termine.
- **Correzione proposta:**
  - durata: "Primo rilascio: pari al contratto, max 1 anno (tempo determinato) o 2 anni (tempo indeterminato). Rinnovo: tempo indeterminato fino a 3 anni; tempo determinato non oltre la durata del contratto e comunque non oltre 1 anno (art. 5 c.3-bis e c.4)."
  - NORME art. 5: "rinnovi fino a 3 anni per il lavoro a tempo indeterminato (c.3-bis lett. c) e per il lavoro autonomo (c.3-quater)".
  - Eliminare la nota "le fonti non sono univoche".
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art5.html (c.3-bis, 3-quater, 4)
- **Certezza:** probabile (sintesi del testo consolidato)

---

## Gravità MEDIA

### M1. GENERALI "Termini, rinnovo e ricevuta": il punto "da verificare" sul c.9-bis si può chiudere
- **Testo attuale:** "Condizioni del c.9-bis dopo il DL 146/2025 (eventuale requisito della domanda entro 60 giorni dalla scadenza): fonti non concordi, verificare".
- **Problema:** il DL 146/2025 ha sostituito il c.9-bis. Ha esteso la regola alle conversioni ed eliminato le condizioni precedenti: domanda presentata alla stipula del contratto oppure prima della scadenza o entro 60 giorni. Il testo vigente è un unico periodo e richiede solo la ricevuta. Il D.Lgs. 83/2026 ha poi portato da 60 a 90 giorni il termine richiamato nel comma, cioè il termine di definizione del c.9. Lasciare il dubbio può portare l'operatore a contestare il lavoro nelle more.
- **Correzione proposta:** "Il c.9-bis, riscritto dal DL 146/2025, non prevede più condizioni sul momento della domanda: chi ha la ricevuta di rilascio, rinnovo o conversione soggiorna e lavora fino all'eventuale comunicazione dei motivi ostativi, anche se è superato il termine di 90 giorni del c.9 (D.Lgs. 83/2026)."
- **Fonti:**
  - https://temi.camera.it/leg19/provvedimento/d-l-146-2025-disposizioni-urgenti-in-materia-di-ingresso-regolare-di-lavoratori-e-cittadini-stranieri-nonch-di-gestione-del-fenomeno-migratorio.html
  - https://www.wikilabour.it/wp-content/uploads/2026/06/DLgs_83-2026.pdf
  - https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art5.html
- **Certezza:** probabile

### M2. `famit`: la durata è certa (5 anni), il permesso è esente dal contributo e si converte anche in lavoro autonomo
- **Testo attuale:** durata "Fonti non concordi: 5 anni, oppure 2 anni estendibili a 5. Verificare la circolare". Conversioni: solo lav_sub. Il FAMIT non compare tra gli esenti dal contributo in GENERALI.
- **Problema:** l'art. 23 c.1-bis D.Lgs. 30/2007 dice testualmente che il permesso "è valido cinque anni", è rinnovabile e "può essere convertito" in permesso per motivi di lavoro. Lo stesso comma esclude l'applicazione dell'art. 5 c.2-ter TU, quindi il contributo non è dovuto.
- **Correzione proposta:**
  - durata: "5 anni, rinnovabile alla scadenza (art. 23 c.1-bis D.Lgs. 30/2007)."
  - Aggiungere la nota "Non si paga il contributo dell'art. 5 c.2-ter (art. 23 c.1-bis)" e aggiungere "FAMIT" all'elenco degli esenti in GENERALI → Costi 2026.
  - Aggiungere `C("lav_aut", "si", "Convertibile in permesso per motivi di lavoro, anche autonomo, con i requisiti dell'art. 26.", ["art. 23 c.1-bis D.Lgs. 30/2007", "art. 26 TU 286/1998"])`.
- **Fonte:** https://www.esteri.it/wp-content/uploads/2025/12/30_2007.pdf (testo dell'art. 23)
- **Certezza:** certo per durata e contributo; probabile per l'estensione al lavoro autonomo (la norma dice genericamente "motivi di lavoro")

### M3. Protezione speciale esente dal contributo
- **Testo attuale** (GENERALI, Costi): "Esenzione per 18-ter e protezione speciale: da verificare". La scheda `prot_speciale` non ne parla.
- **Problema:** l'art. 5 c.2-ter esenta espressamente il permesso ex art. 32 c.3 D.Lgs. 25/2008, cioè la protezione speciale. Il 18-ter invece non compare nel testo del c.2-ter.
- **Correzione proposta:** "Esenti dal contributo (solo PSE): … protezione speciale (art. 32 c.3 D.Lgs. 25/2008) … Art. 18-ter: non è nell'elenco del c.2-ter (verificare circolari)." Nella scheda `prot_speciale`, aggiungere la nota "Esente dal contributo (art. 5 c.2-ter)."
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art5.html (c.2-ter)
- **Certezza:** certo per la protezione speciale; probabile per il 18-ter

### M4. `apolidia`: la conversione in lav_sub applica la norma sbagliata
- **Testo attuale:** "Convertibile in lavoro, salvo che lo straniero fosse in precedenza titolare di permesso per richiesta asilo" (art. 6 c.1-bis lett. d).
- **Problema:** la lett. d riguarda il permesso "per acquisto della cittadinanza o dello stato di apolide" (art. 11 c.1 lett. c DPR 394), cioè il permesso rilasciato mentre il procedimento è in corso. Non riguarda il permesso rilasciato dopo il riconoscimento dello status di apolide. La regola del "salvo ex richiedenti asilo" si applica quindi al permesso in attesa del riconoscimento, non a quello dell'apolide già riconosciuto.
- **Correzione proposta:** cambiare l'esito in "cond" con il testo: "La lett. d dell'art. 6 c.1-bis riguarda il permesso in attesa dell'apolidia (art. 11 c.1 lett. c DPR 394), non convertibile per gli ex richiedenti asilo. Per il permesso dell'apolide riconosciuto la conversione non è disciplinata espressamente." Nota: "Da verificare con le circolari prima di decidere."
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art6.html
- **Certezza:** certo per il contenuto della lett. d; il regime dell'apolide riconosciuto resta da verificare

### M5. `rich_asilo` → `attesa_citt`: la sintesi descrive un'altra regola
- **Testo attuale:** `C("attesa_citt","no","Chi è stato titolare di permesso per richiesta asilo non può convertire il permesso per acquisto cittadinanza o apolidia in lavoro.")`
- **Problema:** la voce dovrebbe dire se dal titolo di richiedente si passa al permesso per attesa cittadinanza. Invece descrive il divieto di conversione attesa_citt → lavoro, che si applica a chi era richiedente asilo e che in effetti è già correttamente indicato nella scheda `attesa_citt`. L'operatore legge un "no" con una motivazione che non c'entra.
- **Correzione proposta:** `C("attesa_citt","cond","Il permesso per acquisto della cittadinanza o apolidia presuppone un permesso per altri motivi (art. 11 c.1 lett. c DPR 394). Se rilasciato a un ex richiedente asilo, non è poi convertibile in lavoro (art. 6 c.1-bis lett. d).",["art. 11 c.1 lett. c DPR 394/1999","art. 6 c.1-bis lett. d TU 286/1998"],None,"Il documento del richiedente rilasciato dal 12/6/2026 non è un permesso di soggiorno: verificare la prassi.")`
- **Fonti:**
  - https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art6.html
  - https://trentininelmondo.it/attachments/article/52/art.11_reg.att._dicembre_2018.pdf
- **Certezza:** probabile

### M6. `assist_fam` (art. 24-bis): manca l'assistenza ai bambini fino a 6 anni
- **Testo attuale:** "Nulla osta fuori quota per assistenza a persona over 80 o con disabilità".
- **Problema:** il DL 146/2025 (art. 5), nel prorogare la misura al 2026-2028, ha esteso l'ingresso fuori quota (10.000 l'anno) all'assistenza dei bambini dalla nascita ai 6 anni (baby sitter). Senza questa voce l'operatore potrebbe ritenere irregolare un nulla osta valido.
- **Correzione proposta:** "Nulla osta fuori quota per assistenza a persona over 80, a persona con disabilità (D.Lgs. 62/2024) o a bambini da 0 a 6 anni (DL 146/2025)". Aggiungere gli alias "baby sitter" e "babysitter".
- **Fonti:**
  - https://temi.camera.it/leg19/provvedimento/d-l-146-2025-disposizioni-urgenti-in-materia-di-ingresso-regolare-di-lavoratori-e-cittadini-stranieri-nonch-di-gestione-del-fenomeno-migratorio.html (testo approvato dalla Camera)
  - https://www.quotidianopiu.it/dettaglio/13594224/convertito-in-legge-il-dl-flussi-tutte-le-modifiche-apportate-dal-parlamento ("baby sitter … entro le 10.000 quote")
- **Certezza:** probabile (confermare sul testo della L. 179/2025)

### M7. Carta blu: il requisito dei 2 anni per il ricongiungimento non si applica
- **Testo attuale** (`carta_blu`, nota): "Applicabilità del requisito dei 2 anni dell'art. 28 c.1-bis ai titolari di Carta blu: da verificare".
- **Problema:** l'art. 28 c.1-bis non menziona la Carta blu. L'art. 27-quater c.16 TU e l'art. 17 della dir. 2021/1883 escludono però che il ricongiungimento dipenda da un periodo minimo di residenza. Prevale la norma speciale di derivazione UE. Lasciare il dubbio può far negare il nulla osta.
- **Correzione proposta:** "Il requisito dei 2 anni dell'art. 28 c.1-bis non si applica: il ricongiungimento del titolare di Carta blu non dipende da un periodo minimo di soggiorno (art. 27-quater c.16 TU; art. 17 dir. 2021/1883)." Aggiungere nella scheda `famiglia`, requisito c.1-bis: "(non per figli minori, titolari di protezione internazionale e titolari di Carta blu)".
- **Fonti:**
  - https://brocardi.it/testo-unico-immigrazione/titolo-iv/art28.html
  - dir. (UE) 2021/1883, art. 17
- **Certezza:** probabile (il comma 16 dell'art. 27-quater non l'ho riscontrato direttamente)

### M8. `studio_form`: manca la conversione in lavoro autonomo; il requisito del "completamento" non è nel TU
- **Testo attuale:** solo `C("lav_sub","si",…,["Completamento del ciclo formativo (da verificare)", …])`.
- **Problema:** l'art. 6 c.1 TU riguarda il permesso per "studio e formazione". Ammette la conversione fuori quota, prima della scadenza, sia con il contratto di soggiorno (subordinato) sia con la certificazione dell'art. 26 (autonomo). Il testo non richiede il completamento del ciclo formativo.
- **Correzione proposta:** nella condizione scrivere "Permesso ancora valido (conversione prima della scadenza)" e, come nota: "Il TU non richiede il completamento del ciclo: eventuali requisiti aggiuntivi vanno verificati sull'art. 14 DPR 394". Aggiungere la conversione in lavoro autonomo (vedi sezione "Conversioni mancanti").
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art6.html
- **Certezza:** certo per il TU; da verificare per il DPR 394

### M9. `lav_stag` → `lav_sub`: la condizione "permesso in corso di validità" è troppo rigida
- **Testo attuale:** condizione "Permesso stagionale in corso di validità". Anche la FAQ dice "con permesso valido".
- **Problema:** l'art. 24 c.10 richiede solo almeno 3 mesi di lavoro regolare e un'offerta di lavoro subordinato a tempo determinato o indeterminato. Non richiede il permesso valido. La giurisprudenza (Cons. Stato n. 7995/2022; TAR Lazio n. 1840/2024) considera il termine "ordinatorio". Il requisito delle 20 ore settimanali e della retribuzione non inferiore all'assegno sociale viene dalle circolari, non dalla legge.
- **Correzione proposta:** sostituire la condizione con "Domanda di norma con permesso valido; un permesso scaduto da poco non è di per sé ostativo secondo la giurisprudenza (CdS 7995/2022)". Sostituire la nota con: "20 ore settimanali e retribuzione ≥ assegno sociale: requisiti di prassi (circolari), non di legge."
- **Fonti:**
  - https://brocardi.it/testo-unico-immigrazione/titolo-iii/art24.html
  - https://www.avvocatofrancescolombardini.it/conversione-permesso-di-soggiorno-stagionale-senza-quote/
- **Certezza:** probabile

### M10. `rifugiato` e `sussidiaria` → `lav_sub`: base normativa assente
- **Testo attuale:** "Convertibile in lavoro fuori quota … art. 23 D.Lgs. 251/2007 … Comma esatto da verificare".
- **Problema:** non ho trovato una norma vigente che preveda la conversione dello status di rifugiato. Per la sussidiaria, fonti datate (INPS, testo originario dell'art. 23 c.2 D.Lgs. 251/2007) la ammettevano "al momento del rinnovo". Fonti divulgative recenti la ammettono con "rinuncia" allo status, ma non citano la norma. Un esito "si" senza norma è rischioso.
- **Correzione proposta:** cambiare l'esito in "cond" con la nota: "Base normativa da verificare (testo vigente dell'art. 23 D.Lgs. 251/2007). Non disporre la conversione senza circolare o indicazione ministeriale; lo status non si perde per effetto della conversione, ma solo per cessazione o revoca."
- **Fonti:**
  - https://servizi2.inps.it/docallegati/Informazioni/lavoratorimigranti/lavorareinitalia/lavoratoreextracomunitario/permessidisoggiorno/Documents/Pds_protezione_sussidiaria.pdf (datata)
  - https://www.leggioggi.it/diritto-immigrazione-come-funziona-la-protezione-sussidiaria/
- **Certezza:** da verificare

### M11. Alias che portano alla scheda sbagliata o che mancano
- **Problemi:**
  - "carta di soggiorno" è alias di `fam_ue`, ma gli operatori usano spesso questo termine per il permesso UE di lungo periodo (ex carta di soggiorno). Rischio di instradamento sbagliato.
  - "volontariato" è alias di `studio_form`, ma il volontariato ha un titolo autonomo (art. 27-bis TU, con contingente triennale dal DL 146/2025).
  - Alias mancanti utili:
    - `prot_speciale`: "motivi umanitari", "umanitario", "ex umanitario", "vita privata e familiare", "art 19";
    - `lungo_periodo`: "permesso ce", "ce soggiornanti", "ex carta di soggiorno", "slp", "lungo soggiornante";
    - `rich_asilo`: "dublino", "c3", "modello c3";
    - `famiglia`: "unione civile", "unito civilmente", "matrimonio", "sposato", "art 29", "art 30";
    - `attesa_occ`: "naspi", "did";
    - `assist_fam`: "baby sitter";
    - `famit`: "coniuge di italiana";
    - `conv_italiano`: "inespellibile".
- **Correzione proposta:**
  - Togliere "carta di soggiorno" da `fam_ue` e mettere al suo posto "carta di soggiorno familiare ue" e "carta familiare". Aggiungere "carta di soggiorno" e "ex carta di soggiorno" a `lungo_periodo`, oppure metterlo come aliasDebole in entrambe le schede.
  - Togliere "volontariato" da `studio_form`.
  - Aggiungere gli alias elencati sopra.
- **Fonte** (per il volontariato): https://temi.camera.it/leg19/provvedimento/d-l-146-2025-disposizioni-urgenti-in-materia-di-ingresso-regolare-di-lavoratori-e-cittadini-stranieri-nonch-di-gestione-del-fenomeno-migratorio.html
- **Certezza:** certo per l'esistenza dell'art. 27-bis; il resto è una valutazione d'uso

### M12. `attesa_occ`: il reddito per il rinnovo va calcolato con i familiari
- **Testo attuale:** "reddito non inferiore all'assegno sociale (7.101,12 € nel 2026) ai sensi dell'art. 29 c.3 lett. b". La FAQ dice lo stesso.
- **Problema:** l'art. 22 c.11 rinvia ai requisiti reddituali dell'art. 29 c.3 lett. b, che crescono con il numero dei familiari a carico (10.651,68 € con 1 familiare e così via). Indicare solo 7.101,12 € può portare a rinnovare chi non ha un reddito sufficiente.
- **Correzione proposta:** "…con un reddito calcolato secondo l'art. 29 c.3 lett. b: almeno 7.101,12 € per il solo titolare, maggiorato della metà dell'assegno sociale per ogni familiare a carico."
- **Fonte:** https://brocardi.it/testo-unico-immigrazione/titolo-iii/art22.html (c.11)
- **Certezza:** probabile (interpretazione del rinvio, coerente con il dato testuale)

### M13. `turismo`: la nota sui diritti propri omette il coniuge di italiano
- **Testo attuale:** "familiare UE o di italiano 'mobile', genitore di minore italiano, convivente con parente italiano entro il 2° grado…".
- **Problema:** l'art. 19 c.2 lett. c protegge anche il coniuge italiano convivente, e dal 2023 esiste il FAMIT (art. 23 c.1-bis), che non richiede uno specifico visto d'ingresso. Così come è scritta, la nota suggerisce che il coniuge di un italiano "statico" entrato come turista non abbia alcun titolo.
- **Correzione proposta:** "…familiare di cittadino UE o di italiano 'mobile' (D.Lgs. 30/2007), familiare di italiano 'statico' (FAMIT, art. 23 c.1-bis; verificare la prassi sul tipo di ingresso), coniuge o parente entro il 2° grado convivente con italiano (art. 19 c.2 lett. c)…". Aggiungere anche `C("famit","cond",…)` (vedi sezione "Conversioni mancanti").
- **Fonti:**
  - https://brocardi.it/testo-unico-immigrazione/titolo-ii/capo-iii/art19.html
  - https://www.esteri.it/wp-content/uploads/2025/12/30_2007.pdf
- **Certezza:** certo per la norma; da verificare per la prassi sul visto

---

## Gravità BASSA

### B1. `prot_speciale` e FAQ: la sentenza CdS 9630/2025 riguarda le cure mediche
- **Testo attuale:** "CdS n. 9630/2025 ha disatteso la circolare dell'1/6/2023" (nella sezione protezione speciale).
- **Problema:** la sentenza (Sez. III, 5/12/2025) riguarda la conversione di un permesso per cure mediche. Per la protezione speciale il principio si applica per analogia, anche richiamando l'art. 7 c.3 DL 20/2023. La sentenza ha disatteso anche la circolare del 29/5/2024.
- **Correzione proposta:** "CdS III, n. 9630/2025 (caso di cure mediche, principio applicabile per analogia): conta la data dell'istanza originaria; disattese le circolari dell'1/6/2023 e del 29/5/2024."
- **Fonte:** https://eius.it/giurisprudenza/2025/7401302
- **Certezza:** certo

### B2. Novità del DL 146/2025: elenchi incompleti
- **Problema:** NORME → "Novità" e `lav_sub.novita` non riportano due modifiche:
  - il contratto di soggiorno va firmato entro 15 giorni dall'ingresso (prima 8). La NORME art. 22 lo dice già correttamente;
  - i termini del nulla osta decorrono dall'assegnazione della quota.
- **Correzione proposta:** aggiungere "contratto di soggiorno entro 15 giorni dall'ingresso (art. 22 c.6); termini del nulla osta dalla data di assegnazione della quota; volontariato con contingente triennale (art. 27-bis)."
- **Fonti:**
  - https://brocardi.it/testo-unico-immigrazione/titolo-iii/art22.html
  - https://temi.camera.it/leg19/provvedimento/d-l-146-2025-disposizioni-urgenti-in-materia-di-ingresso-regolare-di-lavoratori-e-cittadini-stranieri-nonch-di-gestione-del-fenomeno-migratorio.html
- **Certezza:** certo

### B3. `lungo_periodo`: manca la regola del riacquisto dopo la revoca
- **Correzione proposta** (nuova nota): "Chi ha subito la revoca per assenza dall'UE (12 mesi) o dall'Italia (oltre 6 anni) può riottenere il permesso con un periodo di soggiorno ridotto a 3 anni (art. 9 c.8)."
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art9.html
- **Certezza:** probabile

### B4. Ricongiungimento con protezione sussidiaria: formulazioni incoerenti
- **Problema:** le schede non dicono la stessa cosa su chi è esonerato dai requisiti di alloggio e reddito.
  - `famiglia`, nota: "Titolari di protezione internazionale (art. 29-bis): non servono requisiti di alloggio e reddito".
  - NORME art. 29-bis: "Per i titolari dello status di rifugiato".
  - FAQ reddito: "I rifugiati sono esonerati".
- **Correzione:** da verificare. Occorre stabilire se l'art. 29-bis si applica anche alla sussidiaria tramite l'art. 22 D.Lgs. 251/2007. Poi uniformare le tre formulazioni.
- **Certezza:** da verificare

### B5. `art18ter`: posizione rispetto al permesso UE di lungo periodo
- **Problema:** l'art. 9 c.3 lett. b (Brocardi, testo al 16/7/2026) cita ancora l'art. 22 c.12-quater e non il 18-ter. La scheda `art18ter` non dice nulla sul lungo periodo.
- **Correzione:** da verificare. Se il rinvio va letto come riferito al 18-ter, aggiungere `C("lungo_periodo","no",…)`.
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-ii/capo-i/art9.html
- **Certezza:** da verificare

### B6. Tipi di permesso assenti
- **Problema:** mancano alcune schede:
  - volontariato (art. 27-bis TU);
  - cittadini britannici beneficiari dell'Accordo di recesso (art. 18 dell'Accordo, "Brexit");
  - vacanza-lavoro (accordi bilaterali).
- **Correzione:** valutare se aggiungere le schede. Al momento una ricerca su questi casi non trova nulla oppure porta a schede sbagliate.
- **Certezza:** certo per il volontariato; gli altri sono da verificare

### B7. Dati non confermati, già marcati dalla banca dati: restano "da verificare"
- DL 168/2026: proroga della fase transitoria al 30/4/2027 e documento valido 1 anno. Non ho trovato il testo. La data del 30/4/2027 è coerente con la nota INL del 12/10/2026, prot. 2221 (https://www.mysolution.it/lavoro/informazioni/news/2026/10/28/i-chiarimenti-inl-sullinstaurazione-di-rapporto-di-lavoro-con-richiedenti-protezione-internazionale/), che cita solo il DL 100/2026.
- Quota lavoro autonomo 2026 (650).
- Durata "al rinnovo fino a 3 anni" del permesso per famiglia: Brocardi non la conferma per l'art. 30.
- Permesso `ricerca_lav`: requisito del reddito pari all'assegno sociale.

### B8. `minore_eta`: etichetta della conversione in `attesa_occ`
- **Problema:** il permesso "per accesso al lavoro" dell'art. 32 non coincide con l'attesa occupazione dell'art. 22 c.11.
- **Correzione proposta:** nella sintesi scrivere "Al compimento dei 18 anni: permesso per accesso al lavoro (art. 32 c.1), che non richiede i requisiti dell'art. 23; disciplina analoga all'attesa occupazione."
- **Fonte:** https://www.brocardi.it/testo-unico-immigrazione/titolo-iv/art32.html
- **Certezza:** certo

---

## Affermazioni controllate e risultate corrette (sintesi)

- **Art. 5, termini (D.Lgs. 83/2026, in vigore dal 22/5/2026):** rinnovo da chiedere 90 giorni prima della scadenza; termine del c.9 di 90 giorni; permesso unico rilasciato entro 30 giorni (c.8.1-bis); esclusioni dell'art. 5 c.8.2 come riportate.
- **Art. 29:** nulla osta al ricongiungimento entro 150 giorni (c.8). Requisiti e importi di reddito 2026 coerenti con un assegno sociale di 546,24 €/mese.
- **Art. 28 c.1-bis:** requisito dei 2 anni per i familiari delle lett. a, c, d dell'art. 29; esclusa la protezione internazionale.
- **Art. 18:** durata 1 anno, rinnovabile per 1 anno; commi 3-ter/3-quinquies (45 giorni) dal D.Lgs. 115/2026.
- **Art. 20-bis:** 6 mesi + 6, consente il lavoro, non convertibile.
- **Art. 19 c.2 lett. d-bis:** permesso per cure mediche fino a 1 anno, valido solo in Italia; il lavoro non è menzionato.
- **Art. 6 c.1 e c.1-bis:** lettere vigenti e abrogate come riportate. Conversione studio → lavoro fuori quota e prima della scadenza.
- **Art. 29 c.6:** il contrasto con l'art. 6 c.1-bis lett. h esiste davvero, quindi l'esito "cond" è corretto.
- **Art. 22:** nulla osta valido 6 mesi; c.11 come riportato.
- **Art. 24:** durata massima 9 mesi su 12; c.8 SIIL/SIISL.
- **Art. 9:** esenzioni dal test di italiano (ricercatori, protezione internazionale); esonero dall'alloggio per la protezione internazionale (c.1-ter); documento valido 10 o 5 anni; regole di revoca.
- **Art. 9-bis:** lavoro fuori quota (DL 145/2024).
- **Permesso per asilo e sussidiaria:** 5 anni (AIDA Italia, aggiornamento del 14/9/2026).
- **Richiedente asilo:** lavoro dopo 90 giorni (DL 100/2026).
- **Carta blu:** soglia di circa 36.300 €.
- **Protezione temporanea:** proroga UE al 4/3/2028.
- **Corte cost. 376/2000** (permesso al marito convivente nel caso di gravidanza).

---

## Conversioni mancanti da aggiungere

```python
# valore_civile (art. 42-bis): esclusione espressa dall'art. 9 c.3 lett. b
C("lungo_periodo","no","Escluso dal permesso UE di lungo periodo.",["art. 9 c.3 lett. b TU 286/1998"])

# studio_form -> lavoro autonomo (art. 6 c.1: 'studio e formazione', certificazione art. 26)
C("lav_aut","si","Ammessa fuori quota, prima della scadenza, con la certificazione dei requisiti dell'art. 26.",["art. 6 c.1 TU 286/1998","art. 26 TU 286/1998"],["Permesso ancora valido","Certificazione dei requisiti dell'art. 26"])

# studio_form -> famiglia (coesione)
C("famiglia","si","Coesione familiare se ricorrono i requisiti del ricongiungimento.",["art. 30 c.1 lett. c TU 286/1998"],["Requisiti dell'art. 29 c.3 in capo al familiare","Domanda anche entro 1 anno dalla scadenza del titolo"])

# famit -> lavoro autonomo
C("lav_aut","si","Convertibile in permesso per motivi di lavoro, anche autonomo.",["art. 23 c.1-bis D.Lgs. 30/2007","art. 26 TU 286/1998"],["Requisiti dell'art. 26"],"La norma dice 'motivi di lavoro' senza distinguere.")

# attesa_citt -> lavoro autonomo
C("lav_aut","si","Convertibile in lavoro ove ne ricorrano i requisiti, tranne per gli ex richiedenti asilo.",["art. 6 c.1-bis lett. d TU 286/1998","art. 26 TU 286/1998"],["Non provenire da un permesso per richiesta di asilo","Requisiti dell'art. 26"],"L'art. 6 c.1-bis parla di 'motivi di lavoro': verificare la prassi per l'autonomo.")

# res_el_pens, religiosi -> lavoro autonomo (stessa base)
C("lav_aut","cond","Convertibile in permesso per motivi di lavoro ove ne ricorrano i requisiti; per l'autonomo servono i requisiti dell'art. 26.",["art. 6 c.1-bis lett. c (o g) TU 286/1998","art. 26 TU 286/1998"],["Requisiti dell'art. 26"],"Estensione all'autonomo da verificare con la prassi.")

# lav_aut -> attesa occupazione (esito negativo esplicito, evita equivoci)
C("attesa_occ","no","L'art. 22 c.11 riguarda solo la perdita del lavoro subordinato.",["art. 22 c.11 TU 286/1998"])

# attesa_occ -> lungo periodo
C("lungo_periodo","cond","Dopo 5 anni di permesso valido, con i requisiti dell'art. 9.",["art. 9 TU 286/1998"],["Reddito non inferiore all'assegno sociale","Test A2 o esonero"])

# minore_eta -> famiglia (minore affidato o in tutela)
C("famiglia","cond","Il minore affidato, anche di fatto, o sottoposto a tutela ottiene il permesso per motivi familiari.",["art. 10 L. 47/2017"],["Provvedimento di affidamento o di tutela"])

# minore_eta -> cure (art. 32 c.1)
C("cure_mediche","cond","Al compimento dei 18 anni è possibile il permesso per esigenze sanitarie o di cura.",["art. 32 c.1 TU 286/1998"],["Documentazione sanitaria"])

# turismo -> famit (rilascio autonomo, non conversione)
C("famit","cond","Non è una conversione: il familiare di italiano 'statico' può ottenere il FAMIT se ricorre il vincolo familiare e c'è convivenza.",["art. 23 c.1-bis D.Lgs. 30/2007","art. 19 c.2 lett. c TU 286/1998"],["Vincolo familiare con cittadino italiano","Convivenza effettiva"],"Prassi sul tipo di ingresso da verificare.")

# rich_asilo -> famit / fam_ue (diritto proprio)
C("famit","cond","Non è una conversione: se nasce il vincolo con un cittadino italiano 'statico' il FAMIT è rilasciato autonomamente.",["art. 23 c.1-bis D.Lgs. 30/2007"],["Vincolo familiare e convivenza"],"Verificare la prassi della Questura sulla rinuncia alla domanda di protezione.")

# prot_speciale -> famiglia (coesione)
C("famiglia","cond","Coesione familiare ex art. 30 c.1 lett. c se ricorrono i requisiti; il DL 20/2023 ha abolito solo la convertibilità in lavoro.",["art. 30 c.1 lett. c TU 286/1998"],["Requisiti del ricongiungimento in capo al familiare"],"Da verificare: prassi ministeriale non trovata.")

# carta_blu -> famiglia (non serve: già garantito il ricongiungimento) -- opzionale
C("famiglia","si","Coesione familiare se ricorrono i requisiti.",["art. 30 c.1 TU 286/1998"])
```

Le voci con nota "da verificare" non vanno applicate prima di aver confermato la prassi o il testo.

---

## Riepilogo dei conteggi
- **ALTA:** 6 (A1–A6)
- **MEDIA:** 13 (M1–M13)
- **BASSA:** 8 (B1–B8)
