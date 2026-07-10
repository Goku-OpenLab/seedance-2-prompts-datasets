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
- Total Prompts: **7013**
- Updated Today (UTC 2026-07-10): **13**

## 🎬 Today's Updates
### 🎬 World Cup Bicycle Kick Cliffhanger
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07673.jpg" width="480" alt="SD2_07673"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/world-cup-bicycle-kick-cliffhanger-SD2_07673">🌐 Watch Online</a>

#### 📝 Prompt
```
PART 1 (0–15s) Cut 1 (0–5s) — Dressing Room Flashback Mateo sits alone in the empty dressing room before kickoff. Slow push-in. Match cut into a cool-toned flashback where Elena stands in a doorway. Elena: "I'm done with you." She walks away. Hard cut back to the present as Mateo grabs his captain's armband and heads toward the tunnel. Cut 2 (5–10s) — The Final Begins Mateo walks alone from the tunnel into the roaring World Cup Final. Crane shot reveals the packed stadium before dropping to pitch level. He receives an easy pass, hesitates, and loses possession. Cut 3 (10–15s) — The Look A defender taunts Mateo while he jogs back. Defender: "Where's your head today, Reyes?" The Crowd Cam finds Elena on the giant jumbotron. She cups her hands and shouts, Elena: "PLAY LIKE YOU MEAN IT!" Mateo looks up. Their eyes lock across the stadium as time slows. PART 2 (15–30s) Cut 4 (15–19s) — Turning Point Low-angle tracking shot follows Mateo intercepting the ball and dribbling past two defenders. Cut to Elena watching anxiously from the stands. Cut 5 (19–24s) — The Goal Side tracking camera follows Mateo the entire time. A perfect cross arrives. Mateo performs a spectacular bicycle kick while the camera orbits around him. Keep Mateo fully visible throughout the kick. Cut to the ball flying into the top corner. Immediately hard cut after the goal. No celebration. No goal-net shots. Cut 6 (24–30s) — Reunion & Cliffhanger Mateo is already sprinting toward the spectator barrier. Elena rushes forward. Mateo: "You came back." Elena: "I had to tell you something." Just before their hands touch, a mysterious man in a dark coat steps in behind Elena and firmly grabs her shoulder. His body is visible, but his face remains hidden. Elena turns in fear. Mateo freezes. Hard cut to black. End Card EPISODE 1 COMING SOON
```

#### 📌 Details
- Ratio: `0.56` | Duration: `29.47s`

---

### 🎬 Arctic Ice Racer Survival Run
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07671.jpg" width="480" alt="SD2_07671"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/arctic-ice-racer-survival-SD2_07671">🌐 Watch Online</a>

#### 📝 Prompt
```
"A dangerous motorcycle ice racer with frost-covered black racing gear, mirrored helmet visor, and glowing bike headlights cutting through snowstorms. Frozen arctic industrial wasteland during blue-hour twilight. Ice roads, abandoned oil rigs, frozen bridges, collapsing tunnels, snow-covered shipping containers, and blizzard visibility conditions. Dark cinematic techno with deep sub-bass pulses. Ice friction, engine roar, chain vibrations, snow impacts, and freezing wind dominate the soundscape. Ultra-realistic motorsport cinematography mixed with survival thriller aesthetics and premium winter advertising. SHOT 1: Ultra-low front tire tracking shot carving through thick ice dust at dangerous speed. SHOT 2: Whip pan into a near-crash drift around frozen industrial wreckage. SHOT 3: Wide aerial shot showing the motorcycle racing across gigantic frozen ocean surfaces between abandoned structures. SHOT 4: Long-lens jump shot over shattered ice sections while snow explodes behind the bike. SHOT 5: Circular side tracking shot during a prolonged sideways drift inches from a cliff edge. SHOT 6: Final impossible jump through a collapsing frozen tunnel during whiteout conditions. The rider lands violently, fishtails across black ice, then slowly stops beneath flickering industrial lights while snowstorm winds consume the frame. Music cuts instantly."
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.17s`

---

