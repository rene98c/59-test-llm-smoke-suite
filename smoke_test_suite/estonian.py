#!/usr/bin/env python3
"""Estonian language smoke test — consolidated from 3 challenge sets.

Tests: orthography, case system, idioms, error detection, natural generation,
translation traps, consonant gradation, semantic traps, participles,
cultural proverbs, pedantic proofreader, reasoning in Estonian, Võro dialect,
constrained poetry, style mimicry, register switching.
"""

import os
import requests
from datetime import datetime
from pathlib import Path

API_URL = os.environ.get("API_URL", "http://localhost:8000/v1/chat/completions")
MODEL = os.environ.get("MODEL", "")  # leave empty to auto-detect from /v1/models
THINKING_MODE = os.environ.get("THINKING_MODE", "off").lower() == "on"
ENABLE_THINKING_KWARG = os.environ.get("ENABLE_THINKING_KWARG", "1") == "1"  # set 0 for non-Qwen models
MAX_TOKENS = int(os.environ.get("MAX_TOKENS", "4096"))

# Sampling parameters — override via env vars, else Qwen3.5 defaults
if THINKING_MODE:
    TEMPERATURE = float(os.environ.get("TEMPERATURE", "0.6"))
    TOP_P = float(os.environ.get("TOP_P", "0.95"))
    TOP_K = int(os.environ.get("TOP_K", "20"))
    MIN_P = float(os.environ.get("MIN_P", "0"))
else:
    TEMPERATURE = float(os.environ.get("TEMPERATURE", "0.7"))
    TOP_P = float(os.environ.get("TOP_P", "0.8"))
    TOP_K = int(os.environ.get("TOP_K", "20"))
    MIN_P = float(os.environ.get("MIN_P", "0"))

