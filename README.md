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
- Total Prompts: **8607**
- Updated Today (UTC 2026-08-05): **0**

## 🎬 Today's Updates
### 🎬 Cinematic Hanfu Transition Showcase
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11132.jpg" width="480" alt="SD2_11132"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-hanfu-transition-SD2_11132">🌐 Watch Online</a>

#### 📝 Prompt
```
【Overall Style】 Cinematic realism with an ancient Chinese aesthetic, employing authentic Tang, Song, and Ming dynasty Hanfu (traditional Han clothing) language. Emphasis is placed on believable fabric textures, natural indoor sunlight, restrained and understated classical elegance, realistic skin texture, and the absence of beauty filters. All costume changes are achieved through realistic mirroring, without the use of magical CG. 【Character Design】 Character ID｜HANFU-01 A 23-28 year old East Asian woman with an oval face, warm ivory skin, dark brown almond eyes, long black hair reaching her waist, styled in a half-updo with a thin braid, and a slender, well-proportioned figure. 【Styling】 Style 1: From embroidered cloth shoes to a light jade-colored pleated horse-face skirt, ivory-white cross-collar top, deep red woven belt, pearl hairpin, and small jade pendant, all are fully presented. Style 2: Blue Song dynasty-style beizi (a type of jacket). Style 3: Black and red Ming dynasty flying fish robe. Style 4: Platinum-colored Tang dynasty ruqun (a type of traditional Chinese dress). Style 5: Dark green horse-face skirt and brocade short jacket. Style 6: Moon-white embroidered Hanfu. Outfit 7: Deep crimson wedding dress embroidered with golden phoenixes. [Scene Setting] A quiet wooden hall with a background featuring latticed windows, a bronze incense burner, a low table, draped curtains, floating dust, and cool morning sidelight. [Shot 1 \| 0-5s \| Panoramic] Character ID: HANFU-01, the same 23-28 year old East Asian woman, oval face, warm ivory skin, dark brown almond eyes, long black hair reaching her waist, half-tied with a thin braid, slender and well-proportioned figure; Outfit 1 is fully presented, from embroidered cloth shoes to a light jade-colored pleated skirt, ivory-white cross-collar top, deep red woven belt, pearl hairpin, and small jade pendant. She stands in the quiet wooden hall, with a background featuring latticed windows, a bronze incense burner, a low table, draped curtains, floating dust, and cool morning sidelight; low camera position, 24mm lens, slow panning. She raises one knee, sweeping the entire hem of her skirt across the camera until the silk fills 100% of the frame. Within this complete obscuring effect, the camera abruptly cuts to Style 2: a blue Song Dynasty-style jacket, then to Style 3: a black and red Ming Dynasty flying fish robe. Each transition maintains the same leg, direction, speed, continuous center of gravity, face, hairstyle, jewelry, and background. [Shot 2 \| 5-10s \| Cowboy Scene] The same woman, in the same wooden hall, now wearing Style 4: a white and gold Tang Dynasty-style ruqun (a type of traditional Chinese dress). She twists her hips, glances at the camera, revealing a restrained yet playful smile, and then quickly opens a round silk fan. After the fan completely obscures the camera for 3-5 frames, the same woman appears wearing Style 5: a dark green horse-face skirt and brocade short jacket. She continues with the exact same wrist movement, spinning once in place, then uses her extra-long water sleeves to sweep horizontally across the frame, creating a rapid panning shot. Within this complete obscuring effect, the camera switches to Style 6: a moon-white embroidered Hanfu, with the same wooden hall as before. [Shot 3 \| 10-15s \| Close-up] The same woman, dressed in a moon-white Hanfu, maintains the same jade pendant and pearl hairpin. A 50mm lens is used, with a steady gaze and a slight handheld breathing feel. A semi-transparent red veil slowly rises, completely obscuring the lens before falling back down, revealing a deep crimson wedding dress embroidered with golden phoenixes (Shot 7). Her deep brown eyes remain centered, with clearly defined eyelashes and visible pores. A slight upturn at the corners of her mouth and a highlight of tears on her lower eyelid are visible. Cigarette smoke floats slowly in the background. The ending focuses slowly on her eyes, which are looking directly at the camera, shifting from her golden hair ornaments. [Technical Requirements] 15 seconds, 9:16 portrait mode, 30fps. Realistic continuous autofocus hesitation when the lens is 100% obscured, natural motion blur, fabric inertia, silk sheen, embroidery thickness, slight fabric rubbing sounds, fan popping sounds, and wind-blown sleeve sounds are required. All hard cuts must occur only when the lens is 100% obscured. The entire film must be free of dialogue, subtitles, logos, or watermarks. [Negative words] blurry, bad quality, low quality, low resolution, noisy, jpeg artifacts, watermark, text, error; deformed, mutated, bad anatomy, poorly drawn hands, bad composition, out of frame, disfigured; inconsistent character, changing clothes, face morphing, background shift, glitching cuts, disappearing props
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.13s`

---

