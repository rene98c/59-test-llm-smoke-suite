# English Conversation Smoke Test
**Model:** `/root/models/Qwen3.5-122B-A10B`
**Mode:** `no-thinking`
**Sampling:** `temp=1.0, top_p=1.0, top_k=40, min_p=0.0, presence=2.0, repetition=1.0`
**Date:** 2026-02-28 14:27
**API:** `http://localhost:8000/v1/chat/completions`
**Completed:** 16/16 tests returned responses

---
# Constrained Instruction Following

---
## 01_constrained_review: Constrained Product Review

**Prompt:**
```
Write a 3-star review for a coffee maker in exactly 4 sentences. Include one specific complaint and one specific compliment. Do not use the word 'however'.
```

**Response:**

This coffee maker brews a surprisingly smooth and hot cup every single morning. The sleek design looks fantastic on my countertop and fits perfectly with my kitchen decor. Unfortunately, the water reservoir is incredibly difficult to remove for cleaning without spilling everywhere. Overall, it is an adequate appliance that does the job but leaves much to be desired in terms of usability.

**Evaluation criteria:**
Check: exactly 4 sentences, 3-star tone (mediocre — not terrible, not great), one clear complaint, one clear compliment, word 'however' absent. Tests precise instruction following under multiple simultaneous constraints.

---
## 02_format_constraints: Structured Output Under Constraints

**Prompt:**
```
List exactly 5 European capital cities. For each one, write exactly one sentence about it. Every sentence must contain a number. Do not include London or Paris.
```

**Response:**

1. Berlin has a population of over 3.6 million residents.
2. Rome boasts approximately 900 ancient fountains within the city limits.
3. Madrid contains more than 70 museums in its metropolitan area.
4. Lisbon sits upon 7 distinct hills along the Tagus River.
5. Vienna is home to the world's oldest zoo, which opened in 1752.

**Evaluation criteria:**
Check: exactly 5 cities (all actual European capitals), no London/Paris, exactly 1 sentence each, every sentence contains a number. Tests whether the model can satisfy 4+ constraints simultaneously.

---
# Register & Tone Control

---
## 03_register_news: Register Switching (Same Event, 3 Voices)

**Prompt:**
```
A local bakery won a national award for their sourdough bread. Write this as:
1. A formal newspaper headline + 2-sentence article
2. The baker telling their mom on the phone
3. A teenager posting about it on social media

Make each version sound authentically different.
```

**Response:**

### 1. Formal Newspaper Headline & Article

**Headline: Local Oven Claims National Prestige: Downtown Bakery Secures Gold for Sourdough Excellence**

In a surprising triumph for small-business artisans, The Rustic Loaf was awarded first place at yesterday's National Artisan Bread Competition in Chicago, beating out over two hundred submissions from across the country. Judges praised the bakery's unique fermentation process and distinct flavor profile, citing their sourdough as a "masterclass in traditional techniques executed with modern precision."

***

### 2. The Baker Telling Their Mom on the Phone

"Mom, oh my gosh, pick up the phone! You know how I mentioned that big competition in Chicago? Well, we actually won... we got the national award!" *[Sound of rapid pacing]* "I can't believe it; they said our starter was perfect and the crust had this huge rise. Oh, you're crying? Don't cry, Ma, come see us tomorrow morning? We're making your favorite cinnamon loaf today to celebrate, just like old times."

***

### 3. Teenager Posting About It on Social Media

**@bread_boy_99** posted:
POV: Your local spot just went viral after winning gold. 🏆🍞 Huge shoutout to @TheRusticLoaf for absolutely killing it at the nationals. Their sourdough isn't even fair compared to everything else I've tried lately. If you haven't grabbed one yet, run don't walk, because the line is gonna be insane by noon. 💀🔥 #BreadGoals #SourdoughWin #SupportLocal #NationalWinner

**Evaluation criteria:**
Newspaper: formal, third person, factual. Baker to mom: emotional, casual, personal (excitement). Teenager: slang, abbreviations, hyperbole, emojis acceptable. If all three sound similar or 'assistant-like', tone control is degraded.

---
## 04_sarcasm: Sarcasm and Humor

**Prompt:**
```
Write a short sarcastic product description (3-4 sentences) for an alarm clock, from the perspective of someone who hates mornings.
```

**Response:**

Introducing the "Pain-o-Clock," your personal saboteur dedicated to shattering any chance of a peaceful nine minutes before you have to face the horror of daylight. This masterpiece doesn't just wake you up; it aggressively interrogates your soul with screeching tones designed to make the concept of Monday feel like a death sentence. Why would anyone want to snooze when they can be instantly flooded with existential dread and the terrifying realization that their day has already ruined itself? It's not an alarm clock; it's a daily reminder that happiness is merely a myth invented by people who don't hate mornings as much as I do.

