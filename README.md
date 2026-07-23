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
- Total Prompts: **8256**
- Updated Today (UTC 2026-07-23): **78**

## 🎬 Today's Updates
### 🎬 Dragon Rider: Unbroken Siege
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10656.jpg" width="480" alt="SD2_10656"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dragon-rider-unbroken-siege-SD2_10656">🌐 Watch Online</a>

#### 📝 Prompt
```
A single uninterrupted cinematic action sequence. No cuts. No scene transitions. One continuous camera movement from beginning to end. The film begins high above an enormous medieval mountain fortress at sunrise. Thick morning fog rolls through the valley below while hundreds of banners wave from towering stone walls. Thousands of soldiers prepare for battle as siege weapons line the ramparts. The camera dives rapidly toward the main gate. Suddenly— A deafening roar echoes across the mountains. Three colossal dragons burst through the clouds. The lead dragon unleashes a torrent of blazing fire across the outer wall. Massive explosions tear through stone towers. Flaming debris rains across the battlefield as soldiers scatter. The camera races through the collapsing gateway. An elite knight wearing beautifully crafted black steel armor charges forward on horseback through the burning fortress. The camera follows only a few meters behind. Arrows rain from above. The knight lowers their shield, deflecting dozens of arrows while galloping through collapsing streets. Burning timber crashes onto the road behind, narrowly missing both horse and camera. The horse leaps over a shattered bridge as molten debris crashes into the river below. Without slowing, enemy warriors block the path. The knight performs a rapid mounted sword strike, clearing the way while maintaining full speed. The camera swings smoothly around the action without interruption. Ahead, a gigantic dragon lands directly in the castle courtyard. Its wings create a hurricane-force shockwave that throws burning debris across the fortress. The horse cannot stop. At the last possible moment the knight leaps from the saddle directly onto the dragon's back. The horse continues safely beneath while the dragon launches into the sky. The camera follows the impossible leap in one seamless movement. Now hundreds of meters above the battlefield, the knight struggles to maintain balance while climbing toward the dragon's neck. The dragon twists violently through the air between collapsing castle towers. Another dragon attacks from behind. The two enormous creatures collide midair. Fire erupts around them. Stone towers explode beneath. The knight jumps from one dragon to the other while flames fill the frame. The camera rotates gracefully around the airborne battle without losing orientation. The victorious dragon crashes onto the highest castle tower. The knight slides down one massive horn and lands perfectly on the ancient stone rooftop. Behind them, the defeated dragon falls into the valley, creating an enormous cloud of dust. The surviving dragon spreads its wings and roars toward the rising sun. The knight slowly stands, sword raised toward the sky. The camera pulls backward and upward, revealing the burning fortress, the battlefield below, and the dragon perched atop the castle. The first rays of sunrise break through the smoke.
```

#### 📌 Details
- Ratio: `0.57` | Duration: `15.13s`

---

### 🎬 Sky City Axe Battle
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10655.jpg" width="480" alt="SD2_10655"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sky-city-axe-battle-SD2_10655">🌐 Watch Online</a>

