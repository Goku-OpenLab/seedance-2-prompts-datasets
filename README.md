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
- Total Prompts: **8658**
- Updated Today (UTC 2026-08-09): **11**

## 🎬 Today's Updates
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

### 🎬 Moonlit Forest Magic Awakening
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11263.jpg" width="480" alt="SD2_11263"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/moonlit-forest-magic-SD2_11263">🌐 Watch Online</a>

#### 📝 Prompt
```
30-second cinematic fantasy short film, multi-shot sequence, continuous visual storytelling. A mysterious young girl walks alone through an ancient forest at midnight, carrying a tiny antique lantern that flickers with an unusual silver light. 0–5 sec: Wide establishing shot. The girl walks through enormous ancient trees covered in glowing blue moss. Moonlight filters through the branches. Her footsteps disturb tiny floating fireflies that rise around her. Slow cinematic tracking shot from behind. 5–10 sec: She discovers a perfectly circular stone pool hidden between the trees. The water is completely still, reflecting the moon. She kneels and gently places her lantern beside the pool. The silver flame suddenly grows brighter. 10–16 sec: Close-up of the water. Ripples spread outward even though there is no wind. The reflection of the moon begins to crack like glass. A deep magical vibration fills the forest. The girl slowly looks upward in disbelief. 16–22 sec: The moon above the forest suddenly transforms into a gigantic glowing silver flower, unfolding petal by petal in the night sky. Thousands of luminous particles rain gently through the trees. The girl’s cloak and hair move naturally in the magical wind. 22–27 sec: From the glowing moon-flower, a majestic translucent white stag slowly descends through the mist and lands silently beside her. Its antlers resemble branches filled with tiny stars. The girl reaches toward it, emotional and amazed. 27–30 sec: The stag touches its nose to her hand. Instantly, every dead tree in the forest blooms with glowing white flowers. Camera rapidly pulls upward into a breathtaking aerial view of the entire enchanted forest illuminated beneath the enormous moon-flower. Visual style: ultra-realistic cinematic fantasy, magical realism, premium Hollywood fantasy cinematography, 35mm anamorphic lens, realistic skin and fabric texture, detailed ancient forest, volumetric moonlight, atmospheric fog, dreamy bokeh, subtle film grain, natural motion, realistic physics, rich environmental detail, dramatic lighting, elegant color contrast between deep blue night and silver magical light. Camera: cinematic tracking shots, slow push-ins, macro detail shots, low-angle reveal, controlled crane movement, final aerial pullback. No static slideshow feeling. Smooth transitions between shots. Audio: quiet nighttime forest ambience, distant wind, subtle magical chimes, soft footsteps, low mystical rumble during the moon transformation, orchestral crescendo during the stag reveal, ending with a gentle emotional musical note. Performance: natural facial expressions, genuine curiosity turning into awe, subtle breathing and blinking, restrained cinematic acting. Ending: mysterious, emotional, visually spectacular — the feeling that the girl has just awakened an ancient magic that has been sleeping for centuries.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.05s`

---

### 🎬 Snow Temple Kung Fu Revenge Duel
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11251.jpg" width="480" alt="SD2_11251"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/snow-temple-kung-fu-revenge-SD2_11251">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-realistic original stylized kung-fu revenge duel in a snow-covered temple courtyard at blue twilight. 0–4s: wide shot of a silent courtyard covered in white snow and scattered petals, a female swordswoman and a tall white-robed assassin face each other motionless beneath bare trees, slow orbit, visible breath, calm before impact. 4–9s: sudden violent exchange, both fighters sprint forward and collide in a blur of steel, whipping robes, sharp foot pivots, fast parries, low sweeps, elegant spins, snow blasting upward with every movement, camera tracks and circles tightly around them. 9–15s: the assassin launches a final overhead strike, she steps inside the attack, traps the blade, turns sharply, and delivers a clean finishing cut in one fluid motion. He remains standing for a second as snow falls, then drops to his knees and falls backward into the white courtyard. End on her breathing hard, sword lowered, red fabric fluttering in the cold wind.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Wizard Accidentally Creates Giant Chicken
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11247.jpg" width="480" alt="SD2_11247"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/wizard-giant-chicken-SD2_11247">🌐 Watch Online</a>

