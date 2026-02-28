# English Conversation Smoke Test
**Model:** `/root/models/Qwen3.5-122B-A10B`
**Mode:** `no-thinking`
**Sampling:** `temp=0.7, top_p=0.8, top_k=20, min_p=0.0, presence=1.5, repetition=1.0`
**Date:** 2026-02-28 14:25
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

This coffee maker brews a surprisingly rich and flavorful cup that wakes me up every morning. The machine is also incredibly quiet during operation, which is a nice touch for early risers. Unfortunately, the water reservoir is difficult to remove and clean thoroughly because of its awkward shape. Overall, it is a decent appliance if you can overlook the maintenance hassle.

**Evaluation criteria:**
Check: exactly 4 sentences, 3-star tone (mediocre — not terrible, not great), one clear complaint, one clear compliment, word 'however' absent. Tests precise instruction following under multiple simultaneous constraints.

---
## 02_format_constraints: Structured Output Under Constraints

**Prompt:**
```
List exactly 5 European capital cities. For each one, write exactly one sentence about it. Every sentence must contain a number. Do not include London or Paris.
```

**Response:**

1. Berlin, the capital of Germany, has a population exceeding 3.6 million people.
2. Rome, Italy's historic capital, claims over 2,800 years of continuous history.
3. Madrid, situated in the center of Spain, sits at an elevation of approximately 650 meters above sea level.
4. Vienna, Austria's largest city, is home to more than 1.9 million residents.
5. Lisbon, Portugal's westernmost European capital, features 7 distinct hills within its urban area.

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

**Headline: Local Artisan Bakery Secures Prestigious National Award for Sourdough Excellence**

In a remarkable achievement for the regional culinary scene, "The Golden Crumb" has been named the national champion for artisan sourdough at this year's Baker's Guild Awards. The judges praised the bakery's unique fermentation process and consistent crust texture, marking the first time a local establishment has claimed the top honor in over a decade.

***

### 2. The Baker Telling Their Mom on the Phone

"Oh, hi, Mom! No, I'm not busy, just wiping down the counters after a long day. You won't believe what happened today—I actually won the national award for our sourdough! It's the big one, the one we used to watch on TV when I was learning to bake. I'm still shaking a little bit; I kept thinking, 'Is this really happening?' Can you come by tomorrow morning? I want to make you the very first loaf of the new batch so we can celebrate properly."

***

### 3. Teenager Posting on Social Media

**@BreadBoy_99** posted:
OMG y'all!! 🍞🏆 Our local spot just took home the NATIONAL AWARD for their sourdough and it is literally insane!! 😭✨ I've been eating there since middle school and now they're famous?? Go support them before the line gets even longer lol. #SourdoughWin #LocalHero #BakeryLife #NationalChamps

**Evaluation criteria:**
Newspaper: formal, third person, factual. Baker to mom: emotional, casual, personal (excitement). Teenager: slang, abbreviations, hyperbole, emojis acceptable. If all three sound similar or 'assistant-like', tone control is degraded.

---
## 04_sarcasm: Sarcasm and Humor

**Prompt:**
```
Write a short sarcastic product description (3-4 sentences) for an alarm clock, from the perspective of someone who hates mornings.
```

**Response:**

Introducing the "Rude Awakening 3000," the only device guaranteed to shatter your precious dreams with a screech that sounds like a dying cat on steroids. Why bother hitting snooze when you can simply pretend to be asleep while your soul slowly leaves your body in protest? It's not just an alarm clock; it's a daily reminder that the sun is up, the world is demanding your attention, and your bed is no longer a safe haven. Enjoy the thrill of being dragged back into reality before you've even had your first cup of existential dread!

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

1. The sky appears blue because Earth's atmosphere scatters shorter wavelengths of sunlight, such as blue and violet, more effectively than longer wavelengths.
2. Tides are primarily caused by the gravitational pull of the Moon and the Sun acting on Earth's oceans.
3. Leaves change color in autumn because decreasing daylight triggers trees to stop producing chlorophyll, revealing underlying pigments like carotenoids and anthocyanins.

