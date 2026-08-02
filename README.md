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
- Total Prompts: **8549**
- Updated Today (UTC 2026-08-02): **26**

## 🎬 Today's Updates
### 🎬 Cyber Idol Duo Live Concert
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11022.jpg" width="480" alt="SD2_11022"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cyber-idol-duo-live-SD2_11022">🌐 Watch Online</a>

#### 📝 Prompt
```
@画像1を二人の人物 strictly references to face, hairstyle, and costume, with long-haired black-haired idols always on the left side of the screen and short-haired brown-haired idols always on the right side. @画像2は一つの巨大サイバーライブ会場を示す環境デザイン資料として参照し, the 2×2 grid and white borders are not displayed within the video. High-definition theatrical anime-style design, transparent cel-look of reference images for characters, a cinematic CG venue with deep cinematic CG, blue, cyan, and purple lasers, audio waveform LEDs, a packed audience, and countless blue glow sticks. 0-1.8s: Starts from the peak of the chorus without any preamble. A super wide-angle front view: the two were already on the center stage, holding microphones and singing and dancing in unison. On the first beat, lasers and spectator glow sticks lit up explosively at once, and cameras rapidly closed in on them [cut] 1.8-3.8s: Low-angle full-body two-shot with powerful symmetrical steps and arm swings synchronized to the beat, black and brown hair, translucent sleeves, skirt, and ribbon on the back sway wildly according to inertia. With every step forward, waves of cyan light spread from the floor. [cut] 3.8-5.9s: Close-up shot of two people from the front, the camera smoothly shifts between them, long black hair and short brown hair alternately singing to the lens, ending with both smiles and winks. No clear lyrics are specified; the natural female duo singing perfectly synchronizes their mouth movements and voices, with each person holding only one microphone. [cut] 5.9-8.0s: In a sideways mid-shot, two people line up and run to the front of the stage, provoking the audience by extending a microphone and a hand. The audience simultaneously raised their glow sticks, and in response to the sound pressure of the cheers, the audio waveform LEDs behind them bounced loudly [cut] 8.0-10.2s: Center full-body shot, two spinning simultaneously with back-to-back. The camera rotates semicircles around the two of them, with cyan and purple glowing lines on their costumes tracing circular light trails, and lasers radiating out [cut] 10.2-12.6s: At an extremely low angle, both jump small at the same time, and at the moment of landing, a huge bluish-purple ring of light spreads from the floor to the audience. The camera tilts up sharply from landing, capturing the smiles of the two holding the microphone high [cut] 12.6-15.0s: The camera smoothly rewinds to show a panoramic view of the massive arena. The two leaned together, stretching their free arms wide toward the audience in a perfectly synchronized final strike. The audio waveforms LED, laser, spark, and glow in the background reach maximum brightness on the final beat, and the original BGM is clearly completed with powerful terminal chords and drum hits, leaving a brief echo of cheers, and maintaining the final pose steadily for the last 0.5 seconds. Music: From the very first 0 seconds, the chorus goes all out, an uplifting original cyber J-POP at about 160 BPM, four-beat sounds, sharp synth arpeggios, thick electro bass, powerful drums, bright female duo singing, audience calls, wide arena reverberation, fully synchronized video movement, lighting, and landing, no fade-in, no quiet introduction. Only the two of them appeared, with faces, hairstyles, costumes, physiques, and left-right relationships all preserved. Proliferation of characters, third idols, changes in face or costume, deformed limbs, finger abnormalities, body fusion, microphone proliferation, misalignment between singing voice and mouth, text, subtitles, logos, watermarks, and ending that shows the next part are prohibited.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Cinematic Samurai Sword Fight Montage
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11020.jpg" width="480" alt="SD2_11020"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-samurai-sword-fight-SD2_11020">🌐 Watch Online</a>

#### 📝 Prompt
```
A cinematic live action sequence starting in a dimly lit gritty courtyard. A rugged warrior with dirt on his face meticulously grinds a thick wooden staff against a heavy stone wheel. Wood shavings and glowing sparks fly into the camera in extreme slow motion under a single shaft of natural sunlight. Suddenly the scene smash cuts to an explosive nighttime battlefield. A rapid fire cinematic montage of live action samurai warriors engaging in intense high speed sword fights. Massive bursts of practical fire and glowing orange embers explode from their clashing metal blades lighting up the dark foggy environment. Hyper realistic cinematic lighting with glowing particles swirling in the dark. Extreme close ups of the warriors with fierce determined expressions and sweat dripping from their faces. Dynamic sweeping camera movements spinning around the fast paced action. Shot on 35mm film with anamorphic lenses for natural lens flares and deep cinematic bokeh. Flawless photorealistic textures on armor skin and fire. Aspect ratio 16:9. Length 15 seconds. Seedance 2.0. Music prompt a heavy cinematic bass drop transitioning into a high energy orchestral rock hybrid with aggressive string staccatos and tribal war drums.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.14s`

---

### 🎬 Xianxia Sister's Deadpan Ghost Prank Reaction
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11018.jpg" width="480" alt="SD2_11018"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/xianxia-sister-ghost-prank-SD2_11018">🌐 Watch Online</a>

#### 📝 Prompt
```
[Overall Style] Cinematic realistic texture, pure ancient-style Chinese xianxia aesthetics; the first half builds tension through supernatural suspense, while the second half shifts into a restrained cold comedy; Using classical blank composition, cool moonlight, warm lantern light, dark blue and faded ivory tones, delicate film grain, and clearly positioned sound to mislead, the entire film contains no modern elements. [Character] Character ID A \| Sword Immortal Senior Sister Sword Immortal Senior Sister @图片 1, 25–30 years old, East Asian woman with an oval face, fair natural skin, dark almond-shaped eyes, long black hair half-up, fixed with a white jade hairpin, tall and slender figure, wearing white embroidered silk Hanfu, semi-transparent layered wide sleeves, light silver waistband, jade pendant, and white cloth boots. She enters from the courtyard, her shoes appearing from head to toe in the frame, holding a silver longsword and a bronze lamp. Character ID B \| Little Junior Sister Little Junior Sister @图片 2, an East Asian woman aged 20–25, with a round, lively face, braided black hair, petite figure, wearing a teal-green linen hanfu, a dark cloth belt, a wooden hairpin, and black cloth shoes, plus a layer of removable white tulle. She holds a bamboo slip script, hidden behind a tightly closed screen on the same side. [Shot 1\|0-5s\|Low-angle panoramic follow-up] The abandoned Shanmen opera stage at midnight, the damp stone floor, dark tiled eaves, faded red curtains, tightly closed paper screens, carved wooden pillars, bamboo groves swaying in the wind, an incense burner, and two bronze lamps all form a clear and stable spatial relationship. Character ID A: Sword Immortal Senior Sister @图片 1, an East Asian woman aged 25–30, oval face, fair natural skin, dark almond eyes, long black hair half-up, fixed with a white jade hairpin, tall and slender, wearing white embroidered silk Hanfu, semi-transparent layered wide sleeves, light silver waistband, jade pendant, and white cloth boots. She enters from the courtyard, her shoes appearing from head to toe in the frame, holding a silver longsword and a bronze lamp. Character ID B: Little Junior Sister @图片 2, an East Asian woman aged 20–25, with a round, lively face, braided black hair, petite figure, wearing a teal-green linen hanfu, a dark cloth belt, a wooden hairpin, and black cloth shoes, plus a layer of removable white tulle. She holds a bamboo script and hides behind a tightly closed screen on the same side. From inside the stage came the low sobbing of a woman in the distance and the slow sound of dragging wood; [Shot 2 \| 5-10s \| Medium Shot Follow] The same Sword Immortal senior sister wearing a white embroidered silk Hanfu approaches the same paper screen. The lantern flame trembles gently, and the shadow of a woman with long hair hanging down slowly stands behind the screen. The same junior sister continued hiding behind the screen, shouting in a piercing voice, "Give me back my life—" The same Sword Immortal senior sister drew the same silver longsword, turned once, and then maintained a precise defensive stance; The camera slowly pushes the shadow against the wall, the strings of the guqin gradually tighten, and the wooden floor creaks softly; [Shot 3 \| 10-15s \| Close-up revealed, then extreme close-up] The same paper screen suddenly opens horizontally, clearly revealing the same junior sister in a greenish Hanfu draped in the same loose white tulle, holding the same bamboo script and a wooden wooden awakening stick. She is actually just rehearsing the female ghost character. The little junior sister showed an expectant smile and asked, "Senior sister, does it look like a vengeful ghost?" The same Sword Immortal senior sister was still frozen in place, holding her sword, the tip stopping beside her, replying expressionlessly, "It does." If you had been half a step later, you really would have been in trouble. The little junior sister's smile vanished instantly, and she swallowed nervously. The scene freezes at the moment when the Sword Immortal Senior Sister calmly rolls her eyes, the terrifying soundtrack abruptly stops, and the wooden awakening wood falls with a decisive impact. [Technical Requirements] Strict total duration of 15 seconds, 16:9 landscape mode, three continuous and clear shots, native synchronized Mandarin dialogue, accurate lip movements, stable facial and costume characters, lanterns, shadows, tulle, silk fabric, hair, cigarettes, and longsword movements all realistic and natural, no subtitles generated, only two visible characters always appear. [Negative words] blurry, bad quality, low quality, low resolution, noisy, jpeg artifacts, watermark, text, error; deformed, mutated, bad anatomy, poorly drawn hands, bad composition, out of frame, disfigured; inconsistent character, changing clothes, face morphing, background shift, glitching cuts, disappearing props
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Anime Basketball Game Winner
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11016.jpg" width="480" alt="SD2_11016"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/anime-basketball-game-winner-SD2_11016">🌐 Watch Online</a>