### 🎬 Skater's Handrail Grind Kickflip Combo
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07669.jpg" width="480" alt="SD2_07669"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/skater-handrail-grind-kickflip-SD2_07669">🌐 Watch Online</a>

#### 📝 Prompt
```
Subject: Black man, long dark dreadlocks, black knit beanie, plain black crew neck tee, black cuffed jeans, black gum-sole skate shoes. Starts atop a staircase, ollies onto a handrail, grinds the full rail to the bottom, lands clean, rolls out briefly, then kickflips and lands smoothly. Location: Outdoor CA plaza — light gray concrete stairs, steel center handrail, minimalist architecture, palm trees casting long shadows, bright warm midday sun with natural lens flare. Visual Style: Clean realistic skate-video look — natural skin tones, true-to-life fabric/hair movement, crisp daylight contrast between gray concrete and black wardrobe. Subtle motion blur on fast movement, sharp focus on rider throughout. Camera: Low-angle tracking cam at stair top for the ollie-on, then follows alongside the rail at board height matching descent speed. Brief slow-motion holds at the apex of each trick (ollie-on, kickflip). Ends on steady tracking shot as he rolls away. Timestamps: 00:00–00:01 Set-up: skater at stair top, board angled toward rail, low-angle cam facing him before push-off. 00:01–00:02 Ollie-on: board pops, ~35% slow-mo hold at apex as trucks align over rail top, cam tracks upward with pop. 00:02–00:02.5 Rail contact: trucks land on rail top, full-speed impact, subtle cam jitter to sell contact. 00:02.5–00:05 Grind descent: cam tracks down alongside rail, level with skater grinding full staircase, arms out for balance, stairs blur slightly past cam. 00:05–00:05.5 Landing: pops off rail bottom, lands grind clean on flat ground, cam holds steady at ground level. 00:05.5–00:06.5 Rollout: brief forward roll at normal speed, cam tracks alongside at slight distance. 00:06.5–00:08 Kickflip: board flips mid-air, ~35% slow-mo hold at peak showing rotation, side-profile cam at board height. 00:08–00:09 Kickflip landing: rotation completes, lands squarely on grip tape, full speed resumes, slight cam shake on impact. 00:09–00:10 Resolution: cam pulls back to steady tracking wide shot as he rolls away clean, natural sun flare across frame.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.13s`

---

### 🎬 The Final Replay: Champion's Secret
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07667.jpg" width="480" alt="SD2_07667"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/final-replay-champions-secret-SD2_07667">🌐 Watch Online</a>

#### 📝 Prompt
```
Title: "The Final Replay"** **Duration:** 15 seconds **Style:** Cinematic sports drama, premium feature-film look, realistic lighting, shallow depth of field, emotional performances, ultra-detailed photorealism, dramatic orchestral score with distant crowd ambience. --- ### Scene 1 — Betrayal Revealed (0–5 seconds) Extreme close-up of a smartphone trembling in the blonde woman's hand. On the phone screen is a photograph from the championship celebration: the football star stands proudly beside the World Cup trophy while an elegant dark-haired woman smiles beside him wearing his winner's medal. A tear falls onto the screen, blurring the image. Cut to an intimate blonde woman's devastated expression as ballroom music echoes in the distance. She quietly whispers: **"You promised me this night was ours..."** The camera follows from behind as she stands alone between towering ballroom doors, staring into the celebration beyond. Inside the ballroom: * A World Cup trophy display case glows beneath spotlights. * National flags hang from the ceiling. * Giant replay screens show highlights from the tournament final. * Guests celebrate beneath golden chandeliers. Mood: heartbreak, disbelief, isolation. --- ### Scene 2 — The Secret (5–12 seconds) Cut to the football champion wearing a black suit jacket over an open-collar white shirt, the winner's medal hanging around his neck. He suddenly freezes as if sensing something is wrong. The dark-haired woman approaches confidently through the crowd. She gently places one hand on his arm. A moment later, her fingers lightly touch the medal resting against his chest. Close face-to-face framing. The celebration sounds fade beneath a low dramatic score. She leans closer and softly says: **"Secrets win trophies too."** The man says nothing. His expression shifts from confusion to concern. Mood: tension, manipulation, inner conflict. --- ### Scene 3 — The Final Replay (12–18 seconds) The woman steps back and raises her wine glass with a knowing smile. She glances toward the massive replay screen above the ballroom floor. Football highlights continue playing overhead while guests celebrate below, unaware of the tension unfolding nearby. She slowly lifts the glass to her lips. Without looking at him, she quietly says: **"Wait until they see the final replay."** She takes a slow sip of wine. The camera pushes into the football champion's face as his expression hardens into worry. Cut to the re
```

