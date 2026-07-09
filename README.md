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
- Total Prompts: **5272**
- Updated Today (UTC 2026-07-09): **28**

## 🎬 Today's Updates
### 🎬 Planet Shutter Chase
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05293.jpg" width="480" alt="SD2_05293"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/planet-shutter-chase-SD2_05293">🌐 Watch Online</a>

#### 📝 Prompt
```
10-second cinematic sci-fi action sequence, 16:9, ultra-realistic, breathtaking scale, realistic physics, no visible face. A fighter flies through a gigantic artificial world. The interior contains continents, cities and oceans. Suddenly a planetary defense system activates. Enormous armored plates begin sliding across the sky. Each plate is hundreds of kilometers wide. The world is literally closing. Sunlight disappears section by section. The pilot races through narrowing corridors of light. Entire landscapes vanish beneath moving armor. The remaining opening becomes smaller and smaller. The fighter dives toward the last visible gap. The planetary shutters collide behind him. Cut.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.13s`

---

### 🎬 Nike Emerald Aurora Campaign Film
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05292.jpg" width="480" alt="SD2_05292"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/nike-emerald-aurora-campaign-SD2_05292">🌐 Watch Online</a>

#### 📝 Prompt
```
VIDEO PROMPT — "EMERALD AURORA" Nike Air Max 95 Big Bubble Campaign Film (15s) Style & Mood Premium athletic fashion campaign film. Monochromatic emerald palette — deep emerald green, jade, mint green, pale sage, warm cream — across every surface, garment, background, and product. Soft diffused studio light with warm emerald ambient fill and dramatic single spotlight for silhouette shots. Fluid emerald liquid-glass splashes, motion blur streaks, and champagne-gloss reflections as recurring visual elements. Confident feminine energy. Every frame is editorial-poster quality. Model: Mid-20s Western female, fair sun-kissed skin, striking emerald-green eyes, long tousled honey-blonde hair in loose waves, toned athletic build. Same face, hair, and styling consistent across every shot — no drift. Dynamic Description Shot 01 — Aurora Bloom (0–2.5s): Wide macro product hero — the Nike Air Max 95 Big Bubble in Emerald Aurora floats at a dynamic diagonal angle above a swirling jade-green liquid surface, the liquid curling upward in slow-motion silk waves on both sides of the shoe, translucent emerald spherical droplets suspended in the air around the sole, the champagne-tinted Air bubble unit sharp at frame bottom. Camera pushes slowly toward the sneaker from a low front angle. Text "AURORA BLOOM" fades in lower left in thin white sans-serif. Hard cut. Shot 02 — Air Max 95 Macro Reveal (2.5–5s): 100mm macro slow right-to-left slide — the heel section fills the frame, the large champagne-tinted Air bubble unit glowing warmly under diffused studio light, the quilted sage-green suede panels with stitching lines sharp in the foreground, the deep emerald leather overlay curving across the upper third. Camera slides slowly revealing the Air bubble left to right, light raking across the suede grain and gradient color transitions. Text "AIR MAX 95" fades in upper left. Hard cut. Shot 03 — In Motion Walk (5–7.5s): Wide stabilized shot — the model in a cream crop top and loose sage-green cargo trousers walks directly toward camera in slow motion, honey-blonde hair flowing behind her as she strides forward, wearing the Emerald Aurora sneakers, a single warm spotlight from above casting a soft shadow ahead of her, background a warm emerald-toned empty studio, soft jade light wrapping her left side. Camera holds at chest height, very slow forward drift. Text "IN MOTION" fades in lower right. Hard cut. Shot 04 — Built to Move (7.5–10s): 35mm dynamic handheld — the model leaps mid-air from left to right in a presidential jump, both feet off the ground, right knee raised, arms swinging, the Emerald Aurora sneakers sharp at the bottom of the frame, motion blur streaks of deep emerald trailing behind her across the frame, hair horizontal in motion, background a gradient of warm cream to deep jade. Camera at mid-body height, slightly handheld, following the arc of the leap. Text "BUILT TO MOVE. / MADE TO STAND OUT." fades in lower left in spaced white caps. Hard cut. Shot 05 — Big Bubble Product Packshot (10–12.5s): Static locked-off center composition — the Nike Air Max 95 Big Bubble sits alone on a minimal pale-sage surface at a clean three-quarter angle, full shoe visible, the oversized champagne-tinted Air bubble unit prominent at the heel, deep emerald lace cage and swoosh logo sharp, small leaf-shaped charm on the lace eyelet catching the light. Soft overhead studio light, no distractions. Camera holds completely still. Text "AIR MAX 95 / BIG BUBBLE" fades in upper center in thin white type. Hard cut. Shot 06 — Just Do It Silhouette End Frame (12.5–15s): 85mm static locked-off — background transitions to a deep rich forest-emerald with a single warm spotlight circle on the wall behind. The model stands in confident pose slightly right of center, one hand on hip, head turned in profile, ponytail falling over one shoulder, the Emerald Aurora sneakers visible on her feet, her silhouette almost entirely in dark shadow against the glowing emerald backdrop with only the edge of the spotlight defining her outline and catching the cream sole of the shoe. The Nike Swoosh logo in solid white appears upper right, beneath it "JUST DO IT." in white spaced tracking. Frame holds locked. Slow fade to black.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 Ultra-Premium Audio Jewelry Campaign
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05291.jpg" width="480" alt="SD2_05291"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ultra-premium-audio-jewelry-SD2_05291">🌐 Watch Online</a>

#### 📝 Prompt
```
Style & Mood: Ultra-premium audio jewelry campaign. Acoustic, sculptural, pure. Pearl white and space black studio environments. The ceramic shell catching directional light in clean organic curves. Mint green Æ emblem a precise point of color on the white
```

#### 📌 Details
- Ratio: `0.75` | Duration: `15.08s`

---

### 🎬 Runner's Epic World Journey
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05290.jpg" width="480" alt="SD2_05290"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/runners-epic-world-journey-SD2_05290">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: Ultra-realistic, cinematic, high-energy sports commercial, 4K HDR, dynamic lighting, dramatic slow motion, seamless environment transitions. 0–3s: Close-up of a runner tightening their running shoes at dawn. The camera follows as they take their first step onto a quiet city street. The impact creates a ripple of light across the pavement. 3–6s: With the second stride, the city seamlessly transforms into a lush green forest. The camera tracks beside the runner as sunlight streams through the trees. 6–9s: The third stride lands on a rocky mountain trail. Snow-capped peaks appear in the distance while the runner continues without slowing down. Aerial drone shot reveals the breathtaking landscape. 9–12s: The fourth stride transitions into a golden desert at sunset, then instantly onto a stunning coastal cliff road with waves crashing below
```

