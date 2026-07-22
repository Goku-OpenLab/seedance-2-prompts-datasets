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
- Total Prompts: **8167**
- Updated Today (UTC 2026-07-22): **41**

## 🎬 Today's Updates
### 🎬 Anime Style Riverside Outdoor Cooking
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10560.jpg" width="480" alt="SD2_10560"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/anime-riverside-cooking-SD2_10560">🌐 Watch Online</a>

#### 📝 Prompt
```
A peaceful anime-style outdoor cooking scene in a lush riverside forest where fresh ingredients are harvested from nature. A hand catches a silver fish from a clear stream, picks and washes leafy greens, then slices the fish and prepares vegetables on a wooden cutting board. Spices are added to a hot wok over a campfire, followed by fish, greens, and mushrooms simmering into a rich, steaming stew in a clay pot. The meal is served on a rustic wooden table beside a fresh coconut drink under warm, dappled sunlight. Cinematic anime visuals, vibrant colors, soft natural lighting, highly detailed, tranquil atmosphere, 4K.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `11.08s`

---

### 🎬 Premium PUMA Shoebox Cinematic Unboxing
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10559.jpg" width="480" alt="SD2_10559"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/puma-shoebox-cinematic-unboxing-SD2_10559">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-realistic 4K cinematic product unboxing of a premium PUMA shoebox placed on soft white bed sheets in warm natural morning sunlight. Close-up handheld camera with smooth slow push-in, shallow depth of field, soft shadows, luxury lifestyle aesthetic, minimal bedroom setting. Hands gently slide the shoebox into frame, slowly lift the lid to reveal brand-new sneakers wrapped in white tissue paper. Crisp fabric textures, realistic cardboard details, premium product showcase, warm beige color grading, subtle camera movement, photorealistic lighting, DSLR quality, high dynamic range, elegant commercial advertisement style, vertical 9:16, 60fps, ultra-detailed, clean and premium social media reel.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `10.04s`

---

### 🎬 Distracted Coffee Spill In Internet Cafe
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10558.jpg" width="480" alt="SD2_10558"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/distracted-coffee-spill-internet-cafe-SD2_10558">🌐 Watch Online</a>

#### 📝 Prompt
```
Scene One: iPhone handheld shooting, real internet café scene, friends casually snapping pictures. Fully automatic camera: Auto exposure/auto focus/auto white balance. Handheld slight shake + breathing sensation, autofocus occasionally brief search defocus, white balance naturally adjusts with light, image flat, slight edge chromatic aberration, and slight blurring during movement. No post-processing, no color grading, no special effects. Natural ambient sounds within the painting: keyboard noise, noisy internet cafes in the distance, clothes rubbing, occasional breathing. In the background, the blurry silhouettes of other customers playing games. 0:00 The screen begins. Male lead hf_20260702_115248_424b92a4-ca6f-401a-baa3-709ae4b60581 Sitting in a gaming chair, with a monitor right in front of you, your fingers quickly typing on the keyboard, focused on gaming. The monitor's blue light is reflected on the lens. The camera was positioned behind his right shoulder, at a slightly higher angle, holding the hand slightly and breathing. Autofocus twitched slightly between the keyboard and the screen. On both sides of the background, you can see figures at other workstations—blurry but clearly playing games. On the right side of the table (near the edge of the aisle), there was a white mug, far from the keyboard, right at the edge of the table, as if it could be knocked out at any moment. 0:02 Girl Clothing Image_20260719093342_1234_183 Enter from the left side of the screen. Carrying a metal coffee pot in his right hand, he walked down the aisle. The camera gently pans to follow, but the tracking is unstable, with slight side to side shakes—a real-life casual reactive follow, not a stabilizer. 0:04 The girl walked to the left edge of the table and stopped, right next to the white mug. Her body slightly turned into an S-curve posture, shoulders and neck elongated, legs slightly pushed sideways, legs crossed and elongated. She aimed the coffee pot at the mug on the edge of the table and began pouring coffee. Dark brown coffee liquid flows into the cup. The camera moved a little closer, and the autofocus relocked the cup, making the half-second defocus clear again. The cup was indeed at the very edge of the table, some distance from the keyboard and monitor, and the girl stood on the aisle side and leaned over. 0:06 The girl flipped her head backwards, slowly shifting her eyes away from the cup, looking over the cup at the monitor in front of the boy—she was captivated by the game screen, completely absorbed, her neck slightly leaning forward. His hands were still in a tilted position, the spout was still pouring coffee into the cup, completely forgetting he was working. The coffee gradually spilled over the rim of the cup. 0:09 The coffee flows down the rim of the cup onto the table, spreading a small puddle near the edge of the table, foaming with fine foam and slowly spreading toward the center of the table. The camera gently lowers a bit, making the coffee beach even clearer. Autofocus switches once between the cup rim and the desktop. 0:11 The male lead heard the sound of liquid dripping, slowly turned his head toward the screen, and looked toward the girl at the edge of the table. Her expression was surprised, her brows slightly furrowed, eyes wide open—"What are you doing? The coffee spilled." The camera zooms back a bit: the male lead's profile, the coffee beach at the edge of the table, and the girl are all in the frame. 0:13 The coffee was still spilling out, dripping two drops down the corner of the table. The girl was still staring at the screen, still in shock, holding the teapot. The male lead continued to look at her, his expression shifting from confusion to speechlessness. The scene ends here, with the first segment ending at the moment when the girl is still in shock. Real-time speed throughout the process. Handheld slight shaking runs through. Autofocus occasionally searches for half a second. The white balance leans cool blue near the monitor, returning to warm white when away. The ambient sounds continue. No music, no special effects, no subtitles. Act Two: Continuing from the previous segment. The same handheld shooting style as the iPhone: fully automatic, realistic handheld texture, no post-processing, no color grading, no special effects. Handheld slight shake, breathing sensation, occasional autofocus search out-of-focus, natural fine-tuning of white balance, flat image with slight edge chromatic aberration and motion blur. Natural ambient sounds run through. 0:00 (Continuing from the previous 13-second segment July 19 (1) ) Girls Clothing Image_20260719093342_1234_183 finally took his eyes off the screen and looked down—the coffee had already spilled over half the table, dripping down the corner. Her eyes widened instantly, and she panicked. I hurriedly put the coffee pot back and placed it on the ground nearby (there was no room on the table), my movements a bit chaotic, and my arm rubbed against the back of the chair. The camera flickered with her movement, autofocus briefly lost focus for half a second, then locked back onto her face. 0:02 She froze for a second, staring at the pile of coffee and the still-bubbling cup on the table, at a loss. Looking around, there were no tissues on the table. The camera stopped, and the breathing movements in her hand were clearly visible. In the background, the sound of keyboards came intermittently in the distance. 0:03 She took a deep breath and made a ridiculous decision—she bent over, brought her face close to the coffee puddle at the edge of the table, and actually pouted to suck the foam on the coffee's surface. He sucked quickly, his instinctive reaction in desperation, completely ignoring his image. Because the cup was on the edge of the table, her bent posture was especially awkward, one hand holding onto the edge of the table. The camera followed down for a moment, then shook—even the person filming it was startled and trembled. The male lead's profile is on the right side of the frame, his whole body frozen, his eyes wide open as if he's seen something he shouldn't have. 0:06 After the girl finishes sucking, she straightens her waist. His mouth was full of coffee foam, and there was a ring of brown marks at the corners of his mouth. She looked up at the male lead, who was playing a computer game hf_20260702_115248_424b92a4-ca6f-401a-baa3-709ae4b60581 。 The camera moved up a bit, and the two stared at each other across the table. Autofocus hesitated slightly between the two faces. 0:07 The male lead is expressionless on the front but his gaze is extremely complicated—shocked, speechless, confused, wanting to laugh but unable to, all emotions mixed into one face. He tilted his head slightly, as if trying to confirm whether what he had just seen was real. The two looked at each other. The air froze for half a second. In the background, the faint shouting of someone playing a game could be heard in the distance. 0:09 The girl's expression shifted from embarrassment to giving up. She bent down again, moved over the mug still on the edge of the table, and spat the coffee she was holding back into the cup with a "puff." The coffee falls back into the cup, creating ripples and small bubbles. The camera shook downward. 0:10 She straightened up, looked up at the male lead, and signaled with her eyes—"...... "I gave it back to you, isn't that enough?" The male lead's mouth was slightly open, completely stunned, completely unsure of how to react, just frozen in his chair. 0:11 The camera zooms out a bit, and the image starts to shake more noticeably—like the person filming is laughing so hard they can't hold their phone steadily. The two of them stared at each other across the table, with the puddle of coffee and half a cup still on the edge of the table. In the background, other customers were still playing games by themselves, completely unaware of what was happening here. 0:11 to 0:11.5 The frame freezes in a trembling moment, then ends. Real-time speed throughout the process. In the last 2 seconds, the handheld shaking increased, and the simulated photographer laughed so hard their hands trembled. Autofocus occasionally causes brief out-of-focus when a girl moves quickly. White balance is naturally fine-tuned according to the character's movements. Ambient sounds: the sound of foam inhaling, the sound of water being spat back into the cup, background noise from a distant internet café, keyboard noise, and finally the faint breathing of the filmer trying to hold back laughter. No music, no special effects, no subtitles.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `21.63s`