#### 📝 Prompt
```
A mixed-media video featuring 2D anime characters @image1 @image2 and ultra-realistic live-action backgrounds @image3. Create a cinematic basketball movie using @image1 as the main player, @image2 as teammates, @image3 as the outdoor urban basketball court, and @image3 as the golden-hour lighting atmosphere. Hyper-realistic sports broadcast aesthetic, dynamic handheld camera movement, cinematic depth of field, realistic sweat and jersey physics, smooth shot transitions, natural body proportions, photorealistic 8K quality. Shot 1 (0-2s): Wide sunset shot. The main player dribbles aggressively past defenders while teammates spread out. Low-angle tracking camera follows fast footwork and bouncing ball, energetic crowd in background. Shot 2 (2-5s): Medium tracking shot. Fast chest pass to teammate, followed by a smooth no-look behind-the-back return pass. Quick whip-pan camera movement follows the ball, defenders react late. Shot 3 (5-7s): Cinematic close-up. The main player catches the ball and performs a hesitation dribble, intense focus toward the hoop, sneaker scrape sounds, dramatic sunset rim lighting, shallow depth of field. Shot 4 (7-10s): Slow-motion finale. The main player jumps for a game-winning three-pointer. Orbit camera and slow dolly-in follow the ball into the net with realistic crowd reaction and cinematic sports-commercial ending. No onscreen text.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.13s`

---

### 🎬 Olympic Platform Diving Slow Motion
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11014.jpg" width="480" alt="SD2_11014"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/olympic-platform-diving-slow-mo-SD2_11014">🌐 Watch Online</a>

