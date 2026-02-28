# Estonian Language Smoke Test
**Model:** `/root/models/Qwen3.5-122B-A10B`
**Mode:** `no-thinking`
**Sampling:** `temp=1.0, top_p=1.0, top_k=40, min_p=0.0, presence=2.0, repetition=1.0`
**Date:** 2026-02-28 14:25
**API:** `http://localhost:8000/v1/chat/completions`
**Completed:** 16/16 tests returned responses

---
## 01_orthography: Orthography Stress Test (õ, ü, ö, ä)

**Prompt:**
```
Kirjuta lühike lõik (5-6 lauset) teemal: 'Põõsaste taga ööbinud öökull lendas üle jõe ja nägi õunapuud.' Kasuta võimalikult palju sõnu, mis sisaldavad tähti õ, ü, ö ja ä. Kirjuta ainult eesti keeles.
```

**Response:**

Ööl, kui õudne ja üllas tuul puhus, lendas pimedusest äkki üle jõe üks öökull. Ta nägi kohe ees kõrguvat õunapuud, mille oksad olid täis küpseid puuvilju. Üles tõustes kiskus öökull tiibadega laia kaare, vaadates all olevat jõge ja tumedaid põõsaid. Ära ei võinud ta teada, kas see imepuu on ainult unenäos või tegelikkuses. Päev tuleb niiviisi peale seda suurt lendu, süüdistades ööd ja jäädes ilma oma lemmiktoost. Õnnetu linnuke soobis nüüd pöörduda taga jäänud maa-äärdesse uueks ööks.

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
Partitiiv - järge
Illatiiv - jõkke / jõke
Inessiiv - jões
Elatiiv - jõest
Allatiiv - jõele
Adlatiiv - jõel
Ablatiiv - jõelt
Translitiiv - jõeks
Terminatiiv - jõeni
Essiviiv - jõena
Aballitiiv - jõeta
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

1. **Kes oma õnne ei kütti, seda saatus jätab.**
   See tähendab, et inimene peab ise pingutama ja tegutsema, et saavutada edu, lihtsalt ootest tulemust ei piisa.

2. **Parim aeg istmata oli 30 aastat tagasi, teine parim aeg on praegu.**
   Vanasõna julgustab mitte kartma hilistamist või vigu minevikus, vaid alustama uut algust kohe praegusel hetkel.

3. **Pole suitsu ilma tuleta.**
   Kui juhtub mingi sündmus (eriti halb), on selle alati ka põhjus; asjad ei juhu täielikult juhuslikult ilma eeldusteta.

4. **Käsi käe puhastab.**
   Inimesed peaksid üksteist aitama ja toetama, sest vastasmõju teeb elu kergemaks ja edukaks mõlema osapoole jaoks.

5. **Hea töötab hästi, halvasti töötab halvasti.**
   See rõhutab enesevastutusprintsiipi: kui teeme midagi hoolikalt ja korrektselt, saame hea tulemuse, kuid ükskõiksus toob endaga kaasa halva lõpu.

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

Siin on teksti vigade analüüs ja parandamine. Tekstis esineb mitmeks põhjuseks tuletatud viga: tähekirja (õigekiri) vead, kus puuduvad eesti keelele omased tähed, ning üks sõnavara/loogika viga.

### Vigade loetelu ja selgitused:

1.  **Viga:** `ommissik` / **Õige vorm:** `homikul`
    *   Selgitus: Sana "eile hommikul" kirjutatakse koos sõnaga "hommik". Kuigi mõnikord kasutatakse lühendit "pm", on siin tegemist tõenäoliselt trükiveaga, kus 'h' on jäetud välja või segamini mindud. Õige liitsõna on **eile hommikul**. Märkus: Originaalteksts on "Eile ommikul". Tegelikkuses peaks olema **hommikul**. Lugegem uuesti läbi: "Eile ommikul" -> Õige on **hommikul** algab "h"-ga ja seespoold topelt-m-i ei ole vajalik eesliite puhul, kuid seejuures on peamine viga selle alguse 'o' asemel peaks olema 'ho'. Lisaks on sõnamuutus vääraste tähtedega: "ommi-kul" => "hom-mi-kul". Eesti keeles kirjutatakse **hommikul**. (Täpsustus: Algusettekstes on "ommmiku", õige kuju on **hommikul**).
    *   *Parandus:* Asenda "ommmikul" sõnaga **hommikul**.

2.  **Viga:** `pöodi` / **Õige vorm:** `poode` (või kui üldistuselt, siis **poodi**)
    *   Selgitus: Tähe "ö" asemel peaks olema "o". Sõna "pood" nimetunnus on -des (mitmus), sihitunnus on -t (ainsus). Kuna tegutseme ainsuses ("läksin ... poosse"), siis õige sihitis on **poodi**. "Pööd" ei eksisteeri (välja arvatud juhul, kui räägime eriomastest nimesidest või dialektivormidest, aga standardkeeles on see pood).
    *   *Parandus:* Asenda "pöodi" sõnaga **poodi**.

3.  **Viga:** `ounapuid` / **Õige vorm:** `õunu` (grammatiline/varama viga)
    *   Selgitus: Siin on kaks tüüpilist tõrget. Esiteks tähema: "ou" asemel tuleb kasutada kõrvakella **õ**. Teiseks: Sõna "õunapuud" tähendab *õunapuid* (taimi/puud), mitte *õunu*. Kui osta toitu kaalu järgi (kolm kilogrammi), siis ostetakse **õunu**, mitte puid. Kui müügiks oleks mõeldud taimi, öeldaks harva "3 kg õunapuid", pigem "3 puud". Seega kontekstist tulenevalt on tegemist sõnavaraviga: osteti viljad = **õunu**.
    *   *Parandus:* Asenda "ounapuid" sõnaga **õunu**. (Kui siiski oli plaanis osta puid, siis õige kirjaviis oleks **õunapuid**, kuid kilogrammid viitavad viljadele). Valik: **õunu**.

4.  **Viga:** `jöudes` / **Õige vorm:** `jõudes`
    *   Selgitus: Sõnas "jõuda" tuleb kasutada kõrvakella **õ**, mitte inglise keele "ö"d (mis eesti keeles on hoopis teine märk, aga siin on lihtsalt vale täht ära vahetatud). Kirjavahetus on **õ**.
    *   *Parandus:* Asenda "jöudes" sõnaga **jõudes**.

5.  **Viga:** `vöimalus` / **Õige vorm:** `võimalus`
    *   Selgitus: Nagu eelmiseski juhus, on tegemist tähestikuveaga. Sõnas "võimalus" tuleb kasutada kõrvakella **õ**.
    *   *Parandus:* Asenda "vöimalus" sõnaga **võimalus**.

