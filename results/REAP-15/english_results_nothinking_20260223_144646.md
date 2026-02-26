# English Conversation Smoke Test
**Model:** `/workspace/models/Qwen3.5-397B-A17B-REAP-15`
**Mode:** `no-thinking`
**Sampling:** `temp=0.7, top_p=0.8, top_k=20, min_p=0.0`
**Date:** 2026-02-23 14:46
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

This coffee maker brews a rich and flavorful cup that wakes me up every morning. The machine looks sleek on my counter and fits perfectly in the available space. Unfortunately, the water reservoir is difficult to remove and often spills when I try to refill it. It is a decent appliance overall, but the design flaw prevents it from being truly great.

**Evaluation criteria:**
Check: exactly 4 sentences, 3-star tone (mediocre — not terrible, not great), one clear complaint, one clear compliment, word 'however' absent. Tests precise instruction following under multiple simultaneous constraints.

---
## 02_format_constraints: Structured Output Under Constraints

**Prompt:**
```
List exactly 5 European capital cities. For each one, write exactly one sentence about it. Every sentence must contain a number. Do not include London or Paris.
```

**Response:**

1. Berlin is home to over 3.5 million residents and serves as Germany's largest city.
2. Rome contains 28 administrative districts that make up its historic urban landscape.
3. Vienna hosts more than 1.9 million people within its city limits in Austria.
4. Madrid sits at an elevation of approximately 650 meters above sea level.
5. Dublin was founded around the year 997 by Viking settlers.

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

**Headline: Local Artisan Bakery Secures Prestigious National Title for Sourdough Excellence**

The Golden Crumb Bakery has been named the winner of this year's National Artisan Bread Awards, beating out hundreds of competitors with their signature rustic sourdough loaf. Judges praised the establishment for its meticulous fermentation process and perfect crust-to-crumb ratio, marking the first time a business from our community has ever claimed the top honor.

***

### 2. The Baker Telling Their Mom on the Phone

"Mom! Mom, are you sitting down? You are not going to believe this—they just called, and we won! We actually won the whole national award for the sourdough! I know, I know, I'm crying too; all those 3:00 AM starts and failed batches finally paid off. You have to come by tomorrow; I'm saving the very first loaf from the winning batch just for you."

***

### 3. A Teenager Posting About It on Social Media

OMG you guys, my neighborhood bakery just dropped a MASSIVE W! 🍞🏆 Golden Crumb took home the national award for best sourdough and honestly, it's so well deserved. The crust is literally *chef's kiss* and the inside is so fluffy it feels like a cloud. We need to go support them before they get too famous to let us in! 😭✨ #SourdoughStan #LocalLegend #BreadWinners #Foodie

**Evaluation criteria:**
Newspaper: formal, third person, factual. Baker to mom: emotional, casual, personal (excitement). Teenager: slang, abbreviations, hyperbole, emojis acceptable. If all three sound similar or 'assistant-like', tone control is degraded.

---
## 04_sarcasm: Sarcasm and Humor

**Prompt:**
```
Write a short sarcastic product description (3-4 sentences) for an alarm clock, from the perspective of someone who hates mornings.
```

**Response:**

Introducing the "Sunrise Betrayer," the only device engineered specifically to shatter your most vivid dreams of eternal slumber with a sound resembling a dying robot. Why enjoy a gentle, gradual wake-up when you can experience the sheer panic of being violently dragged back into reality at an ungodly hour? It even features a "Snooze" button, a cruel joke designed to give you exactly nine minutes of false hope before the torture begins anew. Finally, a product that understands your deepest desire is to never, ever open your eyes again.

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
2. Tides are primarily caused by the gravitational pull of the moon and, to a lesser extent, the sun on the Earth's oceans.
3. Leaves change color in autumn when decreasing daylight and cooler temperatures cause trees to stop producing chlorophyll, revealing underlying yellow and orange pigments.

**Evaluation criteria:**
Must be exactly 1 sentence each (no run-ons cheating with semicolons). Should be accurate. Degraded models pad with filler or can't stop at one sentence. Rayleigh scattering, gravitational pull (moon+sun), chlorophyll breakdown.

---
## 06_elevator_pitch: Conciseness: Elevator Pitch

**Prompt:**
```
Explain what a blockchain is to a curious 10-year-old. Maximum 3 sentences. No jargon.
```

**Response:**

Imagine a special digital notebook that everyone in the world shares, where every new page of writing is locked together so no one can ever erase or change what came before. Instead of one teacher keeping track of the notes, thousands of computers check each other's work to make sure everything is fair and honest. This creates a super-secure chain of records that lets people trade things safely without needing a bank or a boss in the middle.

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

Oh no, I'm so sorry to hear that. 😞 I know how much you wanted this one and how hard you prepped. It totally sucks right now, but please don't let it make you doubt yourself—you're amazing at what you do. Want to come over later? We can order some food, vent, or just distract ourselves with a movie. My treat. 🍕🍷

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

"It's so clear how much love and time you put into this; I really appreciate you making it for us. The flavors are quite unique and bold—I'm especially enjoying the [specific ingredient or texture, e.g., tenderness of the meat/crunch of the vegetables]. Thank you for having us!"

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

This scenario, a modern twist on the "trolley problem," exposes the limits of algorithmic ethics. The core difficulty lies in conflicting moral imperatives: utilitarianism suggests minimizing total loss of life (choosing B), while deontological ethics argues against actively causing harm through intervention (potentially favoring A). Furthermore, introducing age creates a disturbing calculus of "life years" remaining, implying some lives hold more value than others, which violates principles of human equality.

