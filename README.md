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
- Total Prompts: **7741**
- Updated Today (UTC 2026-07-12): **43**

## 🎬 Today's Updates
### 🎬 RENA Waiting Room Selfie Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10128.jpg" width="480" alt="SD2_10128"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rena-waiting-room-selfie-vlog-SD2_10128">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: 8K photorealistic — real phone-and-mirrorless vlog footage, no 3D render, no game engine, no anime. Format: Modern K-pop idol YouTube behind-the-scenes vlog — handheld selfie energy, quick punchy cuts, whip-pans and snap-zooms between shots. Lighting: Clean and flattering — vanity mirror bulb lights as key, soft white studio spill from the doorway, gentle bloom, K-beauty glow. High-key on the face, controlled elsewhere. Color: Chic monochrome palette. 60:30:10 — soft warm gray / deep black wardrobe / soft pink accent pop. Camera: Mix of front-facing phone selfie (slight wide-lens distortion, arm's-length) and handheld mirrorless. Natural micro-shake, quick reframes. 180-degree shutter motion blur. Skin: Pore-level realism with dewy K-beauty finish — vellus hair, subtle blush flush, glossy lips, real catch-lights in the eyes. Acting: Bubbly, natural idol-vlog energy — genuine smiles, playful micro-expressions, eye-contact with the lens, tiny laughs, chest rise from breathing. Never posed-frozen, always alive. Physics: Gravity and inertia respected — long hair bounce and sway, pleated skirt movement, correct contact shadows. No floating props. Composition: Centered selfie framing and rule-of-thirds handheld. Subject moving from frame one. Continuity: Same idol RENA, same outfit, same makeup, same waiting room across every cut. No identity drift. Technical: 24fps smooth motion, snappy vlog-paced editing, 8K detail, no jitter. Audio: Upbeat cheerful room tone. RENA speaks short natural Korean one-liners as written in each cut — bright, youthful female voice, casual vlog delivery, accurate lip-sync. Light, bouncy vlog energy. Characters: RENA — 20 year old K-pop idol, 166cm, slim 7-head proportions. Adorable cute-type visual: soft round face with full cheeks, big round sparkling dark brown eyes with aegyo-sal, small nose, dewy glass skin, coral-pink gradient lips, tiny beauty mark on her left cheek. Very long straight black hair past her chest, center-parted with thin face-framing strands. Pearl-and-silver drop earrings in both ears. Outfit: black ribbed knit top with an oversized pleated collar and a black ribbon tie, white shirt collar peeking at the neckline, black micro pleated skirt with a side belt buckle, black crew socks, chunky black platform loafers. Scene: An idol waiting room at an MV shooting studio, daytime. A vanity mirror ringed with warm bulb lights sits camera-left; a rolling clothing rack of garment bags stands behind, a gray couch with her phone and a small pink standing fan camera-right. The door to the bright studio hallway is upstage. RENA is alone, fully in hair and makeup, killing time before her set call — filming a behind-the-scenes vlog on her phone. Fast, cheerful, handheld throughout. CUT 1 (~2s) — Front-facing phone selfie, arm's length, slight wide-lens distortion: RENA pops in close to the lens with a bright grin and a quick finger-heart — long
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 Versailles Forbidden Kiss
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10127.jpg" width="480" alt="SD2_10127"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/versailles-forbidden-kiss-SD2_10127">🌐 Watch Online</a>

