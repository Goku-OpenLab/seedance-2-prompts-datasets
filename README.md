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
- Total Prompts: **8679**
- Updated Today (UTC 2026-08-12): **4**

## 🎬 Today's Updates
### 🎬 Ice vs Fire Cherry Blossom Duel
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11340.jpg" width="480" alt="SD2_11340"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ice-fire-cherry-blossom-duel-SD2_11340">🌐 Watch Online</a>

#### 📝 Prompt
```
"Icewoman vs. Firefighter Accurate 30 seconds, Seedance 2.5, keeping the original frame of the reference picture. Ultra-realistic high-budget live-action martial arts fantasy movie, ARRI Alexa 35, natural Asian actors, real skin and clothing, long hair physics, cinematic depth of field, natural motion blur, restrained film grain; no anime, gamey feel or cheap CG. Strictly locked @Image1 adult heroine's face, hairstyle, alabaster green costume and body; @Image2 adult heroine's face, long hair, black and crimson costume and body; @Image3 same giant cherry blossom tree, guqin, stone pedestal, pool, ancient buildings, distant mountains, light and spatial relations, no drifting throughout. The female warrior opens unarmed, only to be attacked with the pool water condensing into the only translucent jade-blue ice sword; the male warrior always wields only a solid black longsword, with crimson and gold flames clinging to the blade. Duplicating, changing hands, disappearing or morphing is prohibited. [Absolute Timeline 0-3 seconds Guqin; 3-6 seconds Fire Sword Assault from behind; 6-8 seconds Gathering Water into an Ice Sword; 8-20 seconds Uninterrupted High-Speed Solid Sword Fighting; 20-24 seconds "Water Dragon "Water Dragon" awakens and summons a water dragon; 24-27 seconds "Fire Phoenix" awakens and summons a phoenix; 27-30 seconds Ultimate Clash. 20 seconds prior to this time, inscriptions, spell formations, dragons, phoenixes, or any summoning omens are strictly prohibited; you may not return to the swordfight after summoning. Sword Fight. Characters must have realistic expressions: calm when playing the piano; pupil rotation, brow tightening, and respiratory arrest when detecting a sneak attack; sharp eyes and tight jaw when Near-Miss; eyes tracking opponents and blades in a duel, startled reaction to a close avoidance, clenched teeth, furrowed brow, and exhale on impact; anger, exhaustion, and tremendous force when summoned. The movements are inhumanly high-speed and ferocious, driven by footwork, waist and hips, shoulders, Body Spin, cartwheels, light sliding, and borrowed power to change direction, and prohibited from standing and swinging arms. 90% of the speed is maintained at high speeds, with only 3cm Near-Miss and the clashing swords using a Speed Ramp of 0.12-0.18 seconds. cameras such as the Third Warrior: Partial Cam, Whip Pan, 20 seconds off the ground, and the Sword Ramp, which are used by the Third Warrior, are also used. , Whip Pan, Low-Level Track 20cm off the ground, Fast Surround, Top Down, Dolly Zoom; wild but clear, switching positions every 3-4 seconds, close-ups of faces only 0.2-0.35 seconds, non-stop action. [0-3 sec] 50mm close to strings panning across, heroine alone under cherry blossom tree realistically plucking strings, petals falling; camera passes over fingers & calm side face then quick Dolly Out reveals courtyard, pool & old building. The male warrior shall not appear earlier. [3-6 seconds]. Hard cut to the back side of the Female Warrior. Male Warrior sprints against the ground from ten meters directly behind her, holding his only fire sword in both hands, and slashes vertically downward at close range with a sprint, shoulder and waist power, never a fireball or sword breath. When the sword is 3 centimeters away from the back of her head, her pupils turn sideways, twisting her waist to the right side of the screen to dodge; the camera is shaken once to the left by the wind pressure, and immediately Whip Pan chases the right. The fire sword hit the stone platform, forming straight burning cracks, rubble, sparks and scattered cherry blossoms, the piano suddenly stopped. [6-8 seconds] She slides to the edge of the pool and raises her hand; transparent ribbons of water condense from hilt to tip into the sole water sword, the outer layer quickly freezing to a jade-blue ice blade, the inner water ripples flowing. The male warrior arrives in pursuit; she turns 360° to block at the moment of sword formation, and the two swords clash in a short ring of steam, sparks, shattered ice, and impact. [8-14 seconds] 18mm low camera high speed backward follow up shot. Man Man's continuous downward chop, backhand crosscut, low sweep, and spinning back chop; Woman Man's side head Near-Miss, low body slide, back pick, sword back block, and 360° spin into the inside. Male Warrior tucks his stomach to avoid the ice blade and sweeps his leg with one hand on the ground; she leaps over and rises with her foot pointing the back of her sword for a flip back chop, which he spins around to block and jolts her toward the cherry blossom tree. Interspersed with close-ups of the moment when the sole of his shoe crumbles, the hand holding the sword, the fire blade grazes his eye by 3 centimeters, and the ice blade cuts through his sleeve. [14-20 seconds] The heroine leans back to avoid the sweep, steps on a tree trunk for three vertical runs and catapults into the air; the hero crushes the ground to catch up. The two run and jump along the branches and eaves of the tree, using the environment and the blade of the sword to change directions continuously: downward slash, side block, reverse Body Spin, flip backstab, spinning body block and kick, leaping again from the eaves of the house, and cross-positioning in the air, and never levitating and posing. Fire rails are short and close to the edge, and ice swords only leave short bursts of water, cold mist, and ice crystals; long-range sword energy is strictly forbidden. The final airborne crash of the swords creates a ring of vapor impact, and the two are pushed to opposite ends of the courtyard, flipping to the ground and looking angrily at each other, ending the swordfight. [20-24 seconds｜Water Dragon Hard cut woman single center close up, breathing sharply. Inside the ice sword, the stabilizing ancient seal script "水龍", not a subtitle or a floating script; "水" (water) to "龍" (dragon) lights up along the strokes, and the blue light reflects on her face. Holding the sword with both hands, she rotated her whole body through 360° and then raised it violently, the tip of the sword unfolded a three-layer water spell formation; the huge amount of water in the pool was molded into the dragon's horns, head, whiskers, scales, long body, and tail in turn. She gritted her teeth and stabbed the sword forward, the inscriptions bursting into flames and guiding the complete eastern water dragon to roar out; the sword only lifted the seal, never turning into a dragon. 24-27 seconds｜Fire Phoenix The hard-cut male warrior is single and ultra-low, approaching water pressure blowing his long hair and sleeves. He is gritting his teeth and staring angrily, and the ancient seal of the black sword, "Fiery Phoenix," is lit up in red gold along the strokes, stabilizing the perspective. Holding the sword with both hands, he chopped his whole body in a circle and then raised it vertically, the tip of the sword unfolded a multi-layered fire formation, the flames formed the phoenix's head, feathers, complete wings and long tail in turn. He presses the sword forward and the inscription bursts into light, guiding the giant phoenix to meet it; the sword shall not become a phoenix. [27-30 seconds] 24mm side ultra-wide angle: female warrior left, male warrior right, both in dynamic sword stance controlling divine beasts, teeth clenched and breathing, feet sliding back by reaction force. Complete water dragon and fire phoenix in the center of the collision, water and fire continue to push pressure, steam, ice crystals, fire feathers, charm light and cherry blossom rotation; the core of the prohibited white overexposure, dragon head and body, phoenix head and wings and long tail is always clear. The last 0.3 seconds "speed → 10% → recovery", two inscriptions at the same time burst bright, both sides of the whole body to push the sword, release the blue and red ring shock wave and cut black. No BGM, no narration; only Guqin, Wind, Breath, Footsteps, Clothes, Wind Breaker, Flame, Ice Cracker, Water Flow, Sword Crash, Steam, Rune Whisper, Dragon Roar, Phoenix Sound, Ultimate Low Frequency. Prohibit garbled code, floating characters, character/weapon/beast duplication, extra limbs, mold wearing, transient, stiff repetition, empty expression, identity clothing scene drifting and obvious AI sense.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `36.9s`

---

### 🎬 White Rabbit Watch Chase Scene
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11320.jpg" width="480" alt="SD2_11320"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/white-rabbit-watch-chase-SD2_11320">🌐 Watch Online</a>

#### 📝 Prompt
```
Fifteen-second rapid, action-led sequence with no dialogue. Begin on a medium-wide eye-level composition: Girl at screen left has just risen from the grass, while the White Rabbit has stopped at screen right beside the hedge. Keep the dark opening under the roots visible behind the Rabbit but do not let it enter yet. The camera makes a short, cautious push toward Girl’s sightline as the Rabbit reaches into its waistcoat pocket and produces a small watch. Cut to an insert of the watch held in the Rabbit’s hand: its case is solid metal, its face is period-appropriate, and its movement is plainly impossible because a formally dressed rabbit is checking it with human alarm. A warm sun glint flashes across the glass. Cut immediately to Girl in medium close-up; she takes one involuntary step forward, breath held, eyes moving from the watch to the Rabbit’s face. Cut back wider as Rabbit closes the watch and pivots toward the root-framed hole. The camera reframes right to include the hole and preserve the visible causal chain: watch proves anomaly, anomaly makes pursuit inevitable. Grass rustles under Girl’s first step; hedge leaves tremble in a faint wind; the hole’s interior is cool and black against the amber bank. End with Rabbit beginning to hurry toward the opening and Girl fully upright in left midground, intent and poised to chase. Do not show Sister. Do not have Girl touch the Rabbit or narrate her thoughts. The emotional beat is revelation, not terror: Girl has seen enough to choose action. Use crisp cuts, but keep physical geography consistent: Girl remains left of Rabbit, Rabbit remains right and nearer the hedge.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