#### 📌 Details
- Ratio: `0.56` | Duration: `29.2s`

---

### 🎬 Animator Finds Perfect Character Idea
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07666.jpg" width="480" alt="SD2_07666"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/animator-character-inspiration-SD2_07666">🌐 Watch Online</a>

#### 📝 Prompt
```
Part 1: "an animator is struggling to come up with ideas. it's driving him made. he throws out the drawing. tries again. pulls his beard. starts over. paper thrown into trash can. comedy. animation style. multi-scene. high end animation." Part 2 (giving it part 1 video as reference) "continue this video. after struggling to come up with a concept for a character, the artist take a deep breath and say to him self to focus harold. then he draws a beautiful and cool badass princess with a gun. he holds it up proud and whispers that's it. comedy. animation style. multi-scene. high end animation."
```

#### 📌 Details
- Ratio: `1.78` | Duration: `35.29s`

---

### 🎬 The Day Time Stuttered
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07665.jpg" width="480" alt="SD2_07665"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/the-day-time-stuttered-SD2_07665">🌐 Watch Online</a>

#### 📝 Prompt
```
Anamorphic 21:9 ultra-widescreen cinematic, surreal psychological thriller. The Day Time Stuttered. 0-4s: A hyper-busy [Setting]. Suddenly, all sound drops to zero and every person, vehicle, and falling object freezes dead in mid-motion. Camera slowly tracks past static figures. 4-8s: Anamorphic low-angle tracking shot. A lone [Character] walks slowly through the frozen crowd, weaving between mid-air suspended rain droplets and frozen splashes. Oval bokeh glimmers off the motionless water. 8-12s: Extreme vertigo rotation — camera orbits 360 degrees around a frozen explosion of [Particles/Water], showcasing impossible frozen physics. Horizontal neon light flares cut through the frame. 12-15s: The character reaches out to touch a frozen droplet. Time snaps back instantly — ocean of sound returns, water crashes down, people move in fast unison. Camera retreats skyward rapidly in 21:9 glory. Photorealistic 8K, David Fincher style camera precision, anamorphic prime lenses, volumetric rain, temporal lock physics. Anamorphic 21:9 ultra-widescreen cinematic, surreal psychological thriller. The Day Time Stuttered. 0-4s: A hyper-busy rain-slicked New York crosswalk. Suddenly, all sound drops to zero and every person, vehicle, and falling raindrop freezes dead in mid-motion. Camera slowly tracks past static figures. 4-8s: Anamorphic low-angle tracking shot. A lone woman in a yellow coat walks slowly through the frozen crowd, weaving between mid-air suspended rain droplets and frozen yellow cab splashes. Oval bokeh glimmers off the motionless water. 8-12s: Extreme vertigo rotation — camera orbits 360 degrees around a frozen splash from a puddle, showcasing impossible frozen physics. Horizontal neon light flares cut through the frame. 12-15s: The woman reaches out to touch a frozen droplet. Time snaps back instantly — ocean of sound returns, water crashes down, people move in fast unison. Camera retreats skyward rapidly in 21:9 glory. Photorealistic 8K, David Fincher style camera precision, anamorphic prime lenses, volumetric rain, temporal lock physics.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.13s`

---

### 🎬 Sequin Dress Glow Up Transition
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07664.jpg" width="480" alt="SD2_07664"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sequin-dress-glow-up-SD2_07664">🌐 Watch Online</a>