#### 📌 Details
- Ratio: `1.78` | Duration: `13.93s`

---

### 🎬 Korean Morning GRWM Routine
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05289.jpg" width="480" alt="SD2_05289"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-morning-grwm-routine-SD2_05289">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a realistic GRWM (Get Ready With Me) lifestyle video featuring a stylish Korean woman with long silky black hair, radiant skin, and a fresh natural look. Bright modern apartment with floor-to-ceiling windows, warm morning sunlight, cozy Scandinavian décor, premium fashion vlog aesthetic, cinematic handheld camera, ultra-realistic photography. The video opens with her stepping out of the bathroom wrapped in a soft white bath towel, gently drying her damp hair while smiling at herself in the mirror. She walks into her bright bedroom where sunlight fills the room and soft music plays in the background. She changes into a cute pastel crop-top pajama set with matching shorts and begins her morning skincare routine using cleanser, toner, serum, moisturizer, and lip balm. Cinematic beauty close-ups highlight her naturally glowing skin. She sits at her vanity and styles her hair into soft loose waves before applying fresh everyday makeup with foundation, blush, mascara, soft eyeliner, and a glossy pink lip tint. She smiles naturally while checking her makeup in the mirror. She walks to her wardrobe and browses several outfits before choosing a fitted white crop top with high-waisted blue jeans. She changes into the outfit, accessorizes with small gold hoop earrings, a delicate necklace, sunglasses, and sprays her favorite perfume. Standing in front of a full-length mirror, she admires her outfit, spins once with a smile, takes a quick mirror selfie, then grabs a small shoulder bag and her phone. The video transitions outdoors as she strolls through a sunny neighborhood lined with cafés and flowers. She arrives at a charming artisan ice cream shop, happily choosing her favorite flavor. She receives a colorful waffle cone, takes the first bite with a bright smile, and laughs while enjoying the sunny afternoon. She walks through the park eating her ice cream, occasionally looking toward the camera with a playful expression. The video ends with her sitting on a park bench under golden sunlight, enjoying the last bite of her ice cream as the camera slowly pulls back to reveal the peaceful surroundings. Style: premium GRWM fashion vlog, luxury lifestyle content, cozy summer aesthetic, cinematic handheld camera, warm natural lighting, elegant transitions, photorealistic, shallow depth of field, vibrant colors, commercial-quality visuals, 4K HDR, 16:9 widescreen, no subtitles, no text overlays.
```

#### 📌 Details
- Ratio: `1.72` | Duration: `15.07s`

---

### 🎬 Cinematic Morning Lifestyle Routine
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05288.jpg" width="480" alt="SD2_05288"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-morning-lifestyle-SD2_05288">🌐 Watch Online</a>

#### 📝 Prompt
```
Create an ultra-realistic cinematic lifestyle video featuring the same young woman throughout the entire sequence. Maintain identical facial features, hairstyle, body proportions, outfit, and accessories in every shot. She wears a white ribbed crop top, beige cotton shorts, white ankle socks, and a messy high ponytail. The setting is a bright, modern apartment filled with warm morning sunlight, wooden furniture, soft neutral décor, and plenty of indoor plants. The video begins with her waking naturally and stretching beside the bed as golden sunlight pours through sheer curtains. She smiles, takes a deep breath, and walks into the bathroom where she gently washes her face before applying her complete skincare routine in front of the mirror. She massages moisturizer into her skin, applies serum, and admires the healthy glow with a relaxed smile. She walks into the living room, picks up a cordless vacuum cleaner, and begins cleaning the apartment. While vacuuming, she playfully dances to herself, laughing naturally as she spins around the room. Sunlight streams through the large windows, creating soft shadows across the floor. She opens the sliding balcony door and steps outside carrying a watering can. She carefully waters rows of colorful flower pots and lush green plants, gently touching the petals and leaves while enjoying the peaceful morning breeze. Butterflies flutter nearby as sunlight illuminates the flowers. After finishing, she prepares a large iced coffee, sits comfortably in a balcony chair surrounded by blooming plants, and quietly enjoys the view over the city skyline. She closes her eyes for a moment, feeling the warm breeze, then notices the camera, smiles softly, raises her coffee toward the lens in a friendly toast, and relaxes as the camera slowly pulls back to reveal the peaceful balcony garden. Natural ambient audio only: birds chirping, gentle breeze, distant city ambience, vacuum cleaner, running water, footsteps, leaves rustling, water pouring onto plants, coffee ice clinking softly. No background music, no subtitles, no logos, no watermarks, and no on-screen text. Premium commercial-quality cinematography, smooth handheld lifestyle camera movement, realistic skin texture, natural facial expressions, detailed hair movement, physically accurate lighting, warm golden morning atmosphere, 16:9 widescreen.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Stadium Tears of Joy
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05287.jpg" width="480" alt="SD2_05287"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/stadium-joy-tears-SD2_05287">🌐 Watch Online</a>

