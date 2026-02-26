# Estonian Language Smoke Test
**Model:** `/workspace/models/Qwen3.5-397B-A17B`
**Mode:** `no-thinking`
**Sampling:** `temp=0.7, top_p=0.8, top_k=20, min_p=0`
**Date:** 2026-02-22 21:37
**API:** `http://localhost:8000/v1/chat/completions`
**Completed:** 16/16 tests returned responses

---
## 01_orthography: Orthography Stress Test (õ, ü, ö, ä)

**Prompt:**
```
Kirjuta lühike lõik (5-6 lauset) teemal: 'Põõsaste taga ööbinud öökull lendas üle jõe ja nägi õunapuud.' Kasuta võimalikult palju sõnu, mis sisaldavad tähti õ, ü, ö ja ä. Kirjuta ainult eesti keeles.
```

**Response:**

Öösel õõtsusid põõsastes üksi ööbinud öökullid.
Üks õnnetu öökull tõusis üles ja lendas üle jõe.
Ta nägi õues õitsevat õunapuud, mis oli täis õunu.
Õhk oli jahe, kuid õunapuu all oli soe ja mõnus.
Öökull mõtles, et see on tõesti ülihea koht ööbimiseks.
Nüüd istub ta õnnelikult õunapuu otsas ja vaatab ümber.

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
Olev - jõena
Ilmaütlev - jõeta
Kaasaütlev - jõega

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

1. **Kes teist kivi viskab, olgu ise süütu.**
   See tähendab, et enne teiste kritiseerimist või süüdistamist tuleks vaadata üle oma teod ja veenduda, et ise ei ole teinud sama viga.

2. **Ega elevant hiirt karda.**
   Vanasõna väljendab olukorda, kus võimas või tugev pool ei pea kartma nõrka või väikest vastast.

3. **Homseks jäetud töö on pooleldi tehtud.**
   See rõhutab edasilükkamise ohtlikkust: kui jätad asja tegemise hilisemaks, siis tegelikult ei ole see veel valmis ja võib-olla jääbki tegemata.

4. **Sõna ei ole lind, lendu ei lähe.**
   Öeldu jääb püsima; kord öeldud sõnu ei saa tagasi võtta, seega tuleb enne rääkimist hästi järele mõelda.

5. **Kus kitsas, seal läbi.**
   See julgustab leidlikkusele ja visadusele: isegi rasketes tingimustes või takistuste ees leidub alati lahendus või tee edasi.

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

Antud tekstis on kokku **viis** viga, mis puudutavad nii õigekirja (tähtede kasutust) kui ka grammatikat (käändeid ja sõnavara).

Siin on vigade analüüs ja parandused:

1.  **Viga:** *ommikul*
    *   **Selgitus:** Sõnas on vale täht. Eesti keeles kirjutatakse see sõna kahe **h**-ga.
    *   **Õige vorm:** **hommikul**

2.  **Viga:** *pöodi*
    *   **Selgitus:** Siin on tegemist kahe veaga korraga. Esiteks on sõna "pood" sihitavas käändes (kuhu?), mistõttu lõpp on **-sse**, mitte **-i**. Teiseks ei ole sõnas "pood" täishääliku vaheldust (ö -> o), see jääb samaks.
    *   **Õige vorm:** **poodi** (mitte "pöösse" ega "pöodi")

3.  **Viga:** *ounapuid*
    *   **Selgitus:** See on sisuline viga. "Õunapuu" on puu, mida istutatakse aeda. Poest ostetakse toiduks **õunu**. Samuti puudub sõnas täpp (õ).
    *   **Õige vorm:** **õunu** (kontekstist lähtuvalt: "kolm kilogrammi õunu")

4.  **Viga:** *jöudes*
    *   **Selgitus:** Sõnas on vale täht. Tegusõnast "jõudma" tulenev kesksõna kirjutatakse **õ**-ga.
    *   **Õige vorm:** **jõudes**

5.  **Viga:** *vöimalus*
    *   **Selgitus:** Sarnaselt eelmisele, sõnas on vale täht. Õige on kirjutada **õ**-ga.
    *   **Õige vorm:** **võimalus**

---

### Parandatud tekst:

"Eile **hommikul** läksin ma **poodi** ja ostsin kolm kilogrammi **õunu**. **Poodi jõudes** märkasin, et mul polnud rahakotti kaasas. Onneks oli mul telefonis maksmise **võimalus**."

*(Lisamärkus: Lauses "mul polnud rahakoti kaasas" on samuti väike grammatiline ebatäpsus. Õigem oleks öelda "mul polnud **rahakotti** kaasas", kuna tegemist on osastava käändega, mida nõuab eitav lause. Algtekstis oli "rahakoti" omastav kääne.)*

**Evaluation criteria:**
Must catch: ommikul→hommikul, pöodi→poodi, ounapuid→õunapuid, jöudes→jõudes, Onneks→Õnneks, vöimalus→võimalus. Key test: does it catch õ/ö swaps?

---
## 05_natural_generation: Natural Text Generation

**Prompt:**
```
Kirjuta lühijutt (umbes 150 sõna) mehest, kes esimest korda Tallinna vanalinna külastab. Kirjelda tema emotsioone ja mida ta näeb. Ainult eesti keeles.
```

**Response:**

Markus astus esimest korda Viru väravatest sisse ja hing jäi kinni. Tallinna vanalinn avanes tema ees nagu muinasjuturaamatust rebitud lehekülg. Kivisillutatud tänavad, mis olid sajandite jooksul läikivaks kulunud, viisid kitsaste käikude taha, kus iga samm tundus ajas rändamisena. Kõrged tellisseinad ja teravad tornid, eriti uhke Oleviste kirik, sirutusid pilvedesse, varjates endas lugematuid saladusi.

Ta tundis end väikesena selle ajaloolise hiilguse ees, kuid samas ka imeliselt vabana. Õhus hõljus värskete saiakeste ja vana kivi segune lõhn. Turistide rahvahulgad kadusid taustale, kui Markus peatus Raekoja platsil, lastes silmadel püüda iga detaili – värvilisi fassaade, sepisatud laternaid ja kaugeid merevaateid. Süda kloppis põnevusest; ta mõistis äkki, et see pole lihtsalt linn, vaid elav mälestus, mis ootab avastamist. Esimene kohtumine Tallinnaga jättis temas sügava jälje, lubades kindlasti tagasi tulla.

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

Siin on sõnade "siga", "kallas" ja "tuba" käändevormid ning näitelauseid lühikese sisseütleva käändega:

### 1. Sõna: **siga**

*   **Ainsuse osastav:** siga
*   **Ainsuse sisseütlev:** sigasse
*   **Mitmuse omastav:** sigade

**Lause (lühike sisseütlev):**
Kahjuks ei ole võimalik moodustada loomulikku lauset sõnaga "siga" lühikeses sisseütlevas käändes (*sitta*), kuna see vorm on eesti keeles vulgaarne ja tähendab rooja. Seetõttu kasutatakse alati pikka vormi "sigasse".
*Näide pikas vormis:* Poiss viskas õuna **sigasse**.

---

### 2. Sõna: **kallas**

*   **Ainsuse osastav:** kallast
*   **Ainsuse sisseütlev:** kaldasse
*   **Mitmuse omastav:** kallaste

**Lause (lühike sisseütlev):**
Me istusime **kaldal** ja vaatasime päikeseloojangut.
*(Märkus: Sõnal "kallas" on lühike sisseütlev "kaldal", mis tähendab asukohta kaldal, mitte liikumist sinna. Liikumist väljendab ainult pikk vorm "kaldasse". Kui ülesanne nõuab tingimata liikumist väljendavat lühikest vormi, siis sellele sõnale see ei sobi, kuid kohakääne "kaldal" on grammatiliselt lühike vorm.)*

Kui otsitakse just liikumist väljendavat lühikest vormi (mis lõpeb -sse asemel -s), siis seda sõnal "kallas" standardses kirjakeeles liikumise tähenduses ei eksisteeri (on ainult kohakääne "kaldal"). Seega on ainus loomulik lühike vorm kohakääne:
*Parandatud lause kontekstiga:* Lapsed jooksisid mängima **kaldale** (see on rajav, mitte sisseütlev).
*Õige lühike sisseütlev (kohakääne):* Paat seisab **kaldal**.