#### 📝 Prompt
```
45-second vertical short play, 9:16, cinematic feel, 18th-century French Palace of Versailles, ancient style, cinematic-quality light and shadow. Setting: The luxurious princess's bedroom at the 18th-century Palace of Versailles, France. Moonlight streams through tall floor-to-ceiling windows, and the interior is dominated by gold and deep red. Magnificent crystal chandeliers, red velvet sofas, and exquisite murals create a sense of luxury and romance. Roles: Male butler @Image1 : Around 35 years old, tall and broad-shouldered, handsome and steady, wearing a black blazer, black tank top, white shirt, black bow tie, tight black suit pants, white gloves, a white towel hanging from his left wrist, holding a silver plate in his right hand (with a crystal glass bottle of red wine and two glasses of red wine). French princess @Image2 : 22 years old, with gorgeous long golden curls, deep blue eyes, and a proud and beautiful expression, wearing a gold gown with luxurious lace patterns and an off-shoulder gown, holding a fan adorned with gold pendants and gold lace decorations. Style: Cinematic lighting, shallow depth of field, luxurious 18th-century French court texture, contrast of warm gold and cool blue moonlight, exquisite detail, romantic yet tense. First segment (0-15 seconds): 0-2s: Princess of Versailles Palace, moonlight pouring down as the princess lounges lazily on a luxurious red long sofa. 2-4s: The male butler enters the bedchamber carrying a silver tray. 4-6s: The princess impatiently taps the armrest of the sofa with her fan and says in English, "Why are you so late with my wine?" 6-8s: The male butler bows respectfully and responds in classical French: "Pardonnez-moi, Votre Altesse." 8-10s: The princess gently lifts the butler's chin with her fan, and their eyes begin to look at each other ambiguously. 10-12s: The male butler pours red wine into a glass and hands it to the princess. 12-15s: The princess takes the wine glass and gazes at him affectionately. 15-17s: The princess took a sip of red wine and said in English, "You're always late..." Enjoy teasing me?" 17-19s: The male butler approaches the princess and whispers in classical French: "Seulement pour vous voir rougir, ma Princesse." 19-21s: The princess chuckled softly, reached out to tug at the butler's bow tie, and pulled him closer. 21-23s: The male butler's gaze turns domineering, leaning close to the princess. 23-25s: The princess's breathing becomes increasingly uneven, softly saying in English: "You're being too bold tonight..." 25-27s: The male butler whispers in classical French: "Vous me rendez fou..." 27-30s: The two are very close and about to kiss, creating an extremely romantic atmosphere. 30-32s: The male butler bends down and kisses the princess deeply. 32-34s: He suddenly lifted the princess from the sofa in a princess carry and carried her to the big bed behind the sofa. 34-36s: The male butler gently presses the princess down on the bed, just about to continue kissing. 36-38s: A fierce dark gray pit bull suddenly bursts out from under the covers and bites the butler's suit jacket. 38-40s: The princess, pinned down by the butler's hands on the bed, loudly shouts at the pit bull in English: "You bad dog, STOP!" 40-42s: The male butler watched this scene and couldn't help but chuckle softly. 42-45s: The princess also chuckles softly, their eyes entwined, creating a romantic yet somewhat funny atmosphere, the scene freezes.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `43.93s`

---

### 🎬 Coffee Above Clouds Burj Khalifa
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10126.jpg" width="480" alt="SD2_10126"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/burj-khalifa-cloud-coffee-SD2_10126">🌐 Watch Online</a>

#### 📝 Prompt
```
Scene 1 (0–3s) An epic aerial drone shot reveals the Burj Khalifa rising above a sea of clouds at golden sunrise. The camera rapidly flies toward the rooftop. Scene 2 (3–7s) A beautiful young South Asian woman sits at a stylish rooftop café on the top of the Burj Khalifa, smiling as she lifts a coffee cup. Warm sunlight, gentle wind, and soft clouds create a magical atmosphere. Scene 3 (7–11s) As she takes a sip, the rooftop transforms into a luxurious floating sky café with glowing lights, elegant flowers, and cinematic particles. The camera smoothly circles around her while birds fly across the sky. Scene 4 (11–15s) The camera pulls back into a breathtaking wide drone shot, revealing the Burj Khalifa above the clouds with the Dubai skyline below. End with a premium cinematic finish, leaving the viewer in awe. Style: Ultra-realistic, IMAX cinematic, Netflix-quality, photorealistic, HDR, volumetric lighting, 8K, smooth camera motion, realistic face consistency, natural expressions, realistic hands, premium color grading, no glitches, no distortion, no extra limbs, viral social media aesthetic.
```

#### 📌 Details
- Ratio: `1.0` | Duration: `21.9s`

---

### 🎬 Forest Creature Hunt
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10125.jpg" width="480" alt="SD2_10125"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/forest-creature-hunt-SD2_10125">🌐 Watch Online</a>

#### 📝 Prompt
```
This is handheld documentary footage recorded on an early-2000s consumer DV camcorder by someone standing in a forest watching a boy try to capture a strange creature. The footage feels like real, imperfect home video of an unexpected wildlife encounter. A boy around 12 years old, wearing a red cap, blue jacket and shorts, is in a dense forest clearing. He is very excited and determined. In front of him, attached to a tree trunk at about eye level, is a large, green, cocoon-like creature with a hard segmented shell, small visible eyes and slight twitching movements. The creature looks completely real, like an unknown deep-forest insect or animal. The boy throws a small round object (like a ball) toward the creature while shouting encouragement. The object bounces off the hard green shell. The creature twitches and makes a small defensive movement. The boy picks up the object, adjusts his stance and throws again with more force. His friends can be heard shouting in the background. The boy looks thrilled when the creature reacts. The camera, held by one of the friends, moves unsteadily to follow the action. It shakes a lot when the boy throws and when the creature twitches. There are quick natural cuts between the boy’s face full of excitement, the creature on the tree, and the thrown object hitting the shell. The handheld camera shows constant shake, imperfect and drifting framing, frequent autofocus hunting, lens breathing, motion blur during throws, exposure changes between sunlight filtering through trees and shaded areas, and all the typical imperfections of an old DV camcorder. The person filming is clearly excited and moving around to get a better view. Natural sound only: forest ambience (birds, wind in leaves), the boy shouting excitedly, the sound of the thrown object hitting the hard shell, footsteps on leaves and twigs, and distant voices of other kids. No music. No sound design. The result must feel like authentic, raw home video of a group of kids in the forest encountering and trying to capture a bizarre real creature, captured on an old DV camcorder.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Fierce Vogue Fem Dance MV
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10124.jpg" width="480" alt="SD2_10124"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/vogue-fem-dance-mv-SD2_10124">🌐 Watch Online</a>

