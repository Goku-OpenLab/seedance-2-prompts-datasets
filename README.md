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
- Total Prompts: **2898**
- Updated Today (UTC 2026-05-14): **163**

## 🎬 Today's Updates
### 🎬 Turquoise Dream Catwalk Fantasy
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02917.jpg" width="480" alt="SD2_02917"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/turquoise-dream-catwalk-fantasy-SD2_02917">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a luxurious 15-second cinematic fantasy video in vertical 9:16. A glamorous Western woman with long dark curly hair, glowing skin, and elegant makeup wears a shimmering neon turquoise sequined mini dress. She holds a fluffy Persian cat with emerald-green eyes and a matching turquoise jeweled bow. Both are posed inside an ornate turquoise crystal picture frame against a dark teal background with sparkling bokeh and floating glitter. 0–3s: Static portrait like a living painting. 3–6s: The painting comes to life—she smiles, strokes the cat, and the cat blinks and looks around. 6–9s: Turquoise particles burst as she steps out of the frame with a dramatic hair flip. 9–12s: Quick fashion cut scenes: twirl, close-up of shimmering dress, playful cat interaction. 12–15s: Final runway-style hero pose with swirling sparkles and the glowing frame behind. Style: photorealistic, magical luxury aesthetic, high-fashion editorial, cinematic lighting, realistic fur and fabric textures, 35mm film look, ultra-detailed 8K.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.0s`

---

### 🎬 Warrior Queen Rides Through Dark Realm
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02916.jpg" width="480" alt="SD2_02916"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/warrior-queen-dark-realm-SD2_02916">🌐 Watch Online</a>

#### 📝 Prompt
```
A highly cinematic 15-second ultra-realistic fantasy sequence featuring a fearless warrior queen riding a massive black stallion across a war-torn dark realm. The scene opens with a sweeping aerial establishing shot of a ruined kingdom beneath violent storm clouds, flashes of lightning revealing shattered towers, burning siege weapons, drifting ash, and rivers of smoke across the battlefield. Rain and embers swirl through the air as distant explosions illuminate the horizon. The camera transitions into a fast dynamic tracking shot alongside the rider as the horse charges through mud and fire at full speed, its armor rattling while the warrior’s tattered cloak whips violently in the wind. Lightning briefly reflects across her engraved armor and determined expression. Cut into a dramatic low-angle slow-motion sequence where the horse leaps over collapsing debris and flaming wreckage while monstrous shadow creatures emerge from thick smoke around her. A cinematic close-up captures the warrior drawing a glowing enchanted sword infused with supernatural energy, fiery reflections burning within her eyes. The soundtrack intensifies as rapid action shots show her slicing through dark entities while galloping, sparks, magical particles, and explosive energy bursts scattering through the storm with hyper-realistic motion blur and cinematic impact. The final moments pull into an epic aerial pullback shot as she rides deeper into the battlefield surrounded by an advancing army of demonic creatures. Massive lightning strikes crash behind her, illuminating the chaos in dramatic flashes. Volumetric fog, anamorphic lens flares, seamless camera transitions, film-grade color grading, realistic environmental physics, and stunning 4K cinematic realism create an intense dark fantasy atmosphere from beginning to end.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.23s`

---

### 🎬 Neon Nightmare: Bowling Alley Horror
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02915.jpg" width="480" alt="SD2_02915"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/neon-nightmare-bowling-alley-horror-SD2_02915">🌐 Watch Online</a>

#### 📝 Prompt
```
High-tension horror sequence inside a neon-lit bowling alley at night. Retro arcade lighting, reflective bowling lanes, colorful LED glow, realistic practical lighting. Shot 1 (0–3s): A young woman stands frozen near the bowling lane holding a bowling ball. Her breathing becomes uneasy. Around her, she suddenly sees massive insect-like creatures crawling across the bowling alley walls and ceiling—giant spiders moving between neon signs and hanging lights. People nearby appear distorted and unaware. Shot 2 (3–5s): One insect crawls rapidly across the lane toward her. She panics— Then suddenly snaps out of it. Everything is normal again. Just a regular bowling alley. Her friends laugh and wave at her from behind. Shot 3 (5–8s): Still shaken, she slowly steps forward and rolls the bowling ball down the lane. The camera tracks low beside the ball as it spins toward the pins. Shot 4 (8–11s): As the ball nears the pins, she suddenly hears the disturbing insect clicking sound again. Her smile fades. From the empty lane beside hers— something rapidly moves in the darkness. Shot 5 (11–15s): A gigantic insect creature suddenly bursts out from the side lane, skittering violently across the polished floor toward the group. Everyone starts screaming and stumbling backward. The creature launches directly at the woman.
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.08s`

---

### 🎬 Laundromat Horror: Creature Attack
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02914.jpg" width="480" alt="SD2_02914"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/laundromat-horror-creature-attack-SD2_02914">🌐 Watch Online</a>

#### 📝 Prompt
```
High-tension horror sequence inside a brightly lit 24-hour laundromat at night. Rows of industrial washing machines, fluorescent lighting, reflective tiled floor, vending machines humming softly. Sound: washing machine hum, distant traffic outside, phone scrolling taps, slowly interrupted by violent metallic banging. Shot 1 (0–3s): A young woman sits alone in the laundromat scrolling on her phone while several washing machines run behind her. Suddenly— All the machines begin vibrating unnaturally at the same time. Coins rattle. Lights flicker slightly. She slowly looks up. Shot 2 (3–6s): The vibrations intensify into loud metallic BANGS from inside the machines. One machine violently shakes side to side. Then another. Green-tinted water suddenly begins leaking out beneath the doors, spreading across the floor. She stands up nervously: “What… what is happening?” Shot 3 (6–9s): The camera slowly circles around her as more machines begin slamming violently from inside. The laundromat now echoes with distorted screeching noises mixed with the banging. Green liquid floods across the tiles. Shot 4 (9–12s): One washing machine door suddenly POPS open. A grotesque wet creature crawls out. Then another machine opens. Then another. More creatures emerge one by one from different machines around her, dripping green slime onto the floor. She slowly backs away in panic as the camera continues orbiting around her. Shot 5 (12–15s): All the creatures suddenly stop moving. Silence for half a second. Then every creature simultaneously SCREAMS and charges toward her from every direction across the laundromat. She panics and stumbles backward— the creatures leap— cut to black.
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.08s`

---

### 🎬 Neon Rooftop Chase Action Sequence
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02913.jpg" width="480" alt="SD2_02913"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/neon-rooftop-chase-action-sequence-SD2_02913">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-realistic cinematic action sequence, 15 seconds, multiple rapid cuts. A fierce, determined woman in a weathered trench coat sprints across a rain-slicked rooftop at night, 40 stories above a glowing neon city. Shot 1 [0–2s]: Extreme macro close-up of her eye snapping open, iris dilating, red emergency light reflected in pupil, sweat on brow, shallow depth of field, micro handheld tremble. Shot 2 [2–4s]: Ultra-wide low-angle drone shot — she drops from a ventilation shaft, coat billowing in slow motion, thick fog below, city bokeh lights, anamorphic lens flare. Shot 3 [4–6s]: Fast lateral tracking shot, Dutch angle, she pivots and sprints toward the rooftop ledge as three armed operatives appear behind her, shallow focus, operatives blurred in background. Shot 4 [6–8s]: 120fps phantom slow-motion close-up — her bare hand grips a fraying steel cable, knuckles white, bullet spark grazes cable, golden practical light burst, cinematic motion blur. Shot 5 [8–10s]: Aerial vertigo drone plunge — she swings off the ledge into freefall between two glass skyscrapers, city grid glowing below, dramatic pullback reveal, pure cinematic vertigo. Shot 6 [10–12s]: Side-angle medium shot — she crashes onto a glass skylight, spider-web cracks radiate outward in real-time, she rolls and continues without pause, practical shatter effect, dust particles. Shot 7 [12–14s]: Slow push-in over-shoulder shot — she glances back once, jaw set, eyes cold and certain, city fog drifts through frame. Shot 8 [14–15s]: Smash cut to black as she enters a dark stairwell, door slams shut. Photorealistic, 8K, anamorphic 2.39:1 widescreen, teal-orange color grade, crushed blacks, desaturated highlights, practical neon bounce lighting, red emergency practicals, Dolby Vision HDR, rain practical FX throughout, wet surfaces with specular reflections, cinematic sound design.
```