#### 📝 Prompt
```
Subject: A close-up, candid shot of a young woman experiencing an overwhelming moment of joy and emotion in a crowded football stadium. Expression & Emotion: She is crying happy tears, eyes glistening with moisture, with a soft, genuine. Her hands are pressed together in front of her chest as if clapping or in a moment of intense gratitude. Hair & Makeup: Sleek, dark hair pulled back into a high, neat ponytail. Makeup is natural and dewy, focusing on fresh skin texture with a healthy, natural flush on the cheeks and eyelids caused by emotion. Lips are glossy and natural. Outfit & Accessories: Wearing a white and light blue/mint patterned sports jersey (fan shirt) portugal that is tied at the waist. She is wearing bold, large, red statement earrings. Neck is adorned with a delicate thin gold chain necklace with small charms. Wrists feature stacked thin gold bracelets and rings on her fingers. Setting & Atmosphere: Background is a blurred, massive football stadium filled with a crowd. The atmosphere is energetic and loud, with hints of red and team colors in the blurred background. Photography Style: Authentic smartphone camera aesthetic, camera wide iphone 17 pro max, candid photography, high resolution, sharp focus on facial features and eyes, natural stadium lighting, raw and honest emotional vibe, 8k resolution, realistic skin textures. Negative Prompt (text, watermark, logo, UI elements:1.5), (distorted face:1.5), (bad anatomy:1.4), (plastic skin:1.5), (cartoon, illustration, 3d render:1.5), (studio lighting:1.5), (harsh shadows:1.4), artificial filters, overly airbrushed, fake tears, expressionless, rigid posing, low resolution, closed eyes, looking away from camera.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `22.23s`

---

### 🎬 Wildlife Documentary Visuals
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05286.jpg" width="480" alt="SD2_05286"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/wildlife-documentary-visuals-SD2_05286">🌐 Watch Online</a>

#### 📝 Prompt
```
Wolf: "wolf moves silently through dense snow-covered boreal forest, extreme close-up on snout reading scent particles, ultra slow motion, no narration, documentary" Whale: "humpback whale navigating open ocean by echolocation, sound waves visible as geometric ripples through blue water, slow drift, cinematic" Glacier: "glacier retreating in time, clinical wide shot, no color grading, raw blue-grey ice, just time passing, no music" Butterfly: "monarch butterfly mid-flight, Earth's magnetic field lines visible as faint luminous threads guiding its path, 2000-mile migration, macro lens, golden hour"
```

#### 📌 Details
- Ratio: `1.78` | Duration: `96.97s`

---

### 🎬 Pastel Mob Beach Dance Party
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05285.jpg" width="480" alt="SD2_05285"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pastel-mob-beach-dance-SD2_05285">🌐 Watch Online</a>

#### 📝 Prompt
```
A Japanese full-color anime with no captions, no background music, rapid-fire editing, a high frame count, and 24 FPS. Use 「アット」image1 as the main reference for the overall pastel beach-pop mood, shark-hoodie styling, cute character proportions, and playful summer energy. Use 「アット」image2 as the reference for calm-cute facial rendering, pastel eye design, and soft fashion balance. Use 「アット」image3 as the reference for the brighter pastel shark motif, simplified cute silhouette, and pop color blocking. Use 「アット」image4 as the reference for expressive face variety, comic-style split-panel layouts, and energetic reaction diversity. Use 「アット」image5 as the reference for exaggerated cute-chaotic expressions, candy-like graphic decoration, and playful visual intensity. Reference 「アット」audio1 only for beat timing and rhythm if an audio reference is later provided. Do not generate music. Goal: Create a 15-second 720p anime MV-style sequence showing a small group of cute pastel mob dancers joyfully dancing together. The scene should feel playful, bright, social, and energetic, like a fun crowd dance or kawaii flash-mob moment. Do not lock the performance into one exact choreography. Let Seedance infer the dance naturally from the references: group swaying, bouncing, step-touch rhythms, simple synchronized moves, playful arm gestures, turns, reactions, spacing changes, and cheerful group interaction. Focus on lively group motion, camera play, split-screen rhythm, and a cute party atmosphere. Use camera effects and panel composition actively, but keep the characters readable and fun. 0-3s: Open with a lively group reveal. Show multiple cute mob dancers already in motion, using a wide shot, medium group shot, or fisheye-led opening chosen naturally by the generation. Let the group feel immediately active and upbeat. Use playful camera motion, light fisheye distortion, and buoyant rhythm. The dancers should not hold one fixed pose; they should already be moving together in a casual but coordinated way. Floating bubbles, stars, candy-like shapes, clouds, pastel particles, and beachy pop motifs may move through the frame. 3-6s: Move into a more dance-focused section. Let Seedance infer a variety of cute mob-dance actions: small synchronized steps, side-to-side movement, hand waves, shoulder bounces, light turns, call-and-response gestures, and little formation changes. Use alternating camera sizes: medium group shots, brief close-ups, and occasional fisheye push-ins. Show the group’s fun and shared rhythm rather than one leader doing all the work. The dancers should feel like a cheerful crowd moving together. 6-10s: Introduce split-panel and collage rhythm. Break the frame into multiple angled panels that show different dancers, different moments, or different fragments of the same group dance. Some panels may show close-up expressions, some body movement, some group spacing, some hands or accessories. Do not repeat the same pose across all panels. Let the panels behave like a playful remix of the dance. Use sliding panel borders, snapping cuts, slight rotation, and rhythmic reassembly. Allow occasional prism-like edge duplication, cute glitch fragments, or macro inserts of accessories and eyes, but keep the dance energy central. 10-13s: Escalate the group energy. Let the mob dance become more animated and varied without becoming chaotic noise. Seedance may infer little jumps, spins, bounce accents, quick turns, mirrored motions, or playful interaction between neighboring dancers. Use camera effects more actively here: fisheye close-ups, brief macro flashes, snap zooms, whip-like transitions, and layered panel bursts. The group should feel increasingly joyful and lively, as if the dance is peaking. 13-15s: Do not force a standard final hero pose. Let the ending emerge naturally from the dance. Possible endings may include: the group clustering together while still moving, a playful freeze during motion, a split-panel collapse into one group image, a joyful reaction burst, a cute jump or bounce accent, or a clean energetic cut while the dance is still alive. The final beat should feel fun, spontaneous, and satisfying, without looking mechanically predetermined. Keep: - Keep the overall design language consistent with the references: pastel pink, cyan, mint, yellow, lavender, sky blue, and candy-pop accents. - Keep the characters chibi-cute, stylized, expressive, and visually unified, while allowing some variety between mob dancers. - Keep the shark-hoodie / beach-pop / candy-kawaii styling language from the references. - Keep the mood fun, light, social, and energetic. - Keep the animation group-oriented, with multiple dancers visible across the sequence. - Keep the visual emphasis on cheerful dancing, panel rhythm, cute expressions, and playful camera effects. - Keep the rendering flat, graphic, clean, colorful, and slightly sketchy with lively line energy. - Keep the sequence readable even when the edits become fast. Avoid: - No generated text, no subtitles, no logos, no readable signs. - No dark or horror tone. - No gore, no violent imagery. - No realistic live-action look. - No lonely solo performance for the whole clip; it should clearly feel like a mob dance or group dance. - No rigid repeated loop of the exact same move. - No overcomplicated choreography that looks stiff or mechanical. - No excessive effects that hide the dancers for long periods. - No muddy colors or desaturated lighting. - No off-model redesigns that break the reference style.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `130.65s`