### 🎬 Sword Fairy Bike Swap Comedy
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11316.jpg" width="480" alt="SD2_11316"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sword-fairy-bike-swap-SD2_11316">🌐 Watch Online</a>

#### 📝 Prompt
```
【Video Specifications】 Strictly 10 seconds total length, 16:9 aspect ratio, landscape mode, 24fps. Two clean shots must end precisely within 10 seconds; no 10-15 second content should be generated. 【Overall Style】 Cinematic realism, employing elegant action-comedy pacing, high-end commercial advertising lighting, clear Hong Kong action film spatial relationships, restrained facial reactions, and a brand-new &quot;skill exchange&quot; mechanism. Neither side is defeated or humiliated; instead, the two discover that their proficient riding experience can only be partially transferred to a completely different &quot;mount.&quot; The core of the comedy comes from: familiar habits → misplaced transfer → mutual reminders → simultaneous correction → unexpected establishment of tacit understanding. 【Scene Setting】 An empty elevated riverside plaza in the early morning. Pale golden sunlight, long building shadows, brushed concrete pavement, glass railings, distant city skyline, light morning mist, and a natural breeze blowing through clothing. A training route approximately twenty meters long is clearly visible. The space must be open, simple, and readable, ensuring that the two characters, the bicycle, the flying sword, and the subsequent left and right movement trajectories remain clear. 【Character Lock】 Character ID A \| Sword Fairy Sister: Same 25-30 year old East Asian Sword Fairy Sister from @Image 1. Strictly maintain the following in the reference image: Same face, sharp dark brown eyes, long straight black hair, tall and slender figure, white cloth boots, white embroidered silk Hanfu, semi-transparent layered wide sleeves, silver waist ornament, jade hairpin, same silver flying sword. Character ID B \| Bicycle Sister: Same 25-30 year old East Asian Bicycle Sister from @Image 2. Strictly maintain the following in the reference image: Same face, brown ponytail, same figure, yellow coat, blue jeans, white sneakers, accessories, same bicycle. 【Core Items】 Same silver flying sword, same bicycle. Cannot be copied, replaced, disappeared, or temporarily generated as a second bicycle or a second flying sword. 【Scene 1 \| 0-5s \| Low-angle panoramic slow tracking】 The camera uses a low-angle panoramic slow tracking to first establish the elevated riverside plaza and a training route of about 20 meters in the early morning. The same Sword Fairy Sister and the same Bicycle Sister stand face to face. The same bicycle and the same floating flying sword are located between the two. The cyclist pointed to the flying sword. The swordswoman simultaneously pointed to the bicycle. The cyclist asked, &quot;Switch?&quot; The swordswoman replied, &quot;Switch.&quot; Both maintained incredibly serious expressions, as if performing a formal handover ceremony, before exchanging positions: the cyclist walked towards the flying sword, and the swordswoman towards the bicycle. Their movements were direct, restrained, and clear, without any added humor. [Scene 2 \| 5–10s \| Cowboy scene within a shot, side view] The camera switches to a cowboy scene within a shot, side view. The two characters each use the other&#39;s familiar mount, moving in opposite directions, eventually passing each other in the frame. Cyclist \| Riding the Flying Sword: The same cyclist steps onto the same silver flying sword. Due to muscle memory formed from long-term cycling, she instinctively: bends her knees, lowers her body, and makes pedaling motions with both feet, attempting to pedal pedals that don&#39;t actually exist. She isn&#39;t walking on the sword itself, but rather, her feet are already firmly planted on the flying sword, yet she subconsciously makes cycling-style pedaling motions. The flying sword, affected by the body&#39;s movement, immediately accelerates forward. Sword Fairy Sister \| Riding a Bicycle Meanwhile, the same Sword Fairy Sister, dressed in a white embroidered silk Hanfu, rode the same bicycle. Due to the ingrained habits of sword-wielding, she instinctively released one hand and attempted to control the bicycle using a two-finger hand gesture. The bicycle didn&#39;t respond to the gesture, causing a slight swerve in the front wheel. She remained seated, neither falling nor losing control, but had to relearn the actual function of the handlebars. [Intersection and Dialogue] The two continued in opposite directions, passing each other on the same training route. Sword Fairy Sister shouted: &quot;Don&#39;t pedal!&quot; Bicycle Sister immediately shouted back: &quot;Hold the handlebars!&quot; [Synchronized Correction] Both understood each other&#39;s reminders at the same instant and corrected their movements simultaneously. Bicycle Sister: Stopped pedaling, stabilized her feet on the flying sword, adjusted her center of gravity, and restored a stable sword-wielding posture. Sword Fairy Sister: Immediately regained control, firmly gripped the handlebars, corrected the front wheel&#39;s direction, and maintained normal riding balance. Neither failed, nor did either gain a clear advantage. They simply discovered that: the other&#39;s mount couldn&#39;t be controlled entirely according to their old habits. [10-Second Ending Shot] After the corrections, the two continue to move forward steadily. While maintaining their new, stable driving posture, they glance at each other with a restrained yet unexpectedly approving look. The shot must end precisely at 10.0 seconds with a clean parallel motion composition: both characters are in stable motion, the same bicycle is moving normally, the same flying sword is gliding smoothly, both are confidently controlling their swapped mounts, their movement direction is clearly aligned with the camera axis, and there are no pauses, falls, collisions, or additional reversals. End directly at 10.0 seconds.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.08s`

