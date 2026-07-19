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
- Total Prompts: **7959**
- Updated Today (UTC 2026-07-19): **214**

## 🎬 Today's Updates
### 🎬 Rainy Night Magic Tree
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10419.jpg" width="480" alt="SD2_10419"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/night-rain-magic-tree-SD2_10419">🌐 Watch Online</a>

#### 📝 Prompt
```
Night rain, reflections on the pavement, a glowing magical tree, and the lights of the city—it's the perfect blend of magic and modernity.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.03s`

---

### 🎬 Cinematic Single Take Extreme Surfing
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10418.jpg" width="480" alt="SD2_10418"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-extreme-surfing-SD2_10418">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a hyper-cinematic 15-second continuous single-take extreme surfing video. Strictly use the provided character chart as a reference for female [@图片1]'s identity, face, pale skin, bright eyes, long straight black hair, athletic build, white-navy surf outfit, white/blue surfboard, and all equipment. No changes to her identity, clothing, board, or equipment are allowed. Only one surfer appears in the entire video: this woman. Do not display other surfers, surfers, swimmers, boats, silhouettes, or background figures anywhere in the ocean or sky. She was completely alone. Scene: Open ocean, under bright sunlight, deep blue-green water, sunlight reflection, undulating waves, splashing seawater, and powerful winds. The atmosphere must feel raw, fast, dangerous, cinematic, and physically believable. Video style: A continuous 15-second shot, no editing, no hidden clips, no transitions, no montage. Surreal motion, blurred natural motion, water droplets on camera, splashing seawater, wind noise, tension in the strings, the sound of boards scraping across the water, and believable body weight adjustments. No text, no logos, no subtitles, no music, no soundtrack, preserves live sound effects. The video begins with the woman standing on a surfboard, rapidly moving forward under the gentle waves, facing the camera from a strong frontal perspective. The camera is very close to her upper body and face, slightly lowered, showing She's focused eyes, wind-blown wet black hair, constantly adjusting posture, and facial expressions. She appears calm, fearless, and completely in control. The camera moves smoothly downward, keeping in front of her, then slides continuously around her body toward a low tracking angle near the surfboard. Once behind her, the camera stays extremely low, level with the board, close to the water, slightly shifting from behind to the tail and edge positions, as if chasing a board crossing the ocean. She accelerated fiercely, leaning back against the momentum of the waves. The board quickly glides across the water, cutting into small waves. She lowered one hand, gliding her fingertips across the water, splashing water behind the low-angle camera. The camera captures water touches, board vibrations, leg force, speed, and splashes. Then it accelerates into a rising wave. The waves grew louder and larger, and she pressed against the edge of the board. She soared powerfully into the air. The entire jump is kept in the same continuous shot. As she rises, time shifts to dramatic slow motion. Water droplets floated in the air, her hair lifted in the wind, and the surfboard was clearly visible. While in the air, she performs a controlled surf spin. The camera stays low, slightly behind and below the action, looking up to watch her rotate. She briefly turns her face toward the camera, her gaze intense and focused, then naturally continues. At the apex, slow motion becomes even more dramatic. She reached down, grabbed the surfboard with one hand, and adjusted her posture with the other to maintain balance. The board is close to the camera, with the white/teal design clearly visible, splashes below, and a vast ocean stretching out behind it. This was the main viral highlight. She released the board, completed the spin, and landed cleanly with a violent, explosive splash. The lens stays at a low level on the water at the back of the board, closely following the impact. She squatted down, instantly regained speed, continued to ride through the waves, and slid quickly along the side wall of the semicircular dome cave formed by another big wave, following the shot, with splashes filling the frame. The video quickly moves through her in the same continuous single shot, ending with a hero's perspective of a frontal close-up of her face.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Tteokbokki Mukbang ASMR Night
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10417.jpg" width="480" alt="SD2_10417"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/tteokbokki-mukbang-asmr-night-SD2_10417">🌐 Watch Online</a>

