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
- Total Prompts: **4194**
- Updated Today (UTC 2026-07-01): **38**

## 🎬 Today's Updates
### 🎬 Sketchbook Worlds: Imagination Unleashed
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04213.jpg" width="480" alt="SD2_04213"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sketchbook-worlds-imagination-SD2_04213">🌐 Watch Online</a>

#### 📝 Prompt
```
Single uninterrupted cinematic shot begins inside a cozy child's bedroom during golden afternoon light. Sunbeams stream through the window, illuminating floating dust particles. Colored pencils, brushes, and scattered sketchbooks cover a wooden desk. The atmosphere feels warm, peaceful, and filled with creative energy. The camera slowly glides toward an open sketchbook. A child finishes drawing a simple green tree with a colored pencil. As the final stroke touches the paper, the ink begins glowing softly. Leaves gently rustle although there is no wind. Tiny particles of light rise from the page. Without any cut, the camera dives directly into the drawing. The flat paper transforms seamlessly into a vast three-dimensional forest. The camera flies between enormous ancient trees covered in moss. Shafts of sunlight filter through the canopy while birds soar overhead. Butterflies drift naturally through the air. Every leaf moves realistically in the breeze. The transition from paper to reality is completely seamless. The child draws a blue river. Instantly the forest floor opens into a crystal-clear river flowing through the landscape. The camera follows the rushing water at high speed before bursting through a waterfall into an endless ocean. Waves sparkle under the sunlight while giant whales leap gracefully beside the camera. Schools of colorful fish swim beneath the surface. Everything feels alive and physically believable. The child adds distant mountains. Massive snow-covered peaks rise naturally from the horizon as if the world is creating itself. The camera races through valleys and climbs above the mountains into the clouds. The child sketches a dragon soaring across the page. Golden lines become shimmering scales as a majestic dragon comes to life. Instead of attacking, it flies peacefully beside the camera. The camera circles around the dragon while sunlight reflects across its wings. The dragon glides effortlessly through floating islands suspended above the clouds. The child paints stars across the page. The blue sky slowly transforms into deep space while the floating islands drift among colorful nebulae. Entire galaxies appear in the distance. Planets rotate naturally while glowing comets streak silently across the background. The child places one final glowing star in the corner of the drawing. The camera flies toward it until it fills the entire screen. The star suddenly becomes the reflection inside the child's eye. The camera gently pulls back to reveal the child smiling at the finished drawing. The sketchbook now appears ordinary again, but tiny glowing particles continue drifting upward from its pages, hinting that imagination never truly disappears. The final frame holds on the child's smile as warm sunlight fills the room. Camera: One continuous uninterrupted shot. Smooth floating camera movement. Seamless transitions between every environment. Natural acceleration and graceful curves.
```

#### 📌 Details
- Ratio: `0.57` | Duration: `15.17s`

---

### 🎬 Exploring an Interstellar Space Tree
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04212.jpg" width="480" alt="SD2_04212"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/interstellar-space-tree-SD2_04212">🌐 Watch Online</a>