#### 📝 Prompt
```
[Global Vision & Tone] Cinematic 15s sequence, fast-paced viral Douyin "Catch and Wipe" glow-up transition. Core VFX: Object catch, lens-wipe match-cut, slow-motion catwalk, and background extras turning heads. AUDIO INSTRUCTION: STRICTLY NO BACKGROUND MUSIC. Pure ASMR sound design (fabric catching, heavy cloth wiping lens, sharp high heel clicks on wet asphalt, muffled city street ambiance). LIVE-ACTION REAL HUMAN (Female face base input_file_0.png). High-fashion, edgy, and glamorous aesthetic. [Shot Breakdown] [0.0-5.0s] The Reality (Shot 1): Static medium shot in a bright, modern room. The subject (input_file_0.png) stands confidently wearing casual chic minimalist clothing (a stylish sleeveless summer top and denim shorts). Suddenly, a glamorous, highly reflective white sequined mini dress (haute couture) flies into the frame from off-screen. She catches it effortlessly with one hand. She gives a confident smile, takes a dynamic step forward, and aggressively thrusts the sparkling white dress directly into the camera lens, blacking out the screen. ASMR fabric catch and heavy cloth wipe. [5.0-15.0s] The Street Superstar Reveal (5 Rapid Shots): [5.0-6.5s] Shot 2 (Match-Cut Reveal): The fabric is aggressively pulled away! Explosive match-cut. The room dissolves into a vibrant, neon-lit city street at night. The subject is now fully transformed, wearing the exact breathtaking white sequined high-fashion mini dress she caught. The dress sparkles blindingly under the streetlights. [6.5-8.5s] Shot 3 (Dynamic Catwalk): Medium tracking shot moving backward. She executes a powerful, highly confident high-fashion runway strut down the glowing wet asphalt. Her edgy, elegant styling stands out perfectly against the dark city background. [8.5-10.5s] Shot 4 (The Head-Turners): Slow-motion wide tracking shot. As she confidently walks past, blurred background extras (passersby) visibly stop and turn their heads in absolute awe, completely mesmerized by her aura. [10.5-12.5s] Shot 5 (Low-Angle Details): Low-angle tracking shot focusing on her incredibly long legs and sparkling diamond-studded high heels clicking rhythmically on the neon-lit pavement. ASMR sharp heel clicks. [12.5-15.0s] Shot 6 (Final Hold): Extreme close-up on her face. Flawless Douyin-style makeup (glossy lips, glowing glass skin V10.2). Cinematic city wind whips her perfectly styled hair. She stares directly into the lens with an edgy, charismatic, and arrogant smirk, knowing she owns the street. Fades to black. Kodak Vision3 500T film look, beautiful anamorphic lens flares.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `10.13s`

---

### 🎬 Cute Daruma Pose Switch Challenge
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07663.jpg" width="480" alt="SD2_07663"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cute-daruma-pose-switch-SD2_07663">🌐 Watch Online</a>

#### 📝 Prompt
```
Repeat the cycle of looking at the daruma and looking at this one, and then looking at the daruma again. The moment she looks at me, she strikes a cute pose, repeats it over and over at high speed, and when she looks at me, she presses her daruma to her cheek and mutters 'Killaan.'
```

#### 📌 Details
- Ratio: `1.78` | Duration: `8.0s`

---

### 🎬 Moody Red Black Kpop Stage
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07662.jpg" width="480" alt="SD2_07662"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/moody-red-black-kpop-stage-SD2_07662">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: Moody, high contrast K pop, single color saturated set (deep red/crimson with black), theatrical spotlighting, slower beat drop builds Subject: Female idol, structured red and black outfit with sheer/metallic panel details [0:00-0:03] Close up, performer's hand emerges from darkness into a single spotlight, slow reveal of face on the beat, camera pulls back to a full silhouette against a red cyclorama. [0:03-0:07] Wide shot, sharp choreography with strong shadow-play against the red backdrop, camera does a slow lateral track, dramatic spotlight chases her movement. [0:07-0:11] Medium shot, performer delivers hook line seated on a minimalist throne like set piece, quick cut to a dramatic red fog stage backdrop. [0:11-0:15] Triple cut power poses each lit from a different angle (side, top, back), freeze frame hero pose with red haze burst, punch-in, fade to logo.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.13s`

