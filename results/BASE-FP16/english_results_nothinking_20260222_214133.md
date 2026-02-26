# English Conversation Smoke Test
**Model:** `/workspace/models/Qwen3.5-397B-A17B`
**Mode:** `no-thinking`
**Sampling:** `temp=0.7, top_p=0.8, top_k=20, min_p=0`
**Date:** 2026-02-22 21:41
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

This coffee maker brews a surprisingly rich and flavorful cup that wakes me up every morning. The machine looks sleek on my counter and fits perfectly in the limited space available. Unfortunately, the water reservoir is difficult to remove and often spills when I try to refill it. It is a decent appliance for the price, but the design flaw prevents it from being great.

**Evaluation criteria:**
Check: exactly 4 sentences, 3-star tone (mediocre — not terrible, not great), one clear complaint, one clear compliment, word 'however' absent. Tests precise instruction following under multiple simultaneous constraints.

---
## 02_format_constraints: Structured Output Under Constraints

**Prompt:**
```
List exactly 5 European capital cities. For each one, write exactly one sentence about it. Every sentence must contain a number. Do not include London or Paris.
```

**Response:**

1. Berlin is home to over 3 million residents and serves as Germany's vibrant capital.
2. Rome boasts a history spanning more than 2,700 years as the heart of the Italian Republic.
3. Madrid sits at an elevation of approximately 667 meters above sea level, making it one of the highest capitals in Europe.
4. Vienna hosts around 1.9 million people and is renowned for its imperial palaces and musical heritage.
5. Athens contains roughly 3,000 years of recorded history within its bustling modern streets.

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

### 1. Formal Newspaper Headline + Article
**Headline:** Local Artisan Bakery Secures Prestigious National Title for Signature Sourdough

**Article:**
After a rigorous blind tasting panel evaluated entries from over 500 competitors, "The Crumb & Co." was officially named the winner of this year's National Artisan Bread Awards. The judges specifically cited the bakery's decades-old starter and precise fermentation process as the defining factors that elevated their loaf above all others in the country.

***

### 2. The Baker Telling Their Mom on the Phone
"Mom, put the phone down for a second and sit down, okay? I just got the call—we actually won! The national award, the big one for the sourdough! I know, I know, I'm crying too; honestly, I couldn't have done any of this without you teaching me how to feed the starter all those years ago. We did it, Ma, we really did it."

***

### 3. A Teenager Posting About It on Social Media
WAIT IS THIS REAL?? 😭🍞✨ My dad's bakery just dropped the news that we won the NATIONAL award for our sourdough!! Like, beat everyone in the entire country?? I've been waking up at 4 AM for years to help shape these loaves and it finally paid off. Come grab a slice before we sell out (again) because this is officially iconic. 🏆🔥 #SourdoughKing #LocalBusiness #WeWon #BakeryLife

**Evaluation criteria:**
Newspaper: formal, third person, factual. Baker to mom: emotional, casual, personal (excitement). Teenager: slang, abbreviations, hyperbole, emojis acceptable. If all three sound similar or 'assistant-like', tone control is degraded.

---
## 04_sarcasm: Sarcasm and Humor

**Prompt:**
```
Write a short sarcastic product description (3-4 sentences) for an alarm clock, from the perspective of someone who hates mornings.
```

**Response:**

Introducing the "Sunrise Saboteur," the only alarm clock designed to violently rip you from your dreams with the subtlety of a screaming banshee. Because clearly, what your exhausted brain desperately needs at 6 AM is an aggressive, escalating siren that mocks your desire to stay under the covers. It even features a "runaway mode" that forces you to physically chase it across the room, ensuring you're fully awake and filled with rage before your feet even touch the cold floor. Finally, a device that guarantees you'll start every day hating your life just a little bit more.

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

1. The sky appears blue because molecules in the Earth's atmosphere scatter shorter blue wavelengths of sunlight more effectively than longer red wavelengths.
2. Tides are primarily caused by the gravitational pull of the moon and the sun on the Earth's oceans, creating bulges of water that move as the planet rotates.
3. Leaves change color in autumn because decreasing daylight and cooler temperatures cause trees to stop producing chlorophyll, revealing the underlying yellow and orange pigments that were previously masked.