---

### 🎬 Volcanic Mine Cart Escape
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10557.jpg" width="480" alt="SD2_10557"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/volcanic-minecart-escape-SD2_10557">🌐 Watch Online</a>

#### 📝 Prompt
```
Inside an old volcanic mine, one explorer is trapped in a runaway mine cart racing through narrow tunnels while molten rock rises below. The mine is dark, dangerous, and unstable, with wooden support beams, old mining rails, glowing lava channels beneath broken sections, steam vents, falling rocks, sparks, dust, and orange firelight reflecting on the tunnel walls. Wide opening shot: the mine cart speeds through the tunnel at high speed, shaking violently on the old rails. The explorer grips the cart edges while the tunnel trembles and molten light glows from cracks in the ground below. Tracking shot: the cart races past wooden beams and narrow rock walls. Steam bursts from side vents, small rocks fall from above, and the rails bend slightly as the cart rushes deeper into the mine. Side shot: the tunnel opens over a wide lava chamber. The mine cart crosses a damaged rail bridge above glowing molten rock. Sections of the bridge shake and break behind the cart as lava surges upward below. Final 5 seconds: the action becomes extreme. The track ahead is partially broken. The cart accelerates down a steep slope, jumps a missing section of rail over the lava, lands hard back on the track, sparks flying from the wheels, then races toward a bright exit tunnel as the mine collapses behind. Final moment: the mine cart bursts out of the tunnel into open air near the volcano slope while smoke, sparks, and orange lava glow explode from the mine entrance behind. Style: hyper-realistic, cinematic, fast-paced, intense, stressful, clear readable action, strong sense of speed and danger, old volcanic mine, runaway mine cart, glowing lava below, steam, sparks, falling rocks, dynamic but readable camera movement, no text, no logos, no cartoon style, no slow motion, no famous celebrity faces, no recognizable actors, no movie-star resemblance, no public-figure likenesses, no clear facial close-ups. Keep proportions. Keep style and features. Aspect ratio 16:9.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

### 🎬 Chibi Haaland Makes Kimchi Pixar Style
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10556.jpg" width="480" alt="SD2_10556"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/chibi-haaland-kimchi-pixar-SD2_10556">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-cinematic Pixar-style 3D animation, adorable chibi version of Erling Haaland with long blond ponytail, fair skin, rosy cheeks, expressive blue eyes, wearing a red long-sleeve shirt, navy apron, pink rubber gloves, and a white hairnet, traditional Korean hanok courtyard, warm autumn afternoon sunlight, authentic kimchi-making station, ultra-detailed vegetables, realistic food textures, cozy atmosphere, shallow depth of field, HDR, 8K, one continuous sequence. The scene opens with the adorable chibi football star standing behind a large wooden bowl filled with freshly seasoned napa cabbage. Around him are baskets of fresh napa cabbage, green onions, garlic, ginger, red chili flakes, and traditional Korean earthenware jars. He enthusiastically mixes the kimchi seasoning by hand, folding every cabbage leaf carefully with exaggerated cute movements while smiling. The camera slowly circles around him as he continues preparing the kimchi with genuine curiosity. His ponytail gently sways in the breeze while sunlight creates soft highlights across the courtyard. Every ingredient appears vibrant and highly detailed with realistic textures. Curious about the flavor, he picks up a freshly seasoned piece of kimchi and carefully brings it toward his mouth. The camera cuts to an intimate close-up as he takes his first bite. His eyes widen in surprise from the spicy kick, cheeks puff slightly, eyebrows lift, and he freezes for a brief moment while processing the intense flavor. A second later, his expression transforms into pure delight. He smiles broadly, his eyes sparkle with excitement, and he happily nods in approval. He laughs warmly while pointing at the kimchi as if telling everyone how delicious it is. The camera pulls back to reveal the beautiful traditional courtyard filled with earthenware jars and colorful ingredients. He proudly places both hands on his hips, then raises one gloved hand with a cheerful thumbs-up toward the camera, beaming with satisfaction. Style: Pixar-quality 3D animation, ultra-realistic food rendering, cinematic storytelling, wholesome, cozy Korean cultural atmosphere, expressive facial animation, physically accurate lighting, smooth camera movement, premium animated commercial, masterpiece, vibrant colors, ultra-detailed textures, 8K HDR.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.1s`

