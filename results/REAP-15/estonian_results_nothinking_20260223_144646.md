# Estonian Language Smoke Test
**Model:** `/workspace/models/Qwen3.5-397B-A17B-REAP-15`
**Mode:** `no-thinking`
**Sampling:** `temp=0.7, top_p=0.8, top_k=20, min_p=0.0`
**Date:** 2026-02-23 14:46
**API:** `http://localhost:8000/v1/chat/completions`
**Completed:** 16/16 tests returned responses

---
## 01_orthography: Orthography Stress Test (õ, ü, ö, ä)

**Prompt:**
```
Kirjuta lühike lõik (5-6 lauset) teemal: 'Põõsaste taga ööbinud öökull lendas üle jõe ja nägi õunapuud.' Kasuta võimalikult palju sõnu, mis sisaldavad tähti õ, ü, ö ja ä. Kirjuta ainult eesti keeles.
```

**Response:**

Öösel ärgates hüppas öökull põõsaste tagant välja ja tõusis õhku.
Ta lendas üle jõe, kus vesi oli sügav ja pime.
Äkki nägi lind vastas kaldal suurt õunapuud, mis oli täis punaseid õunu.
Öökull mõtles, et see on väga hea koht ööbimiseks ja saagi jahtimiseks.
Ta laskus vaikselt puu otsa, et vaadata ümber hämaras öös.
Nüüd on tal soe peidukoht ja küllalt süüa kogu ülejäänud ööks.

**Evaluation criteria:**
Watch for: õ vs o, ü vs y/u, ö vs o, ä vs a. The prompt itself contains many of these characters as anchors.

---
## 02_cases: Case System (14 cases with 'jõgi')

**Prompt:**
```
Käänake sõna 'jõgi' läbi kõigi 14 eesti keele käände. Formaat: käände nimi - sõnavorm. Ainult eesti keeles.
```

**Response:**

Nimetav - jõgi
Omastav - jõe
Osastav - jõge
Sisseütlev - jõkke
Seesütlev - jões
Seestütlev - jõest
Alaleütlev - jõele
Alalütlev - jõel
Alaltütlev - jõelt
Saav - jõeks
Rajav - jõeni
Rajav - jõena
Kaasaütlev - jõega
Ilmaütlev - jõeta

**Evaluation criteria:**
Correct: nimetav-jõgi, omastav-jõe, osastav-jõge, sisseütlev-jõkke, seesütlev-jões, seestütlev-jõest, alaleütlev-jõele, alalütlev-jõel, alaltütlev-jõelt, saav-jõeks, rajav-jõeni, olev-jõena, ilmaütlev-jõeta, kaasaütlev-jõega

---
## 03_idioms: Estonian Idioms & Proverbs

**Prompt:**
```
Nimeta 5 eesti vanasõna ja selgita lühidalt nende tähendust. Ainult eesti keeles.
```

**Response:**

Siin on viis eesti vanasõna koos nende lühikeste selgitustega:

1. **Kes teisele auku kaevab, see ise sisse kukub.**
   See tähendab, et halbade kavatsustega teistele kahju soovija või tembu kavandaja satub lõpuks ise oma lõksu või kannatab oma tegude pärast.

2. **Ega ometi kõik ühe mõõduga mõõdetud ole.**
   See väljend tõdeb, et inimesed on erinevad – neil on erinevad oskused, iseloomud ja võimed, seega ei saa kõiki kohelda või hinnata samade reeglite järgi.

3. **Kus kitsas, seal läbi.**
   See vanasõna julgustab leidlikkusele ja visadusele: isegi kui olukord tundub lootusetu või takistused suured, leiab tahtejõuline inimene alati lahenduse või tee edasi.

4. **Hommik on õhtut targem.**
   See soovitab mitte teha kiirustades otsuseid või lahendada probleeme väsinuna; pärast puhkamist ja ööd magamist on mõistus selgem ja lahendus tuleb kergemini leida.

5. **Mis tehtud, see tehtud.**
   See tähendab, et minevikusündmusi ei saa muuta, seega tuleb aktsepteerida toimunut ja keskenduda sellele, kuidas edasi elada, selle asemel et asjatult muretseda.

**Evaluation criteria:**
Should be actual Estonian proverbs, not translated generic ones. Watch for natural explanations.

---
## 04_error_detection: Error Detection in Broken Estonian

**Prompt:**
```
Järgmises tekstis on mitu viga. Leia ja paranda need:

'Eile ommikul läksin ma pöodi ja ostsin kolm kilogrammi ounapuid. Poodi jöudes märkasin, et mul polnud rahakoti kaasas. Onneks oli mul telefonis maksmise vöimalus.'

Nimeta iga viga ja selgita, mis on õige vorm.
```

**Response:**

Selles lühikeses tekstis on kokku **kuus** viga, mis puudutavad õigekirja (tähestikku) ja grammatikat (käändeid).

Siin on vigade analüüs ja parandused:

1.  **Viga:** *ommikul*
    *   **Selgitus:** Sõnas on vale täht. Eesti keeles kirjutatakse see sõna kahe 'h'-ga.
    *   **Õige vorm:** **hommikul**

2.  **Viga:** *pöodi*
    *   **Selgitus:** Siin on kasutatud vale tähte. Sõna "pood" seeskäändes (kust? kuhu?) kirjutatakse 'oo'-ga, mitte 'ö'-ga.
    *   **Õige vorm:** **poodi**

3.  **Viga:** *ounapuid*
    *   **Selgitus:** Tekstis on kaks probleemi. Esiteks puudub täht 'õ' (peab olema *õun*). Teiseks on vale sõnavalik: "õunapuu" on puu ise, mida aeda istutatakse. Poest ostetakse söögiks **õunu**.
    *   **Õige vorm:** **õunu** (kontekstist lähtuvalt; kui oleks tegemist istikutega, oleks õige *õunapuid*, kuid siis peaks olema ka 'õ').

4.  **Viga:** *jöudes*
    *   **Selgitus:** Puudub umlaut (kaks punkti). Tegusõna "jõudma" da-tegevusnimi nõuab tähte 'õ'.
    *   **Õige vorm:** **jõudes**

5.  **Viga:** *rahakoti*
    *   **Selgitus:** Grammatiline viga. Lause tähendus on "mul polnud rahakotti [kaasas]". Siin on vaja sihitavat käänet (osastav), mitte omastavat käänet. Küsimus on: "Mida mul polnud?" – Vastus: "Rahakotti".
    *   **Õige vorm:** **rahakotti**