---

### 🎬 Cozy Korean Night Skincare Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11310.jpg" width="480" alt="SD2_11310"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-night-skincare-vlog-SD2_11310">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-realistic cinematic vertical video, 10 seconds. A beautiful young Korean woman spending a peaceful late-night skincare routine in her cozy bedroom. She is wearing the same oversized cream-white T-shirt throughout the entire video. Warm bedside lamp light mixes naturally with soft cool moonlight coming through the window. The room has a cozy Korean bedroom aesthetic with a full-length mirror, soft bedding, subtle fairy lights, and a small bedside table. The entire video is filmed as authentic handheld smartphone selfies, like a personal nighttime vlog. Natural movements, realistic facial expressions, subtle breathing, natural blinking, lifelike hair movement, realistic skin texture, no overly posed movements. Shot 1 (0–2s): Front handheld selfie in front of the full-length mirror. She gently moves her hair behind her shoulders, looks at herself briefly, then turns her eyes toward the phone camera and gives a soft natural smile. The phone has subtle realistic handheld movement. Shot 2 (2–4s): Slightly high-angle selfie while she sits comfortably on the edge of the bed. She picks up a small skincare cream, applies a little to her face naturally with her fingertips, then gives a playful subtle expression toward the camera. Shot 3 (4–6s): Mirror selfie. She stands close to the mirror and gently fixes a few loose strands of hair while looking at her reflection. After a moment, she looks directly at the phone screen and smiles naturally. Shot 4 (6–8s): Side-profile handheld selfie near the bedside table. She reaches for a clear water bottle, takes a small natural sip, lowers it, and looks toward the camera with a soft relaxed smile. Her hair moves naturally as she turns. Shot 5 (8–10s): Front close-up selfie. She comfortably lies back against the pillows under a soft blanket, looks directly into the camera, makes a tiny finger-heart gesture close to the lens, then finishes with a warm genuine smile as the camera gently moves backward. Style: Ultra-photorealistic Korean beauty, authentic smartphone camera quality, natural handheld selfie movement, realistic skin pores and texture, natural blinking and breathing, lifelike hair simulation, realistic hand and finger movements, soft warm bedside lighting mixed with cool moonlight, subtle bedroom shadows, cinematic shallow depth of field, natural lens behavior, premium film color grading, intimate cozy nighttime atmosphere, 24fps, 8K, vertical 9:16. No text, no subtitles, no logos, no unnatural body movements, no excessive beauty filter.
```

#### 📌 Details
- Ratio: `0.75` | Duration: `10.08s`

---

### 🎬 Cinematic Fashion Montage With Glitch Effects
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11303.jpg" width="480" alt="SD2_11303"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-fashion-montage-SD2_11303">🌐 Watch Online</a>

#### 📝 Prompt
```
A fast paced cinematic fashion montage featuring a stylish young woman wearing a black leather jacket baggy light blue jeans a white crop top and dark sunglasses The video begins with a fast tracking shot of her running past metal shopping carts in a cool toned concrete parking garage The camera transitions rapidly using whip pans and barrel rolls An extreme low angle fisheye shot reveals her standing against a tall concrete building under a bright overcast sky This immediately cuts to a high angle drone shot looking straight down as she spins in an empty parking lot Digital glitch effects and visual warp distortions appear briefly between cuts The sequence features dynamic hand transitions where the subject reaches for the lens It concludes with a low angle tracking shot of her walking confidently forward The lighting shifts between dim fluorescent garage lights and bright overcast daylight Highly realistic motion blur cinematic color grading natural skin textures and authentic clothing physics Upbeat electronic music plays in the background aspect ratio 16 9 duration 12 seconds
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.07s`

---

### 🎬 Epic Elemental Warriors Clash Battle
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11299.jpg" width="480" alt="SD2_11299"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/elemental-warriors-clash-SD2_11299">🌐 Watch Online</a>

#### 📝 Prompt
```
A cinematic, high-octane 3D fantasy action scene featuring two elemental female warriors clashing in battle. On the left, a fierce dark-haired warrior in red leather armor with glowing fiery flames and burning embers wrapped around her arm. On the right, a graceful warrior with flowing hair in white and ice-blue attire, wielding a glowing blue ice-rose whip sword. They charge and leap toward each other across a desolate landscape filled with ancient crumbling stone pillars under a stormy sunset sky. As they collide in mid-air, fiery orange magical aura clashes directly against bright blue ice energy, creating a massive cinematic explosion of light, embers, blue rose petals, and flying debris. Dynamic camera pan, slow-motion impact, hyper-realistic 8K CGI, Unreal Engine 5 render style, dramatic lighting.
```

#### 📌 Details
- Ratio: `2.35` | Duration: `15.19s`

---

### 🎬 Kittens Dancing On Night Beach
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11298.jpg" width="480" alt="SD2_11298"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/kittens-dancing-night-beach-SD2_11298">🌐 Watch Online</a>

#### 📝 Prompt
```
A 10-second realistic handheld video at night on a wet sandy beach. A tiny white kitten with grey markings on its head stands upright on its hind legs in shallow water, front paws raised like it’s dancing or balancing, looking curiously at the camera. A small light-brown (ginger) kitten walks toward it, then also rises onto its hind legs beside the white one, both cats standing side-by-side with paws up in a playful, almost human-like pose. Gentle ocean waves roll in the dark background, wet sand glistening under soft night lighting. Cute, slightly shaky handheld footage, adorable and whimsical atmosphere
```

#### 📌 Details
- Ratio: `1.78` | Duration: `9.97s`

---

### 🎬 Hyper-Realistic Cinematic Storyboard Sequence
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11296.jpg" width="480" alt="SD2_11296"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/hyper-realistic-cinematic-storyboard-SD2_11296">🌐 Watch Online</a>

#### 📝 Prompt
```
Use @[Image] as storyboard reference for cinematic sequence. use as first shot 01 A 15-second majestic cinematic sequence transitioning smoothly through all 8 storyboard panels in strict chronological order. Visual style: hyper-realistic
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 Luxury Smartwatch Cinematic Demo
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11293.jpg" width="480" alt="SD2_11293"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/luxury-smartwatch-demo-SD2_11293">🌐 Watch Online</a>

