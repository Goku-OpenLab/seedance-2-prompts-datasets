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
- Total Prompts: **4760**
- Updated Today (UTC 2026-07-06): **0**

## 🎬 Today's Updates
### 🎬 One Flower Connects The World
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04783.jpg" width="480" alt="SD2_04783"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/one-flower-connects-world-SD2_04783">🌐 Watch Online</a>

#### 📝 Prompt
```
Live-action shooting style, fast editing, cinematic feel, 4K, 24fps, warm natural light, real character performances, natural lip-syncing, no subtitles. Using the transmission of a single flower as the core visual thread of the entire video, flowers rapidly travel from one country to another, connecting different regions and people worldwide. At every scene, a character would receive the flowers, smile sincerely, and say "thank you" in the local language. The overall rhythm is lively and smooth, the camera is dynamic, emphasizing authentic street and daily life, cross-cultural warm connections, and the transmission of goodwill between people. Transition method: Previously, one person handed the flower out of the frame, and in the next shot, another person caught the flower in a new scene or used quick lens shifts, motion blur, or foreground occlusion to complete seamless transitions to maintain visual continuity of the flowers in the frame, creating a "one shot to convey the world" feel. Camera style: handheld follow-shooting, slight camera shake, quick push-pull, combination of close-up and mid-shot, realistic ambient sound and atmosphere, cinematic street photography quality. The background music is warm, upbeat, and world-traveling, ending gently and fading. Scene 1 @图像1中国花店内, realistic real-life scenarios. The girl took a rose, looked at Qiantou with a smile, and naturally said, "Thank you!" The camera follows the flowers from the right side of the frame, where the girl gently lifts the bouquet after receiving them. Scene 2 @图像2英格兰街 head, slightly cool weather, natural street scene. The man took a carnation, smiled, nodded, and said, "Thank you!" Through a toss-and-shoot transition, the flower is thrown from the previous scene into this one. Scene 3 @图像3墨西哥市场, rich in color and full of everyday life. Auntie took a bouquet of marigolds, put her hands together warmly, and said, "¡Gracias!" The camera quickly skirts the stalls and crowds, freezing at the moment of receiving flowers. Scene 4 @图像4印尼乡村, natural sunlight pours in. The child takes a frangipani, smiles happily, bows slightly, and says, "Terima kasih!" The camera has a touch of running energy, and the atmosphere is pure and natural. Scene 5: @图像5泰国街头, bustling cityscape. The vendor took a jasmine wreath, put his palms together, and said warmly, "ขอบคุณค่ะ!" The camera moves forward briskly, the wreath @图像6阿拉伯庭院 in the sunlight, soft light and shadow, and an elegant environment. The lady took a Desert Rose Puppet, touched her chest with a smile, and said, "IJSul." The scene is quiet and warm, and the characters' expressions are sincere. Scene 7: Micro-oscillation. Scene 6 @图像7巴西社区, the atmosphere is lively and enthusiastic. The boy took a gerbera and happily said, "Obrigado!" The shots are rhythmic and full of vitality. Scene 8: @图像8日本街道, an office worker takes a small flower from a lunchbox, bows politely, and says, "Thank you!" The shots are short and crisp, retaining the urban rhythm. Scene 9 @图像9韩国街头, modern urban feel. The young woman took a branch of azalea, naturally clasped her hands together, and smiled, saying, "Thank you!" The camera pauses briefly at the moment she smiles, then softly fades out of the painting.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `18.08s`

---

### 🎬 Racing Heart, Finding Light
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04782.jpg" width="480" alt="SD2_04782"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/racing-heart-finding-light-SD2_04782">🌐 Watch Online</a>

#### 📝 Prompt
```
A 30-second cinematic youth racing short film with 2D animation style. The protagonist is a young rider riding a motorcycle in a high-level competition. The overall style is passionate, youthful, emotionally intense, and cinematic, featuring a complete beginning, development, transition, and clear emotional arc. The entire film uses only two types of camera movements: high-speed follow shots and slow-motion surround. Lines are very few, appearing naturally like fragments of memory, with a tone that is sincere, gentle, and restrained, without shouting slogans or excessive emotional expression. No sense of disaster, no negative expressions, no exaggerated sci-fi stories. Emphasis is placed on love, support, counterattacks, and growth in the race of youth. From 0 seconds to 5 seconds on the dusk track, the high-speed and intense race kicks off the race. The camera closely followed the teenager's motorcycle at high speed on the ground, with tires skimming the track sideline, the motorcycle roaring, the wind howling, and the atmosphere tense and heated. The boy was fully focused, the setting sun casting sharp highlights on the car's metal body. Between 5 and 9 seconds into the crucial turn, the young man was suddenly overtaken by his opponent. The high-speed follow-up continues, with the footage showing a sense of pressure as the rankings drop and the rhythm is disrupted. Brief distraction, shortness of breath, and slight trembling in the helmet in close-up. The boy whispered, "Can I still catch up..." From 9 seconds to 14 seconds, the boy fell behind, his breathing heavier, and his emotions hit rock bottom. The race didn't stop; the locomotive continued speeding forward. The scene begins to flash through warm memories during high-speed riding: when learning to ride as a child, someone supported him from behind; His father helped him tidy his helmet, moving carefully and quietly; Before the finish line—a gentle smile watching him; On the dusk slope, the silhouettes walking side by side. All these memories are presented with golden backlighting, soft slow motion, and fragmented sensations. From 14 to 18 seconds, the music gradually shifts from repression to uplifting. A restrained yet gentle voice echoed in my memory: "Don't be afraid - I'm always here." Stay steady. And locokforward." The boy's gaze refocused, his breathing steadying, and his emotions shifted from movement to determination. From 18 seconds to 23 seconds, the young man regained his faith, accelerated at full speed, and counterattacked with precise cuts. High-speed tracking white expresses the motorcycle's power and control when cornering, exiting, and closing in on the vehicle ahead. The boy said softly but firmly, "Iwon't stop here." Between 23 and 27 seconds, a stretch of uphill track appeared, and the boy sprinted at full speed toward the sunset. The visuals retain only breathing sounds, engine noises, and rising music, without adding unnecessary lines. The locomotive was lifted off by inertia, entering shocking slow motion. At the end of the depths of my memory, a gentle voice with a smile echoed: "Goon." Between 27 and 30 seconds, the camera performs slow-motion close-ups around the locomotive suspended in midair. Pushing passion, gentleness, freedom, and upward leaps to a climax. A blooming effect appears behind you, followed by seedance, referring to @图像1
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.07s`

---

### 🎬 Morning Alley Moments
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04781.jpg" width="480" alt="SD2_04781"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/morning-alley-moments-SD2_04781">🌐 Watch Online</a>

#### 📝 Prompt
```
Main subject: young Korean woman, early 20s, natural everyday appearance, faded charcoal-grey sleeveless crop top, loose high-waisted light-wash jeans, black canvas sneakers, black cord necklace, black wavy hair in a messy side ponytail with wispy bangs. Realistic skin texture, minimal makeup, warm and approachable personality. Maintain consistent identity, clothing, hairstyle, and appearance throughout the entire video.
Location: Authentic Korean residential neighborhood during a calm late morning. Narrow concrete alleys, low-rise homes, small terraces, potted plants, laundry lines, bicycles, utility poles, overhead wires, mature trees casting moving shadows, quiet residential atmosphere. No stores, advertisements, cafés, crowds, or commercial activity.
Visual Style: Ultra-realistic documentary realism. Genuine candid behavior. Natural body language. Unscripted slice-of-life feeling. Strong environmental authenticity. Rich real-world details and believable human motion.
Camera Style: Early-2000s consumer DV camcorder aesthetic. Friend casually recording everyday moments. Heavy handheld shake, imperfect framing, frequent autofocus hunting, lens breathing, exposure pumping when moving between sun and shade, occasional motion blur, subtle rolling shutter, mild digital compression artifacts, faded colors, soft contrast, slight sensor noise. No stabilization. No cinematic camera moves. No modern color grading.
00:00–00:02
Outside a small house entrance. She sits on a low concrete wall adjusting her ponytail with both hands raised. A light breeze moves loose strands of hair. She smiles naturally while the camera struggles to hold focus.
00:02–00:04
The camera follows her into a narrow alley lined with potted plants and concrete walls. She notices a stray cat approaching and crouches down. Framing drifts off-center as the operator tries to keep up.
00:04–00:06
She gently pets and feeds the cat. Autofocus repeatedly shifts between her face and the animal. Morning sunlight flickers through leaves overhead.
00:06–00:08
Small front yard beside her house. She hangs laundry on a clothesline while fabrics sway in the breeze. Exposure changes as clouds briefly pass overhead.
00:08–00:10
On a quiet terrace with a ceramic coffee cup. She sits comfortably watching the neighborhood, occasionally brushing hair behind her ear. Loose handheld side angle with natural camera drift.
00:10–00:12
Close side profile. Someone off-camera greets her. She turns, raises her hand, smiles warmly, and casually says, “Annyeong.” The camera catches the moment slightly late.
00:12–00:15
Walking slowly down a tree-lined residential lane holding her coffee cup. She notices the camera, gives a small genuine smile, then looks away and continues walking. Recording cuts abruptly to black mid-motion as if the camcorder was switched off.