#### 📝 Prompt
```
The camera races along a branch of an impossibly large tree floating in space. The trunk is wider than continents and the branches stretch across entire star systems. Two flight craft weave through glowing leaves the size of cities while rivers of light flow through the bark like veins. The camera follows as they dive through hollow sections of the branch containing ecosystems, floating settlements, and glowing forests. A transparent observation chamber is embedded inside the tree itself, overlooking the flow of luminous sap through the structure. The craft spiral upward through the canopy and emerge above the branches where countless stars hang between the leaves.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Morning Zen Calm
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04211.jpg" width="480" alt="SD2_04211"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/morning-zen-calm-SD2_04211">🌐 Watch Online</a>

#### 📝 Prompt
```
A morning-related video, cinematic, zen and calm, minimalist and modern, smooth transitions and cuts.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.08s`

---

### 🎬 Cyberpunk Wingsuit Canyon Dive
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04210.jpg" width="480" alt="SD2_04210"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cyberpunk-wingsuit-dive-SD2_04210">🌐 Watch Online</a>

#### 📝 Prompt
```
use @[Image 1] as character sheet An ultra-dynamic cyberpunk anime cinematic wingsuit proximity-flying video featuring Jax Storm. Preserve his exact face, glowing cyan cybernetic eyes, messy neon-green hair styled in a sharp undercut, sleek matte-black tech wingsuit with glowing green circuitry lines, integrated helmet with a retractable mirrored visor, carbon-fiber gauntlets, and a pulsing energy core on his chest. Keep perfect character consistency the whole time. Never change his outfit, hair, or face. STYLE: ultra-premium anime feature-film quality, high-energy futuristic sports-anime cinematography, aggressive dynamic action animation, realistic aerodynamics in an stylized anime aesthetic, dramatic twilight lighting, detailed wind and particle simulation, lively expressive facial acting. Absolutely no slow motion at any point. Constant high speed and momentum. SETTING: high-speed flight through a massive futuristic canyon city at dusk, brilliant neon sun flares from towering skyscrapers, fast-rushing holographic advertisements, distant streams of hover-traffic far below, vivid cyberpunk summer atmosphere. FORMAT: one continuous single-take shot, no cuts, no transitions, no montage, one uninterrupted aggressive camera move. HOOK (first 2 seconds): open EXTREMELY close on Jax's face mid-dive from a skyscraper ledge, looking straight into the lens with a fearless, confident smirk, neon hair whipping violently in the wind, helmet visor retracted up. He gives a quick nod toward the camera. Instant speed and energy from frame one. CAMERA: the camera rips backward off his face and whips into a fast 360-degree orbit around his body as he drops. In one unbroken motion, it swings overhead, revealing the massive vertical city drop below, then dives down alongside him. It chases tightly, snapping between front, side, and over-the-shoulder angles, always fast, always handheld-energetic, never static. ACTION FLOW: Jax slams his visor down, snaps his arms out to engage the wingsuit, and slices through the air, accelerating hard as neon clouds blast past. He spreads into a tight tracking glide, weaving dangerously close between two holographic billboards, his body angling sideways across the screen. He throws a cheeky thumbs-up at the camera mid-turn. Then, with a sudden powerful shift in body weight, he pulls up hard—his suit's thrusters fire open with a neon green burst, snapping him upward into a hard, punchy braking maneuver (fast and forceful, NOT slow). The air ripples, his body tenses, and the camera shakes violently with the impact of the deceleration. FINAL MOMENT: now dropping cleanly onto a high-altitude landing platform, the camera swings around to his front. He slides to a halt, the glowing city horizon stretching behind him. He stands up, flips his visor open, grins, and gives a confident two-finger salute toward the lens. The camera pushes in slightly on his smile as the video ends on his triumphant exp
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Anime Girl's Pudding Heist
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04209.jpg" width="480" alt="SD2_04209"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/anime-girl-pudding-heist-SD2_04209">🌐 Watch Online</a>