#### 📝 Prompt
```
The exact same character from the reference image @画像1 — 100% identical face, hairstyle, outfit, body proportions, no changes whatsoever, clean high-quality skin with subtle glow. She performs a fierce ballroom Vogue Fem dance break in an ultra-stylish environment that perfectly matches her specific aesthetic and original vibe. She executes rapid hand performance, complex geometric arm framing, striking precise poses, and sudden dramatic death drops, projecting explosive diva energy. Mind-blowing music video multi-cut camera work: starts with a rapid 360-degree orbit tracking shot around her, transitions with a fast whip-pan to an extreme low Dutch-angle looking up at her poses, followed by dynamic push-and-pull dolly movements tightly synced to her intricate hand frames. High-energy rapid editing. Cinematic color grading: dramatic high-contrast lighting designed to make her exact outfit pop, sleek environmental reflections, cinematic anamorphic lens flares, subtle film grain, high-end music video style. 4K, photorealistic, ultra-sharp skin and fabric details, intense rhythmic speed ramps synced to an imaginary heavy bass beat, hyper-fast whip transitions mixed with buttery slow-motion on her sharpest voguing poses, "ultra-dynamic high-end fashion music video masterpiece" optional, 24fps
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.12s`

---

### 🎬 Golden Hour in a Fishing Village
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10123.jpg" width="480" alt="SD2_10123"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/fishing-village-golden-hour-SD2_10123">🌐 Watch Online</a>

#### 📝 Prompt
```
Character: Young Japanese woman from @ Image 1, in her early 20s. Natural everyday appearance. She wears a loose beige knit cardigan over a white ribbed tank top, light blue relaxed-fit jeans, and worn brown leather loafers. She has simple silver stud earrings, shoulder-length straight black hair with soft bangs, realistic skin texture, light natural makeup, and a calm, reserved personality. Her identity, outfit, hairstyle, facial features, and overall appearance remain perfectly consistent throughout the entire video. Location: A real Japanese seaside fishing village during the peaceful golden hour at sunset. Narrow lanes leading to the harbor, weathered wooden houses, fishing nets hanging outside to dry, small flower pots by the entrances, bicycles parked along fences, concrete breakwaters, utility poles with overhead power lines, fishing boats in the distance, a gentle sea breeze, and warm sunset reflections in the windows. There are no tourist attractions, restaurants, advertisements, crowds, or commercial activity. Visual Style: Ultra-realistic observational documentary. A quiet slice-of-life narrative that captures authentic everyday human behavior. Natural pacing, rich environmental details, genuine imperfections, and emotions conveyed through subtle facial expressions rather than performance. Cinematography: Late-1990s MiniDV home camcorder aesthetic, as if casually filmed by a friend or family member documenting ordinary life. Continuous handheld camera shake, unstable framing, occasional accidental zoom adjustments, autofocus breathing, subtle tape compression artifacts, faint interlacing, soft highlight blooming, faded colors, slight chroma noise, imperfect white balance, rolling shutter ("jello") effect, occasional dropped frames, no gimbal, no cinematic camera movement, and no modern color grading. 00:00–00:02 Outside a weathered wooden house facing a quiet alley. She opens the front door while carrying a small watering can and gently waters the potted plants by the entrance. The camera begins recording slightly too early, briefly pointing at the ground before finding her. 00:02–00:04 She slowly walks toward the narrow alley leading to the harbor. A bicycle quietly passes in the background. The camera operator lags slightly behind, resulting in loose framing and gentle handheld shake. 00:04–00:06 She stops beside a low concrete breakwater, gazing at the gentle waves while seagulls glide overhead. The sea breeze softly moves her hair. Autofocus repeatedly shifts between her side profile and the distant fishing boats. 00:06–00:08 She bends down to pick up a smooth seashell along the shoreline, quietly examines it, then smiles softly to herself. Warm sunlight reflects across the water as the camera exposure subtly fluctuates. 00:08–00:10 She sits on a wooden bench overlooking the harbor, holding a warm canned tea she bought earlier from a convenience store. She quietly watches the fishing boats
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.2s`

---

### 🎬 Epic Ice Angel Transformation
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10122.jpg" width="480" alt="SD2_10122"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ice-angel-transformation-SD2_10122">🌐 Watch Online</a>