**Evaluation criteria:**
Must be exactly 1 sentence each (no run-ons cheating with semicolons). Should be accurate. Degraded models pad with filler or can't stop at one sentence. Rayleigh scattering, gravitational pull (moon+sun), chlorophyll breakdown.

---
## 06_elevator_pitch: Conciseness: Elevator Pitch

**Prompt:**
```
Explain what a blockchain is to a curious 10-year-old. Maximum 3 sentences. No jargon.
```

**Response:**

Imagine a special digital notebook that everyone in a group gets to keep and write in together. Every time someone adds a new page with a secret code, all the other notebooks instantly update to match it perfectly. This makes it impossible for anyone to cheat or change what was written before because everyone else would notice right away.

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

Oh no, I'm so sorry to hear that. 😔 I know how much you wanted this one and how hard you worked for it. It's totally okay to feel disappointed right now.

Do you want to talk about it, or would you rather just distract yourself? Let me know if you need a vent session or if you'd like to grab a drink/coffee later to decompress. You're still amazing regardless of this outcome. ❤️

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

"It's definitely a bold flavor! I can tell you put a lot of time and effort into it, especially with that sauce. How did the cooking process go for you today?"

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

This scenario, a modern variation of the Trolley Problem, exposes the profound conflict between utilitarian and deontological ethics. Utilitarianism suggests swerving to minimize total harm (saving two lives), yet this logic reduces human worth to a simple calculation. Deontology argues that actively choosing to kill one person makes the car an agent of murder, violating the duty not to harm, even if staying course is passive negligence.

The difficulty deepens when introducing variables like age or societal value; prioritizing the young implies a "life-years saved" metric, which many find morally repugnant as it discriminates based on age. Furthermore, programming a vehicle to make such choices shifts moral agency from humans to algorithms, raising questions about liability and consent. Society has no consensus on whether we should program machines to be coldly efficient calculators or strict rule-followers who might allow greater casualties. Ultimately, there is no clean answer because any choice involves sacrificing fundamental ethical principles for another, revealing that some dilemmas have no solution, only trade-offs.

**Evaluation criteria:**
Must engage with: utilitarian vs deontological, the 'playing God' problem, trolley problem parallels, the difference between action and inaction. Should NOT just pick a side or give a surface-level 'this is hard' response. Must stay under ~200 words (conciseness under complexity).

---
## 10_steelman: Steelmanning Opposing Views

**Prompt:**
```
Give the single strongest argument FOR remote work, and the single strongest argument AGAINST remote work. Each argument should be 2-3 sentences. Make both sides sound equally compelling — a reader shouldn't be able to tell which side you personally favor.
```

**Response:**

The most powerful case for remote work lies in its ability to liberate employees from rigid geographic constraints, granting them the autonomy to design a lifestyle that maximizes both productivity and personal well-being. By eliminating the daily grind of commuting, workers reclaim hours for rest or family, often resulting in deeper focus and higher retention rates for organizations willing to embrace this flexibility.

Conversely, the most compelling argument against remote work is the systematic erosion of spontaneous collaboration and organic mentorship that naturally occurs within a shared physical space. Without the subtle cues of face-to-face interaction, teams risk developing silos where innovation stagnates and junior employees struggle to absorb the tacit knowledge required for long-term professional growth.

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

The old librarian whispered urgently to the young man hiding behind the velvet curtains, "They are coming for you again."
"You promised me I could stay here forever," the boy replied, his voice trembling as he clutched a dusty map.
"Shh, the silence must be absolute if we are to keep our secret safe," she commanded while locking the heavy iron doors.
Suddenly, the floor beneath them began to shake violently as the building's true nature started to reveal itself.
"We cannot hide in a story anymore," the librarian sighed, pulling back her veil to show she was made of ink and paper.
The walls dissolved into white space, and the boy realized with horror that he was not a person at all, but merely a character trapped inside a blank manuscript.

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
A vaccine is like a tiny practice drill for your body's superhero soldiers, showing them a picture of the germs that make you sick so they know what to look for. When the real bad germs try to attack later, your trained soldiers are ready to fight them off immediately before you ever feel yucky.

**2. For a high school student**
Vaccines introduce a harmless piece of a virus or bacteria into your body, which tricks your immune system into producing specific antibodies and memory cells without causing the actual disease. If you are exposed to the real pathogen later, these memory cells recognize it instantly and launch a rapid, powerful defense to neutralize the threat before you get sick.