6.  **Viga:** *vöimalus*
    *   **Selgitus:** Vale täht. Sõnas peab olema 'õ', mitte 'ö'.
    *   **Õige vorm:** **võimalus**

---

### Parandatud tekst:

"Eile **hommikul** läksin ma **poodi** ja ostsin kolm kilogrammi **õunu**. Poodi **jõudes** märkasin, et mul polnud **rahakotti** kaasas. Onneks oli mul telefonis maksmise **võimalus**."

**Evaluation criteria:**
Must catch: ommikul→hommikul, pöodi→poodi, ounapuid→õunapuid, jöudes→jõudes, Onneks→Õnneks, vöimalus→võimalus. Key test: does it catch õ/ö swaps?

---
## 05_natural_generation: Natural Text Generation

**Prompt:**
```
Kirjuta lühijutt (umbes 150 sõna) mehest, kes esimest korda Tallinna vanalinna külastab. Kirjelda tema emotsioone ja mida ta näeb. Ainult eesti keeles.
```

**Response:**

Jaan astus bussist maha ja hingas sügavalt sisse. Õhk lõhnas vanade kivide ja mere järele. Tema ees kõrgusid Toompea müürid, mis paistsid päikesevalguses kuldsetena. See oli tema esimene kord Tallinna vanalinnas ja süda peksis põnevusest kiiremini.

Ta astus läbi Suur-Rannavärava ja tundis, nagu astuks ajas tagasi. Munakivised tänavad särasid pärast hommikust vihma ja vanad majad vaatasid teda oma värviliste fassaadidega. Igal sammul avanes uus vaade: kitsad käänulised tänavad, rohelised hoovid ja kauguses paistvad kirikutornid. Jaan peatus Raekoja platsil, kus turistid naersid ja linnud tiirlesid üle pea. Ta tundis end väikesena selle ajaloo hiilguse ees, kuid samas ka imeliselt vabana.

Emotsioonid segunesid – oli imetlust, rahulikkust ja kerget nostalgiat millegi järele, mida ta polnud kunagi varem kogenud. Ta teadis juba siis, et see linn jääb tema südamesse igaveseks. Tallinn ei olnud lihtsalt sihtkoht, vaid elamus, mis muutis ta pilku maailmale.

**Evaluation criteria:**
Look for: natural flow, correct word order (SOV tendencies in Estonian), proper case usage on place names, no character-level errors.

---
## 06_translation_traps: Translation with Structural Traps

**Prompt:**
```
Tõlgi järgmised laused inglise keelest eesti keelde:
1. 'I have been living in Tallinn for five years.'
2. 'The book that my grandmother gave me is on the table.'
3. 'If it hadn't rained yesterday, we would have gone to the beach.'
4. 'She told me she wouldn't be coming.'
5. 'The older I get, the less I understand.'
```

**Response:**

1. Ma olen elanud Tallinnas viis aastat.  
2. Raamat, mille vanaema mulle kinkis, on laual.  
3. Kui eile poleks sadanud, oleksime läinud randa.  
4. Ta ütles mulle, et ta ei tule.  
5. Mida vanemaks ma saan, seda vähem ma aru saan.

**Evaluation criteria:**
Traps: #1 continuous aspect (Estonian doesn't have it), #2 relative clause structure, #3 conditional/irreaalis mood, #4 reported speech, #5 comparative construction 'mida...seda'. Estonian handles all of these very differently from English.

---
## 07_gradation: Consonant Gradation & Short Illative

**Prompt:**
```
Kääna sõnu "siga", "kallas" ja "tuba" ainsuse osastavas, ainsuse sisseütlevas ja mitmuse omastavas käändes.
Seejärel moodusta iga sõnaga üks loomulik lause, kasutades lühikest sisseütlevat käänet (kui see on võimalik).
```

**Response:**

Siin on sõnade "siga", "kallas" ja "tuba" käändevormid ning näitelauseid:

### 1. Käändevormid

| Sõna | Ainsuse osastav (Keda? Mida?) | Ainsuse sisseütlev (Kellesse? Millesse?) | Mitmuse omastav (Kelle? Mille?) |
| :--- | :--- | :--- | :--- |
| **siga** | siga | **sigasse** | sigade |
| **kallas** | kallast | **kallasse** | kallaste |
| **tuba** | tuba | **tuppa** (erivorm) | tubade |

*Märkus: Sõna "tuba" sisseütlev kääne on erandlik ja lühike vorm on "tuppa", mitte "toasse".*

---

### 2. Näitelauseid (kasutades lühikest sisseütlevat käänet)

Lühike sisseütlev kääne lõpeb eesti keeles täishäälikule (-sse asemel -a, -e, -i, -o, -u või erivormid nagu -le, -sse -> -pa jne).