---

### 🎬 Tiny City Inside Candle Flame
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05284.jpg" width="480" alt="SD2_05284"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/candle-flame-micro-city-SD2_05284">🌐 Watch Online</a>

#### 📝 Prompt
```
Extreme macro shot of a single candle flame burning in a dark room. The background is black, silent, intimate. Wax melts slowly down the candle, forming translucent golden rivers. Opening frame: the camera pushes closer into the flame until the flickering fire fills the entire frame. At the 2-second mark, buildings become visible inside the flame. A tiny city exists within the fire , skyscrapers made of light, streets made of glowing embers, crowds moving like sparks through golden avenues. The camera enters the flame and becomes part of this miniature burning metropolis. Inside, the city is alive and unstable. Towers bend with every flicker. Roads flare and vanish. People made of fire move through the streets, leaving trails of smoke behind them. The sky above is the dark room outside the candle, seen as an infinite black universe. VFX escalation: the candle begins burning faster. Wax rivers flood the city from below like molten glass. Flame-winds tear through streets, reshaping buildings into abstract sculptures of heat and light. Velocity ramp: a burning tower collapses in slow motion, its sparks suspended mid-air like golden snow. Final moment: the camera pulls back out of the flame. The candle is nearly extinguished. Just before the flame dies, the tiny city lights flicker one last time. Macro surrealism, miniature city inside fire, molten wax physics, ember particles, extreme shallow depth of field, dark poetic atmosphere, 4K.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Rooftop Laundry Sunshine
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05283.jpg" width="480" alt="SD2_05283"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rooftop-laundry-sunshine-SD2_05283">🌐 Watch Online</a>

#### 📝 Prompt
```
Main Subject: Young Korean woman, early 20s, oversized t-shirt and shorts, hair in a high messy bun, barefoot on rooftop tiles, cheerful domestic energy. Location: Apartment rooftop clothesline area, sunny midday. Clotheslines with hanging sheets, water tanks, potted herbs in small pots, city rooftops visible in distance. No people in background. Visual Style: Bright realistic domestic documentary tone, breezy and cheerful, strong natural sunlight. Camera Style: Early 2000s handycam, handheld with light natural shake, exposure pumping between shaded and sunny areas, soft grain. No stabilization. Timeline (15 sec, each slot = 2 compressed beats): 00:00–00:03 → She hangs a wet sheet on the line, then smooths out the wrinkles. 00:03–00:06 → She turns to camera saying "오늘 날씨 완전 빨래하기 좋다" ("The weather today is perfect for laundry"), smiling. 00:06–00:09 → She waters a small herb pot nearby, then wipes her hands on her shorts. 00:09–00:12 → A breeze catches the sheets; she laughs, stepping back to watch them billow. 00:12–00:15 → She looks at camera saying "다 끝났다, 이제 쉬어야지" ("All done, now I should rest"), then walks toward the rooftop door as it fades. Audio: Fabric flapping in wind, distant city hum, footsteps on rooftop tiles, faint birds. Her dialogue as noted above. No music. Goal: A cheerful, breezy domestic rooftop moment warm, everyday, real.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Ember Crawling Frayed Cord Macro
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05282.jpg" width="480" alt="SD2_05282"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ember-crawling-cord-macro-SD2_05282">🌐 Watch Online</a>