Audio: Natural ambient sound only — morning birds, distant motorcycles, light wind, leaves rustling, faint neighborhood
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Ancient Oak Four Seasons Orbit
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04780.jpg" width="480" alt="SD2_04780"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ancient-oak-four-seasons-SD2_04780">🌐 Watch Online</a>

#### 📝 Prompt
```
A single uninterrupted cinematic shot begins at sunrise in the middle of a vast peaceful meadow. At the center stands one enormous ancient oak tree with a wide trunk, sprawling branches, and deeply textured bark. The surrounding landscape is calm, covered in fresh green grass with distant mountains beneath a soft golden sky. Gentle birdsong fills the air as the camera slowly begins orbiting the tree in a perfectly smooth circular motion. The tree remains at the exact center of the frame throughout the entire film. As the camera completes the first quarter of its orbit, spring awakens instantly around the tree. Tiny buds emerge along every branch. Fresh green leaves unfurl in beautiful synchronized motion. Wildflowers bloom across the meadow in waves of color. Butterflies flutter through the warm air while birds begin building nests among the branches. Soft morning mist lifts from the grass as sunlight grows brighter. Without stopping, the camera continues its orbit. The landscape gradually transforms into vibrant summer. The tree's canopy becomes dense and full. Long grass sways gently in the warm breeze. Bees collect pollen from blooming flowers. A nearby stream sparkles under intense sunlight. Children briefly appear beneath the tree enjoying a picnic before naturally fading as time continues moving forward. Everything feels alive with warmth and abundance. The camera never cuts. As it reaches the opposite side of the tree, summer slowly gives way to autumn. The sunlight becomes warmer and lower in the sky. Leaves transition through brilliant shades of emerald, yellow, orange, crimson, and deep red. Gentle wind carries thousands of leaves into elegant swirling patterns around the camera. The meadow changes into rich golden tones while migrating birds cross the distant horizon. Time accelerates. The final leaves drift gracefully to the ground. The orbit continues. A quiet snowfall begins. Within moments the landscape transforms into winter. Snow blankets every branch with delicate crystalline detail. Frost slowly spreads across the bark. The nearby stream freezes into clear ice. The sky becomes pale blue while soft snowflakes fall silently through the air. The entire world feels peaceful and still. The camera completes one full orbit. Instead of stopping, it continues circling faster. Each complete revolution now represents decades instead of seasons. Spring, summer, autumn, and winter flow continuously around the tree in increasingly rapid succession. Blossoms bloom and disappear. Leaves grow, change color, and fall. Snow arrives and melts.
```