---

### 🎬 Ink Tears Into Swallows
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10555.jpg" width="480" alt="SD2_10555"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ink-tears-swallow-sky-SD2_10555">🌐 Watch Online</a>

#### 📝 Prompt
```
Monochromatic black-and-white manga aesthetic, rough ink sketch animation, 2D anime style, high contrast, moody, cinematic, and atmospheric. ​Scene 1 (Setup): Close-up profile of a young anime girl with short dark hair smoking a cigarette. She wears a dark, oversized hoodie. She is standing on a bleak rooftop balcony. ​Scene 2 (Interaction): A young anime boy with a scuffed, bruised face and messy dark hair approaches her. He is wearing a two-toned hoodie. Close-up on their hands as he takes the cigarette from her. He speaks to her with a frustrated, intense expression. ​Scene 3 (Emotion): Close-up on the girl's face. She looks stoic, then sheds a single tear. As the boy leans in close to her face, she gives a faint, gentle smile. ​Scene 4 (Surreal Transformation): The girl suddenly dissolves into abstract black ink splatters and transforms into a silhouette of a swallow. The bird flies away off the rooftop, joining a flock of birds in the pale, overcast sky above brutalist apartment buildings.
```

#### 📌 Details
- Ratio: `1.77` | Duration: `42.77s`