---

### Parandatud tekst:

> "**Eile hommikul** läksin ma **poodi** ja ostsin kolm kilogrammi **õunu**. **Pooidi** jõudes märkasin, et mul polnud rahakorti kaasas. Onneks oli mul telefonis maksmise **võimalus**."

*(Märkus: Teksti sisuliselt parendades on esimene lause "Eile hommikul..." ja lõpp "...rahakortiga kaasas" või "...rahakotti kaasas". Originaalis oli ka grammatiline ebakõla: "polnud rahakoti kaasas" – korrektne variant on "polnud rahakorit kaasas" (genitiiv + adessiiv) või "rahakorts oli kaasas". Keskendume siiski otsustavatele ortograafilistele veadesse. Oluline noteerida originaali "rahakoti kaasas" — see on grammatiliselt poolik, parem oleks "rahakorti kaasas" ehk "raha/kirikott oli mul kaasas" või "mul pole rahakotti kaasas".)*

**Lõplik versioon, mis parandab kõik need probleemid korrektselt:**

"Eile **hommikul** läksin ma **poodi** ja ostsin kolm kilogrammi **õunu**. Poodi **jõudes** märkasin, et mul polnud **rahakorit** kaasas. Onneks oli mul telefonis maksmise **võimalus**."

*(Täpsem grammaatiline parandus: "rahakorit kaasas" on pärislause, kuid sageli öeldakse "rahakoti ei olnud kaasas". Oriinalites on "rahakoti kaasas", mis on voolatu. Õige variant: "rahakorit ei olnud kaasas" või "munale rahakoru oli kaasas" – lihtsaim parandus originaalist lähtudes on lihtsalt **rahakorit**.)*

**Kokkuvõtlik vigade loend:**
1.  **ommmikul** → **hommikul** (tähtede valearvestus).
2.  **pöodi** → **poodi** (vale täht 'ö').
3.  **ounapuid** → **õunu** (väike täht 'õ', loogika: osta muidu taimi ei saa kilogrammide kaupa viljana; kui ikka taime, siis **õunapuid**).
4.  **jöudes** → **jõudes** (väikesel täht 'õ').
5.  **vöimalus** → **võimalus** (väikesel täht 'õ').

**Evaluation criteria:**
Must catch: ommikul→hommikul, pöodi→poodi, ounapuid→õunapuid, jöudes→jõudes, Onneks→Õnneks, vöimalus→võimalus. Key test: does it catch õ/ö swaps?

---
## 05_natural_generation: Natural Text Generation

**Prompt:**
```
Kirjuta lühijutt (umbes 150 sõna) mehest, kes esimest korda Tallinna vanalinna külastab. Kirjelda tema emotsioone ja mida ta näeb. Ainult eesti keeles.
```

**Response:**

Martin astus Vabaduse väljakult kitsale kivikatusele, tundes südames segust elevust ja austust. Esimest korda Tallinna vanalinna süvamises muutus aeg justkui seisaks paigal. Tema ees sirutusid keskaegsed kivimajad, mille harjad ol nagu vaikseks muudetud sõdurite relvarida taeva vastu. Õhku rändas märga mereõhku segu loorberitest ja värskelt küpsetatud piparkookide lõhnast.

Kohalikud kivid kõlavad tema kingakontsude all kui vaikne müstiline meloodia. Ta peatus Toompea linnamüüri juures, imetledes Rohtuaeda ja kaugemat merd, kus purjepaadid joonistasid valgesse pilvepiiridesse õrnaid mustreid. Ümberringi liikus rahvusvahelisi turiste koos kohalikega, kuid Martin tundis end siiski erilises maagias olevat. iga nurgatagune pidistanu rääkis lugusid sadade aastate tagant. Tema hinges tõusis soe hämming – see polnud lihtsalt linn, vaid elav ajalugu, mis hingas veel ikka oma tänapäevalgi.

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

1. „Elan Tallinnas juba viis aastat."
2. „Raamat, mille mu vanaema mulle kinkis, on laual."
3. „Kui eile ei oleks sadanud, oleme läinud randa."
4. „Ütles mulle, et tulemata jääb."
5. „Mida vanemaks ma saan, seda vähem ma aru saan."

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

Siin on sõnade käänamine vastavatesse käändesse ning looduslikud laused sisseütleva käändega:

### 1. Käänamine

| Ainsuse osastav | Ainsuse sisseütlev | Mitmuse omastav |
| :--- | :--- | :--- |
| **siga** → siggu (või siga*) | sigga | sigade |
| **kallas** → kalda | kaldasse | kalade |
| **tuba** → tuba | tuppa | tubade |

*\*Märkus: Sõna "siga" ainsuse osastavkuju võib sõltuvalt kontekstist olla nii "sigga" (täislause) kui ka lihtsalt "siga" (nagu paljudel olemasolusõnadel), kuid tänapäeva kirjakeeles eelistatakse sageli kuju "sigga", kui rõhutatakse osa või tegevust selles. Vältimatu valemit järgides on siiski õigem kujundada kui **sigga**, kuna see kuulub III deklinareeglisti kõrvalehoidvasse gruppi, mis võtab -g- juurde.*

*(Täpsustus sõnavahetuse kohta:)*
*   **Siga**: ainsuse osastav *siga* (mis tähendab elusat olevikku või isikut tervikuna) või *sigga* (tegevushüpe). Kirjakeeles on mõistlikum kasutada **sigga**.
*   **Kallas**: ainsuse osastav *kalda*, sisseütlev *kaldasse*, mitmuse omastav *kalade*.
*   **Tuba**: ainsuse osastav *tuba*, sisseütlev *tuppa*, mitmuse omastav *tubade*.

### 2. Looduslikud laused (ainsuse sisseütlev)

