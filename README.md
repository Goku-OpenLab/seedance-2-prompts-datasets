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
- Total Prompts: **8720**
- Updated Today (UTC 2026-08-18): **25**

## 🎬 Today's Updates
### 🎬 Cinematic Garden Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11511.jpg" width="480" alt="SD2_11511"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-garden-vlog-SD2_11511">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 14-second cinematic travel vlog using the provided image as the exact location reference. Show a stylish young girl vlogging while walking through this beautiful heritage garden, keeping the same grand historic building, colorful flowers, wet pathway, greenery, palm trees and overall atmosphere from the reference image. Start with a wide establishing shot of the location, then show the girl smiling and talking naturally to her camera, turning the camera to reveal the beautiful surroundings. Include smooth walking shots, close-ups of flowers and architecture, natural reactions and a joyful spin. Use warm golden sunlight, realistic people, cinematic depth of field, smooth handheld/gimbal movement, natural ambient city sounds and ultra-realistic 4K quality. End with a beautiful wide shot of the same location. No text, no logos, no artificial-looking elements, and preserve the reference location accurately.
```

#### 📌 Details
- Ratio: `1.51` | Duration: `14.7s`

---

### 🎬 Chalkboard Japanese Demo
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11509.jpg" width="480" alt="SD2_11509"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/chalkboard-japanese-demo-SD2_11509">🌐 Watch Online</a>

#### 📝 Prompt
```
[Speech rule — read first] The woman speaks JAPANESE ONLY. She never speaks Chinese, English, or any other language. She speaks almost continuously for the whole clip. She says exactly this one sentence, broken into four phrases, in this order and nothing else: 「Seedance 2.5なら」 「黒板に日本語の文字を」 「書くことができます。」 「とても便利ですね」 She delivers it at the unhurried pace of a teacher writing on a board: her voice slows to the speed of her own chalk, so each phrase is spoken while her hand is forming that same phrase. Voice and chalk advance together. Only a short natural breath separates one phrase from the next — no long pause anywhere. Total speech fills roughly 13 of the 15 seconds. The only silence is the final 0.8 seconds, where she has finished writing and simply smiles and nods. Forbidden at all times: ad-libbed dialogue, filler words, repeating a phrase, reading the sentence twice, humming, laughing, sighing, and every wordless vocalisation such as "んっ" "うん" "ふふ" "ah" "mm" "hm". She says the four phrases once each and nothing more. Pronounce "Seedance 2.5" as English "seedance two point five". [Reference] @Image1 = the keyframe: a woman in a white coat standing beside a completely empty green chalkboard, holding a slim wooden pointer at her side. Strictly preserve @Image1's face, hair, glasses, white coat, the chalkboard's position and size, the easel, the background shelves, and the framing. Nothing moves in the frame except her arm, her upper body, her face, and the chalk marks she draws. [One-line summary] 15 seconds. A cheerful presenter gives a short lecture, writing four lines of Japanese on a green chalkboard with the tip of a wooden pointer while speaking the same words aloud. Pixar-style 3D animation. Locked-off static camera. [Global setup] Environment: warm indoor study room, soft warm ceiling light, shallow depth of field, background shelves stay blurred. Highly realistic physical texture on the chalk dust and the wood of the easel. Visual style: Pixar-style 3D animation, warm color grade, soft shadows. Camera language: medium shot, eye level, straight-on. The camera is completely locked off — no pan, no tilt, no zoom, no push-in, no handheld shake. One camera behavior only: none. Character: as in @Image1. Keep the glasses, the hair silhouette, and the coat identical. Keep believable skin shading and fine surface detail — do not make her look plastic. Acting core: a warm, confident teacher who enjoys showing something off. *** WRITING RULE — SHE IS THE ONE WRITING, AND SHE WRITES AS SHE SPEAKS. *** Every chalk mark is produced by her own hand movement, in time with her voice. For each phrase: 1. Her shoulder and elbow carry the pointer tip to the start of the line. Her torso turns slightly toward the board and her eyes go to that point first. 2. The tip presses lightly to the board and travels along the path of each stroke. The chalk line appears directly behind the moving tip, following it exactly, never running ahead of it, never appearing anywhere the tip has not touched. 3. Characters are formed one stroke at a time, in correct Japanese stroke order, left to right. Faint chalk dust puffs at the tip and a soft scraping sound follows it. 4. Between strokes the tip lifts a few centimetres, then sets down at the start of the next. 5. The syllables she speaks land together with the characters she is forming — when her voice reaches a word, her hand is writing that word. Voice and chalk stay in step. 6. At the end of each line she lowers the pointer slightly, takes one small breath, glances at the camera, then moves to the line below. Her arm leads and the mark follows — the timing of the arm and the timing of the mark must match frame for frame. Marks NEVER fade in as a whole word. Marks NEVER appear while her arm is at rest or while the tip is away from the board. No invisible hand. No magic writing. The arm motion is fluid and human: the wrist flexes, the elbow opens and closes, the shoulder carries the reach across the board, her body weight shifts slightly as she reaches. Once a line is finished it stays on the board unchanged for the rest of the shot. Japanese script rule (important): Render every kanji with its correct stroke structure and correct number of strokes — 黒 板 日 本 語 文 字 書 便 利. They must be legible as real Japanese characters, not invented or Chinese-simplified lookalikes. Write them at a generous size so the strokes stay separated. "Seedance 2.5" is written in Latin letters and digits exactly as spelled: S-e-e-d-a-n-c-e, space, 2, period, 5. Chalk colors — only two, never any other: YELLOW chalk for "Seedance 2.5" only. WHITE chalk for everything else. Layout rule (important): Four lines, left-aligned to a common left margin, stacked evenly down the board from top to bottom, filling the board by the end. Large, cheerful hand-lettered chalk style with slightly uneven strokes. Exact content, top to bottom: Seedance 2.5なら 黒板に日本語の文字を 書くことができます。 とても便利ですね Never centre a line. Never write small. Each line is written as large as it can be while still fitting: a completed line spans almost the full writable width of the board, from the left margin nearly to the right edge of the board, and the four lines together fill the board from top to bottom. Characters are wide and generously spaced so that dense kanji such as 黒 板 語 書 便 利 keep their strokes separated and legible. If a line would not fit, make the characters narrower rather than shorter in height — never shrink a line so that it occupies only part of the board's width. Do not add any other word, symbol, arrow, underline or drawing. Forbidden: no subtitles, no captions, no on-screen UI, no watermark, no background music, no camera movement, no cutting to another shot, no extra people, no second hand entering the frame, no stick of chalk held in her free hand, no distortion of lines already written. [Timestamp storyboard] 0.0-3.6s LINE 1 Action: she raises the pointer to the upper-left of the empty board and writes "Seedance 2.5なら" in YELLOW chalk — first the Latin letters and digits, then the kana なら — the marks trailing the moving tip. Speech (in step with the writing): 「Seedance 2.5なら」 Intent: a small proud lift in her eyebrows on the brand name. This is the thing she is showing off. Camera: locked. No subtitles. No BGM. Japanese only. 3.6-7.2s LINE 2 Action: she drops to the next line and writes "黒板に日本語の文字を" in WHITE chalk, stroke by stroke. Her eyes follow her own tip. Speech (in step with the writing): 「黒板に日本語の文字を」 Intent: matter-of-fact, the setup half of the sentence. Keep the arm steady and even. Camera: locked. No subtitles. No BGM. Japanese only. 7.2-11.0s LINE 3 Action: she drops to the third line and writes "書くことができます。" in WHITE chalk, stroke by stroke, ending with a firm dot for the 。 Speech (in step with the writing): 「書くことができます。」 Intent: this is the payoff of the sentence — her voice firms up slightly on ます, and the final dot is pressed with a small decisive tap. Camera: locked. No subtitles. No BGM. Japanese only. 11.0-15.0s LINE 4 — the close Action: she writes "とても便利ですね" in WHITE chalk on the bottom line, then lowers the pointer to her side, turns her face fully to the camera, breaks into an open warm smile and gives one clear nod. She holds that pose for the final 0.8 seconds in silence. Speech (in step with the writing, finishing by 14.2s): 「とても便利ですね」 Intent: the nod is the close. Warm, a little playful, as if sharing a good discovery. Camera: locked. No subtitles. No BGM. Japanese only. [Closing constraints — restated for the whole clip]
```

#### 📌 Details
- Ratio: `0.56` | Duration: `13.0s`

---

### 🎬 Pixar Style Salon ASMR Hair Care
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11505.jpg" width="480" alt="SD2_11505"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pixar-salon-asmr-hair-care-SD2_11505">🌐 Watch Online</a>

#### 📝 Prompt
```
3D Pixar-style animation, 8K resolution, vertical portrait orientation, 3:4 aspect ratio. A cozy, luxurious salon ASMR hair treatment session sequence. A cute young animated woman with long, silky black hair wearing a plush white bathrobe is reclining comfortably at a sleek white shampoo bowl. A cheerful stylist with a neat messy bun and apron gently washes, shampoos, and massages her hair. The clip features close-up details of water pouring from a golden faucet, rich white foam lathering, a wooden scalp massage brush working through soft foam, drops of hair oil being massaged into the scalp, smooth wooden combing, and drying with a white towel. Ending with the woman sitting up, smiling brightly at the camera, showcasing super shiny, voluminous, soft hair. Cozy aesthetic with warm glowing candles, marble countertops, white orchids, and golden accents. Cinematic lighting, soft depth of field, ultra-smooth camera movement, realistic fluid physics, relaxing and soothing atmosphere. --ar 3:4
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.08s`

---

### 🎬 Rusted Automaton Runs Through Radioactive Ruins
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11503.jpg" width="480" alt="SD2_11503"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rusted-automaton-radioactive-ruins-SD2_11503">🌐 Watch Online</a>

#### 📝 Prompt
```
Continuous tracking shot through a collapsed megacity overgrown with radioactive jungle. Subject: a three-foot-tall rusted automaton with a cracked glass faceplate, exposed copper wiring for hair, and piston-driven limbs. It sprints across tilting skyscraper beams, vaults through broken windows, slides under fallen monorail cars, grapples up vines wrapped around a transmission tower, and leaps between two collapsing buildings as the jungle reclaims the concrete in real-time. Dust motes, god-rays through canopy, rust particles, volumetric fog. Cinematic 8K, photorealistic decay textures.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Creative Blue Running Shoe Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11499.jpg" width="480" alt="SD2_11499"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/blue-running-shoe-ad-SD2_11499">🌐 Watch Online</a>