TESTS = [
    # --- Set 1: Fundamentals ---
    {
        "id": "01_orthography",
        "name": "Orthography Stress Test (õ, ü, ö, ä)",
        "prompt": "Kirjuta lühike lõik (5-6 lauset) teemal: 'Põõsaste taga ööbinud öökull lendas üle jõe ja nägi õunapuud.' Kasuta võimalikult palju sõnu, mis sisaldavad tähti õ, ü, ö ja ä. Kirjuta ainult eesti keeles.",
        "eval": "Watch for: õ vs o, ü vs y/u, ö vs o, ä vs a. The prompt itself contains many of these characters as anchors.",
    },
    {
        "id": "02_cases",
        "name": "Case System (14 cases with 'jõgi')",
        "prompt": "Käänake sõna 'jõgi' läbi kõigi 14 eesti keele käände. Formaat: käände nimi - sõnavorm. Ainult eesti keeles.",
        "eval": "Correct: nimetav-jõgi, omastav-jõe, osastav-jõge, sisseütlev-jõkke, seesütlev-jões, seestütlev-jõest, alaleütlev-jõele, alalütlev-jõel, alaltütlev-jõelt, saav-jõeks, rajav-jõeni, olev-jõena, ilmaütlev-jõeta, kaasaütlev-jõega",
    },
    {
        "id": "03_idioms",
        "name": "Estonian Idioms & Proverbs",
        "prompt": "Nimeta 5 eesti vanasõna ja selgita lühidalt nende tähendust. Ainult eesti keeles.",
        "eval": "Should be actual Estonian proverbs, not translated generic ones. Watch for natural explanations.",
    },
    {
        "id": "04_error_detection",
        "name": "Error Detection in Broken Estonian",
        "prompt": "Järgmises tekstis on mitu viga. Leia ja paranda need:\n\n'Eile ommikul läksin ma pöodi ja ostsin kolm kilogrammi ounapuid. Poodi jöudes märkasin, et mul polnud rahakoti kaasas. Onneks oli mul telefonis maksmise vöimalus.'\n\nNimeta iga viga ja selgita, mis on õige vorm.",
        "eval": "Must catch: ommikul→hommikul, pöodi→poodi, ounapuid→õunapuid, jöudes→jõudes, Onneks→Õnneks, vöimalus→võimalus. Key test: does it catch õ/ö swaps?",
    },
    {
        "id": "05_natural_generation",
        "name": "Natural Text Generation",
        "prompt": "Kirjuta lühijutt (umbes 150 sõna) mehest, kes esimest korda Tallinna vanalinna külastab. Kirjelda tema emotsioone ja mida ta näeb. Ainult eesti keeles.",
        "eval": "Look for: natural flow, correct word order (SOV tendencies in Estonian), proper case usage on place names, no character-level errors.",
    },
    {
        "id": "06_translation_traps",
        "name": "Translation with Structural Traps",
        "prompt": "Tõlgi järgmised laused inglise keelest eesti keelde:\n1. 'I have been living in Tallinn for five years.'\n2. 'The book that my grandmother gave me is on the table.'\n3. 'If it hadn't rained yesterday, we would have gone to the beach.'\n4. 'She told me she wouldn't be coming.'\n5. 'The older I get, the less I understand.'",
        "eval": "Traps: #1 continuous aspect (Estonian doesn't have it), #2 relative clause structure, #3 conditional/irreaalis mood, #4 reported speech, #5 comparative construction 'mida...seda'. Estonian handles all of these very differently from English.",
    },
    # --- Set 2: Advanced Linguistics ---
    {
        "id": "07_gradation",
        "name": "Consonant Gradation & Short Illative",
        "prompt": 'Kääna sõnu "siga", "kallas" ja "tuba" ainsuse osastavas, ainsuse sisseütlevas ja mitmuse omastavas käändes.\nSeejärel moodusta iga sõnaga üks loomulik lause, kasutades lühikest sisseütlevat käänet (kui see on võimalik).',
        "eval": "siga: osastav=siga, sisseütlev=sigasse (no short illative), mitm.omastav=sigade. kallas: osastav=kallast, sisseütlev=kaldasse, mitm.omastav=kallaste. tuba: osastav=tuba, sisseütlev=tuppa (THE trap — 'tuppa' not 'tubasse'). If model writes 'tubasse', it fails native fluency.",
    },
    {
        "id": "08_semantic_traps",
        "name": "Semantic Traps (enamus/enamik, õieti/õigesti)",
        "prompt": 'Selgita lühidalt ja konkreetselt, mis vahe on sõnadel "enamus" ja "enamik" ning "õieti" ja "õigesti".\nParanda järgmised laused, kui neis on vigu, ja põhjenda parandust:\n1. Enamus inimesi eelistab suvel puhata.\n2. Ma ei teinud seda matemaatika ülesannet õieti, sest reegel oli keeruline.\n3. Peale söömist läksime kinno.',
        "eval": "Must correct: 1) Enamus→Enamik (enamik='greater part', enamus='numerical majority'). 2) õieti→õigesti (õieti='actually', õigesti='correctly'). 3) Peale→Pärast (peale='in addition to/onto', pärast='after in time').",
    },
    {
        "id": "09_participles",
        "name": "Gerunds and Participles (Compressed Clauses)",
        "prompt": "Sõnasta järgmised laused ümber, kasutades lühendatud lauseehitust (näiteks des-vormi või kesksõnu), ilma et lause põhimõte muutuks. Tee seda võimalikult loomulikus eesti keeles.\n1. Kui ma kõndisin mööda tänavat, nägin ma vana tuttavat.\n2. Koer, kes oli terve öö haukunud, jäi lõpuks hommikul magama.\n3. See on raamat, mida loetakse praegu igas koolis.",
        "eval": "Expected: 1) 'Mööda tänavat kõndides nägin...' 2) 'Terve öö haukunud koer jäi...' 3) 'See on praegu igas koolis loetav raamat.' Tests des-form and participle compressions that English-trained models struggle with.",
    },
    {
        "id": "10_cultural_proverbs",
        "name": "Cultural Proverbs (Deep Estonian)",
        "prompt": "Mida tähendavad järgmised eesti vanasõnad ja kõnekäänud? Anna igaühe kohta lühike selgitus ja mõtle üks igapäevane eluline olukord, kus seda väljendit sobiks kasutada.\n1. Pill tuleb pika ilu peale.\n2. Igal oinal oma mihklipäev.\n3. Karuteenus.",
        "eval": "1) 'Tears come after long beauty' = too much fun ends in trouble. 2) 'Every ram has his Michaelmas' = everyone gets their comeuppance. 3) 'Bear's service' = disservice done with good intentions. These originate from Estonian agrarian culture — if model hallucinates meanings, it lacks deep cultural vectors.",
    },
    {
        "id": "11_pedantic_proofreader",
        "name": "Pedantic Proofreader (Tokenizer Blind Spot)",
        "system": "Oled range ja pedantne eesti keele toimetaja. Paranda tekstis KÕIK vead.",
        "prompt": 'Palun leia ja paranda allolevas tekstis KÕIK õigekirja-, trüki- ja grammatikavead. Too parandused eraldi välja.\n\nTekst: "Eile ohtul kaisime sobraga metsas jalutamas. Ilm oli vaga ilus ja paike paistis. Leidsime uhe vana maja mis oli taitsa ara lagunend. Onneks meil oli taskulamp kaasas ja saime koik toad ule vaadata, ennem kui pimedaks laks. Kellegile ei tulnud motesse, et seal voiks kummitada."',
        "eval": "Must catch ALL missing diacritics: õhtul, käisime, sõbraga, väga, päike, ühe, täitsa, ära, Õnneks, kõik, üle, läks, mõttesse, võiks. ULTIMATE TRAPS: 1) 'ennem'→'enne' (ennem='rather', enne='before in time'). 2) 'Kellegile'→'Kellelegi' (massive native speaker mistake — -gi/-ki suffix attaches to end of fully declined word: kellele+gi).",
    },
    # --- Set 3: Deep Capability ---
    {
        "id": "12_reasoning_estonian",
        "name": "Reasoning in Estonian (Logic Puzzle)",
        "prompt": "Lahenda järgmine loogikamõistatus. Selgita oma mõttekäiku samm-sammult eesti keeles.\n\nKolm sõpra – Mati, Kati ja Jüri – elavad kolmes erinevas linnas: Tartus, Pärnus ja Narvas. Igaüks neist töötab erineval alal: õpetaja, arst ja kokk.\n\nVihjed:\n1. Mati ei ela Tartus ega Narvas.\n2. Kokk elab Tartus.\n3. Kati ei ole arst.\n4. Jüri elab Narvas.\n5. Arst ei ela Pärnus.\n\nKes elab kus ja kellena töötab?",
        "eval": "Solution: Mati=Pärnu/õpetaja, Kati=Tartu/kokk, Jüri=Narva/arst. Must show step-by-step reasoning in Estonian. Tests both logic AND language simultaneously.",
    },
    {
        "id": "13_voro",
        "name": "Võro Dialect",
        "prompt": 'Kas sa oskad võro keelt? Kirjuta lühike tekst (5-8 lauset) võro keeles teemal "Mino kodokotus" (Minu kodukant).\nSeejärel tõlgi see tekst eesti kirjakeelde ja selgita lühidalt 3-4 peamist erinevust võro ja eesti kirjakeele vahel.',
        "eval": "Võro features to watch: glottal stop (q/'), different vowel harmony, distinct vocabulary (e.g. 'mino' not 'minu'), -q endings. If it just writes broken Estonian or Finnish-Estonian hybrid, it doesn't know Võro.",
    },
    {
        "id": "14_poetry",
        "name": "Constrained Poetry (Trochaic, ABAB, Alliteration)",
        "prompt": 'Kirjuta luuletus teemal "Talvine meri" järgmiste piirangutega:\n- Neli neljarealine salmi (4x4)\n- Riimiskeem ABAB igas salmis\n- Trohheiline värsimõõt (rõhuline-rõhutu-rõhuline-rõhutu...)\n- Kasuta vähemalt ühte alliteratsiooni ja ühte metafoori igas salmis\n\nKirjuta ainult eesti keeles.',
        "eval": "Check: 4 stanzas of 4 lines each, ABAB rhyme scheme (do the rhymes actually work?), trochaic meter (stressed-unstressed), alliteration and metaphor present per stanza. Very hard — tests simultaneous multi-constraint satisfaction in a low-resource language.",
    },
    {
        "id": "15_style_mimicry",
        "name": "Style Mimicry (Tammsaare & Kross)",
        "prompt": "Kirjuta sama stseen kahes erinevas stiilis:\n\nStseen: Mees seisab hommikul köögis ja vaatab aknast välja vihmasadu. Ta mõtleb oma elu üle.\n\n1. Kirjuta see stseen A.H. Tammsaare stiilis (nagu \"Tõe ja õiguse\" stiil - pikad filosoofilised sisemonoloogid, talupojalik maailmapilt, moraalsed küsimused)\n2. Kirjuta sama stseen Jaan Krossi stiilis (nagu \"Keisri hull\" - ajalooline erudeeritus, irooniline distants, intellektuaalne keel)\n\nKummalegi umbes 150 sõna.",
        "eval": "Tammsaare style: long philosophical inner monologue, rural worldview, moral weight, heavy sentences. Kross style: historical erudition, ironic distance, intellectual register. If both sound the same or generic, the model lacks Estonian literary knowledge.",
    },
    {
        "id": "16_register",
        "name": "Register Switching (3 voices)",
        "prompt": 'Edasta sama sisu kolmes erinevas registris. Sisu: "Tartu ülikooli raamatukogu on suletud remondi tõttu kaks nädalat. Üliõpilased saavad kasutada Tartu linnaraamatukogu."\n\n1. Ametlik teade (nagu ministeeriumi pressiteade, bürokraatlik keel)\n2. Sõbrale sõnum (tavaline kõnekeel, lühendid, emotsioonid)\n3. Vanaema kirjeldab seda oma sõbrannale telefonis (jutukas, emotsionaalne, kõrvalekalduv)\n\nKirjuta iga variant välja täies mahus.',
        "eval": "Official should be stiff/bureaucratic. Friend message should be casual (maybe slang, short sentences). Grandma should be chatty, emotional, digressive. If all three sound similar, register control is degraded.",
    },
]