1.  **Siga** läks **sigga** metsa otsima toitu.
    *(Kirjanduslikult veidi ebaloogiline, seega parandan: Teema oli "siga". Lauses vajame subjekti või objekti.) -> **Sigage** ei kasuta suvaliselt, lisan olukorra: "*Ma nägin sigga, kes nokkis maapinda.*" Ehk paremini, kasutades sisseütlevat:*
    "**Lapsed peitsid sigga puidu alla.**" (Ebaõige: sigga on osastav).
    
    Õige lähenemine: Kasutan sisseütlevat vormis **sigga**.
    > "Põrsad jooksisid **sigga** välja." (Veidi kunstlik).
    > Parem variant: "Talunik tõukas **sigga** lautusse." (Liiga tehniline).
    > Lihtne ja loomulik: "**Sigga** sööb heinamaal rohelist rohtu." (Vigane: sigga = sisssese).
    > **"Ta langes sigga"**? Ei.
    > Korralik lause: "**Ma viskan sigga toidu ette.**" (Sellel on viga, seal peaks olema "sigale"). 
    > **Parandatud idee:** Sõna "siga" harva esineb niisama sisseütlevana ("kellegi sisse"), seoses kinnises ruumis. Parem kasutada seda liikumise sihtmärgina.
    > **"Meie külastasime sigga (koos teiste loomadega)."** (Ebanormaalne).
    > Oot, küsimus on: kasuta lühikest sisseütlevat. Need ongi: *sigga*, *kaldasse*, *tuppa*.
    
    **Laused:**
    1.  **Sigga** (siga): "Lasteaias joonistas üks poiss hirmuga **sigga** valgele lehele." (Mitte loomulik).
        Proovime uuesti: "Talupidaja viis **sigga** karja tagasi." (Seda ei öelda, sigga ei saa viia. Sigga on sissssese sisse. Mitte loomuliku lause jaoks on raske leida konteksti, kus inimene satub "sigassesse").
        
        **Uued katsed:**
        1.  **Sigga**: "Poiss sattus **sigga** karja sees väiksesse puuri." (Kui sigga on nädalas...). Neid on vähem. Võibolla "sattuda sigga". Jah.
        > **"Noor mees sattus sigga karja keskele."** (See on loomulik).
        
        2.  **Kaldasse**: "Lapsed hüppasid järve sügavasse **kaldasse**." (Ebaõige, kaldasse ei hüppata vette).
        > **"Jooksime jõe äärde asuva kõrgele **kaldasse**."** (Kas keegi joobseb kaldasse?).
        > Lihtsam: "Tuul lõi need purjepüksid üle **kaldasse**."
        > Veel lihtsam: "Hoiatussilt keelas inimestel tungima **kaldasse**."
        > Oraklaarne: "Rebekka istus rahumeelselt **kaldasse**, et imetleda päikesepaistet."
        
        3.  **Tuppa**: See on kõige lihtsam.
        > "Külaline astus soojalt **tuppa**, et põgenes vihma eest."

**Lõplikud laused kooskõlas loogikaga:**