#### 📝 Prompt
```
The girl from Image1 is used as a reference character. Japanese full-color anime, don't make people different. Maintain a cute and soft atmosphere through costumes, hairstyles, hair color separation, and clothing silhouettes. Fully maintain the character sheet. A refined 15-second cel-look 3D animation. Not realistic live-action, but exaggerated 3D cartoon animation performances. Delicate features, expressive eyes, beautiful contours, soft skin shading, fine costume materials, glowing magical particles, moonlight, cinematic depth of field, dramatic rim lights. The contour lines are modest. Visualize clearly readable facial expressions, eyes, eyebrows, mouth, and poses. The setting is a spacious and luxurious island kitchen. Large island counter, rear storage, refrigerator, hanging lighting, spacious floor, and a deep space. On the central island counter, there is a single premium pudding with a golden caramel gloss. Pudding always appears important as an object. The positions of the kitchen, counter, and pudding are consistent throughout the cut. He doesn't act normally. Make your movements big, fast, sharp, and comical. スナッピーなポーズ・トゥ・ポーズ。 Smooth uniform movement is prohibited. Each action is a pause, a short hold, a sudden acceleration, a big overpass, a recoil, a complete stop, and only the hair and sleeves sway slowly and slowly. Add a short finishing touch at the end of the main pose. The shape of the body and the costume are not ruined. Her expression naturally does not become restrained. Only at important moments, quickly switch the angles of the eyes, eyebrows, mouth, cheeks, gaze, and neck. The facial expressions used include wary narrow eyes, a suspicious face raised with one eyebrow, a big surprised face, a sideways sinister face, a scheming suspicious face, a nervous face puffing out cheeks, a starry eye that discovers something, a look of emotion, and a happy, satisfied expression. Maintain cuteness while making comical and bold expressions. 0.0 to 1.5 seconds: Ultra-wide shot of a spacious island kitchen. Golden pudding is placed on the central island counter. The caramel pudding sparkled. From the shadow of the counter at the edge of the screen, the girl's white hair popped out for a moment, then quickly withdrew. 1.5 to 3.0 seconds: A girl slowly poked her head out from behind the counter. At first, just the eyes. I looked at the pudding with a slender, wary gaze. He raised an eyebrow. The next moment, her eyes opened wide, and her pupils sparkled. Hold your fingertips upright, place your back on the side of the counter, and stop firmly. Only her hair and sleeves swayed with delay. 3.0–4.8 seconds: The first major move. The girl crouched down slightly, hugging her body tightly. The next moment, it explosively shot out sideways from behind the counter. Short afterimages and a modest speedline. Upon arrival, I went a bit too far and hurried back to stick to the side of the counter. Her expression quickly shifts from seriousness, surprise, impatience, to a grin. Finally, it comes to a complete stop. Her hair, sleeves, and hem of her clothes sway heavily and belatedly. 4.8–6.5 seconds: Moved further into the shadows of refrigerators and storage shelves. He stomped his feet at super high speed with his toes, pausing briefly with only his upper body. The next moment, it moves with a 'buon' (a sound). The camera tilts slightly to the side, chasing with a sharp pan. Upon arrival, she lifts one leg and spreads her arms to balance in an exaggerated signature pose. Switch to sideways glances, suspicious faces, and confident faces. 6.5–8.5 seconds: A girl sneaks low to an island counter with pudding. Not a natural walk, but cartoon-style exaggerated sneaking feet. With every step, stop, just move your feet forward, your body catches up all at once, your head goes a bit too far, you bounce back, and you come to a sudden stop. Her gaze quickly switches to the pudding, right, left, behind, and pudding. Sudden braking near the counter. Only her hair and sleeves flowed forward and returned. 8.5–10.5 seconds: The highlight of discovering pudding. A girl poked her head out from under the counter. At first, just the eyes. After checking left and right, I look at the golden pudding. His eyes opened wide, sparkling like stars in them. My eyebrows twitched, and my cheeks turned red. I put both hands on the counter and my body stretched upward for a moment. Switch between an emotionally moved face, a mesmerized face, or a scheming, scheming face. Finally, she stopped completely with a signature pose. 10.5–12.5 seconds: The girl gently lifts the pudding with both hands. Before lifting, shrink slightly and focus. The next moment, she quickly pulled the pudding close to her chest. I pushed a little backward with momentum, then retreated with recoil. Unable to contain my joy, I trembled slightly. Switching between serious faces, surprised faces, smirks, and sparkling faces full of anticipation. The camera suddenly stopped closer. Pudding placed with a spoon. Just before bringing my face close to Pudding, I stopped briefly. 12.5–14.2 seconds: The biggest reaction to tasting the pudding. The moment the girl tasted the pudding with her spoon, she made a strong impact for just one frame. Her shoulders bounce wildly, and her hair and sleeves bounce upward. A cute reaction like a small shockwave. My cheeks turned red, and I pressed my cheek with one hand. Quickly switch to expressions of surprise, emotion, happiness, and satisfaction. 14.2–15.0 seconds: The final signature pose. Holding a plate with pudding in one hand while holding one hand to her cheek. She narrowed her eyes and smiled happily. My body came to a complete halt. Only her hair, sleeves, and hem of her clothes swayed gently in the afterglow. The camera leans in slightly, focusing on her happy expression. Finish with a cute and satisfying finishing piece. The camera uses ultra-wide, sharp zoom, low angle, light Dutch angle, sharp shots, and short cut-ins. When discovering pudding, teleporting, making sudden stops, or tasting it, the camera is brought close. However, the positions of the characters' faces, pudding, and island counters are always clearly visible.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `61.05s`

---

### 🎬 Cherry Blossom Farewell
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04208.jpg" width="480" alt="SD2_04208"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cherry-blossom-farewell-SD2_04208">🌐 Watch Online</a>

#### 📝 Prompt
```
Use @image1 as the permanent facial identity reference. Preserve the exact face, skin tone, makeup, eye shape, and expression in every frame. Only change outfit, hairstyle, accessories, pose, and body movement. Create a 15-second Makoto Shinkai-inspired cinematic anime sequence. A young woman enjoys a peaceful walk through a cherry blossom hill at golden hour. She accidentally steps on a hidden envelope, kneels to pick it up, and discovers her own name written in familiar handwriting. She quietly freezes for a moment, then walks to a large cherry blossom tree, opens the letter, and reads it. Tiny golden particles rise from the handwritten words like fading memories. She gently closes the letter, holds it to her heart, and stands beneath the tree as thousands of petals swirl around her while the camera pulls into a breathtaking aerial farewell shot. Style: Photorealistic anime, Your Name, Suzume, Weathering With You, warm golden-hour lighting, HDR, 4K, ultra-detailed backgrounds, cinematic depth of field, realistic cloth and hair physics, natural cherry blossom petal motion, smooth camera transitions, emotional storytelling, Joe Hisaishi-inspired orchestral atmosphere. Negative Prompt: No facial changes, no identity drift, no extra characters, no ghosts, no anatomy errors, no flicker, no camera shake, no harsh VFX, no oversaturated colors, no clipping, no unrealistic physics.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 One Disastrous Morning
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04207.jpg" width="480" alt="SD2_04207"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/disastrous-morning-SD2_04207">🌐 Watch Online</a>