#### 📌 Details
- Ratio: `0.57` | Duration: `15.17s`

---

### 🎬 Tokyo Summer Girl Travel Diary
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04779.jpg" width="480" alt="SD2_04779"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/tokyo-summer-girl-travel-diary-SD2_04779">🌐 Watch Online</a>

#### 📝 Prompt
```
Use the reference grid image as the source of the same girl and her 10 summer travel scenes in Tokyo. Create a single 15-second feel-good travel-vlog montage, 16:9 horizontal, flowing through all 10 scenes in order as quick handheld phone shots, about 1.5 seconds each, snappy cuts on the beat. The same girl in every shot with consistent face and hairstyle; in each shot her outfit matches that scene in the reference. Throughout, she radiates excitement and joy — bright eyes, easy smiles, playful energy — and each shot shows off what makes that spot special. Authentic smartphone look, natural ambient light, subtle grain, light handheld motion. Bright, joyful sightseeing music that conveys the fun of travel, around 125 bpm. Shot 1 — Inokashira pond swan boat: she laughs with delight and rocks the pedal boat, sparkling water and a swan boat gliding behind, warm sun flare. Shot 2 — cafe matcha kakigori: eyes lighting up, she lifts a spoonful of fluffy shaved ice toward the camera and beams, the towering dessert in frame. Shot 3 — Harmonica Yokocho alley at night: she strolls through the glowing red-lantern alley, glances back with an excited grin, lively izakaya signs around her. Shot 4 — hotel mirror selfie: a happy, relaxed mirror selfie, she tilts her head and smiles softly, calm window light, cozy room mood. Shot 5 — summer festival night: she bites a bright candy apple and bursts into a giggle, swaying paper lanterns and a buzzing crowd behind her. Shot 6 — golden-hour window selfie: an arm's-length selfie bathed in warm sunset light, soft hair movement, a contented joyful smile. Shot 7 — ivy-covered Ghibli-style museum: she gazes up in wonder, spinning slightly to take it all in as the camera tilts up the lush green facade. Shot 8 — Inokashira park path: she crouches with a delighted laugh and points as a small squirrel scampers by, dappled sunlight, playful energy. Shot 9 — Harajuku shop window with bubble tea: she sips happily through a straw, her reflection shimmering in the glass, the bustling colorful street behind. Shot 10 — on the train home: a calm, satisfied selfie, hand on her cheek, city skyline streaking past the window, a soft fulfilled smile. Smooth energetic flow from shot to shot, consistent color and grain throughout, upbeat happy travel-diary mood.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Storm Crane Escape
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04778.jpg" width="480" alt="SD2_04778"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/storm-crane-escape-SD2_04778">🌐 Watch Online</a>

#### 📝 Prompt
```
Hyper-realistic cinematic action sequence, 15 seconds, aspect ratio 16:9. Night. High above a futuristic city during a violent storm, two agents, one man and one woman, run across the long horizontal arm of a giant construction crane connecting one skyscraper to another unfinished tower. Both wear dark fitted tactical clothing with no hoods, no helmets, and no masks. Their hair is visible and moves in the wind. No celebrity resemblance and no famous actor look. Heavy rain lashes the metal surface, wind shakes the crane, warning lights blink red, and the glowing city stretches far below through mist. Wide opening shot: the two agents sprint along the crane arm high above the city while several chasers follow behind from the rooftop access point. Rain, wind, and height create immediate danger. Tracking shot: the agents continue running along the narrow crane arm. The crane sways in the storm, loose tools and metal parts slide past them, and the surface becomes slick with rain. They keep low for balance while the chasers gain behind. Side exterior shot: a powerful gust makes the crane swing harder. One section rattles violently, a hanging cable whips across the frame, and debris flies away into the night. The agents keep moving toward the unfinished tower ahead. Final 5 seconds: the sequence becomes more intense. The crane arm tilts and shakes. One agent nearly loses footing but the other grabs and steadies them without stopping. They reach the far end of the crane and make a fast desperate jump from the crane arm onto the unfinished floor of the next skyscraper. They land hard, roll across the wet concrete, and regain balance as the crane continues swaying behind them. Final moment: the two agents rise on the unfinished tower floor, storm raging around them, while the giant crane swings behind against the glowing city skyline. Style: hyper-realistic, cinematic, fast-paced, suspenseful, clear and readable action, strong sense of height and danger, storm, rain, wind, blinking warning lights, metal structure, dynamic but readable camera movement, visible hair, no hoods, no helmets, no masks, no celebrity resemblance, no text, no logos, no cartoon style, no slow motion. Keep proportions. Keep style and features. Aspect ratio 16:9.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.13s`

---

### 🎬 Neon Kawaii Hyper Pop Chaos
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04777.jpg" width="480" alt="SD2_04777"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/neon-kawaii-hyper-pop-SD2_04777">🌐 Watch Online</a>

#### 📝 Prompt
```
Use the uploaded images as character and style references. 15-second kawaii hyper-pop music video at BPM 174. No lip-sync. No singing focus. Create a fast, chaotic, cute visual sequence with rapid character switching among all uploaded reference characters. Style: Pastel neon anime, pink, cyan, yellow, mint, lavender, bold outlines, flat shading, stickers, flowers, bows, spirals, halftone dots, manga panels, candy glitch accents. Main motion: Fast BPM174 rhythm, rapid cuts every 0.1–0.4 seconds, cute dance bursts, sudden poses, bouncing, spinning, mob-dance energy, exaggerated reactions, clone echoes, split panels, and visual overload. Lens effects: Use strong fisheye and ultra-wide distortion. Make the center bulge forward. Stretch and curve the edges clearly. Use obvious barrel distortion, warped perspective, tunnel zooms, crash zooms, rotating camera, dutch angles, whip pans, and sudden push-ins. Variation: Do not repeat similar shots. Each section should introduce a different effect: fisheye close-up, spinning camera, split-panel shatter, clone multiplication, kaleidoscope mirror, mob-dance burst, sticker tunnel, wide-angle distortion, radial explosion, multi-character chaos. Timeline: 0–3s: extreme fisheye close-ups, fast character switching, sticker bursts. 3–6s: rotating camera, panel splits, shattered manga frames. 6–9s: clone multiplication, mob-dance bouncing, wide-lens warping. 9–12s: kaleidoscope mirrors, tunnel zooms, crash zoom reactions. 12–15s: maximum chaos, rapid effect relay, all characters in fast succession, final distorted cute impact frame. Important: Make the fisheye distortion visually obvious, especially at the edges. Keep faces cute and readable. Use many different visual tricks, not one repeated effect. Negative prompt: weak fisheye, only round frame, static camera, repetitive shots, slow motion, lip-sync, realistic style, horror, grotesque face, broken anatomy, extra limbs, muddy colors, low energy
```

#### 📌 Details
- Ratio: `1.74` | Duration: `16.43s`

---

### 🎬 Gears' Workshop Chaos
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04776.jpg" width="480" alt="SD2_04776"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/gears-workshop-chaos-SD2_04776">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: High-quality, vibrant 3D animated cartoon (Pixar/Illumination style). Frantic pace, squash-and-stretch physics, exaggerated expressions, dynamic lighting, and detailed textures. Characters: Gears, a small, overly enthusiastic, bright blue inventor’s robot with tread-wheels, multiple springy arms, and big, expressive digital eyes. He is constantly moving and beep-booping excitedly. Duration: 15 Seconds Setting: A colorful, chaotic, Rube Goldberg-esque inventor's workshop, filled with giant gears, conveyor belts, tubes, levers, and sparking gadgets. 15-Second Animation Breakdown: (0-3 seconds: The Start): The camera starts with a rapid zoom following Gears as he races through the workshop on his treads. He’s bouncing off cushions, weaving through moving mechanical legs, and juggling three shiny silver cogs. His arms are a blur of motion. He narrowly dodges a swinging giant pendulum with a comical "whoosh" sound effect. (3-7 seconds: The Chain Reaction): Gears accidentally bumps into a large, messy workbench, tripping a large red lever. This triggers a chaotic chain reaction.A boxing glove pops out, punching a ball down a spiral ramp.The ball triggers a fan that blows colorful feathers everywhere.A tube starts rapidly firing brightly colored ping-pong balls. Gears is in the middle of this chaos, wide-eyed and sputtering, frantically ducking the boxing glove, batting away feathers, and comically trying to catch the ping-pong balls, spinning around wildly on his treads. (7-11 seconds: Escalation): A conveyor belt speeds up fast, loaded with wobbly, jelly-like robotic parts. Gears tries to sort them but they bounce everywhere. He grabs a spring that stretches ridiculously far, launching him across the room. He lands on another conveyor belt, which quickly pulls him towards a large, goofy mechanical claw. (11-14 seconds: Maximum Chaos): The mechanical claw grabs Gears and a wobbly, half-assembled robot toy he was holding. It spins them both in a dizzying circle high above the workshop chaos. The workshop background is a blur of motion, flying parts, sparks, and steam. Gears has a look of comical terror, but is also trying to fix the toy while spinning. (14-15 seconds: The Punchline): The claw abruptly stops. The workshop goes instantly quiet, but everything is messy and askew. Gears is hanging upside down from the claw, dizzy, eyes swirly. He finally places the last cog on the wobbly robot toy. The toy instantly springs to life, makes a cheerful beep-boop sound, and wiggles its arms. Gears gives a dizzy grin and a "thumbs-up" to the camera as the scene fades. Camera: Constantly moving, dynamic, tracking Gears closely, utilizing rapid pans and zooms to match the frantic pacing. Audio: Fast-paced, cartoon music, lots of vibrant sound effects (boings, whizzes, clangs, beeps).
```