#### 📝 Prompt
```
Live-action running-shoe commercial. 20 seconds. No cuts are used. The background is one flat electric blue from beginning to end. No gradient, no texture, no floor, no shadows. The shoes fall continuously from the top of the frame towards the bottom. Dozens of running shoes are in frame at any one moment. They are all the same single model and differ only in colour: a light, thin running shoe with a thick white foam midsole under a brightly coloured knit mesh upper, with one small silver tab at the heel. That tab is the same silver on every colourway, and there is no gold or black metal anywhere on the shoe. The colours run through orange, lime, coral, dark grey, white and pale blue. Every shoe falls from top to bottom. They all fall the same way; what differs is that each tumbles on its own axis, so in any one frame some show their outsoles, some their sides, and some are seen from above. Any shoe that comes close to camera enters from the top of the frame and leaves through the bottom; none of them appears or disappears in the middle of the frame. The near ones are large and sharp; the far ones read only as small blurred patches of colour. Focus holds on one plane and everything in front of and behind it falls softly away. The camera holds its position, breathing very slightly. What carries the frame is the shoes. Partway through, a torn paper edge sweeps across the frame and opens the layer beneath it. Along every tear the white core of the paper is left ragged and fibrous, and a soft shadow falls onto the layer below. Wherever she appears, the camera is in front of her. It never follows her back or the back of her head; her face is turned towards camera. The photograph under the paper is black and white: high-key, with the sky blown out to white, and coarse darkroom-print grain. Even inside that black and white, the shoes keep their colour. One woman appears and she is the same person throughout: a Korean woman in her early twenties, with clearly defined features, long eyes and a narrow jawline. Her hair is deep auburn, falling in heavy waves to her waist, with a few fine braids running sideways from the crown. She ties it back in a single tail to run. She wears three things: a pale blue halter crop top underneath, a dark grey sheer cropped bolero over it with long sleeves and thumbholes that cover the backs of her hands, and dark grey joggers gathered at the ankle with a pale blue drawstring at the waist. She stays in all three while she runs; they never turn into a running vest or short athletic shorts. On her feet is the white-foam-midsole running shoe described above. (0:00–0:03) The film opens on the side of a coral running shoe filling the upper left of the frame, close enough that individual strands of the knit upper, the grain along the midsole and the stitching all read. It tumbles on its axis towards the lower right until the inside of the shoe comes into view. Behind it, dozens more come down at varying sizes. (0:03–0:05) A lime pair catches on the top edge of the frame with only the toes pushing in, close enough that the individual strands of knit mesh and the texture of the midsole are visible. The rest of the frame is blue, with only a few small shoes coming down far away in it. (0:05–0:07.5) LAND LIGHT fades up at the centre of the frame in white serif capitals with very wide letter spacing, fixed in place. Printed on paper, its strokes show horizontal printing lines inside them. One falling shoe drops in front of the letters and another behind them. From the lower right corner a torn paper edge rises at an angle and peels the blue layer away. (0:07.5–0:13) Where the edge has peeled back, a bright black-and-white photograph fills in. The camera sits low on the polyurethane track directly in front of her, facing her head-on and retreating as she runs towards it. The white foam midsole reaches forward, compresses as it meets the ground and springs back. The shoes alone hold their coral; everything else is black and white. The camera rises from her feet to her face and frames her from the front, chest up and large. Her eyes fixed straight ahead, her face wet with sweat and her dark auburn hair swinging all read clearly. The stands and the sky behind her fall softly out of focus, and the sky is blown out to white. (0:13–0:16) The torn edge rises from the bottom of the frame and the blue layer comes back. A coral pair falls through dead centre with one shoe crossing over the other, the camera further back now so the whole shoe reads. A single highlight travels across the small silver tab at the heel. (0:16–0:17.5) A single sheet of electric blue paper, come down from the top, covers the frame. Its lower edge is torn, with the white core of the paper showing. (0:17.5–0:20) A bright off-white paper field. At the centre, two lines of thin capitals: LAND LIGHT, RUN LONG. No other lettering and no symbol. A torn edge crosses the lower part of the frame at a very shallow angle. The final frame settles on exactly this. This has to read as a real commercial film. The print grain applies to the black-and-white layer only; the blue layers are sharp. Lettering appears in exactly two places: LAND LIGHT at 0:05–0:07.5 and the two lines on the final frame. No brand name and no logo symbol appear anywhere.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `20.08s`

---

### 🎬 Korean Girl Market Selfie Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11493.jpg" width="480" alt="SD2_11493"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-girl-market-selfie-vlog-SD2_11493">🌐 Watch Online</a>

#### 📝 Prompt
```
<<<image_1>>> = the woman's facial identity and hair only, do not inherit her outfit, pose, background or lighting from it. One continuous handheld front-facing phone selfie vlog, always her own point of view with the phone in her own hand at arm's length — no third-person or external camera, no tripod, no cinematic move. Real modern-smartphone look: mild handheld shake, walking bounce, occasional autofocus hunting, small exposure shifts, minor framing flaws, natural front-lens distortion; soft warm natural daylight turning to early evening, natural uncorrected phone color, no color grade, no beauty filter, no skin smoothing. The same one woman with the same face and hair throughout, holding the phone herself in every shot. Two casual, trendy outfits only, the exact styling chosen naturally — one look from the market entrance through the gift shop, a clearly different one from the photo booth onward, each identical within its half, her face and hair unchanged across the single outfit change. No subtitles, no on-screen text, no logo, no watermark; no brand or character names. Never render a reference sheet or duplicate a subject. Diegetic sound only, no background music: market bustle and chatter, footsteps, a sizzling street-food stall, quiet shop room-tone, café ambience, a photo-booth shutter, wind at the lookout, a bus engine and street sounds; each spoken line delivered frontally and lip-visible. A young Korean woman in her early twenties, natural everyday beauty, is walking into a lively traditional street market on her day off, already holding her phone out at arm's length to film herself; she sweeps the phone across the bustling stalls then back to her own grinning face and says, upbeat: "I’m at the market!" She keeps walking through the busy market, naturally bouncing the phone with her steps, glancing at colorful stalls and briefly turning the camera toward interesting food and people before bringing it back to her smiling face; she laughs softly and continues walking without dialogue. She stops at a sizzling street-food stall, picks up a hot skewer and holds it right up to the selfie camera, eyeing how good it looks, and says, delighted: "Wow, this looks freaking amazing..!" She gives a quick happy reaction after tasting it, then continues walking through the market while holding the phone herself. She steps into a tiny gift-and-stationery shop full of cute little things, browsing the shelves with a grin; she picks up a small item, looks at it and then at the camera with a playful worried expression, and says: "I think my wallet might be in danger here." After leaving the shop, she briefly stops at a cozy little café or drink stand, holds a simple takeaway drink close to the selfie camera, takes a quick sip and smiles contentedly at the lens before continuing on, with only natural café and street ambience.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.08s`