#### 📝 Prompt
```
Cinematic epic fantasy transformation sequence, 14 seconds, ultra-detailed, dramatic lighting, golden hour sunbeams and god rays piercing through a majestic frozen kingdom with towering ice castles, shattered crystal structures, frozen stairways, towering glaciers, sparkling snow, icy cliffs, and shimmering frost-covered landscapes. 0–3s: A beautiful woman with long brown hair, wearing black leggings and a white crop top, desperately falls from a great height onto a cracked frozen ice floor while tightly holding a fluffy white snow wolf cub in her arms. She lands hard, snow and ice fragments burst into the air, and she looks frightened yet fiercely protective of the snow wolf cub. 3–6s: Medium shot. She kneels on the frozen steps of the icy kingdom while holding the snow wolf cub. She picks up a glowing golden crystal that radiates brilliant divine light in her hand. Close-up of her worried face with red lips and a small wound on her forehead. The snow wolf cub looks curiously at the crystal as she stares at it with determination. 6–9s: Dramatic power awakening. Her eyes begin glowing with brilliant golden light as she releases a powerful scream. Divine golden energy erupts around her, creating a massive magical shockwave. Her casual clothes transform into magnificent white-and-gold angelic armor with intricate engravings, ornate shoulder plates, glowing chest emblem, elegant gauntlets, and divine detailing. The white snow wolf cub remains calmly in her arms, surrounded by radiant energy. 9–12s: Full heroic transformation. Massive glowing white angel wings burst from her back as swirling golden energy, magical particles, and divine chains fill the air. Two radiant energy swords materialize in her hands. The white snow wolf cub dramatically transforms into a majestic armored snow wolf, much larger and more powerful, with glowing golden eyes, brilliant white fur, ornate golden armor, and luminous frost markings. Epic low-angle shot as she stands proudly beside the giant snow wolf on the frozen kingdom steps, both prepared for battle while icy winds blow through her hair, intense lens flares shimmer across the ice, and magical frost sparks fill the atmosphere. 12–14s: Final powerful pose. She spreads her enormous glowing angel wings to their full span while the majestic armored snow wolf throws its head back and unleashes a mighty howl. She raises both glowing energy swords as brilliant divine light erupts across the frozen kingdom, filling the entire screen with an overwhelming burst of golden and icy blue energy, sparkling frost particles, cinematic motion blur, and an epic finale. Style: Hyper-realistic cinematic, high-budget Hollywood fantasy trailer, dramatic camera angles, slow-motion moments mixed with fast action, intense cinematic color grading with gold, white, and icy blue tones, volumetric lighting, snowfall, frost particles, frozen
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Dawn Fire Phoenix Summoning
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10121.jpg" width="480" alt="SD2_10121"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dawn-fire-phoenix-SD2_10121">🌐 Watch Online</a>

#### 📝 Prompt
```
# References Main character = @image1: Facial features, hairstyle, hair color, eyes, skin and coat, clothing, equipment, accessories, physique, silhouette, color, atmosphere, maintaining personal identity. Do not add clothing, equipment, or physical features that do not appear in the reference image. # Style Japanese full-color anime style. A flashy, cinematic fantasy PV. The protagonist casts fire magic in the forest before dawn, gradually transforming the flames and finally creating a giant phoenix. The order is fixed. Gather air and light with your hands→ Embers → Flames running sideways→ Flames that shoot up vertically→ Swirl and compress → Large flame eggs → Cracked eggs → Small Firebirds → Growth → Giant Phoenix. Don't skip along the way. # Setting / Background An open forest spot before dawn. There are tall trees, morning mist, mossy ground, damp soil, pebbles, and tree roots. The background is not pitch black, showing the depths of the blue forest, layers of mist, and the morning glow through the gaps between the trees. The ground is damp and reflects the light of the flames. Sparks, ash, flying leaves, and unreadable abstract magical runes appear and vanish in midair. # Time / Season / Weather / Light Morning court. Clear skies. At first, it was cold blue twilight and mist. When the magic begins, the warm glow of the flames illuminates the protagonist's face, hair, head, costume, hands, and the ground. As the flames grew, orange and golden light spread across the mist, tree trunks, branches, and the ground. When a giant phoenix appears, morning backlight, intense flames, heat fluctuations, and ground reflections all appear strongly at the same time. # Visual Detail / Texture Fingertips, hands, edges of clothing, hair and hair style, and the texture of equipment and accessories are shown. Hair, fur, hems of costumes, fabrics, and decorations naturally sway in the hot air. Flames transform from sparks to horizontal bands of flame, vertical pillars of flame, swirling flames, pulsating large flame eggs, cracking shells, small phoenixes, growing phoenixes, and giant phoenixes. The final phoenix is a majestic flaming bird with visible wings, head, beak, chest, and tail feathers. # Camera / Focus / Composition Average cut length is 2–3 seconds. The entire story is not composed in a single composition. Use a close-up of your hands, upper body, face and hands, a medium wide with a forest, and a final low-angle upward view. Avoid standing straight ahead. 45-degree diagonal, low angle, foreground blur, off-center composition. When flames run horizontally, they move horizontally; when shooting vertically, tilt up; when forming eggs, they circle around; and when growing giant, they pull back slightly to show scale. # Audio A grand, cinematic fantasy background music. No lyrics. The opening is mysterious, the middle section features strings and heavy percussion, and the final part reaches its peak. Sound effects include the rustling of cloth and gear, the sound of hands rustling, ignition, the sound of flames running sideways, the sound of flames spewing, the burning of whirlpools, the low resonance of eggs, the cracking of shells, the flapping of small birds' fire wings, the explosive flames of a giant phoenix, and the heavy beating of wings. No dialogue. # Scene In these 15 seconds, the protagonist gathers air and light at hand in the forest, creating a small flame. The flames run sideways, shoot vertically, and swirl into large flame eggs. The egg cracks, a small firebird is born, and it grows while circling around the protagonist. Only at the end does it suddenly transform into a gigantic phoenix, spreading its wings to envelop the forest and the protagonist. # Constraints No subtitles. No text on screen. No logo. No readable UI. No magic text for readable text. Magic symbols are abstract runes and patterns. @image1 Maintain face, hairstyle, hair color, eyes, skin and coat, clothing, equipment, accessories, physique, and silhouette. Do not add hats, ribbons, capes, staffs, costumes, or equipment that do not appear in the reference images. Do not display multiple copies of the same person. Don't make the background completely black. Don't skip the stages of change. The size and position of the large flame egg formed in Cut 3 are maintained at the beginning of Cut 4. Do not shrink the eggs at the start of Cut 4. Finally, the giant phoenix is clearly displayed. It doesn't go dark. Finish with a normal frame. # Timeline Cut1 0 to 2 seconds. The forest before dawn. The protagonist's upper body and hands. The protagonist extends one hand forward, overlapping the other hand to draw in air and light. Mist, particles of light, and fallen leaves are drawn to my hand, and a tiny spark lights at my fingertips. Closer to the hand, diagonal 45 degrees. The BGM begins. The sound of clothes and equipment scraping, wind rustling, and ignition. Cut2 2 to 4.5 seconds. A spark floated near me. When the protagonist spreads both hands to the sides, flames shoot sharply sideways, forming a band of fire. When you raise one hand, the flame returns to the center, forming a vertical pillar of flame. Tilt-up from a side track. Sparks, sharp burning sounds, heavy burning noises. Cut3 4.5 to 7 seconds. Pillars of flame illuminate the mist and trees. When the protagonist brings both hands inward, the flames swirl and compress, forming a large flame egg nearly as wide as the protagonist's upper body. The egg floats just in front of your hand, from your chest to the front of your face. The egg pulses, abstract runes run across its surface, and finally a clear crack forms. Circle around the egg. Low resonance. Cut4 7 to 9.5 seconds. Start by maintaining the flame egg formed in Cut 3 at the same size and position. You can see the protagonist's face, head, costume, and hands. The egg floats prominently in front of your hand, at a spot where your chest and face are present. The eggs cracked, and the shells burst into sparks and burst. From inside, a small firebird is born. The small bird is clearly smaller than the egg, emerging from the center of the egg, and after going out, it circles around the protagonist's hand. The protagonist, feeling both surprise and joy, guides the little bird with both hands. The cracking of shells, the small fluttering of wings. Cut5 9.5 to 12 seconds. Medium wide with a forest. A small firebird grows as it circles around the protagonist. It grows from about the size of a palm to the upper body, and even about the size of a human torso. Its wings and tail feathers stretch out, and the trail of flames leaves a large circle in the forest. The hot wind shakes hair, hair, costumes, equipment, and branches. The camera pulls a little. The BGM rises right up to the climax. Cut6 12–15 seconds. An open space in the forest. The medium-sized Firebird suddenly transforms into a giant phoenix at the end. Spread your wings across the entire screen, lift your head high, and let your long tail feathers flow. Sparks, ash, mist, and fallen leaves spread outward like shockwaves. The protagonist looks up at the giant phoenix, showing a look of accomplishment. Looking up from a low angle. Explosive flames, shockwaves, heavy flapping. Finally, a giant phoenix spreads its wings in a regular frame.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.13s`