#### 📝 Prompt
```
Extreme macro on a single ember crawling along a frayed cord against pure black. Frame opens black; at 1 second one ember glows to life, ignites, and travels laterally — slow-motion sparks lifting and dying, a thin spiral of smoke curling, individual carbon fibers glowing white-hot then blackening and folding. Builds to a small bright flare near 12 seconds, settling to a single glowing tip. The ember is the only light source — self-illuminated hot orange against absolute black, hard chiaroscuro. Camera tracks the spark with a tight micro push-in. Color palette: pure black and incandescent orange with a white-hot core — minimal, maximum dynamic range. Audio: low ominous drone, dry crackle and hiss of burning, a single sub-bass pulse.
```

#### 📌 Details
- Ratio: `2.33` | Duration: `15.03s`

---

### 🎬 Ultimate Bungee Jump Thrill
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05281.jpg" width="480" alt="SD2_05281"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/bungee-jump-valley-thrill-SD2_05281">🌐 Watch Online</a>

#### 📝 Prompt
```
Reference image: [MAIN CHARACTER IMAGE user provided] [0:00–0:03] Platform — Confidence Build Main character stands on a high bungee launch platform, harnessed with visible safety gear and a yellow bungee cord attached to the ankles. Two crew members support her/him by the arms, adjusting the harness. Character smiles, points confidently toward the camera, relaxed and excited energy. Camera static, medium shot, slight handheld sway. Clear blue sky and misty mountain valley visible in the background. [0:03–0:05] Countdown — Final Brace Crew steps back slightly. Character shifts weight forward to the edge of the platform, arms loosening, expression shifts from smile to focused determination. Camera holds steady medium-wide shot, slow subtle push-in. [0:05–0:07] The Jump — Free Fall Character leaps forward off the platform into free fall, arms spread wide, body straight and diving forward, hair/clothing whipping upward from the fall speed. Camera follows in a fast drone-style descending tracking shot, staying just behind and above the falling figure. Misty green valley rushing up in the background. [0:07–0:09] Cord Recoil — Inversion Bungee cord reaches full extension and recoils, flipping the character upside down mid-air. Body bounces naturally with cord elasticity, arms and legs reacting to the momentum. Camera holds a steady mid-air tracking shot, slightly below the subject looking up. [0:09–0:11] Aerial Hold — Wide Valley Shot Camera pulls back to a wide aerial shot showing the character suspended upside down on the bungee cord, dangling above a lush green valley with a river/bridge visible far below. Slow gentle swinging motion. Camera holds steady, slow zoom out to reveal full scale of the height and landscape. Camera Techniques: static medium shot → slow push-in → descending drone-tracking shot → mid-air follow shot → wide aerial pull-back Lighting: natural daylight, soft overcast/hazy mountain light, cool-toned atmosphere with slight golden warmth on skin tones Color Grade: natural outdoor grade, slightly enhanced greens and blues, realistic contrast, no heavy stylization Technical Requirements: Maintain exact facial identity, hairstyle, and body proportions from reference image throughout all shots Anatomically accurate limbs and hands during free fall and inversion no distortion, stretching, or fused fingers Realistic harness, cord, and clothing physics natural tension, swing, and recoil behavior No on-screen text, logos, watermarks, subtitles, or UI overlays anywhere in frame Aspect ratio: 9:16 vertical, consistent framing across all shots Smooth camera motion, no motion-blur artifacts or warping during fast tracking shots Consistent lighting and color continuity across all five shots
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.12s`