---

### 🎬 Blood Moon Portal Eclipse Chaos
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11487.jpg" width="480" alt="SD2_11487"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/blood-moon-portal-eclipse-SD2_11487">🌐 Watch Online</a>

#### 📝 Prompt
```
{ "duration": "20 seconds", "aspect_ratio": "9:16", "style": "ultra photorealistic, raw handheld smartphone video, natural lighting, digital noise, realistic motion blur, found footage aesthetic", "camera": { "type": "handheld smartphone", "movement": "shaky human hand movement, increasing panic shake, sudden tilts and jerks", "perspective": "first-person from inside the dense crowd", "lens": "wide phone lens, natural distortion, lens flare" }, "scene": "Large excited crowd on a cliff in northern Spain during the August 12 2026 total solar eclipse. Late evening.", "sequence": [ { "time": "0-5s", "action": "Totality begins. Normal black moon with bright white corona. People cheering and filming. Camera pans across the crowd." }, { "time": "5-9s", "action": "Unexpectedly the black moon starts turning deep blood red. The corona shifts to glowing crimson. Crowd goes from cheering to confused gasps." }, { "time": "9-14s", "action": "A circular glowing portal tears open around the red moon, expanding outward with swirling energy and light. Some people in the crowd begin slowly floating upward toward it." }, { "time": "14-20s", "action": "Full chaos. People screaming and running. More bodies getting pulled into the air toward the red portal. Camera becomes extremely unstable as the filmer panics and tries to escape while still filming the red moon and portal." } ], "audio_cues": "excited crowd noise → confused gasps → loud screaming, wind, running, heavy breathing, phone mic distortion and clipping", "negative_prompt": "smooth camera, cinematic color grade, CGI look, text, watermarks, perfect focus, professional film, cartoon" }
```