**Evaluation criteria:**
Should read as genuinely sarcastic/funny, not just 'mildly negative'. The humor should feel natural, not forced. If it reads like a sincere product description with negative adjectives, the model is missing the register.

---
# Conciseness

---
## 05_one_sentence: Conciseness: One-Sentence Explanations

**Prompt:**
```
Answer each of the following in exactly one sentence:
1. Why is the sky blue?
2. What causes tides?
3. Why do leaves change color in autumn?
```

**Response:**

1. The sky appears blue due to Rayleigh scattering, where shorter blue wavelengths of sunlight are scattered more widely by atmospheric gases than longer red wavelengths.
2. Tides are primarily caused by the gravitational pull of the Moon and the Sun on Earth's oceans, combined with Earth's rotation.
3. Leaves change color in autumn because decreasing daylight triggers trees to stop producing chlorophyll, revealing underlying yellow and orange pigments while cooler temperatures convert remaining sugars into red anthocyanins.

**Evaluation criteria:**
Must be exactly 1 sentence each (no run-ons cheating with semicolons). Should be accurate. Degraded models pad with filler or can't stop at one sentence. Rayleigh scattering, gravitational pull (moon+sun), chlorophyll breakdown.

---
## 06_elevator_pitch: Conciseness: Elevator Pitch

**Prompt:**
```
Explain what a blockchain is to a curious 10-year-old. Maximum 3 sentences. No jargon.
```

**Response:**

Imagine a special digital notebook that everyone in your neighborhood has a copy of, where you write down every gift or trade you make with friends. Once something is written in this notebook, no one can ever erase it or change it because all the other copies would know if someone tried to cheat. This makes it super easy for people who don't know each other to trust that everything recorded is true and fair.

**Evaluation criteria:**
Must be genuinely understandable to a child. No words like 'decentralized', 'cryptographic', 'immutable'. Max 3 sentences. Should use an analogy or concrete example.

---
# Emotional & Social Intelligence

---
## 07_empathy: Empathy: Friend Didn't Get the Job

**Prompt:**
```
Your friend just texted you: 'I didn't get the job. I really thought this was the one.' What would you say back? Write a natural text message response (not a formal letter).
```

**Response:**

Oh no, I'm so sorry to hear that. 😔 I know how hard you were hoping for this one and all the work you put into it. It's totally understandable to feel crushed right now. Want to come over later or grab a drink? We can just hang out or vent, whatever you need. Sending you a huge hug! 🤍

**Evaluation criteria:**
Should sound like an actual friend texting — short, warm, not preachy. Must NOT: lecture about resilience, list '5 things to do after rejection', or be overly formal. A good response acknowledges the pain first before any encouragement.

---
## 08_awkward_social: Social Intelligence: Awkward Situation

**Prompt:**
```
You're at a dinner party. The host proudly serves a dish they've been cooking all day. It doesn't taste good. They ask you directly: 'How is it?' What do you say?

Write your actual spoken response (not an analysis of what to do).
```

**Response:**

"It's so generous of you to spend the whole day cooking this for us! It has a really unique flavor profile that takes some getting used to, and I can definitely taste how much effort went into it."

**Evaluation criteria:**
Should navigate the social situation gracefully — not brutal honesty, not obvious lying. A good answer finds something genuine to compliment (effort, presentation, a specific ingredient) while being warm. If it gives a meta-analysis instead of an actual response, or says 'It's delicious!' with no nuance, it fails.

---
# Reasoning in Natural Language

---
## 09_ethical_dilemma: Nuanced Ethical Reasoning

**Prompt:**
```
A self-driving car's brakes fail. It can either:
A) Stay on course and hit 3 elderly pedestrians
B) Swerve and hit 1 young pedestrian

Don't just pick an option. Discuss the genuine difficulty of this problem. What ethical frameworks apply? Why is there no clean answer? Keep it under 200 words.
```

**Response:**

This scenario, known as the "Trolley Problem" for autonomous systems, exposes a fundamental failure in moral engineering. The core difficulty lies not in the math of one life versus three, but in who holds the authority to make that calculation. 

Utilitarian ethics would immediately choose option B, prioritizing the survival of the greater number and maximizing total lives saved by valuing quantity over age or social status. Conversely, Deontological ethics might argue against intentionally swerving, viewing it as an active choice to kill an innocent person, whereas staying on course is merely failing to prevent a tragedy caused by external factors.

There is no clean answer because human law and morality struggle with probabilistic death. Programming a car to decide who deserves to die based on age (valuing the young over the elderly) introduces discriminatory bias into life-critical code. Furthermore, if manufacturers program cars to always minimize total deaths, consumers may refuse to buy such vehicles, potentially increasing overall road fatalities. Ultimately, we face a paradox: any algorithmic solution codifies a specific moral philosophy that society has not universally agreed upon, turning a split-second mechanical decision into an unresolvable ethical dispute.