#### 📝 Prompt
```
STYLE: High-end stylized 3D animated female character, cinematic lighting, expressive facial animation, polished materials, exaggerated but believable motion, comedic visual storytelling. CHARACTER: Young adult woman with expressive eyes and medium-length hair, maintaining consistent facial features throughout all shots. WARDROBE: Blue striped pajamas in shots 1–9. Dark business suit, white shirt, blazer, formal trousers or skirt, and dress shoes in shots 12–15. Final shot: still wearing the same rain-soaked business suit. ENVIRONMENT: Cozy bedroom, bathroom, kitchen, rainy street, bus stop, office, and dark bedroom in the final scene. MOOD: Chaotic, rushed, unlucky, comedic frustration, escalating panic, humorous mishaps, ending in emotional defeat. STORY FLOW: She wakes up late when her alarm rings, rushes out of bed in panic, gets ready as fast as possible, discovers there's almost nothing in the refrigerator, quickly grabs breakfast, brushes her teeth while multitasking, spills water, struggles to get dressed, runs through heavy rain to catch the bus, arrives late at work, gets scolded by her boss, and finally returns home exhausted, collapsing onto her bed. Maintain consistent character appearance, outfit continuity, cinematic framing, expressive acting, and Pixar-quality 3D animation across every storyboard panel.
```

#### 📌 Details
- Ratio: `0.75` | Duration: `14.94s`

---

