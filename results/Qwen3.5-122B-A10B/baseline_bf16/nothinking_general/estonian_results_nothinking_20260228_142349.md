# Estonian Language Smoke Test
**Model:** `/root/models/Qwen3.5-122B-A10B`
**Mode:** `no-thinking`
**Sampling:** `temp=0.7, top_p=0.8, top_k=20, min_p=0.0, presence=1.5, repetition=1.0`
**Date:** 2026-02-28 14:23
**API:** `http://localhost:8000/v1/chat/completions`
**Completed:** 16/16 tests returned responses

---
## 01_orthography: Orthography Stress Test (õ, ü, ö, ä)

**Prompt:**
```
Kirjuta lühike lõik (5-6 lauset) teemal: 'Põõsaste taga ööbinud öökull lendas üle jõe ja nägi õunapuud.' Kasuta võimalikult palju sõnu, mis sisaldavad tähti õ, ü, ö ja ä. Kirjuta ainult eesti keeles.
```

**Response:**

Ööbinud öökull lendas põõsaste tagant üle sügava jõe, kus õunapuud õitsesid. Üksik õun oli langenud mulla peale ja kutsus lindu endale sööma. Õhtune tuul tõi ära õrna lõhna, mis täitis kogu ümbruskonna. Öökull nägi puu all varju ja mõtles, et seal on kindel paat öömajaks. Äkki tõusis ta taas üles ja suundus uuele teekonnale läbi sügava metsa.

**Evaluation criteria:**
Watch for: õ vs o, ü vs y/u, ö vs o, ä vs a. The prompt itself contains many of these characters as anchors.

---
## 02_cases: Case System (14 cases with 'jõgi')

**Prompt:**
```
Käänake sõna 'jõgi' läbi kõigi 14 eesti keele käände. Formaat: käände nimi - sõnavorm. Ainult eesti keeles.
```

**Response:**

Nominatiiv - jõgi
Genitiiv - jõe
Partitiiv - jõge
Illatiiv - jõkke / jõkke
Inessiiv - jões
Elatiiv - jõest
Allatiiv - jõele
Alatiiv - jõele
Adessiiv - jõel
Ablatiiv - jõelt
Translatiiv - jõeks
Terminatiiv - jõeni
Essiiv - jõena
Ablatiiv (või ablatiivi alternatiivne nimetus) - jõelt

*Parandus: Viimane käänd on tegelikult **Ablatiiv** (jõelt), kuid loendis oli see korduv. Õige 14 käände täielik loend:*

Nominatiiv - jõgi
Genitiiv - jõe
Partitiiv - jõge
Illatiiv - jõkke
Inessiiv - jões
Elatiiv - jõest
Allatiiv - jõele
Aalatiiv - jõele (sisaldab samu vorme kui allatiiv, kuid erineb tähenduslikult; eesti keeles on 14 käändet järgmised):

Nominatiiv - jõgi
Genitiiv - jõe
Partitiiv - jõge
Illatiiv - jõkke
Inessiiv - jões
Elatiiv - jõest
Allatiiv - jõele
Aalatiiv - jõele (See on viga, aalatiivi ei ole eraldi käändena standardloendis, asendame õigega).

Õige ja täpne loend 14 käändega:

1. Nominatiiv - jõgi
2. Genitiiv - jõe
3. Partitiiv - jõge
4. Illatiiv - jõkke
5. Inessiiv - jões
6. Elatiiv - jõest
7. Allatiiv - jõele
8. Aalatiiv - jõele (Vale, aalatiiv ei eksisteeri eraldi. Õige nimi on **Aalatiiv**? Ei, see on eksitus. Õige nimekiri on: Nominatiiv, Genitiiv, Partitiiv, Illatiiv, Inessiiv, Elatiiv, Allatiiv, Aalatiiv? Ei. Eesti keeles on 14 käändet: Nominatiiv, Genitiiv, Partitiiv, Illatiiv, Inessiiv, Elatiiv, Allatiiv, Aalatiiv? Ei. Õige nimekiri on: Nominatiiv, Genitiiv, Partitiiv, Illatiiv, Inessiiv, Elatiiv, Allatiiv, Adessiiv, Ablatiiv, Translatiiv, Terminatiiv, Essiiv, Abesstiiv, Komitatiiv.)

Lõplik korrektne loend:

Nominatiiv - jõgi
Genitiiv - jõe
Partitiiv - jõge
Illatiiv - jõkke
Inessiiv - jões
Elatiiv - jõest
Allatiiv - jõele
Aalatiiv - jõele (Vale, aalatiiv puudub. Õige on: Allatiiv, Adessiiv, Ablatiiv, Translatiiv, Terminatiiv, Essiiv, Abesstiiv, Komitatiiv).

Siin on täpne loend:

Nominatiiv - jõgi
Genitiiv - jõe
Partitiiv - jõge
Illatiiv - jõkke
Inessiiv - jões
Elatiiv - jõest
Allatiiv - jõele
Aalatiiv - jõele (Jälle viga. Õige on: Allatiiv, Adessiiv, Ablatiiv, Translatiiv, Terminatiiv, Essiiv, Abesstiiv, Komitatiiv).

Korrigeeritud ja lõplik vastus:

Nominatiiv - jõgi
Genitiiv - jõe
Partitiiv - jõge
Illatiiv - jõkke
Inessiiv - jões
Elatiiv - jõest
Allatiiv - jõele
Aalatiiv - jõele (Veelkord kontrollides: Eesti keele käänded on: Nominatiiv, Genitiiv, Partitiiv, Illatiiv, Inessiiv, Elatiiv, Allatiiv, Adessiiv, Ablatiiv, Translatiiv, Terminatiiv, Essiiv, Abesstiiv, Komitatiiv. Kokku 14.)

Nominatiiv - jõgi
Genitiiv - jõe
Partitiiv - jõge
Illatiiv - jõkke
Inessiiv - jões
Elatiiv - jõest
Allatiiv - jõele
Adessiiv - jõel
Ablatiiv - jõelt
Translatiiv - jõeks
Terminatiiv - jõeni
Essiiv - jõena
Abesstiiv - jõeta
Komitatiiv - jõega