#### 📌 Details
- Ratio: `2.33` | Duration: `15.08s`

---

### 🎬 Alien Chase at Dusk Construction Site
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04775.jpg" width="480" alt="SD2_04775"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alien-chase-construction-site-SD2_04775">🌐 Watch Online</a>

#### 📝 Prompt
```
A hyper-real cinematic action sequence set in an active construction site at dusk. Exposed rebar, scaffolding, unfinished concrete floors, and a tall tower crane dominate the scene. Dust hangs in the air. Sound design: heavy breathing, metallic clanks, distant machinery, and guttural alien screeches. The video starts mid-chase. sprints across a half-built floor, leaping over gaps and dodging debris. Behind her, three alien —slick, elongated, with pale skin and wet, sinewy movement—pursue aggressively, closing in. She spots a tower crane ladder and veers hard toward it, grabbing on and climbing fast. The camera stays tight, tracking her ascent as the creatures scale the structure with unnatural speed. One creature lunges upward and grabs her ankle. She kicks violently, freeing herself, scraping against metal. No pause—she climbs the last few rungs and pulls herself onto the crane cabin platform. She yanks the cabin door open, dives inside, and slams it shut. Immediate silence shift—muffled exterior sounds. She stumbles back, breathing hard. Seconds later, the creatures reach the cabin. Slimy hands and distorted faces press against the glass, leaving streaks. The cabin rattles under their weight. She watches, frozen, as they claw and slide across the windows. Close on her face—panic, controlled breathing. Exterior noise builds. No hard cut.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.08s`