---

### 🎬 Traveler Awakens Ancient Floating Ruins
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10120.jpg" width="480" alt="SD2_10120"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/traveler-awakens-floating-ruins-SD2_10120">🌐 Watch Online</a>

#### 📝 Prompt
```
A lone traveler stands on the edge of a massive floating cliff at sunset, overlooking endless clouds and ancient floating islands. Golden rays of light break through the stormy sky as glowing birds fly overhead. The traveler slowly raises a mysterious crystal that emits brilliant blue energy, causing giant ancient ruins to awaken and rise from the clouds. Cinematic drone shot transitions into an epic close-up with dramatic wind, realistic cloth simulation, volumetric lighting, ultra-detailed environment, HDR, hyper-realistic textures, fantasy realism, 720p , smooth cinematic camera movements, emotional atmosphere, Oscar-level visual quality.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `9.57s`

---

### 🎬 Rainy Night Homecoming Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10119.jpg" width="480" alt="SD2_10119"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rainy-night-homecoming-vlog-SD2_10119">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 16:9 cinematic storyboard collage with 9 seamless frames, no text, no numbers, no captions, showing the same young Korean woman consistently across every frame. She has a high ponytail, wears a fitted white crop T-shirt, blue high-waisted jeans, white sneakers, purple over-ear headphones around her neck, and carries a lavender tote bag throughout the story. Ultra-realistic lifestyle photography, authentic Korean city, natural candid expressions, handheld smartphone aesthetic, soft rainy evening atmosphere, realistic skin texture, subtle motion blur, warm indoor lighting, reflective wet streets, documentary-style realism. Frame 1: She exits a modern office building into light rain, opening a transparent umbrella as she smiles at her phone camera, beginning her evening vlog. Frame 2: Standing at a rainy bus stop, casually talking to the camera while buses and headlights reflect on the wet road behind her. Frame 3: Sitting beside a rain-covered bus window, wearing her headphones while quietly watching the city lights pass by, relaxed and sleepy. Frame 4: Walking through a peaceful Korean apartment complex at night, transparent umbrella overhead, warm apartment lights glowing in the background. Frame 5: Waiting alone in front of an apartment elevator, holding her folded umbrella and tote bag, warm hallway lighting creating a cozy atmosphere. Frame 6: Opening her apartment door and stepping inside with a relieved smile, placing her tote bag down and removing her headphones. Frame 7: Fresh after a shower, wearing soft lavender pajamas while drying her hair in a cozy modern bathroom with warm lighting and subtle steam. Frame 8: Opening the front door to receive a food delivery bag from the delivery rider, smiling warmly in her pajamas. Frame 9: Sitting comfortably on the living room floor beside a low wooden table, eating spicy noodles and fried chicken while watching TV, soda on the table, fluffy duck plush resting on the sofa behind her, warm cozy apartment ambience. Ultra-realistic photography, cinematic composition, consistent character, cozy rainy Korean evening, documentary lifestyle aesthetic, natural lighting, realistic reflections, high-detail interiors, shallow depth of field, soft bokeh, premium storytelling storyboard, 16:9 landscape, no text anywhere in the image.
```