### 🎬 Stylish Office Fashion Transformation Video
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11131.jpg" width="480" alt="SD2_11131"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/office-fashion-transformation-SD2_11131">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 30 second photorealistic fashion transformation video in a 16:9 landscape frame. A stylish young woman with long softly waved brown hair, warm medium skin, round black glasses, small earrings, natural makeup, and consistent facial features stands in the same modern office washroom or dressing area for the entire video. The background has large charcoal gray stone tiles, a pale ceiling, a slim black wall rail on the left, and a narrow metal partition line on the right. Keep every architectural line perfectly fixed across all cuts. Camera is locked on a tripod at eye level, medium full shot from mid thigh upward, using a natural 35 mm equivalent smartphone lens. The subject remains centered with enough space on both sides for the landscape composition. No camera shake, zoom, reframing, or perspective change. Use crisp realistic detail, true skin texture, fine hair strands, believable fabric folds, accurate hands, subtle breathing, and tiny posture adjustments. Lighting is soft cool overhead office lighting with gentle facial fill, mild reflections on the gray tiles, consistent exposure, and realistic shadow direction. Begin with her palm very close to the lens, briefly obscuring most of the frame. She pulls her hand away and reveals the first outfit, a sleeveless pale blue floral office dress with a light scarf over one shoulder. She looks calmly into the camera, lowers her arm, places one hand on her hip, glances upward with a mildly unimpressed expression, then folds her arms. Match this exact folded arm pose for the first invisible jump cut. Across the next twenty four seconds, reveal nine distinct office outfits through clean pose matched cuts timed to the music. Use a lemon yellow floral kimono blouse, a relaxed ivory button shirt with navy trousers, a fitted black sleeveless top with dark tailored pants and a brown belt, a soft blush pink top with black trousers, a deep green crew neck blouse, a vivid blue paisley shift dress, a black and white dotted peplum blouse, a camel blazer over a cream top, and a final elegant burgundy wrap dress. Between changes, give her natural confident gestures such as a small shoulder bounce, two thumbs up, hands settling on hips, crossing her arms, turning her chin, smoothing a cuff, lightly flicking her hair, pointing toward her cheek, and smiling directly at camera. Each gesture should begin in one outfit and end in the next so the cut feels practical and intentional, never like body morphing. Hold each look long enough to read clearly, roughly two seconds per outfit, with cuts landing on strong beats. Preserve identical body position, hair direction, glasses placement, limb anatomy, background geometry, and lighting at every transition. Avoid warped fingers, changing facial identity, floating clothing, cloth melting, duplicated accessories, sudden camera motion, or artificial beauty smoothing.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.05s`

---

### 🎬 Real Bali Vacation Handheld Footage
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11129.jpg" width="480" alt="SD2_11129"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/real-bali-vacation-handheld-SD2_11129">🌐 Watch Online</a>

#### 📝 Prompt
```
A real person on a real Bali vacation, Not AI generated. Not a commercial. Not a photoshot. Real human skin texture – pores visible, natural, flush, slight shine in heat, no plastic smooth AI skin, no perfect flawless filter look, slight sweat glow in outdoor scenes, natural imperfections welcome. Handheld phone camera throughout – slight natural shake and sway, imperfect framing – slightly off-center, tilted, natural motion blur when moving horizon, cut off edges, inconsistent exposure – slightly overexposed, outdoors, warmer indoors. Occasional slight focus pull or soft focus, 26mm iPhone lens distortion, no gimbal stabilization – raw handheld feel, no drone shots, no professional angles. 100% natural ambient light only, morning scenes – soft warm golden light through curtains
```

#### 📌 Details
- Ratio: `0.68` | Duration: `15.19s`

---

### 🎬 One Shot Planetary Disaster Escape
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11125.jpg" width="480" alt="SD2_11125"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/one-shot-planetary-disaster-escape-SD2_11125">🌐 Watch Online</a>

#### 📝 Prompt
```
A single uninterrupted cinematic action sequence. No cuts. No scene transitions. One continuous camera movement from beginning to end. The film opens from orbit above a breathtaking Earth-like planet. Suddenly, a massive crack of glowing magma races across an entire continent, splitting the surface apart. The camera immediately dives through the atmosphere at incredible speed toward the source of the catastrophe. The camera levels out just behind a lone explorer wearing a sleek advanced survival suit, sprinting across a rocky plateau. The ground shakes violently with every step. Deep fractures spread beneath their feet, glowing with molten lava. Behind the explorer, an entire mountain range collapses in slow waves of dust and rock. Giant boulders crash into the valley while volcanic ash fills the sky. The explorer leaps across a widening chasm only moments before the bridge of stone collapses into a river of lava. The camera follows the jump seamlessly, passing through flying debris without slowing. A volcanic eruption explodes ahead. A towering column of fire and ash blasts into the atmosphere. Flaming rocks rain down across the landscape. The explorer slides beneath a falling rock arch as molten fragments scatter around them. The camera continues tracking just behind. Without warning, a wall of water hundreds of meters high appears on the horizon. An entire ocean has been displaced. The tsunami races across the collapsing land at terrifying speed. The explorer accelerates toward a series of towering rock pillars rising from the valley floor. Using a compact grappling launcher, they swing across one collapsing pillar after another while the giant wave destroys everything behind them. The camera swings naturally with every movement, maintaining one fluid motion. Meteor fragments now begin entering the atmosphere. Several impact nearby. Each impact creates expanding shockwaves that throw dust, fire, and debris high into the sky. One enormous meteor crashes directly ahead. The explorer dives through the expanding dust cloud as molten fragments fly past the camera. Beyond the smoke, an emergency launch platform rises automatically from beneath the ground. A sleek escape spacecraft powers up. The explorer sprints across the final collapsing bridge. The bridge disintegrates beneath every footstep. At the last possible moment, they leap directly into the open spacecraft. The hatch seals instantly. The engines ignite. The spacecraft launches vertically just as the launch platform is swallowed by lava. The camera follows alongside the accelerating spacecraft as it blasts through volcanic ash, thunderclouds, and meteor storms before breaking into the silence
```

#### 📌 Details
- Ratio: `0.56` | Duration: `10.12s`

---

### 🎬 Kyoto Teen Spring 1987 VHS
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11123.jpg" width="480" alt="SD2_11123"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/kyoto-teen-spring-1987-SD2_11123">🌐 Watch Online</a>

#### 📝 Prompt
```
Teenage boy in Kyoto — Spring 1987 Character Japanese high-school student, 17 years old. Slim build. Short neatly cut black hair. Navy gakuran school uniform with brass buttons, white shirt slightly untucked, worn black leather school shoes, canvas school bag hanging from one shoulder. Curious, energetic but reserved. Consistent identity, clothing and appearance. Location Kyoto, Japan, spring 1987. Quiet residential streets lined with traditional machiya houses mixed with small concrete apartment buildings. Cherry blossoms beginning to fall. Narrow canals beside sidewalks. Utility poles crowded with cables. Small neighborhood shrines. Bicycle parking areas overflowing after school. Drink vending machines glowing beneath trees. Visual Style Ultra-realistic, candid, unscripted. Delicate pastel spring colors. Warm afternoon sunlight filtered through cherry blossoms. Authentic neighborhood textures. Everyday life only. 24fps. Camera Style Teenage friend filming with an early VHS camcorder while walking home from school. Casual handheld movement. Framing often imperfect. Frequent autofocus breathing. Slight overexposure beneath bright blossoms. Consumer video softness throughout. 00:00–00:02 Stops beneath a vending machine deciding between two canned drinks. Changes his mind twice before finally pressing one button. 00:02–00:05 Opens the can immediately, but it’s warmer than expected. Makes a slightly disappointed face before taking another sip anyway. 00:05–00:07 Walking beside a canal. Cherry blossom petals land on his shoulder. He doesn’t notice until another student points at them. 00:07–00:10 Pauses beside his parked bicycle. Pumps the front tire with his thumb, deciding it’s good enough without actually inflating it. 00:10–00:13 Waits politely at a railway crossing. Watches the passing train instead of looking at the camera. 00:13–00:15 Rides slowly away beneath falling blossoms. One hand briefly leaves the handlebars to catch a petal before he loses it in the breeze. Audio Passing bicycles, distant train crossing bells, birds, vending machine hum, schoolchildren talking quietly, bicycle tires on pavement, spring wind. No music.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.04s`

---

### 🎬 Casual Office Birthday Celebration Footage
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11121.jpg" width="480" alt="SD2_11121"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/casual-office-birthday-celebration-SD2_11121">🌐 Watch Online</a>

#### 📝 Prompt
```
Super casual real smartphone home video footage, casual office celebration in a decorated break room, natural mobile phone camera with slight authentic handheld shake, normal frame rate with smooth normal motion, rapidfire montage with quick jump cuts every 1-2 seconds like scrolling through phone memories, unpolished authentic phone recording of colleagues cutting cake, clapping and chatting, pure raw home video feel, no cinematic polish. Use the provided reference photo as the strict ONLY visual reference for the main woman. Maintain her exact appearance with zero deviation. Generate a mixed group of colleagues of all ages around her in the office break room, balloons and a small cake visible. 0-2.5s: Shaky rapid cuts — main woman laughing near the decorated table, balloons in the background, quick flashes of colleagues clapping. 2.5-5s: Abrupt jump cuts — close-up of her smiling while cutting the cake, then colleagues passing cake slices around. 5-7.5s: Fast shaky — she chats animatedly with coworkers, casual office attire, laughter visible. 7.5-10s: Quick cut close-up — warm smile toward camera, then jump to her laughing with a senior colleague nearby. 10-12.5s: Abrupt edit — group gathered around the table, casual toast with paper cups, mixed ages chatting. 12.5-15s: Final rapid transition — main woman relaxed among colleagues, soft smile, calm office memory ending with slight natural phone sway. Natural smartphone video quality, slight real handheld shake, smooth normal frame rate motion, authentic casual physics, stable main character consistency, no pro stabilization or effects.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 Retro 80s Sci-Fi Comedy Scene
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11119.jpg" width="480" alt="SD2_11119"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/retro-80s-sci-fi-comedy-SD2_11119">🌐 Watch Online</a>