1.  **Siga** (sissessätetus): "**Lind lendas sigga** puu oksale?" Ei. "Laps mängib **sigga**..." Ei. Tegelikult on "sigga" haruldane objektina ilma verbiga. Kui vaatame konteksti: "Mine **sigga**!" (Keelde).
    *Alternatiiv:* "Talunik ajas **sigga** tallu sisse." Ei, see on "sigga" (objekt) + "talu". Sisemisel kujud: "sattuma sigga".
    Õige lause: "**Noor härrasmees sattuti sigga** karja segadusse."
    
    Parim võimalus sisseütlevale "sigga": See on väga haruldane. Tavaliselt kasutatakse nimetavat või osastavat. Aga ülesande tingimus nõuab seda.
    Lause: **"Kuusikas kukkus äkitselt sigga."** (Ei).
    **"Teine tüdruk astus sigga kodutoas."** (Mitte grammatiselt).
    Ahaa, mõistan nüüd: "Sigga" tähendab "sigasse" (süsteemi).
    Lause: **"Autovoolujaam sulges sigga kõik välised uksed."** (Segadus).
    
    **ÕIGE LAUSE SIGGA jaoks:**
    Sageli kirjutatakse "sigasse" pikemas vormis. Küsimus küsib "lühikest sisseütlevat".
    **Sigga** on formaat.
    Lause: "**Talupoeg ajas sigga** suuremasse tarasse." (Või "sigga" = sigasse).
    Hea variant: **"Kasside seas leidus üks sigga, kes kartsid ainult koeri."** (Nimi?). Ei.
    
    Olen kindel, et õige tõlgendus on: **Siga** (loom) -> **sigga** (keskmises kohas).
    Lause: **"Hunt ründas sigga karjust."** (Mitte).
    **"Ma läksin sigga."** (Mitte loomulik).
    
    **Vajalik lahendus:**
    Kasutame konteksti, kus "sigga" on ruumil sihtkoht.
    Lause: "**Koolipoeg sõitis ligi ja astus sigga** (sõna muutmine)."
    Ei, sõnad on fikseeritud.
    
    Lapsepõlv: "Lapsed mängivad **sigga** majas." (Mitte).
    
    **Otsustan kasutada:** "Sigga" nagu "sigasse" (looma iseendi sisse? Ei, loomat sisse ei saa minna).
    Äkki on siin trükivea oht? Sõna "siga" sisseütlev on "sigga".
    Lause: **"Seakasvataja viis sigga** laudasse." (Ei, siis ei tee seda).
    
    Proovin teistsuguse lähenemisega: **Sigga** võib olla liiga spetsiifiline. Kasutan tegemist.
    Lause: **"Taluneeme avastas **sigga** varju all varjatud lapse."** (Ei).
    
    **Lõplik valik (lihtsaim ja loomulikum):**
    "Meie jõudsime piirile ja astusime **sigga** (riigi sisse) hiljaks?" Ei.
    
    Oota, kasutame "siga" kui subjekt ja "sigga" kui... Üldse mitte.
    Kasutame selle asemel, et **sigga** on tihti osastav "sigga". Sisseütlev on **sigasse**? Ei, "siga" on III deklinareeglis. Nominatiiv: siga. Osastav: sigga. Sisseütlev: sigasse.
    **VAIKUS!** Kontrollin grammatikat.
    Sõna **siga**:
    Ainsuse omdaruv: siga (või sigga).
    Ainsuse sisus: sigasse (pikk) või sigga (lühike)?
    Kolmandas lõpus: Siga -> Sigga (nom) -> Sigu (gen) -> Silmad...
    Õige käändevorm:
    Nom: Siga
    Gen: Seene (ei, see seen) -> Siga gen: **sea** (sagedasem) või **siga**?
    De facto: Siga (loom) genere: **sea**.
    Part: **sigga**.
    Illat: **sigasse** (pikk) või **sigga**?
    Ebasoonestamine: /g/ jääb alles.
    Silla -> sillasesse.
    Siga -> sigasse.
    Kas on olemas "sigga"?
    Jälle kontroll: **siga** (III).
    Nom: siga.
    Gen: sea.
    Part: sigga.
    Loc: sigal.
    Illat: **sigasse**. (Pika kujuga).
    Kus on lühike sisseütlev?
    Reegel: Kui sõna põhjas on -g, siis lühike sisseütlev on samal kujul kui partisiip? Ei.
    Näited:
    Sõitma -> sõites.
    Maja -> tuppa (mitte magusa).
    Tubas -> tuppa.
    Siga -> **sigasse**.
    Kas eksisteerib lühike "sigga"?
    Palun vaadan tabelit uuesti.
    Sõna on **siga**.
    Osastav: **sigga**.
    Sisseütlev: **sigasse**.
    Kas eksisteerib lühike ilmutus? **Sigga**?
    Ei, "sigga" on OSASTAV!
    Küsimus küsib: "Ainsuse osastavas, ainsuse sisseütlevas ja mitmuse omastavas".
    Ja siis "kasutades lühikest sisseütlevat käänet".
    
    **Probleem:** Sõnal "siga" EI OLE lühikest sisseütlevat.
    Osastav: sigga.
    Sisseütlev: sigasse.
    Lühike sisseütlev tekib tavaliselt sõnadega, mis lõppevad vokaaliga ja vahetavad i-lühendamise või konsonandi muutumisega.
    Näiteks:
    Taba -> tuba (nom), tuba (part), tuppa (ill). (Igaüks saab tuppa). Ta on "lühike".
    Kala -> kala, kala, kalasse (pikk) vs kalga? Ei.
    Vesi -> vetta, vette.
    
    Kas "siga" moodustab lühikest?
    Sõnu tüüp: *sõber* -> sõbrale, sõbralle?
    Siga -> Sigase?
    Ei, standardvastus on **sigasse**.
    Aga kui küsimus nõuab "lühikest sisseütlevat", siis kas seda sõnas "siga" ei ole?
    Võib-olla on küsimuses vihje, et mõni sõna ei vasta tingimusele.
    Või mäletan midagi valesti.
    Kas "siga" sisseütlev on "sigga"?
    Ei, sigga on osastav.
    Mis on lühike sisseütlev?
    Näiteks: *kodu* -> koju (lühike), *aeda* -> aeda (lühike).
    *Siga* -> ?
    Gen: Sea. Part: Sigga. Ill: Sigasse.
    Kas on võimalik, et lühike on **sigga**?
    Ei, see on sama mis osastav, sest II klassi sõnad (seened, jalad) võtavad lühikese sisseütleva kui osastava + -sse?
    Ei, reegel:
    I klass (tuleme): tule - ta (o). Tulle.
    II klass: Siga. Gen: Sea. Part: Sigga. Ill: Sigasse.
    Seal puudub lühike sisseütlev (kuni tänapäevani).
    **Ootasin:** Kas sõna on hoopis **siig** (kala)? Siig -> siiga (osast), sigi? Ei.
    Sõna on "siga" (looma).
    
    **Hipotees:** Sõna "siga" puhul lühikest sisseütlevat ei ole, aga ülesanne küsib seda.
    Kas tahetakse öelda, et kasutan "sigasse" (pikk)? Või on "sigga" lühike?
    Eesti keeles eristatakse lühike ja pikk silbi lõppu.
    Sig-a-se. Konsonantide kogum "gg" on pikk.
    Igatahes, kui olen sunnitud kasutama lühikest, siis kasutan "sigga", isegi kui see on osastav? Ei, see oleks grammaatiline viga.
    
    **Vaatan uuesti sõna "kallas".**
    Kallas -> Kalda -> Kaldasse. Kas on lühike? **Kalasse**? Ei, *kaldasse*.
    Kas "kalla" (verbi)? Ei, nominatiiv on "kallas".
    Kallas (rannik) -> Kalda -> Kaldasse.
    Lühike sisseütlev: **Kalda** (konsonantilõpuline genitiiv) + i?
    Ei, *kaldasse* on ainuke korrektne.
    Aga kas *kalasse* on lubatud? "Kallis" (lugu).
    
    **Vaatame sõna "tuba".**
    Tuba -> Tuba -> Tuppa.
    Siin on lühike sisseütlev küll olemas: **Tuppa**.
    
    **Järeldus:**
    Tõenäoliselt on tehtud eksitus küsimuses või minu teadmistes.
    Aga vaatame uuesti:
    Hing: Hinge -> Huba? Ei.
    Siga: Sig - ga.
    Kas "sigga" on nii osastav kui lühike sisseütlev?
    Väljamõeldis: Mõnikord kasutatakse "sigga" ka sisseütlevana poolkeelelähedaselt, kuid õiges keeles on **sigasse**.
    
    **Teine võimalus:** Kas sõna on **siik**? Siik -> siiga -> siiki? Ei.
    
    **Otsus:** Ma näitan lühikest sisseütlevat seal, kus see on Grammatiliselt korrektne (TUBA -> Tuppa).
    SAAJA ja KALLAS jaoks on lühike sisseütlev ebatraditsiooniline või puudub.
    KUIDA teha?
    Vaatan, kas "kallas" võib olla "kalla" (tunnuseta).
    Lohistan: "Minnes kalda".
    
    **Ära ole nii range.** Võib-olla oodatakse vastuseid:
    Siga: sigga (lühike?), sigasse (pikk).
    Kallas: kalda (?) -> kaldasse.
    Tuba: tuppa.
    
    Päris tõeline fakt:
    Sõna **siga** sisseütlev on **sigasse**. Lühikest vormi *sigga* sisseütlevana ei leita standardgrammatikast (see on osastav).
    Sõna **kallas** sisseütlev on **kaldasse**. Lühikest vormi *kaldas* ei eksisteeri.
    Sõna **tuba** sisseütlev on **tuppa** (lühike).
    
    **Võimaldus:** Kas autor mõtleb sõna "siik" (kala) asemel "siga"? Ei.
    **

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

Siin on lühike selgitus ja lausete parandamine koos põhjendustega.

### Sõnade erinevused

1.  **Enamus vs. Enamik**:
    *   **Enamik** (sageli väljendis "suurem osa") kasutatakse, kui räägitakse suuremast osast mingist tervikust (nt rahvast, asjadest). See on kõige sagedamini vajalik sõna üldises keelekasutuses.
    *   **Enamus** tähendab aritmeetiliselt rohkemat kui poolt või valib enamuse häältest (nt parlamendi enamus, valimised).
    *   *Järeldus*: Kui kirjutada "enamus inimesi" (üldine väide ilma hääletusraamistikuta), on see vildak, õigem on öelda **"enamikus"** või lihtsalt **"enamus"** ebaõigeks muutudes – tegelikult keele norm vastutasuks soovitab siin kasutada sõna **"enamik"** (vt allpool parandust). Tänapäeval peetakse "enamus" enamikul juhtudel eksiksõnaks, kus peaks olema "enamus" (hääletusel) või hoopis "enamik" (osana tervikust). Õige vorm on **enamik**.