#### 📝 Prompt
```
A cinematic product demo of a luxury smartwatch. Open with macro shots highlighting the display, premium materials, smooth camera movement, dramatic lighting, and product features before showing the final use case. Ultra-realistic commercial style, 4K. A cinematic product demo of a luxury smartwatch. Open with the finished commercial showing the smartwatch in use during a workout. After revealing the outcome, transition into the workflow and close-up feature shots with premium lighting, smooth cinematic movement, ultra-realistic commercial style, 4K.
```

#### 📌 Details
- Ratio: `0.63` | Duration: `20.03s`

---

### 🎬 Hyper-Realistic CGI Figurine Render
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11289.jpg" width="480" alt="SD2_11289"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/hyper-realistic-cgi-figurine-render-SD2_11289">🌐 Watch Online</a>

#### 📝 Prompt
```
Cinematic hyper-realistic 3D CGI collectible-figurine render, like a live-action blockbuster VFX sequence: physically-based rendering (PBR), octane-render-quality lighting and materials, fabric with visible weave and natural drape, metal with realistic wear
```

#### 📌 Details
- Ratio: `1.78` | Duration: `13.97s`

---

### 🎬 Rainy Night Alien Chase
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11287.jpg" width="480" alt="SD2_11287"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rainy-night-alien-chase-SD2_11287">🌐 Watch Online</a>