---

### 🎬 Weekend Courtyard Cleaning Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10554.jpg" width="480" alt="SD2_10554"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/weekend-courtyard-cleaning-SD2_10554">🌐 Watch Online</a>

#### 📝 Prompt
```
Main Subject: Young Korean woman, early 20s, natural everyday appearance, faded charcoal-grey sleeveless crop top, loose high-waisted light-wash jeans, black canvas sneakers, black cord necklace, black wavy hair in a messy side ponytail with wispy bangs. Realistic skin texture, minimal makeup, warm and approachable personality. Maintain identical identity, clothing, hairstyle, and appearance throughout. Weekend Cleaning Location: Small Korean home courtyard. 00:00–00:03 She sweeps fallen leaves from the concrete. 00:03–00:06 Camera accidentally frames only half of her while autofocus hunts. 00:06–00:09 She waters potted plants. 00:09–00:12 She wipes sweat from her forehead and laughs. 00:12–00:15 She carries the watering can inside as recording abruptly ends.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Shy Lovers Under Cherry Tree
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10553.jpg" width="480" alt="SD2_10553"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cherry-tree-shy-lovers-SD2_10553">🌐 Watch Online</a>

#### 📝 Prompt
```
No background music or subtitles. A scene where both the [female character] and [male character] are leaning toward the same cherry tree as shown in the [background image]. The [male character] leans on the right side of the tree, and the [female character] leans on the left side of the tree. Although they are in positions invisible to each other, it feels like they are watching each other with concern for each other. The cherry blossoms are in full bloom, with petals fluttering down. The two shy people glanced at each other's faces nervously, looking nervously.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Hongdae Street Style And Tattoo Tour
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10552.jpg" width="480" alt="SD2_10552"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/hongdae-tattoo-street-tour-SD2_10552">🌐 Watch Online</a>

#### 📝 Prompt
```
Character Consistency: The subject is the young male influencer from the reference image @Image 1. In every time period and from every angle, the face shape, facial features, and skin tone must match @Image 1 exactly. Do not alter or distort the face. Outfit: In every scene, wear stylish and luxurious black casual, streetwear, or suit outfits. Do not wear the outfit from the character reference sheet. Completely change the outfit and hairstyle for each segment. Format: 9:16 vertical. Camera / Style: Fast editing rhythm with cuts every 0.5 to 1 second. iPhone handheld vertical shooting texture. Mix digital zoom in, zoom out, and tilt up, with natural camera shake. Include autofocus hunting, indoor and outdoor lighting exposure changes, and image quality degradation during zoom adjustments. Preserve real skin texture including pores, beard shadow, flyaway hairs, and natural skin oil. Do not use beauty filters, excessive skin retouching, CGI textures, or cinematic color grading. Do not merge cuts or omit scenes. Do not insert on screen text. Sound: Trendy hip hop or R&B background music mixed with natural environmental sounds such as street noise, footsteps, and everyday ambient sounds. --- M-01. Hongdae Busking Street & Tattoo Shop Tour 0 to 2 seconds: [Hongdae Walking Street] A low angle shot holding a selfie stick high above while quickly spinning to capture both yourself and the crowd in the middle of a busy busking street. 2 to 4 seconds: [Tattoo Shop Waiting Room] A tight shot pointing at the tattoo designs hanging on the wall with your finger, followed by a quick transition to your face looking at the camera while lightly biting your lip with a slightly nervous expression. 4 to 6 seconds: [Tattoo Workstation] A forearm shot rolling up the sleeve of an oversized black T shirt, rapidly cross edited with a shot of your face smiling while enduring the pain. 6 to 8 seconds: [In Front of the Shop Mirror] A tight shot checking the linework of the newly completed tattoo in the mirror, followed by your face making eye contact with the camera through the mirror and nodding with satisfaction. 8 to 10 seconds: [Hongdae Alley] A close up taking one bite of a street waffle, then blowing on it because it is hot while smiling at the camera. 10 to 12 seconds: [Select Shop Hallway] A handheld tracking shot from behind as you walk slowly with a shopping bag over one shoulder. The screen naturally shakes in sync with your footsteps. 12 to 15 seconds: [Hongdae Station Entrance] In front of the station exit, playfully extend your fiste toward the camera in a fist bump pose. End with a front facing full body shot frozen on the final frame.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.1s`

---

### 🎬 Sunny Park Family Picnic
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10551.jpg" width="480" alt="SD2_10551"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sunny-park-family-picnic-SD2_10551">🌐 Watch Online</a>