### 🎬 Morning Breakfast Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04206.jpg" width="480" alt="SD2_04206"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/morning-breakfast-vlog-SD2_04206">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a photorealistic, cinematic lifestyle vlog featuring a **22-year-old female influencer** in a bright, modern apartment kitchen during golden morning light. The video should feel like it was casually filmed on a high-end smartphone with natural handheld camera movement, subtle autofocus shifts, realistic lighting, authentic kitchen sounds, and believable facial expressions. Maintain the same character throughout the entire sequence. **Scene 1 (0–3s):** She walks into the kitchen wearing an oversized cream sweatshirt and grey lounge shorts, smiling at the camera while opening the refrigerator. She grabs eggs, milk, butter, yogurt, berries, granola, and coffee beans. **Dialogue:** "Come make breakfast with me... I'm starving." **Scene 2 (3–6s):** Close-up of butter sizzling in a pan as she cracks two eggs with one hand. She gently stirs them into fluffy scrambled eggs while steam rises naturally. **Dialogue:** "Scrambled eggs are non-negotiable." **Scene 3 (6–9s):** She pours pancake batter onto a hot pan, flips a golden pancake in one smooth motion, then laughs after catching it perfectly. **Dialogue:** "Okay... that flip was actually kind of impressive." **Scene 4 (9–12s):** She assembles a yogurt bowl with thick Greek yogurt, crunchy granola, fresh strawberries, blueberries, banana slices, and a drizzle of honey. Quick macro shots capture the textures and movement. **Dialogue:** "This might be my favorite part." **Scene 5 (12–15s):** She pours a fresh cup of coffee, carries everything to a sunny dining table, sits down, takes a bite of pancake, then a sip of coffee while smiling at the camera. **Dialogue:** "Breakfast is served. Hope you have the best day." **Style Notes:** Ultra-realistic, premium influencer aesthetic, natural skin texture, soft morning sunlight through windows, cozy neutral kitchen, realistic food textures, shallow depth of field, smooth handheld camera, subtle cinematic motion blur, authentic ambient sounds (sizzling pan, coffee pouring, utensils, birds outside), warm color grading, 4K quality, highly detailed, TikTok/Instagram Reel lifestyle vlog, seamless continuity, no jumpy character changes, natural lip-sync matching dialogue.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

### 🎬 Sweaty Morning Walk Through Korean Village
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04205.jpg" width="480" alt="SD2_04205"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sweaty-korean-village-morning-walk-SD2_04205">🌐 Watch Online</a>