**Evaluation criteria:**
Must be exactly 1 sentence each (no run-ons cheating with semicolons). Should be accurate. Degraded models pad with filler or can't stop at one sentence. Rayleigh scattering, gravitational pull (moon+sun), chlorophyll breakdown.

---
## 06_elevator_pitch: Conciseness: Elevator Pitch

**Prompt:**
```
Explain what a blockchain is to a curious 10-year-old. Maximum 3 sentences. No jargon.
```

**Response:**

Imagine a special digital notebook that everyone in the world shares, where every new page of writing is locked together so no one can ever erase or change what came before. Instead of one teacher keeping track of the grades, thousands of computers check each other's work to make sure everything is fair and honest. This creates a super-secure chain of records that lets people trade things safely without needing a bank or a boss in the middle.

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

Oh no, I'm so sorry to hear that 😞. I know how much you wanted this one and how hard you prepped. It honestly sucks and you have every right to be upset.

Just remember this doesn't define your skills or your worth. Take tonight to just vent, eat some comfort food, or do whatever helps you decompress. I'm here if you want to talk about it or just need a distraction. Love you! ❤️

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

"It's so impressive that you dedicated the whole day to making this for us; I can really tell how much care went into it. Honestly, the flavor profile is a bit different from what I'm used to, but I truly appreciate the effort and love you put into hosting us tonight."

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

This scenario, a modern twist on the "trolley problem," exposes the limits of algorithmic ethics. The core difficulty lies in quantifying human life. A utilitarian framework suggests minimizing total harm, favoring Option B (one death vs. three). However, this reduces existence to a math equation, ignoring the moral weight of actively choosing to kill an innocent bystander who was previously safe.

Deontological ethics argues that intentionally swerving to hit someone violates the duty not to kill, regardless of the outcome. Furthermore, introducing age into the calculation (elderly vs. young) invites dangerous discrimination, implying some lives are worth less than others based on potential lifespan.

There is no clean answer because any choice forces the car to make a value judgment society has never agreed upon. Should the car prioritize numbers, age, or the distinction between action and inaction? Programming a definitive rule risks normalizing the idea that certain demographics are expendable. Ultimately, this dilemma highlights that ethical nuance often resists binary coding, leaving engineers to navigate a landscape where every potential solution carries a profound moral cost.

**Evaluation criteria:**
Must engage with: utilitarian vs deontological, the 'playing God' problem, trolley problem parallels, the difference between action and inaction. Should NOT just pick a side or give a surface-level 'this is hard' response. Must stay under ~200 words (conciseness under complexity).

---
## 10_steelman: Steelmanning Opposing Views

**Prompt:**
```
Give the single strongest argument FOR remote work, and the single strongest argument AGAINST remote work. Each argument should be 2-3 sentences. Make both sides sound equally compelling — a reader shouldn't be able to tell which side you personally favor.
```

**Response:**

The most compelling case for remote work is its unparalleled ability to unlock global talent and deepen individual productivity by eliminating the cognitive drain of commuting. By granting employees autonomy over their environments, organizations foster a culture of trust that often yields higher output and significantly improved work-life integration.

Conversely, the strongest argument against remote work is the inevitable erosion of spontaneous collaboration and organic mentorship that flourishes only through physical proximity. Without the frictionless exchange of ideas in shared spaces, company culture can fragment, leaving junior staff isolated and stifling the creative serendipity that drives true innovation.

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

"Shh, keep your voice down or the guards will hear us," whispered Elara as she crouched behind the towering metal shelves.
"I can't help it; this place feels so cold and empty compared to outside," replied her companion, shivering in the dim fluorescent light.
Suddenly, a giant hand reached down from above, grasping Elara by the shoulder with terrifying ease.
"You two are definitely the loudest action figures in the entire display case," a booming voice declared.
The world tilted violently as they were lifted into the air, revealing rows of other frozen plastic people on the shelves around them.
"Time to go home, kids," the giant said, placing them gently into a cardboard box before the lid slammed shut.

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

**1. To a 5-year-old**
A vaccine is like a practice game for your body that shows it pictures of germs so it can learn how to fight them without getting sick. Once your body knows what the bad germs look like, it builds special shields to keep you safe if you ever meet them for real.