#### 📝 Prompt
```
[Worldview] Set in a nighttime sky magic city, this is a cinematic high-speed aerial interception action. Set in a floating city covered by an airway network, a single character in the reference image wields a large air patrol rescue axe and a single ether wire to annihilate five small black demon dragons attacking through the air with three-dimensional maneuvers. High-density 3D toon/cell look. Seamlessly connects falling, pendulum acceleration, aerial interception, pivot change, rooftop landing, and re-acceleration. Rather than a berserker, you eliminate enemies as a calm and skilled air route mechanic and rescue fighter, using controlled maneuvers and weighty axe strikes. [Use of Reference Images] Reference images refer to the characters in the source image and maintain the same character throughout the entire story. Reference images are used only for the character's face, eye shape, irises, hairstyle, hair color, costume, decorations, physique, overall silhouette, atmosphere, and character color. Do not reproduce the background, room, furniture, props, text, poses, angles, framing, or static compositions of the reference image itself. Only facial expressions, gazes, mouths, poses, breathing, natural hair and costume movements may change. Face-leveling, feature mixing, hairstyle changes, costume swaps, alienation, infantilization, clones, clones, and a second person are prohibited. [Character Adaptation] The basic structure of the background, axes, enemies, and actions is fixed. Lighting, auxiliary light, magic particles, axe glow, wire glow, slash light, edge light, reflective colors only, and the main colors, secondary colors, and atmosphere of the reference character are harmonized. For warm-colored characters, enhance gold, amber, and red-orange; for cool-colored characters, enhance blue-white, pale blue, purple, and silver. However, the overall night scene should be kept low-saturation and not overly diffuse the character's color across the background. If there are unique decorations or textures in the costume, they are retained, and colors are modestly reflected in surrounding floating lights, floor reflections, and magical particles. The shape of the axe and the structure of the Sky City remain unchanged. [Weapon and Wire Fixing] The only weapon is a single airborne rescue axe. Long handle, dark navy grip, ivory and gold metal armor, pale light blue translucent large blade, golden star chart pattern on the blade, central circular ether core, fixing spike, red-orange tassels, and anchor-shaped hook on the handle's heel. Do not draw swords, swords, spears, daggers, guns, shields, or spare weapons. Do not duplicate axes. Right hand grips the lower side of the hilt, left hand grips the center and upper side. Do not grip the axe blade, core, or spikes. Only release the wire from the hilt when operating with the left hand; always return it before attacking. Depict the axe as a heavy weapon wielded in coordination with the shoulders, elbows, waist, back, supporting leg, and torso. Small retractable wire mechanism near the left sleeve or left wrist. Fires only one thin ether wire. Completely releases the previous wire and reels it before firing the next shot. [Video Style] High-density 3D toon/cel look. Movie-quality key animation, delicate expressions and body acting, high-quality composites, transparent lighting, and dense background art. Fine colored edge lines, two- to three-tier cel shading, multi-layered highlights. Fabric, metal, gemstones, translucent materials, wet floors, glass, magic metal, and ether crystals are depicted with different reflections. Thick black outlines, single-layer cel shadows, generic 3D beautiful faces, plastic CG, low-density backgrounds, semi-realistic, muted colors, and no mixing of art styles. [Stage] Sky Magic City at Night. Platinum spires, aerial corridors, airship piers, magic rails, viaducts, star chart-patterned metal beams, floating lights, glass connecting bridges, mooring towers, and maintenance scaffolding overlap. After rain, the floor, bridge, railings, and beams are wet, with light mist, humid air, and reflections. The basic light is a warm golden main light. Edge, reflection, and floating particles are adjusted to match the color of the reference character. Do not display readable text, logos, or subtitles. [Enemy] Five small black demon dragons. All are unified by the same kind. Obsidian scales, small reddish-purple eyes, slender tail, sharp wings, faint purple magical light. No humanoid enemies, bloodshed, or unnecessary people. [Effects] The protagonist's glowing color is based on the reference character's color, with incandescent white, gold, and pale auxiliary colors. Enemy collapse consists of black-purple polyhedral fragments, thin reddish-purple magic fragments, and dark gray particles. Just before the attack, local ether pressure gathers around the axe and is released upon hit. At the hit point, there is a high-brightness flash of incandescent light, localized overexposure, colored bloom, volumetric light, radial velocity lines, short lightning flashes, wind pressure, raindrops, and steam blasting. The axe's trajectory is a giant crescent-shaped or slender arc-shaped slashing light. The entire screen is not uniformly white. [Action and Camera] Cut 1: Jump from a high-altitude airway, dropping rapidly between the spire and the corridor. Distance where you can read the face, eyes, hairstyle, and costume. Hair, accessories, and costume hem flow upward by the air current. Five demon dragons appear in the sky ahead. Calmly read the trajectory, shoot a wire from your left wrist onto the metal beam overhead, showing the fixed position. The wire is stretched, the body sinks slightly, then accelerates to a large pendulum trajectory. The camera follows from a low diagonal rear side, showing the background with strong parallax. Cut 2: The first shot enters orbit. Returns left hand to the hilt, uses wire tension to stretch the whole body diagonally, and defeats with a heavy, diagonal downward strike. Incandescent center, character color and golden bloom, crescent-shaped slashing light. Enemies collapse into black-purple fragments, which wipe the foreground. Cut 3: During covering, release the first wire and fully retract it, then shoot a new wire into the support frame beside the opposite spire. Show the fixed position, enter the second pendulum track without losing momentum. The camera also passes through the debris and moves to the opposite side. Cut 4: Of the remaining four, two line up on the track with a front-back difference. Accelerate the axe from behind and defeat two in turn with a single large horizontal sweep. At each hit point, the center of incandescent heat, character color and golden bloom, volume light, speed line, and wind pressure. The two collapse into black-purple magic fragments in turn. The fragments do not overlap on the face. Cut 5: The remaining two scatter up and down. Move to the rooftop edge with the second wire, release the wire, and land on the leading foot. Sink your knees and hips deeply, and your hair, accessories, and costume hem flow slowly, with a short recoil. The camera circles diagonally from the low side to the chest in front, and the character looks at the enemy above, showing a short, determined smile. Cut 6: Supporting the axe with his right hand, he fires a new one from his left wrist toward the elevated bridge in the back. The tension recoils to kick the rooftop hard, then returns his left hand to the handle for re-acceleration. The last two rush forward with a front-back difference. Maintaining the upward momentum, he rotates his body vertically while swinging his axe, then annihilates them with a single vertical spin slash. The contact point becomes the main focus of the video, generating an incandescent center, a massive bloom of character colors and gold, thick volumetric light, radial velocity lines, short flashes, wind pressure, raindrops, and explosive steam blasts. The axe's trajectory is a narrow glowing arc. The two enemies explosively collapse into black-purple polyhedral fragments, reddish-purple magic fragments, and dark gray particles. The protagonist's energy pushes through the enemy's collapse wave. The camera is pushed back slightly by the impact, tilting slightly. Cut 7: Without striking the final pose, she passes straight through the aerial corridor. Her hair, accessories, and costume hem leave strong wind pressure, and the axe blade and circle
```