---

### 🎬 The Flame Chef: Culinary Cinema
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05280.jpg" width="480" alt="SD2_05280"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/flame-chef-culinary-cinema-SD2_05280">🌐 Watch Online</a>

#### 📝 Prompt
```
THE FLAME CHEF - 15 second high-energy cinematic cooking film, 10 rapid scenes, fast rhythmic pacing, whip-pan and speed-ramp transitions between every scene, kinetic kitchen artistry from fresh ingredients to final plated dish. Shot on ARRI Alexa 35, 35mm lens, natural film grain, rich warm color grade with deep shadows and golden highlights, professional food cinematography, photorealistic, not CGI. Dark moody restaurant kitchen, dramatic overhead lighting, steam and warm glow. SCENE 1 (0-1.5s): Chef's hand places a cast iron pan onto a glowing gas burner with confident energy, blue flame rising around the edges, quick real time then micro slow motion on the flame glow, hard whip-pan into locked close-up. SCENE 2 (1.5-3s): Rapid skilled vegetable prep, knife rocking smoothly through fresh herbs and bell peppers in rhythmic motion, hyper-fast real time with hands in controlled motion, one pepper slice spinning in brief slow motion, top-down locked shot. SCENE 3 (3-4.5s): Butter cube tossed gracefully through the air landing in the warm pan, melting instantly into golden foam and swirl, slow motion flight with speed ramp to real time on the sizzle, side macro tracking the arc. SCENE 4 (4.5-6s): Chef flips the pan, vegetables rising upward in a golden arc, warm flame glow beneath, tiny seasoning embers drifting, speed ramp from real time flip into dramatic slow motion at the peak of the toss, low hero angle. SCENE 5 (6-7.5s): Extreme macro, garlic and chili meeting hot oil, lively golden bubbles, steam rising in a soft backlit plume, 120fps slow motion with every bubble crisp, probe lens push-in through the steam. SCENE 6 (7.5-9s): Chef seasoning from height with flowing hand movement, salt crystals raining down in slow motion through a shaft of overhead light catching like snow, slow motion rain against fast hand movement, side close-up with shallow focus on the crystals. SCENE 7 (9-10.5s): Sauce poured from a steel pan in a glossy ribbon coating the dish in one continuous silky wave, steam curling, silky hypnotic slow motion, orbiting macro around the pour. SCENE 8 (10.5-12s): Fresh herbs dropped from above, leaves tumbling in slow motion landing perfectly on the glistening dish, tiny sparkle of sauce, slow motion fall with real time landing, top-down locked shot. SCENE 9 (12-13.5s): Chef wipes the plate rim in one confident swift motion and spins the plate a quarter turn, steam rising through dramatic side light, fast confident real time, close-up tracking the hand with whip-pan on the spin. SCENE 10 (13.5-15s): Final hero shot, finished dish center frame under a single overhead spotlight, steam rising in elegant curls, background fading to darkness, chef's silhouette stepping back with sati
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.2s`