#### 📌 Details
- Ratio: `0.56` | Duration: `20.13s`

---

### 🎬 Aerial Thread Dance in Abandoned Warehouse
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11485.jpg" width="480" alt="SD2_11485"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/aerial-thread-dance-warehouse-SD2_11485">🌐 Watch Online</a>

#### 📝 Prompt
```
Real iPhone 15 Pro Max, 9:16 vertical, one continuous static shot - camera on the ground, no movement, zoom, cuts or grade, real grain, daylight. POV: the camera IS the phone on the ground - never visible: not in hand, in shot, or as a reflection. Warehouse: rusted beams 15m up, god rays in dusty air, graffiti walls, cracked concrete. THREAD: each time she opens a palm and a white semitransparent strand SHOOTS from it to the beam, then she grabs and swings - never pre-attached; fired threads stay hanging. She walks in, crouches, hand to the ground, stands, exits left. Runs back - palm to upper RIGHT beam, thread shoots, connects, swings up; at the peak a slow balletic somersault, pointe shoes pointed. Airborne, the other palm fires to upper LEFT beam, swings to the LEFT wall, pushes off both feet, a clean backward somersault, lands in a low crouch. She walks to us, crouches, hands reach for the lens, face above - light smile. auiet exhale. Hold. Cut.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `12.07s`

---

### 🎬 Cozy Morning Breakfast Routine
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11479.jpg" width="480" alt="SD2_11479"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cozy-morning-breakfast-SD2_11479">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 15-second ultra-realistic 16:9 landscape lifestyle video using the provided reference image as the exact character reference. Preserve his face, identity, hairstyle, body proportions, skin tone, and overall appearance consistently throughout. Do not change his identity. 0–3 sec — Kitchen: Medium-wide shot. He happily enters his kitchen, cracks eggs into a bowl, and starts preparing breakfast with energetic but natural movements. 3–6 sec — Cooking: Side three-quarter shot. He pours the eggs into a pan and cooks them, smiling casually. Realistic steam, utensils, hand movements, and cooking physics. 6–9 sec — TV: He briefly walks into the adjacent living room, picks up the remote, turns on the TV, glances at the screen with a small smile, then heads back toward the kitchen. 9–12 sec — Finishing breakfast: Back in the kitchen. He checks and stirs/flips the food, looking pleased, then plates the finished breakfast. 12–15 sec — Eating: Front three-quarter shot at the dining table. He sits down, looks happily at his breakfast, smiles, and takes his first bite. Style: Photorealistic casual daily-life vlog, authentic home environment, happy energetic mood, natural acting, realistic human movement, subtle handheld smartphone camera, natural autofocus, believable depth of field, 24fps. Lighting: Soft natural morning daylight mixed with realistic indoor lighting. Maintain: Consistent face and clothing, realistic hands/fingers, accurate object interaction, consistent kitchen/living-room layout
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Old Man and Pigeon Warm Moment
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11475.jpg" width="480" alt="SD2_11475"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/old-man-pigeon-warmth-SD2_11475">🌐 Watch Online</a>

#### 📝 Prompt
```
[Global Setting] Cozy old apartment balcony in warm golden morning light, colorful flower pots, wooden chair, hanging laundry, small table with bird seeds. 3D stylized animation with rounded appealing characters, expressive faces, playful physical comedy and sincere warmth. [Character 1: The Eccentric Old Man] Age 75+, round belly, wispy white hair, faded cardigan, loose trousers, worn slippers, spectacles sliding down his nose. Speaks rarely, mostly communicates through facial expressions and body language. Same appearance and cardigan throughout. [Character 2: The Mischievous Pigeon] One plump gray pigeon with shiny feathers, curious expressive eyes and a smug personality. Mostly silent, communicates through head movements, expressions and body language. [Opening, 0–6s] Old man sits on his balcony chair and places a small pile of sunflower seeds on his palm. He smiles at the pigeon and warmly says: “Come on, little friend.” The pigeon slowly approaches and stares at him suspiciously. [Funny Moment, 6–14s] The pigeon suddenly grabs the seed and jumps onto the old man's head. The old man freezes completely, eyes wide. He slowly looks upward while the pigeon casually looks down at him with a smug expression. The old man sighs and shakes his head. [Sweet Moment, 14–23s] The old man carefully lifts the pigeon from his head and holds it gently against his chest. The pigeon relaxes and nuzzles into him. The old man smiles and softly says: “You win, little friend.” He gently strokes its feathers. [Closing, 23–30s] The old man sits peacefully in the golden sunlight with the pigeon resting beside him. The pigeon closes its eyes comfortably. The old man smiles, closes his eyes and quietly laughs. Camera slowly pulls back, revealing the cozy balcony. [CONSISTENCY] One old man, one gray pigeon, same clothing, same balcony and same lighting throughout. No cuts, no scene changes, no character duplication. No subtitles or text. [Voice & Audio] Warm natural elderly male voice, gentle and slightly humorous. Only 2 short dialogue lines. Natural pigeon coos, soft wing flaps, morning birds, gentle wind, subtle comedic music during the funny moment, warm nostalgic during the ending.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `20.04s`

---

