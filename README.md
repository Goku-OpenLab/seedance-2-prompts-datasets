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
- Total Prompts: **5187**
- Updated Today (UTC 2026-07-07): **26**

## 🎬 Today's Updates
### 🎬 Sunset Cyclist Kicks Truck Flying
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05207.jpg" width="480" alt="SD2_05207"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sunset-cyclist-kicks-truck-SD2_05207">🌐 Watch Online</a>

#### 📝 Prompt
```
Generate a first-person perspective: I'm riding a bike, on a sunny afternoon on a road with a sunset. Then a Dayun commercial semi-trailer comes over, almost hitting me, and I kick it flying.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 Biker Kicks Semi Truck Flying
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05206.jpg" width="480" alt="SD2_05206"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/biker-kicks-semi-truck-SD2_05206">🌐 Watch Online</a>

#### 📝 Prompt
```
Generate a first-person perspective: I'm riding a bike, on a sunny afternoon on a road with a sunset. Then a Dayun commercial semi-trailer comes over, almost hitting me, and I kick it flying.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 Fading Smile in Dusk Breeze
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05205.jpg" width="480" alt="SD2_05205"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/fading-smile-dusk-breeze-SD2_05205">🌐 Watch Online</a>

#### 📝 Prompt
```
First, generate a close-up of the girl. Refer to this image: the image should be completely kept in the state it was at the beginning. Close-up of the girl, standing in the dusk breeze, her face slightly tilted, hair blown in front of her face, eyes calm, expressionless and emotionless. The camera is handheld close-up, with slight breathing movements, like the camera is on but the actors haven't started the performance yet. A very soft voice came from outside the painting: "Alright, let's begin." After hearing this, the girl began to perform. She slowly shifted her gaze to the camera, first flashing a sweet, natural smile, as if trying to reassure people. Her smile was very clean, the corners of her mouth gently lifted, and her eyes curved along with her. For the first two seconds, there was no sign of sadness at all. The wind kept blowing, and a few strands of hair stuck to her face, but she didn't tidy it up. The smile remained, but his gaze gradually became a bit empty. It's not an outburst of sadness, but rather that after laughing for too long, the facial muscles are starting to give up. The corners of his mouth still smiled, but the light in his eyes gradually dimmed. In the last two seconds, she still smiled at the camera. Only the nostrils twitched slightly, his throat felt like he had swallowed, his eyes a little moist, but no tears fell. She tried hard to keep a sweet smile on her lips, but her eyes showed fatigue. Finally, she gently lowered her eyes, then looked up, as if suppressing her emotions back down, 3:4
```

#### 📌 Details
- Ratio: `0.56` | Duration: `13.04s`

---

### 🎬 One-Take Seamless Outfit Change
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05204.jpg" width="480" alt="SD2_05204"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/one-take-outfit-change-SD2_05204">🌐 Watch Online</a>

#### 📝 Prompt
```
Single continuous long take (0:00–0:15) — UGC selfie, seamless clothing + scene transitions ×3, one-shot, no editing. Format: 9:16 portrait, 15 seconds, 100% real-time. Reference: @img1 = Dark-haired woman in the photo — Focus on her face, long, dark brown
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.15s`

---

### 🎬 Supernatural Martial Arts Clash
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05203.jpg" width="480" alt="SD2_05203"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/supernatural-martial-arts-clash-SD2_05203">🌐 Watch Online</a>

#### 📝 Prompt
```
Supernatural martial arts duels between @[character1 ref] and @[character2 ref] with aura bursts and heavy impact accents. 16 beats. Open on immediate action, maintain escalating momentum throughout, and end on a decisive final impact with no slow introduction or cooldown.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.03s`

---

### 🎬 Cargo Terminal Escape Chase
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05202.jpg" width="480" alt="SD2_05202"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cargo-terminal-escape-chase-SD2_05202">🌐 Watch Online</a>