---

### 🎬 Delivery Girl Shy Glance Back
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04774.jpg" width="480" alt="SD2_04774"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/delivery-girl-shy-glance-SD2_04774">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: 8K cinematic texture. Realistic Photography—No 3D rendering, no game engine, no game cutscenes. Photography: Master-level naturalist photography. Lighting: Only natural light—backlight contour light, with the camera position on the shadow side, and a thin mist in the air. The main light comes only from daylight and window light. Color: 60:30:10 — main color / secondary color / accent color. Lens: Physical movie shots. 180° shutter motion blur. Skin: Pore-level realism—hair texture, asymmetrical moles, capillary redness, pore shadows matched to on-site lighting. Performance: Top-tier cinematic — slight pauses before reactions, precise gaze, moist, expressive eyes with a glint, visible breathing and chest movements. Physics: Observes gravity and inertia—mass has real weight, correct contact with shadows, no levitation objects. Composition: Thirds + golden ratio. From the very first frame, everyone moved. Continuity: Characters, props, and environments are identical in every shot, with no identity drift. Technology: 24fps smooth movement. 8K detail. No shaking. Audio: ambient sound only. No music. No subtitles. SUBJECT — The delivery person is the uploaded first frame: a high-bun hairstyle, yellow-black contrasting softshell jacket with a light khaki vest and gray sweatpants, carrying a black insulated delivery box in the right hand. The video continues from this first frame straight to the end, with the appearance, clothing, hairstyle, and incubator consistently matching the first frame. WB 5200K。 MULTISHOT — greeting at the door, entering the house, dropping off takeout, and giving a shy and playful glance back before leaving. Chinese lines, lip-syncing. LOCATION — Modern apartment elevator corridor, beige marble and warm corridor lights, transitioning inward to a tidy entryway. The video naturally extends from the corridor space in the first frame into the interior, with delivery workers moving within the real space. ACTION — POV First-Person: The camera refers to "you" (the customer) opening the door and watching her enter the room. The frame starts moving from the opening frame (where she stands in the hallway, looking up at the camera). SHOT 1 (0:00–0:05) — Opening frame: the delivery person looks up at the camera, a warm smile, right suitcase. She said, "Hello, your food delivery has arrived." " The male voice (customer/camera) responds: "Alright, help me bring it in." " Hard cut. SHOT 2 (0:05–0:10) — The camera steps back slightly as she enters. She steps over the threshold into the entryway, bends down to place the incubator beside the cabinet, takes out the lunch box and arranges it neatly, then straightens the hem of her jacket. Voiceover: "Thank you." She lowered her head slightly, her cheeks flushed, paused shyly, and then said, "No need to thank me. Wish you a pleasant meal." " Hard cut. SHOT 3 (0:10–0:15) — She turns to leave, then stops, looks back over her shoulder to look at the camera, her eyes curved, fingers gently flicking the backpack strap. With a playful pause, she said, "Do you want me to stay and eat with you?" " Fixed on her smile as she glanced back over her shoulder, the warm glow softening softly. CAMERA — SHOT 1: POV head-up view, lock the camera position at the entrance, 35mm texture, light handheld breathability; Motivation—first meeting. SHOT 2: POV chest height slowly pulls back as she enters the room, 28mm, slight handheld movement; Motivation—to make room for her to enter. SHOT 3: POV zoom to 50mm medium close-up, landing on her face as she turns back; Motivation—playful hooks. STYLE — Main color: Warm beige marble with corridor lamp tungsten silk gloss 60% / Secondary color: Cool gray sweatpants and black thermal case 30% / Accent: yellow outdoor jacket 10%. WB 5200K。 The main light comes from the corridor ceiling light and the exterior interior lights, creating a light and misty feel. CONSTRAINTS — 9:16 vertical mode. No slow motion, natural 24fps throughout. The video strictly continues from the uploaded first frame, without altering the appearance or composition of the first frame. POV maintains first-person perspective, with no camera showing the customer's body (at most implying hands). The delivery person's identity, clothing, hairstyle, and the incubator are exactly the same. The location is naturally appropriate. Three lines of Chinese dialogue are clean and lip-synced. No eyes glow, no burning subtitles.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.13s`

---

### 🎬 Tokyo 10-Second Travel Diary
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04773.jpg" width="480" alt="SD2_04773"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/tokyo-10s-travel-diary-SD2_04773">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 10-second cinematic travel vlog montage. Use the uploaded woman’s face consistently throughout every shot. She is a stunning young female travel creator with long dark wavy hair with curly bangs,wearing fashionable oversized Japanese streetwear (burgundy long leather jacket,shoulder bag), natural makeup, cheerful personality. The entire video should feel like real smartphone footage, with handheld camera movement, imperfect framing, accidental lens flare, slight motion blur, rolling shutter, high ISO noise at night, autofocus hunting, overexposed highlights, slight barrel distortion from a phone wide-angle lens, tiny lens smudges, and natural camera shake. No polished commercial look. Story Flow (10s) 0.0–0.8s Low-angle selfie in front of Tokyo Tower. She smiles naturally while adjusting the phone. Slightly tilted horizon. Bright overexposed cloudy sky. Tiny fingerprint on lens. 0.8–1.6s Walking through Shibuya Crossing at night. Looks back at camera while walking. Neon reflections on wet road. Strong motion blur. Quick whip-pan transition. 1.6–2.4s Inside a Japanese convenience store. Holding an onigiri close to camera. Playful eyebrow raise cutely . Harsh fluorescent lighting. Background shelves softly blurred. 2.4–3.2s Sitting alone in Yoyogi Park. Quiet candid moment. Looking away from camera. Soft sunlight filtering through trees. Slight focus miss. 3.2–4.0s Eating freshly made takoyaki. Instant reaction after first bite. Warm lantern lighting. Face slightly blurred from movement. Laughing naturally. 4.0–4.8s Standing in front of a glowing vending machine. Blue and pink lighting on face. Pressing drink button casually. Visible night grain. 4.8–5.6s Reflection in Tokyo tram window. Layered city lights reflected on glass. She looks outside thoughtfully. Train moving creates light streaks. 5.6–6.4s Walking beneath a Torii gate. Low-angle tracking shot from behind. Turns her head briefly. Motion blur. Bright halo from sky. 6.4–7.2s Immersive digital art exhibition. Blue, purple and gold lights moving across face. Looking upward in amazement. Natural low-light noise. 7.2–8.0s Wide-angle low-angle shot beside the giant silver bullet sculpture. She appears small beneath the sculpture. Phone lens distortion. Sky slightly blown out. 8.0–8.8s Walking through a lantern-lit alley. Camera follows behind. She turns around with a smile. Warm lantern glow. Natural night grain. 8.8–10.0s Rooftop selfie overlooking Tokyo skyline. Wind blows hair across camera lens. Slightly tilted horizon. Overexposed city lights. She laughs naturally while extending one arm toward the skyline. Editing Style * Fast whip-pan transitions * Speed ramps * Match cuts * Natural jump cuts * Handheld camera movement * Slight rolling shutter * Smartphone HDR exposure * Real travel vlog energy * No slow motion * No cinematic movie grading * Authentic TikTok creator aesthetic * Warm
```