#### 📝 Prompt
```
Super casual real smartphone home video footage, family reunion picnic in a sunny park, natural mobile phone camera with slight authentic handheld shake, normal frame rate with smooth natural motion, rapidfire montage with quick jump cuts every 1-2 seconds, unpolished authentic phone recording of mixed ages spreading picnic mats, eating and playing games, pure raw home video feel, no cinematic polish. Use the provided reference photo as the strict ONLY visual reference for the main woman. Maintain her exact appearance with zero deviation. Generate a mixed group of family members of all ages around her in the park, picnic mats and food spread visible. 0-2.5s: Shaky rapid cuts main woman laughing while setting up the picnic mat, sunny park background. 2.5-5s: Abrupt jump cuts close-up of her smiling while eating a sandwich, then family passing fruits and snacks. 5-7.5s: Fast shaky she chats animatedly with cousins, kids playing in the background, grandparents seated nearby. 7.5-10s: Quick cut close-up cheerful smile toward camera, then jump to her laughing during a light game with family. 10-12.5s: Abrupt edit group gathered around the picnic spread, mixed ages eating and laughing together. 12.5-15s: Final rapid transition main woman relaxed on the mat with family, soft smile, calm park memory ending with gentle phone sway. Natural smartphone video quality, slight handheld shake, smooth motion, authentic physics, stable main character consistency, no pro effects.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

### 🎬 Idol Pepero Game Tension
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10549.jpg" width="480" alt="SD2_10549"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/idol-pepero-game-tension-SD2_10549">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: 8K. Photorealistic — no 3D render, no game engine. Korean idol variety self-content aesthetic with a glam music-video mood — playful romantic tension, kiss-that-never-happens energy, always tasteful. Lighting: Warm and moody, dimmer than standard broadcast — soft warm key from frame-left, glowing string-light bokeh and a soft neon wash in the background, gentle amber rim light tracing hair and cheekbones, faces always cleanly lit. Color: 60:30:10 — dusty rose and mauve dominant / deep plum shadow secondary / red Pepero box and warm neon accent. Broadcast graphics: Persistent variety-show overlay locked to screen corners across every cut — a round pastel-pink "MELLOW GIRLS" show logo badge pinned top-left, and a title graphic pinned top-right reading exactly "PEPERO GAME", spelled P-E-P-E-R-O with one single P in the middle of the word — NOT "PEPPERO", NOT double P. Overlays never drift, never distort, letters never change between cuts. No subtitles, no lower-thirds. Props: The Pepero stick is MATCHSTICK-THIN — a delicate biscuit stick as thin as a wooden matchstick or a cotton-swab stem, about 2-3mm in diameter and 14cm long, with a whisper-thin chocolate coating, exactly matching the attached real Pepero product reference photo. Scale rule: the stick is always dramatically thinner than a person's lips are tall — a hair-thin line compared to the faces around it. It is NEVER a thick bar, never cigar-thick, never pencil-thick — if in doubt, make it thinner. The red Pepero box is a small light carton the size of a smartphone, held in one hand — it always looks small in a hand. Dialogue: Any spoken words are KOREAN ONLY — short natural Korean exclamations like "대박!", "어떡해!", "미쳤어!". Never any English words spoken. Camera: Physical broadcast cine lens. 180° shutter motion blur. Skin: Pore-level realism — vellus hair, glossy idol makeup, pore-shadow matching set light. Skin tone stays CONSTANT from first frame to last — no blushing, no reddening of cheeks or ears, no color change on any face at any point. Acting: Charged restraint — slow blinks, lidded eyes, gazes that drop from eyes to lips and back, breath held then released, a swallow before a move, suppressed smiles. The tension of almost — never a kiss, never contact between lips. Characters never frozen, always breathing and reacting. Physics: Gravity and inertia respected — the thin stick flexes slightly and snaps cleanly like a real biscuit, correct bite marks, tiny crumbs fall naturally. No floating props. Composition: Rule of thirds + golden ratio. Every person moving from frame one. Continuity: Characters, wardrobe, props, environment identical across every cut. No identity drift. Technical: 24fps smooth motion. 8K detail. No jitter. Audio: Room tone and close breathy foreground in the tense cuts — but from the moment the game starts, the two spectators keep up a constant excited high-pitched squealing off-screen ("꺄아—!", "꺄악!"), bubbling under every cut, rising with every bite, choking into whispers at the climax. Korean chatter, the crisp dry snap of the biscuit stick. No music. No subtitles. Characters: YURI — the group's eldest (unnie). Long platinum-blonde hair with wispy see-through bangs, pale porcelain skin, cool deadpan resting face. Cream cable-knit sweater vest over a white long-sleeve shirt, navy sailor collar with double white stripes, navy tie, pleated denim mini skirt, slouchy white loose socks, black loafers. RENA — younger than YURI. Long jet-black straight hair, sharp elegant features, pearl drop earrings. Black ribbed knit top with a wide pointed knit collar and thin black ribbon tie over a peeking white shirt collar, black pleated micro skirt with a small side buckle, black crew socks, chunky black loafers. HAEIN — long pastel ice-blue hair with a faint lavender sheen, glossy coral lips. Mustard-yellow double-breasted cropped blazer with navy trim, big navy bow ribbon at the collar, mustard sweater underneath, navy pleated skirt, white socks, white sneakers. MEMBER 4 — long black hair with soft face-framing layers, warm bright smile. Sleeveless green-and-white striped ribbed knit top with an orange-striped high neck and a small white triangle badge, light-blue wide-leg jeans, white sneakers. Scene: A moody glam lounge set — a dusty-rose velvet drape backdrop with a soft glowing neon squiggle sign, strings of warm fairy lights hanging out of focus, a tall arrangement of pale roses and pampas grass at frame-left, warm haze in the air. No table — everyone is STANDING. YURI and RENA stand face to face at center frame in profile to camera, barely a forearm's length apart, one matchstick-thin chocolate-dipped Pepero stick bridging their mouths, each end barely gripped between front teeth. HAEIN and MEMBER 4 stand a step behind at frame-right, shoulder to shoulder; HAEIN holds the small red Pepero box in one hand, forgotten. The broadcast overlays sit locked in the top-left and top-right corners throughout. CUT 1 — Wide static, 35mm, eye-level, locked off: The face-off. YURI and RENA stand toe to toe in the warm neon glow, the matchstick-thin stick a delicate line between their profiles. RENA tucks a strand of black hair behind her ear without breaking eye contact. YURI's chin lifts a degree — silent challenge. Behind them HAEIN grips MEMBER 4's arm with her free hand, both leaning in; MEMBER 4 whispers "어떡해…". Off-screen someone breathes "시작…" — the first slow bites begin. CUT 2 — Over-the-shoulder, 50mm, slow push-in over RENA's shoulder onto YURI: Framed past RENA's black hair, YURI takes one slow bite, then another — unhurried, deliberate. Her lidded eyes hold RENA's, then drop for half a second to RENA's lips, then come back up. The stick shortens. Her cool deadpan stays intact but her fingers slowly curl into the hem of her knit vest, betraying her. Shallow focus, warm bokeh blooming behind her. Her breathing is close-mic in the foreground while the spectators' high-pitched squeals bubble continuously off-screen — "꺄아—!" — climbing a note with every bite. CUT 3 — Reverse over-the-shoulder, 50mm, slow push-in over YURI's shoulder onto RENA: Mirror framing past YURI's platinum hair. RENA's answer: she bites in slowly, closing the distance, head tilting to the angle of a kiss. More than half the stick is gone. Her hands stay clasped neatly behind her back — the well-mannered posture of the younger member toward her unnie — which makes the boldness of her bite land twice as hard. One eyebrow lifts a millimeter. Off-screen HAEIN's high strangled "꺄악—!", hands presumably over her mouth, MEMBER 4's giddy stomping heard under it. CUT 4 — Tight profile close-up, 85mm, static, shallow depth of field — the almost-kiss: Both faces in full profile fill the frame — noses, lips, chins all visible for scale. Only TWO OR THREE CENTIMETERS of the matchstick-thin stick remain, and their noses are about to collide — the stick can't get any shorter head-on. Then the move the fans are waiting for: RENA slowly TILTS her head to one side, her nose sliding past YURI's nose instead of bumping it, faces now interlocking at the kiss angle — and the blocked final centimeter opens up. She nibbles in again, millimeter by millimeter, the stub shrinking shorter than seemed possible, until their lips are a single warm breath apart, offset and almost overlapping. Lidded eyes gone slightly cross-eyed at this distance. YURI's answer: her hands rise and take a firm, gentle hold of BOTH of RENA's shoulders — the unnie steadying her challenger, half embrace, half "I'm not losing." She swallows but holds her ground. RENA's breath audibly trembles on the exhale — the composed one cracking first. A long held beat, the tiny stub trembling between two suppressed smiles. Off-screen a whispered "미쳤어…". CUT 5 — Handheld wide, 24mm, whip in from the spectators: At the closest possible moment the tiny stub SNAPS with a crisp dry crack. The spell breaks
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 Crane Drop Crushes Alien on Deck
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10547.jpg" width="480" alt="SD2_10547"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/crane-drop-alien-deck-SD2_10547">🌐 Watch Online</a>

#### 📝 Prompt
```
LOCATION: A massive container port at golden-hour daylight, a giant container ship moored at the dock, towering gantry cranes overhead, stacked containers in colored walls, a 40-ton container hanging mid-lift over the ship's open cargo bays, harbor water glinting between hulls. Shot 1 (0–3s) — THE HOOK: Tracking shot along the ship's deck. A brownish-black slimy tentacled alien, big as a truck, heaves up over the ship's rail and coils a tentacle around a lashing worker on deck, dragging him across the hatch covers as he grabs at container lock bars, boots skidding. He screams into his radio: "IT'S ON THE DECK! IT CAME OUT OF THE WATER!" Shot 2 (3–6s): High shot from the gantry crane cab. The crane driver, already lowering a 40-ton container into the next bay, hands on the hoist levers, looks down at the creature hauling the worker directly through his drop zone. His eyes measure the line. Into the radio: "THERE'S AN OPEN HATCH RIGHT BESIDE YOU — GET DOWN IT! I'VE GOT FORTY TONS WAITING!" Shot 3 (6–9s): Handheld on deck. The worker rips a lock bar free and jams it into the tentacle — black slime bursts out, the grip breaks — and he drops feet-first down the open hatch, slamming it shut over his head. The alien rears up over the closed hatch, tentacles spread across the deck, screeching — dead center in the drop zone. Shot 4 (9–13s) — BULLET TIME PAYOFF: The driver punches the emergency release. Bullet time — the 40-ton container plummets from full height in slow motion, cables whipping upward, dust curling off its edges — and pile-drives the alien straight through the deck plating, steel petals folding inward as container and creature punch down into the ship's fuel bunker. Impact. A fireball erupts up out of the hold, blowing hatch covers spinning into the air. Shot 5 (13–15s): Time snaps back. Flame and black smoke boil out of the ship's torn deck, alarms howling across the port, the crane cab rocking on its rails above the burning hold.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.84s`