#### 📝 Prompt
```
Hyper-realistic cinematic action sequence Night. Inside a massive futuristic airport cargo terminal, two agents, one man and one woman, race through a high-speed baggage and cargo handling zone while a security team closes in behind them. The environment is large, bright, and industrial: giant moving luggage conveyors, cargo belts at different heights, robotic loading arms, rolling containers, metal platforms, flashing warning lights, and large cargo doors that begin closing automatically. Both agents wear dark fitted tactical clothing, no hoods, no helmets, no masks, visible hair, no celebrity resemblance. Wide opening shot: the two agents sprint into the cargo handling area at full speed while security enters behind them. Conveyor belts move in different directions, luggage and cargo cases slide past, and robotic arms swing overhead. Tracking shot: the agents run along a moving conveyor belt, then jump across to another belt at a different height. They weave between rolling baggage containers and duck under a robotic arm as it swings into position. The security team follows, struggling to keep up across the moving machinery. Side shot: the chase becomes more intense. One agent slides across a belt loaded with luggage while the other vaults over a low cargo divider. A robotic arm lowers a cargo crate into their path, forcing them to change direction quickly. Warning lights flash red as a large cargo exit begins closing in the distance. Final 5 seconds: the pace increases sharply. The agents sprint across the final set of moving conveyors, jump a narrow gap between belts, pass under one last robotic arm, and dive through the narrowing cargo doorway just before it closes. Loose baggage and cargo cases tumble behind them as the security team is delayed on the belts. Final moment: the two agents land hard on the far side of the cargo door and turn back for a split second as the machinery continues moving behind the sealed doorway. Style: hyper-realistic, cinematic, fast-paced, tense, clear and readable action, strong sense of motion and urgency, airport cargo terminal, moving conveyor belts, robotic arms, flashing warning lights, dynamic but clear camera movement, no text, no logos, no cartoon style. Keep proportions. Keep style and features. Aspect ratio 16:9.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

### 🎬 Ramen Warrior vs Ninjas
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05201.jpg" width="480" alt="SD2_05201"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ramen-warrior-ninjas-SD2_05201">🌐 Watch Online</a>

#### 📝 Prompt
```
PART 1 (0:00–0:15) Cut 1 (0:00–0:05) — Sneaking Through the Market 1920s Osaka market, Betamax film look. Yuki stealthily tiptoes through crowded stalls, sleeve over her mouth, eyes scanning. She spots a ramen shop, grins, and dashes through the noren curtain. Cut 2 (0:05–0:10) — Ramen at Last Inside the steamy ramen shop, Yuki excitedly orders a giant tonkotsu ramen with extra pork and egg. She sits down as the steaming bowl arrives, smiling and raising her chopsticks like a sword. Cut 3 (0:10–0:15) — Ninja Ambush Three burly ninja-like thugs notice her, pull on masks, and suddenly attack. Tables scatter as they leap through the air. Yuki flips clear while protecting her ramen, frozen mid-slurp with an annoyed glare. PART 2 (0:15–0:30) Cut 4 (0:15–0:20) — Noodle Defense A ninja throws a shuriken. Yuki instantly catches it by stretching a single ramen noodle between her chopsticks, then effortlessly dodges the ninjas' attacks with playful martial-arts agility. Cut 5 (0:20–0:25) — Men-no-Jutsu Yuki plants her feet and chants, "Men-no-jutsu!" Glowing ramen noodles rise from the bowl and whip through the shop, wrapping around all three ninjas and tying them together. Cut 6 (0:25–0:30) — Bowl Finish The tangled ninjas stumble and crash into a heap. Yuki leaps high into the air and smashes the empty ramen bowl onto their heads with a triple bonk. Freeze frame on her fierce pout as her gold-and-red hairpins sparkle under the lantern light.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.13s`

---

### 🎬 Rocket Blast Kills Giant Crocodile
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05200.jpg" width="480" alt="SD2_05200"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/giant-crocodile-rocket-blast-SD2_05200">🌐 Watch Online</a>