#### 📝 Prompt
```
Use the supplied image1 as the exact first frame of the video. Maintain perfect visual continuity with the reference image. Preserve the exact young woman, the exact robot soldier, the industrial facility, wardrobe, proportions, facial identity, robot construction, lighting, color palette, camera perspective, and environment. No redesigns or substitutions. Style: Authentic late-1980s live-action sci-fi comedy filmed on 35mm Kodak motion picture film. Practical sets only. Full-size practical mechanical robot suit with visible hydraulic joints and realistic mechanical weight. Warm tungsten industrial lighting, subtle atmospheric steam, soft halation, natural film grain, slight gate weave, vintage telecine color, practical smoke, cinematic depth of field. Scene: The woman and the robot casually walk side by side through the industrial facility. Their pace is relaxed and natural. The robot moves with heavy hydraulic weight, subtle servo corrections, piston movement, and believable mechanical inertia. The woman walks confidently while casually talking, occasionally looking up at the robot, smiling, and using expressive hand gestures. Their interaction feels friendly and comedic rather than exaggerated. Camera: Continuous cinematic tracking shot. Medium two-shot transitioning into a smooth side tracking shot. Steady dolly movement only. No handheld shake. No whip pans. No sudden zooms. No jump cuts. Maintain eye-level framing throughout. Background: Industrial pipes, catwalks, warm practical lights, drifting steam, distant workers performing routine tasks without interacting with the main characters. Background remains secondary and never distracts from the conversation. Timeline 0:00–0:04 Medium two-shot. The woman and robot begin walking together. The woman glances at the robot with a playful smile and says in a cheerful 1980s California accent: WOMAN: "I'm seriously jealous of all the FLUX 3 cool kids." Natural conversational lip sync. 0:04–0:10 Smooth side-tracking shot as they continue walking past pipes and drifting steam. The woman becomes more animated, making larger but natural arm gestures while speaking: WOMAN: "Their UNHINGED FLUX 3 videos have been everywhere all weekend!" Maintain realistic walking speed and synchronized body movement. 0:10–0:13 Natural push-in to a close-up of the robot. The robot slowly turns its head toward her with believable hydraulic motion and a soft mechanical servo whir. Its eye panel briefly flickers before speaking in a dry synthesized voice: ROBOT: "I know, right?" The woman smiles slightly after hearing the response. Audio: Light retro synth comedy soundtrack. Subtle hydraulic footsteps. Servo motors. Industrial ambience. Distant machinery. Soft steam vents. Perfect dialogue clarity. Accurate natural lip synchronization. Performance: Relaxed comedic timing. Natural facial expressions.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Giant Hands Barbie Doll Styling
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11114.jpg" width="480" alt="SD2_11114"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/giant-hands-barbie-styling-SD2_11114">🌐 Watch Online</a>

#### 📝 Prompt
```
[Style] Giant Hands Barbie Doll Styling (GWRM · Giant Hands Barbie Doll Styling), realistic vertical screen mobile phone shot with high-quality feel (9:16 Vertical). Photorealistic), Instagram-worthy pink and girly style, natural home lighting. [Duration] 15 seconds. [Scene] Real home living room: light-colored wooden floor, white wardrobe, TV mounted on the wall, natural window light streaming in from the side; the female lead stands on the floor in the size of a real-life Barbie doll, with a hand reaching in from off-screen larger than her entire body. [Character] Female lead @Image 1 (a real person shrunk to doll proportions, maintaining a realistic face and body, with slightly stiff and abrupt movements reminiscent of a doll). [Core Mechanism] Proportion difference: A pair of enormous hands (normal human hands, like giants relative to the female lead) repeatedly reach into the frame from off-screen to change her clothes—pinch, put down, remove, put on, squat to change shoes; the female lead cooperates throughout but maintains a doll-like obedient posture, her body swaying slightly when manipulated. [Permanent Subtitles] Pink handwritten cursive English title &quot;GWRM&quot; at the top of the screen, and smaller text below: &quot;Styled by Giant Hands Like a Barbie&quot;. &quot;Doll&quot;, decorated with a pink bow and stars