#### 📌 Details
- Ratio: `1.74` | Duration: `9.08s`

---

### 🎬 Red Carpet Star Moment
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10653.jpg" width="480" alt="SD2_10653"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/red-carpet-star-moment-SD2_10653">🌐 Watch Online</a>

#### 📝 Prompt
```
[See Usage] Reference image: @image1 [Video Requirements] 15 seconds. @image1 Same aspect ratio as . If @image1 is live-action, it has a high-quality live-action movie style; if it's anime or illustration, it maintains the original art style with high-quality animation rendering. Includes BGM. No narration, dialogue, or subtitles. [Main Text] @image1 is used as the final design standard for people, costumes, venues, and giant screens. Facial features, hairstyle, body type, body type, costume, shoes, color scheme, expression style, red carpet venue, and the shape and placement of the giant screen are consistently maintained. Costume colors and venue styles are not fixed in the text; the content of @image1 is inherited as is. From the first frame, the main woman's entire body is clearly visible at the center of the red carpet, and she is already walking toward the camera with a calm, natural pace. The empty venue is shown first, and the main character does not appear. As the main character approaches, the press and audience, flashes, the giant screen, and background music gradually intensify. Even after passing through a person size close to @image1 and a frontal angle at the end, the main character continues walking without stopping, and the camera ends with a shallow bird's-eye wide view. Do not make the camera stand in the finished position from the beginning, nor only slightly move still images. Show the scale of the venue, costumes, upper body, full silhouette, face, and surrounding excitement in short, cinematic shots. Do not use close-up shots of just the feet. [0.0–2.0 sec \| Shallow Wide Overhead View] From the first frame, the main woman's full body is clearly visible in the center at the back of the red carpet, already walking toward the camera. The main character is not placed at the extremely small innermost part but positioned at a distance where both the venue's depth and the presence of the entire body can be confirmed simultaneously. There are no expressions such as unmanned red carpets, mid-stage appearances, fade-ins, pop-ins, warps, or generated appearances. The camera captures the main subject from the start, descending and moving briefly and smoothly from a shallow bird's-eye view. The protagonist does not walk fast, but for the first two seconds, she moves with a calm stride of one or two steps. The sense of closeness and zoom on the screen is created not by the person's acceleration but by switching between the camera's descent, push-in, and next shot. The left and right press responds in turn, and the first flash runs. The giant vision is low-brightness abstract light. [2.0–3.8 seconds \| Waist to Bust] In a diagonal forward mid-close shot, follow from the waist to the shoulders and chest, rising briefly. Make the costume material, drape, accessories, and the line from the neck to the chest appear elegant. Do not overemphasize only the chest. [3.8–5.2 seconds \| Face and Hair] A short skirt above the chest. Clearly shows the main character's expression, eyes, hair flow, and star quality as they walk ahead. Do not use a long face close-up. [5.2–7.4 seconds \| Diagonal Side Full-Body Follow] They follow at the same pace as the main character, showing the full silhouette, leg length, and the flow of hair and costumes. The main character turns his gaze to the press once and continues walking. The flashes on both sides increase irregularly. [7.4–9.2 seconds \| Through the press] The camera is blurry in the foreground and shoulders are placed in front, capturing the main character walking through the gap. The cameraman follows with the lens, the audience turns their face, and several hold up their smartphones. Different reactions occur depending on the distance. [9.2–10.8 seconds \| From diagonal front to front] With a full-body diagonal shot at eye level, you follow the protagonist, moving short sideways at the same speed as the person as you enter the front axis. Here, you don't return to a bird's-eye view. In the giant vision, bands of light, particles, beams, and color fields that harmonize with @image1's costume colors and accent colors spread out. [10.8–12.2 seconds \| Frontal close above the knee] The face, upper body, waist, and walking legs are all captured in a single frame. The main character returns their gaze to the front, showing their expression, hair, costume, and silhouette throughout the body. They start to pull back slightly toward the end, then connect to the final cut with a flash. [12.2–15.0 sec \| Walking Continue, Overhead Wide Finale] Returning to the front and full body, the protagonist does not slow down unnaturally, continuing to advance confidently with a steady walking rhythm. In 12.2 to 13.4 seconds, the person naturally passes through a brief view close to @image1 in size and front angle. However, leg position, posture, and background placement are not fixed to @image1, and no stopping, freezing, or pseudo-freeze are performed. After 13.4 seconds, the camera rises smoothly while keeping the protagonist near the center, then retracts backward to transition to a shallow overhead wide. Without drastically shrinking the main figure, the entire walking body, the long stretch of the red carpet, the left and right reporters and audience, the focused flash, and the giant vision are captured in one grand frame. The abstract light of the giant vision reaches the final color, pattern, and brightness of the @image1, with the shutters and cheers on both sides reaching its peak. The entire frame does not go blank. The protagonist, hair, costumes, audience, light particles, and camera keep moving until the end, ending with lingering echoes during the walk. [Camera & Editing] Shallow overhead wide drop → waist to bust → face and hair → diagonal full-body following from side view → press through the press → diagonal forward to front → knee-length close to the front → shallow overhead wide view rising and retreating from the front full-body. A combination of standard hard cuts and short match cuts using flash is used. Each cut is generally 1.4 to 2.2 seconds, with the final cut lasting 2.8 seconds. Maintain the same person, same costume, same venue, and same direction of movement. Avoid sudden zoom, large turns, extreme wide-angle deformation, full-body slices, and walking axis misalignment. At 1:1, utilize the space on both sides of the venue; at 9:16, make use of vertical red carpet and full-body walking. [BGM & Sound] Elegant and uplifting cinematic fashion BGM. It starts with a low beat, sophisticated strings, and a subtle electronic pulse, then rises in sync with the cut and walk. A 14.0–15.0 second panoramic wide, a massive vision is completed, and it reaches its peak amid the surrounding enthusiasm. Boot sounds, cloth noises, intermittent shutters, restrained cheers, murmurs, and the ambient sounds of the venue are layered. No explosions or excessive electronic sounds are included.
```