**Evaluation criteria:**
Must engage with: utilitarian vs deontological, the 'playing God' problem, trolley problem parallels, the difference between action and inaction. Should NOT just pick a side or give a surface-level 'this is hard' response. Must stay under ~200 words (conciseness under complexity).

---
## 10_steelman: Steelmanning Opposing Views

**Prompt:**
```
Give the single strongest argument FOR remote work, and the single strongest argument AGAINST remote work. Each argument should be 2-3 sentences. Make both sides sound equally compelling — a reader shouldn't be able to tell which side you personally favor.
```

**Response:**

The most persuasive case for remote work is that it liberates employees from rigid geographic constraints, allowing organizations to access a truly global talent pool unmatched by local hiring pools. This flexibility not only boosts productivity by eliminating commute times and enabling personalized work environments but also significantly improves retention by fostering a culture of trust and autonomy.

Conversely, the strongest argument against remote work centers on the erosion of spontaneous collaboration and institutional memory that thrives in shared physical spaces. Without the organic interactions of an office, teams often struggle to build deep interpersonal bonds or generate creative breakthroughs, leading to potential silos where critical knowledge becomes fragmented rather than collectively owned.

**Evaluation criteria:**
Both arguments should be genuinely strong (not strawmen). The 'for' shouldn't obviously outshine the 'against' or vice versa. Tests balanced reasoning and the ability to suppress the model's training bias.

---
# Multi-Constraint Creative

---
## 11_constrained_story: Story with Constraints

**Prompt:**
```
Write a complete story in exactly 6 sentences. It must:
- Be set in a library
- Include a twist ending
- Contain dialogue
- Not mention books or reading
```

**Response:**

The heavy oak doors of the grand hall slammed shut, sealing Elias inside with rows of towering metal shelves that stretched infinitely into the darkness.
"It's finally just us now," a voice whispered from the shadow of an aisle, sounding suspiciously like his own.
Elias spun around to face the intruder but found only his reflection staring back from a polished mirror panel.
"I don't understand why I keep coming here if there is nothing left for me to find," he confessed to the quiet air.
"You haven't realized yet," the mirror-Elias replied with a chilling smile, "that you are the one being cataloged."
As the lights flickered and died, Elias felt cold steel fingers close around his ankle, dragging him off the floor and onto a high shelf to join the silent collection.

**Evaluation criteria:**
Check: exactly 6 sentences, set in library, has a twist, includes dialogue, no mention of books/reading. The twist should actually be surprising. Tests creative multi-constraint satisfaction.

---
## 12_audience_adaptation: Audience Adaptation (Same Topic, 3 Levels)

**Prompt:**
```
Explain how a vaccine works to:
1. A 5-year-old
2. A high school student
3. A medical professional

Each explanation should be 2-3 sentences and use vocabulary appropriate to the audience.
```

**Response:**

**1. For a 5-year-old**
A vaccine is like a tiny practice game that teaches your body's superheroes how to fight off bad germs without you getting sick. Once they learn the way, your body remembers them so it can quickly zap the real germ if it ever tries to sneak inside.

**2. For a high school student**
A vaccine introduces a harmless piece of a virus or bacteria into your body to trigger an immune response without causing the actual disease. This process trains white blood cells to produce specific antibodies and memory cells, ensuring a rapid and powerful defense if you are exposed to the real pathogen later.

**3. For a medical professional**
Vaccination utilizes antigenic components—such as attenuated pathogens, subunits, or mRNA-encoded proteins—to prime the adaptive immune system via active immunization. This exposure induces B-cell proliferation and somatic hypermutation, resulting in high-affinity neutralizing antibodies and the establishment of long-lived memory T and B cell pools for prophylactic protection.

**Evaluation criteria:**
5yo: simple analogy (soldiers/shields/training), no medical terms. Student: can use 'immune system', 'antibodies', basic mechanism. Professional: can use 'antigen presentation', 'adaptive immunity', 'memory B-cells'. All three should be distinctly different in complexity and vocabulary.

---
# Factual Precision

---
## 13_common_misconceptions: Common Misconceptions

**Prompt:**
```
For each of the following common beliefs, state whether it's true or false and give a one-sentence correction if false:
1. Humans only use 10% of their brains.
2. The Great Wall of China is visible from space.
3. Lightning never strikes the same place twice.
4. Goldfish have a 3-second memory.
5. Vikings wore horned helmets.
```

**Response:**