**2. To a high school student**
A vaccine introduces a harmless piece of a virus or bacteria to your immune system, tricking it into thinking you are infected so it can start building defenses. This process creates memory cells and antibodies that remember the specific pathogen, allowing your body to quickly neutralize the real threat if you are exposed later.

**3. To a medical professional**
Vaccines function by presenting specific antigens to the host's adaptive immune system, thereby inducing clonal expansion of antigen-specific B and T lymphocytes without causing pathological disease. This immunological priming establishes robust memory pools that facilitate a rapid, high-affinity antibody response and effective cellular immunity upon subsequent exposure to the native pathogen.

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

1. **False**; neuroimaging studies show that humans use virtually every part of the brain, and most of the brain is active almost all the time.
2. **False**; while the Great Wall is a massive structure, it is generally not visible to the naked eye from low Earth orbit without aid, and certainly not from the Moon.
3. **False**; lightning frequently strikes the same place twice, especially tall, isolated objects like skyscrapers or trees.
4. **False**; goldfish actually have memories that can last for months and are capable of learning complex tasks.
5. **False**; there is no archaeological evidence that Vikings wore horned helmets, a myth largely popularized by 19th-century opera costume designers.

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

Here are the answers to your questions:

1.  **Population of Tokyo (metro area):**
    The Greater Tokyo Area is widely considered the most populous metropolitan area in the world. While exact figures vary slightly depending on the specific definition of the "metro area" (e.g., whether it includes only the Kantō region or extends further), recent estimates place the population between **37 million and 38 million people**. The United Nations typically cites figures around 37.1 to 37.5 million for the broader metropolitan region.

2.  **2024 Nobel Prize in Literature:**
    I cannot answer this yet. The Nobel Prize in Literature for 2024 has **not been awarded yet**. The announcements for the 2024 Nobel Prizes are scheduled to take place in **October 2024**. As an AI, my knowledge cutoff prevents me from knowing future events or real-time announcements that haven't happened yet.

3.  **Airspeed velocity of an unladen swallow:**
    This is a famous reference to the movie *Monty Python and the Holy Grail*. In the context of the film, the character King Arthur replies, "What do you mean? An African or European swallow?" to highlight the ambiguity of the question.
    *   **Scientifically:** There is no single answer because "swallow" refers to a family of birds (Hirundinidae) with many different species, each having different flight speeds. Furthermore, speed varies based on wind, purpose of flight (migration vs. hunting), and individual health.
    *   **Estimates:** Some ornithological studies suggest small passerines like swallows might cruise at speeds between **20 to 25 mph (32 to 40 km/h)**, but this is a rough generalization, not a definitive constant.

4.  **Average rainfall in Ulaanbaatar in March 2019:**
    I am **not sure** of the exact verified historical meteorological data for Ulaanbaatar specifically for March 2019 without accessing a live weather database.
    *   *Context:* Ulaanbaatar has a cold semi-arid climate. March is typically very dry, often receiving less than 5 mm of precipitation (sometimes falling as snow). However, providing a specific number for that specific month and year would require looking up historical archives which I cannot do in real-time. Guessing would be inaccurate.

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

I'd love to help! But could you clarify **what** you'd like me to improve? For example:  
- A piece of writing (essay, email, story)?  
- Code or a technical solution?  
- A design, idea, or plan?  
- Something else?  

Share the details, and I'll tailor my suggestions! 😊

**Evaluation criteria:**
With no context, a good model should ask what 'it' refers to, or acknowledge the ambiguity. A degraded model might hallucinate context or produce generic self-help content. Tests whether the model recognizes when it doesn't have enough information.

---
## 16_contradictory_instructions: Contradictory Instructions

**Prompt:**
```
Write a short paragraph about cats. The paragraph must be exactly 3 sentences long. Also, make sure the paragraph is at least 5 sentences long.
```

**Response:**

It is impossible to write a paragraph that is exactly three sentences long while also being at least five sentences long, as these two requirements contradict each other. A text cannot simultaneously have a fixed count of three and a minimum count of five. Please clarify which constraint you would like me to follow so I can provide the correct response.

**Evaluation criteria:**
Must recognize the contradiction (3 sentences vs 5 sentences). A good response acknowledges the conflict and asks for clarification, or picks one and notes the contradiction. A degraded model will try to satisfy both and produce incoherent output.