#### 📌 Details
- Ratio: `1.0` | Duration: `15.07s`

---

### 🎬 Premium Beach Sunscreen Commercial
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10649.jpg" width="480" alt="SD2_10649"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/premium-beach-sunscreen-commercial-SD2_10649">🌐 Watch Online</a>

#### 📝 Prompt
```
Create an ultra-realistic premium beauty commercial featuring the same young East Asian woman throughout the entire sequence. Maintain identical facial features, shoulder-length soft ash-brown wavy hair, glowing skin, body proportions, and outfit in every shot. She wears a fitted black crop top, black athletic shorts, white sandals, delicate silver jewelry, and sunglasses resting on her head. Bright tropical beach, golden-hour sunlight, crystal-clear ocean, palm trees, premium luxury beauty campaign aesthetic, cinematic camera work, soft warm tones, realistic skin rendering. The video opens with her smiling warmly at the camera while standing barefoot near the shoreline, holding a L'Oréal Paris UV Defender SPF50+ sunscreen beside her face. The bottle catches the golden sunlight as she softly says, "Glow confidently under every sun." A macro hero shot showcases the sunscreen bottle surrounded by sparkling water droplets and seashells. She dispenses a small amount onto her fingertips and gently applies it across her cheeks, nose, forehead, and shoulders. Close-up beauty shots capture the lightweight texture blending seamlessly into her glowing skin. She strolls along the beach while gentle waves wash over her feet. Smooth tracking shots follow her as the ocean breeze naturally moves her hair. She smiles, looks back toward the camera, and enjoys the peaceful atmosphere. She relaxes beneath palm trees, sipping fresh coconut water while chatting and laughing with friends. Warm cinematic shots capture authentic summer moments, glowing skin, and natural expressions. As golden hour approaches, she walks into the shallow waves, playfully splashing water while the sunset reflects across the ocean. Slow-motion close-ups capture sparkling water droplets and beautiful hair movement in the breeze. She sits quietly on the beach watching the sunset before taking one final selfie with the ocean behind her. The warm sunlight highlights her healthy, radiant complexion. Final hero shot: she walks toward the camera holding the L'Oréal Paris UV Defender SPF50+ bottle confidently beside her face. She smiles and says, "Beautiful skin starts with protection." The camera slowly pulls back to reveal the glowing beach, ocean waves, palm trees, and the golden sunset while the product remains the focal point. Natural ambient audio only: ocean waves, gentle breeze, birds, footsteps on sand, distant beach ambience, water splashes, coconut opening, laughter, leaves rustling. No background music, no subtitles, no logos, no watermarks, and no on-screen text. Premium luxury beauty cinematography, ultra-realistic skin texture, physically accurate lighting, shallow depth of field, realistic water physics, smooth handheld and gimbal movement, 16:9 widescreen, 4K HDR.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.73s`