#### 📝 Prompt
```
Mukbang ASMR Vlog CAMERA/LOOK: Handheld DV 16mm camcorder selfie-POV (JIYU holds the camera and films herself; no separate camera person visible), occasionally propped for stability. Shaky, imperfect framing, delayed focus pulls, clumsy zooms, occasional face-cut-off selfie framing. Soft/blurry tape quality, faint noise, bloomy highlights, flickering auto-exposure, muted contrast, natural skin tones. STYLE: Mukbang x ASMR-lite. Quiet, minimal dialogue, whispered/soft-spoken lines only. Slow cuts, close framing, stillness. Ambient sound focus: chopsticks, soft bubbling sauce, steam, gentle chewing, quiet sighs. JIYU: Korean, age 20, extremely cute rabbit-like face — big round eyes, under-eye aegyo-sal, slightly chubby cheeks, soft coral lips, youthful glow. Bangs with shoulder-length wavy hair (soft light brown / ash brown). Petite height, casual but curvy build. Cozy grey zip-up hoodie loungewear set (zipper open, white inner peeking), minimal jewelry. Soft, relaxed energy; occasional glances/smiles at lens. SETTING: Dorm room at night, warm lamp light, small food table, camera angled to capture her + food, low ambient noise. STORYBOARD: (2s, propped, medium) Sits on floor cushion, adjusts camera, soft wave. 대사: "안녕 애들아... 진짜 인기 있는 떡볶이 시켜봤어." (2s, close insert) Steam off a bowl of tteokbokki, chopsticks lift one piece — soft bubbling sound only. (2s, handheld, face track) Slow bite, eyes close, soft exhale. 대사: "음... 진짜 맛있다." (1.5s, macro, shallow DOF) Chopsticks lift another piece of tteokbokki, glossy sauce glistening, steam close-up — soft clink sound only. (2s, medium) Warm smile at lens, head tilt. 대사: "이거 나중에 또 시켜 먹어야지." (2s, close/propped) Quiet sip, sets cup down, content sigh — ambient only. (1.5s, tight punch-in) Chin on hand, gazing at the tteokbokki. 대사: "아 이러고 살찌면 어떡하지." (2s, slow fade-out) Reaches to end recording, soft smile, hand blocks lens as it cuts. 대사: "다들 잘 자." CONSISTENCY: Keep JIYU's exact face, hair, and outfit identical in every shot — never morph into a different person. Natural, realistic hands and chopstick handling (no distorted fingers). No on-screen text, subtitles, logos, or watermarks.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

### 🎬 Undersea Tunnel Escape Action Sequence
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10416.jpg" width="480" alt="SD2_10416"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/undersea-tunnel-escape-SD2_10416">🌐 Watch Online</a>

#### 📝 Prompt
```
Hyper-realistic cinematic action sequence, 15 seconds, 16:9. Deep beneath the ocean at night. A futuristic transparent glass transit tunnel runs along the ocean floor, surrounded by a massive black abyss. Outside the curved reinforced glass: dark water, glowing marine life, distant gigantic shadows moving through the depths. Inside: flashing blue emergency lights, wet reflective floor, warning alarms. The scene begins already in chaos. Two covert agents, a man and a woman in sleek black tactical clothing, faces visible, no helmets, no masks, are sprinting at maximum speed through the tunnel. They are not jogging. They are running for their lives. Their breathing is heavy, arms pumping violently, footsteps exploding through ankle-deep water. The camera flies backward inches in front of them, shaking with their movement. Behind them, security forces sprint after them. The tunnel suddenly violently shakes. A deep crack rips across the glass wall. The agents do not stop. They accelerate. Glass fractures race across the tunnel like lightning. Water blasts through in powerful jets, throwing spray across their faces. They duck under falling metal beams while maintaining full speed. The floor becomes flooded, forcing them to slide and fight for balance without slowing. The camera switches to a side tracking shot as the tunnel begins collapsing behind them. A massive section of glass ruptures. A violent ocean surge tears through the corridor, swallowing the security team and racing toward the agents like a tsunami inside the tunnel. Ahead, the blast door is still open. They are almost there. Emergency sensors detect the incoming flood. The blast door begins closing. The agents are only meters away. They sprint harder than ever. Their feet slip on the flooded floor. One falls forward, the other grabs their arm and yanks them upright while both continue running. No hesitation. The water wave is seconds behind them. The door opening becomes smaller. They dive through the gap at full speed. The blast door slams shut immediately behind them as the ocean crashes into it with explosive force, shaking the entire chamber. The agents slide across the floor, soaked and exhausted, while water pounds against the sealed door. Style: ultra-realistic Hollywood action movie, IMAX scale, extreme urgency, frantic movement, desperate sprinting, explosive physical reactions, realistic human motion, dynamic handheld camera, aggressive tracking shots, realistic water physics, collapsing structure, high tension, no dialogue, no slow motion, no text, no logos, no cartoon style.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