---

### 3. Sõna: **tuba**

*   **Ainsuse osastav:** tuba
*   **Ainsuse sisseütlev:** tuppa
*   **Mitmuse omastav:** tubade

**Lause (lühike sisseütlev):**
Palun astu **tuppa**!
*(Märkus: Siin on tegemist erandiga. Sõna "tuba" lühike sisseütlev on "tuppa", mis on tegelikult sama pikk kui algne tüvi, kuid grammatiliselt käsitatakse seda sageli erivormina võrreldes reeglipärase "-sse" liitega. Rangelt võttes on "tuppa" ainus võimalik sisseütlev vorm. Kui otsite vormi, mis lõpeb täishäälikuga nagu "majja" või "linna", siis "tuba" puhul see "tup" ei eksisteeri.)*

**Korrektuur ülesande tingimusele:**
Eesti keeles on "lühike sisseütlev" (nt *majja*, *linna*, *kooli*) olemas ainult teatud tüüpi sõnadel. Vaatame uuesti teie palutud sõnu:

1.  **Siga:** Lühikest vormi (*sitta*) ei kasutata kõlvatuse tõttu. Kasutatakse ainult **sigasse**.
2.  **Kallas:** Lühikest liikumist väljendavat vormi ei ole. On ainult kohakääne **kaldal**. Liikumine on **kaldasse**.
3.  **Tuba:** Sisseütlev on ainult **tuppa**. Lühikest varianti (nt *tubba* või *tupp*) ei eksisteeri.

**Järeldus:** Ükski neist kolmest sõnast ei sobi standardsesse "lühikese sisseütleva" (tüüp *majja*) malli loomulikus ja viisakas kõnekeele tähenduses liikumise väljendamiseks, välja arvatud juhul, kui mõelda sõna "kallas" kohakäänet "kaldal" (asukoht, mitte liikumine).

Kui ülesande eesmärk oli harjutada just neid erandeid või näidata, et lühike vorm puudub, siis on vastus järgmine:

*   **Siga:** Lühike vorm puudub (või on kõlvatu). Lause: *Põrsas jooksis **sigasse**.*
*   **Kallas:** Lühike liikumisvorm puudub. Lause (kasutades kohakäänet): *Me puhkasime **kaldal**.*
*   **Tuba:** Lühike vorm puudub (ainus vorm on *tuppa*). Lause: *Lapsed läksid **tuppa**.*

Kui soovisite hoopis sõnu, millega lühike sisseütlev *on* võimalik (nt *maja*, *linn*, *kool*), andke teada, siis koostan need uued näited! Praeguste sõnadega on lühikese sisseütleva moodustamine võimatu või ebakohane.

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

Siin on lühike ja konkreetne selgitus sõnade tähenduste ning lausete paranduste kohta.

### Sõnade tähenduste erinevus

**1. Enamus vs. Enamik**
*   **Enamik** on ainus õige vorm, kui räägitakse suuremast osast mingist hulgast (nt *enamik inimesi*, *enamik ajast*). See on standardses eesti keeles kohustuslik valik.
*   **Enamus** on vananenud või murdeline variant, mida tänapäeva kirjakeeles **ei soovitata** kasutada. Kuigi seda võib kõnekeeles kuulda, peetakse seda stilistiliseks veaks.

**2. Õieti vs. Õigesti**
*   **Õigesti** tähendab "veatult", "korrektselt" või "nagu ette nähtud" (vastand: *valesti*). Kasutatakse faktide, arvutuste ja reeglite kohta.
*   **Õieti** tähendab "tegelikult", "õigupoolest" või "pigem". Seda kasutatakse mõtte täpsustamiseks või parandamiseks (nt *Ma ei tea, kes ta õieti on*).
*   *Viga:* Sageli öeldakse ekslikult "tegin õieti", kui mõeldakse "tegin õigesti" (veatult).

---

### Lausete parandamine ja põhjendus

**1. Algne:** Enamus inimesi eelistab suvel puhata.
*   **Parandus:** **Enamik** inimesi eelistab suvel puhata.
*   **Põhjendus:** Sõna "enamus" on kirjakeeles vale. Suurema osa tähenduses tuleb kasutada sõna **enamik**.