#### 📝 Prompt
```
A desperate, low-angle tracking shot following the man from image_1.png, maintaining his likeness and blue eyes, now clad in tactical black gear, sprinting through a rain-soaked, chaotic downtown street at night. Just behind him, a double-decker city bus is captured in the middle of a massive, fiery explosion, sending debris and orange flames into the air. Above the burning cityscape, a colossal biomechanical alien mothership of intricate metallic design descends through the storm clouds, its blue lights pulsing. To the right, emerging from the shadows and wrecked cars, a sleek Alien Predator lunges in pursuit. The camera dynamically retreats and pans to show the scale of the destruction, ending on a wide view of the entire scene. Dramatic lighting with deep contrast between the firelight and cool night tones. Rain pours heavily, creating reflective puddles. No text.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.04s`

---

### 🎬 Storyboard Visual Control Guide
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11285.jpg" width="480" alt="SD2_11285"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/storyboard-visual-control-SD2_11285">🌐 Watch Online</a>

#### 📝 Prompt
```
[REFERENCE CONTROL] Use the uploaded storyboard image as the primary visual reference for story structure, character design, costume design, environment, emotional progression, and shot order.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Chocolate Mango Snack Commercial
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11283.jpg" width="480" alt="SD2_11283"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/chocolate-mango-snack-commercial-SD2_11283">🌐 Watch Online</a>

#### 📝 Prompt
```
Cinematic 3D commercial product video for gourmet dried fruit snacks, vertical 9:16 aspect ratio. Sequence begins with a high-definition close-up of fresh ripe yellow and red mangos on branches with lush green leaves in warm golden sunlight. Seamlessly transitions into a single ripe mango floating against a glowing warm background, transforming into golden dried mango slices floating weightlessly in mid-air. Next, a fresh cracked coconut bursts open alongside a smooth, rich swirl of melted milk chocolate. Dried mango slices dipped in dark chocolate float upward while fine white coconut flakes sprinkle down around them like snow. The sequence culminates in a black snack pouch labeled "MR. VIET Dried Mango with Chocolate & Coconut" floating in the center of the frame, surrounded by floating chocolate-dipped dried mango pieces and fine coconut shreds. Dynamic physics, warm ambient studio lighting, ultra-detailed textures, slow-motion physics, 8k render, photorealistic, advertising food commercial style.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `21.7s`