#### 📝 Prompt
```
[Style] Olympic style platform diving, TV broadcast + cinematic mixed texture (16:9 cinematic, photorealistic), Super Slow-mo, indoor diving hall with cool water blue tones, national-level action standards [Duration] 15 seconds [Scene] Indoor Diving Gym: 20-meter-high platform, anti-slip mats on the platform, a turquoise pool below, shimmering at the bottom, spectator stands blurred into dark blocks against the background, and spotlights on the ceiling [Character] Main Character @ [00:00-00:03] Shot 1: The Stillness Low-angle aerial shot: The protagonist stands at the very edge of the 20-meter platform, toes gripping the edge, arms raised in front of the platform, and the entire venue is so quiet that only the sound of water remains. Close-up: She took a deep breath, her chest rising and falling, fingers slightly straightened, eyes fixed on the water below her front, jaw tightened. [Sound Effects] The venue's ambient sounds suddenly fell silent, with only the faint splashing of the pool water and a deep breath. [00:03-00:05] Shot 2: The Takeoff Side-view medium shot: she presses her arms down, legs pushing off the stage, leaping upward off the stage, her body tightening at the highest point hugging her knees, her whole body spinning backward like a wind-up spinning top. [Sound Effect] A muffled thud of the pedal was followed by only the sound of wind. [00:05-00:10] Shot 3: The Flight, Super Slow-mo Upgraded to slow motion, the camera follows the drop vertically from the height of the jump: she completes three and a half backward flips with knee hugs in midair, flipping cleanly at a steady speed, each twist tightly tightened, water droplets flying from hair tips hanging in the air; After flipping into position, she suddenly opened her body, raised her arms in a straight line, pointing straight at the water, and descended faster, with spotlights flashing swiftly over her. [Sound Effects] The wind during the elevation segment is stretched out, the faint rustling of the fabric as it flips, and the moment the body opens, there is a crisp "whoosh." [00:10-00:12] Scene 4: Rip Entry Restoring normal speed, water surface height side-mounted angle: it plunged vertically into the water like a needle, with only a small ripple and a few droplets bouncing at the entry point, almost no splash, and the water quickly calmed down. [Sound Effect] Entering the water was a brief, clean "puff," followed by a burst of exclamations and applause from the audience. [00:12-00:15] Shot 5: Underwater + Rise Underwater Position: After entering the water, she stretches her body, with bubbles dragging behind her in a straight silver column, and she flips upward in the blue water; Cutting water surface: She breaks through the water, shakes her hair, wipes the water off her face, looks toward the scoreboard with a smile, and freezes the scene. [Sound Effects] The underwater low-frequency gurgling changes to the clear sound of water at the moment of emergence, with continuous applause and a stop-motion stopping tone. [Note] The smaller the splash when entering the entire piece, the better (Rip Entry technique). For aerial somersaults, the posture must be compact and the rotation speed even, avoiding limb looseness
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Luxury Cinematic Fashion Commercial
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11010.jpg" width="480" alt="SD2_11010"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/luxury-cinematic-fashion-commercial-SD2_11010">🌐 Watch Online</a>

#### 📝 Prompt
```
15-second ultra-realistic cinematic fashion commercial. A stylish young woman wearing a white tailored blazer, white fitted square-neck top, high-waisted white trousers, oversized black square sunglasses, a thin gold necklace, and small gold hoop earrings walks confidently outside a modern luxury café with floor-to-ceiling glass windows, cream patio umbrellas, wooden tables, and beige stone flooring. Warm golden-hour sunlight creates soft natural shadows. She gently adjusts her sunglasses, smiles subtly, and walks toward the camera with graceful, confident movements. Smooth gimbal tracking, shallow depth of field, cinematic bokeh, 85mm portrait lens, HDR, premium color grading, realistic skin texture, luxury editorial fashion style, ultra-realistic, 4K, 60fps. No text, no logo, no watermark, no outfit changes, no background changes, no extra people, no blur, no distortion.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.13s`

---

### 🎬 Woman Battles Lions Desert Arena
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11002.jpg" width="480" alt="SD2_11002"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/woman-battles-lions-desert-arena-SD2_11002">🌐 Watch Online</a>

#### 📝 Prompt
```
A 15-second ultra-realistic cinematic action scene of a fearless woman battling a group of wild lions in an ancient desert arena.

Shot 1 (0–3 sec):
Extreme wide cinematic shot of an ancient ruined arena surrounded by rocky mountains at sunset. A powerful woman wearing a rugged warrior outfit stands alone in the center while three massive lions slowly approach from the shadows. Dust moves through the air, dramatic atmosphere, intense tension.

Shot 2 (3–6 sec):
Low-angle action shot as the lions charge toward her. The camera moves quickly around the scene as she dodges the first attack with incredible agility, sliding across the ground while dust explodes around her. Realistic lion movement, detailed fur, cinematic motion blur.

Shot 3 (6–10 sec):
Fast-paced combat sequence. The woman uses her skills and intelligence to fight back, avoiding attacks and overpowering the lions one by one. Dynamic camera angles, close-ups of her determined expression, slow-motion moments showing powerful movements, realistic physics and intense action choreography.

Shot 4 (10–13 sec):
The final lion makes a dramatic leap toward her. The camera rotates in slow motion as she blocks the attack and defeats the lion with a powerful final move. Dust fills the air as the arena becomes silent.

Shot 5 (13–15 sec):
Epic hero shot. The woman stands victorious in the center of the arena as the defeated lions retreat into the distance. The camera slowly pulls back, revealing the vast landscape, golden sunset, wind moving her hair and clothes, cinematic victory moment.

Style:
Ultra-realistic Hollywood action film, epic scale, realistic animal movement, dramatic lighting, cinematic camera work, detailed textures, 4K quality, natural motion, intense atmosphere.