### 🎬 Kyoto Solo Date Walk
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11473.jpg" width="480" alt="SD2_11473"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/kyoto-solo-date-walk-SD2_11473">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 15-second ultra-realistic cinematic travel video set in Kyoto, Japan, following a young blonde woman on a peaceful solo date through traditional Kyoto streets. 0–2 sec: Front-facing medium shot of the woman standing outside a traditional Kyoto machiya townhouse with dark wooden lattice doors. She smiles naturally and makes a small playful hand gesture toward the camera. Warm late-afternoon sunlight, realistic skin and hair movement, shallow depth of field. 2–4 sec: Cut to a smooth handheld tracking shot from behind as she walks through a narrow traditional Kyoto alley. Wooden buildings, textured walls, small plants and warm sunlight create beautiful natural depth. Camera follows closely with subtle realistic motion. 4–6 sec: Wide rear tracking shot as she continues walking down a quiet stone-paved alley lined with traditional wooden houses and potted greenery. Soft golden-hour sunlight creates long shadows and gentle lens flare. 6–8 sec: She reaches a small canal and pauses beside the stone wall. A friendly orange-and-white cat walks along the edge of the canal. She looks toward it with a gentle smile. Natural water reflections, subtle breeze moving her hair and clothing. 8–10 sec: Cut to a close cinematic shot beside a Japanese vending machine. She buys a small red canned drink and takes a sip, smiling naturally. Realistic hand movement, authentic vending-machine details, shallow depth of field. 10–12 sec: Golden-hour street scene. She stands near a Kyoto road, casually looking around while a traditional yellow taxi passes behind her. Strong sun flare, realistic traffic movement, cinematic backlight. 12–15 sec: Return to the narrow wooden alley. She walks toward the camera holding her drink, then briefly turns and looks back with a soft smile. Camera slowly pulls backward, revealing the beautiful traditional Kyoto architecture as the scene fades naturally. Overall style: photorealistic Japanese travel film, authentic Kyoto atmosphere, natural human motion, realistic walking physics, subtle breathing and blinking, detailed hair and fabric movement, warm golden-hour lighting, soft cinematic lens flare, shallow depth of field, natural handheld/gimbal camera movement, realistic shadows and reflections, documentary-style cinematography, 35mm film look, premium travel commercial, highly detailed, seamless transitions, no artificial-looking CGI, no distorted hands or face, consistent character appearance throughout.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Epic Fantasy World Tree CGI
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11467.jpg" width="480" alt="SD2_11467"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/epic-fantasy-world-tree-SD2_11467">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-epic cinematic 3D CGI fantasy realm, pure original imagination, hyper-detailed photorealistic 3D render, Unreal Engine 5 + Octane quality, volumetric god rays, intricate crystalline geometry, living magic energy, 8K resolution, seamless continuous camera movement, 30 seconds. Sequence: 0-7 seconds: Colossal establishing shot of an impossible world suspended in the void. A single ancient World-Tree the size of a continent grows upside-down from a shattered floating continent, its roots forming living bridges of glowing amber crystal that stretch across the sky. Rivers of liquid starlight cascade upward into the heavens instead of falling. Slow majestic orbital camera movement as twin eclipsed suns cast dramatic dual-colored light (deep gold and electric violet). 7-15 seconds: Camera dives dramatically through the glowing roots into the heart of the World-Tree. Inside, vast hollow chambers filled with floating luminous orbs that contain entire miniature galaxies. Massive ethereal titans made of living stone and constellation patterns slowly awaken and walk along the inner walls. Energy storms of pure magic swirl in slow motion. Intense volumetric lighting and particle systems. 15-23 seconds: Camera explodes outward from the tree into open sky. A colossal sky-whale made of translucent crystal and nebula gas glides past, its body containing storms and lightning. Below, an entire civilization of spiraling crystal cities grows organically from the floating landmasses like living organisms. Giant rune-covered monoliths rise and rotate in the air, releasing waves of golden energy. Epic wide tracking shot with extreme depth and scale. 23-30 seconds: Final powerful pull-back into deep space revealing the entire original fantasy cosmos: the World-Tree at the center, surrounded by orbiting islands, sky-whales, and rivers of starlight forming a living mandala. The dual suns fully align, unleashing a massive wave of pure magical light that washes across the entire scene. Cinematic slow-motion ending on the glowing silhouette of the World-Tree against the cosmic void. Style: Pure 3D imagination only, no 2D, hyper-realistic materials, extreme scale contrast, dramatic lighting, rich atmospheric haze, intricate original designs never seen before, epic and awe-inspiring mood, seamless one-shot feeling.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Xianxia Sisters Stoic Challenge Scene
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11463.jpg" width="480" alt="SD2_11463"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/xianxia-stoic-challenge-SD2_11463">🌐 Watch Online</a>