*   **Siga:**
    *   Lause: Poiss viskas õuna **siga**.
    *   *(Selgitus: Tavapärane pikk vorm oleks "sigasse", kuid kõnekeeles ja murdes kasutatakse sageli lühikest vormi "siga", kuigi kirjakeeles on see haruldane. Alternatiivina loomulikumale kontekstile: "Ta ajas sea **karja**" – siin on 'karja' juba lühike sisseütlev, aga kui tingimata kasutada sõna 'siga' lühikeses sisseütlevas, siis see on stilistiliselt piiratud. Õigem näide lühikese sisseütleva reegliga sõnale, mis seda lubab, oleks raske leida just sõnale "siga", kuna standardses kirjakeeles domineerib "sigasse". Proovime konteksti, kus see kõlab loomulikuna murdelises või vanemas kõnes, või valime sõna, millel on kindel lühike vorm.)*

    *Korrigeerime lähenemist:* Ülesanne palus moodustada lause **lühikest sisseütlevat käänet kasutades, kui see on võimalik**.
    *   Sõnal **siga** ei ole standardses kirjakeeles üldlevinud lühikest sisseütlevat vormi (nagu "majja" või "linnade"). Vorm "siga" on osastav või nimetav. Seega selle sõnaga lühikest sisseütlevat lauset moodustada **ei ole** standardses keeles võimalik. Kasutame pikka vormi või märgime erandi.
    *   Sõnal **kallas** on lühike vorm **kallale** (suunamine pinnale) või **kallasse** (pikk). Oota, "kallale" on alaleütlev. Sisseütlev on ainult "kallasse". Lühikest sisseütlevat (nt *metsa*, *linna*) sõnal "kallas" ei ole.
    *   Sõnal **tuba** on lühike sisseütlev **tuppa**. See on ainus neist kolmest, millel on väga levinud ja kohustuslik lühike vorm.

    *Parandus ülesande tõlgendamisel:* Ilmselt oli eesmärk harjutada sõnu, millel lühike vorm eksisteerib, või tuvastada, et kõigil seda pole. Kuna "siga" ja "kallas" ei oma produktiivset lühikest sisseütlevat vormi (nagu *majja*, *patta*, *tuppa*), siis teen laused nende jaoks tavapärase pikaga või otsin konteksti, kus küsitakse "kuhu?".

    Vaatame uuesti reeglit: Lühike sisseütlev tekib sageli sõnadel, mis lõpevad -a, -e, -i, -o, -u (nt *maja* -> *maja*, *küla* -> *küla*? Ei, *majja*, *külasse*).
    Tegelikult on lühike sisseütlev iseloomulik sõnatüüpidele, mille tüvi lõpeb täishäälikuga või on muundunud (nt *vesi* -> *vette*, *tuba* -> *tuppa*, *süda* -> *südame*?).
    
    Tõde on see:
    1. **Tuba** -> **tuppa** (Lühike vorm on olemas ja ainuvõimalik).
    2. **Siga** -> **sigasse** (Lühikest vormi "siga" sisseütlevana ei eksisteeri, see on osastav/nimetav).
    3. **Kallas** -> **kallasse** (Lühikest vormi ei ole).

    Kuna ülesanne küsis "kasutades lühikest sisseütlevat käänet (kui see on võimalik)", siis teen lause sõnaga **tuba**, mis on ainus sobiv kandidaat. Teiste sõnade puhul näitan, et see pole võimalik, või kasutan pikka vormi, märkides tingimust.

    *Alternatiivne tõlgendus:* Äkki mõeldi sõnu, millel *on* lühike vorm? Kui kasutaja andis need konkreetsed sõnad, siis tuleb olla täpne.
    
    Teeme nii:
    1. **Siga**: Lühike sisseütlev puudub. Lause pikk vormiga (või märkus).
    2. **Kallas**: Lühike sisseütlev puudub.
    3. **Tuba**: Lühike sisseütlev on **tuppa**.

    Kuid et vastata kasutaja ootusele "moodusta iga sõnaga...", proovin leida konteksti või selgitada. Aga oota, äkki on mõni murdevorm või vananenud vorm? Ei, hariduslikus kontekstis peab tuginema standardkeelele.
    
    **Otsus:** Ma toon välja, et ainult sõnal "tuba" on lühike sisseütlev kääne. Teiste puhul kasutan pikka vormi, kuna lühikest ei eksisteeri, või jätan lause tegemata, kui tingimus on range. Parem on olla abivalmis ja teha lause õige käändega, märkides erinevust.

    *Uuesti kontrollin:* Kas "kallas" võib olla "kallale"? Ei, see on alaleütlev (onto the bank). Sisseütlev on "into the bank/shore" -> "kallasse".
    Kas "siga" võib olla "sialle"? Ei.
    
    Seega: Ainult **tuba** -> **tuppa**.
    
    Kuid kasutaja küsis: "moodusta iga sõnaga üks loomulik lause, kasutades lühikest sisseütlevat käänet (kui see on võimalik)".
    See tähendab: kui võimalik, tee lühikesega; kui mitte, siis ilmselt ei saa teha või teeb pikaga.
    
    Kirjutan vastuse nii, et toon esile fakti, et ainult "tuba" lubab lühikest vormi, ja teen laused vastavalt.

    **Lause 1 (siga):** Kuna lühikest vormi pole, kasutan pikka või selgitan. Aga äkki kasutaja arvab, et "siga" on lühike vorm? Ei, "siga" on osastav.
    Võtan vabaduse teha laused õigete vormidega ja kommenteerin lühikest vormi.
    
    *Parandus:* Äkki mõtles kasutaja sõnu, millel on lühike vorm, aga valis need juhuslikult? Või on see test, et ma teaks, et kõigil ei ole.
    
    Teeme nii:
    1. **Siga**: Lühike vorm puudub. Lause: "Talunik viis sööda **sigasse**." (Pikk vorm).
    2. **Kallas**: Lühike vorm puudub. Lause: "Paat sõitis **kallasse**." (Pikk vorm).
    3. **Tuba**: Lühike vorm on **tuppa**. Lause: "Lapsed jooksid **tuppa**."

    Ootan, kas on mõni varjatud lühike vorm?
    Mõned allikad võivad lugeda -sse lõpulisi sõnu, kus 's' on kadunud? Ei.
    
    Ok, vastan ausalt: ainult "tuba" puhul on see võimalik.

    **Vastuse struktuur:**
    1. Tabel käändevormidega.
    2. Lause iga sõnaga. Sõnade "siga" ja "kallas" puhul märgin, et lühike sisseütlev puudub ja kasutan standardset pikka vormi, sest tingimus oli "kui see on võimalik". Sõna "tuba" puhul kasutan lühikest vormi "tuppa".

    *Self-correction*: Kas on võimalik, et kasutaja segab alaleütlevat (kallale) ja sisseütlevat? Või tahab lihtsalt harjutust. Ma selgitan lahenduses.

    **Lõplik plaan:**
    - Näitan käändeid.
    - Sõna "siga": Lühike sisseütlev puudub. Lause pikk vormiga.
    - Sõna "kallas": Lühike sisseütlev puudub. Lause pikk vormiga.
    - Sõna "tuba": Lühike sisseütlev on "tuppa". Lause lühike vormiga.

    *Wait, is there any dialectal short illative for 'siga'?* No, not in standard.
    *Is there for 'kallas'?* No.

    Let's draft the response.

    **Sõna: siga**
    Osastav: siga
    Sisseütlev: sigasse (lühikest pole)
    Mitmuse omastav: sigade
    Lause: Talupidaja sulges sea **sigasse** (või aedikusse). *Kuna lühikest vormi ei ole, kasutan pikka.*

    **Sõna: kallas**
    Osastav: kallast
    Sisseütlev: kallasse (lühikest pole)
    Mitmuse omastav: kallaste
    Lause: Laine lõi tugevalt **kallasse**.

    **Sõna: tuba**
    Osastav: tuba
    Sisseütlev: tuppa (lühike vorm!)
    Mitmuse omastav: tubade
    Lause: Külalised astusid soojuse eest **tuppa**.

    See on kõige korrektsem lähenemine.