---

### 🎬 Borus Cyber-Jungle Enforcer
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07661.jpg" width="480" alt="SD2_07661"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/borus-cyber-jungle-enforcer-SD2_07661">🌐 Watch Online</a>

#### 📝 Prompt
```
Use @[Borus Character Sheet] as the authoritative character reference for Borus: red ape-like cyber-jungle enforcer, black facial fur, yellow eyes, grey tactical vest with badges, oversized mechanical gauntlets, dark cargo pants, white boots, long red tail.
```

#### 📌 Details
- Ratio: `0.75` | Duration: `12.07s`

---

### 🎬 Flash Prank on Friend
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07659.jpg" width="480" alt="SD2_07659"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/flash-prank-friend-SD2_07659">🌐 Watch Online</a>

#### 📝 Prompt
```
[Character Identity Lock] Use the reference image as the strict identity reference. The young woman must retain exactly the same facial structure, facial features, proportions, skin tone, and overall appearance as the reference throughout the entire video. Her identity and ethnicity must remain completely unchanged regardless of the scene, lighting, facial expressions, or speech. Create an ultra-realistic handheld smartphone candid video set at night or in a dimly lit indoor environment. The camera is very close to the subject, but avoid extreme face cropping. Keep the top of her head, part of her shoulders, and her raised hand visible in frame. The shot should feel as though a close friend is holding a phone nearby and suddenly turns on the flash to tease her. A harsh smartphone flash fires directly at her face, causing the lighting to become suddenly much brighter. She instinctively raises one hand in front of her forehead and eyes to block the light. Her palm and fingers naturally enter the foreground, creating realistic partial occlusion without completely covering her face or facial features. She tilts her head slightly, squints naturally, gently furrows her brows, and subtly scrunches her nose. Her expression conveys mild annoyance mixed with playful embarrassment and amusement, as if reacting to a close friend teasing her. She should not appear angry, cold, or overly dramatic. Instead, capture the authentic expression someone makes when unexpectedly interrupted by a friend's playful prank. While shielding her eyes, she naturally says "Stop it." Deliver the line softly and casually, like an instinctive reaction that slips out without thinking. Her lip sync should be precise and natural, with realistic mouth movement and speech timing, never exaggerated. After speaking, her expression gradually relaxes into a small, reluctant smile, suggesting that although she's mildly annoyed, she's ultimately amused by the situation. Preserve highly realistic skin detail, including visible pores, subtle blemishes, faint acne marks, natural skin texture, gentle facial shine, cheek texture, and realistic highlights across the bridge of the nose. Her lips should have natural moisture and soft reflections without appearing glossy or heavily made up. Avoid any beauty-filter appearance. Her hair falls naturally with loose wisps across her forehead. A few strands rest against her skin and move subtly with natural motion. The background should be heavily blurred, featuring soft deep blue and purple nighttime ambient lighting with diffused bokeh lights. The overall image should feel like a genuine spontaneous smartphone flash video rather than a commercial, fashion shoot, or posed production. Emphasize everyday realism, authentic interaction, subtle micro-expressions, natural speech, and slightly imperfect framing. The handheld phone feeling should be obvious, with gentle natural camera shake and slight breathing motion typical of someone casually recording on a smartphone. Timeline 0–2 seconds A friend suddenly turns on the phone flash. The bright flash illuminates her face from the front. The camera is very close with subtle handheld movement. She is briefly startled. 2–4 seconds She instinctively raises her hand to block the light, slightly turns her head away, squints, gently furrows her brows, and reacts naturally. 4–6 seconds While still shielding the light, she softly says "Stop it." Her lip sync is clear and natural, with realistic timing and an authentic tone, as if responding to a playful friend. 6–8 seconds She continues partially blocking the light while briefly looking away from the camera. Her expression gradually shifts from mild annoyance to reluctant amusement. 8–10 seconds She relaxes slightly. Her hand remains in the foreground but no longer blocks as much of the light. A subtle smile appears at the corner of her mouth, suggesting she's been won over by the joke. The video ends while maintaining the close handheld smartphone candid aesthetic. Negative Prompt Do not use extreme face cropping. Do not let the hand completely cover the face. Avoid malformed hands, extra fingers, frozen expressions, lifeless eyes, missing blinks, incorrect lip sync, stiff mouth movement while speaking, mismatched audio and lip movement, exaggerated acting, cold or emotionless expressions, AI-looking plastic skin, excessive skin smoothing, beauty filters, influencer-style filters, heavy makeup, posed photography, commercial or cinematic advertising aesthetics, studio lighting, drifting facial features, cluttered backgrounds, subtitles, text, logos, watermarks, phone status bars, playback controls, screen flicker, sudden cuts, or abrupt camera changes. Do not alter the subject's ethnicity under any circumstances. Do not Asianize, Westernize, or otherwise modify the facial characteristics. The character's identity must remain faithfully consistent with the reference image throughout the entire video.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `10.06s`

---

### 🎬 Nile Farmer Ancient Egypt Life
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07657.jpg" width="480" alt="SD2_07657"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/nile-farmer-ancient-egypt-SD2_07657">🌐 Watch Online</a>

#### 📝 Prompt
```
This is handheld documentary footage recorded on an early-2000s consumer DV camcorder following a young man through a farming village along the Nile. The footage should feel like authentic, imperfect home video of daily life in ancient Egypt. The man is in his early 20s. He has dark hair kept short, warm brown skin with natural texture from outdoor work, and wears a simple white linen kilt with a belt. His body shows the physical condition of someone who does heavy agricultural and construction labor. The environment is a modest Egyptian village near the river: mud-brick houses, fields of wheat and flax, irrigation channels, palm trees, and a few donkeys and cattle moving through the area. The recording follows him as he starts the day working in the fields with a wooden plow pulled by two oxen, guiding the animals along the irrigation channels. He then moves to one of the channels to clear mud and debris with a wooden tool. Later he walks toward the river carrying a large basket and joins other men loading harvested crops onto a small wooden boat. On his way back to the village he stops to help repair a section of an irrigation channel using mud bricks. He finishes near his house, sitting on the ground while sharpening a wooden tool with a stone. The camera follows him with natural handheld shake, drifting framing, autofocus issues when he bends or moves quickly, exposure changes between bright fields and shaded areas, and occasional motion blur. Natural sound only: water flowing in the channels, distant animal sounds, the sound of tools hitting mud and wood, voices of other workers, and light wind. No music. The result must feel like real, candid footage of everyday agricultural life in ancient Egypt captured on an old camcorder.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Planetary Shutters Closing
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07655.jpg" width="480" alt="SD2_07655"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/planetary-shutters-closing-SD2_07655">🌐 Watch Online</a>