### 🎬 Dry Saturday Golf Stare
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10415.jpg" width="480" alt="SD2_10415"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dry-saturday-golf-stare-SD2_10415">🌐 Watch Online</a>

#### 📝 Prompt
```
Scene & Mood: Realistic golden hour golf course close up with dry Saturday comedy, warm light, relaxed deadpan energy. Frame Map: Tight chest up frame. image1 stays centered, very close to lens, face upper middle, shoulders low frame. Soft blurred fairway, trees, and hills behind him. Eyeline into camera through sunglasses. Subject Lock image1: Preserve the same face, hair under backward gray cap, sunglasses, light skin, faded blue T shirt, white glove, body shape, silhouette, and unimpressed expression. image1 keeps the same face, hair, wardrobe, body shape, and silhouette throughout. Cross-Frame Rules: Keep him centered, close, and facing camera. No identity drift, wardrobe change, extra people, added logos, or exaggerated smile. Movement: Shot 1 (0–10s): He leans slightly closer, holds a dry stare, gives a tiny nod and faint almost-smirk as the voiceover says, “Good morning everyone and happy Saturday.” Subtle breathing, small jaw tension, gloved hand near hip, shirt and hair moving in light breeze. Camera has gentle handheld breath. Last Frame: End centered in the same tight close-up, leaning toward lens with sunglasses on deadpan stare and faint smirk. Background stays soft. Camera nearly locked. No on-screen text, no captions, no signage typography, no rendered text in the frame. World Plate: Open golf course at golden hour, green fairway, distant trees, low hills, amber side light, soft shadows, mild haze, warm green blue gold palette. Sound Bed: Clean voiceover: “Good morning everyone and happy Saturday.” Light breeze, faint birds, outdoor golf course tone. No music, no song, no score. Capture Realism: Natural matte skin, real pores, worn cotton, soft glove texture, subtle sunglass reflections, lifted shadows, soft highlight rolloff, mild grain, no plastic gloss. Camera Capture: 10 seconds, 40mm lens, shallow depth, realistic handheld close up, 24fps, 180 degree shutter, fine 35mm grain, warm natural grade.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.08s`

---

### 🎬 Leaked Drone Becomes Cinematic
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10413.jpg" width="480" alt="SD2_10413"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/drone-leak-cinematic-SD2_10413">🌐 Watch Online</a>

#### 📝 Prompt
```
Hyperrealistic vertical video, 15 seconds, one continuous unbroken camera move, shot like leaked drone news footage that gradually becomes cinematic — real-world physics, natural motion blur, subtle sensor grain, no color grading at first.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.08s`

---

### 🎬 Lone Sword Under Coral Moon
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10412.jpg" width="480" alt="SD2_10412"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/lone-sword-coral-moon-SD2_10412">🌐 Watch Online</a>