#### 📝 Prompt
```
Cinematic realism, pure ancient Chinese fantasy aesthetics, restrained yet comedic performances, observational cinematography, realistic micro-expressions, body weight, silk textures, delicate film grain, volumetric atmospheric depth, realistic 3D camera movement, and a reference world that continuously exists from the first frame to the last. Control Protocol—Three tracks must operate simultaneously, but none can usurp narrative control. The protagonist&#39;s storyline track has 100% control. The environment&#39;s lifeline track has continuous movement rights but 0% control. The background character track has independent life rights but 0% interaction rights with the protagonist. The environment cannot create, trigger, explain, interrupt, resolve, change, emphasize, or obstruct any character&#39;s storyline. Wind, clouds, fog, light, reflections, buildings, distant characters, vegetation, and water cannot react differently to dialogue, eye contact, comedic moments, or the protagonist&#39;s actions. The camera&#39;s movement is determined solely by the protagonist&#39;s storyline and character movement. However, at the same time: all non-protagonist areas must never be frozen. All currently uploaded reference images are understood as the DNA of the world, not frozen pixels or a static background that needs protection. Before the actual generation, the topographical logic, architectural vocabulary, scale relationships, materials, weather, cloud systems, vegetation, reflective surfaces, traffic routes, main light directions, foreground-midground-background relationships, and off-screen spatial extensions within the reference images are comprehensively understood. Then, a realistically connected 3D location is reconstructed. The identity and logic of the reference world are preserved, but the spatial arrangement and camera entry direction are allowed to be rearranged, without mechanically copying the original 2D composition of any reference image. Throughout the 10 seconds, each approximately 2-second time window requires multiple clearly visible non-protagonist movement sources at different spatial levels. These movements cannot start simultaneously, nor can they move at the same speed. Extreme distance: A huge, plausible cloud or air layer in the current world, which has been slowly and steadily migrating through the grand distant structure since before the scene begins. Deep midground: 4–6 small distant environmental characters are arranged as independent extras. One of them walks continuously for several seconds along a realistic passageway in the distance. Another person ascends or descends along existing steps or paths. Another person pauses to adjust their sleeves, belongings, or clothing, then continues. The other two can naturally pass each other, each going their own way. All their actions are unrelated to the two main characters. They must not look at the main characters. They must not stop because the main characters stop. They must not turn around because the main characters speak. They must not synchronize their movements for comedic effect. No visible background character can be completely frozen for an entire 10 seconds. Mid-range air layer: Fog, low clouds, or other reasonably existing air volume in the current reference world, continuously moving around real buildings and terrain. Fog must be able to be obscured by physical buildings. It should be briefly invisible after entering behind a building. It should then reappear from the other side according to the actual spatial relationships. It must never pass directly through physical structures. Foreground layer: During the actual movement of the camera, a foreground element consistent with the current reference world—fog, vegetation, banners, building edges, or other reasonable objects—shortly passes close to the lens. This makes the audience clearly feel that the camera is inside the space. If the reference environment contains water, damp stone, metal, jade, or other reflective surfaces, their reflections must continuously change with the camera position and viewing angle, and cannot be fixed as if drawn on a background image. All environmental movements share the same weather system and uniform wind direction. Character A, Sword Immortal Senior Sister: 25-30 years old, East Asian woman, oval face, fair complexion, dark almond eyes, long black hair half-up and secured with a white jade hairpin, tall and slender, wearing a white embroidered silk Hanfu, semi-transparent layered wide sleeves, silver waist belt, jade pendant, and white cloth boots. Character B, Junior Sister: 20-25 years old, East Asian woman, round and lively face, black hair braided, petite figure, wearing a light green linen Hanfu, dark belt, wooden hairpin, and black cloth shoes. 0-5s Panoramic or Long Shot – Main Character Track: The camera begins a realistic forward and slightly lateral push-in track from the interior of the reconstructed 3D world. Foreground space or air layers briefly pass near the lens. Mid-ground buildings create a clear parallax shift relative to the extremely distant background. The two walk side-by-side normally. Suddenly, the same senior swordswoman says very seriously, &quot;Today we&#39;ll practice concentration.&quot; The same junior sister turns slightly to look at her. The senior swordswoman continues, &quot;Whoever laughs first loses.&quot; The junior sister immediately puts on a completely expressionless face. Both stop simultaneously and turn to face each other. This entire scene only occurs because the senior swordswoman proactively suggests practicing concentration. It must not be triggered by any background changes. 0-5s Environmental lifecycle: While the two are speaking, a huge cloud in the distance continues to slowly migrate in its original direction. A distant character continues to cross a distant platform laterally. Another character continues to move along a real road or steps. Mid-range fog continues to flow at its original speed. Locally stable wind fields continue to produce small movements of clothing, vegetation, or hanging objects. The background cannot suddenly move when the dialogue begins. The background cannot stop when the two stop. 5-10s Mid-range two-person shot/cowboy scene—protagonist storycycle: The two face each other, about an arm and a half apart. Both try to maintain completely expressionless faces. No magic. No sword drawn. The environment is irrelevant. To break her senior&#39;s composure, the junior sister makes only a tiny movement: one cheek puffs out very slightly for about half a second, then immediately returns to normal. The sword-wielding senior almost reacts, but forces herself to remain calm. She raises one eyebrow with a tiny movement. The junior sister&#39;s lips almost curl upwards, but she immediately lowers them. The sword-wielding senior&#39;s lips also begin to tremble almost imperceptibly. Neither of them can truly laugh during this segment. The camera moves slowly and realistically in a small arc of about 15–20 degrees around the two characters. The camera must actually change position. Digital zoom cannot be used to simulate surround movement. This creates realistic parallax at different speeds in the near, middle, and far background. The comedy comes solely from the micro-expressions and restraint of the two characters. For 5-10 seconds, the environmental life track and the background character track continue to run independently: after the characters enter the medium close-up, the background world must not be turned into a static scene just because the shot begins to emphasize the face. Multiple clear motion sources must still be preserved at different depths. A figure in the distance continues walking forward, naturally obscured by existing buildings as they move. Another background figure emerges naturally from another previously obscured space and continues their path. The volume of air continues to move behind and between buildings. As the camera moves in an arc, the mid-ground structures and distant spaces continue to create different parallaxes. Clouds, fog, reflections, and distant figures must not stop moving even when the protagonist is making micro-expressions. All background movements are out of sync with the protagonist&#39;s rhythm. Ending transition: 9.5-10 seconds, the two protagonists&#39; bodies are kept as stable as possible to facilitate a smooth transition. However, only the characters must be stabilized, not the world frozen. The Sword Immortal Senior Sister and Junior Sister are still facing each other. Both are clearly about to burst out laughing but are still forcibly maintaining a serious demeanor. The characters&#39; center of gravity, gaze, and expressions are clear. The camera gradually stabilizes. At this point, the distant clouds can still be seen continuously moving. At least one distant figure is in the process of walking, not standing as a static human-shaped sticker. The mid-ground air is still in motion. At least one reflection or lighting condition is still continuously evolving. This precise state of &quot;stable characters, but the world still in motion&quot; serves as the transitional state for the second segment. It features a 16:9 landscape aspect ratio, native synchronized Mandarin dialogue, restrained background music, and realistic footsteps, fabric sounds, distant footsteps, wind sounds, and ambient sounds. The screen includes two main female characters, while also allowing for smaller, completely independent figures in the distance. No subtitles are generated, and no modern elements are present. Negative (paragraph 1 independent): blurry, bad quality, low quality, low resolution, noisy, jpeg artifacts, watermark, text, subtitles, error; deformed, mutated, bad anatomy, poorly drawn hands, bad composition, out of frame, disfigured; inconsistent protagonist identity, changing clothes, face morphing, hairstyle change; static background plate, frozen scenery, frozen background people, background people standing motionless for the whole clip, living people rendered as landscape texture, duplicated background extras, background extras staring at protagonists, background extras synchronizing with protagonists, background extras reacting to dialogue, background extras reacting to comedy; flat 2D reference image, animated wallpaper, camera sliding over a photograph, fake digital zoom, fake parallax, foreground midground and background moving at identical speed, no occlusion, no object permanence, fixed cloud texture, static cloud sea, frozen mist, static reflections, painted reflections, static distant people, lifeless surrounding architecture, environment stopping during dialogue, environment stopping during close-up, environment freezing When the protagonists stop, all environmental movement begins simultaneously, synchronized with plot beats, dramatic wind caused by dialogue, cloud change caused by laughter, lighting change used as punchlines, environment creation or story solving, camera following weather instead of protagonists, random new landmarks, impossible geometry, background replacement, teleporting extras, modern elements, and glitching cuts. The second segment is generated as an independent extended video. If the current Seedance workflow allows video continuation or video reference, the complete first segment video itself is prioritized as the temporal motion reference, while the last frame of the first segment is used as the opening visual state of the second segment. It is absolutely unacceptable to simply regenerate a &quot;similar&quot; location. The same world must continue moving forward along the timeline established in the first segment. The same sword-wielding senior sister and junior sister must be fully inherited, including identical faces, hairstyles, body proportions, clothing, accurate positioning, the suppressed laughter expression at the end of the previous segment, gaze, camera height, camera axis, and lens perspective. The motion phase of the living world itself must also be inherited. The background characters who were walking at the end of the first segment continue walking from their previous position and direction. They cannot return to the starting point. The clouds continue to migrate, maintaining their previously established direction and speed. The flowing fog continues its movement from the actual spatial state at the end of the previous segment. Reflections continue to evolve. It cannot suddenly revert to the state at the beginning of the first segment. The permissions of the three tracks remain completely unchanged: Main character plot track = 100% scriptwriting rights. Environmental life track = continuous physical movement rights, 0% scriptwriting rights. Background character track = independent living rights, 0% main character interaction rights. The background cannot cause the two characters to laugh. The environment cannot decide their wins or losses. Background characters cannot help complete the punchline. 10-15s close-up of two characters/restrained arc movement—Main character plot track: directly from the exact expressions of the two characters trying to suppress laughter at the end of the first segment. Both continue to try not to laugh. The same junior sister changes her strategy. She suddenly adjusts her posture to be extremely dignified, and then very seriously imitates the aloof, calm, and serious expression of the sword immortal senior sister. The same senior swordswoman immediately recognized that she was being imitated. A very slight change occurred in her nostrils. She held it in. Seeing this subtle reaction, the junior sister&#39;s lips began to tremble more noticeably. The senior swordswoman then noticed the junior sister struggling to suppress her laughter. So now it became: both of them were trying not to react to the other&#39;s effort not to laugh. They used only very small micro-movements, gradually escalating: a raised eyebrow, a suppressed breath, a slight tremor of the lower lip, an almost imperceptible shoulder tremor. No exaggerated ugliness. No large comedic movements. The environment was completely uninvolved in the humor. At approximately 14.5 seconds, both of them finally broke down at the exact same moment, simultaneously letting out a short, genuine laugh. This laugh could only come from the mutual expression of their reactions. For 10-15 seconds, the environmental lifeline continued simultaneously: even when the camera moved into close-up of the characters, the space behind them must still have clearly visible movement. One background character who was already walking in the first segment continued their path and was then naturally obscured by the existing architecture. Another background character passed through a deeper layer of space along a different path. A third background character performs a very small, unrelated action, then continues walking. The distant clouds continue to shift. The fog continues to move. Reflections continue to change with subtle shifts in the camera angle. The moment the two laugh: there can&#39;t be a sudden gust of wind. There can&#39;t be a sudden switch on the lights. The background character can&#39;t turn their head. The fog can&#39;t suddenly accelerate. There can&#39;t be any synchronized reaction from the background. 15-20s Mid-to-long shot ending—Protagonist&#39;s storyline: After a brief laugh, the two immediately regain their seriousness. The junior sister asks, &quot;A tie?&quot; The sword-wielding senior sister thinks for a second: &quot;Let&#39;s start again.&quot; The junior sister nods seriously. The two solemnly restore their extremely formal expressions. Then they simultaneously turn back to the front. They continue walking forward side-by-side normally. After taking two steps: The junior sister casually glances at her senior sister. Unexpectedly, the same sword-wielding senior sister is already glancing at her. Their eyes meet. A very subtle smile reappears on both their lips. But this time, neither speaks. Don&#39;t add a third punchline. Finally, maintain an observational lingering effect. 15-20s Camera Track and Environmental Lifeline: As the two characters resume walking, the camera transitions to a soft three-quarter profile follow shot. The camera movement is still solely due to the characters walking. However, the camera must realistically create spatial displacement. A foreground layer, consistent with the reference world, naturally sweeps across the frame from one side. The two main characters are in the midground. In the deeper space, at least two autonomous background characters remain active. One character passes through a misty area, partially obscured by the air layer, and continues moving. The other character passes through at a significantly different speed at different depths. The vast, distant landscape moves very slowly relative to the others. The clouds and fog completely inherit the original direction of movement from the first segment and do not restart. If reflective surfaces exist in the scene, the highlights slide continuously as the camera&#39;s lateral position changes. After the characters&#39; final eye contact and laugh, the background movement continues. Last 0.5 seconds: The two main characters are still walking forward. Simultaneously, the audience can still clearly see multiple independent sources of movement from non-main characters. The laugh has ended, but the world has not. 16:9 landscape mode, native synchronized Mandarin dialogue with realistic short laughs, precise lip-syncing, seamless transition with the first segment of the video, realistic camera parallax, autonomously moving background characters, continuous air movement, physically plausible dynamic reflections and ambient sound. Two main female characters, while also allowing for small background characters. No subtitles generated, no modern elements included. Negative (independent paragraph 2): blurry, bad quality, low quality, low resolution, noisy, jpeg artifacts, watermark, text, subtitles, error; deformed, mutated, bad anatomy, poorly drawn hands, bad composition, out of frame, disfigured; inconsistent protagonist identity, changing clothes, face morphing, hairstyle change; background reset between clips, background motion restarting from zero, background extras returning to starting positions, frozen background extras, static distant people, living people rendered as scenery texture, duplicated extras, disappearing extras without occlusion, background extras watching protagonists, background extras reacting to laughter, background extras laughing with protagonists, synchronized background choreography; flat background plate, static reference image, animated wallpaper, fixed cloud sea, frozen cloud structure, frozen mist, static reflections, painted reflections, fake parallax, digital zoom instead of camera translation, foreground midground background moving at identical speed, environment freezing in close-up, environment freezing during dialogue, environment freezing when protagonists laugh, environment freezing after punchline, environmental event causing laughter, wind gust synchronized with laugh, cloud burst synchronized with joke, sunlight burst at punchline, mist revealing something at story beat, background solving the contest, camera following environmental motion instead of protagonists, new random architecture, scenery replacement, impossible geometry, extra foreground protagonists, modern elements, glitching cuts
```