Negative Prompt:
cartoon, fantasy CGI look, unrealistic animals, blurry, bad anatomy, extra limbs, unnatural fighting, blood, gore, distorted face, flickering, low quality, watermark.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.05s`

---

### 🎬 Pink Hanfu Combat Dance in Ancient Temple
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10998.jpg" width="480" alt="SD2_10998"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pink-hanfu-combat-dance-ancient-temple-SD2_10998">🌐 Watch Online</a>

#### 📝 Prompt
```
Inside an enormous ancient temple with towering stone pillars, cracked marble floors, floating dust particles, and powerful beams of sunlight streaming through the ceiling, a beautiful young female martial artist wearing an elegant flowing pink hanfu-inspired combat dress performs an extraordinary combat dance. The sequence opens with an ultra-wide cinematic shot as she glides gracefully across the polished stone floor. Her silk sleeves and layered skirt flow naturally with every movement while the camera circles her in a smooth 360-degree motion. She suddenly launches into an acrobatic spinning kick, flipping through the air with flawless martial arts precision. The camera switches to an extreme low-angle shot emphasizing her height and power as her dress ripples realistically. The action transitions into dramatic slow motion as she lands softly before instantly accelerating into rapid spinning footwork. Every movement creates realistic cloth simulation, subtle dust bursts, and perfectly synchronized body mechanics. She leaps high beneath a brilliant shaft of heavenly light. The camera follows from below while volumetric lighting surrounds her, creating an angelic silhouette. Her expression remains calm, focused, and fearless. As she begins rotating in midair, glowing golden energy ribbons emerge around her body, spiraling outward like magical dragon-shaped currents. Sparks, floating embers, and swirling particles react naturally to her motion. The camera pulls back into a breathtaking wide shot as the golden energy tornado expands across the temple floor, illuminating the ancient architecture with warm orange reflections. Dust rises naturally while light scatters realistically through the atmosphere. The final moment freezes in epic slow motion as she floats gracefully at the center of the glowing spiral beneath the heavenly beam, surrounded by rotating rings of golden energy. The camera slowly cranes upward, revealing the magnificent temple from above before fading to black.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 A Day In Her Life
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10994.jpg" width="480" alt="SD2_10994"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/day-in-her-life-SD2_10994">🌐 Watch Online</a>

#### 📝 Prompt
```
Use the uploaded storyboard image as the visual sequence reference and preserve the exact same beautiful young woman throughout the entire film. Maintain identical facial identity, hairstyle, skin tone, makeup, black fitted crop top, grey jogger pants, black shoulder bag, body proportions, and accessories across every scene. Ensure perfect character consistency and realistic anatomy. Create an ultra-realistic cinematic "A Day in My Life" lifestyle film with premium commercial cinematography. The atmosphere should feel calm, authentic, and aspirational, using warm natural lighting, soft shadows, realistic reflections, cinematic colour grading, shallow depth of field, smooth handheld and gimbal camera movements, and subtle environmental ambience. The film begins with her sleeping peacefully as an alarm rings beside the bed. She slowly wakes up, reaches for her phone, and turns the alarm off. She walks into a modern bathroom where she washes her face with cold water before getting dressed. Standing beside an open wardrobe, she chooses a black jacket, then prepares a healthy smoothie in her minimalist kitchen before taking a sip. She leaves her apartment and confidently walks through a lively city street before entering the subway station. She rides the escalator, waits on the platform, and boards a crowded train while quietly observing the people around her. After arriving, she walks through the office lobby and rides the elevator before entering a modern open workspace where she works on her laptop with complete focus. As the workday ends, she walks through the city during golden hour, enjoying the peaceful evening atmosphere. The film concludes with her back in her bedroom, lying on the bed while scrolling through her phone with a relaxed smile before placing it beside her and closing her eyes. Style: Premium lifestyle commercial, realistic daily routine, cinematic storytelling, natural performances, luxury colour grading, soft bokeh, subtle lens flares, smooth transitions, emotionally warm atmosphere, photorealistic, ultra-detailed, commercial quality. Negative Prompt: No text, no subtitles, no logos, no watermarks, no duplicate people, no distorted anatomy, no unrealistic facial features, no AI artifacts, no cartoon style, no flickering, no oversaturated colours, no abrupt transitions.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.55s`

---

### 🎬 Raccoon Salty Cooking Fail
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10992.jpg" width="480" alt="SD2_10992"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/raccoon-salty-cooking-fail-SD2_10992">🌐 Watch Online</a>

#### 📝 Prompt
```
Live-action + flat 2D sticker composite, POV cooking vlog, vertical 9:16, 10 seconds, 8K, light handheld micro-shake. Realistic kitchen + funny flat sticker character. Scene: Home kitchen from first-person perspective. Beef and greens are frying in a black pan, oil sizzles, steam rises. White tiles, sauce bottles, sink on the right, side daylight. Character: Little chibi raccoon Solka as a flat 2D sticker: gray-blue fur, dark mask around eyes, striped tail, big red bow, round black glasses, yellow dress, red shoes. Thick outline, paper texture, colored pencil style. Sitting on a small stool by the stove. 00:00–00:03 — Salty Avalanche Real hand stirs meat with a spatula. Solka smiles cunningly and pours a whole jar of salt into the pan. Salt falls like a waterfall, forming a white mound. SFX: sizzling, salt pouring. 00:03–00:05 — Oops Hand takes the jar away, next to her head the spatula makes a comical "BONK!". Glasses slide down, tail stands on end, Solka jumps. SFX: bonk, cartoon spring. 00:05–00:08 — Salty Payback Solka tastes the oversalted food. Cheeks puff up, eyes become spirals, cartoon tears spray from eyes. SFX: crunch, pause, exaggerated crying. 00:08–00:10 — Salty K.O. She swallows, eyes turn into Xs, falls off the stool like a paper sticker. Stars around head, final freeze-frame. SFX: croak, soft thud, funny spirit sound. Negative prompt: 3D raccoon, realistic fur, redesign, extra limbs, deformed hands, morphing, flicker, blur, fake salt physics, gore, subtitles, watermark, UI.
```