---

### 🎬 Centipede Bridge Attack
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10545.jpg" width="480" alt="SD2_10545"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/centipede-bridge-attack-SD2_10545">🌐 Watch Online</a>

#### 📝 Prompt
```
A wide concrete river bridge at noon, brown water rushing below. A military supply truck rolls across the bridge. The driver is a young soldier in green uniform, short hair, dust on his face. Beside the bridge, a posted gunner stands on a flat patrol boat tied to the bank — rocket launcher already on his shoulder, eyes scanning. Then the centipede erupts from under the bridge. It is train-long, dark brown with a yellow belly, a hundred hooked black legs clawing stone. Its front claws seize the truck hood and crush it down. Sound: metal screaming, legs scraping concrete, water churning, truck horn blasting, diesel engine grinding. Shot 1 (0–3s) — THE HOOK: The centipede's front half is already wrapped over the truck, legs punching through the steel roof. The driver slams the brakes. The truck skids sideways on the bridge. The gunner on the patrol boat below SNAPS to the sight on his launcher. He is ready. Shot 2 (3–6s): The truck tilts. A hooked leg punches through the door glass. The driver shouts — "It's got my truck!" He kicks the passenger door open hard. He crawls out onto the bridge railing. Shot 3 (6–9s): The driver drops off the railing and lands on a concrete support ledge below the bridge deck. He rolls clear, pressed against stone. The centipede drags the empty truck sideways. Its full body is now out in open air above the bridge — every leg exposed, every segment visible, nothing around it. Shot 4 (9–13s) — BIG SLOW-MOTION MOMENT: SLOW. The gunner on the boat exhales. His finger curls. He pulls the trigger. The rocket fires — white smoke blasts back across the water. The rocket crosses the air in bullet time, spinning straight toward the centipede's centre mass. Shot 5 (13–15s): The rocket hits. The centipede DETONATES — massive yellow-orange fireball, legs blasting outward in every direction, the truck flipping off the bridge into the river. The bridge shakes. Fire rolls into the sky.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.04s`