#### 📝 Prompt
```
Use image_1 as the visual storyboard anchor for shot order, camera grammar, staging, prop/effect state, screen direction, and spatial continuity. Render the final filmed scene, not the sheet; do not add events outside this prompt. Read each panel as a separate full-frame shot sample. Preserve the same C#/object identities, avoid split-screen or quadrant frames, and do not show any creature reflected in the sword. Use <<<image_1>>> as the sole authority for C1 final appearance, face, body, wardrobe, proportions, materials, sword scale, and likeness; storyboard silhouettes are staging references only. VISUAL STYLE: High-speed sakuga 2D anime action; flat graphic fills, sharp edges, hard shadows, no painterly textures, no realism. NOT 3D, NOT CGI, NOT grey, NOT desaturated. COLOR PALETTE: Coral-pink field and sky pulled directly from the character reference background; off-white moon disk; all enemies rendered as pure flat black silhouettes with no surface detail; C1 wardrobe in white and black only; glowing white-blue katana blade edge; black ink-blood burst effects on impact. AUDIO: Cloth snaps, grass cuts, blade rings, wet ink impacts, creature breath, staccato footwork, and abrupt near-silence before the final hit; no melodic score, only diegetic impact rhythm and flash-cut stings. ENVIRONMENT: Open grass field under a huge moon disk, low cloud blocks at the horizon, sparse grass, empty graphic sky, no extra fighters. Field and sky are saturated coral-pink, no grey or blue atmosphere. EMOTIONAL GUIDANCE: C1 starts statuesque and unimpressed, then becomes a streaking blade line; the creatures lose ground through recoil, air time, and impact poses. RHYTHM + ESCALATION: One held poster-frame breath detonates into sakuga smear cuts, speed ramps, whip cuts, burst cuts, and one-frame impact flashes, peaking in a moon-backed final stance with two threats still alive. BEATS: P01: Low wide hero frame: C1 stands center-left, long katana glowing diagonally across the body, moon behind, oversized white jacket open and skirt settled; C2, C3, C4, and C5 wait at the grass edge as flat black silhouettes. P02: Grass-level threat: C3 claws into foreground left as a black silhouette shape; C1 drops into a sprinter crouch and snaps the blade tip screen right as C2 and C4 surge behind; hard cut on the claw. P03: Tight hand-and-blade insert: C1's grip on the katana handle slides, blade flare pops near the hand, wrist twists into a white smear frame; flash cut into launch. P04: Compressed profile medium: C1 becomes a horizontal slash streak through C3; black ink-blood tears open behind the crawler and the body whips low into grass. P05: Low impact wide: C2 black silhouette charges from screen left; C1 meets it with a two-hand cross-body guard, blade bending the attack line, burst cut punching the contact; white jacket billowing from impact force. P06: Over-shoulder from C2: C1 corkscrews under the brute's arm, black pleated skirt and white hair snapping outward, sword arc whipping up toward C4 overhead. P07: High diagonal wide: C1 air-dashes screen right across the field lane, fallen C3 below, C2 staggered left, C4 diving from upper right, C5 small at the moon line; all enemies remain flat black silhouettes. P08: Ground insert: C1's feet skid through grass beside one black ink streak, heel carving a crescent, blade sweeping low as a flash-cut smear hides the angle change. P09: Frontal medium hit: C1 springs upward and drives the long katana into C4 midair, clean glowing blade edge forward, black ink-blood exploding behind the black wing silhouette; smash cut at contact. P10: Creature POV from C5: C1 rocket-dashes into lens with glowing sword point forward, harness straps and jacket trailing, C2 cropped left and fallen C4 dropping right; speed ramp snaps from freeze to attack. P11: Side silhouette payoff: C1 lunges full-body in a long smear pose and slices past C5 at the moon edge; black ink-blood arcs upward while C2 recoils far left; hair and jacket cape outward. P12: Low static wide release: C1 lands center foreground in a sliding stop with glowing katana across the body, jacket settling, C3 and C4 fallen around the lane, C2 alive far left, wounded C5 far right. STORYBOARD PROMPT: Create a 16:9 kinetic sword-combat storyboard sheet image. [SUBJECT] A polished modern-minimal production board for a lone sword fighter turning a poised moonlit stance into high-speed creature combat. Communicate full-frame camera angles, sword state, impact poses, liquid hit effects, screen direction, and enemy state across twelve panels. [HEADER] Design an artistic production-board header with scene-aware typography, thin rules, clear hierarchy, generous spacing, and restrained graphic treatment outside panel interiors. The header must contain exactly these two quoted lines: "Blade Under Moon" "A poised sword stance detonates into twelve sakuga strike frames." [BOARD STRUCTURE] Use AUTO layout with 12 panels. Use compact panel headers exactly in this format: `P## / shot tag / beat name`. Draw one panel per BEATS entry in P## order. [VISUAL STYLE] Panel interiors are silent ultra-clean blocking thumbnails: open-outline silhouettes, thin medium-light graphite linework, broad negative space, and only anchors needed for pose, contact, direction, smear shape, and spatial result. Show only outer body-mass and limb contours: no face, anatomy, clothing detail, texture, tonal modeling, or shaded fill. Keep panel interiors monochrome. Describe final-video colored elements by color-neutral shape/function here; final color and palette stay only in `prompt_video.txt`. [REFERENCES] Image A: lead silhouette, hair mass, shirt-and-skirt/trouser block, long sword scale, hand placement, moon-and-cloud composition only. [CONTINUITY] Keep role identity, entity count, sword state, liquid-effect origin, screen direction, geography, and spatial result consistent. Each panel is one full-frame composition, never a split-screen, quadrant, four-way frame, inset, or multi-view panel. The sword may show shine or flare shape, but never a creature reflection. Fallen, marked, and damaged states are the same role/object continuing across panels, not repeated extra copies. Each panel is one frozen instant with one pose/state per role/object; avoid before/after wording such as `then`, `after`, `before`, `first`, `next`, or `later`. [COUNT LOCK] Across the sequence preserve exactly one lead fighter, one sword, and four named enemy roles: horned brute, low crawler, winged attacker, rear leaper. Draw only roles named in each beat; never add extra creatures, duplicate fallen roles, ghost poses, split-screen copies, or reflected creatures. Fallen low crawler, fallen winged attacker, and wounded rear leaper are continuing states when named, not new bodies. [TEXT RULES] Visible text: only the two quoted header lines and compact panel headers. Do not render section labels, role names, entity IDs, notes, arrows, callouts, or annotations. [CONSTRAINTS] Avoid logos, watermarks, overlays, extra panels, split-screen panels, quadrant frames, insets, sword reflections of creatures, finished illustration, dense detail, panel color, duplicate/ghost entities, visible IDs, and inconsistent counts. [BEATS] Draw one storyboard panel per visual BEAT: BEATS: P01 / low moon stance / blade held: low wide full-frame view; lead fighter stands center-left with long sword held diagonally across body, moon disk behind, four enemy silhouettes wait along the grass edge. P02 / ground threat / sprinter drop: grass-height close-wide; low crawler claw dominates foreground left, lead fighter crouches like a sprinter with sword tip screen right, horned brute and winged attacker surge behind. P03 / object flare / wrist snap: tight insert on lead fighter hands and long sword; one flare shape sits near the grip, wrist angle twists hard, blade surface stays clean. P04 / impact profile / slash streak: hip
```

#### 📌 Details
- Ratio: `0.88` | Duration: `15.0s`

---

### 🎬 Tokyo Hypercar Chase Mayhem
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10411.jpg" width="480" alt="SD2_10411"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/tokyo-hypercar-chase-mayhem-SD2_10411">🌐 Watch Online</a>

#### 📝 Prompt
```
This is an intense chase scene set in a daytime urban area. Extremely realistic action scenes from a live-action Hollywood blockbuster movie. Photorealistic visuals that completely eliminate the effects of CGI. A beautiful young Japanese female driver is piloting a futuristic hypercar. Her face matches the attached reference image perfectly. The car is a futuristic hypercar with an aggressive design (heavy, authentic texture). Scene flow: - A military helicopter rapidly approaches from above, sped through the high-rise district and congested lanes while being chased by military drones. - Squeeze into a traffic jam, drive in the opposite lane at high speed, and squeeze through just as tightly as possible. Drones explode one after another around the area. - Finally, he rams head-on at high speed into a giant advertising billboard along the highway (a drinking water sign with a beautiful woman posing in a gravure pose), shattering it to pieces. Amid flying debris, it sped at super speed right in front of the camera and disappeared. A massive chain explosion occurs behind the scenes. Hollywood-level live-action VFX, natural texture, powerful camera work, 8K, completely eliminating any CG odor.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `26.03s`