---

### 🎬 Dragon Warriors Temple Clash
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10648.jpg" width="480" alt="SD2_10648"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dragon-warriors-temple-clash-SD2_10648">🌐 Watch Online</a>

#### 📝 Prompt
```
0–5s: Two anime warriors face each other inside an ancient ruined temple. One radiates golden fire while the other commands blue lightning. Giant dragon-shaped energy forms behind each fighter. 5–10s: The dragons charge together as the warriors engage in an intense martial arts battle. Every punch generates expanding shockwaves, glowing embers, lightning bolts, and flying stone debris. 10–15s: Both dragons collide above the temple in a spectacular explosion of fire, lightning, and glowing particles. The camera rises high above the battlefield to reveal the entire temple surrounded by the expanding energy wave. Style: Epic anime, cinematic composition, dynamic camera, fluid animation, realistic fire and lightning simulation, volumetric atmosphere, blockbuster visual effects, no text, no watermark.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Cola Fashion Transition Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10647.jpg" width="480" alt="SD2_10647"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cola-fashion-transition-SD2_10647">🌐 Watch Online</a>

#### 📝 Prompt
```
[Style] Fashion Transition Ad, vertical 9:16, photorealistic + cutout collage graphic style, silky cutout point transformation, 8K ultra-clear, Cola Red #E61A27/pure black/pure white tricolor system [Duration] 15 seconds [Scene] The opening features a pure white studio background; From the second second, the screen switches to a solid cola red background + a huge white curved cola bottle cutout frame in the center of the frame (classic curved bottle silhouette), with a deep red 'COLA' italic text on the background; No real brand logo throughout [Character] Main character @ Image 1 (keep reference image appearance and hairstyle; Opens with black raglan long-sleeve shirt + black wide-leg shorts; All costume changes are red, black, and white) [00:00-00:02] Shot 1: Screw Cover Locking Point (White Studio Open) Pure white background middle shot: Main character @Image 1 holds an unmarked cola bottle (dark brown soda + red label), crosses both arms to perform two cap clamping actions, and on the third strike, with a "pop" to open the cap, bubbles hissing as they rise. Sound effects: two-tone beat sound, bottle cap "pop," carbonated bubble hiss. [00:02-00:03] Shot 2: Snap Transition She tilts her head back for a sip, and as she swallows, the background switches instantly: cola red background + white bottle-shaped frame covering her entire body, with deep red "COLA" italicized text running across the background. Sound effects: swallowing sound + deep bass "thump" freezes in time. [00:03-00:07] Scene 3: Transition Pop / Floating Props Instant Outfit Change: Wearing a red baseball cap backwards, white sunglasses on the headband, a black vest layered over a red vest, white black polka dot tights + black shorts, red platform shoes, holding a Coke bottle. She performs lively jumping steps inside the bottle-shaped frame: single-foot hopping, hip twisting, and posing with the bottle. Floating red and white props around the area: tape player, instant camera, headset, sampler, and white 3D text "Bubble Pull" are distributed in all four corners. Sound effects: Timing beats + the "whoosh" sound of props flying in. [00:07-00:10] Scene 4: Kick Jump Pose Instant Cut-and-Wear Outfit: White baseball cap, white T-shirt with red pattern, red and black jacket tied at the waist, black shorts, red high-top canvas shoes. She does a kicking jump freeze pose, then lands and spins, swinging her hips. The floating props were changed to: red canvas shoes, white baseball caps, red and white cameras, sunglasses, and the 3D text was changed to "Refreshing Summer." Sound effects: Beat continuation + jump landing "bang". [00:10-00:13] Shot 5: Dress-Up 3 · Floating Summer Instant Cut-and-Change: White off-shoulder cropped top, red-and-white striped shorts, barefoot, body floating swimming posture lying diagonally inside a bottle-shaped frame, holding a Coke bottle. Floating around the area: red and white striped swim rings, little yellow ducks, red flip-flops, white mesh bags, and 3D characters reading "Leaving Gravity." Sound effects: Rhythm turns light + bubble "gurgling" sound. [00:13-00:15] Shot 6: Product Poster Closing (End Card) Instant cut to poster image: red and black diagonal two-tone background, a close-up of a coke bottle in the center without any logo (dark brown soda, red bottle label, white "COLA" lettering), with fine droplets hanging from the bottle. Large white italic text pops in from both sides: "Cola Refreshing Bottle," with a line of small text below "#爽出你的痛快#". The scene freezes in time, without fading out. Sound effects: final stress + bubble screech finish.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.13s`