#### 📝 Prompt
```
A village road in bright daylight, small houses on both sides. A big water tanker truck is driving down the road. A mega crocodile, as big as a truck, bites onto the back of the water tanker and pulls it hard. On the roof of a nearby building, a soldier holds a rocket launcher. Sounds: loud truck engine, crashing metal, people shouting, the crocodile growling. Shot 1 (0–3s) — THE HOOK: We see the water tanker shaking hard. The mega crocodile has its mouth locked on the back of the truck, pulling it side to side. Water splashes out. The driver is scared and shouts on his radio: "IT'S GOT MY TRUCK!" Shot 2 (3–6s): On the roof of a building nearby, the soldier gets ready with his rocket launcher. He watches closely but does not shoot yet — the driver is still too close. He says on the radio: "Jump out! Run now!" Shot 3 (6–9s): The driver opens his door and jumps out of the truck. He runs fast down the road. The crocodile lets go of the truck and comes onto the open road, chasing after him. Now the crocodile is all alone in the open. Shot 4 (9–13s) — BIG SLOW MOMENT: The crocodile is out in the open road now. The soldier fires his rocket launcher from the roof. We see it in slow motion — smoke comes out, and the rocket flies down through the air, right at the crocodile. Shot 5 (13–15s): Everything goes back to normal speed. BOOM! Fire and smoke burst out where the crocodile was. The truck sits still and safe. The driver looks back from far away, safe. Smoke goes up into the sky. Cut.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.88s`

---

### 🎬 Giant Snake Boat Attack
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05199.jpg" width="480" alt="SD2_05199"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/giant-snake-boat-attack-SD2_05199">🌐 Watch Online</a>