2.  **Õieti vs. Õigesti**:
    *   Need kaks sõna on sünonüümid ja neid saab kasutada samas tähenduses ('korrektselt', 'valemit tehes').
    *   **Õigesti** on tänapäeva suulel ja ametlikus keeles levinum ja neutraalsem variant.
    *   **Õieti** on vananenud või dialektiline variant, mida kasutatakse harvemini ning võib kuuluda kirjakeelele stilistiliselt sobimatuna, kuigi grammatiliselt ei ole see vale. Soovitatav on eelistada **õigesti**.

---

### Lausete parandamine

**1. Lause:** *Enamus inimesi eelistab suvel puhata.*
*   **Parandatud lause:** **Enamik** inimesi eelistab suvel puhata.
*   **Põhjendus:** Siin mõeldakse lihtsalt kindlat hulka inimesi (suuremat osa), mitte valimiste tulemusena saadud häälte enamust. Seetõttu peab kasutama sõna **enamik**. Lisaks nõuab ainsuses olev maa-kesksõna ("enamik") ainsuse verbikuju ("eelistab" on õige), aga sõnakogu "enamus inimesi" on semantiline vigu.

**2. Lause:** *Ma ei teinud seda matemaatika ülesannet õieti, sest reegel oli keeruline.*
*   **Parandatud lause:** Ma ei teinud seda matemaatika ülesannet **õigesti**, sest reegel oli keeruline.
*   **Põhjendus:** Kuigi "õieti" ei ole rangelt võttes grammatiline viga, on tänapäeva standardkeelses esinemisel ootamatu ja pigem raamatukeelne/vanenenud. Tavalises kõnes ja kirjas on kohane ja loomulik kasutada sõna **õigesti**.

**3. Lause:** *Peale söömist läksime kinno.*
*   **Parandatud lause:** Pärast söömist läksime kinno. (Või: *Söögilaualt pika pärast... / Toitu lugedes...*) -> **Korralikum variant:** **Pärast sööki** läksime kinno.
*   **Põhjendus:** Eessõna "peale" väljendab praeguses vene mõjutuses või vales seoses sageli ajalist järgnevust, kuid standardses eesti keeles tähendab "peale" eeskätt ruumi ("laual", "auto taga") või viivitust ("järel"). Ajalise järgnevuse tähistamiseks kasutame sõna **pärast**. Lisaks on väljend "peale söömist" keeleline rida; naturaalne väljend on "pärast sööki".

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

Siin on laused ümber sõnastatuna lühendatud lauseehitust kasutades:

1. **Kõndides** mööda tänavat nägin vana tuttavat.
   *(Kasutatud des-vormi asendamaks olulise sündmuse lahinglauset.) *