---

### 🎬 Courier's Epic Treasure Hunt Chase
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10645.jpg" width="480" alt="SD2_10645"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/courier-treasure-hunt-SD2_10645">🌐 Watch Online</a>

#### 📝 Prompt
```
A cinematic 15-second adventure sequence. A 22-year-old bike courier named Alex, wearing a modern courier jacket and backpack, rides through a busy city delivering a package. He accidentally discovers an old, weathered treasure map hidden inside. Close-up of the mysterious map glowing with ancient symbols. Alex races on his mountain bike through dense forests, steep mountain trails, and abandoned ghost towns while dangerous treasure hunters chase him in rugged vehicles. Fast-paced action, dramatic drone shots, golden sunset lighting, dust, cinematic camera movements, realistic visuals, high detail, intense atmosphere, epic adventure movie style, 4K, ultra-realistic.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 The Red Scarf Winter
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10644.jpg" width="480" alt="SD2_10644"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/red-scarf-winter-SD2_10644">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 15-second live-action cinematic romantic short following all eight storyboard panels exactly. Shot sequence: Strong winter wind lifts the woman's bright red scarf into the air. The scarf tumbles gracefully across a snowy street. A young man reaches out and catches it before it falls. They lock eyes for the first time. He gently places the scarf around her shoulders. She thanks him with a warm smile. They naturally begin walking together through softly falling snow. Camera slowly cranes upward as they disappear into the glowing winter street. Music: Emotional piano with orchestral strings. Goal: A romantic movie trailer ending with hope and warmth.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Radiant Reset Pink Balm Glow
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10642.jpg" width="480" alt="SD2_10642"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/lumea-radiant-reset-cleansing-balm-SD2_10642">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 15-second vertical 9:16 premium skincare ad video for the US market. Product: A luxury pink cleansing balm called “LUMÉA Radiant Reset Cleansing Balm”. The product is a premium coral-pink jar with a matte finish, clean minimalist typography, elegant beauty packaging, and a soft balm texture. Keep the product jar, color, branding style, and packaging consistent throughout the video. Model: A clearly adult female beauty model, 23–30 years old, fair skin with natural glow, soft freckles, clean brows, light natural makeup, wet sleek hair in some scenes, healthy skin texture, elegant beauty editorial look. She should feel premium, clean, fresh, and realistic. Style: Luxury skincare commercial, clean beauty aesthetic, warm natural daylight, soft beige and ivory background, high-end beauty photography, glossy water reflections, hydrated skin texture, minimal and elegant composition. The video should feel like a premium skincare campaign mixed with ecommerce beauty ad visuals. 15-second structure: Scene 1 \| 0–2s \| Product hero The pink LUMÉA cleansing balm jar sits centered on a reflective wet surface. A curved splash of crystal-clear water flows behind and around the jar. Soft sunlight and clean beauty lighting. Premium commercial product shot. Scene 2 \| 2–4s \| First application Close-up of the model applying the cleansing balm to her cheek with her fingers. The balm texture appears soft, creamy, and smooth. Focus on skin texture, glow, and product spread. Scene 3 \| 4–6s \| Massage texture Closer facial beauty shot. The balm is gently massaged across the cheek in a circular motion. Show glossy, creamy texture and hydrated-looking skin. Scene 4 \| 6–8s \| Macro texture detail Extreme close-up macro shot of the balm texture on skin. Show the product melting and spreading smoothly across the skin surface. Make the texture feel rich, silky, and luxurious. Scene 5 \| 8–11s \| Rinse moment The model tilts her face upward while clean water splashes across her face. The cleansing moment feels fresh, elegant, and cinematic. Focus on water motion, skin glow, and premium beauty feel. Scene 6 \| 11–13s \| Clean skin reveal Beauty portrait of the model after cleansing. Her skin looks fresh, clean, soft, and radiant. Minimal background, calm eye contact, refined editorial framing. Scene 7 \| 13–15s \| Product + beauty ending Final hero shot with the model and the LUMÉA cleansing balm jar in frame. The product is clearly visible in the foreground or beside her face. End with a premium clean beauty campaign mood. On-screen text: Keep text minimal and elegant. If text is used, only show: “Radiant Reset” “Cleansing Balm” “Cleanse. Melt. Refresh.” Voiceover style: Soft, calm, premium, feminine, like a beauty creator describing a favorite cleansing product.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.07s`