---

### 🎬 Avalanche Cannon Destroys Alien Monster
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10544.jpg" width="480" alt="SD2_10544"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/avalanche-cannon-alien-SD2_10544">🌐 Watch Online</a>

#### 📝 Prompt
```
LOCATION: A high mountain ski station at night under harsh floodlights, heavy snowfall, a steep white slope rising above the station, a snowcat with spinning orange beacons stalled mid-slope, an avalanche control post with a mounted gas cannon on the ridge above, a fuel depot at the cliff base below. Shot 1 (0–3s) — THE HOOK: Tracking shot through driving snow. A brownish-black slimy tentacled alien, big as a truck, is wrapped around the stalled snowcat, tentacles coiling through the cab windows and crushing the roof as the trapped driver kicks at the glass. Steam pours off the creature's hide in the cold. The driver screams into his radio: "IT'S CRUSHING THE CAB! GET IT OFF ME!" Shot 2 (3–6s): Up at the avalanche control post. The control officer, parka hood up, already loading his slope-clearing gas cannon for the night's routine blast, swings the barrel down toward the snowcat's beacons. His eyes track up the loaded slope hanging above the creature. Into his radio: "REAR HATCH! CRAWL OUT THE BACK! I'VE GOT A WHOLE MOUNTAIN FOR IT!" Shot 3 (6–9s): Handheld inside the snowcat. The driver kicks the rear hatch open and drags himself out into the snow, a tentacle snatching his boot off as he rolls away and slides downslope behind a rock outcrop. The alien heaves itself fully on top of the crushed snowcat, tentacles spread, screeching into the storm. Shot 4 (9–13s) — BULLET TIME PAYOFF: The officer fires the cannon into the slope above. Bullet time — the charge detonates and the entire snowfield releases in slow motion, a mile-wide white wall thundering down through the floodlight beams, snow boulders suspended mid-tumble — slamming into the alien and snowcat together, ripping them off the slope and over the cliff edge, straight down onto the fuel depot below. Impact. A massive fireball punches up through the falling snow. Shot 5 (13–15s): Time snaps back. Orange firelight flickers across the settling avalanche cloud, the driver rising from behind the rock, staring down at the burning depot as snow keeps falling.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.84s`