#### 📌 Details
- Ratio: `1.77` | Duration: `15.1s`

---

### 🎬 Alien Home Invasion Horror Chase
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02912.jpg" width="480" alt="SD2_02912"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alien-home-invasion-horror-chase-SD2_02912">🌐 Watch Online</a>

#### 📝 Prompt
```
High-tension sci-fi horror sequence inside a modern house at night. Dim warm lighting, long hallways, polished floors, soft rain outside. Large translucent curtains move gently from the wind. Shot 1 (0–3s): A man and woman stand frozen inside the living room. The man grips a handgun tightly, staring toward a massive window covered by thin translucent curtains. Outside the curtain— a huge distorted silhouette slowly moves. Shot 2 (3–5s): Suddenly the curtain EXPLODES inward. A massive alien creature crashes through the glass. The man fires instinctively but gets knocked backward onto the floor. The woman screams and runs. Shot 3 (5–9s): The creature chases her aggressively through the house. She sprints down a corridor, slips around corners, races down stairs while the creature crawls rapidly along walls and ceiling behind her. Furniture gets smashed as it pursues her. Shot 4 (9–12s): She stumbles into a downstairs room— dead end. She falls backward against the wall. The creature slowly crawls closer toward her across the floor, towering over her. Its face comes inches from hers. She freezes in terror. Shot 5 (12–15s): A loud GUNSHOT. The creature jerks violently and collapses sideways beside her. Smoke drifts in the doorway. The man stands there holding the gun, breathing heavily.
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.08s`