#### 📝 Prompt
```
A river with green trees on both sides, in the bright sun. A small boat is moving on the water. A giant snake wraps around the boat, squeezing it tight. On the river bank, a soldier is loading his gun. Sounds: water splashing, boat engine, snake hissing, people shouting. Shot 1 (0–3s) — THE HOOK: The giant snake wraps tight around the boat. The boat tips side to side. The driver holds on and shouts on his radio: "IT'S SQUEEZING US!" Shot 2 (3–6s): On the river bank, the soldier holds his gun, ready. He waits — he can't shoot yet, the snake is too close to the boat. He says: "Cut the net! Do it now!" Shot 3 (6–9s): The boat driver grabs a knife and cuts the rope holding a big heavy net. The net falls — and so does the snake! It falls out of the boat and lands in the open water. Now the snake is all alone, out in the open. Shot 4 (9–13s) — BIG SLOW MOMENT: The snake is in the open water now. The soldier fires his gun from the bank. We see it slow — smoke puffs out, and the shot flies fast across the water, right at the snake. Shot 5 (13–15s): Everything goes back to normal speed. BOOM! Water splashes up high where the snake was hit. The boat floats safe on the water. The driver looks back, happy and safe.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `11.88s`

---

### 🎬 Anime Sticker Girl vs Retro Arena
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05198.jpg" width="480" alt="SD2_05198"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/anime-girl-retro-arena-SD2_05198">🌐 Watch Online</a>

#### 📝 Prompt
```
{ "style": "Authentic early-1990s British Saturday-night ITV broadcast style, realistic recreation of Gladiators arena footage, huge indoor arena with neon lighting rigs and foam-waving crowd, broadcast video texture with slight smear, electric atmosphere.", "main_character": "Q-version Anime Sticker Character with flat 2D sticker texture, bold cartoon outlines, and paper-cut feel. She has long golden hair with straight bangs and big purple round eyes. She wears a simple red and white athletic outfit with white helmet and knee pads. Her movements retain a slightly exaggerated, sticker-like quality while interacting with the realistic environment.", "shots": [ { "time": "0-3s", "camera": "Wide arena shot", "description": "The Q-version anime sticker girl sprints toward the Travelator — a steep upward conveyor belt running fast downward against her. The crowd roars as neon arena lights sweep across the stage." }, { "time": "3-6s", "camera": "Low-angle tracking shot", "description": "She leaps onto the belt and attacks it at full sprint. For a moment she gains ground, her long golden hair flowing as she pushes forward while the belt whines beneath her feet." }, { "time": "6-9s", "camera": "Side medium shot", "description": "Her stride shortens — the belt wins. She’s running at full effort while slowly sliding backward, arms flailing, her big purple eyes shifting from focus to panic." }, { "time": "9-12s", "camera": "Close action shot with motion blur", "description": "She drops to all fours and claws at the rubber surface, carpet-crawling desperately before getting dragged down and spat off the bottom onto the crash mat in a heap." }, { "time": "12-15s", "camera": "Handheld follow shot", "description": "She lies on the mat, chest heaving, one arm raised in a hopeless thumbs-up as the buzzer sounds time-out. The Travelator keeps humming triumphantly behind her. Frame holds." } ], "technical_details": "High fidelity realistic live-action footage in the style of early-90s UK arena game show. Accurate conveyor-belt treadmill physics, neon arena lighting, and coherent character movement. The main character remains in flat 2D anime sticker style while the environment and physics stay realistic.", "negative_prompt": "blurry, low quality, deformed character, extra limbs, text, watermark, logo, overexposed, underexposed, modern artifacts, 3D rendered character" }
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.03s`

---

### 🎬 Korean Morning GRWM Routine
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05197.jpg" width="480" alt="SD2_05197"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-morning-grwm-routine-SD2_05197">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a realistic GRWM (Get Ready With Me) lifestyle video featuring a stylish Korean woman with long silky black hair, radiant skin, and a fresh natural look. Bright modern apartment with floor-to-ceiling windows, warm morning sunlight, Scandinavian-inspired décor, premium fashion vlog aesthetic, cinematic handheld camera, ultra-realistic photography. The video opens with her sitting on the edge of her bed. She smiles softly, stretches, and walks to the window, pulling the curtains open as warm golden sunlight fills the room. She makes her bed before heading to her vanity. She begins a refreshing skincare routine using a cleanser, toner, serum, moisturizer, and lip balm. Close-up beauty shots highlight glowing skin while natural sunlight reflects through the room. Next, she styles her hair into soft loose waves using a curling iron, gently brushing through the curls for a smooth finish. She applies light everyday makeup including foundation, blush, mascara, soft eyeliner, and a glossy pink lip tint, smiling naturally into the mirror. She walks to her wardrobe, slides open the closet, and compares several outfits before choosing a pastel pink fitted crop top with high-waisted blue jeans. She changes into the outfit, adjusts the fit, and adds small gold hoop earrings, a delicate necklace, a watch, and sunglasses. She sprays her favorite perfume, slips on white sneakers, picks up a small shoulder bag, and grabs an iced coffee from the kitchen counter. Standing in front of a full-length mirror, she checks her outfit from different angles, spins once with a smile, and takes a quick mirror selfie. The video ends as she opens the apartment door and walks outside into the bright morning sunshine. The camera follows her as she confidently strolls down a peaceful tree-lined street holding her iced coffee, ending with a cinematic pullback. Style: premium GRWM fashion vlog, luxury lifestyle content, warm natural lighting, cozy apartment aesthetic, realistic handheld and gimbal cinematography, soft cinematic color grading, photorealistic, elegant transitions, shallow depth of field, 4K HDR, 16:9 widescreen, no subtitles, no text overlays.
```

#### 📌 Details
- Ratio: `1.73` | Duration: `15.07s`

---

### 🎬 Soldier Saves Bus From Giant Crocodile
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05196.jpg" width="480" alt="SD2_05196"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/soldier-saves-bus-crocodile-SD2_05196">🌐 Watch Online</a>