#### 📌 Details
- Ratio: `1.97` | Duration: `10.21s`

---

### 🎬 Pharaoh Rage EDM Performance
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04772.jpg" width="480" alt="SD2_04772"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pharaoh-rage-edm-performance-SD2_04772">🌐 Watch Online</a>

#### 📝 Prompt
```
Have the Pharaoh walk across the scene, moving from the center to the left side of the screen. He should act as if he is enraged, then seamlessly transition to the right side of the screen. Ensure the movement is fluid and continuous. Use energetic EDM music. The audience should be visibly interacting—jumping, dancing, cheering, and recording the performance with their smartphones.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Six Rooms Emotional Journey
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04771.jpg" width="480" alt="SD2_04771"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/six-rooms-emotional-journey-SD2_04771">🌐 Watch Online</a>

#### 📝 Prompt
```
In a single continuous take, the camera smoothly follows a person in a black coat (see @图像1) from left to right through six connected rooms with different tones and atmospheres. Each room has the same structure: white walls, light-colored herringbone flooring, French double-leaf floor-to-ceiling windows, white sheer curtains, and the reference @图像2但窗外风景 and interior atmosphere are completely different. The protagonist walks at a steady pace throughout, passing through every open door on the wall. 0-5 seconds, first room, themed around American comic fights, where the protagonist enters the house and fights characters @图像3), resulting in defeat; 5-10 seconds, second room, theme warm, felt style, outdoor scene sunflower field @图像4), indoor lighting warm orange soft light, an artist painting sunflowers @图像5). After the protagonist enters, it also takes on a felt style; 10-15 seconds, third room, theme is sadness. The entire scene is in a black-and-white comic stop-motion animation style. Outside the window, it's rainy, the room is cold and gloomy. Sitting alone on the empty room center floor, head bowed and hugging knees, a phone beside me is lit up with an unanswered call screen. After entering the room, the protagonist turns off the lights and immediately turns them on, turning the room into colors and instantly filling the room with flowers; 15-20 seconds, fourth room, theme of joy, the entire scene is a room soaking in the sea, reference @图像6, the protagonist swims into the room, surrounded by beautiful coral reefs and schools of fish; 20-25 seconds, fifth room, themed around surprise, outside the window scenes are filled with fireworks and night sky, reference @图像7, indoor light flickers in color, the protagonist is swept into the cheering atmosphere. At 25-30 seconds, the protagonist finally arrives in a blank room, stands in the center, snaps his fingers, and the sound effect is a snap sound. The screen is completely black, and the words "seedance" appear in the middle. See @图像8. The overall cinematic texture and high-end fashion advertising style are entirely determined by the lighting outside the window, creating a strong emotional contrast with no text in the visuals.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `29.93s`