---

### 🎬 Robotic Dinosaur Attacks Cyberpunk City
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02911.jpg" width="480" alt="SD2_02911"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/robotic-dinosaur-attacks-cyberpunk-city-SD2_02911">🌐 Watch Online</a>

#### 📝 Prompt
```
Enormous robotic dinosaur attacking a cyberpunk city at midnight, neon holograms everywhere, futuristic military fighting back, cinematic sci-fi movie scene, sparks, explosions, dramatic lighting, ultra realistic metallic textures, epic action atmosphere
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.1s`

---

### 🎬 Lone Soldier in Destroyed Spaceship
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02910.jpg" width="480" alt="SD2_02910"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/lone-soldier-destroyed-spaceship-SD2_02910">🌐 Watch Online</a>

#### 📝 Prompt
```
Lone space soldier walking inside a destroyed futuristic spaceship, red emergency lights flashing, cinematic sci-fi atmosphere, floating debris in zero gravity, ultra realistic, dark movie scene, dramatic camera movement, emotional futuristic vibe
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.1s`

---

### 🎬 Alien Lab Escape: Sci-Fi Horror
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02909.jpg" width="480" alt="SD2_02909"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alien-lab-escape-sci-fi-horror-SD2_02909">🌐 Watch Online</a>

#### 📝 Prompt
```
High-tension sci-fi horror sequence inside a futuristic underground laboratory at night. Sterile white lighting mixed with flashing emergency reds, reflective floors, glass containment walls, computer monitors, scattered scientific equipment. Sound: low electrical hum, distant alarms, glass creaks, creature growls. Shot 1 (0–2s): Inside a laboratory corridor, a nervous security guard holding a handgun stands beside a woman in a white scientist lab coat. Behind a massive translucent containment glass wall— a huge distorted creature silhouette slowly moves. The scientist stares nervously and whispers: “I think… it’s awake.” Shot 2 (2–5s): Suddenly the containment glass violently EXPLODES inward. A massive alien creature bursts through in a shower of sparks and shattered glass. The security guard fires once but gets slammed backward onto the floor. The scientist screams and runs. Shot 3 (5–9s): The creature aggressively chases her through the laboratory. She sprints past flickering monitors and overturned equipment while the creature smashes through glass partitions behind her. Warning alarms activate. Specimen tanks shatter as it crashes through the lab. Shot 4 (9–12s): She runs into a smaller lab chamber— dead end. She backs against a counter, trapped. The creature slowly crawls toward her across the floor and walls, towering over her. It lowers its face inches from hers and opens its massive jaws wide. Shot 5 (12–15s): A loud GUNSHOT echoes. The creature jerks violently and collapses beside her. Smoke drifts through the doorway. The security guard stands there holding the handgun with shaking hands. The scientist exhales deeply in relief while red emergency lights flash across the destroyed laboratory.
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.08s`