---

### 🎬 Dam Escape: Agents on the Run
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10409.jpg" width="480" alt="SD2_10409"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dam-escape-agents-run-SD2_10409">🌐 Watch Online</a>

#### 📝 Prompt
```
Hyper-realistic cinematic action sequence, 15 seconds, aspect ratio 16:9. Daytime during a violent storm. Two agents, one man and one woman, run along the top of a massive concrete dam while a security team chases behind them. The dam is huge and exposed, with narrow maintenance walkways, steel railings, warning lights, control boxes, heavy spray, and roaring water far below. Dark clouds gather overhead, wind drives rain across the structure, and the entire dam feels unstable under growing pressure. Wide opening shot: the two agents sprint along the top of the dam at full speed while security appears behind them, closing in. Water crashes below on one side, and storm wind pushes mist and spray across the walkway. Tracking shot: the agents keep running along the narrow concrete path as warning alarms flash. Ahead, massive spillway gates begin opening one by one. The structure shudders under the force, water erupts downward in huge torrents, and the agents struggle to keep balance on the slick surface. Side shot: the pressure increases. The dam shakes harder as more gates open. Spray blasts across the walkway, metal railings rattle, and one section of the path cracks near the edge. The agents keep moving, ducking around control structures and staying ahead of the security team. Final 5 seconds: the action becomes extreme. A maintenance section ahead partially breaks and drops, creating a gap in the walkway. The agents accelerate into a final desperate sprint, leap across the broken section, land hard, and keep moving while the spillway fully opens beside them. Water explodes downward with enormous force, the whole structure trembles, and the security team is slowed behind by spray and collapsing debris. Final moment: the two agents reach a safer platform near a control access door while the open spillway roars beside them, with storm, mist, and massive water pressure filling the frame. Style: hyper-realistic, cinematic, fast-paced, intense, stressful, clear readable action, strong sense of scale and danger, storm, rain, concrete dam, roaring water, heavy spray, shaking structure, dynamic but readable camera movement, no text, no logos, no cartoon style, no slow motion, no famous celebrity faces, no recognizable actors, no movie-star resemblance, no public-figure likenesses, no clear facial close-ups. Keep proportions. Keep style and features. Aspect ratio 16:9.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

### 🎬 Crypto Nerd's AI Content Grind
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10407.jpg" width="480" alt="SD2_10407"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/crypto-ai-creator-daily-SD2_10407">🌐 Watch Online</a>

#### 📝 Prompt
```
Photorealistic behind-the-scenes smartphone vlog footage of a crypto/web3 enthusiast and AI content creator. Faux vertical smartphone footage naturally cropped into 16:9. Authentic handheld phone aesthetic. No cinematic color grading, no HDR, no beauty filters. Feels like genuine casual vlog footage. Character: A white stylized 3D mascot-like character (exactly like the reference image <<<Image1>>> ) with a smooth white body, black sunglasses, and a distinctive white mohawk/crest on its head. The character has a simple, expressive face and moves in a slightly exaggerated but natural way. Maintain the exact same design, proportions, and identity from the reference image in every scene. Setting: A simple, slightly messy small apartment. Clothes on the chair, multiple monitors and gadgets on the desk, empty coffee cups, snack wrappers, tangled cables, and crypto-themed posters on the wall. Natural and lived-in feeling. Lighting: Starts with soft morning light coming through the window, gradually transitions into warm afternoon and evening indoor lighting. Natural smartphone exposure changes. Camera: Simulated smartphone footage with gentle handheld movement, natural walking, subtle autofocus breathing, occasional imperfect framing, and realistic phone compression. Feels like a friend casually filming. Style & Mood: Casual, relatable, and a bit funny. The character has the personality of a chill but passionate crypto and AI content creator — sometimes excited, sometimes chaotic, but always sincere. Scene Sequence: CUT 1 — Waking Up Morning. The character slowly wakes up in bed, still wearing sunglasses. It sits up, looks around the messy room, then dramatically falls back onto the pillow for a few seconds before forcing itself to get up. It stretches lazily. CUT 2 — Morning Coffee & Checking Charts The character walks to the kitchen (still in pajamas or oversized shirt), makes coffee, then sits in front of multiple monitors. It excitedly checks crypto charts and AI tools while talking to itself. It suddenly reacts to a big green candle. CUT 3 — Content Creation Chaos The character is at the desk trying to create content. It’s switching between different AI tools, recording voiceovers, and getting slightly overwhelmed with too many tabs open. It accidentally knocks over a cup while celebrating a good prompt. CUT 4 — Midday Break The character takes a break, eats instant noodles while scrolling through Twitter/X and Discord on its phone. It laughs at a meme, then suddenly gets an idea and rushes back to the computer. CUT 5 — Evening Work Session Late afternoon turning into evening. The room is messier now. The character is deeply focused on editing a video using multiple AI tools. It talks to the camera while working, explaining what it’s doing in a casual way. CUT 6 — Late Night Wind Down Night time. The character is tired but satisfied. It cleans up a bit (half-heartedly), sits on
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.2s`

---

### 🎬 Korean Courtyard Candlelit Romance
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10405.jpg" width="480" alt="SD2_10405"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-courtyard-candlelit-romance-SD2_10405">🌐 Watch Online</a>

#### 📝 Prompt
```
A young Korean couple in their mid-20s enjoys a romantic candlelit dinner together in a beautiful traditional Korean-style wooden courtyard at night. The woman has shoulder-length wavy black hair with soft curtain bangs and wears an elegant off-white blouse with navy trousers and delicate gold jewelry. The man has neatly styled black hair with light stubble and wears a light gray linen shirt with rolled sleeves and black trousers. Maintain perfect facial consistency, hairstyles, outfits, and loving chemistry throughout the entire video. The setting features warm candlelight, paper lanterns, traditional wooden architecture, tiled roofs, flowering plants, and a cozy outdoor dining table. A peaceful city skyline glows softly in the distance. The environment is completely original and fictional with no resemblance to any specific real-world location or landmark. Ultra-realistic cinematic night photography, warm golden lighting, cool blue ambient light, soft volumetric lighting, realistic skin textures, shallow depth of field, natural bokeh, premium cinematic color grading, subtle film grain, smooth stabilized camera movement, gentle push-ins, slow cinematic orbits, elegant rack focus, horizontal 16:9. 00:00–00:03 Wide establishing shot as the couple walks onto the candlelit terrace, smiling warmly at each other before taking their seats. 00:03–00:06 The man gently lights the centerpiece candle while the woman watches with an affectionate smile. Close-up of their faces glowing in the candlelight. 00:06–00:09 They raise elegant glasses for a romantic toast, maintaining warm eye contact before taking a sip together. 00:09–00:12 They enjoy dinner, share food, laugh naturally, and exchange gentle affectionate gestures across the table. 00:12–00:15 Standing beside the terrace railing, they admire the peaceful night view. They then turn toward the camera, smile warmly, raise their glasses, wave together, and the scene fades into soft candle bokeh. Audio: Gentle evening ambience with soft breeze, distant city atmosphere, quiet conversation, subtle wind chimes, delicate acoustic guitar and piano, warm laughter, natural glass clinks, and soft fabric movement. Goal: Create a warm, elegant, emotionally authentic romantic dinner with realistic human expressions, luxurious cinematic lighting, and premium storytelling in a completely original fictional setting.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Rooftop Selfie Sweet Moment
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10404.jpg" width="480" alt="SD2_10404"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rooftop-selfie-sweet-moment-SD2_10404">🌐 Watch Online</a>