---

### 🎬 Nostalgic Trainee Flashback DV Footage
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11272.jpg" width="480" alt="SD2_11272"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/trainee-nostalgic-flashback-SD2_11272">🌐 Watch Online</a>

#### 📝 Prompt
```
@CHASE is the same character throughout. Maintain strict facial, hairstyle and appearance consistency.

Create a 15-second nostalgic early-2000s trainee flashback filmed entirely on a handheld DV/16mm camcorder. Raw personal-footage aesthetic: natural camera shake, imperfect framing, slow autofocus, clumsy micro-zooms, slight blur, tape noise, motion smearing, bloomed highlights and occasional exposure flicker. No modern polished cinematography.

STORY:
0–2s: Before sunrise, she wakes exhausted in a trainee dorm. “Nobody saw how it started.”
2–4s: She enters an empty dance studio, turns on the light and prepares to practice.
4–6s: In a vocal room, she misses a difficult note, exhales and tries again. “There were days I thought I wasn't good enough.”
6–9s: Repeatedly practices choreography, makes mistakes, then keeps going.
9–11s: Quick DV close-ups of worn sneakers, tired hands, sweat and a movement finally landing perfectly.
11–13s: Exhausted in a hallway, she smiles quietly, hears the practice music and gets back up. “But somehow… I kept coming back.”
13–15s: She walks toward a brightly lit evaluation room, pauses, takes a breath and enters. “Maybe that was enough to begin.” Cut to black.
Raw, intimate and emotional. Subtle acting, realistic exhaustion and determination. Hard cuts, authentic room ambience, footsteps and breathing. Soft emotional music gradually builds. Make it feel like forgotten personal trainee footage, not a music video.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Pink Hair Ink Action Visual
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11271.jpg" width="480" alt="SD2_11271"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pink-hair-ink-action-SD2_11271">🌐 Watch Online</a>

#### 📝 Prompt
```
P1 [0:00–0:01.25] Use the provided storyboard frame, character reference image, and provided Higgsfield logo reference image. Maintain exact character appearance: pink hair, olive cargo pants, white crop top, green cap, tattoos on arms. Keep the Higgsfield logo and “Higgsfield” text naturally visible throughout the scene as environmental branding. Real photography, low-angle shot, young woman with pink hair and olive cargo pants crouching low, black ink explosion erupting from the ground around her fist impact, high-speed photography, dramatic studio lighting, ink splatter physics, hyper-detailed skin texture, Canon R5, 85mm f/1.4. P2 [0:01.25–0:02.50] Photorealistic, motion blur, athletic woman with pink hair executing a spinning back kick, black ink trails streaking through the air, cinematic lighting, shallow depth of field, gritty concrete environment, sports photography style, Nikon Z9. Maintain exact character appearance and keep Higgsfield branding visible. P3 [0:02.50–0:03.75] Photorealistic low-angle upward shot, woman with pink hair leaping vertically, massive black ink vortex surrounding her, dramatic rim lighting, rising pressure distortion, high-speed shutter, realistic fabric movement, dynamic pose, 24mm wide lens. P4 [0:03.75–0:05.00] Macro photography of a swirling black ink whirlpool on a flat surface, spiral formation, high-contrast black and white tones, studio lighting, ultra-sharp focus, realistic fluid dynamics. Character visible at the edge or reflected in the ink vortex. P5 [0:05.00–0:06.25] Photorealistic dynamic action shot, woman with pink hair dodging low, black ink ribbons whipping around her body, motion blur, hard dramatic lighting, gritty urban backdrop, athletic wear, cinematic color grade. P6 [0:06.25–0:07.50] Real photography, woman with pink hair sprinting toward camera, black ink streaks rushing past her, wind-blown hair, sharp focus on face, motion-blurred background, dramatic backlight silhouette. P7 [0:07.50–0:08.75] Cinematic photorealistic shot, woman with pink hair bursting through a shattering surface, fragmented ink-soaked debris suspended in air, dynamic landing pose, explosive backlighting, dust and ink particles, deep focus, IMAX-style drama. P8 [0:08.75–0:10.00] Photorealistic cinematic medium shot, young woman with pink hair standing upright facing camera with direct eye contact, black ink dripping from both fists, ink-splattered clothes, defiant expression, dramatic backlight, ink mist settling around her feet, shallow depth of field, gritty atmosphere, Canon R5, 85mm f/1.4. Global Instruction: Use the provided Higgsfield logo reference image exactly as supplied. Do not alter the logo design or the “Higgsfield” text. Keep the branding clearly visible throughout every shot and until the final frame.
```

#### 📌 Details
- Ratio: `1.77` | Duration: `10.08s`

---

<!-- STATS_END -->