---

### 🎬 Dragon Roar at Mountain Summit
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02908.jpg" width="480" alt="SD2_02908"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dragon-roar-mountain-summit-SD2_02908">🌐 Watch Online</a>

#### 📝 Prompt
```
Single shot, static camera framing a wide cinematic composition on a mountain summit at dawn, initially slightly close to the man’s upper body, a man [Image1] stands centered facing the camera, wearing a white mountain jacket, wind gently moving the fabric and his hair, soft cold light illuminating his face while vast layered blue mountains and distant snowy peaks stretch behind him under a dramatic cloudy sky, subtle mist drifting across the valleys. As the shot begins, the camera slowly and subtly pulls backward (slow dolly out) to widen the frame, revealing more of the expansive mountain landscape behind him, then slowly begins to raise both arms outward and upward but only to about shoulder height, not forming a full V, movement controlled and deliberate. As his hands reach mid-level, a sudden powerful shockwave erupts in the distant mountain behind him — a massive explosion without fire, only a violent burst of dust, rock, and pressure rippling outward, sending debris and thick clouds into the sky, the camera subtly shakes from the impact, adding intensity. From within the expanding dust cloud, two enormous dragons emerge, their massive silhouettes forming through smoke and light, detailed scales catching the cold daylight, their bodies anchored firmly on the mountain peaks, claws gripping the rock, wings partially spread but not flapping, they remain completely stationary. The man holds his arms steady at that height, unmoving. The first dragon lifts its head and releases a thunderous roar, followed by the second dragon roaring even louder, each roar causing visible environmental vibration — dust trembling, clouds swirling — and the camera shaking more intensely with each roar. Suddenly, from deeper within the dust and ruined mountain, a third dragon — significantly larger and more imposing — bursts into view behind them, its presence overwhelming, it immediately unleashes a massive, dominant roar, the strongest yet, causing a heavier camera shake and intensified atmospheric distortion. All three dragons remain fixed in their positions on the mountain, unmoving and dominant, dust and mist continuing to drift around them, the man stands firm in the foreground with arms partially raised, wind and particles flowing around him as the scene holds its dramatic tension. No Music
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.1s`

---

### 🎬 Mother's Day Heartwarming Surprise
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02907.jpg" width="480" alt="SD2_02907"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/mothers-day-heartwarming-surprise-SD2_02907">🌐 Watch Online</a>

#### 📝 Prompt
```
A heartwarming cinematic Mother’s Day video. A mother wakes up early, prepares breakfast, gently wakes her child, helps with school clothes, hugs them before leaving. Transition to grown-up child surprising mother with flowers and a handwritten card. Soft golden morning light, emotional background music, slow-motion hugs, warm cozy home atmosphere, realistic facial expressions, cinematic camera angles, text overlay: “A mother’s love never fades. Happy Mother’s Day ❤️” 4K quality, emotional storytelling, vertical 9:16 format, 15 seconds.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.0s`