#### 📌 Details
- Ratio: `0.57` | Duration: `15.08s`

---

### 🎬 Lazy Boss Lady Diner Comedy
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10990.jpg" width="480" alt="SD2_10990"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/lazy-boss-lady-diner-comedy-SD2_10990">🌐 Watch Online</a>

#### 📝 Prompt
```
Act 1: [Reference Locking] Reference Figure 1 hf_20260730_044943_833909d3-0181-4d86-b4ad-8fdd91945fbd For Boss Lady #1 Wearing hf_20260730_045132_8f945ce1-0e33-4e9c-86c6-5b5bdb0b0185 Leg-to-foot proportions, thin sock texture, sofa sitting, and black high heel placement are the highest priorities; Maintain #1's preset face, hairstyle, makeup, and clothing. Reference video shows the small restaurant space, male #2's appearance, physique, clothing, and lifestyle performance rhythm as the highest priority. #1, #2, #3均为成年人, face-swapping, copying, merging, or swapping identities are not allowed. [Overall Setting] A real comedy of small restaurant life. Boss #1 sits on the sofa in the left rear lounge area scrolling on her phone, striking a restrained and natural "Siren Pose": leaning against the sofa, one shoulder slightly lowered, waist and back forming a natural, soft S-shaped curve; legs elegantly crossed and slightly stretched forward, toes relaxed; head slightly tilted, long black hair naturally falling over one shoulder. The posture is quiet, lazy, and attractive, but she does not actively tease diners, does not lick lips, flirts, or deliberately twist her body. Man #2 sits at the first green old table in the front right to eat noodles. Diner #3 sits at another independent table in the right rear to eat noodles, leaving a clear aisle between the two tables; the two never sit at the same table. Male #2 paused briefly while eating noodles while watching the boss #1, then asked her to get an orange drink. Diner #3 sat at another table eating noodles from the moment he first appeared at the table, setting up space for the subsequent reversals. [Real Photography] Unedited real video handheld on iPhone. 9:16 portrait, 1080×1920, 30fps, 26–28mm equivalent focal length, an average diner stands about 1–1.5 meters away. Auto exposure, auto focus, auto white balance. Retention of slight hand shake, breathing fluctuations, half-shot delay of reframing, brief focus search, motion blur, local window overexposure, and shadow noise. No filters, no beauty filters, no skin smoothing, no cinematic lighting, no static camera movement, no artificial shallow depth of field. Preserves real skin texture, scattered hair, clothing wrinkles, and thin socks with natural reflection. [Character Position] Boss #1: Beige gray double sofa in the left back. Reclining on the sofa scrolling on her phone, maintaining a natural siren-like posture, not paying attention to the diner for now. Man #2: The first green old dining table in the front right, eating noodles alone, the person who calls for a drink. Diner #3: The second independent old dining table in the right back, about one meter away from Man #2, with a clear aisle in the middle. He eats noodles alone, not moving in sync with Man #2 or speaking in advance. [Space and Props] Rear left: beige sofa, the owner's wife's phone, a pair of black high heels at his feet, one of which is closer to the camera. Center rear: beverage freezer, service desk, beige accounting book. First table front right: Man #2, a bowl of noodles, a pair of chopsticks, a small dish of seasonings. Second table at the back right: Diner #3, another bowl of noodles, another pair of chopsticks, and another small plate of seasonings. The two male diners' tables, bowls, chopsticks, and condiments are completely independent—not shared, copied, or exchanged. Inside the freezer is only one bottle of orange drink: about 500ml of transparent hard plastic bottle, filled with naturally translucent orange-yellow liquid and a colored anti-theft ring screw cap. This bottle appears only throughout the film and cannot be placed on the dining table in advance. [15-Second Strict Storyboarding] → 0–2 seconds: Low-angle foot-building shot. The shot starts with Boss #1's legs resting on the edge of the sofa. She maintains a restrained siren-style posture: legs naturally crossed, legs slightly stretched forward, thin socks with delicate but not excessive realistic reflections, and her toes naturally relaxed. A pair of black high heels rests on the wood-grain floor, one of which is close to the foreground. After a brief search, autofocus lands on the front foot and the edge of the sofa. The camera is only for quick, everyday life, not slowly scanning the legs. → 2–4 seconds: Boss lady sofa middle shot. The photographer naturally raises her arm, and the camera quickly pans to her upper body. She leans against the sofa, one shoulder slightly lower, her waist and back forming a soft S-shaped curve, her head slightly tilted, and her long hair falling to one shoulder. She lowers her head and swipes her phone with her thumb, a faint smile at the corner of her mouth because of the phone content, her expression calm and lazy, not looking at the two diners. Focus naturally drifts from the foreground to her face. → 4–6.8 seconds: Two dining tables in the same frame, cutting the slightly wider right dining area to medium shot. Man #2 sits at the first table in the front right; Diner #3 clearly appears at the second table in the right rear. There was a clear corridor between the two tables. Man #2 took a sip of noodles, then looked over the bowl to look at the proprietress in the rear left. His chopsticks stopped at his mouth, and the remaining noodles briefly hung between the chopsticks and the bowl, naturally distracted. Diner #3 was always at another table, looking down to pick up noodles, blowing on them, and chewing, never looking up or synchronizing with Greek #2. → 6.8–8.5 seconds: Male#2 ordered a drink. Male#2 blinked to snap back to reality, finished the remaining noodles, and raised his hand toward the proprietress, calling out: "Proprietress, another drink!" Diner #3 was still eating noodles at his table at the rear right, only pausing slightly when hearing the sound, but neither looking up nor speaking. → 8.5–10.5 seconds: The boss lady responds and stands up. Hard cut to the middle shot. She stops scrolling on her phone, looks up at Man #2, and calmly responds: "Hey, here it comes." She locks her phone and places it face down on the armrest of the sofa. Then she ends her reclining posture, naturally leans forward, slides her feet into a pair of black high heels on the floor, and stands up. The phone must be left on the armrest of the sofa. → 10.5–12.5 seconds: Drinks taken from the freezer, hard cut from the side of the freezer. Middle view from the side of the freezer. The lady boss opens an old glass freezer, only taking out a sealed orange drink; Her left hand smoothly picks up the beige account book from the front desk. After the freezer closes, she immediately turns into the central aisle, walks slightly to the side of her body forming an S-curve, slightly pushes her hips sideways, stretches her legs forward and backward, half-lowered eyes cold and forward. → 12.5–15 seconds: Sent to the side of Man #2's table. Handheld camera follows the proprietress moving quickly from left rear to right front, with natural vertical shaking and slight motion blur. She stops in the middle of the aisle between two tables, slightly turning her body toward Man #2 on the left side of the frame, forming a smooth S-curve, elongating shoulders and neck, half-lowering eyes cold eye gazing directly at #2, placing an orange drink on the #2 table: "Here, your drink." "Final frame: The orange drink remains sealed, the proprietress holds an accounting notebook in her left hand; Two male diners sit at two different tables. [Audio] Only natural sounds inside the restaurant painting are used: freezer compressor, exhaust fan, distant conversation, noodle sucking sounds, chopsticks clinking bowls, high heels hitting the floor, cabinet door opening and closing, footsteps, and the sound of beverage bottles touching the table. White-backed reverb with real restaurant reverb, volume naturally changing as distance changes. No background music, narration, canned laughter, or post-production sound effects. [Continuity Requirements] The proprietress always moves from the rear left to the right front. Male #2 is fixed at the first table in the front right, and Diner #3 is fixed at the second table in the rear right; no two people should sit together. #3从用餐区第一次出现时就必须清楚存在. Two dining tables, two bowls of noodles, and two pairs of chopsticks are each separate. The orange drink can only be taken out of the freezer once and remains sealed when delivered to the side of Table #2. The lady proprietress's siren-style pose only appears in the sofa segment; After getting up to work, return to a natural, neat restaurant owner's wife's movements. [Negative Tips] Do not let Male #2 and Diner #3 sit at the same table; Do not share bowls, chopsticks, or seasonings; Do not turn #3 into a replica of #2; Do not eat noodles, look up at the same time, or speak simultaneously. Do not show siren-style poses as dancing, hip-shaking, flirting, licking lips, exaggerated chest puffing, or erotic performances; Do not sexualize leg and foot shots, do not slowly scan the body. Do not change #1's face, hairstyle, clothing, leg-to-foot proportions, or thin sock texture; Do not let phones, high heels, noodles, chopsticks, ledgers, or drinks float, teleport, or duplicate. Do not turn an ordinary small restaurant into a luxury restaurant; Avoid HDR, cinematic color grading, strong halos, excessive bokeh, plastic skin, stabilizer camera movement, slow motion, subtitles, watermarks, or platform UI. Act 2: [Reference Lock] Reference Image 1 hf_20260730_044943_833909d3-0181-4d86-b4ad-8fdd91945fbd for boss #1 wearing hf_20260730_045132_8f945ce1-0e33-4e9c-86c6-5b5bdb0b0b0185 with leg-to-foot proportions, thin sock texture, body lines, and black high heel styling as the highest priority; Maintain #1's preset face, hairstyle, makeup, and clothing. Reference video shows the top priority for the appearance, physique, clothing, and lifestyle performance rhythm of the restaurant space, male #2, and diner #3. All three are adults and may not swap faces, copy, merge, or swap identities. [Continued Starting Point] Using the last frame of Part A July 30: Lady #1 stands in the aisle between two tables, slightly turning her body toward Man #2, holding a beige ledger in her left hand; Male #2 sits at the first green old dining table in the front right, his right hand just touching the only sealed orange drink on the table; Diner #3 sits at the second independent table at the rear right, holding chopsticks and observing from the side and back. The lady boss's phone remains on the armrest of the sofa in the left rear. The characters, tables and chairs, tableware, lighting, and restaurant space fully continue from Part A. [Overall Setting] Male #2 asks about the drink price; after hearing six dollars, he only agrees to pay five. The lady boss didn't argue, maintaining a restrained and natural siren-style pose, took back the drink, opened it, took a small sip, and handed the drink to Mr. #2. Diner #3 saw the whole process, stopped eating noodles, looked at the lady proprietress, and said, "Like this, give me a box." The lady boss still had a small amount of drink in her mouth, her cold expression instantly broken, covering half her face with the ledger, and couldn't help but laugh at the back of the notebook. [Realistic Shot] Unedited real video held on an iPhone. 9:16 portrait, 1080×1920, 30fps, 26–28mm equivalent focal length, an average diner filmed from about 1–1.5 meters away. Auto exposure, auto focus, auto white balance. When the camera rotates between Male #2, the boss lady, and customer #3, slight hand tremors, breathing fluctuations, half-frame delays in reframing, brief focus searches, and real motion blur are retained. White balance slightly shifts between natural store light, cool white fluorescent ceiling light, and freezer afterglow. Image flat, preserving local overexposure near windows, dark noise, edge chromatic aberration, and natural skin texture. No filters, beauty filters, skin smoothing, cinematic lighting, stabilizer camera movement, or artificial shallow depth of field. [Character Positioning and Performance] Boss Lady #1: Stands in the aisle beside two tables, mainly facing Man #2, while not obstructing customer #3 from observing her drink. Body slightly tilted, shoulders relaxed and sunken, neck naturally elongated, waist, back, and hips forming a soft S-shaped curve; Legs staggered, one leg bearing weight. Half-lowered eyelids, calm expression with a distant expression, but not actively flirting. Man #2: Fixed at the first table at the front right, responsible for asking prices, haggling, and taking drinks. Diner #3: Fixed at the second independent table at the right back, about one meter away from #2. He can only observe and say the last sentence, not approach table #2. [Space and Props] The first table at the front right belongs to Guest #2: a bowl of noodles, a pair of chopsticks, and a small plate of seasonings. The second table at the back right belongs to Guest #3: another bowl of noodles, another pair of chopsticks, and another small plate of seasonings. The two tables are completely independent, not shared, copied, or exchanged. The entire film contains only one approximately 500ml bottle of orange drink: a transparent hard plastic bottle, orange-yellow liquid, and a colorful security ring with a screw-on cap. Status strictly continuous: Sealed full bottle → #2拿起 → Shop owner takes it back → Open → Take a sip → Liquid level drops → Hand #2 The cap and beige ledger must not disappear, deform, or duplicate. [15-second strict storyboard] → 0–2 seconds: Price inquiry and answer Male #2 picks up the sealed orange drink, glances at the bottle, looks up and asks: "How much is this?" Autofocus first falls on the orange liquid and the bottle highlight, then slowly turns to #2's face. The shop owner turns slightly to him, shoulders lowered, neck lengthened. She glances at the drink from under half-lowered eyelids, then calmly answers: "Six pieces." Diner #3 is still eating noodles at his own table at the right rear and does not join in early. → 2–3.8 seconds: Man #2 bargains. Man #2 lightly weighs his drink, raises his eyebrows, and negotiates: "I'll just give five yuan. Is five yuan okay?" Customer #3 pauses slightly as he picks up the noodles, his eyes looking from above the bowl to the two of them but not looking up to speak. → 3.8–5 seconds: The lady boss takes back the drink. The lady boss doesn't argue or get angry. She quietly watches #2 for about 0.3 seconds, maintaining a gentle S-shaped stance, then reaches out with her right hand to grasp the bottle neck. Man #2 lets go after confirming she's holding it firmly. The drink returns intact to the lady owner; their hands don't stick, don't pierce the mold, and don't touch for long. → 5–6.3 seconds: Opening the bottle The owner holds the ledger between her left arm and body, holds the colored bottle cap with her left hand, secures the bottle with her right hand, and unscrews the security ring cap. A clear "click" sound is heard. The cap stays in her left hand, and the drink doesn't splash. The focus briefly falls on her fingers and the cap. → 6.3–7.8 seconds: A sip The owner tilts her body slightly, chin raised only about 8–10 degrees, and her neck naturally lengthens. She lifts the orange drink and takes a small sip, half-lowers her eyes to briefly look over the bottle at Man #2, then naturally moves away. The liquid level tilts along with the bottle body. She swallows only a portion, keeping a small amount in her mouth, lips naturally closed, cheeks slightly puffed out. The liquid level inside the bottle has truly dropped by about one sip. Her position cannot cover customer #3, #3必须清楚看见她喝饮料. → 7.8–9 seconds: Handing to Man #2 The proprietress loosens the cap back on the bottle mouth and hands the already sip drink to Man #2. Man #2 catches the middle of the bottle at his table. The proprietress lets go after confirming he holds it firmly. The liquid inside the bottle weakens twice due to the handover. Man #2 first looks at the bottle mouth, then looks up at the owner, mouth slightly open, expression stunned. → 9–11.8 seconds: Diner #3 delivers a reversal line Diner #3 stops eating noodles, chopsticks hanging above his bowl. He first looks at the drink in Man #2's hand that has opened and the liquid level has dropped, then looks up at the proprietress. The camera slightly turns to #3, autofocus briefly searches and stabilizes on his face. #3坐在原位, she gently pointed at the drink with her chopsticks and said seriously, "Like this, get me a case." #3不站起. Doesn't approach #2, doesn't lick her lips, doesn't raise her eyebrows, and doesn't make lecherous faces. → 11.8–15 seconds: The boss's wife bursts out laughing. The camera quickly switches back to the boss's wife. She still has a small amount of orange drink she hadn't fully swallowed earlier. She originally kept her half-lowered eyelids and calmly slithering in an S-shape; After hearing #3's words, her eyes suddenly widened, eyebrows lifted, her head turned to #3, and her body froze for about 0.3 seconds. Then she immediately raised her beige ledger to cover the lower half of her face, her shoulders shaking uncontrollably, failing to hold back laughter. A small amount of orange mist and two or three drops of drink are briefly sprayed onto the back of the ledger, splashing from the top and side edges before falling down. Do not spray on #2, #3, two bowls of noodles or other food. Final frame: Male #2 sits at the first table, holding a drink he drank in a daze; Diner #3 sits at the second table, seriously waiting for a box; The proprietress stands in the aisle, covering her face with the ledger to cough lightly and suppress laughter. [Audio] Only natural sounds from the restaurant painting are used: freezer compressor, exhaust fan, distant conversation, noodle sipping sounds from different directions at two tables, chopsticks clinking and bowl clinking, broken bottle cap anti-theft rings, liquid shaking, swallowing, and the owner's brief coughing and laughter at the end. Dialogue synchronizes with lip-syncing, with only the sound source. No background music, narration, canned laughter, or post-production reversal sound effects. [Continuity and Negative Warnings] Male #2 is fixed at the first table at the front right, and Guest #3 is at the second table at the rear right; Do not share tables, switch seats, or share bowls and chopsticks. #2负责问价. Bargain and take bottles; #3只能观察并说最后一句, do not participate in bargaining or touch drinks. Do not change the faces, hairstyles, clothing, or body shapes of the three people; Do not float, teleport, mold, or duplicate drink bottles, caps, ledgers, or tableware; Do not turn drinks into water, do not lower the liquid level, or automatically refill it; Do not fake drinking, lip piercing, or swallowing completely before spraying out into thin air. Do not exaggerate hip twisting, catwalking, licking lips, sticking out tongue, or performing in a sexual manner; Do not use banshee horns, wings, tails, or fantasy effects; Do not turn a small restaurant into a luxury restaurant or hotel; Do not spit loudly, vomit, or spray on people and food; Do not use HDR, cinematic color grading, excessive bokeh, plastic skin, stabilized camera movement, slow motion, subtitles, watermarks, or platform UI.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `37.83s`

---

### 🎬 Dark Fantasy Beast Rider Charge
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10986.jpg" width="480" alt="SD2_10986"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dark-fantasy-beast-charge-SD2_10986">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-realistic original dark fantasy war sequence on a vast volcanic plain at dusk. An army of terrifying beast riders mounted on armored reptilian and wolf-like creatures charges toward a disciplined line of elite spearmen. 0–4s: extreme wide shot showing hundreds of mounted creatures racing across ash and burning grass, dust clouds and embers exploding behind them. 4–9s: low-angle tracking beside the charge, claws pounding the ground, riders roaring, capes and armor shaking, camera weaving between galloping monsters with intense speed. 9–15s: full-force impact as the beast riders crash into the shield wall, spears splinter, bodies recoil, creatures leap through smoke, the formation bends under enormous pressure. Epic scale, brutal energy, ultra dynamic camera, photorealistic textures, cinematic dust, ash, sparks, deep orange firelight against black storm clouds.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

### 🎬 Armed Gnome Bodycam Takedown
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10984.jpg" width="480" alt="SD2_10984"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/armed-gnome-bodycam-takedown-SD2_10984">🌐 Watch Online</a>

#### 📝 Prompt
```
Garden gnomes with guns. In bodycam POV. 0-4s breach, 4-10s gnomes attack with tiny weapons, 10-15s combat takedown.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