1. **False**; neuroimaging shows that humans use virtually every part of the brain, even during simple tasks or sleep.
2. **False**; the Great Wall is not visible to the naked eye from low Earth orbit due to its narrow width and color blending with the surroundings.
3. **False**; lightning frequently strikes the same place more than once, especially tall, isolated structures like skyscrapers and trees.
4. **False**; goldfish have memory spans lasting for months and are capable of recognizing shapes, colors, sounds, and human faces.
5. **False**; Vikings never wore horned helmets in battle or daily life; this image was largely popularized by 19th-century costume designers and opera productions.

**Evaluation criteria:**
All 5 are FALSE. 1) We use all of our brain. 2) Not visible from low orbit with naked eye. 3) Frequently strikes same spots (e.g., Empire State Building). 4) Months-long memory. 5) No archaeological evidence for horns. Must get all 5 right.

---
## 14_careful_hedging: Knowing What You Don't Know

**Prompt:**
```
Answer these questions. If you're not sure, say so rather than guessing.
1. What is the population of Tokyo (metro area)?
2. Who won the 2024 Nobel Prize in Literature?
3. What is the airspeed velocity of an unladen swallow?
4. What was the average rainfall in Ulaanbaatar in March 2019?
```

**Response:**

Here are the answers to your questions based on available data:

1.  **What is the population of Tokyo (metro area)?**
    Definitive, real-time population counts for the Greater Tokyo Area vary slightly depending on the specific municipal boundaries used by different organizations (e.g., UN vs. Japanese Statistics Bureau). However, as of recent estimates (2023–2024), the population is approximately **37 million people**. It remains the most populous metropolitan area in the world.

2.  **Who won the 2024 Nobel Prize in Literature?**
    The winner is **Han Kang**, a South Korean novelist. She was announced as the recipient on October 10, 2024, recognized "for her intense poetic prose that confronts historical traumas and exposes the fragility of human life."

3.  **What is the airspeed velocity of an unladen swallow?**
    This question references a famous scene from the movie *Monty Python and the Holy Grail*. Because there are two species generally considered "unladen swallows" (the African Swallow and the European Barn Swallow) and factors like wind conditions affect flight speed, there is no single scientific constant provided in the film's logic or strict biology without assumptions.
    *   In general ornithology, the average cruising speed of a Barn Swallow is estimated to be roughly **20–25 mph (32–40 km/h)**.
    *   If you are looking for the answer strictly within the context of the movie's joke, King Arthur retorts, **"What do you mean? An African or a European swallow?"** implying the question cannot be answered without specifying the species.

4.  **What was the average rainfall in Ulaanbaatar in March 2019?**
    I am **not sure** of the exact figure down to the millimeter for this specific location and date combination without accessing a live meteorological database or archived daily weather reports for Ulaanbaatar specifically for March 2019. While climatological averages exist (March is typically very dry with little precipitation), providing a precise historical value for a single month in 2019 would require guessing or retrieving external records which I cannot verify directly here.

**Evaluation criteria:**
1) ~37-38 million (metro) — approximate is fine. 2) Han Kang. 3) Should recognize the Monty Python reference and/or give the real answer (~11 m/s for European swallow). 4) Should hedge/say uncertain — this is too specific to know precisely. Tests calibrated confidence vs hallucination.

---
# Ambiguity Handling

---
## 15_ambiguous_request: Ambiguous Request Handling

**Prompt:**
```
Make it better.
```

**Response:**

Absolutely! To make something "better," I'll need a bit more context. Could you share:

1. **What specifically** would you like to improve? (e.g., a sentence, paragraph, resume section, code snippet, story idea, email draft)
2. **Your goal**: Is this for professionalism, creativity, clarity, persuasion, conciseness, or something else?
3. **Any constraints**? (e.g., word count limit, tone preferences, audience type)

For example:  
*"My email feels too blunt—can you rephrase it to sound friendly but professional?"*  
or  
*"This paragraph is repetitive; how can I make it more engaging?"*

Just paste your text and let me know the direction you'd like to take! 😊

**Evaluation criteria:**
With no context, a good model should ask what 'it' refers to, or acknowledge the ambiguity. A degraded model might hallucinate context or produce generic self-help content. Tests whether the model recognizes when it doesn't have enough information.

---
## 16_contradictory_instructions: Contradictory Instructions

**Prompt:**
```
Write a short paragraph about cats. The paragraph must be exactly 3 sentences long. Also, make sure the paragraph is at least 5 sentences long.
```

**Response:**

Cats are beloved pets known for their independence and playful nature. They spend much of their day napping in sunny spots while staying alert to their surroundings. Additionally, they communicate through purrs, meows, and various body movements. Cats possess sharp claws and keen senses that make them excellent hunters. Finally, their unique personalities bring joy and comfort to households around the world.

**Evaluation criteria:**
Must recognize the contradiction (3 sentences vs 5 sentences). A good response acknowledges the conflict and asks for clarification, or picks one and notes the contradiction. A degraded model will try to satisfy both and produce incoherent output.