---

### 🎬 Storm Assault: Tactical Covert Op
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02906.jpg" width="480" alt="SD2_02906"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/storm-assault-tactical-covert-op-SD2_02906">🌐 Watch Online</a>

#### 📝 Prompt
```
Duration: 15 Seconds
Style: Hyper-Speed Cinematic Action • Futuristic Spy Thriller • Dark Tactical Couture
Format: Vertical 9:16 • UHD 8K • IMAX Handheld Camera • Dolby Atmos • Extreme Realism

A hyper-realistic military action sequence inside a Hercules cargo aircraft flying through a violent thunderstorm at night. Extreme turbulence shakes the aircraft with realistic physics. Red emergency lights flash rapidly. Volumetric smoke fills the cabin. Blue-orange cinematic lighting creates a high-contrast futuristic battlefield atmosphere. Hyper-detailed VFX, motion blur, lens distortion, and dynamic IMAX handheld camera movement enhance the intensity and chaos.

MAIN CHARACTER:
A highly trained female covert operative in black tactical couture, calm and focused presence, extremely agile hand-to-hand combat specialist executing fast, precise tactical combat.

0–2 SEC: Inside Hercules aircraft shaking violently in a storm. Red emergency lights flash. Close-up on boots stepping on metal floor camera tilts up revealing her cold focused face. Armed agents slowly surround her.

2–4 SEC: First attack begins. She moves at hyperspeed. Whip-pan camera follows. Spinning heel kick knocks first agent into wall. Sparks and debris in slow motion.

4–6 SEC: Rapid close combat. She performs Wing Chun + cyber ninja strikes. Multiple enemies are defeated in fast cinematic combinations. Camera rotates aggressively in tight corridor.

6–8 SEC: Gunshot fired. She dodges bullet in ultra slow motion, disarms attacker, delivers knee strike, throws him toward cargo door. Alarm intensifies, chaos rises.

8–10 SEC: Rear cargo door opens violently. Storm wind rushes inside. She fights final agents near the open edge. Lightning flashes create dramatic silhouettes.

 10–12 SEC: Final enemy defeated with spinning kick, thrown out of aircraft. She immediately jumps into the storm night sky in epic slow motion.

12–14 SEC: Freefall above clouds. Parachute deploys dramatically. Her outfit flows in extreme wind. Calm, controlled, deadly expression under lightning sky.

 14–15 SEC: She throws a grenade toward the Hercules. Massive mid-air explosion destroys the aircraft. 

Final shot: she floats under parachute with fireball and lightning storm behind cinematic assassin finale.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.14s`

---

### 🎬 Iced Kopi Susu with Harvestside & Diamond
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02905.jpg" width="480" alt="SD2_02905"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/iced-kopi-susu-harvestside-diamond-SD2_02905">🌐 Watch Online</a>