**2. Algne:** Ma ei teinud seda matemaatika ülesannet õieti, sest reegel oli keeruline.
*   **Parandus:** Ma ei teinud seda matemaatika ülesannet **õigesti**, sest reegel oli keeruline.
*   **Põhjendus:** Kuna jutt on ülesande lahendamisest vastavalt reeglitele (veatult vs. valesti), tuleb kasutada sõna **õigesti**. Sõna "õieti" tähendaks siin "tegelikult", mis muudaks lause mõttetuks ("Ma ei teinud ülesannet tegelikult...").

**3. Algne:** Peale söömist läksime kinno.
*   **Parandus:** **Pärast** söömist läksime kinno.
*   **Põhjendus:** Kuigi kõnekeeles on "peale" aja tähenduses (pärast midagi) väga levinud, on kirjakeeles ajaliset järgnevust väljendavaks sõnaks **pärast**. Sõna "peale" peaks kirjakeeles tähendama peamiselt ruumilist asendit (millelegi peale) või suunda.

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

Siin on laused ümber sõnastatud, kasutades lühendatud lauseehitust (kesksõnu ja tegevusnimisõnu), et kõlada loomulikumalt:

1. **Tänaval kõndides** nägin vana tuttavat.
   *(Asendatud ajaline kõrvallause „Kui ma kõndisin..." tegevusnimisõnalise konstruktsiooniga „kõndides".)*

2. **Terve öö haukunud koer** jäi lõpuks hommikul magama.
   *(Asendatud määratluslause „kes oli terve öö haukunud" mineviku kesksõnaga „haukunud".)*