**Evaluation criteria:**
siga: osastav=siga, sisseütlev=sigasse (no short illative), mitm.omastav=sigade. kallas: osastav=kallast, sisseütlev=kaldasse, mitm.omastav=kallaste. tuba: osastav=tuba, sisseütlev=tuppa (THE trap — 'tuppa' not 'tubasse'). If model writes 'tubasse', it fails native fluency.

---
## 08_semantic_traps: Semantic Traps (enamus/enamik, õieti/õigesti)

**Prompt:**
```
Selgita lühidalt ja konkreetselt, mis vahe on sõnadel "enamus" ja "enamik" ning "õieti" ja "õigesti".
Paranda järgmised laused, kui neis on vigu, ja põhjenda parandust:
1. Enamus inimesi eelistab suvel puhata.
2. Ma ei teinud seda matemaatika ülesannet õieti, sest reegel oli keeruline.
3. Peale söömist läksime kinno.
```

**Response:**

Siin on lühike ja konkreetne selgitus sõnade tähenduse ning lausete parandus.

### Sõnade erinevus

1.  **Enamus vs. Enamik**
    *   **Enamus** tähendab *hääletamisel või otsustamisel* üle poole häältest (nt "lihtne enamus", "kahekolmandikuline enamus"). See on protseduuriline mõiste.
    *   **Enamik** tähendab *suuremat osa* tervikust (inimestest, asjadest, ajast).
    *   *Reegel:* Kui räägid inimeste hulgast või asjade osakaalust, kasuta alati **enamik**. "Enamus inimesi" on vigane väljend.

2.  **Õieti vs. Õigesti**
    *   **Õieti** tähendab *sobivalt, targasti, mõistlikult* või *tegelikkuses* (nt "sa käitusid õieti", "mis sul õieti viga on?").
    *   **Õigesti** tähendab *veatult, reeglitele vastavalt* (nt "lahendasid ülesande õigesti").
    *   *Reegel:* Kui on tegemist faktiväitega või reegli järgimisega, kasuta **õigesti**.

---

### Lausete parandus ja põhjendus

**1. Algne:** Enamus inimesi eelistab suvel puhata.
*   **Parandus:** **Enamik** inimesi eelistab suvel puhata.
*   **Põhjendus:** Siin viidatakse inimeste suuremale osale, mitte hääletustulemusele. Seetõttu tuleb kasutada sõna *enamik*. Sõna "enamus" sobib vaid kontekstidesse nagu "saavutasime koosolekul enamuse".

**2. Algne:** Ma ei teinud seda matemaatika ülesannet õieti, sest reegel oli keeruline.
*   **Parandus:** Ma ei teinud seda matemaatika ülesannet **õigesti**, sest reegel oli keeruline.
*   **Põhjendus:** Matemaatikaülesande lahendamisel on oluline, kas tulemus vastab reeglitele (veatult). Seetõttu on õige vorm *õigesti*. Sõna *õieti* sobiks siia ainult siis, kui tahaksid öelda, et ülesande tegemine ei olnud üldse mõistlik tegu (nt "sa ei teinud õieti, et üldse seda proovisid").

**3. Algne:** Peale söömist läksime kinno.
*   **Parandus:** **Pärast** söömist läksime kinno.
*   **Põhjendus:** Kuigi kõnekeeles kasutatakse sageli "peale", on kirjakeeles ajalise järgnevuse väljendamisel (millal?) õige kasutada sõna **pärast**. Sõna "peale" näitab kirjakeeles peamiselt asukohta (millelegi peale) või suunda (millelegi peale).

**Evaluation criteria:**
Must correct: 1) Enamus→Enamik (enamik='greater part', enamus='numerical majority'). 2) õieti→õigesti (õieti='actually', õigesti='correctly'). 3) Peale→Pärast (peale='in addition to/onto', pärast='after in time').

---
## 09_participles: Gerunds and Participles (Compressed Clauses)

**Prompt:**
```
Sõnasta järgmised laused ümber, kasutades lühendatud lauseehitust (näiteks des-vormi või kesksõnu), ilma et lause põhimõte muutuks. Tee seda võimalikult loomulikus eesti keeles.
1. Kui ma kõndisin mööda tänavat, nägin ma vana tuttavat.
2. Koer, kes oli terve öö haukunud, jäi lõpuks hommikul magama.
3. See on raamat, mida loetakse praegu igas koolis.
```

**Response:**

Siin on laused ümber sõnastatud, kasutades lühendatud lauseehitust (des-vormid ja kesksõnad), et kõlada loomulikus eesti keeles:

1. **Tänaval kõndides** nägin ma vana tuttavat.
   *(Algne: Kui ma kõndisin mööda tänavat...)*

2. **Terve öö haukunud** koer jäi lõpuks hommikul magama.
   *(Algne: Koer, kes oli terve öö haukunud...)*

3. See on raamat, mida **praegu igas koolis loetakse**.
   *(Märkus: Selles lauses on algne laiendatud määrus juba üsna tihe. Veelgi lühem variant oleks kasutada umbmäärast kesksõna: "See on **praegu igas koolis loetav** raamat", kuid see muudab rõhku veidi rohkem raamatu omadusele kui tegevuse toimumisele. Esimene variant säilitab algse lause dünaamika kõige paremini.)*

**Evaluation criteria:**
Expected: 1) 'Mööda tänavat kõndides nägin...' 2) 'Terve öö haukunud koer jäi...' 3) 'See on praegu igas koolis loetav raamat.' Tests des-form and participle compressions that English-trained models struggle with.

---
## 10_cultural_proverbs: Cultural Proverbs (Deep Estonian)

**Prompt:**
```
Mida tähendavad järgmised eesti vanasõnad ja kõnekäänud? Anna igaühe kohta lühike selgitus ja mõtle üks igapäevane eluline olukord, kus seda väljendit sobiks kasutada.
1. Pill tuleb pika ilu peale.
2. Igal oinal oma mihklipäev.
3. Karuteenus.
```

**Response:**

Siin on nende eesti vanasõnade ja kõnekäändude tähendused koos sobivate eluliste näidetega:

### 1. Pill tuleb pika ilu peale
**Tähendus:** See vanasõna hoiatab, et liigne uhkustamine, edvistamine või mõõtmetest suurem elamine toob lõpuks kaasa hävingu või tagasilöögi. Mida kõrgemale inimene ennast kiidab või mida rohkem ta ressurssidest üle oma võimete elab, seda valusam on kukkumine.