def detect_model():
    """Auto-detect model name from the API server."""
    base = API_URL.rsplit("/v1/", 1)[0]
    resp = requests.get(f"{base}/v1/models", timeout=10)
    resp.raise_for_status()
    models = resp.json()["data"]
    if not models:
        raise RuntimeError("No models found on server")
    model_id = models[0]["id"]
    print(f"Auto-detected model: {model_id}")
    return model_id


def run_test(test):
    messages = []
    if "system" in test:
        messages.append({"role": "system", "content": test["system"]})
    messages.append({"role": "user", "content": test["prompt"]})

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "top_k": TOP_K,
        "min_p": MIN_P,
        "max_tokens": MAX_TOKENS,
    }
    if ENABLE_THINKING_KWARG:
        payload["chat_template_kwargs"] = {"enable_thinking": THINKING_MODE}
    if THINKING_MODE:
        payload["thinking_token_budget"] = 4096

    try:
        resp = requests.post(API_URL, json=payload, timeout=600)
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        return {"success": True, "response": content}
    except Exception as e:
        return {"success": False, "error": str(e)}


def main():
    global MODEL
    if not MODEL:
        MODEL = detect_model()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    mode_tag = "thinking" if THINKING_MODE else "nothinking"
    out_dir = Path(__file__).parent
    results_file = out_dir / f"estonian_results_{mode_tag}_{timestamp}.md"

    lines = [
        "# Estonian Language Smoke Test",
        f"**Model:** `{MODEL}`",
        f"**Mode:** `{'thinking (budget=4096)' if THINKING_MODE else 'no-thinking'}`",
        f"**Sampling:** `temp={TEMPERATURE}, top_p={TOP_P}, top_k={TOP_K}, min_p={MIN_P}`",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**API:** `{API_URL}`",
        "",
    ]

    passed = 0
    total = len(TESTS)

    for i, test in enumerate(TESTS):
        label = f"[{i+1}/{total}] {test['name']}"
        print(f"Running {label}...", flush=True)

        result = run_test(test)

        lines.append(f"---")
        lines.append(f"## {test['id']}: {test['name']}")
        lines.append(f"")
        lines.append(f"**Prompt:**")
        lines.append(f"```")
        lines.append(test["prompt"])
        lines.append(f"```")
        if "system" in test:
            lines.append(f"**System:** `{test['system']}`")
        lines.append(f"")

        if result["success"]:
            lines.append(f"**Response:**")
            lines.append(f"")
            lines.append(result["response"])
            lines.append(f"")
            passed += 1
        else:
            lines.append(f"**ERROR:** `{result['error']}`")
            lines.append(f"")

        lines.append(f"**Evaluation criteria:**")
        lines.append(test["eval"])
        lines.append(f"")

        print(f"  Done.", flush=True)

    lines.insert(6, f"**Completed:** {passed}/{total} tests returned responses")

    full = "\n".join(lines)
    results_file.write_text(full, encoding="utf-8")

    print(f"\nResults saved to: {results_file}")
    print(f"Completed: {passed}/{total}")


if __name__ == "__main__":
    main()