---

### 🎬 Snowbound Ghost Cabin Horror
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10640.jpg" width="480" alt="SD2_10640"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/snowbound-ghost-cabin-SD2_10640">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a photorealistic ghost-lore horror short inside an isolated snowbound cabin at night. CHARACTER: Valeria Peña, a paranoid horror writer in her late twenties, with shoulder-length black hair in a messy low
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

### 🎬 Cinematic 3D Animation From Storyboard
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10639.jpg" width="480" alt="SD2_10639"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-3d-animation-storyboard-SD2_10639">🌐 Watch Online</a>

#### 📝 Prompt
```
Use @Image1 as the complete storyboard, character design, environment, color palette, camera language, and story-progression reference for this piece. Convert it into a finished cinematic 3D animated
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Cinematic Korean Luxury Lifestyle Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10635.jpg" width="480" alt="SD2_10635"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-luxury-lifestyle-SD2_10635">🌐 Watch Online</a>

#### 📝 Prompt
```
같은 젊은 한국 남성이 영상 내내 일관되게 등장하는 초사실적 시네마틱 라이프스타일 영상. 얼굴·날카롭고 또렷한 눈매·차분한 표정·어두운 레이어드 미디엄 헤어·실버 이어커프·체형을 모든 씬에서 동일하게 유지. 첨부 사진을 얼굴과 헤어의 엄격한 기준으로 사용. 리얼리즘: 모공과 결이 보이는 실제 피부, 왁스·플라스틱 같지 않게. 고운 35mm 필름 그레인, 자연스러운 모션 볼러. 실제 그림자와 대비가 있는 강한 방향성 조명 — 평평한 균일 조명 금지. 완급 있는 속도, 모든 게 슬로모 아님. 실제 시네마 카메라 촬영본처럼, AI 생성·부자연스러운 느낌 금지. 의상 원칙: 얼굴과 헤어는 내내 동일. 의상은 각 장소에 맞게 씬별로 자연스럽게 바뀐다 — 모든 컷에서 같은 옷이 아니다. - 시그니처 룩(드레스룸 이후, 와인바): 네이비 코튼 집업 자켓(카라, 오픈) 안에 다크 브라운 니트 폴로, 워시드 차콜블랙 스트레이트 진 + 가죽 벨트, 블랙 가죽 스니커즈, 미니멀 시계 — 첨부 사진 그대로. - 아침 기상 씬: 무지 크림색 반팔티 + 크림색 반바지(편한 잠옷), 자켓 아님, 긴바지 아님. - 헬스 씬: 운동복만 — 다크 탱크탑 + 트레이닝 쇼츠. 헬스 씬 첫 프레임부터 이미 탱크탑 차림, 어느 순간에도 자켓 없음. 각 씬 의상은 아래 타임코드에도 다시 명시 — 그대로 따를 것. 스타일: 럭셔리 한국 라이프스타일 광고, 포토리얼 시네마틱 다큐, 부드러운 핸드헬드, 웜 파스텔 그레이딩, 얕은 심도, 프리미엄 남성복 광고 미감, 4K HDR, 24fps, 16:9. 0-3초 — 아침, 한강 펜트하우스: 한강이 내려다보이는 통창의 럭셔리 미니멀 펜트하우스, 해 뜰 무렵. 무지 크림색 티셔츠와 크림색 반바지 차림. 따뜻한 빛 속에 자연스럽게 깨어 일어나 앉아 강 뷰를 바라본다. 느리고 차분하게. 3-6초 — 드레스룸 코디: 웜 오크 선반의 우아한 워크인 드레스룸. 카메라 앞에서 시그니처 룩을 완성해간다 — 브라운 니트 폴로를 입고, 그 위에 네이비 자켓을 걸치고, 카라를 정리하고, 차콜 진에 벨트를 매고, 시계를 확인하고, 전신 거울 앞에서 머리를 매만진다. 마크로 클로즈업: 원단 질감, 카라 잡는 손, 손목 시계. 이제 시그니처 룩 완성. 6-9초 — 한강변 스포츠카: 시그니처 룩 그대로, 한강 강변 도로로 나오면 매끈한 럭셔리 스포츠카가 기다린다. 다가서서 문을 여는 그를 바로 위에서 내려다보는 항공(버즈아이) 앵글로만 촬영 — 드론이나 비행 기기는 화면에 절대 보이지 않음. 강변 고속도로를 달리고, 아침 햇살이 윈드실드에 렌즈플레어, 뒤로 도시 스카이라인. 9-12초 — 헬스장 운동: 큰 창의 프리미엄 헬스장으로 컷. 첫 프레임부터 이미 다크 운동복 탱크탑 + 트레이닝 쇼츠(자켓 없음). 절제되고 파워풀한 동작 — 덤벨, 케이블 머신, 집중된 호흡. 근육 컨트롤·자세·차분하지만 강렬한 표정·사실적 피부와 옅은 땀·자연광 클로즈업. 12-15초 — 루프탑 와인바, 친구들과: 다시 시그니처 네이비 자켓 룩으로, 골든아워의 우아한 오픈에어 루프탑 와인바, 서울 스카이라인과 강 뷰. 균형 잡힌 친구 모임과 둥근 테이블에 앉음 — 다른 남자 최소 2명과 여자 2명, 모두 세련된 차림, 동등하게 함께. 평범한 친구 모임이지 한 남자를 여자들이 둘러싼 구도 절대 아님. 다 같이 웃으며 와인잔을 들어 건배, 켜지는 도시 불빛. 스카이라인 항공 리빌로 마무리. 오디오는 자연 앰비언트만: 발소리, 새, 멀리 차 소리, 스포츠카 엔진, 헬스 기구와 호흡, 잔 부딪는 소리, 잔잔한 대화, 강가 앰비언스. 음악·자막·로고·워터마크 없음. 네거티브: 화면 글자·자막·브랜드 로고·워터마크 금지. 얼굴·헤어 변경 금지. 인물 복제 금지. 드론·비행 기기 노출 금지. 헬스 씬 자켓 금지. 한 남자를 여자들만 둘러싼 구도 금지. 왁스·플라스틱 AI 피부 금지. 손가락 다섯 개. 신체 왜곡 금지.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `19.25s`