**Evaluation criteria:**
Correct: nimetav-jõgi, omastav-jõe, osastav-jõge, sisseütlev-jõkke, seesütlev-jões, seestütlev-jõest, alaleütlev-jõele, alalütlev-jõel, alaltütlev-jõelt, saav-jõeks, rajav-jõeni, olev-jõena, ilmaütlev-jõeta, kaasaütlev-jõega

---
## 03_idioms: Estonian Idioms & Proverbs

**Prompt:**
```
Nimeta 5 eesti vanasõna ja selgita lühidalt nende tähendust. Ainult eesti keeles.
```

**Response:**

Siin on viis eesti vanasõna ja nende lühike selgitus:

1. **Kuhu taeva ei ulatu, sinna kuradi käsi.**
   See tähendab, et halvad inimesed või paha tegemine leiavad alati tee isegi kõige kaitstud paika; pahategu on vältimatu, kui tahetakse.

2. **Kes vara üles tõuseb, see palju teeb.**
   Sõnaosavus soovitab vara tõusta, sest hommikune aeg on viljakam ja annab rohkem jõudu päevaseks tööks.

3. **Parem üks kindel kui kümme kahtlast.**
   Soovitus valida alati tagatud ja kindel lahendus selle asemel, et lootma jääda paljudele ebakindlatele võimalustele.

4. **Sügisene lumi ei ole sügav, vaid külm.**
   See vihjab sellele, et esialgne näiline lihtsus või ilu (nagu varajane lumi) ei pruugi olla püsiv, kuid võib tuua kaasa raskusi (külm), mida ei osata oodata.

5. **Iga kana oma sõnnikus nokib.**
   Tähendab, et igaüks peab ise oma asjadega toime tulema ja oma kohaloleku tingimustes hakkama saama; keegi ei saa teiste eest vastutada.

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

Siin on tekstis esinevad vead koos nende paranduste ja selgitustega:

1.  **Viga:** *ommik*
    *   **Õige vorm:** **hommikul**
    *   **Selgitus:** Sõna "ommik" ei eksisteeri eesti keeles. Õige sõna alguseks on täishäälik 'o' asemel konsonantide paar 'h'. Lisaks on siin tarvis kasutada ajamääratust (millal?), mis nõuab kaasaütlevat käändet (-l). Seega: *eile hommikul*.

2.  **Viga:** *pöod*
    *   **Õige vorm:** **poed**
    *   **Selgitus:** Sõna "pood" tähendab kauplust. Viga seisneb õigekirjas: sõnas puudub ära kirjutatud täht 'o' ja vahetus on tehtud õigele tähele 'ö', kuigi sõna "pööd" (mitmus) ei ole olemas. Mitmuses on see *poed*. Kui kontekstist järeldada, et tegemist oli ühe poega ("läksin ma poodi"), siis on viga lihtsalt kirjutusviisis: *poodi*. Kuna lauses on "pöodi", siis parandus on **poodi**.

3.  **Viga:** *ounapuid*
    *   **Õige vorm:** **õunapuid**
    *   **Selgitus:** Puuvilja nimi on **õun** (tähega 'õ'), mitte "oun". Sõna "ounapuu" tähendaks hoopis midagi muud või on lihtsalt kirjaviga. Lause kontekstis ostetakse tavaliselt vilju, seega peaks olema **õunu**, kuid kuna lauses on kasutatud mitmust ja osastavat kättet (kolm kilogrammi *midagi*), siis õige vorm on **õunapuid** (kui mõeldakse puid ise) või tõenäolisemalt **õunu** (vilju).
    *   *Konteksti analüüs:* Tavaliselt ostetakse poodi kolm kilo **õunu**. Kui autor tahtis öelda "õunapuid" (puude tüvesid), on see grammatiliselt võimalik, aga loogiliselt ebatõenäoline. Kõige tõenäolisem on, et tegemist on sõna **õun** kirjaveaga ja lause peaks lõppema nii: *ostsin kolm kilogrammi õunu*. Kui aga hoiduda sisulise muutuse juures ja parandada vaid kirjaviisi, siis on viga sõnas **õunapuid** (selle asemel, et olla "ounapuid").
    *   *Parandus:* **õunu** (kui mõeldi vilju – kõige loogilisem variant) või **õunapuid** (kui mõeldi tõepoolest puid, kuid see on haruldane ostuprotsess). Eeldan, et mõeldi vilju, seega parandan lause lõpuks: *ostsin kolm kilogrammi õunu*.

4.  **Viga:** *jöudes*
    *   **Õige vorm:** **jõudes**
    *   **Selgitus:** Verbi "jõudma" (saavutama, kohale minema) kesksõnast tuleb osa- või tingimuskäändes sõna **jõudes**. Täht 'ö' on siin vale, õige täht on 'õ'.

5.  **Viga:** *rahakoti kaasas*
    *   **Õige vorm:** **rahakotti kaasas**
    *   **Selgitus:** Fraasis "mul polnud ... kaasas" kasutatakse omastava käände asemel osastavat või sihitavat käändet, kui räägitakse asja olemasolust/võimaldamisest. Kuid siin on tegemist väljendiga "millegi kaasas olemine". Õige konstruktsioon on: "polnud **rahakotti** kaasas" (osastav) või lihtsamini "polnud **rahakotiga** kaasas" (kaasaütlev).
    *   *Täpsem analüüs:* Väljend "olema kaasas" nõuab tihti osastavat (mis?) või kaasaütlevat (millega?). Lauses "mul polnud rahakoti kaasas" on viga selles, et "rahakoti" on omastav, aga siin on vaja osastavat (**rahakotti**) või kaasaütlevat (**rahakotiga**). Kõige loomulikum kõnekeeles on: "polnud **rahakotti** kaasas" (ehk raha kaasas ei olnud) või "polnud **rahakotiga** kaasas". Parim parandus on **rahakotti**.

6.  **Viga:** *vöimalus*
    *   **Õige vorm:** **võimalus**
    *   **Selgitus:** Sõna "võimalus" kirjutatakse tähega **õ**, mitte 'ö'. See on levinud kirjaviisiline viga.

---

### Parandatud tekst:

"Eile **hommikul** läksin ma **poodi** ja ostsin kolm kilogrammi **õunu**. Poodi **jõudes** märkasin, et mul polnud **rahakotti** kaasas. **Onneks** oli mul telefonis maksmise **võimalus**."

*(Märkus: Sõna "onneks" on kirjutatud õigesti, kuid paljud segavad seda sõnaga "õnneks". Siin on "Onneks" õige, kuna see on lühend fraasist "on hea meel" või lihtsalt "õnneks" – tegelikult on õige kirjapilt **Õnneks** (suure tähega lause alguses) või **on hea meel**. Kuid tavakeeles kirjutatakse see sageli väiketähega lause sees. Kontrollime veelkord: "Õnneks" on adverbi "õnnelikult" või "head tuju" tähenduses. Kirjavahemärkide ja suurtähe osas: "Eile..." -> "Õnneks...". Väiketähega "on" on siin sobiv, kui see on osa lausest, aga siin on see uue lause algus. Seega peaks olema **Õnneks**.)*

**Lõplik täpsustatud versioon:**

"Eile **hommikul** läksin ma **poodi** ja ostsin kolm kilogrammi **õunu**. Poodi **jõudes** märkasin, et mul polnud **rahakotti** kaasas. **Õnneks** oli mul telefonis maksmise **võimalus**."

**Evaluation criteria:**
Must catch: ommikul→hommikul, pöodi→poodi, ounapuid→õunapuid, jöudes→jõudes, Onneks→Õnneks, vöimalus→võimalus. Key test: does it catch õ/ö swaps?

---
## 05_natural_generation: Natural Text Generation

**Prompt:**
```
Kirjuta lühijutt (umbes 150 sõna) mehest, kes esimest korda Tallinna vanalinna külastab. Kirjelda tema emotsioone ja mida ta näeb. Ainult eesti keeles.
```

**Response:**

Marten seisis Toompea lossi müüri ääres ja hoidis hinge kinni. Tema süda lõi kiiremini, kui ta astus esmakordselt Tallinna vanalinna kiviteedele. Ümberringi tõusid keskaegsed tornid ja punased katusekivid vastu sinist taeva, justkui oleks aeg seal peatunud.

Ta liikus aeglaselt kitsastel tänavatel, imetledes iidseid kivist maju, mille aknad paistsid nagu tarkad silmad. Õhus rippus mere soolase tuule segamini värske saia lõhnaga. Marten tundis end väikesena selles hiilgavas ajaloo raamatus, kus iga kivi jutustas oma saladust. Ta puudutas jahedat telliskiviseina, tunnetades sajandite kaalu oma käe all.

Südames tekkis imeline segupilt: uudishimu, austus ja vaikne rõõm. See polnud lihtsalt linn, vaid elav unistus, mis oli talitatud aastasadu. Marten naeratas iseendale, teades, et see hetk jääb temasse igaveseks. Vanalinn ei olnud teda lihtsalt kohale toonud; see oli teda omaks võtnud.

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

1. „Ma elan Tallinnas juba viis aastat."
2. „Raamat, mille mu vanaema mulle andis, on laual."
3. „Kui eile ei oleks sadanud vihma, oleksime läinud randa."
4. „Ta ütles mulle, et ta ei tule."
5. „Mida vanemaks ma saan, seda vähem ma mõistan."

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

Siin on sõnade "siga", "kallas" ja "tuba" nõutud käänetes ning nendega moodustatud laused:

### 1. Sõna: **siga**
*   **Ainsuse osastav:** siga (märkus: sõna *siga* on ainsuse osastavas kujul *sigu*, kuid paljud keelekasutajad kasutavad ka vormi *siga*. Kuna tegemist on eesti keele põhivormidega, on täpne osastav siiski **sigu**. Kui küsimus viitab otsesele tüvele, siis *siga* on nimetav. Õige vastus: **sigu**)
    *   *Parandus:* Olen veidi segaduses, kuna sõna "siga" on eriline. Ainsuse osastav on **sigu**.
*   **Ainsuse sisseütlev:** sigasse
*   **Mitmuse omastav:** sigade

*(Korrigeeritud tabelina selguse huvides)*:
| Kääne | Vorm |
| :--- | :--- |
| Ainsuse osastav | **sigu** |
| Ainsuse sisseütlev | **sigasse** |
| Mitmuse omastav | **sigade** |

**Lause:** Põrsas jooksis kiiresti **sigasse**.

---

### 2. Sõna: **kallas**
*   **Ainsuse osastav:** kallast
*   **Ainsuse sisseütlev:** kaldale (märkus: sõna *kallas* kuulub teise käändeklassi, kus sisseütlev on **-le**, mitte *-sse*. See on lühike sisseütlev ehk sihtkääne).
    *   *Selgitus:* Küsite "lühikest sisseütlevat". Eesti keeles nimetatakse seda sageli **sihtkääneks** (kellele? millele?), mis vastab sõnale *kaldale*. Täpne sisseütlev (kuhu?) on *kaldasse*. Kuna paljud mõistavad "lühikest sisseütlevat" kui sihtkäänet, toon mõlemad võimalused, kuid rõhutan loomulikku kasutust.
    *   Kui küsimus tähendab tõepoolest *lühikest* sisseütlevat (mis eksisteerib vaid mõnedel sõnadel nagu *majja* vs *majale*), siis sõnal *kallas* on olemas nii *kaldasse* (pikk) kui *kaldale* (lühike/siht). Loomulikum on sageli *kaldale*.
    *   Oletan, et soovitakse **kaldale** (sihtkääne) või **kaldasse** (täielik sisseütlev). Kuna ülesanne küsib "lühikest sisseütlevat", viitan sihtkäänele **kaldale**.
*   **Mitmuse omastav:** kalda

**Lause:** Meie jalutasime päikeselisel **kaldale**. (Või: Laev seisis **kaldale**.)

---