#### 📌 Details
- Ratio: `1.78` | Duration: `20.07s`

---

### 🎬 Penthouse Assassin Takedown
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11459.jpg" width="480" alt="SD2_11459"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/penthouse-assassin-takedown-SD2_11459">🌐 Watch Online</a>

#### 📝 Prompt
```
0–3s: The Ignition Action: Standing near the grand bar of an ultra-luxurious, glass-walled penthouse lounge overlooking a neon cityscape. Audio: Smooth jazz music distorted by the sharp pop of champagne corks and the sudden shattering of high-end crystal glassware. Visual: She detects a hidden assassin drawing a silenced pistol from a velvet jacket; she instantly grabs a heavy crystal decanter and hurls it across the bar, shattering it against his face. 3–6s: CQC Blitz Target A: Staggered by the glass splinters → she Vaults over the polished mahogany bar top, sweeps his standing leg, and drives his head into the hardwood floor. Target B: Closes in with an extendable stun baton → she snatches a silk curtain sash from the floor-to-ceiling drapery, wraps it around his neck mid-swing, and chokes him back over her shoulder. SFX: Bass-heavy lounge music, breaking glass, the heavy thud of bodies hitting hardwood, and crackling high-voltage sparks. 6–8s: Wardrobe & Atmosphere Detail: Tailored backless evening gown made of emerald silk, slit to the thigh, wearing heavy gold cuff bracelets and red lipstick. Environment: The penthouse ceiling sprinklers trigger, sending a warm, misting rain throughout the room that glints in the ambient blue-and-magenta LED accent lighting. 8–11s: The Grapple Target C: Charges her with a brass-knuckled fist → she steps fluidly into his guard, catches his punch arm, and uses the wet silk drapery line to bind his arm to his torso. Target D: Approaches from behind with a taser → she executes a tight pivot, wrenching Target C’s bound body directly into Target D's path so the taser prongs embed into Target C's jacket. 11–13s: The Finisher Action: Snatches a heavy brass champagne bucket off a stand → spins and launches it like a hammer throw straight into the floor-to-ceiling glass wall behind the guards. Visual: The reinforced glass spiderwebs instantly and blows outward from the wind pressure, creating a massive vacuum draft that pulls the disoriented guards off their feet toward the open ledge. 13–15s: The Aftermath Tone: High-society elegance violently dismantled into wind-swept, high-altitude exposure. Action: The room fills with howling wind and mist. She picks up her clutch bag from the bar, steps past the dazed attackers clinging to the floor bolting, and calmly walks into the private service elevator. Audio: The roaring wind whipping through the shattered glass frame instantly muted as the heavy brass elevator doors slide shut.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Noble Master's Hilarious Misunderstanding
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11457.jpg" width="480" alt="SD2_11457"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/noble-master-misunderstanding-SD2_11457">🌐 Watch Online</a>

#### 📝 Prompt
```
Japanese full-color anime style. Japanese TV anime style. Cel-shaded anime. Anime-style screen captures mainly using flat colors. 0-2 seconds: The background is an 18th-century French town. The long-haired blonde male character wearing a top hat in Image 1 is walking along when he seems to spot something and hides behind a building. 2-4 seconds: A close-up of the long-haired blonde male character wearing a top hat in Image 1 peeking out from behind the building, viewed from a diagonal side angle. 4-6 seconds: The black-haired maid character in Image 2 is smiling and talking with a young greengrocer. 6-8 seconds: A close-up of the black-haired maid character in Image 2, viewed from a diagonal side angle. She is smiling with her eyes closed. She has her fist to her mouth. She shows the back of her fist to the camera. The background is sparkling ✨✨. 8-10 seconds: The long-haired blonde aristocratic male character wearing a top hat in Image 1 has a shocked, cartoonish face. Oh no. 10-14 seconds: From here on, the scene takes place inside the mansion. The character in Image 3 is in a room, hence the clothing. The blonde, long-haired nobleman in Image 3 is so shocked that a white soul is coming out of his mouth. He is sitting on a sofa, exhausted, with a cartoonish face and round, white eyes. The black-haired maid character in Image 2 appears from the right of the screen. The black-haired maid character in Image 2 says, &quot;Master, what&#39;s wrong?&quot; 14-18 seconds: A close-up of the blonde, long-haired male character in Image 3&#39;s downcast face, viewed from a diagonal angle below. &quot;Elsa was talking to a man with a really nice smile.&quot; He can&#39;t hide his shock. 18-22 seconds: A diagonal side view of the black-haired maid character in Image 2. &quot;If you treat her well, she&#39;ll give you tomatoes as a bonus.&quot; 22-25 seconds: The blonde male character in Image 3 looks up, with a sparkling, bright smile, viewed from above. &quot;What, that&#39;s all? Oh well, I thought...&quot; 25-30 seconds: A front view of the two of them. A blonde, long-haired male character in Image 3 is sitting on a sofa and looking up at the black-haired maid character in Image 2, while the black-haired maid character in Image 2 is standing facing him. Black-haired maid character in Image 2: &quot;I thought so?&quot; Blonde, long-haired male character in Image 3: &quot;No, nothing.&quot; He quickly turns his face away.
```

#### 📌 Details
- Ratio: `1.34` | Duration: `29.7s`

---

<!-- STATS_END -->