---

### 🎬 Mumbai Rain Night Humanoid Bat Horror
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04770.jpg" width="480" alt="SD2_04770"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/mumbai-rain-humanoid-bat-SD2_04770">🌐 Watch Online</a>

#### 📝 Prompt
```
Video edit, ultra-realistic. Handheld camera slowly zooming in on the tall L-shaped street light pole on a rainy Mumbai evening. From the top arm of the pole, a realistic humanoid creature (Image attached) is hanging upside down like a bat — muscular bat-like body with leathery wings folded, human-like face, wet fur and skin texture, claws gripping the pole. The camera pushes in closer. At the very end, the humanoid bat’s eyes suddenly snap open, glowing faintly, and it stares directly at the camera with an intense look. Moody blue-orange street light glow, rain falling, atmospheric and creepy.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `7.7s`

---

### 🎬 Luxury Pink Fashion Pool Commercial
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/0/SD2_04769.jpg" width="480" alt="SD2_04769"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pink-luxury-fashion-commercial-SD2_04769">🌐 Watch Online</a>

#### 📝 Prompt
```
“PINKY RARE 10s \| 9:16 Vertical \| Luxury Fashion Commercial 1. 0:00–0:01 — WIDE ESTABLISHING SHOT Camera: 28mm locked, slow dolly forward Notes: Pool water ripples gently, palm leaves sway naturally. 2. 0:01–0:02 — SIDE POOL VIEW Camera: 35mm, slow left-to-right slide Notes: Realistic parallax, sparkling turquoise water and striped umbrellas. 3. 0:02–0:03 — MACRO POOL WATER Camera: Macro, tilt downward Notes: Tilt naturally until shimmering reflections fill the frame. 4. 0:03–0:04 — FEET WALKING Camera: Low angle-level tracking, 85mm Notes: Follow her bare feet walking beside the pool. Sunglasses hang naturally from her hand. 5. 0:04–0:05 — SUN KISS PORTRAIT Camera: Low-angle, tilt up Notes: She raises her hand to shield the sun. Warm lens flare between her fingers. 6. 0:05–0:06 — BEAUTY CLOSE-UP Camera: 85mm, slow push-in Notes: She lowers her hand, gently adjusts her sunglasses and smiles confidently. 7. 0:06–0:07 — OVER-SHOULDER PORTRAIT Camera: 50mm, slow arc Notes: Camera arcs around her shoulder as she turns back toward the pool with relaxed elegance. 8. 0:07–0:08 — SWIMSUIT MACRO Camera: 100mm macro, slow push-in Notes: Reveal realistic stitching, folds, woven texture and sparkling water droplets. 9. 0:08–0:10 — FINAL HERO SHOT Camera: Extreme macro, slow push Notes: Hold on final frame. Logo remains clean and static. Tiny water droplets shimmer in the sunlight. Audio Direction: Dreamy luxury summer music, subtle pool ambience, gentle breeze, soft footsteps, elegant fashion commercial sound design. Notes: Smooth cinematic transitions. Consistent lighting, color grading and environment. No extra people, no outfit changes, no AI morphing.”
```

#### 📌 Details
- Ratio: `0.57` | Duration: `10.13s`

---

<!-- STATS_END -->