#### 📝 Prompt
```
@image_1 is used as a reference for people, clothing, and locations. @image_1 two people are taking selfies on the rooftop terrace. Action: Two people smile while looking at the screen. After the shoot, they peer into the screen, bring their faces close, and laugh together as if watching the scene. Her bangs swayed in the wind. Line: "Ah, I'm sleeping," "It's true, one more time," she says with a laugh. Sound: BGM: None / Environmental sounds and dialogue: Yes (wind sound, voices from distant terrace seats)
```

#### 📌 Details
- Ratio: `0.57` | Duration: `3.76s`

---

### 🎬 White Wolf Awakens Ancient Guardian
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10403.jpg" width="480" alt="SD2_10403"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/white-wolf-ancient-guardian-SD2_10403">🌐 Watch Online</a>

#### 📝 Prompt
```
15-Second Cinematic Prompt (Hollywood Trailer Style) Scene 1 (0–3 sec) – The Hunt Begins A violent blizzard sweeps across the Swiss Alps beneath a glowing full moon. The camera starts with an epic aerial shot of endless snow-covered peaks before descending into a frozen pine forest. A lone hunter in a weathered leather coat and fur-lined hood kneels beside enormous wolf footprints—far larger than any ordinary wolf. He brushes snow away from the tracks, realizing they are fresh. He loads a single silver bullet into his antique rifle, lifts an oil lantern, and steps into the darkness. The icy wind whistles through the trees, and a distant wolf howl echoes across the mountains. Scene 2 (3–7 sec) – The White Guardian The hunter reaches a frozen cliff overlooking the valley. Standing silently on the edge is a majestic white wolf, illuminated by cold moonlight. Its thick fur moves naturally in the wind, and its glowing blue eyes lock onto the hunter. Instead of attacking, the wolf slowly turns and walks toward a hidden mountain pass, pausing several times to look back as if guiding him. The hunter lowers his rifle and follows through a narrow canyon where ancient stone carvings, half-buried in snow, hint at a forgotten civilization. Scene 3 (7–11 sec) – The Awakening The wolf stops before a colossal glacier. Silence fills the valley. Suddenly the ground begins to shake violently. Massive cracks race across the frozen mountain, glowing with blue energy beneath the ice. Entire sections of the glacier collapse with thunderous force. From deep beneath the ice, an enormous stone hand slowly pushes through the glacier. Snow avalanches down the cliffs as the hunter stumbles backward in disbelief. The wolf stands perfectly still, staring at the awakening giant without fear. Scene 4 (11–15 sec) – The Guardian's Truth The hunter instinctively raises his rifle toward the emerging giant. Before he can pull the trigger, the white wolf steps directly in front of him, shielding the mountain. Time seems to slow. The hunter looks into the wolf's calm blue eyes and realizes the truth—it was never leading him to prey, but protecting an ancient guardian imprisoned beneath the Alps. Suddenly, two gigantic glowing blue eyes open inside the mountain. A deep roar echoes through the valley as snow erupts into the air. The wolf howls toward the sky while the camera rapidly pulls back, revealing the immense frozen landscape beneath the moon. Cut to black.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.9s`