---

### 🎬 Neon Night Drift: Integra
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05279.jpg" width="480" alt="SD2_05279"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/neon-night-drift-integra-SD2_05279">🌐 Watch Online</a>

#### 📝 Prompt
```
GLOBAL STYLE: Stylized 3D animation, cel shaded graphics, comic book rendering, Spider Verse inspired visual style, vibrant high contrast color palette, fluid dynamic motion, Unreal Engine 5 aesthetic, cinematic lighting, 4K quality. CHARACTER CONTINUITY: Stylized young male driver with wavy blonde hair, thick black glasses, short goatee, intricate black tattoo sleeves on both arms, black shirt, dark pants, brown loafers. VEHICLE CONTINUITY: Modified white 1990s Honda Integra, black brush stroke "46" side decal, glowing red underglow, deep dish rims, lowered stance, clean body kit. Keep the same car throughout. No logos or text changes. ENVIRONMENT: Neon lit New York inspired streets beneath elevated subway tracks at dusk, wet reflective asphalt, glowing storefronts, cinematic atmosphere. SEQUENCE: 0:00–0:05 Low angle tracking shot follows the driver walking confidently toward the parked white Honda Integra. The glowing red underglow reflects across the wet pavement. Close up of the tattooed hand pulling the door handle, entering the car, then turning the ignition key. Smooth cinematic transitions. 0:05–0:08 Macro shot of the exhaust pipe blasting thick stylized gray smoke. Quick cut to tattooed hands gripping the steering wheel tightly. Dashboard lights illuminate the driver's focused face. 0:08–0:11 Dashcam POV as the Integra rapidly accelerates beneath elevated train tracks. Neon storefronts streak past with heavy motion blur. Camera shakes naturally with speed. 0:11–0:15 Extreme close up of the driver's determined eyes reflected in the rearview mirror. Hard cut to an aggressive drift around a city corner. Thick tire smoke, glowing orange sparks from the wheels, vivid red underglow reflecting on the wet road. End with a cinematic action shoT
```

#### 📌 Details
- Ratio: `0.74` | Duration: `15.08s`

---

<!-- STATS_END -->