#### 📝 Prompt
```
**SCENE** Seedance 2.0 slice-of-life, 15 seconds. @ image1 = Main Subject. Preserve exact face, hairstyle, features, skin tone, and body proportions throughout. **OUTFIT:** Oversized olive sleeveless linen shirt loosely tucked into wide-leg dusty burgundy trousers, flat brown leather sandals, small gold hoop earrings. Shirt naturally damp/sweat-stained at collar, underarms, chest. Hair loosely down, natural waves, few strands sticking to face and neck. Completely unglamorous. **LOCATION:** Authentic traditional Korean rural village. Dirt/gravel paths. Mossy stone walls. Hanok houses with aged clay tile roofs. Wooden fences. Overgrown grass. Gnarled old trees. Stone water basin. Hanging dried chili peppers. Cracked stone steps. Ceramic facial jars. Free-roaming roosters. Morning cooking smoke. Dense hillside vegetation. Zero modern elements. **CAMERA:** Late-2000s flip cam vlog. Heavy handheld shake. Imperfect reframing. Subject frequently off-center or cropped. Aggressive autofocus hunting. Lens breathing. Strong exposure swings. Rolling shutter. Heavy motion blur. Warm faded washed-out muddy tones. Blown highlights. Crushed blacks. Heavy digital noise and compression artifacts. Maximum home-video imperfection. --- **00:00–00:02** — Mossy stone wall path. Loose sweaty arm's-length self-shot. Woman smiles tiredly, speaks casually to lens while walking. Weeds brush past. Camera tilts mid-walk. **00:02–00:04** — Hanok courtyard. Handheld from behind. Woman walks through; stray dog trots alongside. Jangdok jars along wall. Morning smoke drifts low. **00:04–00:06** — Stone water basin. Handheld close. Woman crouches, splashes cool water on sweaty face and neck, exhales with relief, laughs softly. Focus hunts aggressively. **00:06–00:08** — Gnarled tree, stone wall. Low handheld. Woman crouches, hand-feeds stray dog. Camera breathes between her face and the dog. **00:08–00:10** — Village path. Handheld side tracking. Woman walks slowly, wipes sweat from forehead, glances around. Rooster crosses ahead. Camera sways, reframes late. **00:10–00:12** — Shaded hanok exterior, stacked ceramic pots. Woman sits on cracked stone step, sips from battered tin cup. Shirt visibly damp. Elderly woman moves in background. Breeze lifts hair. **00:12–00:15** — Dirt path near gnarled tree. Self-shot. Woman raises camera to sweaty face, laughs tiredly, speaks casually, gives small wave. Recording cuts abruptly mid-moment. --- No posing. No fashion look. No perfect composition. No stabilization. No cinematic glamour. No modern grading. No music. **AUDIO:** Morning birds, roosters, distant village chatter, dog, water on stone, crackling fire, footsteps on dirt, rustling leaves, wind, ceramic sounds. **16:9.**
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Pixar Style Female Firefighter
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04204.jpg" width="480" alt="SD2_04204"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pixar-female-firefighter-SD2_04204">🌐 Watch Online</a>

#### 📝 Prompt
```
Use the attached THE FIREFIGHTER storyboard image as the exact reference. Create a 12-second 16:9 animated firefighting sequence that follows the 8-shot storyboard exactly. Preserve the same Pixar-style strong brave female firefighter, full
```

#### 📌 Details
- Ratio: `0.75` | Duration: `15.08s`

---

### 🎬 Ancient Beauty's Silent Gaze
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04203.jpg" width="480" alt="SD2_04203"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ancient-beauty-silent-gaze-SD2_04203">🌐 Watch Online</a>

#### 📝 Prompt
```
Reference image video · Seedance 2.0 · 4K · Portrait 9:16 · 15 seconds · Pure Eye Expression Facial Scenes · Zero Lines · Ultimate Live Performance Character Reference CHARACTER REF (=upload setting image, lock character image): ancient-style beauty, black hair with high buns and curled long hair hanging down, gold-inlaid gemstone floral crown + pearl tassel dangling, bare shoulders pink floral embroidered strapless long dress, light pink tulle over top, long tassel earrings. Facial features, makeup, hair accessories, and clothing must be 100% consistent with the reference images throughout; no deformation or face swapping allowed. Vertical composition: 9:16 vertical format, with the subject's face centered slightly upward, leaving breathing room, suitable for close-ups and dual-eye macros, with background blurred above and below. SCENE (newly generated): A quiet courtyard waterside pavilion, behind a half-sheer gauze curtain, distant flower shadows hazy, warm dusk light slanting in, dust drifting in the beam of light, a gentle breeze stirring the gauze curtains and hair. Quiet, elegant, and open space. Core of performance: pure eye contact + facial expressions, zero lines, no narration, zero subtitles throughout—all emotions are expressed through the slightest movements of the eyes, eyelashes, brows, nose, and lips. Queen-level live-action performance: all the drama is on the face, the subtext is in the eyes. Real skin is fine and breathing fluctuates, blinking rhythms are irregular, eyes move first, head follows, micro-expressions convey an "imperfect realism," lively yet natural, with no plastic AI vibe. Storyboard script (emotional progression, no lines, mainly vertical close-up): SHOT 1 \| 0-2.5 sec \| Medium Close-up of Face (vertical composition) Slightly lowered eyes, gaze falls into the empty space before the eyes, eyes calm and absent-minded, eyelashes tremble slightly, lips parted and gently pursed, breathing visible. SHOT 2 \| 2.5-5.5 sec \| Close-up of Eyes macro Eye waves shift from still, pupils shift subtly as if reminiscing, a gentle warmth first rises in the eyes, and the corners of the mouth soften almost imperceptibly—emotion rises only in the eyes, the face barely moves. SHOT 3 \| 5.5-8.5 seconds \| Close-up of the face A sudden sting flashes through the warmth, her eyes tremble slightly, tears glisten in her eyes, her brows furrow and relax, nostrils twitch, and she struggles to keep her emotions from escaping. SHOT 4 \| 8.5-11.5 seconds \| Close-up of both eyes macro Tears swirl in her eyes but never fall; she slowly closes her eyes for a moment, and when she opens them again, vulnerability is fully embraced—this is the film's most restrained emotional explosive moment. SHOT 5 \| 11.5-15 seconds \| Back to Face Medium Close-up (Freeze Frame) Slowly lift your eyes to look out of the frame, your gaze soft, gentle, and slightly bright. A faint, relieved yet slightly wistful smile forms at the corner of your lips. Your lips move slightly, then quickly withdraw (wanting to speak but pause), finally freezing in a cool, gentle, slightly melancholic mood—your gaze still 'speaking,' and the scene has already gone still. Camera: Vertical handheld with very slight breathing sensation, multi-shot—alternating between mid-close and binocular macro shots on the face; Switching to match the emotional rhythm, shallow depth of field, blurred shadows of the background curtain, occasional subtle breath-like refocusing, always keeping the eyes and face in check. Atmosphere & Light: Warm light at dusk, soft warmth tones, light beams floating dust, grainy film shots, soft highlights without exposure; The gauze curtains, stray hair, and pearl tassels move gently with the light airflow, leaving the painting with a faint flow to avoid dead silence. CONSTRAINTS: - 4K ultra HD, vertical screen at 9:16, 15 seconds, characters match reference images (no camera changes, no faces, no costumes) - Zero lines, no narration, zero subtitles throughout—pure eye contact and facial expressions - Emotions build up layer by layer (mesmerized→ gentle memories→ painful tears→ restrained → letting go but holding back) - Queen-level live-action filming: real skin, irregular blinking, eyes moving before turning, tears stay in the eyes - Eliminate AI flavor: no excessive skin smoothing, excessive symmetry, excessive smoothness, Plastic masks, stiff and dull – avoid glowing eyes and abnormal pupils; Tears are truly restrained - storyboard transitions closely match the emotional beat, no frame skipping or flickering - the ending naturally freezes with a hesitant expression, no black screen, no transitions - no subtitles, no watermarks, no marks, no text
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.03s`

---

### 🎬 Female Assassin Cliff Leap
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04202.jpg" width="480" alt="SD2_04202"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/female-assassin-cliff-leap-SD2_04202">🌐 Watch Online</a>

#### 📝 Prompt
```
SECTION 1 (0–15s) — The Hunt A moonlit forest covered in mist. A skilled female assassin, Rin, sprints through the trees with incredible speed while armed soldiers chase her. The camera switches between close-ups of her determined eyes, her boots hitting the ground, and the pursuers crashing through branches. Enemy: "There she is! Don't let her escape!" Commander (radio): "Cut her off! She can't get far!" Earpiece: "Rin, they're surrounding you. Head for the cliff!" Rin (calmly): "I'm counting on it." She accelerates deeper into the forest. SECTION 2 (15–30s) — The Fight Two enemies suddenly block her path. She stops instantly. The forest falls silent for a moment. Enemy: "It's over. Drop your weapon." Rin gives a faint smile. Rin: "You should've stayed out of my way." An intense fight erupts. She dodges a knife, disarms one attacker, throws him into a tree, spins behind the second, and knocks him unconscious with a precise strike. More enemies rush in from every direction. Commander: "Move! She's heading for the cliff!" Rin glances ahead and starts running again SECTION 3 (30–45s) — The Final Leap Rin reaches the edge of a towering cliff overlooking a violent ocean. Dozens of armed soldiers surround her with rifles aimed. Commander: "You're out of options. Surrender." Rin slowly turns to face them, completely fearless. Rin: "You think this is the end..." She steps backward toward the edge. Rin: "...this is only the beginning." She leaps off the cliff in slow motion. The soldiers rush to the edge and look down. A huge splash echoes through the night. The water below slowly turns crimson red, spreading across the waves. The commander whispers, Commander: "...What have we done?" Cut to black.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `42.13s`