---

### 🎬 Iron Lotus Strike Shatters Power
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10402.jpg" width="480" alt="SD2_10402"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/iron-lotus-strike-SD2_10402">🌐 Watch Online</a>

#### 📝 Prompt
```
Iron Lotus Strike — one fighter's silent precision breaks raw power in four brutal seconds, silver energy surging, torchlight flaring, until the ground shakes with victory.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 The Man Who Remembers Tomorrow
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10401.jpg" width="480" alt="SD2_10401"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/man-who-remembers-tomorrow-SD2_10401">🌐 Watch Online</a>

#### 📝 Prompt
```
TITLE:THE MAN WHO REMEMBERS TOMORROW Style: Ultra-realistic cinematic movie trailer, psychological thriller, dark neo-noir, Hollywood quality, IMAX, anamorphic lens flares, volumetric lighting, dramatic shadows, shallow depth of field, realistic facial expressions, handheld and cinematic dolly shots, intense orchestral score with deep bass hits, suspenseful sound design, 4K photorealistic. 0:00–0:03 Fade in from black. A deserted underground subway station at 3:00 AM. Flickering fluorescent lights. The camera slowly pushes toward a lone man lying on a cold concrete floor. He suddenly opens his eyes, breathing heavily. SFX: Low cinematic boom. Electrical buzzing. Text on screen:"Some futures refuse to stay hidden." --- 0:03–0:06 Close-up of the man's wristwatch. The second hand jerks violently before stopping completely. Extreme close-up of his eyes reflecting the flickering lights. Voice-over (calm, haunted): I don't dream about tomorrow..." The soundtrack begins building with slow strings. --- 0:06–0:09 Rapid cinematic montage. • A red balloon slips from a child's hand and floats into a gray sky. • A speeding black sedan races toward a busy intersection. • A terrified woman turns suddenly as if someone called her name. • A cracked digital clock flashes 00:00 Each shot lasts less than one second with dramatic trailer transitions. --- 0:09–0:12 The man stands in the middle of a rain-soaked city street. Everything around him moves in slow motion except him. He stares directly into the camera. Voice-over: I remember it. The music cuts abruptly to silence. 0:12–0:16 Rain pours across empty streets. The man runs through crowds while everyone else appears frozen in time. The camera circles him in a fast cinematic orbit. He suddenly stops. At the far end of the street, a mysterious stranger is staring directly at him. The stranger slowly smiles. A deep bass impact shakes the soundtrack. --- 0:16–0:20 Quick trailer montage. • Glass explodes in slow motion. • Police lights flash through thick fog. • Long, dark hallways stretch endlessly. • A shadow moves just beyond the edge of the frame. • The man sprints through an abandoned building. Voice-over: "Every time I change the future..." The music rises rapidly. --- 0:20–0:24 Silence. Extreme close-up of the stranger's face. He calmly whispers: "You're already too late." The camera slowly pushes in as his smile widens unnaturally. --- 0:24–0:27 Hard cut to black. One loud heartbeat echoes. A faint ticking clock begins. Title appears in metallic cinematic typography: THE MAN WHO REMEMBERS TOMORROW Tagline: "The future is watching."
```

#### 📌 Details
- Ratio: `1.78` | Duration: `25.33s`

---

<!-- STATS_END -->