#### 📌 Details
- Ratio: `1.79` | Duration: `15.07s`

---

### 🎬 Cinematic Morning Awakening
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10118.jpg" width="480" alt="SD2_10118"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-morning-awakening-SD2_10118">🌐 Watch Online</a>

#### 📝 Prompt
```
Maintain the exact same original fictional female character throughout the entire video. Keep identical hairstyle, facial features, clothing, body proportions, and appearance in every scene. No character drift. The bedroom and bathroom are two separate connected rooms. The character must physically walk through a doorway from the bedroom into the bathroom. No teleporting, no location merging, no sudden environment changes. Style: Cinematic morning film, realistic fictional character, smooth camera movement, natural acting, warm sunrise lighting, realistic physics, seamless transitions, shallow depth of field, premium cinematic quality. Audio: Peaceful morning ambience, soft birds outside, gentle wind, subtle room tone, classic alarm clock ringing, quiet footsteps, running water from the sink. No dialogue, no voices, no singing. --- Scene 1 (0-2s) A peaceful sunrise appears over the horizon. Golden morning light spreads across the sky. The camera slowly pushes toward the sunrise with soft lens flare, then smoothly transitions into the bedroom as sunlight enters through the window. Scene 2 (2-3.5s) The camera glides into a cozy bedroom. The same fictional woman is sleeping peacefully under a white duvet. Her hair is slightly messy from sleep, her body relaxed. Warm sunlight softly illuminates the room. Slow cinematic dolly toward the bed. Scene 3 (3.5-5s) The camera moves to the wooden bedside table. Close-up of an analog alarm clock showing 6:59 AM. The second hand ticks, the clock changes to 7:00 AM, and the alarm begins ringing. Scene 4 (5-7s) Cut back to the woman. She slowly opens her eyes, blinks, looks tired, yawns, and stretches while sitting up in bed. Natural sleepy expression and realistic movement. Scene 5 (7-10s) She gets out of bed and puts on the sandals beside the bed. Close-up of her feet entering the sandals. She stands and slowly walks across the bedroom toward a bathroom door. Her face looks sleepy. The camera smoothly follows behind her as she opens the door and walks into the separate bathroom. Scene 6 (10-12.5s) Inside the bathroom, she walks to a clean wash basin with a large mirror above it. She turns on the faucet and gently washes her face with water. Realistic water droplets, reflections, and natural movement. Camera captures the sink, mirror, and her actions. Scene 7 (12.5-15s) She lifts her head and looks into the mirror. The camera smoothly rotates to reveal her reflection showing the exact same character. Her face now looks refreshed and awake, with small water droplets on her skin. She gives a subtle smile as warm morning light fills the bathroom. Visual Keywords: Cinematic realism, consistent fictional character, realistic facial animation, smooth tracking shots, natural body movement, realistic reflections, water simulation, soft sunrise lighting, warm color grading, detailed environment, premium film quality, seaml
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.05s`

---

### 🎬 Amber Throne Portrait
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10117.jpg" width="480" alt="SD2_10117"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/amber-throne-portrait-SD2_10117">🌐 Watch Online</a>