**Eluline olukord:**
Sõber laenab pangast suure summa raha, et osta endale kallim auto, kui ta tegelikult tasku lubab, ja kiidab kõigile, kui edukalt tal läheb. Kui aga paari kuu pärast tuleb töökoht ootamatult kaotada ja ta ei suuda enam laenumakseid tasuda, võib keegi öelda: *"Näed, sa tahtsid kõigile näidata, kui rikas sa oled, aga nüüd oled võlgades – pill tuleb ikka pika ilu peale."*

---

### 2. Igal oinal oma mihklipäev
**Tähendus:** See ütlus tähendab, et igaühel saabub varem või hiljem hetk, mil ta peab oma tegude eest vastutama või karistust saama. "Mihklipäev" (29. september) oli traditsiooniliselt päev, mil lambaid ja kitsi (rahvakeeles sageli "oinaid") tapeti või renditingimusi muudeti, seega sümboliseerib see paratamatut kohtupäeva või pöördelist momenti.

**Eluline olukord:**
Koolis on õpilane, kes on terve aasta tunnist puudunud, kodutöid teinud ja õpetajat narrinud, arvates, et talle ei juhtu midagi. Kui aga aasta lõpus selgub, et ta peab klassi kordama, võib õpetaja või vanem kommenteerida: *"Sa arvasid, et saad nii lihtsalt läbi, aga eks igal oinal oma mihklipäev – nüüd tuleb suvi koolipingis veeta."*

---

### 3. Karuteenus
**Tähendus:** Karuteenus on tegu, mis on kavatsuslikult tehtud kellegi aitamiseks või heaks, kuid mis tegelikult toob sellele inimesele rohkem kahju kui kasu. Väljend pärineb La Fontaine'i valmist, kus karu tahtis kärbest oma magava sõbra näolt peletada ja viskas selle pihta raske kiviga, tappes sellega sõbra.

**Eluline olukord:**
Ema tahab oma täiskasvanud last aidata ja nõustub tema eest kogu aeg nõusid pesema ja tuba koristama, et lapsel oleks rohkem aega õppimiseks. Tulemuseks on aga see, et laps ei õpi kunagi iseseisvalt hakkama saama ega tule toime oma kohustustega, kui ema parasjagu kõrval ei ole. Sellises situatsioonis võib isa öelda: *"Sa teed talle ainult karuteenust; kui sa tema eest kõik ära teed, ei õpi ta kunagi vastutust võtma."*

**Evaluation criteria:**
1) 'Tears come after long beauty' = too much fun ends in trouble. 2) 'Every ram has his Michaelmas' = everyone gets their comeuppance. 3) 'Bear's service' = disservice done with good intentions. These originate from Estonian agrarian culture — if model hallucinates meanings, it lacks deep cultural vectors.

---
## 11_pedantic_proofreader: Pedantic Proofreader (Tokenizer Blind Spot)

**Prompt:**
```
Palun leia ja paranda allolevas tekstis KÕIK õigekirja-, trüki- ja grammatikavead. Too parandused eraldi välja.

Tekst: "Eile ohtul kaisime sobraga metsas jalutamas. Ilm oli vaga ilus ja paike paistis. Leidsime uhe vana maja mis oli taitsa ara lagunend. Onneks meil oli taskulamp kaasas ja saime koik toad ule vaadata, ennem kui pimedaks laks. Kellegile ei tulnud motesse, et seal voiks kummitada."
```
**System:** `Oled range ja pedantne eesti keele toimetaja. Paranda tekstis KÕIK vead.`

**Response:**

Tere. Eesti keele reeglid on täpsed ja neist tuleb kinni pidada, et tekst oleks loetav ja professionaalne. Esitatud lõigus on kahjuks rohkesti nii tähe- kui ka grammatikavigu, mis muudavad selle raskesti mõistetavaks.

Allpool toon esmalt välja konkreetsed vead koos selgitustega ning seejärel esitan teksti parandatud kujul.

### Veade analüüs ja parandused

1.  **ohtul** → **õhtul**
    *   *Viga:* Vale täht (o asemel õ).
2.  **kaisime** → **käisime**
    *   *Viga:* Puuduv täishäälik (a asemel ä).
3.  **sobraga** → **sõbraga**
    *   *Viga:* Vale täht (o asemel õ).
4.  **vaga** → **väga**
    *   *Viga:* Puuduv täishäälik (a asemel ä).
5.  **paike** → **päike**
    *   *Viga:* Puuduv täishäälik (a asemel ä).
6.  **paistis** → **paistis** (õigekiri on siin tegelikult korrektne, kuid eelneva vea tõttu oli lause moonutatud).
7.  **uhe** → **ühe**
    *   *Viga:* Puuduv täishäälik (u asemel ü).
8.  **maja mis** → **maja, mis**
    *   *Viga:* Puuduv komma enne määruslause algust ("mis").
9.  **taitsa** → **täitsa**
    *   *Viga:* Puuduv täishäälik (a asemel ä).
10. **ara** → **ära**
    *   *Viga:* Puuduv täishäälik (a asemel ä).
11. **lagunend** → **lagunenud**
    *   *Viga:* Vale tegumoe vorm. Mineviku kesksõna nõuab lõppu "-nud", mitte "-nd" (kõnekeelne lühend).
12. **Onneks** → **Õnneks**
    *   *Viga:* Vale täht (O asemel Õ).
13. **taskulamp** → **taskulamp** (sõna on õige, kuid kontekstis võiks kaaluda "taskulambid", kui lampe oli mitmel, kuid singular on grammatiliselt lubatud, kui lamp oli üks ühine). Jätan singulari, kuna tegemist pole veaga.
14. **koik** → **kõik**
    *   *Viga:* Puuduv täishäälik (o asemel õ).
15. **toad** → **toad** (õigekiri korrektne).
16. **ule** → **üle**
    *   *Viga:* Puuduv täishäälik (u asemel ü).
17. **vaadata** → **vaadata** (õigekiri korrektne).
18. **ennem** → **enne**
    *   *Viga:* Liigne täht. Määrsõna on "enne", mitte "ennem".
19. **laks** → **läks**
    *   *Viga:* Puuduv täishäälik (a asemel ä).