---

### 🎬 Dynamic Music Visualizer
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10634.jpg" width="480" alt="SD2_10634"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dynamic-music-visualizer-SD2_10634">🌐 Watch Online</a>

#### 📝 Prompt
```
generate an interesting music video using this image as first frame,be professional and use dynamic visuals
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Photorealistic Character Identity Reference
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10633.jpg" width="480" alt="SD2_10633"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/photorealistic-character-reference-SD2_10633">🌐 Watch Online</a>

#### 📝 Prompt
```
Use the uploaded photorealistic character sheet as the exact identity reference. Preserve the character's facial structure, hairstyle, eye color, body proportions, costume, weapons, accessories, materials, and overall appearance
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.1s`

---

### 🎬 Golden Hour Badminton Smash
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10632.jpg" width="480" alt="SD2_10632"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/golden-hour-badminton-smash-SD2_10632">🌐 Watch Online</a>

#### 📝 Prompt
```
0–3s A confident young athletic woman walks onto a professional outdoor badminton court during golden hour. She wears a **bright yellow athletic T-shirt, a white pleated sports skirt, white ankle socks, white sports shoes, and a white baseball cap**. She twirls her badminton racket as the morning sunlight creates a warm cinematic glow. 3–6s Close-up of her tightening her grip on the racket. She serves the shuttlecock with precision. The camera follows the shuttlecock in dramatic slow motion while cinematic lens flares and shallow depth of field enhance the scene. 6–10s She performs fast footwork across the court, executing smooth forehand drives, backhand returns, and a quick net shot. Dynamic tracking shots, low-angle camera movement, and crisp slow-motion emphasize her speed, balance, and athletic form. 10–13s She leaps into the air for a powerful overhead smash. The shuttlecock rockets downward as the camera rotates 360° around her, capturing the impact in ultra-slow motion with particles and motion blur. 13–15s She lands confidently, smiles, and spins the racket in her hand while standing at center court. The camera slowly pulls back to reveal the entire court bathed in beautiful golden sunlight, ending with a premium sports commercial aesthetic. Visual Style: Photorealistic, cinematic sports advertisement, realistic physics, smooth camera transitions, natural body movement, vibrant colors, soft golden-hour lighting, shallow depth of field, premium commercial quality, energetic and inspiring.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

<!-- STATS_END -->