#### 📝 Prompt
```
A road in the daytime. A regular bus is driving with people inside. A big crocodile bites the back of the bus. On a hill nearby, a soldier holds a big gun. Sounds: loud bus engine, people yelling, crocodile growling. Shot 1 (0–3s) — THE HOOK: The big crocodile bites the back of the bus. The bus shakes hard. People inside scream. The driver shouts on his radio: "IT'S BITING THE BUS!" Shot 2 (3–6s): On the hill, the soldier holds his big gun ready. He watches close but does not shoot yet. The bus is too close to the crocodile. He says: "Turn now! Get away!" Shot 3 (6–9s): The bus driver turns the wheel fast. The bus gets away from the crocodile's mouth. The big crocodile runs onto the open road all by itself, chasing behind. Shot 4 (9–13s) — BIG SLOW MOMENT: The crocodile is alone in the open road now. The soldier on the hill shoots his big gun. We see it slow. Smoke comes out. The shot flies fast down the road at the crocodile. Shot 5 (13–15s): Everything goes back to normal speed. BOOM! Big fire goes up where the crocodile was. The bus is safe and drives away. People inside look back, happy and safe. Smoke goes up in the sky. Cut.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.88s`

---

### 🎬 Ben's NYC Times Square Adventure
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05195.jpg" width="480" alt="SD2_05195"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ben-nyc-times-square-vlog-SD2_05195">🌐 Watch Online</a>

#### 📝 Prompt
```
Use the attached reference image as Ben's exact identity. Preserve identical face, hairstyle, eyes, jawline, beard stubble, skin texture, age, voice, body shape, clothing, personality, and mannerisms. No face drift. No identity changes. Same person throughout all clips. Realistic American travel vlogger. Documentary realism. Authentic New York City atmosphere. Natural crowd behavior. Realistic speech and lip sync. English language. Auto captions matching spoken dialogue. High-end travel vlog. Frequent camera angle changes." CLIP 1 (0:00–0:15) 0:00–0:03 Selfie shot, Times Square behind Ben. Ben: "Hey everyone, my name is Ben. Welcome back to another vlog." 0:03–0:06 Camera turns toward giant screens. Ben: "Today I'm right in the heart of New York City, standing in Times Square." 0:06–0:09 Crowd shots. Ben: "This place has been on my travel list for years." 0:09–0:12 Back to Ben. Ben: "The energy here is honestly unbelievable." 0:12–0:15 Walking forward. Ben: "Let's spend the day exploring together." CLIP 2 (0:15–0:30) 0:15–0:18 POV walking. Ben: "The first thing you notice is the sound." 0:18–0:21 Taxi passes. Ben: "Cars, music, conversations." 0:21–0:24 Street performer visible. Ben: "Something is happening every few feet." 0:24–0:27 Billboard shot. Ben: "You can feel the city moving around you." 0:27–0:30 Crowd shot. Ben: "It's impossible to get bored here." CLIP 3 (0:30–0:45) 0:30–0:33 Looking upward. Ben: "Look at these screens." 0:33–0:36 Giant LED advertisements. Ben: "Some are taller than entire buildings." 0:36–0:39 Traffic below. Ben: "Millions of people pass through here." 0:39–0:42 Tourists taking photos. Ben: "Everyone is trying to capture the moment." 0:42–0:45 Wide city shot. Ben: "And I completely understand why." CLIP 4 (0:45–1:00) 0:45–0:48 Walking shot. Ben: "One thing I love about New York is the diversity." 0:48–0:51 Different people visible. Ben: "People from all over the world." 0:51–0:54 Street food carts. Ben: "Different cultures." 0:54–0:57 Storefronts. Ben: "Different stories." 0:57–1:00 Ben briefly visible. Ben: "All sharing the same streets." CLIP 5 (1:00–1:15) 0:00–0:03 Opening taxi door. Ben: "Let's head downtown." 0:03–0:06 Entering yellow cab. Ben: "Nothing feels more New York than this." 0:06–0:09 Taxi moving. Ben: "A classic yellow cab." 0:09–0:12 Window view. Ben: "Perfect way to see the city." 0:12–0:15 Streets passing by. Ben: "Let's enjoy the ride." CLIP 6 (1:15–1:30) Taxi interior. Ben talks about architecture, old buildings, skyscrapers, and how Manhattan combines history and modern design. CLIP 7 (1:30–1:45) Taxi window views. Ben talks about people rushing to work and how the city never seems to slow down. CLIP 8 (1:45–2:00) Taxi reaches destination. Ben exits and says every neighborhood feels completely different despite being in the same city. CLIP 9 (2:00–2:15) Walking through a small park. Ben notices a friendly cat. Ben: "Well hello there little guy."
```