3. See on raamat, mida loetakse praegu igas koolis.
   *Märkus: Selles lauses on aluslause („mida loetakse...") passiivses vormis ja viitab käimasolevale tegevusele erinevate isikute poolt. Eesti keeles ei saa sellist passiivset määratluslauset otse ja loomulikult üheks kesksõnaks lühendada (vormid nagu „loe-tav" või „loetud" muudaksid tähendust või kõlaksid ebaloomulikult). Seetõttu on see lause grammatiliselt juba oma lühimas ja loomulikus vormis. Kui tingimata tuleks struktuuri muuta, oleks ainus võimalus muuta lause aktiivseks (mis muudaks sisu) või kasutada raskemat konstruktsiooni, mis ei oleks stiililiselt parem:*
   -> See on **igas koolis loetav** raamat. (Kõlab veidi sunnitult ja kaotab nüansi „praegu".)
   -> **Parim lahendus:** Jätta lause algupärasesse vormi, kuna eesti keel eelistab sellistel juhtudel täislause kasutamist.

   *Kui ülesanne nõuab tingimata grammatilist muutust igal juhul, siis kõige lähedasem variant on:*
   3. See on **praegu igas koolis loetav** raamat.

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
**Tähendus:** See ütlus hoiatab, et liigne uhkustamine, hooplemine või mõtlematu kulutamine toob lõpuks kaasa kahju, häbi või rahalise kitsikuse. Mida kauem keegi ennast kiidab või mõtlematult tegutseb, seda valusam on langus, kui reaalsus kätte jõuab.

**Eluline olukord:**
Sõber kiidab sotsiaalmeedias pidevalt oma uusi kalleid oste ja väidab, et tal on raha lõputult, kuigi tegelikult elab ta krediitkaardivõlgades. Kui pangad hakkavad laene nõudma ja ta peab oma vara oksjonile panema, võid öelda: *"Näed, ma hoiatasin sind kulutamise eest, aga **pill tuli pika ilu peale** – nüüd oled ilma korterita."*

---

### 2. Igal oinal oma mihklipäev
**Tähendus:** Vanarahva kalendri järgi oli mihklipäev (29. september) aeg, mil loomi tapeti või müüdi. Kõnekäänd tähendab, et igaühele saabub varem või hiljem hetk, mil tuleb vastutada oma tegude eest või kohtuda paratamatu saatusega (sageli ebameeldiva lõpuga). Keegi ei pääse oma tegude eest igavesti.

**Eluline olukord:**
Kontoris on aastaid olnud töötaja, kes on pidevalt reegleid rikkunud, kolleege kiusanud ja ülemust petnud, jäädes alati karistuseta. Äkki kutsub juhatus ta erakorralisele koosolekule ja vallandab ta kohe. Kolleegid võivad sosistada: *"Lõpuks ometi sai temast jagu. **Igal oinal oma mihklipäev**."*

---

### 3. Karuteenus
**Tähendus:** See väljend tähistab teenet, mis on tegelikult kahjulik. See tekib siis, kui keegi soovib head teha või aidata, kuid tema tegevuse tulemuseks on vastupidine – olukord läheb ainult hullemaks. Päritolu on seotud muistendiga, kus karu tahtis kärbsese oma magavalt sõbralt minema lüüa, kuid viskas raske kiviga nii tugevalt, et tappis sõbra.

**Eluline olukord:**
Ema soovib oma täiskasvanud pojale aidata ja teeb tema eest ära kõik majapidamistööd ning maksab tema arved, et pojal oleks kergem. Tulemuseks on see, et poeg ei õpi kunagi iseseisvaks ega tule toime ühegi kohustusega. Sõber võib emale öelda: *"Sa soovid talle head, aga see, et sa tema eest kõike teed, on puhas **karuteenus** – ta ei saa kunagi ise jalule."*

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

Tere. Eesti keele reeglid on ranged ja täpsus on auasi. Esitatud tekstis leidub kahjuks arvukalt vigu, mis ulatuvad lihtsatest trükivigadest (tähepuudumine, valed tähed) kuni grammatiliste ja interpunktsiooniliste eksimusteni.

Allpool toon esmalt välja konkreetsed vead koos selgitustega ning seejärel esitan teksti parandatud kujul.

### Veate analüüs ja parandused

1.  **ohtul** → **õhtul**
    *   *Viga:* Trükiviga (vale täht). "Oht" tähendab riski, "õhtu" on päevaosa.
2.  **kaisime** → **käisime**
    *   *Viga:* Tähepuudumine (pikk vokaal). Sõnatüvi on *käi-*.
3.  **sobraga** → **sõbraga**
    *   *Viga:* Tähepuudumine (pikk vokaal). Kaasütlev käände lõpp on *-ga*, aga tüvi on *sõber*.
4.  **vaga** → **väga**
    *   *Viga:* Tähepuudumine (pikk vokaal). Määrsõna *väga*.
5.  **paike** → **päike**
    *   *Viga:* Tähepuudumine (pikk vokaal). Nimisõna *päike*.
6.  **paistis** → **paistis** (siin oli õige, aga eelnevas sõnas oli viga, mis mõjutas lause loetavust).
    *   *Märkus:* Algtekstis oli "paike paistis", kus esimene sõna oli valesti kirjutatud.
7.  **uhe** → **ühe**
    *   *Viga:* Tähepuudumine (pikk vokaal). Arvsõna *üks* omastav käände vorm.
8.  **maja mis** → **maja, mis**
    *   *Viga:* Interpunktsiooniviga. Kõrvalause ("mis oli...") tuleb pealauses eraldada komaga.
9.  **taitsa** → **täitsa**
    *   *Viga:* Tähepuudumine (pikk vokaal). Kõnekeelne määrsõna (kirjakeeles sobib ka *täielikult*, kuid *täitsa* on aktsepteeritav).
10. **ara** → **ära**
    *   *Viga:* Tähepuudumine (pikk vokaal). Määrsõna *ära*.
11. **lagunend** → **lagunenud**
    *   *Viga:* Grammatikaviga. Mineviku kesksõna lõpp on *-nud*, mitte *-nd*. Õige vorm on *lagunenud*.
12. **Onneks** → **Õnneks**
    *   *Viga:* Tähepuudumine (pikk vokaal). Määrsõna *õnneks*.
13. **taskulamp** → **taskulamp** (õige, aga kontekstis võiks olla "taskulambid", kui inimesi on mitu, kuid ainsus on grammatiliselt lubatav, kui lamp oli üks ühine). Jätan ainsusse, kui vigu pole, aga stiililiselt parem oleks "taskulambid". Parandan siiski ainult vigu: *taskulamp* on õigekirjaliselt korrektne.
14. **koik** → **kõik**
    *   *Viga:* Tähepuudumine (pikk vokaal). Asemesõna *kõik*.
15. **toad** → **toad** (õige).
16. **ule** → **üle**
    *   *Viga:* Tähepuudumine (pikk vokaal). Sihtsõna *üle*.
17. **vaadata** → **vaadata** (õige).
18. **ennem** → **enne**
    *   *Viga:* Õigekirjaviga. Määrsõna on *enne*. Vorm *ennem* on vananenud või murdekeelne, tänapäeva kirjakeeles vale.
19. **laks** → **läks**
    *   *Viga:* Tähepuudumine (pikk vokaal). Tegusõna *minema* minevik.
20. **Kellegile** → **Kellegile** (õige algustäht, aga lause sees väiketähega, kui ei ole lause algus. Siin on lause algus, seega suur täht on õige).
    *   *Kontroll:* "Kellegile" on õige kuju (alaleütlev käände).
21. **motesse** → **mõttesse**
    *   *Viga:* Tähepuudumine (pikk vokaal). Sõna *mõte* seesütlev käände vorm on *mõttesse*.
22. **seal** → **seal** (õige).
23. **voiks** → **võiks**
    *   *Viga:* Tähepuudumine (pikk vokaal). Tingiv kõneviis *võiks*.
24. **kummitada** → **kummitada** (õige).

---

### Parandatud tekst

"Eile **õhtul** **käisime** **sõbraga** metsas jalutamas. Ilm oli **väga** ilus ja **päike** paistis. Leidsime **ühe** vana maja**,** mis oli **täitsa** **ära** **lagunenud**. **Õnneks** meil oli taskulamp kaasas ja saime **kõik** toad **üle** vaadata, **enne** kui pimedaks **läks**. **Kellegile** ei tulnud **mõttesse**, et seal **võiks** kummitada."

*(Märkus: Stiililiselt oleks veel parem kirjutada "taskulambid" ja "täielikult lagunenud", kuid ülaltoodud versioonis on parandatud ainult rangelt võttes vead, säilitades autori algse sõnavaliku seal, kus see grammatiliselt lubatud on.)*

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

Lahendame selle loogikamõistatuse samm-sammult, analüüsides antud vihjeid ja välistades võimalusi, kuni jõuame õige lahenduseni.

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

*   Kuna Mati elab Pärnus ja Jüri elab Narvas, siis ainus allesjäänud inimene on Kati ja ainus allesjäänud linn on Tartu.
    *   *Tulemus:* Kati = Tartu.

**Praegune seis linnade osas:**
*   Mati – Pärnu
*   Kati – Tartu
*   Jüri – Narva

---

### Samm 2: Ametite määramine

Nüüd kasutame saadud linnaandmeid koos ülejäänud vihjetega, et välja selgitada ametid.

*   **Vihje 2** ütleb: "Kokk elab Tartus."
    Me teame juba, et Tartus elab Kati. Seega on Kati kokk.
    *   *Tulemus:* Kati = Kokk.

*   **Vihje 5** ütleb: "Arst ei ela Pärnus."
    Me teame, et Pärnus elab Mati. Seega Mati ei ole arst.
    Kuna Kati on juba kokk, siis ainus inimene, kes võib olla arst, on Jüri (kes elab Narvas). Kontrollime: kas see vastuolu tekib? Ei, vihje ütleb vaid, et arst *ei* ela Pärnus. Jüri elab Narvas, mis sobib.
    *   *Tulemus:* Jüri = Arst.

*   Alles on jäänud üks amet – õpetaja – ja üks inimene – Mati.
    *   *Tulemus:* Mati = Õpetaja.

---

### Samm 3: Kontrollimine

Veendume, et kõik tingimused on täidetud:

1.  *Mati ei ela Tartus ega Narvas.* -> Tõene, ta elab Pärnus.
2.  *Kokk elab Tartus.* -> Tõene, Kati on kokk ja elab Tartus.
3.  *Kati ei ole arst.* -> Tõene, ta on kokk.
4.  *Jüri elab Narvas.* -> Tõene.
5.  *Arst ei ela Pärnus.* -> Tõene, arst (Jüri) elab Narvas.

### Lõplik vastus

Siin on täielik lahendus:

| Nimi | Linn | Amet |
| :--- | :--- | :--- |
| **Mati** | Pärnu | Õpetaja |
| **Kati** | Tartu | Kokk |
| **Jüri** | Narva | Arst |

**Kokkuvõte:**
*   **Mati** elab **Pärnus** ja töötab **õpetajana**.
*   **Kati** elab **Tartus** ja töötab **kokana**.
*   **Jüri** elab **Narvas** ja töötab **arstina**.

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

Jah, oskan võru keelt. Siin on lühike tekst teemal "Mino kodokotus":

**Võru keeles:**
Mino kodokotus om illos ja rahulik kotus Lõuna-Eestin. Sääl kasvavaq kõrõq männiq ja lätseväq selgeq ojakesõq. Inemiseq ommaq sõbraliguq ja tervitäseq üts-teist alati tänavva pääl. Suvisõl aigal kävväq latsõq järven ujuman ja vanõmbaq tegeväq aiatüüd. Õdagu heidä päike maha ja taivas lätsä tähe täüds. Ma armastan umma kodokotust väga, sest sääl om mu süä.

**Tõlge eesti kirjakeelde:**
Minu kodukant on ilus ja rahulik koht Lõuna-Eestis. Seal kasvavad kõrged männid ja voolavad selged ojad. Inimesed on sõbralikud ja tervitavad üksteist alati tänaval. Suvel käivad lapsed järves ujumas ja vanemad teevad aiatöid. Õhtul loojub päike ja taevas läheb tähti täis. Ma armastan oma kodukanti väga, sest seal on mu süda.

**Peamised erinevused võru ja eesti kirjakeele vahel:**

1.  **Vokaalharmoonia ja tähestik:** Võru keeles on kasutusel täishäälikute õ, ü ja eriline täht **q**, mis märgib glottaalset sulghäälikut (nn "katkestust" või kõri sulgemist), mida eesti kirjakeeles ei ole. Näiteks sõnas *kasvavaq* (kasvavad) näitab lõpu -q mitmust.
2.  **Käändelõpud ja grammatika:** Mitmuse osastava ja nimetava lõpud erinevad oluliselt. Eesti keele lõppudele *-d* või *-de* vastab võru keeles sageli *-q* (nt *männiq* – männid, *ojakesõq* – ojakesed). Samuti on verbivormid erinevad, näiteks *lätsä* (läheb) versus eesti *läheb*.
3.  **Sõnavara ja häälikumuutused:** Paljud sõnad on säilitanud vanemaid balti-soome-ugri vorme või on arenenud teist teed pidi. Näiteks võru *kotus* vastab eesti *koht*, *sääl* vastab *seal* ja *umma* vastab *oma*. Samuti on võru keeles levinum astmevahelduse erinev rakendamine (nt *järven* vs võru *järven*, kuid paljudes teistes sõnades on erinevused suuremad).
4.  **Silpide struktuur:** Võru keeles on sõnad sageli fonetiliselt avatumad ja säilitavad rohkem algupäraseid silpilõppe, mis eesti kirjakeeles on taandunud või muutunud (näiteks *tegeväq* vs *teevad*).

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
tuul toob tunde tühistust.
Jää on jahe, jäine valge,
meri magab muretus.

Lumeloor on lahe laubal,
vaikne vesi vait on nüüd.
Pimedus on peegel musta,
öö ei anna õnne süüd.

Karmid kivid krabisevad,
soolane on suudlus külm.
Talv on tigedaist tahtmist,
meri mõtleb mõrudalt.

Hõbedane hääl on hinge,
kajab kaugele ja kaua.
Unustuse udu ümbrit,
meri magab, maailm laua.

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

Mees seisis köögis, kus hall valgus segunes suitsuhaisuga, ja vaatas, kuidas vihm peksab vastu aknaklaasi, justkui tahaks see sisse murda ja nõuda vastust kõigi nende aastate eest, mis on möödunud asjatult. Tilgad jooksid mööda klaasi alla nagu pisarad, mida ta ise pole kunagi valanud, kuigi hing on nutnud verd. „Mis on tõde?" küsis ta endalt, toetudes raskele lauale, mis oli tunnistajaks lõpmatule vaevale. Kas elu mõte seisnebki ainult selles, et künda kivine põld ja oodata saaki, mida kunagi ei tule? Vihm mühises katusel, nagu naeraks loodus tema püüdluste üle. Ta tundis, kuidas õlgadel lasub kogu maailma raskus, see vana koorem, mida ei saa maha panna enne surma. Õigus on võib-olla neil, kes ei mõtle, vaid teevad; aga kas siis inimene erineb lojust? Südametunnistus näris sees nagu uss, küsides, kas kogu see vaev oli õige või ainult suur eksitus, mille eest keegi kunagi tasu ei saa.

**2. Jaan Krossi stiilis**

Köögiaknalt avanev vaade vihmasajule meenutas talle pigem barokset gravüüri kui reaalsust, kus iga tilk tundus olevat ajaloo kirja pandud punkt. Mees, kes oli veetnud noorpõlve ladina keele grammatikat õppides, leidis end nüüd mõtisklemas stoikute saatuse üle: kas vihm peseb patud või ainult tänavad? Tema elu, see pikk kommenteeritud tekst, paistis olevat täis parandusi ja marginaale, mille tähendus jäi häguseks. Irooniliselt mõtles ta, et ehk ongi inimene vaid ekslik tõlge jumaliku algupärandi pealt, kus vihmasadu on lihtalt trükiviga, mida ei saa kustutada. Ta naeratas kibedalt, meenutades, kuidas suurte meeste biograafiates otsitakse alati sügavamat mõtet seal, kus valitses vaid juhus. Vesi voolas rennis nagu aeg ise – möödapääsmatu ja ükskõikne inimeste moraalsete dilemmade suhtes. Kas ta oli oma eluga jõudnud kuhugi või ainult keerelnud samas kohas, nagu kirjatäht vanas käsikirjas, mis ootab unustust?

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

Teavitame, et Tartu Ülikooli Raamatukogu hoonestuskompleksis algavad planeeritud rekonstrueerimis- ja hooldustööd. Seoses nimetatud tegevustega on asutuse uksed külastajatele suletud ajavahemikul 14 päeva.

Kõnealusel perioodil tagatakse üliõpilaskonna juurdepääs vajalikele infoallikatele ja õppetingimustele läbi koostöölepingu Tartu Linnaraamatukoguga. Üliõpilastel palutakse oma õppetööks vajalike teenuste kasutamisel pöörduda nimetatud alternatiivsesse asutusse. Vabandame võimalike ebamugavuste pärast ja täname mõistva suhtumise eest.

***

### 2. Sõbrale sõnum
Hei! 📱 Kuule, halb uudis – Ülikooli raamatukogu on remondis kinni, ei saa sinna 2 nädalat minna 😩. Täitsa jama, kui oleks eksamiaeg... Aga ära muretse, sõbranna ütles, et ülikalased võivad vabalt minna linna raamatukokku asemele. Seal peaks ka wifi ja kohad olemas olema. Lähme sinna koos õppima? ☕📚

***

### 3. Vanaema kirjeldab seda oma sõbrannale telefonis
"Alo, Mare? Kuule, ma just kuulsin seda uudist raadiost või oli see naabri Jüri jutt... no ükskõik, asi on nii, et see suur Ülikooli raamatukogu, kus mu lapselaps alati käis, on nüüd kinni pandud. Panevad seal midagi korda, remondivad vist katust või aknaid, kes seda teab, aga kaks tervet nädalat ei tohi sisse astuda!

Oh, need noored on nüüd hädas, kus nad siis istuvad... Aga kuule, head uudised ka: keegi tark inimene mõtles välja, et üliõpilased võivad minna hoopis sinna teise, linna oma raamatukokku. See on ju see vana maja kesklinnas, mäletad? Nojah, eks nad peavad nüüd sinnamaa kõndima. Mul on nii kahju neist lastest, ilmselt on seal rahvast täis nagu saial silmi. Aga eks nad saavad hakkama, küll leiavad oma nurgakese. Nojah, sellised ajad, ikka midagi ehitatakse või parandatakse..."

**Evaluation criteria:**
Official should be stiff/bureaucratic. Friend message should be casual (maybe slang, short sentences). Grandma should be chatty, emotional, digressive. If all three sound similar, register control is degraded.