### 🎬 Giant Burning Hands Crush Demon
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10980.jpg" width="480" alt="SD2_10980"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/burning-hands-crush-demon-SD2_10980">🌐 Watch Online</a>

#### 📝 Prompt
```
Strict first-person POV, male hero, face never visible. Do not keep the hero’s hands constantly in frame. The hands appear only during the dodge recovery and the spellcasting moment. One continuous shot, no cuts, vertical cinematic dark fantasy, realistic body-driven camera motion. The camera behaves like the hero’s head and torso, with strong physical reaction during the dodge, then controlled forward focus during the spell. Over the rooftops of a burning medieval city under a storm-black sky, narrow streets below, dark roof tiles, timber-and-stone houses, cathedral spires in the distance, dense smoke columns, scattered rooftop fires, falling embers, hot smoky air. A giant demon suddenly erupts upward from the ground between the buildings, tearing through stone and rooflines, surrounded by dust, fire, and debris. The demon is enormous, heavily armored in jagged black metal with molten red-orange cracks glowing between the plates, bright red eyes, horned helmet, massive chest and shoulders, long heavy limbs, real physical weight. In one hand it wields a burning spear with a blazing red-orange tip. The demon instantly hurls the flaming spear straight at the hero. At the last possible moment the hero performs a dramatic Hollywood-style backward dodge, bending low like a Matrix lean. Enter brief slow motion as the spear slices directly over the camera and narrowly passes above the hero’s head, trailing fire, sparks, and heat distortion. In that near-death moment, the hero breathes out in alarm, “No...” The shot then snaps back to real-time as the spear slams past into the city behind. The hero regains balance and raises both hands only briefly to cast. Thin molten orange-red magic lines along the forearms flare brighter. The demon steps forward through smoke and fire, preparing to attack again. The hero channels a powerful summoning spell upward. From the storm clouds high above, two colossal burning hands descend from the sky, not from the hero’s body, not from the ground. They appear like divine infernal constructs falling through smoke, enormous, symmetrical, clearly shaped like giant human hands, with white-hot edges, dense orange inner fire, thick blazing fingers, and controlled purposeful motion. The giant burning hands drop on both sides of the demon and slam inward with overwhelming force, seizing and crushing the demon’s torso from left and right. Tight center focus on the impact. The demon struggles violently with real mass, armor buckling and collapsing inward, molten cracks bursting brighter across its chest and ribs. Fire pours through the fractures as the crushing pressure intensifies. The demon ignites inside the grip of the giant hands, burns rapidly from within, and its body breaks apart into flames, black ash, sparks, and fragments of ruined armor. The crushing hands keep closing until the dem
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.03s`

---

### 🎬 Cyber Samurai Train Duel
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10978.jpg" width="480" alt="SD2_10978"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cyber-samurai-train-duel-SD2_10978">🌐 Watch Online</a>

#### 📝 Prompt
```
15-second cinematic action sequence aboard a magnetic levitation war train speeding through a dystopian night desert, electric storms illuminating giant industrial ruins in the distance. 0.0–3.0s: Low tracking shot races along the side of the train as a cyber samurai runs across the magnetic exterior panels, sparks erupting beneath his boots. 3.0–6.0s: A chrome-armored assassin descends from a hovering drone transport onto the train roof, neon katana igniting blue light through the storm. 6.0–9.0s: First sword clash sends electrical arcs across the train roof while lightning flashes overhead in slow motion. 9.0–12.0s: High-speed duel across unstable train cars, both fighters nearly thrown off balance as the train tears through debris and collapsing structures. 12.0–15.0s: Massive aerial pull-back reveals the glowing train cutting across the dark wasteland while the duel continues atop the final car.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

<!-- STATS_END -->