#### 📝 Prompt
```
10-second cinematic sci-fi action sequence, 16:9, ultra-realistic, breathtaking scale, realistic physics, no visible face. A fighter flies through a gigantic artificial world. The interior contains continents, cities and oceans. Suddenly a planetary defense system activates. Enormous armored plates begin sliding across the sky. Each plate is hundreds of kilometers wide. The world is literally closing. Sunlight disappears section by section. The pilot races through narrowing corridors of light. Entire landscapes vanish beneath moving armor. The remaining opening becomes smaller and smaller. The fighter dives toward the last visible gap. The planetary shutters collide behind him. Cut.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.13s`

---

### 🎬 Birds Dissipate To Music
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07654.jpg" width="480" alt="SD2_07654"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/birds-dissipate-music-SD2_07654">🌐 Watch Online</a>

#### 📝 Prompt
```
The birds from &lt;video&gt; loosely form the imperfect shape of a bird based on &lt;image&gt;. They move to the music from &lt;audio&gt; and dissipate as they fly
```

#### 📌 Details
- Ratio: `1.78` | Duration: `8.25s`

---

### 🎬 Apartment Lights Dance to Music
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07653.jpg" width="480" alt="SD2_07653"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/apartment-lights-music-sync-SD2_07653">🌐 Watch Online</a>

#### 📝 Prompt
```
The lights of the apartments start turning on in sync with the music.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

<!-- STATS_END -->