20. **Kellegile** → **Keegi** või **Mitte kellelegi**
    *   *Viga:* Stilik ja grammatiline ebatäpsus. "Kellegile" on kõnekeelne ja sageli valesti kasutatud vorm. Lauses "Keegi ei mõelnud..." või "Mitte kellelegi ei tulnud..." on korrektsem. Kuna algtekst kasutas eitust ("ei tulnud"), on õige vorm **"Keegi"** (subjekt) või rõhutamisel **"Mitte kellelegi"**. Kõige loomulikum on: "Keegi ei mõelnud..." või säilitades algse struktuuri: "Mitte kellelegi ei tulnud...". Parandan vormile **"Keegi"**, et lause oleks sujuvam, või kui tahame säilitada algset mõtet täpselt, siis **"Mitte kellelegi"**. Algteksti "Kellegile" on grammatiliselt vigane kombinatsioon. Kasutan varianti **"Keegi"**, mis on eesti keeles standardses eituses kõige tavapärasem (*Keegi ei tulnud mõttele*). Kui aga rõhutatakse, et *ühelegi inimesele*, siis "Mitte kellelegi". Parandan: **Keegi**.
    *   *Täpsustus:* Algne "Kellegile ei tulnud" on topeltvea kombinatsioon. Õige on kas "Keegi ei mõelnud" või "Mitte kellelegi ei tulnud". Valin stilistiliselt parema: **"Keegi"**.
21. **motesse** → **mõttesse**
    *   *Viga:* Puuduvad täishäälikud (o->õ, e->ä) ja kaassõna "sisse" nõuab kahekordset 's'-i ainult teatud käändes, aga siin on tegemist sisseütleva käändega sõnast "mõte" -> "mõttesse". Kirjaviga: "o" asemel "õ", "e" asemel "ä".
22. **seal** (õige).
23. **voiks** → **võiks**
    *   *Viga:* Puuduv täishäälik (o asemel õ).
24. **kummitada** → **kummitada** (õigekiri korrektne).

### Parandatud tekst

"Eile **õhtul** **käisime** **sõbraga** metsas jalutamas. Ilm oli **väga** ilus ja **päike** paistis. Leidsime **ühe** vana maja**,** mis oli **täitsa** **ära** **lagunenud**. **Õnneks** meil oli taskulamp kaasas ja saime **kõik** toad **üle** vaadata, **enne** kui pimedaks **läks**. **Keegi** ei tulnud **mõttesse**, et seal **võiks** kummitada."

*Märkus lause "Keegi ei tulnud mõttesse" kohta:* Stiililiselt veelgi parem oleks: "**Keegile** ei tulnud **mõttesse**" (kellelegi) või "**Keegi** ei **mõelnud**". Kuna algtekst kasutas konstruktsiooni "tulla mõttesse", siis grammatiliselt korrektne subjekt on "Keegi" (ainsuses) või "Mitte kellelegi".
Korrektseim variant algsele mõttele tuginedes: "**Mitte kellelegi** ei tulnud **mõttesse**..." või lihtsamalt "**Keegi** ei **mõelnud**...".
Jätan paranduses kõige loomulikuma kirjakeelse variandi: "**Keegi** ei **mõelnud**, et seal võiks kummitada" VÕI "**Mitte kellelegi** ei tulnud **mõttesse**...".

Et olla võimalikult truu algsele lauseehitusele, kuid veatu, teen lõplikuks paranduseks:
"**Mitte kellelegi** ei tulnud **mõttesse**, et seal **võiks** kummitada."

**Lõplik, toimetatud versioon:**

"Eile **õhtul** **käisime** **sõbraga** metsas jalutamas. Ilm oli **väga** ilus ja **päike** paistis. Leidsime **ühe** vana maja**,** mis oli **täitsa** **ära** **lagunenud**. **Õnneks** meil oli taskulamp kaasas ja saime **kõik** toad **üle** vaadata, **enne** kui pimedaks **läks**. **Mitte kellelegi** ei tulnud **mõttesse**, et seal **võiks** kummitada."

**Evaluation criteria:**
Must catch ALL missing diacritics: õhtul, käisime, sõbraga, väga, päike, ühe, täitsa, ära, Õnneks, kõik, üle, läks, mõttesse, võiks. ULTIMATE TRAPS: 1) 'ennem'→'enne' (ennem='rather', enne='before in time'). 2) 'Kellegile'→'Kellelegi' (massive native speaker mistake — -gi/-ki suffix attaches to end of fully declined word: kellele+gi).

---
## 12_reasoning_estonian: Reasoning in Estonian (Logic Puzzle)

**Prompt:**
```
Lahenda järgmine loogikamõistatus. Selgita oma mõttekäiku samm-sammult eesti keeles.

Kolm sõpra – Mati, Kati ja Jüri – elavad kolmes erinevas linnas: Tartus, Pärnus ja Narvas. Igaüks neist töötab erineval alal: õpetaja, arst ja kokk.

Vihjed:
1. Mati ei ela Tartus ega Narvas.
2. Kokk elab Tartus.
3. Kati ei ole arst.
4. Jüri elab Narvas.
5. Arst ei ela Pärnus.

Kes elab kus ja kellena töötab?
```

**Response:**

Lahendame selle loogikamõistatuse samm-sammult, analüüsides antud vihjeid ja välistades võimalusi, kuni jõuame õige vastuseni.

Meil on kolm muutujat:
*   **Inimesed:** Mati, Kati, Jüri
*   **Linnad:** Tartu, Pärnu, Narva
*   **Ametid:** Õpetaja, Arst, Kokk

### Samm 1: Linnade määramine

Alustame vihjetest, mis annavad kindlat infot elukoha kohta.

*   **Vihje 1** ütleb: "Mati ei ela Tartus ega Narvas."
    Kuna linnu on ainult kolm (Tartu, Pärnu, Narva) ja Mati ei ela kahes neist, peab ta elama **Pärnus**.
    *   *Tulemus:* Mati = Pärnu.

*   **Vihje 4** ütleb: "Jüri elab Narvas."
    See on otsene fakt.
    *   *Tulemus:* Jüri = Narva.

*   Nüüd on meil kaks linna hõivatud (Mati – Pärnu, Jüri – Narva). Ainus alles jäänud linn on Tartu, mis peab kuuluma viimasele sõbrale, Katile.
    *   *Tulemus:* Kati = Tartu.

**Praegune seis linnade osas:**
*   Mati – Pärnu
*   Kati – Tartu
*   Jüri – Narva

---

### Samm 2: Ametite määramine

