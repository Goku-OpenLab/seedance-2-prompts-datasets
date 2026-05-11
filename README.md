[English](./README.MD) | [简体中文](./README_zh.md)

# 🎞️ Seedance-2-prompts-datasets

[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) [![Dataset Size](https://img.shields.io/badge/Size-12GB%2B-blue)](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets) [![Format](https://img.shields.io/badge/Format-JSONL%20%2F%20MP4-green)](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets)

> 🎞️ The ultimate Seedance-2 video prompt dataset (12GB+). 2000+ video generation prompts with full metadata and preview frames. Truly open source: No login, no ads, no redirection. Just pure data for AI video creators.

This project is a massive collection of prompts used for Bytedance's Seedance 2.0 and the resulting generated videos. The entire dataset exceeds **12GB** and contains **2000+ videos**, all structured into a comprehensive dataset.

Due to GitHub's limitations with large file storage, the full dataset is hosted on Hugging Face. The Hugging Face repository contains the generated **videos (.mp4)**, **cover images (.jpg)**, and a highly structured **.jsonl file** that holds all prompt metadata.

**Download the full dataset here:**  
[https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets)

![huggingface](img/huggingface.jpg)

## 🌐 Online Viewer
No login required, lighting-fast response.  
👉 **[View Online](https://prompthub.gokuscraper.com/)**

![website](img/website.jpg)

## 📖 Introduction
Launched by **GokuOpenLab**, **seedance-2-prompts-datasets** is a prompt data infrastructure project created for developers and researchers.

In the current AI ecosystem, prompts are the new "productivity interface". However, reality reveals several issues:
- Prompt data is highly fragmented.
- There is a lack of unified structural standards.
- Retrieving and reusing prompts is difficult.
- They are not suitable for engineering and systematic utilization.

This project's goal is NOT just to "display prompts", but to:
> Transform internet prompts into **structured, calculable, and redistributable data assets.**

## 🚫 Our Manifesto
Before building this project, we analyzed the absolute chaos in the open-source community and decided to firmly say "NO":
- **NO to black-box prompt distribution:** Closed systems that don't provide structured data and forbid secondary usage.
- **NO to traffic-driven pseudo-open source:** Repositories using GitHub as clickbait while hiding core data behind private platforms or logins.
- **NO to uncomputable data formats:** Simple text displays that cannot be parsed by programs or used for model training.

## ✨ Why Goku Prompt Hub?

### 1️⃣ 100% Open Data
All collected data is fully accessible. There are no "preview versions" or locked contents.
- Direct download via Hugging Face.
- Seamless online browsing.

### 2️⃣ Structured Data System (.jsonl)
Our prompt data is stored in a structured JSONL format. Every single prompt undergoes unified parsing and standardization, connecting the video assets to their exact configurations.

*Example entry from our JSONL records:*
```json
{
  "version": "1.0",
  "id": "SD2_00133",
  "category": "Entertainment",
  "is_featured": false,
  "date": "2026-04-28",
  "slug": "glacial-tiger-vs-frost-serpent",
  "model_info": { "name": "seedance", "version": "2.0" },
  "raw_p": "Environment: A colossal glacial canyon under pale blue twilight...",
  "media": {
    "v": "seedance-2/videos/SD2_00133.mp4",
    "c": "seedance-2/covers/SD2_00133.jpg"
  },
  "spec": { "width": 1280, "height": 720, "ratio": 1.78, "duration": 15.12, "safety_rating": "Safe for Work" },
  "i18n": {
    "zh": {
      "t": "冰谷虎蛇战",
      "p": "环境：一座巨大的冰川峡谷，笼罩在淡蓝色的暮光之下...",
      "tags": ["冰川峡谷", "冰虎", "霜蛇"]
    },
    "en": {
      "t": "Glacial Tiger vs Frost Serpent",
      "p": "Environment: A colossal glacial canyon under pale blue twilight...",
      "tags": ["ice canyon", "frozen battle", "cinematic"]
    }
  },
  "platform": "x",
  "sourceLink": "https://x.com/LudovicCreator/status/2045419585491317186",
  "file_name": "seedance-2/videos/SD2_00133.mp4"
}
```

### 3️⃣ Developer Friendly
- **Unified JSON Schema**: JSONL perfectly formats logs into lines of JSON objects.
- **Database Ready**: Seamlessly import into SQLite, Supabase, or your local AI toolchains.
- **One-line Python Integration**: Load the dataset directly into a Pandas DataFrame in 1 second:

```python
import pandas as pd

# Load Goku's dataset instantly!
url = "https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/raw/main/metadata.jsonl"
df = pd.read_json(url, lines=True)
print(f"✅ Loaded {len(df)} structured video prompts!")
```


### 4️⃣ Open License (CC BY 4.0)
All data operates under the **CC BY 4.0 License**:
- ✔ Free to use
- ✔ Commercial use allowed
- ✔ Modification allowed
- ✔ Redistribution allowed
- ❗ **Attribute original source required**

## 📊 Data Overview
- **Total Prompts:** 2110+
- **Languages:** English / Chinese
- **Target Models / Engines:** Bytedance Seedance 2.0, Midjourney, Stable Diffusion, DALL·E 3, Flux, etc.
- **Update Frequency:** Continuous automated syncs.

## 🛡️ Disclaimer
The prompts and metadata in this repository are sourced from public internet communities and are strictly intended for learning, research, and data structuring purposes.  
The copyright of the original generated content belongs to the original creators. This project only provides data curation, structured processing, classification, and indexing; it does not claim copyright over the original context.

If you are a copyright holder and believe there is an issue, please contact us via GitHub Issues or email. This project is not affiliated with Bytedance, OpenAI, Google, Anthropic, Midjourney, or any other specific model/platform.

## 🤝 Contributing
Welcome to Goku Prompt Hub!
- **Submit an Issue:** Report bad quality or broken prompts.
- **Submit a PR:** Contribute your high-quality prompt data.
- **Star the repo:** Show your support and push prompt data infrastructure forward!

---
*Happy Prompting!*




<!-- STATS_START -->

## 📊 Statistics
- Total Prompts: **2735**
- Updated Today (UTC 2026-05-11): **243**

## 🎬 Today's Updates
### 🎬 Defense to Dominance: Basketball Storyboard
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02754.jpg" width="480" alt="SD2_02754"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/defense-to-dominance-basketball-storyboard-SD2_02754">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a high-quality 4K cinematic basketball storyboard showing a full sequence from defense to a powerful score, using dynamic arena lighting, dramatic crowd atmosphere, and professional sports broadcast style. The scene begins with an intense half-court moment where a defender performs a clean steal or block, the ball sharply deflected as sweat and motion particles are captured in slow motion. Transition immediately into a fast break: the player recovers the ball, dribbles with speed and control, accelerating past opponents with quick crossovers and footwork. Show close-ups of sneakers gripping the court, the ball bouncing with precise rhythm, and focused facial expressions, mixed with wide shots of the court opening up. Add a key assist moment where the ball is passed sharply between defenders, followed by a sprint toward the basket with the crowd rising in anticipation. Build tension with a slow-motion approach to the paint, then a powerful finish—either a high-impact dunk, smooth layup, or clean jump shot. Show the ball swishing through the net or the rim rattling with force, including defender and crowd reactions. Integrate realistic background audio throughout: squeaking sneakers on hardwood, echoing dribbles, player shouts, referee whistle, crowd murmurs building into loud cheers, commentator-style distant hype, and arena reverb that intensifies during key moments like the steal, fast break, and final shot. End with an emotional celebration: the scorer running back, flexing, or raising arms as teammates join, arena lights glowing and crowd erupting. Use varied camera angles (wide, tracking, close-up, POV, slow motion), strong motion blur, and realistic physics (ball bounce, shoe friction, body movement), emphasizing the transition from defensive control to offensive dominance and victory.
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.07s`

---

### 🎬 LUMIÉRA Seoul Glass Glow Lip Elixir Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02753.jpg" width="480" alt="SD2_02753"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/lumiera-seoul-glass-glow-lip-elixir-ad-SD2_02753">🌐 Watch Online</a>

#### 📝 Prompt
```
Base Setup: “Ultra-realistic fast-paced TikTok-style beauty ad inside a luxury cosmetics store. Bright lighting, glossy reflections, trendy aesthetic. A stylish Korean girl with glowing skin and modern outfit. Fast cuts, dynamic camera movement, viral editing style, 4K.” ⏱️ 0:00 – 0:02 (Hook – Scroll Stopper) – Quick zoom-in on girl entering store – Flash cuts of colorful makeup shelves 🎙️ Text on screen: “WAIT—this changed everything 💄✨” 🎧 Sound: trending upbeat TikTok beat drop ⏱️ 0:02 – 0:05 (Fast Shopping Montage) – Rapid cuts: • Grabbing products • Tossing items into cart • Close-up hand swipes across shelves 🎙️ Text: “Trying EVERYTHING…” ⏱️ 0:05 – 0:07 (Discovery Moment) – Sudden slow-motion contrast – Spotlight on lip gloss – Product label visible: “LUMIÉRA Seoul – Glass Glow Lip Elixir” 👩 Girl (whisper, excited): “Wait… this one?” ⏱️ 0:07 – 0:10 (Transformation Apply) – Quick mirror transition – Fast close-up of lip gloss applying – Smooth glossy shine appears instantly 🎙️ Text: “OMG 😳” 👩 Girl: “Okay… WOW.” ⏱️ 0:10 – 0:13 (Results + Beauty Shots) – Rapid aesthetic cuts: • Lips glowing • Hair flip • Confident look 🎙️ Text: “Glass lips in seconds ✨” ⏱️ 0:13 – 0:15 (Product Close + CTA) – Fast zoom into product – Clean luxury product shot 🎙️ Voiceover: “LUMIÉRA Seoul – Glass Glow Lip Elixir.” 🎙️ Text on screen: “Get yours NOW 🔥” – Beat drop ends Editing Style: Fast cuts, jump transitions, speed ramps, zoom-ins, flash transitions Camera Style: Handheld + quick zooms + macro beauty shots Sound: Trending TikTok audio, beat drops synced with cuts Mood & Style: Trendy, addictive, high-energy, viral beauty ad Modern Gen-Z aesthetic, ultra-polished, 4K
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.2s`

---

### 🎬 Golden Lightning Impact Strike
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02752.jpg" width="480" alt="SD2_02752"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/golden-lightning-impact-strike-SD2_02752">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-realistic cinematic action, grounded physics, IMAX film look, 4K–8K HDR, high contrast, deep shadows, natural skin texture, subtle film grain, anamorphic lens 35mm (f/2.8). No over-glow, no excessive aura. Energy as air pressure distortion + thin golden electricity (sharp, intermittent). Camera: dynamic handheld, rapid tracking, whip pan, impact shake, natural motion blur. SCENE (CONTINUOUS 10 SECONDS): A slim-built man wearing a white tank top and black pants stands on cracked ground. 0–2s: Fast handheld push-in. Body tenses, veins visible, heavy breathing. Small golden electric sparks appear on hands and shoulders. Dust begins to vibrate. 2–4s (FAST TRANSFORMATION): Muscles grow into an athletic build gradually (no instant cut). Hair rises and turns golden. Ground cracks expand radially, small rocks lift and scatter. Subtle air distortion. A short mini shockwave pushes dust outward. Camera: quick orbit + light shake. 4–6s (TARGET LOCK): Reveal a humanoid tentacled monster in front. Tentacles move aggressively with heavy weight. Character condenses power, leans slightly forward, then explodes into a high-speed sprint (realistic dash blur). Camera: extreme whip pan, almost losing subject. 6–8s (IMPACT STRIKE): Character appears instantly in front of the monster. One powerful punch to torso/head. Effects: heavy impact (flesh + mass), brief golden electricity burst at contact, air pressure hit, dust explosion from feet. Camera: impact zoom + violent shake + slight slow motion on contact frame. 8–10s (LAUNCH → MOUNTAIN CRASH): Monster is launched far, leaving a dust trail. Cut to wide shot: monster crashes into a mountainside, rocks collapse, large debris falls (realistic rockfall, no energy explosion). Cut back: character stands still, athletic body, golden hair. Subtle residual electricity flickers. Dust settles. Silence after impact.
```

#### 📌 Details
- Ratio: `2.34` | Duration: `15.13s`

---

### 🎬 Fierce Warrior Unleashes Energy Arrow
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02751.jpg" width="480" alt="SD2_02751"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/fierce-warrior-unleashes-energy-arrow-SD2_02751">🌐 Watch Online</a>

#### 📝 Prompt
```
A cinematic, fast-paced action sequence starting with a close-up of a fierce female warrior with dark hair and silver metallic facial markings, aiming a glowing blue energy bow and arrow. Transition to an extreme close-up of her brown eye as a futuristic orange digital targeting reticle activates over her pupil. The camera cuts to an over-the-shoulder wide shot showing her standing on a high rocky cliff, overlooking a sunlit desert canyon where an army of dark, monstrous creatures is marching. She releases the glowing blue arrow, which splits into multiple brilliant energy beams mid-air. The camera swiftly tracks the main blue beam as it speeds down the canyon towards the monsters, culminating in a massive, explosive impact of thick dust and debris among the creatures.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.23s`

---

### 🎬 Japanese Women's WWE Championship Finale
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02750.jpg" width="480" alt="SD2_02750"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/japanese-women-wwe-championship-finale-SD2_02750">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a hyper-realistic, cinematic 15-second continuous sequence depicting a WWE-style championship finale between two highly athletic Japanese female wrestlers in a packed arena. Follow a precise match progression: fatigued staredown → explosive clothesline → submission hold battle → DDT counter → near fall → German suplex → top-rope moonsault finisher → clean three-count → championship celebration with belt, confetti, and corner pyro. Maintain consistent character identity and matching ring attire throughout. Emphasize realistic sweat, impact physics, crowd energy, and dramatic slow motion on key moves. End with a rising crane shot capturing the victor’s pose. Output should feel like a live WWE broadcast—photorealistic, high contrast, 60fps.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Luxury Beauty Cream Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02749.jpg" width="480" alt="SD2_02749"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/luxury-beauty-cream-ad-SD2_02749">🌐 Watch Online</a>

#### 📝 Prompt
```
Seedance 2.0 – 15 Beauty Cream Advertisement Video Prompt Create a 15-second vertical (9:16) ultra-realistic cinematic advertisement video for a beauty cream. Scene: A young woman in a clean, modern vanity or soft studio bathroom setting. The environment is bright, elegant, and minimal with soft pastel tones and a luxury skincare vibe. Style: High-end skincare commercial, ultra-realistic, smooth cinematic lighting, soft focus, premium beauty brand aesthetic. Sequence (quick cuts): 0–4s: Close-up of woman’s clean, glowing skin under soft natural light 4–8s: She gently applies beauty cream on her face with smooth motion 8–12s: Skin appears more radiant and fresh, confident smile in mirror 12–15s: Hero shot of product jar on clean surface with glowing background Voiceover (soft, calming tone): “Reveal your natural glow… with daily care that feels pure and light.” Lighting: Soft diffused white light, gentle highlights on skin, warm and clean tone. Music: Soft relaxing beauty ad music, light piano with airy ambient sounds. Mood: Fresh, elegant, confident, skincare luxury feel. Ending Text (optional): “Glow starts with care.”
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.05s`

---

### 🎬 Grocery Aisle Memories
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02748.jpg" width="480" alt="SD2_02748"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/grocery-aisle-memories-SD2_02748">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 15-second cinematic short video with a unique emotional storyline. Scene starts inside a softly lit modern grocery store. A young woman (mid-20s, natural look, casual outfit) walks slowly through the aisles, picking up everyday items like milk, bread, and fruits. Camera follows her in smooth tracking shots, focusing on small details—her hands brushing over products, her thoughtful expressions. Mid-scene (5–10 sec): She pauses while holding a chocolate bar, a subtle flashback overlay appears—quick soft-focus memory of her laughing with someone special (suggesting nostalgia or a past relationship). Final scene (10–15 sec): She gently puts the chocolate back, gives a soft, emotional smile, and walks toward the checkout. Camera lingers as she exits the store alone, but calm and stronger. Style: cinematic, shallow depth of field, warm lighting, soft background music, emotional tone Camera: slow motion, close-ups + smooth tracking shots Mood: nostalgic, peaceful, slightly emotional Quality: ultra-realistic, 4K, film-like color grading
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

### 🎬 Royal Princess Ballroom Dance Sequence
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02747.jpg" width="480" alt="SD2_02747"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/royal-princess-ballroom-dance-sequence-SD2_02747">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a cinematic fantasy movie sequence based on this 16-panel storyboard poster. A young royal princess is performing an elegant ballroom dance inside a luxurious European palace ballroom at night. Warm golden chandelier light and candlelight glow fill the room, with soft moonlight coming through tall arched windows. The princess wears a royal blue luxury gown with a layered flowing skirt, sparkling embroidery, a crown/tiara, and elegant jewelry. Animate the dance as one continuous sequence: she enters gracefully, opens her arms, begins slow turns, side-steps smoothly, prepares for spinning, then performs faster spins with her skirt expanding dramatically, pauses under chandelier light, performs a low curtsy sweep, rises with a back-arch motion, then reaches the climax with a grand whirl spin, slowly recovers, turns toward the moonlit window, gives a storytelling back glance, and finishes with a powerful final freeze pose. Camera style: cinematic tracking shots, smooth slow-motion moments, soft depth of field, realistic fabric physics, natural hair movement, subtle sparkle reflections on jewelry, elegant motion blur during spins.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `9.65s`

---

### 🎬 Neon Heist Chase Escape
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02746.jpg" width="480" alt="SD2_02746"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/neon-heist-chase-escape-SD2_02746">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: Cinematic thriller, handheld camera energy, high contrast lighting, teal-orange grading, shallow depth of field, fast rhythmic cuts, realistic motion blur. 0–2s — The Heist Breaks Loose Interior bank vault corridor. Red alarm lights flashing violently. Security doors slam open. Sirens begin blaring in the distance. Close-up: gloved hand grabbing a duffel bag stuffed with cash. 2–5s — Escape Initiated Masked runner bursts through shattered glass doors. Slow-motion glass fragments flying outward, reflecting neon city lights. Camera shakes slightly as the runner hits the street. 5–8s — Street Chaos Wide shot of a crowded city market street. People scatter in confusion. The runner pushes through pedestrians, weaving fast. Police sirens grow louder, red-blue lights washing over buildings. 8–11s — Chase Intensifies Low-angle tracking shot of the runner sprinting across traffic. Cars brake suddenly. A police vehicle skids into frame. Quick cuts: boots hitting pavement, breathing heavy, cash bag swinging. 11–13s — Near Capture Moment Runner slips through a narrow alley. A hand almost grabs them from behind. Neon signs flicker above, rain starts lightly, adding reflection on wet ground. 13–15s — Escape Beat Cliffhanger Runner leaps over a barrier and disappears into a subway entrance. Camera lingers on flashing sirens flooding the alley, then cuts to black mid-siren peak.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.1s`

---

### 🎬 Gourmet Burger ASMR Slow Motion Hook
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02745.jpg" width="480" alt="SD2_02745"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/gourmet-burger-asmr-slow-motion-hook-SD2_02745">🌐 Watch Online</a>

#### 📝 Prompt
```
0–3s (VIRAL HOOK): Extreme macro close-up of a gourmet cheeseburger being lifted slowly. Melted cheese stretches dramatically between bun and patty—thick, glossy, elastic strands. Juices glisten on the patty, steam rises naturally. Slow-motion effect for maximum satisfaction. First frame is slightly grainy/low-quality, then subtly sharpens (to support your before/after idea). 3–6s: Cut to the influencer holding the burger, shot in natural handheld UGC style (phone camera feel). She reacts with excitement: slight smile, raised eyebrows. Soft dialogue or lip-sync: “Okay… this looks insane.” 6–10s: Handheld vlog-style shot. She takes a big bite—cheese stretches again, sauce slightly drips. Real, unfiltered reaction: eyes widen, she nods, subtle laugh. Natural motion shake for authenticity. 10–13s: Extreme close-up ASMR shots: Crispy toasted bun texture Juicy patty fibers Melted cheese pull + sauce drip Background fully blurred, premium food focus. 13–15s (VIRAL END FRAME): She looks into the camera, smiles confidently, gives a subtle thumbs-up. Freeze frame on the burger with a glowing highlight + slight zoom-in punch. Final frame is ultra-sharp 4K HDR (clear “after” quality moment). 🎥 Visual Style (Enhanced) Hyper-realistic burger textures (juicy patty, molten cheese, glossy bun) UGC handheld authenticity + cinematic polish First 5 sec slightly soft/low quality → transitions into crisp 4K clarity Warm cozy lighting + neon reflections Shallow depth of field, subject isolation Natural motion blur + micro camera shake 🔊 Audio Style Trending TikTok food vlog sound / chill lo-fi beat Strong ASMR layer: bite crunch, sauce drip, cheese stretch Subtle bass hit exactly at first cheese pull (hook moment) Audio clarity improves after 5 seconds (matches video quality jump)
```

#### 📌 Details
- Ratio: `1.78` | Duration: `11.73s`

---

### 🎬 Faceless Mannequins Storyboard Composition
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02744.jpg" width="480" alt="SD2_02744"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/faceless-mannequins-storyboard-composition-SD2_02744">🌐 Watch Online</a>

#### 📝 Prompt
```
Read IMG_1 as the sole main character reference. Read IMG_2 as an abstract storyboard reference. The faceless mannequins in IMG_2 are not characters but symbols indicating position, pose, and composition.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Samurai Duel at Dusk
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02743.jpg" width="480" alt="SD2_02743"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/samurai-duel-at-dusk-SD2_02743">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: Cinematic samurai drama, ultra-realistic, muted color palette, natural dusk lighting, slow-motion emphasis, wind-swept atmosphere, shallow depth of field, minimal dialogue, emotional tension, Kurosawa-inspired framing. 0–3s — Silent Approach Wide establishing shot of a mist-covered field at dusk. Two samurai stand far apart, perfectly still. Tall grass sways in heavy wind. A distant temple silhouette fades into haze. Absolute silence—only wind ambience. 3–6s — The Slow Walk Begins Both samurai begin walking toward each other. Alternating low-angle tracking shots. Close-ups of calm, focused eyes. Subtle hand movement near katana hilt. Controlled breathing, tension building with every step. 6–9s — Rising Tension Camera slowly orbits as distance closes. Fabric and hair ripple in stronger wind. Footsteps sink into wet earth. No music, no dialogue—only rhythmic steps and rising pressure in still air. 9–11s — Final Standoff They stop at blade distance. Extreme close-up on hands tightening around sword handles. A single falling leaf drifts between them in slow motion. Time feels suspended. 11–13s — Draw and Strike Instant cut to ultra-slow motion: both draw katana simultaneously. Sharp metallic ring echoes. One decisive crossing slash mid-air. Sparks and motion blur freeze the impact moment. 13–15s — Aftermath Silence One samurai remains standing. The other collapses out of frame. Wind continues through empty field. Camera holds on stillness, lingering on drifting grass, then fades to black.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 Alien Bus Attack in Rainy Night
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02742.jpg" width="480" alt="SD2_02742"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alien-bus-attack-rainy-night-SD2_02742">🌐 Watch Online</a>

#### 📝 Prompt
```
A packed city bus tears through rainy streets at night. Suddenly the entire floor dents upward beneath passengers’ feet with a metallic BOOM. People scream as scraping sounds race underneath the bus at impossible speed. Sparks blast past the windows. A passenger looks down outside — an alien creature is sprinting upside down beneath the chassis, weaving between axles. The driver slams the brakes. The floor rips open from below as the creature bursts upward into the aisle. Shot 1 (0s–2s) — THE HOOK Inside packed moving bus. The floor suddenly BULGES upward violently beneath standing passengers, throwing people sideways instantly. Metal groans loudly. A second impact hits immediately after. Sparks streak past the windows. Shot 2 (2s–5s) Bus swerves hard through traffic. Passengers scream and grab rails. LOUD metallic scraping races from front to back underneath the vehicle like something huge is crawling at extreme speed below them. The entire bus shakes rhythmically with heavy impacts. Shot 3 (5s–8s) A terrified passenger leans toward the side window. Outside below: an alien creature is hanging upside down beneath the moving bus, sprinting between the axles while gripping metal with elongated limbs. Its glowing eyes snap upward toward the passenger instantly. Shot 4 (8s–11s) Driver slams brakes. Everyone lurches forward violently. The creature SMASHES upward repeatedly from below. Floor panels begin tearing open one by one down the aisle toward camera like a zipper exploding upward. Passengers scramble over seats in panic. Shot 5 (11s–15s) — PAYOFF The floor ERUPTS. The creature launches fully into the aisle in a shower of sparks and twisted metal, grabbing a screaming passenger mid-air. Bus crashes sideways into a divider. Final frame: through the shattered windshield, the bus skids while the creature crawls across the ceiling inside the overturned bus toward camera.
```

#### 📌 Details
- Ratio: `1.0` | Duration: `12.17s`

---

### 🎬 Ancient Forest Apocalyptic Fairy Demon Clash
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02741.jpg" width="480" alt="SD2_02741"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ancient-forest-apocalyptic-fairy-demon-clash-SD2_02741">🌐 Watch Online</a>

#### 📝 Prompt
```
A vast ancient forest, towering trees thousands of years old, their bark carved with glowing runes, mist curling through the roots like living creatures. Dead silence. Then — a crack of golden light splits the sky. Thick storm clouds part and a blinding radiance pours through as thousands of fairies descend in formation, wings shimmering like stained glass catching sunlight, armor forged from moonstone and frozen starlight, spears tipped with pure white flame. They move like a murmuration — fluid, synchronized, devastating. Simultaneously — the forest floor fractures. Deep crimson light bleeds through the cracks as the earth tears itself open. A demon horde erupts upward in a volcanic surge — towering horned beasts, scaled warriors with molten eyes, dark wings like torn leather blocking out what remains of the sky, war cries shaking the ancient trees to their roots. The two forces lock eyes across the forest canopy for one suspended breath — complete silence — then collide with catastrophic force. Light meets shadow. Gold meets red. The ancient trees tremble and splinter. Magic detonates in every direction. The forest floor ignites. The sky tears open further. Camera sweeps wide in a breathtaking arc — the full scale of the collision visible — thousands deep on both sides — an apocalyptic clash that has been building for a thousand years finally unleashed in one single devastating moment. Cinematic. Mythic. Earth-shattering. SCENE BREAKDOWN: TimingScene 10–2sEstablishing wide shot ancient rune-carved forest, dead silence, mist curling through roots 22–4sSky cracks open golden light floods through storm clouds fairy army descends in glowing formation 34–6sClose-up fairy warriors in moonstone armor, shimmering wings, white flame spears, moving in unison 46–8sForest floor fractures crimson light bleeds through demon horde erupts violently from the earth 58–10sClose-up towering horned demons, molten eyes, torn leather wings, war cries shaking the trees 610–12sBoth armies lock eyes across the canopy one suspended heartbeat of pure silence 712–14sCatastrophic collision light meets shadow gold meets red magic detonates in every direction 814–15ssweeping wide arc full scale of both armies clashing forest igniting sky tearing open
```

#### 📌 Details
- Ratio: `0.75` | Duration: `15.21s`

---

### 🎬 Pastel Floral Dress Through Italy
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02740.jpg" width="480" alt="SD2_02740"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pastel-floral-dress-through-italy-SD2_02740">🌐 Watch Online</a>

#### 📝 Prompt
```
0–4s Soft morning light spills over Venice. A young girl steps out of a narrow alley wearing a pastel cotton floral dress, light and breathable, flowing gently with every step. The canals shimmer as gondolas pass quietly in the background. 4–8s She travels through the Italian countryside by train. In her same pastel floral cotton dress, now layered with a light cardigan, she gazes out the window. Rolling hills and vineyards blur into a warm, dreamy landscape. 8–12s Florence welcomes her with golden light. She walks through historic streets in her soft cotton floral dress, pastel tones blending with the city’s earthy architecture. Her outfit moves naturally with the breeze as she pauses in front of the cathedral. 12–16s At sunset in Rome, she stands near ancient ruins, still in her elegant pastel floral dress. The fabric catches the warm orange glow of the sky. She smiles softly as the city lights begin to glow, creating a peaceful cinematic ending.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

<!-- STATS_END -->