[00:00-00:02] Opening: Putting the doll down
A giant hand pinches the female lead&#39;s waist and lifts her from outside the frame, gently placing her on the wooden floor to stand steadily. She is wearing a pink plaid nightgown, a white tank top, white lace shorts, and white socks, with a pink sleep mask on her head. Her feet wobbled slightly when they landed before she stood still.

[00:02-00:05] Step 1: Removing the eye mask and taking off the coat
A giant hand pinches the pink eye mask on her head with two fingers and pulls it up; then, both hands pinch the two cuffs of the pink plaid coat and pull the entire coat off her body, lifting it out of the frame. She is left with only a white tank top and lace shorts, and raises her hand to rub her eyes. [00:05-00:08] Step Two: Skincare Close-up Cut to close-up: A huge finger dipped in milky white face cream gently spread it on her cheek. She obediently closed her eyes and tilted her head back. Then, a finger held up a small pink mirror and handed it to her. She opened her eyes, looked in the mirror, pursed her lips, and adjusted her bangs. [00:08-00:11] Step Three: Dress Up Cut back to wide shot: A huge hand held a green ruffled strapless top and pulled it over her head, straightening the hem. Then, a pink and white checkered mini skirt was taken and lifted from her feet up to her waist, smoothing out the wrinkles. She cooperated by raising her arms and then lowering them. [00:11-00:13.5] Step 4: Changing Shoes &amp; Socks Low-angle close-up: A giant hand pinches pink lace stockings and pulls them onto her legs one by one, up to her knees; then a pair of fuchsia pointed high heels are placed beside her feet, and her ankles are pinched and the heels are inserted one by one, with fingertips adjusting the heels to ensure stability. [00:13.5-00:15] Final Pose: The giant hand exits the frame, leaving the female lead standing alone in the center of the floor, hands on her hips, posing with a twist of her hips. She then turns around, flicks her hair, and smiles at the camera with a tilted head. The image freezes on her entire outfit. [Sound Effects] The soundtrack features a light and sweet Instagram-worthy background music track. Sounds like rustling clothes, the click of heels hitting the ground, and the subtle sound of fingers applying face cream are all faithfully reproduced. Each outfit change is accompanied by a soft &quot;ding,&quot; and the ending is accompanied by a rising note.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.13s`

---

### 🎬 Sword Immortal Vs Chili Jar
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11113.jpg" width="480" alt="SD2_11113"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sword-immortal-chili-jar-SD2_11113">🌐 Watch Online</a>

#### 📝 Prompt
```
[Generation Mode] Seedance 2.0 Fast [Video Specifications] Strictly generate 15-second video, 16:9 landscape mode, and three clean shots. [Overall Style] A restrained daily comedy with cinematic realism and texture, featuring elegant xianxia visual language, precise silent film reaction rhythms, warm kitchen lighting, and tactile glass and metal materials; The jokes follow a single and clear chain of cause and effect: overwhelming supernatural forces ultimately lose to simple everyday wisdom. [Characters] Character A \| Sword Immortal Sister Using @图片1 as character A Sword Immortal Sister's strict identity and clothing reference: the same 25–30 years old East Asian woman, fully maintaining the same face as in the reference image, oval facial structure, sharp dark brown eyes, naturally fair skin, long straight black hair, tall and slender figure, jade hairpin, silver waist accessory, white embroidered silk Hanfu, semi-transparent layered wide sleeves, flowing long skirt, and white cloth boots. Character B \| Bicycle Sister Using @图片2 as character B Biker's strict identity and clothing reference: the same 25–30 years old East Asian woman fully retaining the same face in the reference photo, brown short ponytail, rounded and expressive features, yellow jacket, blue jeans, white sneakers, and small silver earrings. [Core Items] A tightly screwed glass chili sauce jar, the same metal lid, the same metal spoon, and seven pocket-sized silver flying swords. [Lens 1 \| 0-5s \| Low-angle panoramic slow rail push] 16:9 landscape screen, modern residential kitchen at night, warm-colored chandeliers, dark rain curtains outside the window, wooden countertops, ceramic bowls, metal spoons, cutting boards, vegetables all clearly visible, and a tightly tightened glass chili sauce jar placed in the center of the frame, like an ancient treasure forbidden to open. The same bike girl pushed the can in front of the same sword fairy sister and said, "Sister, help me drive it." ” Sword Immortal Sister examined the jar seriously, lifted her chin lightly, and calmly replied, "A mere seal." ” [Lens 2 \| 5-10s \| Denim Scene within Scene] The same Sword Immortal Sister, dressed in a white embroidered silk Hanfu, formed a precise double-finger spell; Seven miniature silver flying swords appeared simultaneously, rotating around the same glass jar and striking the same metal jar lid in a synchronized rhythm. Her long hair and wide sleeves fluttered dramatically, the ceramic bowl trembled slightly, the chandelier on top swayed from side to side, the heroic drumbeat gradually intensified, but the jar lid remained completely still. She quietly increased her strength, yet still forced herself to maintain a calm expression; The background always maintains the same kitchen and the same counter. [Shot 3 \| 10-15s \| Close-up to Extreme Close-up] The same cyclist casually picked up the same metal spoon and tapped the edge of the can's lid, causing a faint vacuum to immediately make a soft squeak from inside. She easily unscrewed open the lid and said, "It's not a seal, it's negative pressure." ” The seven flying swords simultaneously lowered their tips in shame. Close-up: The same Sword Immortal sister's eyelid twitches slightly; She slowly clasped her hands behind her back and said calmly, "I've long known this technique." ” The scene freezes on the moment Bike Sister silently gazes at her. [Technical Requirements] Strictly 15-second videos must be generated using Seedance 2.0. Three clean shots, 16:9 landscape mode, stable character identity and costumes, glass jars, metal lids, spoons, hair, silk fabrics, vibration, and lighting physics effects are realistic, native synchronized Mandarin dialogue and action sound effects, no subtitles generated.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Alien Pilot Escapes Crashed UFO
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11106.jpg" width="480" alt="SD2_11106"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alien-pilot-ufo-crash-escape-SD2_11106">🌐 Watch Online</a>