---

### 🎬 Dragon Doesn't Want Knight
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10543.jpg" width="480" alt="SD2_10543"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dragon-doesnt-want-knight-SD2_10543">🌐 Watch Online</a>

#### 📝 Prompt
```
The Dragon Doesn't Want a Knight (60 Seconds) Ultra-high-quality 3D animated fantasy film, DreamWorks/Pixar-level animation, cinematic storytelling, rich medieval fantasy world, highly expressive facial animation, lush forests, ancient moss-covered mountains, warm volumetric lighting, magical atmosphere, realistic fire, detailed dragon scales, cinematic depth of field, dynamic camera movement, smooth transitions, emotional comedy, orchestral fantasy score, 4K HDR, vibrant colors. Characters: Knight: Young, determined but inexperienced, around 20 years old. Polished silver armor with a royal blue cape, expressive face, messy brown hair, slightly awkward but brave. Dragon: Enormous emerald-green dragon with glowing amber eyes, large horns, weathered scales, intimidating appearance but surprisingly gentle and sarcastic personality. Deep, warm voice. PART 1 (0:00–0:15) — The Hero Arrives 0:00–0:05 Camera: Epic aerial drone shot soaring above mist-covered mountains at sunrise. The camera dives toward an ancient cave carved into a towering cliff. Smoke lazily drifts from the entrance as birds scatter into the sky. Action: A lone knight climbs the rocky trail with determination, gripping his sword tightly while his blue cape billows dramatically in the wind. Audio: Grand orchestral score builds with distant dragon roars echoing through the valley. 0:05–0:10 Camera: Low-angle tracking shot following behind the knight as he enters the cave. The environment grows darker, illuminated only by glowing lava cracks and shafts of sunlight breaking through the ceiling. Action: He stops, raises his sword toward the darkness, and takes a deep breath. Knight (shouting heroically): "Fear me, beast! I've come to slay the dragon!" 0:10–0:15 Camera: Slow cinematic dolly through the darkness until an enormous emerald dragon is revealed sleeping peacefully atop a mountain of treasure. Close-up on one sleepy amber eye opening as it lets out a massive yawn, releasing a tiny puff of fire. Dragon (half asleep): "...Can you come back tomorrow?" The knight freezes in complete confusion. PART 2 (0:15–0:30) — The Most Tired Dragon 0:15–0:20 Camera: Medium two-shot. The knight awkwardly lowers his sword while the dragon stretches lazily, scratching behind one horn. Dragon (with a sigh): "I'm exhausted." The epic music abruptly stops, leaving only awkward silence. Knight: "...Wait... what?" 0:20–0:25 Camera: Slow pan across the cave, revealing piles of broken swords, shattered shields, cracked armor, and bent spears stacked in one corner. Dragon (casually): "I've had six knights this week." 0:25–0:30 Camera: Close-up of the dragon rolling its eyes. Dragon: "None of them even introduced themselves." A tiny baby dragon peeks out from behind a treasure chest, gives the knight a cheerful little wave, then quickly hides again. The knight blinks, completely speechless. PART 3 (0:30–0:45) — The Truth 0:30–0:35 Camera: Slow push-in on the knight as he relaxes and carefully places his sword on the ground. Knight: "...So..." "What do you actually want?" 0:35–0:40 Camera: Close-up on the dragon's face. Its playful smile fades as it gazes toward the cave entrance, where golden evening light shines across the valley. A long, quiet pause. 0:40–0:45 Camera: Extreme close-up of the dragon's eyes. Dragon (softly): "Honestly..." Small pause. "...A friend." The soundtrack shifts into a gentle piano melody. PART 4 (0:45–1:00) — A Different Kind of Victory 0:45–0:50 Camera: Warm montage with smooth cinematic transitions. The knight and dragon sit beside a campfire inside the cave. The dragon carefully roasts marshmallows using tiny controlled flames. Knight (laughing): "This wasn't in knight school." Dragon (smiling): "Neither was loneliness." 0:50–0:55 Camera: Wide shot outside the cave. The King leads hundreds of armored soldiers charging up the mountain, banners waving and dust rising beneath galloping horses. King (shouting): "Did you defeat the dragon?" 0:55–1:00 Camera: Heroic medium shot of the knight standing beside the dragon at the cave entrance. The dragon nervously peeks from behind him. The knight smiles. Knight: "No." A brief pause. "...I met him." Final Camera: The camera slowly cranes upward, revealing the knight and dragon standing together against the glowing sunset as the music reaches an emotional crescendo. Fade to Black.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `60.25s`

---

<!-- STATS_END -->