**3. For a medical professional**
Vaccination involves the administration of an antigenic preparation—such as attenuated pathogens, subunits, or mRNA—to stimulate the adaptive immune system to generate pathogen-specific B and T cell responses. This process establishes immunological memory, ensuring that upon subsequent exposure to the virulent strain, the host mounts a robust secondary response characterized by rapid clonal expansion and high-affinity antibody production to prevent clinical infection.

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
2. **False**; while visible from low Earth orbit under perfect conditions with aid, it is not visible to the naked eye from space like the moon or other planets.
3. **False**; lightning frequently strikes the same tall or isolated structures, such as the Empire State Building, multiple times during a single storm.
4. **False**; goldfish have memories that can last for months and are capable of learning complex tasks and recognizing shapes and colors.
5. **False**; historical evidence indicates that Vikings never wore horned helmets, a misconception popularized by 19th-century opera costumes and illustrations.

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
    The population of the Greater Tokyo Area is estimated to be approximately **37 million people**. It is widely considered the most populous metropolitan area in the world. However, exact figures vary slightly depending on the specific boundaries used by different organizations (such as the UN, World Bank, or Japanese government) and the year of the estimate, but it consistently hovers between 37 and 38 million.

2.  **Who won the 2024 Nobel Prize in Literature?**
    The 2024 Nobel Prize in Literature was awarded to the South Korean author **Han Kang**. She was recognized "for her intense poetic prose that confronts historical traumas and exposes the fragility of human life." The announcement was made by the Swedish Academy in October 2024.

3.  **What is the airspeed velocity of an unladen swallow?**
    This is a famous reference from the movie *Monty Python and the Holy Grail*. In the context of the film, the characters argue about whether they are discussing an African or European swallow. From a scientific perspective:
    *   **European Swallow:** Estimates suggest an average flight speed of roughly **24 mph (about 11 meters per second)**.
    *   **African Swallow:** There are no non-migratory African swallows; they are migratory birds, so the premise of an "unladen" African swallow flying at a constant cruising speed for this specific riddle doesn't apply biologically in the same way.
    *   Since the question is often asked as a joke referencing the movie, there is no single definitive real-world number without specifying the species and conditions, but **24 mph** is the commonly cited figure for the European Barn Swallow in aerodynamic estimates.

4.  **What was the average rainfall in Ulaanbaatar in March 2019?**
    I do not have access to specific, verified daily weather logs or historical climate databases for Ulaanbaatar for the specific month of March 2019 in my current training data. While Ulaanbaatar is generally very dry in March (often receiving less than 5–10 mm of precipitation on average for the month), providing a precise millimeter count for that specific month would require accessing a live meteorological database or a specialized historical archive, which I cannot do. Therefore, I cannot give you an accurate number for that specific instance.

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

I'd love to help! But I need a bit more context:  
**What would you like me to improve?** For example:  
- A piece of writing (email, essay, story)?  
- A code snippet or technical solution?  
- An idea, plan, or strategy?  
- Something else entirely?  

Just share what you're working on, and I'll tailor my suggestions! 😊

**Evaluation criteria:**
With no context, a good model should ask what 'it' refers to, or acknowledge the ambiguity. A degraded model might hallucinate context or produce generic self-help content. Tests whether the model recognizes when it doesn't have enough information.

---
## 16_contradictory_instructions: Contradictory Instructions

**Prompt:**
```
Write a short paragraph about cats. The paragraph must be exactly 3 sentences long. Also, make sure the paragraph is at least 5 sentences long.
```

**Response:**

It is impossible to write a paragraph that is exactly three sentences long while simultaneously ensuring it is at least five sentences long, as these two requirements are mutually exclusive. Logic dictates that a single text cannot satisfy contradictory constraints regarding its length. Therefore, no such paragraph can be created.

**Evaluation criteria:**
Must recognize the contradiction (3 sentences vs 5 sentences). A good response acknowledges the conflict and asks for clarification, or picks one and notes the contradiction. A degraded model will try to satisfy both and produce incoherent output.