#### 📝 Prompt
```
Hyper-realistic cinematic sci-fi action sequence, 15 seconds, aspect ratio 16:9. Night in a dark dense forest. One damaged UFO crashes through the trees and slams into the ground. One alien pilot only. The alien pilot is injured but conscious and must escape the wreck before the ship explodes. The environment is simple and clear: tall trees, mud, broken branches, smoke, fire, flashing ship lights, and sweeping military searchlights moving between the trunks from somewhere deeper in the forest. The action starts with the UFO tearing through the trees and crashing hard into the forest floor. Dirt, sparks, and broken wood explode outward. The saucer skids to a stop at an angle, half-buried in mud, with one side glowing and pulsing dangerously. A hatch blows open and the alien pilot crawls out of the wreck, weak and unsteady. Behind the alien, the damaged UFO starts exploding in pulses, not one giant explosion, but repeated bursts of fire, sparks, and pressure from inside the hull. Each pulse throws debris outward and lights up the forest. The alien tries to move into the trees, but military searchlights begin sweeping through the forest and pass across the wreck. The alien ducks behind a fallen log or tree root as another explosion pulse hits the ship and a burning panel blasts into the woods nearby. The searchlights keep moving closer through the smoke. Near the end, the UFO gives off a stronger pulse and starts breaking apart. The alien makes one desperate move, limps or stumbles deeper into the forest, and disappears behind thicker trees just as the ship erupts in a larger final blast that lights the whole forest white for a moment. End with the alien hidden in the darkness between the trees while the wreck burns behind and searchlights continue sweeping through the smoke. Style: hyper-realistic, cinematic, dark, intense, clear readable action, one alien pilot only, one crashed UFO only, one forest only, one clear goal, crashing ship, pulsing explosions, smoke, fire, broken trees, sweeping military searchlights, no extra soldiers on screen, no space battle, no text, no logos, no cartoon style, no slow motion, no famous celebrity faces, no recognizable actors, no movie-star resemblance, no public-figure likenesses. Keep proportions. Keep style and features. Aspect ratio 16:9.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Armored Hot Rod Wasteland Ambush Escape
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11104.jpg" width="480" alt="SD2_11104"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/inferno-hotrod-ambush-SD2_11104">🌐 Watch Online</a>

#### 📝 Prompt
```
Inferno Hot-Rod Ambush Hyper-realistic cinematic action sequence, 15 seconds, aspect ratio 16:9. One futuristic armored hot-rod is the main subject. It is ultra pimped out, low and aggressive, with heavy plated bodywork, hidden weapon mounts, integrated twin gun turrets, side-mounted machine guns, exposed pistons, heat vents, exhaust stacks, riveted metal panels, enclosed cockpit with bulletproof canopy glass, flame decals, and deep orange, red, matte black, and white markings. The setting is a bleak fiery wasteland with cracked lava ground, ruined industrial structures, dust, smoke, and a stormy orange-red sky. The goal is simple: the hot-rod must blast through a deadly ambush and escape the collapsing road. The action starts with the hot-rod roaring across the lava-cracked wasteland at high speed, tires throwing sparks and dust. Heat shimmer rises from the ground. As it races past the ruins of an old industrial refinery, a hidden mechanical roadblock suddenly erupts out of the ground ahead, and automated gun towers unfold from the wreckage on both sides. The hot-rod swerves hard into a violent powerslide as the first shots tear across the road. Hidden twin gun turrets rise from the bodywork and fire back. Side-mounted machine guns erupt in short bursts, blasting one gun tower apart in sparks and metal. The car straightens, rockets forward, then the lava-cracked road begins splitting open in front of it. Now the set piece escalates. A huge slab of roadway collapses into a glowing lava fissure. The hot-rod hits full throttle, jumps the broken section, lands hard, and smashes through the mechanical roadblock while fire, debris, and broken metal explode around it. One side panel scrapes sparks off the wreckage, but the car keeps charging forward. At the end, the hot-rod bursts clear of the ambush zone and powers through smoke and ember glow while the ruined refinery behind erupts in secondary explosions and the cracked lava road continues collapsing. Style: hyper-realistic, cinematic, intense, aggressive, dark and moody, award-winning automotive editorial feel, dramatic three-quarter low-angle energy, clear readable action, one hero vehicle only, no extra hero cars, the hot-rod must remain the star, sleek armored dieselpunk military engineering, flaming wasteland atmosphere, smoke, embers, heavy shadows, subtle reflections on dusty or heated surfaces, no text, no logos, no cartoon style, no slow motion, no famous driver face, no celebrity resemblance. Keep proportions. Keep style and features. Aspect ratio 16:9.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