---

### 🎬 Milkshake Maker Storyboard Poster
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04201.jpg" width="480" alt="SD2_04201"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/milkshake-maker-storyboard-SD2_04201">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a crisp, clean infographic storyboard poster for THE MILKSHAKE MAKER. Wide 16:9 layout, white background, black borders, bold black typography, premium Pixar 3D stylized rendering, bright vivid colors — creamy vanilla white, vivid red cherry, pure white
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Premium Matte Black Earbuds Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04200.jpg" width="480" alt="SD2_04200"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/matte-black-earbuds-ad-SD2_04200">🌐 Watch Online</a>

#### 📝 Prompt
```
A hyper-visual, 16:9 fast-paced 10-second cinematic AI product commercial for premium matte black wireless earbuds, structured with four high-energy, seamless match-cuts. [0-2s] Lifestyle: A low-angle, tracking shot of a sharp, stylish young man walking through a moody, rainy cyberpunk city at night; vibrant neon signs create an ultra-blurred background bokeh while he glances down at a glowing smartphone screen, wearing a sleek earbud. [2-5s] Size & Portability: A top-down, geometric overhead flat-lay on a dark, wet obsidian stone texture. A seamless hard-cut reveals the earbuds precisely arranged alongside a modern smartphone, minimalist carbon-fiber wallet, and a luxury key fob, hit by a dramatic side-shadow. [5-8s] Packaging: An explosive, fast macro-zoom onto a floating, deep-black holographic retail box. The premium packaging performs a rapid 360-degree spin against an abstract, smoky dark background with glowing edge highlights. [8-10s] CTA: A perfectly symmetrical, ultra-close-up hero shot. The dual earbuds float and rotate in mid-air just above their open charging case, illuminated by a brilliant anamorphic lens flare and moody studio rim-lighting. Aesthetic: High-end tech commercial, 8k resolution, photorealistic textures, crisp anamorphic lighting, and snappy, seamless jump-cut transitions.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.0s`