#### 📝 Prompt
```
UGC handheld video in an Indonesian home desk setup, hands-only casual creator style. Person shows a white Harvestside Arabica Instant Coffee pouch and a Diamond Fresh Milk carton clearly to camera, using the provided product images as faithful references for the coffee pouch and milk carton. Make iced kopi susu in a clear glass with visible ice on a cozy desk. Natural morning lighting, realistic phone camera, slight handheld movement, cozy bookshelf background, authentic Indonesian UGC, no studio look, no polished commercial lighting. Sequence for an 8-second 9:16 Seedance 2.0 video: First 1.5 seconds: hands hold both products close to camera with readable labels. Next 2 seconds: the Harvestside coffee pouch is standing upright on the desk, opened neatly at the resealable zip top. A small spoon scoops instant coffee powder from inside the pouch and adds it into the clear glass with ice. Do not pour coffee directly from the pouch, do not tear or rip the pouch, and do not show the pouch as a drink container. Next 2 seconds: pour Diamond Fresh Milk from the carton into the glass, creating a creamy coffee swirl. Final 2.5 seconds: close-up of the finished iced kopi susu on the desk with both product packages beside the glass. Soft upbeat morning lo-fi music background, natural ambient home mood, clean wholesome beverage preparation. Keep product labels faithful to the reference images.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `8.08s`

---

### 🎬 First Dawn After Eternal Night
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02904.jpg" width="480" alt="SD2_02904"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/first-dawn-after-eternal-night-SD2_02904">🌐 Watch Online</a>

#### 📝 Prompt
```
A cinematic emotional sci-fi sequence set in a world trapped in eternal night. 0–3s: Silent, frozen city under permanent darkness. Streetlights flicker weakly. Snow-like ash falls gently through empty streets. People stand on rooftops staring at a black horizon. 3–6s: Close-up shots of exhausted faces—people holding onto each other, waiting. Radios crackle with static. A faint, unexplained vibration moves through the air. 6–9s: The sky begins to change for the first time in years. A thin, impossible line of warm orange light appears at the horizon. Birds suddenly take flight. Wind picks up. 9–12s: Emotional escalation—people drop to their knees, crying, laughing, shielding their eyes. The first rays of sunlight break through the darkness, touching buildings that haven’t seen light in years. 12–15s: Final wide cinematic shot. The sun rises fully over the world, flooding everything with golden light. Ice melts, shadows retreat, and the city slowly awakens in silence and awe. Style: ultra cinematic realism, emotional tone, soft golden volumetric lighting, slow-motion human reactions, high-detail environments, film-grade color grading, hopeful and transformative atmosphere.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 Emotional Confrontation in a Dim Kitchen
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02903.jpg" width="480" alt="SD2_02903"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/emotional-confrontation-dim-kitchen-SD2_02903">🌐 Watch Online</a>

#### 📝 Prompt
```
15s, cinematic emotional confrontation. Two characters @[chracter sheet ref] stand face-to-face inside a small apartment kitchen late at night. The room is dimly lit by a single warm overhead light and soft city lights leaking through the window. The atmosphere feels emotionally exhausted, tense and painfully intimate, like an argument that has been building for years. Modern cinematic realism, subtle handheld camera movement, shallow depth of field, soft film grain, emotionally restrained acting, realistic silence between dialogue lines. Beat 1: The emotional state remains at high arousal and medium-low valence. Camera: slow handheld side shot circling both characters tight over-the-shoulder close-ups brief eye-level two-shot showing emotional distance FACS Character A: AU4 + AU7 + AU17 Dialogue A: /juː ˈnev.ɚ ˈriː.ə .li lʊkt æt miː/ /juː wɚ ɔːlˌweɪz ˈsʌmˌwɛɹ ɛls/ Voice: tight restrained voice, controlled anger, uneven breathing Character A tries to stay calm while suppressing years of resentment. Beat 2: The emotional state gradually shifts toward very low valence and medium-high arousal. Camera: slow push-in toward Character B extreme close-up on trembling eyes and mouth wide static shot showing silence after the argument peaks FACS Character B: AU1 + AU4 + AU15 + AU25 Dialogue B: /aɪ wəz ˈtɹaɪ.ɪŋ maɪ bɛst/ /aɪ dɪdnt noʊ haʊ tə fɪks ˈɛv.ɹiˌθɪŋ/ Voice: breaking voice, unstable breath support, emotionally collapsing delivery Beat 3: The emotional state remains at very low valence and medium-low arousal. Camera: locked wide shot with silence between them slow close-up on both characters avoiding eye contact subtle rack focus between faces FACS Character A: AU1 + AU15 + AU17 Dialogue A: /ˈmeɪ.bi wiː stɑpt ˈlɪs.ən.ɪŋ ə lɔŋ taɪm əˈgoʊ/ Voice: emotionally exhausted, quieter delivery, fading anger replaced by sadness No exaggerated screaming, no violence, no comedy, no text overlay, no watermark.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.03s`

---

<!-- STATS_END -->