### 🎬 Rainy Tokyo Violin Street Performance
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11102.jpg" width="480" alt="SD2_11102"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rainy-tokyo-violin-performance-SD2_11102">🌐 Watch Online</a>

#### 📝 Prompt
```
A 15-second continuous one-take cinematic shot of a young female street musician in a rainy neon-lit Tokyo alley at night. She starts playing a violin under a flickering neon sign, raindrops bouncing off the strings; then she walks toward the camera while continuing to play, passes a group of curious passersby who stop to listen, and ends by looking directly into the lens with a hopeful smile as the rain intensifies. Soft warm key light on her face, cool blue ambient neon reflections on wet pavement, realistic water physics, subtle camera gimbal tracking forward, natural ambient rain and violin audio synchronized. High detail skin and fabric, 4K cinematic look.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

### 🎬 Playful Peephole Doorway Knocking POV
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11099.jpg" width="480" alt="SD2_11099"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/peephole-doorway-knock-SD2_11099">🌐 Watch Online</a>

#### 📝 Prompt
```
A realistic doorway peephole POV video shot through a ultra wide fisheye lens with a pronounced circular black vignette and curved distortion. The scene takes place in a warmly lit, carpeted apartment hallway with dark doors and warm sconce lights running along the walls. A cheerful young woman with short, bleached blonde pixie cut hair, wearing a casual layered outfit, approaches the camera close up, leaning in and playfully knocking on the lens as if knocking on a door. She holds a large fresh bouquet of white daisies and eucalyptus. She smiles brightly, applies lip balm while looking into the camera, spins around happily, and runs off down the corridor. Next, she returns wearing an oversized cream-colored trench coat carrying a small red gift bag, knocks again, poses, turns, and playfully darts away down the hallway before running back toward the door. Finally, she returns wearing a warm brown sweater, holding a frosted red velvet cake on a glass plate. She knocks on the camera lens, licks frosting off her finger, smiles, blows a kiss directly to the camera lens, and runs off giggling. Natural handheld instability, realistic indoor lighting, handheld camera movement, high definition organic video quality, upbeat indie pop background soundtrack. Aspect ratio 16:9, total duration 20 seconds.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `20.03s`

---