---

### 🎬 Flirty Hallway Selfie Tease
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_04199.jpg" width="480" alt="SD2_04199"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/flirty-hallway-selfie-SD2_04199">🌐 Watch Online</a>

#### 📝 Prompt
```
The exact face, features, hairstyle, body proportions, and temperament are fully preserved in the reference images. The main subjects are real adult East Asian women, with the outfit strictly following the beige spaghetti strap pencil skirt shown in the picture. The fabric is lightweight and close-fitting, with a slight glow on the skin. Realistic indoor light film texture, with slight natural handheld phone selfie shake, natural recomposition, slight shaking, and clear and delicate skin texture. 00:00-00:02 Maintaining a squatting selfie angle, she first gently raised her index finger to her lips in a "shh" silence gesture, playfully looking at the camera, a slight smile at the corner of her mouth, and the camera trembled naturally. 00:02-00:05 Naturally turned her head to glance at the corridor behind her, as if checking if anyone was there. Her movements were light and natural, her long hair swaying as she held the camera and turned her head in a natural way. 00:05-00:10 Quickly turns back to face the camera, a more obvious mischievous smile at the corner of her mouth. The hand that doesn't hold the phone gently tugs at the edge of her shirt, making a suggestive tugging gesture (not exposing exposure), with a slightly teasing gaze, a mischievous grin, the action lasts 2-3 seconds, then slowly loosens the shirt, finally a playful wink smile, holding the camera with a slight tremor that naturally ends. Natural environment sounds: Quiet indoor corridors include slight footsteps echoing, breathing, faint rubbing of clothes, and low air conditioning rumbling in the distance. Overall, the atmosphere is quiet and ambiguous, with no music.
```

#### 📌 Details
- Ratio: `0.57` | Duration: `10.08s`

---

<!-- STATS_END -->