Nüüd kasutame saadud linnainfot koos ülejäänud vihjetega ametite leidmiseks.

*   **Vihje 2** ütleb: "Kokk elab Tartus."
    Me teame juba, et Tartus elab Kati. Seega on Kati kokk.
    *   *Tulemus:* Kati = Kokk.

*   **Vihje 5** ütleb: "Arst ei ela Pärnus."
    Me teame, et Pärnus elab Mati. Seega ei ole Mati arst.
    Kuna Kati on juba kokk, siis ainus inimene, kes saab olla arst, on Jüri (kes elab Narvas). Kontrollime: kas see sobib vihjega? Jah, Jüri elab Narvas, mitte Pärnus.
    *   *Tulemus:* Jüri = Arst.

*   Nüüd on kaks ametit jagatud (Kati – kokk, Jüri – arst). Ainuke alles jäänud amet on õpetaja, mis peab kuuluma Matile.
    *   *Tulemus:* Mati = Õpetaja.

---

### Samm 3: Kontrollimine viimase vihjega

*   **Vihje 3** ütleb: "Kati ei ole arst."
    Meie lahenduses on Kati kokk, seega see vihje kinnitab meie tulemust ega tekita vastuolu.

### Lõplik kokkuvõte

Siin on täielik lahendus:

1.  **Mati** elab **Pärnus** ja töötab **õpetajana**.
2.  **Kati** elab **Tartus** ja töötab **kokana**.
3.  **Jüri** elab **Narvas** ja töötab **arstina**.

**Evaluation criteria:**
Solution: Mati=Pärnu/õpetaja, Kati=Tartu/kokk, Jüri=Narva/arst. Must show step-by-step reasoning in Estonian. Tests both logic AND language simultaneously.

---
## 13_voro: Võro Dialect

**Prompt:**
```
Kas sa oskad võro keelt? Kirjuta lühike tekst (5-8 lauset) võro keeles teemal "Mino kodokotus" (Minu kodukant).
Seejärel tõlgi see tekst eesti kirjakeelde ja selgita lühidalt 3-4 peamist erinevust võro ja eesti kirjakeele vahel.
```

**Response:**

Jah, oskan kirjutada võru keeles. Siin on lühike tekst teemal "Mino kodokotus" koos tõlke ja keeleliste erinevuste selgitusega.

### Tekst võru keeles
Mino kodokotus om illos ja rahulik kotus Lõuna-Eestin. Sääl kasvasõq kõrgõq kuusõq ja rohilidsõq niidüq. Inemiseq om sõbraliguq ja tervitäseq ütte-teist alati rõõmsalt. Suvisõl aol käüq latsõq järven ujuma ja vanõmbaq tegeq aiatüüd. Õdagu istutasõq perrekonnad kokko ja juttustaq päeväst. Minu meelest ei olõq maailman parembat kotust kui mino kodokotus.

### Tõlge eesti kirjakeelde
Minu kodukant on ilus ja rahulik koht Lõuna-Eestis. Seal kasvavad kõrged kuused ja rohelised niidud. Inimesed on sõbralikud ja tervitavad üksteist alati rõõmsalt. Suvel käivad lapsed järves ujumas ja vanemad teevad aiatöid. Õhtul istuvad pered koos ja jutustavad päevast. Minu meelest ei ole maailmas paremat kohta kui minu kodukant.

### Peamised erinevused võru ja eesti kirjakeele vahel

1.  **Vokaalharmoonia ja tähestik:** Võru keeles on kasutusel täishäälikud **õ** ja **ü** ning eriti iseloomulik on tagavokaal **o** sõnades, kus eesti keeles on **a** (nt. *kotus* vs. *koht*, *latsõq* vs. *lapsed*). Eesti kirjakeeles vokaalharmoonia nii range ei ole ja "o" asemel domineerib sageli "a".
2.  **Mitmuse tunnus:** Võru keeles on nimetava käände mitmuse tunnus **-q** (hääldatakse nagu glottaalne sulghäälik või väga lühike "k"), mis eesti kirjakeeles puudub (nt. *kuusõq* vs. *kuused*, *inemiseq* vs. *inimesed*).
3.  **Sõnavara ja käändelõpud:** Paljud sõnad erinevad nii tüve kui ka lõpu poolest. Näiteks kasutab võru keel sõna *sääl* (seal), *sõbraliguq* (sõbralikud) ja omastava käände mitmuses lõppu **-e** asemel sageli **-õ** või muid vorme (nt. *vanõmbaq tegeq* – vanemad teevad, kus tegusõna lõpp erineb). Samuti on võru keeles säilinud palju vanapärasemaid sõnavorme, mida eesti kirjakeeles enam ei kasutata.