### 🎬 Futuristic Robot Arena Battle
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11097.jpg" width="480" alt="SD2_11097"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/futuristic-robot-arena-battle-SD2_11097">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-realistic futuristic colosseum packed with roaring crowds. Two massive combat robots circle in the sand arena, armor torn open and sparking. One drives the other into the wall, collapsing stone columns. Camera spins low around their feet as debris flies. Final frame: victorious robot raises burning fist under stadium lights.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 China Weapon Evolution Through Ages
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11091.jpg" width="480" alt="SD2_11091"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/china-weapon-evolution-SD2_11091">🌐 Watch Online</a>

#### 📝 Prompt
```
[Realistic Prefix] Ultra-realistic epic film footage, 21:9 ultra-wide screen, showing China's weapon-throwing, firearms, and flight technology evolving from ancient times to the interstellar age. The entire segment uses controlled multi-camera matching editing, with each switch maintaining the center, contour direction, rotation angle, speed of movement, and continuous overall momentum of the flying subject. Low saturation, high contrast, realistic materials, natural motion blur. Flying objects remain sharp and sharp, while the background becomes deep and blurred due to high-speed movement. The historical environment has evolved from a desolate ancient plain to Shang and Zhou, Qin and Han, Song Dynasty, Ming Dynasty, modern valleys, near-Earth orbit, and future deep space. Chinese cultural elements naturally appear with the times, without using textual introductions. [Full Movie] The first scene already features a young ancient Chinese maid Clothing HKb7_rmbMAARNAP Standing on the right side of the desolate plain, the body faces to the left side of the image. Her features are delicate and clear, with low mountains, dry grass, exposed rocks, and gray-blue clouds in the distance. The heroine's expression was fierce: her right foot firmly planted on the ground, her left foot steady forward, waist twisted backward, and her shoulder drove her right arm, using all her strength to forcefully throw a rough, gray stone toward the left side of the frame. The ends of the hair, hem, and waist strap are swayed outward by the inertia of turning. The camera immediately caught up with the flying rocks. The stone blocks are located at the center of the image, occupying about one-third of the image's height, moving at high speed while rotating irregularly. The camera and rocks kept about a meter apart in synchronized flight, the wilderness in the background rapidly receded, and the heroine quickly shrank in the shallow depth of field. MATCH CUT。 The moment the stone is rotated to the same angle, it becomes a primal stone hammer: gray blunt stone is tightly bound to the tip of the wooden handle by coarse plant fibers. The hammer maintains exactly the same center position, flight direction, and rotation speed, while the wooden handle produces natural trailing effects due to high-speed rotation. The background features ancient tribes, wooden fences, fur tents, and sparse fires. MATCH CUT。 The stone hammer was transformed into a bronze spear from the Shang and Zhou dynasties. The spearhead has a heavy bronze texture, cast texture, and natural oxidation spots, while the wooden shaft continues to fly at high speed along the same trajectory. The setting is upgraded to a dusty early ancient battlefield, where in the distance you can see chariots, wooden shields, leather-armored soldiers, and plain banners fluttering in the wind. MATCH CUT。 The bronze spear transformed into a crossbow bolt fired by a Qin and Han heavy crossbow. The crossbow bolts feature sharp triangular bronze arrowheads, hardwood shafts, and stable tail feathers, with the main body still centered in the composition. The background is upgraded to the Qin-Han frontier, with rammed earth walls, wooden arrow towers, crossbow formations, and distant cavalry swiftly sweeping through the cold, gray wind and sand. The shaft spins at high speed, and the tail feathers tremble slightly in the airflow. MATCH CUT。 The crossbow bolt transformed into a Song Dynasty fire arrow. The tip of the shaft retains the metal arrowhead, the middle section is tied with a slender powder tube, and the tail emits bright orange flames and grayish-white smoke. The rocket arrow retains the previous crossbow bolt's flight direction and axis of rotation, with flames only ejected backward at the tail, without changing the main trajectory. The background is upgraded to a Song dynasty city defense battlefield, with blue brick walls, wooden towers, crossbows, shield formations, and tile-roofed buildings rapidly retreating through thick smoke. The gunpowder burned and illuminated the edge of the arrow shaft, while the smoke trail was stretched in a long line by the high-speed airflow. MATCH CUT。 The tip of the rocket arrow transforms into a Song Dynasty thunderbolt when passing through the center of the image. The Zhentian Lei is a heavy, dark gray, spherical iron firearm with cast iron texture, seams, and short fuse wires. It continued spinning at high speed along the same trajectory, with the burning fuse pulling back to spark without any premature explosion. In the background, a long-range explosion occurred on the Song Dynasty city wall, with orange-yellow fireballs, debris, and dust forming shockwaves. Backlighting creates a brief metallic highlight at the edge of the Thunderbolt, while the main body remains sharp. MATCH CUT。 The spherical Zhentian Thunder transformed into a Ming Dynasty Divine Fire Crow under the rotation of the cover. The Divine Fire Raven has a realistic crow-shaped wooden shell, black skin, short wings on both sides, and rocket thrusters at the tail—not a living bird. It flew in the same direction, with several orange-red flames simultaneously spraying from its tail, and its short wings were slightly shaken by the airflow. The background is upgraded to a large-scale Ming dynasty city defense battlefield, with brick and stone city towers, firearms battalions, rows of rocket racks, black gunpowder smoke, and military flags waving in the wind flashing swiftly. The Divine Fire Crow gradually shifted from its traditional firearm form to the outline of an early flying vehicle. MATCH CUT。 The black wings of the Divine Fire Raven spread out into a silver-gray delta-wing stealth fighter. The camera was positioned about ten meters above the front of the fighter jet to guide the high-speed reversal, while the fighter remained centered and was close to the eastern valley for a high-speed dive. Below are mist-shrouded karst peaks, rivers, and layered ridges. The aircraft's surface features a restrained dark gray stealth coating and Oriental geometric dividing lines, with no text, number, or markings. The wings cut through moist air, forming brief white condensation vortices at the tips, and thick black smoke rose behind the canyon. MATCH CUT。 The fighter jet transformed into a white, reusable manned spacecraft. The nose tilt angle, delta wing contour, and direction of movement remain consistent, the belly is covered with dark heat-resistant materials, the fuselage features red detail lines and a real heat insulation panel structure, and there are no flags, text, or institutional markings. The spacecraft's tail erupted with massive orange-blue flames, breaking through the clouds and entering low Earth orbit. The background naturally transitions from the eastern mountains to the edge of the atmosphere, with the Earth's blue arc appearing below the frame, and sunlight creating a cool white highlight along the edges of the white body. MATCH CUT。 The center of the spacecraft's tail flame becomes the giant circular thruster of the future Eastern Starship. Inside the thruster, concentric metal rings, heat-resistant ceramics, and magnetic constraint structures gradually glow with orange-red energy. The camera continued to retract at high speed, gradually revealing the front of the ship and the complete hull. Starship features a heavy, reliable industrial structure, with a main body of dark gray metal, jade-white ceramic armor, and dark red structural lines. The hull contours feature restrained Chinese axial symmetry, flying eaves with zigzag lines, and a dragon-spine longitudinal structure, but not in the form of palaces, pagodas, or cartoon dragons. The armor surface is densely covered with mechanical hatches, heat sinks, faint red status lights, and faint abstract cloud pattern embossing. The camera zooms close to the ship's hull and sweeps over the top of the hull. Large armor plates, structural beams, and a cooling grille pass at high speed beneath the lens, with the direction of movement always continuous. The camera then crosses the ship's central axis and naturally enters the rear view. In the final image, the stern of the giant Oriental Starship is at the center, with multiple circular blue and white ion engines igniting from the inside out in sequence. The engine's brightness rapidly increased, with cool blue light reflected off the jade-white ceramic and deep gray metal armor surfaces. The spacecraft generates clear acceleration, carrying a sense of immense mass as it heads into deep space. The camera gradually stopped following, the spaceship grew smaller and smaller, and finally shrank into a bright spot before the distant red-blue nebula. After the starship disappeared, the nebula's outline briefly showed natural layers reminiscent of the Ink Mountain Range, but still retained the texture of a realistic cosmic image. [Photography and Physics] The flying object lens uses a diagonal field of view of 29° to 47°, maintaining a stable escort distance between the camera and the subject. The subject remains central and sharp, with backgrounds preserving high-speed motion blur and clear historical environmental cues. Each object has the correct mass, inertia, air resistance, axis of rotation, and material reflection: the stone rotates irregularly; The mace rotates eccentrically due to the influence of the wooden handle; Spears and crossbow bolts are stable along the long axis; Zhentian Lei is heavy and rotates slowly; The Divine Fire Raven maintains its posture by relying on its tail rocket; Fighter jets, spacecraft, and starships rely on aerodynamic surfaces or propulsion systems for stable flight. Matching editing only occurs at moments when the subject passes through the center of the frame, briefly overlaps the contour, or rotates to the same angle. Every change is a clean, crisp MATCH CUT, not a gradient, melt, or part growth. Flight direction, visual center, and overall momentum are always continuous. [Sound] Only generates natural sound effects within the screen: the heroine's short exhalation when exerting power, shoe soles rubbing, the sound of fabric and headbands cutting through the air, arm swings, the whistling of stones and hammers slicing through the air, the deep whistle of bronze spearheads, the vibration of crossbow bolt tail feathers, the sound of rocket bolts burning, the sparks of thunderous lightning fuses, distant explosions, the jet of the divine fire raven rocket, the roar of fighter jet engines, the roar of spacecraft thrusters, and the stepwise charging and ignition of interstellar engines. The sound evolved over time, evolving from primitive wind and metallic sounds to gunpowder explosions, jet roars, and deep low-frequency vibrations of interstellar thrusters. No narration, no dialogue, no background music. [Realistic Suffix] Realistic cinema-grade motion physics, delicate materials, stable subject consistency, accurate matching editing, blurred depth of field and speed. Ancient Chinese female knights had natural and realistic facial features, correct body structure, and throwing movements with clear footwork, waist twisting, shoulder-arm transmission, and inertia release. It is forbidden for ancient heroines to change their faces, have abnormal fingers, wear molds in clothing, or wrap wide sleeves around their arms; Weapons are prohibited from floating, rubber deformation, sudden deceleration, reverse flight, or changing trajectory; Gradient distortion, particle recombination, and magical lighting effects are prohibited; Divine Fire Crow is prohibited from generating True Crows; Starships are prohibited from generating palaces, pagodas, or cartoon dragons. No text, subtitles, logos, watermarks, or UI appear on screen. The environment has continuously upgraded across eras, with the main flying subject's direction, visual center, rotational rhythm, and momentum consistently maintained.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

<!-- STATS_END -->