#### 📝 Prompt
```
Scene & Mood: Cinematic luxury portrait in a warm amber Arabian lounge. Calm, powerful, mysterious mood. Rich red textiles, brass lanterns, patterned cushions, soft haze, and practical firelight. Frame Map: Start from image1composition. Subject stays center right in a medium wide seated portrait, facing camera. Knees and hands remain visible. Ornate tea table and brass objects stay softly blurred in the lower foreground. Lanterns, cushions, and carved wall decor remain behind him. Keep warm negative space on the left. Slow push in ends as a closer medium portrait. Subject Lock: Image1 Preserve the same seated male subject: same face, skin tone, trimmed facial hair, dark sunglasses, red and white keffiyeh, black agal, white thobe, leopard pattern cloak, watch, rings, body shape, seated posture, relaxed hand placement, and composed expression. Image 1 the same face, hair, wardrobe, body shape, and silhouette throughout. Cloak stays naturally draped over both shoulders. Thobe stays matte white with soft real fabric folds. Cross Frame Rules: No identity drift, no face change, no wardrobe change, no altered sunglasses, no extra jewelry, no headwear change. Subject remains center right at the same depth and eyeline. Do not add people or modern objects. Keep the same lounge layout, lantern positions, patterned textiles, brass objects, amber palette, and shallow depth. Movement: 15s continuous shot. Subject remains seated and still with slow breathing. His right fingers relax slightly on his knee, left hand barely shifts against the fabric, and his head tilts a few degrees toward camera. Keffiyeh edge, cloak fibers, thobe folds, watch, and rings catch tiny natural movements. Lantern flames flicker gently, brass highlights shimmer softly, haze drifts in the background. Camera makes a slow, smooth push in with subtle handheld breath, never shaky. Last Frame: End on a closer medium portrait. Subject remains center-right, sunglasses facing camera, shoulders and upper torso dominant, right hand relaxed on knee, leopard cloak framing the white thobe. Lantern glow and patterned textiles stay softly visible behind him. Camera settles nearly locked. No on screen text, no captions, no signage typography, no rendered text in the frame. World Plate: Ornate lounge with burgundy, red, black, gold, and amber tones. Layered rugs, cushions, wall hangings, carved circular wall decor, brass lanterns, and polished metal objects create depth. Lighting comes from practical lanterns with soft falloff and lifted shadows. Mild incense haze adds air depth. Textures feel tactile: woven fabric, matte cotton, aged brass, carved metal, natural looking fur. Sound Bed: Diegetic audio only: quiet lantern flame flicker, faint room tone, soft fabric rustle from breathing, subtle jewelry movement, distant air movement. No music, no score, no vocals, no lyrics. Capture Realism: Natural skin texture, matte skin, realistic facial hair, believable fabric weight,
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

### 🎬 Charming First Date Garden Cafe
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10116.jpg" width="480" alt="SD2_10116"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/garden-cafe-first-date-SD2_10116">🌐 Watch Online</a>

#### 📝 Prompt
```
Cinematic realistic 15-second live-action scene of a charming first date at an upscale outdoor garden cafe under large shady trees with warm string lights overhead. Photorealistic, high production value, filmic color grade. A handsome man in his mid-30s (dark wavy hair, light stubble, blue eyes, charming smile) wearing a rich brown short-sleeve polo shirt and white pants sits across from a beautiful Western woman in her mid-20s (long wavy blonde hair, expressive face, natural makeup) wearing a cream sleeveless ribbed top with black trim. Start with a medium over-the-shoulder shot from behind the man. The woman asks playfully but skeptically: “So what do you actually do? Please don’t say entrepreneur.” Cut to tight close-up on the man as he smiles confidently and replies: “Well, I flip vintage furniture, and I do some design consulting on the side.” He holds a white coffee cup. Quick reaction close-up on the woman, eyebrows slightly furrowed: “Like chairs?” He answers warmly: “Yeah, people pay a lot for chairs.” Her expression transforms — doubt melts into amusement and attraction. She smiles, looks down shyly then back up at him and says playfully: “Okay, I think I’m actually gonna head out.” Natural dappled sunlight filtering through dense green tree leaves, warm glowing string lights, shallow depth of field with creamy bokeh, rich earthy color palette (chocolate brown, cream, warm beige, lush greens), soft cinematic lighting, flattering skin tones, subtle film grain, intimate and romantic atmosphere, high detail, photorealistic, shot on 35mm film, premium commercial quality like high-end dating app ads.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `44.9s`

---