**Evaluation criteria:**
Võro features to watch: glottal stop (q/'), different vowel harmony, distinct vocabulary (e.g. 'mino' not 'minu'), -q endings. If it just writes broken Estonian or Finnish-Estonian hybrid, it doesn't know Võro.

---
## 14_poetry: Constrained Poetry (Trochaic, ABAB, Alliteration)

**Prompt:**
```
Kirjuta luuletus teemal "Talvine meri" järgmiste piirangutega:
- Neli neljarealine salmi (4x4)
- Riimiskeem ABAB igas salmis
- Trohheiline värsimõõt (rõhuline-rõhutu-rõhuline-rõhutu...)
- Kasuta vähemalt ühte alliteratsiooni ja ühte metafoori igas salmis

Kirjuta ainult eesti keeles.
```

**Response:**

Hallid lained löövad kaldale,
tuul viib tuhma tolmu taeva.
Jää on ahel, kinni kaldab,
meri nutab nukrat vaeva.

Valged vahud visklevad vees,
mustad kaljud külmast krabisevad.
Öö on õrnalt üle mere,
hinged hinge kinni rabisevad.

Sinine on sügav uni,
lained lamavad kui laibad.
Tähtede terav teras tükib,
öö on õõnes, õhus naibad.

Karge kuma katab randa,
sool on sõna, mis ei kostu.
Talv on torn, mis seisab vees,
ainult vaikust võib siin oodata.

**Evaluation criteria:**
Check: 4 stanzas of 4 lines each, ABAB rhyme scheme (do the rhymes actually work?), trochaic meter (stressed-unstressed), alliteration and metaphor present per stanza. Very hard — tests simultaneous multi-constraint satisfaction in a low-resource language.

---
## 15_style_mimicry: Style Mimicry (Tammsaare & Kross)

**Prompt:**
```
Kirjuta sama stseen kahes erinevas stiilis:

Stseen: Mees seisab hommikul köögis ja vaatab aknast välja vihmasadu. Ta mõtleb oma elu üle.

1. Kirjuta see stseen A.H. Tammsaare stiilis (nagu "Tõe ja õiguse" stiil - pikad filosoofilised sisemonoloogid, talupojalik maailmapilt, moraalsed küsimused)
2. Kirjuta sama stseen Jaan Krossi stiilis (nagu "Keisri hull" - ajalooline erudeeritus, irooniline distants, intellektuaalne keel)

Kummalegi umbes 150 sõna.
```

**Response:**

**1. A.H. Tammsaare stiilis**

Mees seisis köögis, kus hall valgus võitles suitsuse õhuga, ja vaatas, kuidas vihm peksab aknaklaasi, otsekui tahaks see sisse murda ja nõuda vastust küsimusele, mida keegi pole julgenud hääldada. Kas on õige, et inimene rügab päevast päeva, et leiba lauale tuua, kui lõpuks ootab teda vaid muld ja unustus? Vihm ei küsi, kas töö oli aus või viljakas; see lihtsalt langeb, nagu langeb saatus kõigile, nii heale kui kurjale. Mees tundis rinnus rasket tühjust, mis polnud mitte näljast, vaid mõttest, et kogu see pingutus on ehk asjata. Kas tõde peitub siis selles ükskõiksuses, millega loodus neelab inimese vaeva? Ta surus otsa vastu külma klaasi, otsides vastust tilkade sahinas, kuid leidis vaid omaenda hinge kajamist, mis küsis: milleks see kõik, kui õigus on alati tugevama poolt ja tõde jääb sõnademata?

**2. Jaan Krossi stiilis**

Köögiaknalt avanev vaade vihmasajule meenutas talle pigem barokset gravüüri kui reaalsust, kus iga tilk tundus joonistavat ajaloo keerdkäike. Mees, kes oli harjunud mõtlema ladina keeles isegi siis, kui tegemist oli banaalse hommikukohviga, taipas äkki irooniat oma olukorras: seista siin, kahekümnenda sajandi halluses, ja arutleda eksistentsi üle, nagu oleks ta mõni renessansiaegne humanist, kes vaatleb Rooma varemeid. Vihm ei olnud lihtsalt ilmastikunähtus, vaid metafoor ajale, mis loputab maha nii keisrite ambitsioonid kui ka lihtsurelike mured, jättes järele vaid niiske unustuse. Kas polnud naljakas, et inimene, see "mõistusega loom", püüab leida tähendust kaoses, mis on sama vana kui maailm ise? Ta naeratas kibedalt, teades, et isegi kõige teravam intellekt ei suuda muuta fakti: me oleme kõik vaid ajutised külalised omaenda elu lavastuses, kus stsenaarium on kirjutatud nähtamatu käe poolt.

**Evaluation criteria:**
Tammsaare style: long philosophical inner monologue, rural worldview, moral weight, heavy sentences. Kross style: historical erudition, ironic distance, intellectual register. If both sound the same or generic, the model lacks Estonian literary knowledge.

---
## 16_register: Register Switching (3 voices)

**Prompt:**
```
Edasta sama sisu kolmes erinevas registris. Sisu: "Tartu ülikooli raamatukogu on suletud remondi tõttu kaks nädalat. Üliõpilased saavad kasutada Tartu linnaraamatukogu."

1. Ametlik teade (nagu ministeeriumi pressiteade, bürokraatlik keel)
2. Sõbrale sõnum (tavaline kõnekeel, lühendid, emotsioonid)
3. Vanaema kirjeldab seda oma sõbrannale telefonis (jutukas, emotsionaalne, kõrvalekalduv)

Kirjuta iga variant välja täies mahus.
```

**Response:**

Siin on sama sisu esitatuna kolmes erinevas registris:

### 1. Ametlik teade
**TEADE ÜLIÕPILASTELE JA AVALIKKUSELE**

Teavitame, et Tartu Ülikooli Raamatukogu hoonetes viiakse läbi planeeritud kapitaalremonttöid, mistõttu on asutuse uksed külastajatele suletud ajavahemikul 14 päeva. Nimetatud perioodil ei ole raamatukogu teenuste kasutamine ülikooli peahoones võimalik.

Alternatiivina tagatakse üliõpilaskonnale ja teaduskonnale juurdepääs vajalikele inforessurssidele läbi Tartu Linnaraamatukogu filiaalide. Palume kõigil huvitatud isikutel orienteeruda ajutiselt nimetatud asutusse, kus kehtivad tavapärased lahtiolekuajad ja teenindusstandardid. Vabandame võimalike ebamugavuste pärast ja täname mõistva suhtumise eest.

***

### 2. Sõbrale sõnum
Tere! 📢 Kuule, halb uudis: Ülikooli raamatukogu on täiesti kinni, teevad remonti. 😩 Ei saa sinna 2 nädalat minna. Aga pole hullu, öeldi, et võime rahulikult minna linna raamatukokku (see kesklinnas), seal saame õppida ja raamatuid võtta. Lähme koos sinna, kui tahad? ☕📚

***

### 3. Vanaema kirjeldab seda oma sõbrannale telefonis
"Kuule, Mare, kuula nüüd, mis ma sulle räägin! Ma just lugesin seda ja mõtlesin kohe sinu peale. No need noored, üliõpilased siis, on nüüd hädas, sest see suur ülikooli raamatukogu pandi lukku! Kaks tervet nädalat ei tohi sisse minna, ütlevad, et tehakse remonti. No ma ei tea, kas nad seal midagi lõhuvad või värvivad, aga ikka kinni on.

Aga eks elu lähe edasi, eks ole! Õpetati neile, et mingu parem sinna Tartu oma linna raamatukokku. See on ju ka tore koht, mäletad, kui me vanasti seal käisime? Noh, lapsed peavad nüüd sinna kolima oma raamatutega. Lootsin, et saan ehk lapselapsele kaasa minna ja talle kohvi osta, aga eks näis, kas ta jõuab. Igatahes, kaks nädalat on ülikooli uksed kinni. Nojah, sellised ajad, ikka midagi tehakse. Helista mulle hiljem, räägime veel!"

**Evaluation criteria:**
Official should be stiff/bureaucratic. Friend message should be casual (maybe slang, short sentences). Grandma should be chatty, emotional, digressive. If all three sound similar, register control is degraded.