#### 📝 Prompt
```
Wizard Accidentally Makes a Chicken Too Powerful Hyper-realistic cinematic comedy fantasy sequence, 10 seconds, 16:9. In a medieval village square, one wizard raises his staff for a dramatic spell. He shouts with total confidence: “Behold my power!” A chicken casually walks in front of him at the exact wrong moment. The spell hits the chicken. The chicken becomes huge, glowing, muscular, and emotionally unstoppable. It slowly turns toward the wizard with terrifying confidence. The wizard backs away. The giant chicken flaps once and blasts him backward into a hay cart. Feathers explode everywhere. The chicken steps onto a barrel like a warrior king. End with the wizard lying in hay, whispering: “I have made a mistake.” Style: hyper-realistic, cinematic, ridiculous fantasy comedy, one wizard, one chicken, magical misfire, giant overconfident chicken, no gore, no text, no logos, no cartoon style.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `10.08s`

---

### 🎬 SUV Escapes Collapsing Bridge In Storm
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11241.jpg" width="480" alt="SD2_11241"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/suv-bridge-collapse-storm-SD2_11241">🌐 Watch Online</a>

#### 📝 Prompt
```
Realistic cinematic action sequence, 15 seconds, aspect ratio 16:9. 

At night in heavy rain, a lone driver in a dark SUV races across a long suspension bridge over black water toward the far shore as the bridge begins failing around him. The sequence opens with a wide low angle showing the wet bridge deck, flashing warning lights, and traffic stopped ahead and behind. 

A massive suspension cable suddenly snaps with a violent burst of sparks, the whole bridge lurches, and the road tilts sharply to one side. The driver grips the wheel and accelerates as abandoned cars behind him begin sliding backward across the rain-slick deck into the darkness, smashing into each other and crashing through broken railings.

Keep the action clear and physical. The SUV fishtails but stays under control as the driver swerves around a sliding sedan and a fallen cable whipping across the road. The bridge deck buckles in sections, sending cracks racing through the asphalt. Another support cable snaps, one lane drops lower than the other, and a car behind the SUV loses traction and disappears over the edge. Use dynamic but readable camera movement: wide exterior view of the bridge twisting in the storm, low tracking shot beside the SUV tires cutting through water, and a tense front three-quarter angle as the vehicle climbs the tilted roadway toward safety.

Final action: the driver pushes through the last unstable section just as the center span behind him tears downward. He bursts off the bridge onto solid ground at the far anchorage while the roadway behind collapses in stages, cars sliding backward into the void, cables snapping, sparks flying, and rain exploding off the shattered structure. Realistic storm lighting, hard rain, wet reflections, engine spray, debris, violent structural movement, intense survival atmosphere, no text, no logos, no cartoon style, no slow motion, no extra main characters, no famous celebrity faces, no recognizable actors, no movie-star resemblance, no public-figure likenesses, no clear facial close-ups.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

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

### 🎬 Skyward Journey Through Four Worlds
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11130.jpg" width="480" alt="SD2_11130"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/skyward-journey-four-worlds-SD2_11130">🌐 Watch Online</a>