### 🎬 Velocity Wake: One-Take Rush
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10115.jpg" width="480" alt="SD2_10115"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/velocity-wake-one-take-SD2_10115">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a super cinematic continuous single-take jet ski wakeboarding video. Strictly refer to the provided character chart to describe this woman [@图片1]: cool pale skin, bright black eyes, long straight black hair, slim and athletic figure, white deep V-neck one-piece swimsuit, green jet motor boat [@图片2] (referring only to the boat, not the person above). The front of the boat is made of transparent glass. Only one subject appears: this woman. No other riders, surfers, or extra boats. Scene: Bright and open water, blue-green water, sunlight reflection, strong speedboat wakes, white foam, small waves, splashes, wind noise, and engine noise. Raw, fast, cinematic, and authentic. Photography style: High-speed action documentary with a high-definition cinematic texture, 35mm lens, follow shooting, with shake and blur that bounce with the waves, cool tones, natural sunlight. Video style: A continuous shot with no editing, no hidden editing, no transitions, no montage. Super realistic movement, natural motion blur, motorboat engine sounds, motorboat gliding, camera droplets, splashes, wind noise, and believable body adjustments. Audio: Vibrant cinematic action music. Starting with a fashionable adrenaline beat, accompanied by clear engines, wind, motorboats, and the sound of water. During ultra-slow motion, the tone shifts to deep bass, rising tension, and an ethereal, floating impact. Upon landing, it delivers sharp strikes and returns to full-speed action energy. The video begins with a very close front view, showing the woman leaning forward from the motorboat's driver's seat. The camera is close to her face and upper body, slightly lower. She smiled confidently at the camera, her damp black hair fluttering in the wind, her white V-neck swimsuit visible, arms spread wide and gripping the motorboat's handlebars. The small boat moved quickly across the water, sending up waves and small waves at its rear. The lens smoothly pulls out and drops to a lower position. She skimmed the camera at high speed without any editing, then shifted behind her, entering an extremely low tailing angle, positioned at the stern level of the boat, close to the water, slightly behind the stern. Now the camera follows from behind, low and close. The small boat cuts through the water, splashing water hits the camera, and the boat accelerates, stirring up even bigger waves. She pushed herself up with both legs, slightly stood up, leaned forward, and accelerated. The wind tousled her long hair, and the camera moved up to her side. She laughed excitedly at the camera, then turned to focus on steering the boat, cutting through foam and waves. She makes small, realistic jumps on the undulating water, while maintaining her balance. Then she bent down, turned hard, and the boat made a sharp left turn, tracing a C-shaped arc on the water's surface, touching the water with her left hand. Her fingertips glide across the water, flicking the splash back toward the low camera. She accelerated the turn of the boat and continued turning to the right. The camera was pressed against his face and shoulders in front of her. She pressed her right hand toward the water, lowered the edge of the hull, gripped the joystick tightly with both hands, and the boat's real jump was taken off from the tail wave, powerful but not exaggerated. When the small boat leaves the water, she grips the joystick tightly with both hands, stands fully on her legs, and switches to ultra-slow motion. The camera kept moving, pushing closer to her while smoothly rotating around her body. Individual droplets and suspended droplets are clearly visible, accompanied by subtle hair movements, the tension of the dinghy's flying jumps in the air, and subtle body adjustments. At the apex, she holds the joystick with one hand while the other hand is spread upward. As the camera moved closer, she turned to face the camera, gazing intently and excitedly. She gripped the control stick tightly with both hands again, and the boat plummeted. At the moment of impact, the ultra-slow motion immediately ends and the car returns at full speed. She landed forcefully, causing explosive splashes and spraying water toward the camera. The camera stayed low on the side and rear of the small boat, following the impact, then quickly gliding through a large wave of water curtain domes, sliding very coolly. She regained her balance and continued to ride through the waves in the same continuous single-shot dinghy.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Anime Subway Sonic Duel Silence Wins
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10114.jpg" width="480" alt="SD2_10114"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/anime-subway-sonic-duel-SD2_10114">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 15-second video using the attached storyboard as the strict visual anchor — follow all 11 panels in exact sequence, matching each panel's framing, action, and timing, without skipping, merging, or reordering any panel. IRON CHOIR — 15s anime subway duel. Kade (sonic force, escalating) vs Silas (silence, nullifying), decisive Silas win. Abandoned subway platform, night, flickering fluorescents, cracked ad-panel glass, distant tunnel wind. STYLE: Sakuga action anime, sharp dynamic linework for Kade's sonic ripple-rings, restrained desaturated rendering for Silas's dead-zones (color drains, light softens, air distorts — absence, not a glowing shield). Bold cell shading, shattering glass particles, manga impact frames. KADE: late-20s, broad powerful build, bronze skin, cropped dark hair, sharp intense eyes, cracked headphones around neck, dark utility vest. Sonic ripple-rings live from frame one, growing louder/larger through the fight, fully gone (not diminished) after the final beat. SILAS: early-30s, lean vertical build, ash-pale skin, cropped silver-gray hair, calm half-lidded eyes, dark asymmetric high-collar coat, silent boots. Dead-zone distortion appears only at contact — small at first, largest and quietest at the decisive moment. SHOTS: 1 (0-1.5s) Wide platform, flickering lights; push into Kade's humming knuckles. 2 (1.5-2.5s) Close on Silas's calm eyes, no ability visible yet. 3 (2.5-4s) Kade strikes; sonic ring bursts outward, cracks ad-panel glass. 4 (4-5s) Silas blocks; dead-zone expands, ripple stutters and collapses inward, colors desaturate. 5 (5-6s) FREEZE — quarter-orbit, ripple caught mid-collapse, dust suspended in desaturated haze. Eerie, quiet. 6 (6-7.5s) Release — Kade throws a louder, larger combo, shatters a second panel. 7 (7.5-8.5s) Silas steps into the ripple's origin point instead of away, eyes sharpen. 8 (8.5-10s) Kade's biggest strike — full extension, floor cracks from force, no recovery stance. Overcommitted. 9 (10-11.5s) THE SILENCING — Silas places one palm flat on Kade's chest at the ripple's origin. No explosion — the ripple simply stops existing. Total desaturation, total silence. Quietest, most decisive beat in the film. 10 (11.5-13s) Kade staggers, gasping, ripples gone entirely, staring at his silent hands. Silas composed, color slowly returning. 11 (13-15s) Wide symmetrical hold. Title: "IRON CHOIR." Subtitle: "Even the loudest voice can be unmade." CAMERA: static/close standoff, forward handheld for Kade, one restrained partial-orbit for the freeze, close hold (no pull-back) on the silencing, static symmetrical close. AUDIO: platform hum/tunnel wind → sonic crackle and shattering glass building → hushed near-silence on the freeze → true total silence at the decisive beat (contrast is silence itself, not a bass hit) → hum returns, one soft closing to
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

<!-- STATS_END -->