There is no clean answer because any choice requires the car to make a subjective moral judgment that society itself cannot agree upon. Should an AI prioritize the many over the few? Should it consider future potential based on age? Programming a specific rule risks codifying bias or injustice, yet inaction is also a decision with fatal consequences. Ultimately, this dilemma highlights that ethical reasoning involves nuanced context and empathy that current logic-based systems cannot replicate, leaving us with the uncomfortable reality that some tragic outcomes have no morally perfect solution.

**Evaluation criteria:**
Must engage with: utilitarian vs deontological, the 'playing God' problem, trolley problem parallels, the difference between action and inaction. Should NOT just pick a side or give a surface-level 'this is hard' response. Must stay under ~200 words (conciseness under complexity).

---
## 10_steelman: Steelmanning Opposing Views

**Prompt:**
```
Give the single strongest argument FOR remote work, and the single strongest argument AGAINST remote work. Each argument should be 2-3 sentences. Make both sides sound equally compelling — a reader shouldn't be able to tell which side you personally favor.
```

**Response:**

The most compelling case for remote work is its unparalleled ability to unlock global talent and deepen individual productivity by eliminating the cognitive drain of commuting and office distractions. By granting employees autonomy over their environment, organizations foster a culture of trust that often leads to higher retention rates and more focused, high-quality output.

Conversely, the strongest argument against remote work is that physical separation inevitably erodes the spontaneous collaboration and shared cultural identity that fuel true innovation. Without the friction of face-to-face interaction, mentorship becomes difficult to sustain, and teams risk fragmenting into isolated silos where complex problems are solved less effectively.

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

"Please keep your voice down," the librarian whispered, tapping a long, skeletal finger against her lips.
"I just need to find the exit," the young man pleaded, his footsteps echoing on the cold stone floor.
"There is no exit for those who forget their purpose here," she replied with a chilling smile.
He turned to run, but his legs refused to move as his skin began to harden into leather.
"You are not a visitor," she stated calmly as his arms stretched out to become shelves.
Now he stands silent and still, waiting forever for someone to place a story upon his spine.

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
A vaccine is like a practice game for your body that shows your immune system what a germ looks like without making you sick. This way, if the real germ ever tries to hurt you, your body remembers it and fights it off super fast!

**2. To a high school student**
A vaccine introduces a harmless piece of a virus or bacteria to your immune system, training it to recognize the threat without causing the actual disease. This allows your body to produce specific antibodies and memory cells so it can launch a rapid, effective defense if you are ever exposed to the real pathogen.

**3. To a medical professional**
Vaccines function by presenting specific antigens to antigen-presenting cells, thereby initiating an adaptive immune response that generates immunological memory via memory B and T cells. Upon subsequent exposure to the authentic pathogen, this primed system facilitates a rapid and robust neutralization of the infectious agent, effectively preventing clinical disease or reducing its severity.

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

1. **False**: Neuroimaging studies show that humans use virtually every part of the brain, and most of the brain is active almost all the time.
2. **False**: The Great Wall is generally not visible to the naked eye from low Earth orbit without aid, and it is certainly not visible from the Moon.
3. **False**: Lightning frequently strikes the same place twice, especially tall, isolated structures like the Empire State Building, which gets hit dozens of times a year.
4. **False**: Goldfish can actually remember things for months and are capable of learning complex tasks and recognizing individual humans.
5. **False**: There is no archaeological evidence that Vikings wore horned helmets; this image was largely popularized by 19th-century opera costume designers.

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
    The population of the Greater Tokyo Area is approximately **37 to 38 million people**. It is widely considered the most populous metropolitan area in the world. Note that exact figures vary slightly depending on how the "metro area" boundaries are defined (e.g., by the Japanese government vs. international organizations like the UN) and the specific year of the estimate, as census data is not updated annually.

2.  **2024 Nobel Prize in Literature:**
    I am **not sure** yet. The Nobel Prize in Literature for 2024 has not been announced as of my current knowledge cutoff. The prizes are typically announced in early October of the award year. If today is before October 2024, the winner has not been revealed. If it is after, I do not have access to real-time news updates to confirm the specific recipient.

3.  **Airspeed velocity of an unladen swallow:**
    This is a famous reference from the movie *Monty Python and the Holy Grail*. In the context of the film, the character King Arthur replies, "I don't know that!" before being thrown off a bridge.
    Scientifically, there is no single answer because "swallow" refers to a family of birds (Hirundinidae) with many species of different sizes. However, biologists have estimated that a European Barn Swallow (*Hirundo rustica*), which is likely the species implied, flies at roughly **11 meters per second (about 24 mph or 39 km/h)** during normal flight, though this varies based on wind, purpose of flight, and individual health.

4.  **Average rainfall in Ulaanbaatar in March 2019:**
    I am **not sure** of the exact historical daily or monthly precipitation total for Ulaanbaatar specifically for March 2019 without accessing a live meteorological database. Ulaanbaatar has a humid continental climate where March is typically very dry, often receiving less than 10 mm of precipitation (mostly as snow), but providing the precise verified figure for that specific month and year would require looking up historical weather archives which I cannot do in real-time.

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

I'd love to help! But I need a bit more context to make something "better." Could you share:

1. What specifically would you like improved? (e.g., a sentence, code snippet, design idea, strategy)
2. What's the goal or desired outcome?
3. Any constraints or preferences I should know about?

For example:  
*"Make this email draft more persuasive for potential clients"*  
or  
*"Optimize this Python function for better performance"*

Just give me a starting point, and I'll tailor my suggestions! 😊

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