#### 📌 Details
- Ratio: `1.78` | Duration: `205.03s`

---

### 🎬 Blonde Schoolgirl Hallway Brawl
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05194.jpg" width="480" alt="SD2_05194"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/blonde-schoolgirl-hallway-brawl-SD2_05194">🌐 Watch Online</a>

#### 📝 Prompt
```
A dynamic, high-energy cinematic action sequence in an American high school hallway. A fierce and beautiful Western woman with long wavy blonde hair, wearing a baby pink school uniform blazer with school emblem, white shirt, striped tie, pleated plaid skirt, black knee socks, and shoes, is single-handedly fighting multiple male attackers in an intense hallway brawl. She moves with incredible speed, agility, and martial arts skill — spinning, delivering powerful high kicks, punches, and fluid combos that send the larger men flying into lockers, slamming against walls, and crashing to the floor. Papers scatter everywhere across the polished floor. The men are knocked out or defeated one by one as she advances through the hallway. The camera is highly dynamic: low-angle tracking shots, quick pans, dramatic close-ups of her determined face and flowing blonde hair, wide shots showing the chaos, and intense over-the-shoulder action. Cinematic lighting with overhead fluorescent lights, realistic motion blur on fast movements, dramatic hair whip effects, and intense facial expressions. She looks powerful, confident, and slightly breathless by the end, standing amid the fallen opponents while looking directly forward with focus. Realistic live-action style, high detail, intense choreography similar to action film fight scenes, 14-second duration, 16:9 aspect ratio.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Arena Time Gate Dragon Invasion
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05193.jpg" width="480" alt="SD2_05193"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/arena-time-gate-dragon-invasion-SD2_05193">🌐 Watch Online</a>

#### 📝 Prompt
```
Use @[ref image] as the main reference for the giant circular silver arena gate, two colossal king statues, packed crowd, bright daylight sky, tall white towers, and smartphone POV from inside the crowd.
A continuous horizontal smartphone video from a frightened bystander. The camera shakes naturally, pans, tilts up, stumbles backward, loses framing behind heads, raised phones, dust, flags, and running people. No cuts, no UI, no timestamp, no subtitles, no music.
In a colossal silver-white futuristic arena, the circular time gate stands closed at first, glowing softly with blue-white energy. The crowd is silent, tense, and filming. Suddenly, ancient runes around the gate light up one by one. A deep hum shakes the plaza. Dust rises, banners snap, and a controlled blue-white time vortex forms on the sealed gate surface.
The vortex spins faster, compresses into a vertical crack of light, then tears open with a violent shockwave. D1, a broad-horned dragon, bursts out airborne directly toward the camera. The crowd screams and breaks into panic, people ducking, falling, dropping phones, shoving, and running in every direction.
The camera whips left as D1 flies low over the crowd. D2, a long-necked sky serpent, emerges behind it. The camera swings back to the still-glowing gate as D3, a heavy armored drake, forces through the opening, followed by D4, a narrow-winged blade-like dragon slicing through the air. The gate remains active, bright, and unstable the entire time.
Finally, D5, the largest dragon, fills the entire circular gate with glowing eyes, huge claws, armored chest, and massive wings. It erupts into the sky, spreads wider than the gate, roars above the arena, then breathes a huge golden-orange fire blast across the sky. Blue-white gate light mixes with orange firelight, illuminating the statues, towers, banners, dust, and fleeing crowd. The video ends with D5 dominating the sky while the time gate still glows behind it.
Negative prompt: no galaxy portal, no space tunnel, no visible other world, no gate turning off, no dragons walking or landing, no calm crowd, no clean cinematic camera, no drone shot, no subtitles, no UI, no timestamp, no music.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

<!-- STATS_END -->