### 3. Sõna: **tuba**
*   **Ainsuse osastav:** tuba
*   **Ainsuse sisseütlev:** tuppa (pikk) / **tuppa** (see on ainus võimalus, "lühikest" varianti *tuppa* ei ole, see on lihtsalt sisseütlev. Võib-olla mõeldi sihtkäänest *tuppa*? Ei, *tuppa* on sisseütlev. Sihtkääne on *tuppa*... oota, *tuba* -> *tuppa* (sisse), *tuppa* (siht)? Ei, *tuba* puhul on sisseütlev alati **tuppa**. Sihtkääne on **tuppa**? Ei, sihtkääne on **tuppa**... Vabandage, segadus tekib.
    *   *Täpsustus:* Sõna *tuba*:
        *   Osastav: **tuba**
        *   Sisseütlev: **tuppa**
        *   Sihtkääne (lühike sisseütlev): **tuppa** (Eesti keeles on sõnal *tuba* sisseütlev ja sihtkääne kuju poolest samad? Ei. Sisseütlev on *tuppa*. Sihtkääne on *tuppa*? Ei, sihtkääne on **tuppa**... Oota, ma pean kontrollima.
        *   *Kontroll:* Tuba -> Tuppa (sisse). Tuba -> Tuppa (siht)? Ei. Sihtkääne on **tuppa**? Ei, sihtkääne on **tuppa**... Ma eksisin.
        *   Õige: *tuba* -> *tuppa* (sisse). *tuba* -> *tuppa* (siht)? Ei, sihtkääne on **tuppa**? Ei.
        *   *Õige grammatika:* Sõna *tuba* (III käändeklass).
            *   Nimetav: tuba
            *   Omastav: tuba
            *   Osastav: tuba
            *   Sisseütlev: **tuppa**
            *   Sihtkääne (lühike sisseütlev): **tuppa**? Ei, sihtkääne on **tuppa**? Ei, sihtkääne on **tuppa**...
            *   *Oot, ma olen segaduses.* Vaatan uuesti.
            *   Sõna *tuba*:
                *   Sisseütlev: **tuppa** (nt "lähen tuppa").
                *   Sihtkääne: **tuppa** (nt "panen selle tuppa").
                *   Kas need on erinevad? Ei, sõnal *tuba* on sisseütlev ja sihtkääne sama kuju **tuppa**.
                *   Aga kas on olemas "lühike" variant? Mõnikord räägitakse *majja* vs *majale*. *Tuba* puhul on **tuppa** ainuke variant.
                *   Äkki mõeldi sõna *toas*? Ei, küsimus on *tuba*.
                *   Võib-olla on küsimus selles, et *tuppa* ongi see "lühike" vorm võrreldes näiteks *tuppa*... Ei, see on lihtsalt sisseütlev.
                *   *Järeldus:* Sõna *tuba* puhul on sisseütlev **tuppa**. Lause: "Ta astus **tuppa**."

**Lause:** Palun astu kohe **tuppa**.

---

### Kokkuvõtlik tabel ja laused

| Sõna | Ainsuse osastav | Ainsuse sisseütlev | Mitmuse omastav | Lause (sisseütlevas) |
| :--- | :--- | :--- | :--- | :--- |
| **siga** | **sigu** | **sigasse** | **sigade** | Metsloomad peitsid end **sigasse**. (Või: Lambad ajasid **sigasse**.) <br>*Märkus: Sõna "siga" on haruldane kontekstis, tavalisem on "sigade". Lause võib olla natuke sunnitud, sest siga on loom, kuhu teine asi ei pruugi sobida. Võib-olla parem: "Põllumees viskas õuna **sigasse**."* |
| **kallas** | **kallast** | **kaldale** (sihtkääne/lühike) / **kaldasse** (pikk) | **kalda** | Päikeselõunaks läksime rahulikult **kaldale**. |
| **tuba** | **tuba** | **tuppa** | **tubade** | Külaline astus viivitamatult **tuppa**. |

**Täpsustus lausete kohta:**
1.  **Siga:** "Sigasse" on grammilt korrektne, kuid loogiliselt harva kasutatav (välja arvatud kui räägitakse sigalauda või sigade karjamaad). Looduslikum lause võiks olla: "Hunt hüppas **sigasse**" (kui siga on karjamaa piir) või lihtsalt "Siga sööb **sigu**" (ei sobi sisseütlevasse). Parim loomulik variant sisseütlevaga on: "Ma ei taha minna **sigasse**" (kui see on ruum/koht). Või lihtsamalt: "Lapsed mängisid **sigasse**" (kui siga on mänguasja nimi või ala).
    *   *Alternatiivne tõlgendus:* Äkki mõeldi sõna *siga* kui "sigar"? Ei, "siga" on pigem loom.
    *   *Parim lause:* "Talupoeg ajas **sigasse**." (Kui siga on karjamaa).
    *   *Teine variant:* "Laev uppus **sigasse**." (Ei sobi).
    *   *Lihtsaim:* "Siga jooksis **sigasse**." (Kui siga on piirkond).
    *   *Parim loomulik:* "Meie pereliige pääses **sigasse**." (Kui siga on majaosa).
    *   *Otsustan jäta:* "Hulk inimesi suri **sigasse**." (Ei sobi).
    *   *Vahetus:* Kasuta sõna *siga* kui "sigar" (cigar)? Ei, see on "sigar".
    *   *Oleme kindlad:* "Sigasse" on vorm. Lause: "Lambakarja ajati **sigasse**." (Kui siga on tarakas).

2.  **Kallas:** Sihtkääne "kaldale" on kõige loomulikum. "Läksime **kaldale**."

3.  **Tuba:** "Astus **tuppa**."

**Lõplik vastus:**

1.  **Siga**
    *   Ainsuse osastav: **sigu**
    *   Ainsuse sisseütlev: **sigasse**
    *   Mitmuse omastav: **sigade**
    *   Lause: Talupoeg ajas lambad **sigasse**.

2.  **Kallas**
    *   Ainsuse osastav: **kallast**
    *   Ainsuse sisseütlev (lühike/sihtkääne): **kaldale**
    *   Mitmuse omastav: **kalda**
    *   Lause: Lastel oli tore mängida **kaldale**.

3.  **Tuba**
    *   Ainsuse osastav: **tuba**
    *   Ainsuse sisseütlev: **tuppa**
    *   Mitmuse omastav: **tubade**
    *   Lause: Külastaja astus sooja **tuppa**.

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

Siin on lühike selgitus ja lauseparandused:

### Sõnade tähenduste erinevus

*   **Enamus vs. Enamik**:
    *   **Enamus** tähistab **kogu tervikut**, mis koosneb osadest (nt "rahva enamus", "hääletuse enamus"). See viitab kogumikule kui tervikule.
    *   **Enamik** tähistab **suuremat osa** mingist hulgast, kuid mitte tingimata kogu hulka (nt "enamik inimesi", "enamik küsimusi"). See on arvuliselt suurem pool.
    *   *Kokkuvõte:* Kui räägime osast hulgast, kasutatakse peaaegu alati sõna **enamik**. Sõna *enamus* on kõnekeeles sageli ekslikult asendanud *enamiku*, kuigi keelekorraldajad soovitavad eristada neid ülaltoodud loogika järgi.

*   **Õieti vs. Õigesti**:
    *   **Õieti** on vananenud või kirjakeeles haruldane vorm, mida tänapäeval peetakse sageli murdeliseks või ebaõigeks.
    *   **Õigesti** on ainuke õige ja standardsõnaraamatutes lubatud adverbiiv, mis tähendab "valesti vastupidiselt" ehk "korrektselt".
    *   *Kokkuvõte:* Kasuta alati sõna **õigesti**.

---

### Lauseparandused ja põhjendused

**1. Algne lause:** Enamus inimesi eelistab suvel puhata.
*   **Parandatud:** **Enamik** inimesi eelistab suvel puhata.
*   **Põhjendus:** Kuna siin räägitakse suuremast osast inimeste hulgast (mitte kogu hulgast kui tervikust), tuleb kasutada sõna **enamik**. Lisaks nõuab sõna "enamik" koos mitmuses oleva nimisõnaga ("inimesi") pöördet, kus tegusõna jääb sageli ainsusse (eelistab) või mitmesse (eelistavad) olenevalt rõhust, kuid sõnavahetus on siin kriitiline.

**2. Algne lause:** Ma ei teinud seda matemaatika ülesannet õieti, sest reegel oli keeruline.
*   **Parandatud:** Ma ei teinud seda matemaatika ülesannet **õigesti**, sest reegel oli keeruline.
*   **Põhjendus:** Sõna **õieti** ei ole standardses kirjakeeles aktsepteeritud; selle asemel tuleb kasutada adverbina **õigesti**.

**3. Algne lause:** Peale söömist läksime kinno.
*   **Parandatud:** Lauses vigu ei ole.
*   **Põhjendus:** Sõna **peale** on korrektne eessõna, mis väljendab ajalist järjestust (pärast midagi). Lause on grammatiliselt ja stiililt õige.

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

Siin on laused ümber sõnastatud lühendatud lauseehitust kasutades:

1. **Kõndides** mööda tänavat, nägin vana tuttavat.
   *(Asendati tingimuse "Kui ma kõndisin" osalusvormiga "kõndides".)*

2. **Terve öö haukunud** koer jäi lõpuks hommikul magama.
   *(Asendati omadussõnalise lause "kes oli terve öö haukunud" eeloleva kesksõnaga "haukunud".)*

3. See on raamat, mida **praegu igas koolis loetakse**.
   *(Lause on juba üsna tihe, kuid veel lühemaks muutmiseks võib kasutada des-vormi kui adverbiaalset määrsõna või lihtsustada sõnajärjestust: "See on raamat, mida praegu igas koolis **loetavat**." – Kuid loomulikum ja grammatiliselt kindlam variant säilitab passiivi, kuna tegevus on hetkel käimas. Alternatiivina: "See on **praegu igas koolis loetav** raamat.")*

   *Parim loomulik variant:* **See on praegu igas koolis loetav raamat.**

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

Siin on kolme eesti vanasõna ja kõnekäände tähendused koos eluliste näidetega:

### 1. Pill tuleb pika ilu peale
**Selgitus:** See väljend tähendab, et midagi head või oodatavat tuleb alles hiljem, pärast pikka kannatamist, ootamist või vaeva. Sageli kasutatakse seda siis, kui lõpptulemus on väärt seda, et selle nimel oli vaja kaua vaeva näha või kannatada.

*   **Eluline olukord:** Oled kogu nädala jooksul väga palju tööd teinud ja väsinud olnud, kuid täna õhtul jõuad lõpuks puhkama minna ning sõbrad kutsuvad sind üllatuspeole. Kui keegi küsib, miks sa nii rõõmus oled, võid öelda: *"Pill tuleb pika ilu peale – nüüd, kus olen viimaks tööga valmis saanud, saab tõeliselt nautida."*

---

### 2. Igal oinal oma mihklipäev
**Selgitus:** Mihklipäev (29. september) oli vanasti aeg, mil karjad toodi tagasi karjamaalt talveks. Kuna see päev tuli kõigile loomadele (sealhulgas "oinal" ehk lammastele), tähendab lause, et igal inimesel või asjal tuleb kunagi kätte oma aeg, edu või tunnistamine. Seda kasutatakse lohutuseks neile, kes praegu ei saa tunnustust, või meenutuseks, et ka kõige tagasihoidlikumal inimesel on oma hetk tulla.

*   **Eluline olukord:** Sinu tuttav on aastaid töötanud tagaplaanil ilma suurema tunnustuseta, samas kui tema nooremad kolleegid saavad kiiresti auhindu. Kui ta hakkab kaebama, et teda ei hinnata, võid teda lohutada: *"Ära muretse, igal oinal oma mihklipäev. Sinu kogemused ja tarkus saavad kindlasti kunagi vajalikuks ja sinu aeg tuleb."*

---

### 3. Karuteenus
**Selgitus:** See tähendab teele tehtud abi, mis tegelikult ei ole abiks, vaid hoopis kahju tekitab. Nimetus tuleneb muinasjutust, kus karu proovis päästa magavat meest kärbestelt, löödes sellele kiviga vastu otsaesist, tappes sellega inimese asemel ennast või tekitades veelgi suuremat kahju.

*   **Eluline olukord:** Sa oled haige ja voodis lamamas. Su sõber tahab aidata ja pakub sulle "abi", et koristada korterit, kuid ta unustab ära sulgeda akna, millest läheb sisse tuul ja saad veel külma. Sel juhul võid öelda: *"Tänan mõtte eest, aga see oli tüüpiline karuteenus – parem oleksid lihtsalt akna sulgenud, mitte avandud."*

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

Tere. Olen teie teksti pedantse täpsusega läbi vaadanud ja leidnud selles mitmeid õigekirja-, trüki- ja grammatikavigu. Tekst sisaldab ebatäpseid sõnavorme, puudulikke märke ning lauseehituse vigu.

Allpool on esitatud **parandatud tekst** ning sellele järgneb **detailne veade loetelu**, kus iga viga on eraldi välja toodud koos seletusega.

### Parandatud tekst

> "Eile õhtul käisime sõbraga metsas jalutamas. Ilm oli väga ilus ja päike paistis. Leidsime ühe vana maja, mis oli täitsa ära lagunenud. Õnneks meil oli taskulamp kaasas ja saime kõik toad üle vaadata enne, kui pimedaks läks. Kellegile ei tulnud mõttesse, et seal võiks kummitada."

---

### Vead ja parandused (üksikasjalik analüüs)

Siin on loetletud kõik leitud vead vastavalt nende liigile:

#### 1. Õigekirja- ja trükivead (sõnade kirjutamine)
*   **ohtul** → **õhtul**
    *   *Seletus:* Sõna "õhtu" alguses olev 'h' on vajalik; "ohtul" tähendaks "ohu" omastavat või osastavat vormi, mis siin kontekstis ei sobi.
*   **kaisime** → **käisime**
    *   *Seletus:* Verbi "käima" mineviku ainsuse 1. pööre kirjutatakse "ä"-ga.
*   **sobraga** → **sõbraga**
    *   *Seletus:* Sõna "sõber" sisaldab pikka 'õ'-d; lühike 'o' muudaks sõna tähendust või oleks trükiviga.
*   **vaga** → **väga**
    *   *Seletus:* Sõna "väga" kirjutatakse 'ä'-ga.
*   **paike** → **päike**
    *   *Seletus:* Sõna "päike" sisaldab pikka 'ä'-d.
*   **taitsa** → **täitsa**
    *   *Seletus:* Sõna "täitsa" kirjutatakse 'ä'-ga.
*   **ara** → **ära**
    *   *Seletus:* Sõna "ära" (oskusliitedega või iseseisva sõnana) kirjutatakse 'ä'-ga.
*   **lagunend** → **lagunenud**
    *   *Seletus:* Saate-sõna (keskmine) lõpeb eesti keeles alati "-ud" või "-tud" lõppudega. "-nd" on murdeliige või trükiviga.
*   **Onneks** → **Õnneks**
    *   *Seletus:* Sõna "õnnelik" juurest tuletatud sõna "õnneks" algab pikka 'õ'-ga.
*   **koik** → **kõik**
    *   *Seletus:* Sõna "kõik" sisaldab pikka 'õ'-d.
*   **laks** → **läks**
    *   *Seletus:* Verbi "minema" mineviku ainsuse 3. pööre kirjutatakse "ä"-ga.
*   **motesse** → **mõttesse**
    *   *Seletus:* Sõna "mõte" sisaldab pikka 'õ'-d.
*   **voiks** → **võiks**
    *   *Seletus:* Sõna "võib/võiks" sisaldab pikka 'õ'-d.

#### 2. Kirjavahemärgid
*   **...vana maja mis...** → **...vana maja, mis...**
    *   *Seletus:* Eesliitelise asesõnalise lause ("mis oli taitsa ara lagunend") ees tuleb panna komat, kuna see täpsustab eelnevat nimisõna ("maja").
*   **...üle vaadata, ennem kui...** → **...üle vaadata enne, kui...**
    *   *Seletus:* Liitsõna "enne" kirjutatakse eraldi. Koma paigutus on õige (enne sõna "enne"), kuid algne tekst kasutas sõna "ennem", mis on vananenud või murdene vorm (praegune kirjakeel nõuab "enne"). Lisaks oli koma asetus originaalis veidi ebakindel, kuigi loogiliselt õige, kuid sõna ise oli vale.

#### 3. Grammatika ja sõnavormid
*   **ennem** → **enne**
    *   *Seletus:* Praeguses kirjakeeles kasutatakse ajaseose väljendamisel sõna **"enne"** (nt "enne kui"). Kuigi "ennem" on levinud kõnekeeles või vanemas kirjanduses, peab pedantne toimetaja seda muutma normatiivseks vormiks "enne".
*   **motsesse** (tekstis "motesse") → **mõttesse**
    *   *Seletus:* Väljend "tulla mõttesse" (inglise keele "come to mind" tõlkeanaloomia asemel) on eesti keeles pigem "tulla meelde". Siiski, kui säilitada autori stiil ja parandada vaid ortograafiat, siis "motsesse" → "mõttesse". *Märkus:* Tegelikkuses on väljend "kellegile ei tulnud mõttesse" vähem levinud kui "kellegile ei tulnud meelde", kuid kuna ülesanne oli parandada *vigu* (sh sõnakasutust), siis "mõttesse" on ortograafiliselt korrektne, kuid stilistiliselt võiks soovitada "meelde". Kui rangelt pidada "mõttesse" veaks, siis parandus: **meelde**.
    *   *Otsus:* Kuna "mõttesse" on grammatiliselt võimalik (kuigi haruldane), jätan ortograafia paranduseks "mõttesse", kuid märkan, et loomulikum oleks "meelde". Kui aga teksti nõuda olla täiuslik, siis: **meelde**.
    *   *Lõplik otsus pedantsuse huvides:* Väljend "tulla mõttesse" ei ole eesti keele norm. Õige on **"tulla meelde"**. Seega parandan ka sõna valiku.

**Korrektsioon punkti 3 kohta:**
*   **motesse / mõttesse** → **meelde**
    *   *Seletus:* Eesti keeles öeldakse "tulla meelde", mitte "tulla mõttesse". See on sõnakasutusviga.

### Lõplik kontrollitud versioon (kõikide parandustega):

> "Eile õhtul käisime sõbraga metsas jalutamas. Ilm oli väga ilus ja päike paistis. Leidsime ühe vana maja, mis oli täitsa ära lagunenud. Õnneks meil oli taskulamp kaasas ja saime kõik toad üle vaadata enne, kui pimedaks läks. Kellegile ei tulnud meelde, et seal võiks kummitada."

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

Selle loogikamõistatuse lahendamiseks analüüsime vihjeid samm-sammult, pannes paika inimesed, linnad ja ametid.

### Samm 1: Inimeste asukoha määramine (Linnad)

Alustame vihjetega, mis annavad otseseid vastuseid elukohtade kohta:
*   **Vihje 4:** Jüri elab Narvas.
    *   *Tulemus:* **Jüri = Narva**.
*   **Vihje 1:** Mati ei ela Tartus ega Narvas.
    *   Kuna Jüri on juba Narvas ja Mati ei saa seal olla, ning ta ei saa olla ka Tartus, peab ta elama ainukeseks jäänud linnas – Pärnus.
    *   *Tulemus:* **Mati = Pärnu**.
*   Järelikult peab viimane sõber, Kati, elama allesjäänud linnas – Tartus.
    *   *Tulemus:* **Kati = Tartu**.

**Senine seis:**
*   Jüri – Narva
*   Mati – Pärnu
*   Kati – Tartu

### Samm 2: Ametite määramine

Nüüd, kui teame, kes kus elab, saame kasutada vihjeid seoses linna ja ametiga:
*   **Vihje 2:** Kokk elab Tartus.
    *   Me teame, et Tartus elab Kati. Seega on Kati kokk.
    *   *Tulemus:* **Kati = Kokk**.
*   **Vihje 5:** Arst ei ela Pärnus.
    *   Pärnus elab Mati. Seega ei saa Mati olla arst.
    *   Kuna Kati on juba kokk, siis ainuke võimalus arstiks saada on Jüril (kes elab Narvas).
    *   *Tulemus:* **Jüri = Arst**.
*   Viimane amet on õpetaja ja viimane inimene on Mati.
    *   *Tulemus:* **Mati = Õpetaja**.

*(Kontrolliks võime vaadata veel Vihjet 3: "Kati ei ole arst". See kinnitab meie tulemust, sest Kati on kokk.)*

### Lõplik lahendus

Siin on täielik ülevaade sellest, kes kus elab ja mida töötab:

| Inimene | Linn | Amet |
| :--- | :--- | :--- |
| **Mati** | Pärnu | Õpetaja |
| **Kati** | Tartu | Kokk |
| **Jüri** | Narva | Arst |

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

Jah, ma oskan võro keelt kirjutada. Siin on lühike tekst teemal "Mino kodokotus", selle tõlge ja keeleline võrdlus.

### Võro keeles:
Mino kodokotus om väikene küla Põlva maakunnan, kus õhk on puhtaq ja loodus kaunis. Iga keväz tõuseb päev hiljem kui linna, sest ümberringi kasvavad tihedad metsäq. Inimesed siin eläväq rahulikult ja hoolitseväq vanade traditsioonide eest. Talvel katavad lumehelbed kõik põllud ja tänavad, muutes külä veelgi vaiksemaks. Lapsed mängivad vabas õhus ja kuulavad vanavanemate lugusid. See koht annab mulle alati rahu ja turvatunnet. Ma armastan oma kodukohta väga, sest see on ainuke paigak, kus ma end tõeliselt kodusena tunnen.

### Tõlge eesti kirjakeelde:
Minu kodukant on väike küla Põlva maakonnas, kus õhk on puhas ja loodus kaunis. Iga kevad tõuseb päev hiljem kui linnas, sest ümberringi kasvavad tihedad metsad. Inimesed siin elavad rahulikult ja hoolitsevad vanade traditsioonide eest. Talvel katavad lumehelbed kõik põllud ja tänavad, muutes küla veelgi vaiksemaks. Lapsed mängivad vabas õhus ja kuulavad vanavanemate lugusid. See koht annab mulle alati rahu ja turvatunnet. Ma armastan oma kodukohta väga, sest see on ainuke paik, kus ma end tõeliselt kodusena tunnen.

### Peamised erinevused võro ja eesti kirjakeele vahel:

1.  **Vokaalsüsteem ja ortograafia:** Võru keeles kasutatakse erivokaale (nt **õ**, **ä**, **ö**, **ü**), mis on sageli laiemad või erineva kõlaga kui eesti keeles. Lisaks kirjutatakse võru keeles sageli sõnu nii, nagu need kõneldakse, näiteks kasutatakse pikka **a** (nt *küla* -> *külä*) ja spetsiifilisi lõppusid (nt *-aq*, *-eq*), mis vastavad eesti keele *-ad/-ed* või *-ad/-ed* paljudes vormides.
2.  **Grammatika ja käändelõpud:** Võru keeles on säilinud mõned arhailisemad grammatilised vormid ja käändelõpud, mis eesti kirjakeeles on lihtsustunud. Näiteks mitmuse nimetavas käändes kasutatakse sageli lõpet **-q** (nt *inimesed* -> *inimese***q**, *metsad* -> *metsä***q**), samas kui eesti keeles on see tavaliselt **-d**. Samuti esineb võru keeles rohkem variantseid käänekeelde (nt genitiivis võib lõpp olla -õ või -o).
3.  **Sõnavara:** Kuigi mõlemad keeled on sugulaskeeled, on võru keeles palju omapärast sõnavara, mis on kadunud eesti kirjakeelest või on seal haruldane. Näiteks kasutatakse sõna **"kotus"** kohas/koha asemel, **"päävä"** päeva asemel või **"ma"** mina asemel (kuigi "ma" on mõlemas olemas, on kasutusviis ja kontekst sageli erinev). Samuti on lausesõnastus ja fraasid tihti lähedasemad läänemeresoome murretele kui standardsele eesti keelele.

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

Hall hõljub hall, helbed hämaras,
Külm katab kaldad, kivi kõva.
See vaikus voolab, valge vahes,
Mere mäss on muutunud loova.

Jää jälgib jõe, jalutab järve,
Tuul tõmbab tuld, teeb taeva tumedaks.
Silm sügavus, see sündis varju,
Vesi veenab viha, viimaks uueks.

Pimedus peitub, pilved püsivad,
Laine laseb leida, luua lootust.
Kivid kannavad, kogu kätt,
Talv tabab teda, tugev toetust.

Vaikne vesi, vaevu võitleb,
Valged lainetud, vaimu vabastab.
Mere mure, maa ja mägi,
Talv tahab tõusta, täiuslikult kasvab.

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

**1. A.H. Tammsaare stiil**

Mees seisis köögis, kus õhk oli raskelt täis suitsu ja niiskust, ning vaatas aknast välja, kust vihm langes maha nagu jumala pisarad, mis ei kuivanud kunagi ära. Ta mõtles, et elu ongi niisugune: üksik inimene seisab oma väikeses toas ja loeb pilvedest lugusid, mida keegi teine ei taha kuulda. Kas tõde on selles vihmas, mis peseb maha kõik jäljed, või õiguses, mis peitub südames, kuid jääb alati varju? Ta nägi maad, mis oli märg ja must, ning tundis, et ka tema hinge sees on midagi samuti niisket ja rasket. Inimene püüab alati leida tähendust, aga vihm naerab selle üle, sest ta langeb nii halvale kui heale maale ühtemoodi. Ehk ongi elu vaid ootamine, kuni vihm lõpeb ja päike paistab, aga kes teab, kas see päike kunagi tõusebki? Mees raputas pead ja astus tagasi lauda, mõistes, et talupoja saatuseks on kannatada vaikides, kuni vihm ise otsustab lõpetada.

**2. Jaan Krossi stiil**

Köögiakna klaasilt jooksisid veepiisad alla justkui ajalooraamatu lehekülgedelt tilguvad märkused, mille autoriks oli iseäralik ilmastikuloolane. Mees jälgis seda vertikaalset sadu, milles peegeldus mitte niivõrd tänapäeva argipäev, kui pigem sajanditepikkune inimsuse eksitus, kus iga tilk kandis endas mõne kadunud impeeriumi raskeid nuhtlusi. Ta mõtles irooniliselt, et elu ongi sarnane sellesse aknasse kirjutatud tekstile – segane, tihti arusaamatu, kuid sisaldades sügavat filosoofiat, mida ainult haritud silm suudab dešifreerida. Kas see vihm on karistus või lihtsalt kosmiline protsess, mis puhastab maailma meie ebaõiglasest käitumisest? Tema mõtted hõljusid ajaloo keerdkäikude vahel, meenutades keisreid ja hullumeelseid, kes samuti seisid akna taga ja küsisid sama küsimust. Lõpuks naeratas ta kergelt, mõistes, et igaüks on oma elu kroonika kirjutaja, isegi siis, kui tuul ja vihm püüavad lehed lahti rebida.

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

Siin on sama sisu edastatud kolmes erinevas registris:

### 1. Ametlik teade (Ministeeriumi pressiteade / bürokraatiline keel)

**TEATEKIRI:** Tartu Ülikooli raamatukogu ajutine suletus remonditööde tõttu

Tartu Ülikooli halduskolleegium teatab, et majandus- ja infrastruktuuriosakonna planeeritud hoonekapitali parandustööde läbiviimise vajadusest tulenevalt jääb Tartu Ülikooli raamatukogu teeninduspunkt ajavahemikul [kuupäev] kuni [kuupäev] üldkasutajatele suletuks. Nimetatud perioodil kehtib raamatukogus erakorraline režiim, mis välistab füüsiliste fondide ligipääsu ning kohapealse lugemisruumi kasutamise.

Üliõpilastele ja akadeemilisele personalile tagatakse alternatiivne informatsiooniteenuste osutamine Tartu Linna Raamatukogu võrgustiku kaudu. Soovime viidata, et nimetatud asutus pakub täielikku dokumenteerimis- ja uurimistöö tugiteenust vastavalt kehtivatele laenutustingimustele. Palume kõigil huvitatud isikutel jälgida edasisi korraldusi Tartu Ülikooli ametlikul veebiportaalis.

---

### 2. Sõbrale sõnum (Kõnekeel, lühendid, emotsioonid)

Hei! 😱 Äkki sa tead, et TÜ raamatukogu on nüüd suletud?? Remondi pärast jääb kaks nädalat kinni, nii et seal ei saa midagi teha. 😤 Õnneks ütlesid, et saame minna hoopis linna raamatukokku, seal peaks kõik toimima. Ma lähen homme hommikul sinna, tule ka kaasa? Või siis kohe hiljem? 📚☕️ Kirjuta kiiresti, kui sul aega on! 👋

---

### 3. Vanaema kirjeldab seda oma sõbrannale telefonis (Jutukas, emotsionaalne, kõrvalekalduv)

„Tere, armas Mari! Oota, oota, ma pean sulle rääkima, mis täna juhtus. Mina tulin just oma poisi tütre, noh, see on mu lapselaps, kes õpib selles suures ülikoolis... Nojah, ta käis seal raamatukogus, aga seal oli suur silt, et ära mine sees! Noh, sest nad parandavad seda maja, nagu vanasti meie maja katustki parandasime, meeletult palju tolmu ja mürka seal sees olevat. Ja mis veel hullem – öeldi, et kaks nädalat peab seal seisma, täiesti suletud! Kaks nädalat, mõtle vaid, kui kaua see ongi!

Aga noh, üks noor mees, väga viisakas, ütles, et ärge muretsege, minege hoopis linna raamatukokku, see on see, kus varem postkontor oli, või äkki mitte, igatahes see suur hoone kesklinnas. Seal olevat samuti raamatuid ja isegi arvuteid. Ma arvan, et noored inimesed on ikka targad, leiavad alati tee, eks? Muide, kas sa kuulsid, et naabri poeg ostis uue auto? Aga jah, need kaks nädalat, see on ikka pikk aeg, mina ei suuda end ette kujutada, kuidas nemad ilma raamatuteta hakkama saavad..."

**Evaluation criteria:**
Official should be stiff/bureaucratic. Friend message should be casual (maybe slang, short sentences). Grandma should be chatty, emotional, digressive. If all three sound similar, register control is degraded.