#### 📝 Prompt
```
16:9, 30 seconds, an epic photorealistic fantasy cinematic long take, original worldbuilding, one continuous shot, continuous camera movement, no hard cuts, and no references to any existing film, character, actor, or recognizable cinematic scene. OVERALL STYLE: A high-budget fantasy film aesthetic with realistic cinematography, monumental world scale, and a beautiful protagonist with natural skin, realistic expressions, and believable body proportions. The overall tone is intelligent, elegant, mysterious, and courageous, never childish, cartoonish, or exaggerated cosplay. Four locations are connected through one continuous flight path: Iceland’s black coastline, an alternate Victorian London, a Paris-inspired city at night in the rain, and a futuristic New York-inspired aerial metropolis. UNIFIED COLOR PALETTE: Deep black, silver-gray, and warm gold remain the dominant colors throughout the film. Iceland adds cold blue; London adds gray-green and amber; Paris adds deep blue and wet gold; New York adds deep teal, silver-white, and gold. Maintain realistic atmospheric perspective, thin mist, rainfall, wet surfaces, glass reflections, and volumetric light throughout. Avoid a video-game look, concept-art appearance, and plastic materials. MAIN CHARACTER: There is only one female protagonist throughout the entire video. She is approximately 28 years old, slender, exceptionally beautiful, intelligent, elegant, and quietly determined. Her refined facial features are completely original and must not copy any real actor or movie character. She has naturally bright eyes, clearly defined eyebrows, a soft but strong facial structure, natural skin tone, realistic skin texture, and a restrained, focused expression. She has warm chestnut-brown hair reaching her waist, naturally wavy at the ends. Part of her hair is blown behind her shoulders by the wind. Her hairstyle must remain identical throughout the entire film. She wears a deep forest-green long coat, an ivory high-neck blouse, a dark-red knitted scarf, brown leather wrist guards, dark-gray trousers, and worn leather boots. Her costume has an elevated British fantasy aesthetic, but she does not wear a school uniform or pointed hat. Do not include badges, school emblems, magical-school symbols, recognizable character costumes, or elements from any existing film. She rides the same original flying broom throughout the sequence: a dark, aged wooden handle with silver-gray metallic fibers at the rear and a small warm-gold light at the front. The broom’s shape, size, color, and materials must never change. HER OBJECTIVE: She is flying through different cities to carry the small warm-gold light toward the far edge of the clouds. She is not a combat character. She does not attack anyone or cast explosive magic. She simply continues forward through cities, coastlines, fog, rain, and high-altitude air. Her emotional progression moves from concentration to wonder, then finally to freedom and determination. 0-5 SECONDS: TAKEOFF FROM ICELAND’S BLACK-SAND BEACH The shot begins extremely low above a black volcanic beach using a 24mm wide-angle lens. Black ocean waves are on the left, towering basalt columns on the right, and blue-white glacial mountains in the distance. Cold blue clouds press down across the sky, while a narrow line of warm golden sunset remains near the horizon. The beautiful female traveler rapidly enters from the rear right of the frame, riding her broom just above the ocean surface. Her chestnut-brown hair streams backward in the sea wind. Her dark-red scarf creates a clean motion line behind her, while her deep forest-green coat moves naturally in the airflow. The warm-gold light at the front of the broom illuminates the sea mist and droplets of water. The camera follows her from behind with a stable FPV movement, keeping her slightly right of center. It must not circle around to the front or allow her to leave the frame. Her body leans slightly forward; one hand holds the broom handle while the other maintains balance. She flies toward a massive wall of blue ice. At the fourth second, she enters a natural裂缝 beneath the ice wall. The ice passes rapidly along both sides of the camera. Cold blue crystals briefly intersect with the warm-gold light, creating the first natural transition. No explosion, magical smoke, or sudden transformation. 5-12 SECONDS: VICTORIAN LONDON IN THE FOG As the ice clears the lens, the environment naturally becomes an alternate Victorian city at night. The protagonist and broom retain exactly the same direction, speed, clothing, appearance, and flying posture. The camera continues following from behind. Below are wet dark-gray stone streets. Red-brick buildings, black iron bridges, narrow windows, and old amber streetlamps line both sides. Several dark-red double-decker public vehicles without text or branding move slowly through the fog. The city should evoke Victorian London without reproducing real landmarks. The camera gradually transitions from fast FPV pursuit into a smooth three-quarter rear tracking shot, moving approximately 45 degrees to her left side. Her beautiful profile appears briefly. Her eyes remain focused, and her hair and scarf maintain stable continuity. The warm-gold light leaves only a short trail through the rain and fog. She passes beneath a black elevated iron bridge. Its steel structure moves across the top of the frame as a brief physical occlusion. The camera does not cut, and when the obstruction clears, she remains on the same movement axis. At the tenth second, she flies into a massive arched railway station. Its roof is made from black steel beams and wet glass, with rainwater flowing across the surface. The roof completely covers the frame, creating the second natural transition. 12-19 SECONDS: PARIS-INSPIRED CITY IN THE RAIN When the glass roof clears the camera, the environment becomes a romantic, original Paris-inspired city at night in the rain. Do not reproduce real landmarks. Preserve only the atmosphere of stone bridges, a river, narrow streets, classical stone buildings, wrought-iron balconies, and warm window light. The protagonist flies low above a broad river. The water reflects golden windows and the deep-blue night sky. Pale-gray stone buildings, tall narrow windows, wet rooftops, and fine rain lines extend along both sides. Her deep-green coat and dark-red scarf form a clear silhouette against the blue city, while her chestnut hair streams backward. The camera moves into a parallel tracking position on her right side. The broom stays approximately three meters above the river. The camera remains slightly below shoulder level, preserving the spatial relationship between the woman, broom, river, and architecture. She passes beneath a sequence of classical stone bridges whose arches form continuous reflections in the water. At the seventeenth second, she enters a long mirror corridor made from wet glass walls. The reflections may show only the same woman, the same broom, and the same warm-gold light. Do not create duplicate people. Rainwater, city lights, and reflections slide along the glass surfaces. A powerful warm-gold light appears at the end of the corridor. She flies toward it, creating the third natural transition. 19-24 SECONDS: FUTURISTIC NEW YORK-INSPIRED CITY The mirror corridor opens into an original futuristic New York-inspired metropolis. The camera rapidly but smoothly shifts from the three-quarter rear position into a controlled forward-facing FPV shot moving backward in front of her. Her beautiful, focused face, chestnut hair, dark-red scarf, and the golden broom light are briefly visible. Below are wet streets, glass skyscrapers, metallic elevated bridges, and enormous urban canyons. T
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.1s`

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

<!-- STATS_END -->