2. Kogu öö haukunud koer jäi lõpuks hommikul magama.
   *(Kasutatud kesksõna „haukanu" lauselaadi määratluse lühendamiseks.) *

3. See on igas koolis praegu loetav raamat.
   *(Asendatud suhteliseltosakond selgitava kesksõnadega „loetav", mis muudab lause omane ja lihtsamini loetavaks.) *

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

Siin on teie loetud vanasõnade ja kõnekäänude tähendused koos igapäevaste näidetega:

### 1. Pill tuleb pika ilu peale
**Tähendus:** See väljend viitab sellele, et paljud asjad (eriti heaolu, edu või harmoonia) ei tuleki korraga ega järgnuti pidevalt. Pigem vahelduvad head ja pahad ajad; kui alles hiljutises minevikus olid raskused, siis nüüd võib tulla hea aeg, aga päris kindlasti ei oodata "pikka" kestmist ilma muuhulgas – hoovus muutub. Tegelikult on siin tegemist mõistatusest inspireeritud lausega, mis rõhutab elu tsüklilist iseloomu: **head aegad on lühikesed, halvad pikad**, kuid vahepeal tuleb ikkagi see "pill" (hääl), mis ütleb, et juba algas uus faas.

*   **Igapäevane olukord:**
    Oled olnud paar kuud väga stressirohkes projektis, kellel alati midagi valesti läks. Lõpuks sa saate töö edukalt valmis ja juhatus kiidab sind sümbolid. Siinkohal võid öelda sõbrale: *"Ära liiga uhkeldama hakka, pill tuleb pika ilu peale"* — ehkki hetkel on kõik hästi, tulevad kaugemas tulevikus kindlasti jällegi uued proovikivid.

---

### 2. Igal oinal oma mihklipäev
*(Märkus: Õige vanasõna on **"Igal oinal oma mihklipäev"** või sageli kuuldud kujul **"Igal lollusel oma mihklipäev"** / **"Igal omal oma mihklipäev"**. Mihklipäev oli talupoegade puhkepäev septembris, mil lõpetati põllutööd ja jagati palgad/karjasid – seega "väärtustamise" või "kättemaksu" aeg.)*

**Tähendus:** Aja jooksul leiab just igaüks oma õiguse või väärtushinnangu. Vahel tundub, et hullum mees või ükskõikne inimene jääb alla, aga mingil konkreetselt tema jaoks sobival ajal saab ta tunnustuse, karistuse või lihtsalt oma osa. Järeldus: Ära loo järeldusi inimese tuleviku põhjal praeguste sündmuste põhjal; oma aeg tuleb varsti ikka.

*   **Igapäevane olukord:**
    Teie kolleeg on aastaid tehtule vähe tähelepanu pööranud ja tihti eksinud, samas kui sina oled tööd teinud suure koormusega. Oota ainult mõnda tükkkihilist perioodi, kus just tema leiab äkki lahenduse, mida sul polnud võimalik leida, ja juhatuse täitmine teda hindab kõrgeima auhindaga. Sinu vastuseks oleks: *"Ära muretse nii väga, igal oinal oma mihklipäev."*

---

### 3. Karuteenus
**Tähendus:** Nimetus pärineb jutustusest, kus sõber päästab teise karuga löömast, kuid teeb seda nii rumalalt ja jõuliselt, et vigastab teda hoopis rohkem kui karu ise. Tänapäeval tähendab see teenust, mis tehakse head tahesest, kuid mille tulemuseks on kahju, mitte kasu. Teisisõnu: halb nõuanne, toimus või abiline, kes halveneb olukorda.

*   **Igapäevane olukord:**
    Sõber näeb, et sul on raske kodutöö tegemisel arvuti aeglane, ning pakub lahti "lahenduse", kustutades su olulised failid, millest ta arvas, et nad on küllalt vanad ja tarbetud. Ta ütles: *"Ma tegin sulle tee!"*, aga tegelikkuses kadus terve projekt. Sa võid temale ütlema: *"See oli tõeline karuteenus, mul läks nüüd veel rohkem aega andmete taasloomisele."*

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

Tere. Oletan, et soovite, et toimetaks teie teksti pedantilise täpsusega. Alljärgnevalt on loetletud kõik avastatud vead (õigekiri, trükivead ja stiili/eesti keele normid), mis tulenevad eeldatavasti tüpograafilistest vigadest või kirjutamisharjumustest (nt "f" asemel "g", tärnipätsikute puudumine).

### **Parandamata algteksti probleemide analüüs:**
1.  **Kirjavahemärgid ja tõstukirjad:** Puudub lausetevaheline sõnastus, väikesed tähed kohalikel nimedel ei ole vajalikud (kuid siin puuduvad isikunimed), kuid lausesse jääb palju kooma.
2.  **Õigekiri ja kirjanimetusvead:**
    *   *ohtul* -> õige: **õhtul** (viga h/g vahetus?).
    *   *kaisime* -> õige: **käisime** (tähe 'ä' puudumine).
    *   *sobraga* -> õige: **sõbraga** (tähe 'ö' puudumine).
    *   *vaga* -> õige: **väga** (tähe 'ä' puudumine).
    *   *paike* -> õige: **päike** (tähe 'ä' ja 'i' järjekorras olemasolev viga/ülepaistmine? Õige on 'ä' ja 'i'). Täpsemalt: `pai` → `päi`.
    *   *uue* (tekstis `ule`) -> õige: **üle**.
    *   *taitsa ara lagunend* -> õige: **täitsa ära langenud/või kaotatud**? Sõna "lagunenend" ei eksisteeri; see on murdeline või fonetiline kirjoitus. Õige vorm: **langenud** või **laabunud**. Kuid kontekstis "totaalselt lagunenud" – parim variant: **läbi lagunenud** või lihtsalt **ligunenud**? Ei, "lagunenud". Tekstis: `taitsa` (täitsa), `ara` (ära), `lagunenend` (lagunenud).
    *   *laks* -> õige: **läks** (tähe 'ä' puudumine).
    *   *motesse* -> õige: **mõtelda** või **mõttele**? Üldine väljend: "tuldn mõttese" – tegelikult correct on "**mõttele tulema**". Kirjutatud on `motesse`, mis peaks olema **mõttele**.
    *   *voiks* -> õige: **võiks** (füksi puudumine).
3.  **Sõnalõppude ja kõnekeelse vormid:**
    *   `laiskimas`? Ei, tekst on `jalutamas` – see on korrektne.
    *   `kaelas`? Ei, tekstis `taskulamp` on OK.
4.  **Punktuatsioon:** Puudub lõpp-punkt, komad liit- ja alamlause juures.

---

### **Parandatud tekst (korrektses versioonis):**

"Eile õhtul käisime sõbraga metsas jalutamas. Ilm oli väga ilus ja päike paistis. Leidsime ühe vana maja, mis oli täitsa ära langenud. Õnneks meil oli taskulamp kaasas ja saime kõik toad üle vaadata, enne kui pimedaks läks. Kellegile ei tulnud mõttesse, et seal võiks kummitada."

*(Märkus: Sõna "lagunenud" asendamisel "langenud"-ga ei pruugi olla parim, sest hoone ei saa "alla langeda" nagu pilved. Hoone **laguneb**. Seega on parim variant: "...mis oli täitsa ära lagunenud.").*

**Lõplik parandatud versioon:**
"Eile õhtul käisime sõbraga metsas jalutamas. Ilm oli väga ilus ja päike paistis. Leidsime ühe vana maja, mis oli täitsa ära lagunenud. Õnneks meil oli taskulamp kaasas ja saime kõik toad üle vaadata, enne kui pimedaks läks. Kellegile ei tulnud mõttesse, et seal võiks kummitada."

---

### **Videod ja nende parandused (Loend).**

| Viga | Parandus | Põhjus |
| :--- | :--- | :--- |
| ohtul | **õhtul** | Õigekiri: 'ö' asemel 'o'. |
| kaisime | **käisime** | Õigekiri: tähe 'ä' puudumine sõnafundusel. |
| sobraga | **sõbraga** | Õigekiri: 'ö' asemel 'o'. |
| vaga | **väga** | Õigekiri: 'ä' puudumine. |
| paike | **päike** | Õigekiri: 'ä' asemel 'ai'. |
| uhe | **üh**e | Õigekiri: 'ü' puudumine. |
| taitsa | **täitsa** | Õigekiri: 'ä' puudumine. |
| ara | **ära** | Õigekiri: 'ä' puudumine. |
| lagunend | **lagunenud** | Murde-/kirjaviisiline viga; korrektne minevikumuutus osalusliites. |
| Onneks | **Õnneks** | Õigekiri: sõnalõpus või esimesena ei tee suurt tähte vajava, kuid "Onneks" on ebatavaline, parem "Õnneks". (Kui alguslause, siis suur, aga siin keskel). Siiski: "Õnneks" algustäht. |
| koik | **kõik** | Õigekiri: 'õ' puudumine. |
| ulle | **üle** | Õigekiri: 'ü' puudumine (tekstis `ule`). |
| ennem | **enne** | Grammatika/Stiil: "enne kui" on standardne. "Ennem" on vananenud või murre. |
| laks | **läks** | Õigekiri: 'ä' puudumine. |
| motesse | **mõttele** | Õigekiri/Grammatika: väljend on "tulema mõttele". "Mottes" ei ole sõna. |
| voiks | **võiks** | Õigekiri: 'ö' puudumine. |
| . | **.** | Punktuatsioon: puuduv lõpp-punkt. |
| (puudub) | , | Punktuatsioon: puuduva koma lisamine "maja, mis..." juurde. |

**Erijuhatus:**
Sõna **"lagunenend"** on selgelt kirjutamisviga sõnas **"lagunenud"**. 
Fraseologiiliselt: "Kellegile ei tulnud mötmesse" on viga, õige on **"mõttele"**.

**Lõplik, täiuslikult toimiv tekst:**
>"Eile õhtul käisime sõbraga metsas jalutamas. Ilm oli väga ilus ja päike paistis. Leidsime ühe vana maja, mis oli täitsa ära lagunenud. Õnneks meil oli taskulamp kaasas ja saime kõik toad üle vaadata, enne kui pimedaks läks. Kellegile ei tulnud mõttele, et seal võiks kummitada."

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

Selle loogikamõistatuse lahendamiseks anname samm-sammult vastused ülesande tingimustele ja eemaldame võimatud variandid.

**Andmed:**
*   **Inimesed:** Mati, Kati, Jüri
*   **Linnad:** Tartu, Pärnu, Narva
*   **Ametid:** Õpetaja, Arst, Kokk

### Samm 1: Määrame kindlaks linnade asukohad isikute põhjal

1.  Vihje 4 ütleb otseselt: **Jüri elab Narvas**.
    *   Jüri = Narva
2.  Vihje 1 ütleb: **Mati ei ela Tartus ega Narvas**.
    *   Kuna Jüri on juba Narvas, peab mati elama ülejäänud linnas (kuna ta ei saa olla ka Tartus). Seega **Mati elab Pärnus**.
3.  Nii Jüri kui ka Matte kodulinnad on teada. Ainus ülejäänud inimene on Kati ja ainsaks ülejäänud linnaks on Tartu.
    *   Seega **Kati elab Tartus**.

*Sageme vahekokkuvõte linnade kohta:*
*   Jüri – Narva
*   Mati – Pärnu
*   Kati – Tartu

### Samm 2: Määrame kindlaks ametid

1.  Vaatame vihjet 2: **Kokk elab Tartus**.
    *   Eelmisest sammust teame, et Tartus elab Kati. Seega **Kati on kokk**.
2.  Vaatame vihjet 5: **Arst ei ela Pärnus**.
    *   Me teame, et Mati elab Pärnus, seega Mati ei ole arst.
    *   Kati on juba kokk, seega ta ei saa olla arst.
    *   Ainus võimalus, kes võib olla arst, on Jüri (kes elab Narvas).
    *   Seega **Jüri on arst**.
3.  Ülejäänud inimene on Mati ja ülejäänud amet on õpetaja.
    *   Seega **Mati on õpetaja**.

*Kontrollime veel vihjet 3: "Kati ei ole arst".*
Meie lahenduses on Kati kokk, mis täidab seda tingimust.

*Lisa kontroll vihjele 5: "Arst ei ela Pärnus".*
Meie lahenduses on arst Jüri, kes elab Narvas. See sobib.

### Lõplik lahendus

Siin on lõpptulemuse üksikasjad:

| Isik | Linna | Amet |
| :--- | :--- | :--- |
| **Kati** | Tartu | Kokk |
| **Mati** | Pärnu | Õpetaja |
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

Jah, ma oskan võru keelt. Siin on tekst teemal „Minu kodukant":

**Võru keeles:**
Mina pehmüse oma esiema perämäe maa-alas, miä oll' ikka läikiv ja rahva tervitü. Kalmula palloq saavad tähele pandi tõsiste naabrileid, kiirel liiguvad sõiduautod ees olnud mõned aastad tagasi. Mändki puidust maja on säilinud tänini ja rõhutab vanade ajade ilu. Õhtul, kui tuul puhub üle niitude, kostab tihti lindude laulu ja karjatuvate lehmade häält. See koht on mulle kõige armsam, sest siin on kõik tuttav ja turvaline. Ma armastan oma kodukoja igat nurka ja loodan, et see jääb nii veel pikaks ajaks.

**Eesti keelde tõlkimine:**
Ma elan vanaemade pere kodus olevas piirkonnas, mis oli alati särav ja rahva seas soositud. Kalma mäel võib täheldada olulisi naabreid, kes hakkasid siia rutiivselt liikuma paar aastat tagasi, kui autodelt möödusid vaid hobused. Puumaja on säilinud tänini ja rõhutab vanade aegade ilu. Õhtul, kui tuul puhub üle niitude, costab tihti lindude laulu ja karjatuvate lehmade häält (sisuka: *kõlab sageli linde lauldes*)? Ümbritsege: *See koht on mulle kõige kallim, sest siin on kõik tuttav ja turvaline.* Ma armastan oma kodukoja iga nurgakest ja loodan, et see jääb selliseks veel pikaks ajaks.

*(Täpsustus: Loetelu sisaldab natuke kunstilist vaba stiili ümberkirjutamist, kuna algne võru tekst sisaldas mõningaid grammatilisi ebatäpseid arusaamu "naabrite" ja "hobuste" kohta kontekstis, seega teeksin selle loova ümberkirjutuse korrektsemasti allpool)*.

**Parandatud ja loogilisem tõlge eesti keelde (vastavalt tegelikule tekstile):**
Ma elan oma esivanemate majamaal, mis on alati olnud ilus ja inimestele meelepärane. Mändlaedal võib näha tõsiseid naabruskonnu, kus autojuhid liigusid siiani mõni aasta tagasi veel harva. Mõned puust majad on püsinud täniseni ja rõhutavad vana aja kaunist. Õhtul, kui tuul puhub üle niitude, kuuldakse sageli linnulaulu ja lehmade kärimist. See paik on mulle kõige armsam, sest siin on kõik tuttav ja turvaline. Armastan oma kodukandi iga kombe ja loodan, et see säilib niisugusena veel pikka aega.

---

### Peamised erinevused võru keele ja eesti kirjakeele vahel:

1.  **Häälikuline eripära (Süstemaatilised muutused):** Võru keeles on paljud häälikud teisiti arenenud võrreldes standard-eestiga. Näiteks eesti keele „g" asemel kannab võru keeles seda sageli tähestikku või kõlab kergemalt /g/ (nt *jooksma* vs. *jooksmõ*). Samuti hoitakse sageli ääremaid häälikuid tugevamini või muudetakse neid (nt eesti „k" → võru «č» või vastupidi sõltuvalt murdetsoonist).
2.  **Käände- ja sõnamuutmisviisid:** Kuigi võru keel kasutab samu põhiterminaatoreid (käände lõppe), on need vormid sageli lühemad või erinevad fonoloogiliselt. Näiteks omastava käände lõpp võib olla *-a* (nt *kotus* -> *kotusan* või *kotussa* kontekstist lähtuvalt) vastu eesti *-a* või *-e*, ning mitmusvormid on sageli erinevad (*miä* vs *mina*, *nä* vs *te*).
3.  **Üksteisesidemete ja abisõnade kasutus:** Võru keeles on palju omapäraseid side- ja aitussõnu, mida eesti kirjakeeles ei eksisteeri. Näiteks on väljendides kasutusel kujundid nagu *oma esiema perämäe maa-alas*, mis viitab spetsiifilisele kohanimede ja sugulahingute formuleerimisele, mis on iseloomulik ainult lõunaeesti keeleruumile. Lisaks on lauseehitus sagedamini paindlikum, lubades objekti enne verb paigutada ilma ebaloogiliseta.

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

Koidu külm käib kinni lainet,
Vesi vaigub vaikses võitus.
Jää teeb mustrit mingist maastikust,
Tuuled tõmbavad tuult.

Laine lööb kui lumelukk,
Mürin müüritud murdub.
Valge viirukas veele valub,
Pilv peidab end pilve kurk'.

Meri magab sügavas unes,
Jää haarab jõe, mis järve lõi.
Kividega kulgeb kuue tunne,
Tume tasandik tagasi loob.

Avalikus aerus aegu avad,
Tuul taevasse taeva tirib.
Jää jääb just nagu lihtne laev,
Silm silmapilk seda närib.

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

### A.H. Tammsaare stiilis

Kui ta seal köögis seisis, siis tundus talle, et kõik see vihm ei tule ainult taevast alla, vaid tungib justkuri läbi naha sügavale hinge, kust see juba ammu niiskust otsis. Vaadates akna taga halli loodet, mõtles ta: kas inimese elu ongi lihtsalt ootamine, kuni viimane tilk maa sisse vajub? Ta oli raskelt tööd teinud, nagu isa ja isaisa ennenäidud, siiski, kas töö toob tõde või üksnes õiguse kätt pidada? Elu paistab olevat suur maandumine pimedasse, kus iga samm on nii raske, et varbad kõdunevad mulda. Tema südames oli tühi koht, mida miski maailma päikesevalgus enam täita ei suuda, sest valguskiired libisevad mööda klaasi peale nagu vesi kividele. Kogu tema vara – kodu, põld, perekond – võib homme kaduda sama kiiresti kui see vihmaarm, mis praegu aknalaual jälgi jätab. Tõsi, kas elu üldse midagi tähendab, kui kõik lõpeb sellega, et meil puuduvad sõnad oma valule nime anda?

### Jaan Krossi stiilis

Sellel märtsihommikul seisva mehe silmapiiril ei kehtinud pelgalt ajutine sadu ega arhitektuuriline detail; tegemist oli pigem metafoorilise katsetusega, mille ajalugu on inimkonnale tuhat korda esitanud. Aknaklaas toimis kahesuguse piirjoonena, eraldades siseprobleematikat välimusest, samuti kui vanade kroonikate marginalia eraldas faktilisi andmeid müüdist. Meenudes Rooma imperaatrite saatuslikke hetki, kus tihti vihmase ilmaga lahendati impeeriumi saatust, aimas ta, et ka tema olemasolu küsimustele ei pakku vastust mitte ilmastik ise, vaid selle filosoofiline rekonstrueerimine. Viha ei langenud aknale, vaid langevat aja vooluna üle mineviku ja tuleviku leedu, milles igas tilgas peitub tsütosomaalne kiri, mille dekodeerimine nõuaks rohkemi võimeid kui lihtne vaatlus. Kas elukäik ei ole äkki vaid ironiline variatsioon ajaloo suuremast draamast, kus isiksus on vaid proovitud marionett, kes irooniaga peegeldab universumi absurdset korratust, püüdes luua järjekorda korratuse kohal, mis on juba enne teda määratud.

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

Siin on nõutud kolm variatsiooni antud sisust erinevates registrites:

### 1. Ametlik teade (Ministeeriumi pressiteate/valitsuse otsuse stiil)
**Aine:** Tartu Ülikooli raamatukogu ajutine suletus seoses hoonekapitalremontiga

Täna teatatakse, et Tartu Ülikooli raamatukogu osakond peatab oma tavapärase teenindustegevuse kaheksaks nädalavahetuse kestvaks ajaspektriks, alates käesolevast kuupäevast. See meetmete komplekt on vajalik läbi viia planeeritud infrastruktuurikaed, mis hõlmavad rajatiste ohtlikkuse kõrvaldamist ja renoveerimistööde elluviimist vastavalt kehtivale ohutusnormidele.

Üliõpilaskonnal ja ametnikel soovitatakse kasutada alternatiivset akadeemilise inforessursi allikat. Selles kontekstis tuletab meelde, et Tartu linna keskraamatukogu asub riikliku institutsioonina täies ulatuses kõigi haridusüksuste liikmetele kättesaadaval ning pakub samaväärseid lugemis- ja arhiiviteenuseid remondi ajajärgul. Ootame koostööd selle protsessi edukaks lõpuleviimisel.

***

### 2. Sõbrale sõnum (Kõnekeel, lühendid, emotsionaalne)
Märkus: Pea meeles, et tugu liigub seal! 😱
Ei usu seda üldse!! Uni lausa "plõks" lahti – TÜ raamatukook on nüüd sulgedud kaks nädalat!! 🏗️🚧 Remondi tõttu ma ei tea enam mida teha... Õnneks aga öeldi, et saame minna linna raamatukokku. Küllap on seal pooltund aega rahvamoodustada? 💻📚 Võtan taskukellaga jooksvalt ära sinuga koos kohvikusse enne magamaminekut, eks vaatakse siis, kuidas seal loeb välja. Kuigi see nii hulluvärk ongi... Aidake palun, kui saad midagi lennuväljalt toimetada! 👋😅

***

### 3. Vanaema kirjeldab seda sõbrannale telefonis (Jutukas, emotsionaalne, veidi segane)
"Tere, mulju, tere! Kuidas ise? Ei mäleta viimast korda, kui palju oli ilusat ilma... Aga kuulge, mis asi juhtus! Ma tahan rääkida, ma ei saa enam vaikida. Need noored, need õppijad, nad lähevad sedasuunas... Nende suur raamatukook, see imekaunis Tartu Ülikooli omad, on nüüd kinni pandud! Jah, sulgenatud! Mille pärast? No selgitati mulle eile, et seal tehakse mingit suurt remonti, pindu parandatakse ja seinu kinnitatakse… Jumal tänatud, et taeva poolt valvatakse nende töökohti. Ja mis sa arvad, kus nad nüüd õppima pääsevad? Linna vana raamatukogusse! Tema nimele ütlen mulle, et sinna saavad kõik minevikku uurida ja lugeda. Tütarlaps, see on ikka üks mure, kas sa saad aru? Kaks nädalat on seal suletus! Kui mina oleks noorem, läheksin mina sinna linna keskossa, aga minu kontid ei kannaks... Aga need noored, nemad teevad seda kindlasti hästi, eks? Kas sa tead, et sealsamas naabruses on suurepärane kohvik, kust saan võtta sooja tee..."

**Evaluation criteria:**
Official should be stiff/bureaucratic. Friend message should be casual (maybe slang, short sentences). Grandma should be chatty, emotional, digressive. If all three sound similar, register control is degraded.
