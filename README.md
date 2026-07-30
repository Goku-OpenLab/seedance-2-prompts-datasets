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
- Total Prompts: **8506**
- Updated Today (UTC 2026-07-30): **16**

## 🎬 Today's Updates
### 🎬 Photorealistic Airplane Crash Sequence
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10936.jpg" width="480" alt="SD2_10936"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/photorealistic-airplane-crash-SD2_10936">🌐 Watch Online</a>

#### 📝 Prompt
```
SEEDANCE 2.0 — LIVE-ACTION AIRPLANE CRASH FORMAT 15 seconds \| 16:9 \| live-action disaster drama Fictional scenario. Photorealistic, grounded visual realism. 5 sequential shots with continuous event progression. SETTING A commercial passenger aircraft approaching a large coastal city during severe storm conditions. Late afternoon. Heavy cloud cover, turbulent wind, rain, wet surfaces and reduced visibility. Aircraft design remains fictional with no real airline branding. 00–03s — SOMETHING IS WRONG Interior passenger cabin. Medium handheld shot from aisle height. The aircraft suddenly shudders through severe turbulence. Overhead lights flicker. Passengers instinctively grip armrests and look toward one another. Loose objects vibrate naturally. Camera shakes because the aircraft moves, not through artificial cinematic shake. AUDIO: deep engine rumble, cabin rattling, rain against fuselage, nervous breathing. 03–06s — LOSS OF CONTROL Exterior telephoto shot from ground level. The passenger aircraft emerges beneath dark clouds at unusually low altitude, descending rapidly with a slight unstable bank. Rain trails across the fuselage. Wings react subtly to turbulent airflow. Camera operator struggles to keep the aircraft centred while tracking it. AUDIO: distant aircraft roar, wind, rain. 06–09s — CABIN Close handheld aisle perspective. The aircraft banks harder. Passengers lean naturally with inertia. A bag falls from an open overhead compartment. Cabin crew brace themselves against fixed structures. Lighting changes as the aircraft rotates relative to the storm outside. No exaggerated screaming or theatrical performances. 09–12s — FINAL DESCENT Long ground-level shot. Aircraft passes behind foreground buildings and trees, partially obscuring the view. Camera rapidly pans to follow. The aircraft disappears beyond the distant structures. AUDIO: engine noise grows louder, then becomes partially muffled after the aircraft disappears. 12–15s — IMPACT IMPLIED Camera remains on the distant skyline. A powerful impact occurs beyond the visible horizon. A delayed plume of dark smoke and dust rises behind the buildings. Nearby birds scatter. The camera operator instinctively lowers the camera slightly before reframing toward the smoke. Sound reaches the camera after a physically believable delay: distant low impact → environmental echo → car alarms beginning nearby. No visible bodies. No graphic injuries. CAMERA REALISM Observational disaster footage. Believable camera placement for every shot. Natural handheld micro-movement. Imperfect reframing. Realistic autofocus adjustments. Natural motion blur during rapid pans. No impossible camera movement. PHYSICS Aircraft maintains believable scale, mass, momentum and forward velocity. Passengers react according to aircraft acceleration and banking. Rain, clothing, loose objects and smoke respond naturally. Impact remains geographicall
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Food Summon Freeze Pose Challenge
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10930.jpg" width="480" alt="SD2_10930"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/food-summon-freeze-pose-SD2_10930">🌐 Watch Online</a>

#### 📝 Prompt
```
[Style] Food Summon Freeze Pose, DJI Action Camera First-Person POV (Action-Cam Ultra Wide, 9:16 Vertical), Real handheld wide-angle distortion and natural light, Mannequin Time-Stop effect, TikTok viral meme rhythm [Duration] 10 seconds [Scenes] Six food scenes switch in sequence: milk tea shop→ charcoal barbecue restaurant→ Sichuan hotpot restaurant→ pizza shop→ dessert shop, → burger shop [Character] Female lead image 1 (facial features consistent throughout, changing outfits for each scene) [Core Mechanics] Summoning + freeze-frame logic is unified throughout the film: Each scene starts with an empty shot, where the user reaches the food from below the frame to the center of the frame and stops→ half a second later, the female lead appears out of thin air (hard cut, no gradual display). When she appears, her actions stop halfway—reaching out to catch halfway, biting halfway, opening her mouth to bite halfway through—the whole person freezes as if time has stopped, with body, expressions, and hair completely still; The only thing moving is the natural shaking of the handheld camera and the food's own heat, strings, and drips; After freezing for about 1 second, a scene is forcefully cut [00:00-00:01.5] Scene 1: Brown sugar bubble tea (brown sugar bubble tea). In front of the warm-light bar at the milk tea shop, an empty shot shows a cup of brown sugar pearl milk held up toward the center of the frame, with the brown sugar syrup slowly sliding down the wall of the cup→. The female lead appears in a beige knit cardigan, frozen halfway through the cup, eyes fixed on the pearls shining without moving. [00:01.5-00:03.5] Scene 2: Charcoal-grilled pork belly On the grill at the barbecue restaurant, pork belly sizzles with oil, its edges crispy and curled, smoke rising from the air, and the seats across from you are empty; She picks up a piece of shiny pork belly with tongs and reaches for an empty seat→ The female lead appears in a black-and-white striped shirt, frozen on the half-cut gesture of opening her mouth to lean toward the meat, with only the smoke of the charcoal continuing to drift. [00:03.5-00:05] Scene 3: Red Oil Beef Tripe Hotpot In hot pot restaurants, the bottom of the hot pot is bubbling with chili oil, and chili and Sichuan peppercorns swirl around the soup surface; She picks up a piece of tripe coated in red oil with chopsticks and reaches it to the center of the frame. As the oil drips down→ the female lead appears in a red sweatshirt, frozen at the moment when her mouth is wide open and the tripe hangs one centimeter from her mouth, the oil in the pan continues to bubble. [00:05-00:07] Scene 4: Cheese Pulled Pizza A whole plate of freshly baked thick cheese pizza on the wooden table in the pizzeria; She picked up a corner of the pizza and lifted it up, pulling out half-meter-long strands of cheese that still connected to the plate. Steam rose → the female lead appeared instantly in a black off-shoulder top, frozen in a pose of tilting her head back and mouth open to catch the shredded cheese, the strands trembling slightly above her lips. [00:07-00:08.5] Scene 5: Lava cake bursting with slurry On the marble countertop of the dessert shop, a chocolate lava cake is just being cut open with a spoon. Dark brown lava flows from the cut, slowly dripping onto the plate. The female lead appears in a cream-white dress→ frozen in a pose of holding a spoon close and raising an eyebrow at the camera, the lava flowing continuously. [00:08.5-00:10] Scene 6: Double cheeseburger finish Under the warm light of the burger shop, she holds up a double-layer cheese beef burger. The cheese melts from the edge of the patty, the juices glistening under the light→ and the female lead instantly appears, frozen in moments as she holds the burger with both hands, her mouth wide open to the max, eyes wide open. The scene stops at this moment and closes to the scene. [Sound Effects] Light and playful background music, with a snap "click" sound + a slight static "buzz" sound during each freeze; The food sound effects in the empty shot are amplified—the sizzling sound of barbecue, the slurp of hotpot, the sticky shredding of cheese, the thick, smooth pouring of molten heart, all ending with a frozen frame and a high-pitched closing sound
```

#### 📌 Details
- Ratio: `0.56` | Duration: `10.19s`

---

### 🎬 Futuristic Racer on Frozen Moon
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10928.jpg" width="480" alt="SD2_10928"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/futuristic-racer-frozen-moon-SD2_10928">🌐 Watch Online</a>

#### 📝 Prompt
```
Vehicle identity locked to @snowcar. Color grade and mood matched to @snowcar grade. Hyper-realistic cinematic action sequence. A futuristic racer blasts through razor-thin ice canyons on a frozen alien moon while an avalanche of collapsing glaciers
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Sleek Wireless Earbuds Commercial Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10926.jpg" width="480" alt="SD2_10926"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sleek-wireless-earbuds-ad-SD2_10926">🌐 Watch Online</a>

#### 📝 Prompt
```
A sleek, high-end commercial ad for modern wireless earbuds in a stylish, brightly lit modern apartment kitchen. A woman's hands hold a matte charcoal grey charging case labeled "LOOVA". She pops open the case to reveal dark metallic wireless earbuds with glowing LED indicators. Camera zooms into a macro shot of the earbuds inside the case. A stylish woman wearing a black baseball cap, white off-the-shoulder top, and gold hoop earrings inserts one earbud into her ear. She taps the side touch control, closes her eyes, and smiles contentedly as music plays. Close-up shot showing the detailed fit of the earbud in her ear as she gently adjusts it. She looks directly at the camera with a warm smile and gives a confident thumbs-up. Cuts to a glossy hero product shot of the open earbud case resting on a polished reflective countertop. Soft natural daylight, warm aesthetic, modern lifestyle product commercial, 4k resolution, smooth cinematic camera motion, photorealistic.
```

#### 📌 Details
- Ratio: `1.0` | Duration: `30.1s`

---

### 🎬 Epic Wuxia Duel On Misty Cliff
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10924.jpg" width="480" alt="SD2_10924"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/wuxia-duel-misty-cliff-SD2_10924">🌐 Watch Online</a>

#### 📝 Prompt
```
Cinematic 15-second storyboard, vertical/portrait aspect ratio, ultra-detailed anime-realism hybrid style, epic wuxia fantasy action. Character (Heroine – exact match to reference): Beautiful young woman with waist-length flowing pure white hair, wearing an ornate white horned mask with sharp upward horns covering the upper face, revealing only lips and chin. Form-fitting white battle dress with open midriff, layered sheer white fabric, white arm wraps, thigh high white bandages, and white heeled sandals. Dual-wielding: right hand a long white sword with wooden handle held high, left hand a pure white blade held low. Pale skin, athletic build, dynamic combat stance. Setting: Wet circular stone platform high on misty mountain cliffs, towering jagged green-gray rock peaks in background, soft overcast light, light fog, water droplets on the ground. Opponent: Dark mirror counterpart – tall male warrior in black tattered armor with crimson accents, dual black blades, red glowing eyes under a horned black mask. 15-second timed sequence (storyboard panels): 0–3s Wide establishing shot → medium shot. Heroine stands in ready pose on the wet platform, white hair and fabric gently moving in the wind. Opponent steps into frame from the mist. Both raise their dual blades. Tension builds, slight camera push-in. 3–6s Fast cut to close-up of eyes through masks → full body dynamic exchange. Heroine launches forward with a spinning slash using the wooden-handled sword. Opponent blocks and counters with a low sweep. Sparks and white energy trails fly. Quick side-tracking camera follows the clash. 6–10s Mid-air aerial combo. Heroine leaps high, white hair and dress flowing dramatically, dual swords crossing in an X-slash. Opponent jumps to meet her. Multiple rapid blade clashes in the air, white and black energy trails intertwining. Slow-motion moment as blades lock, then they separate and land hard on the platform, water splashing. 10–13s Ground power clash. Both charge, blades colliding in a massive impact. Camera circles 180° around them. Heroine uses the momentum to spin low and strike upward. Opponent staggers back. Intense motion blur on the swords, glowing white energy cracks the stone floor slightly. 13–15s Final decisive moment. Heroine performs a graceful yet deadly finishing dual-sword thrust, white energy exploding outward. Opponent is pushed back to the edge of the platform. Freeze-frame on her powerful pose (matching the reference image energy), white hair and fabric dramatically billowing, mountains in background, soft mist swirling. Fade to black with lingering energy particles. Style notes for every panel: Photorealistic skin and fabric details, cinematic lighting with soft volumetric fog, high-speed action clarity, elegant feminine power, no blood, pure fantasy martial arts energy. Consistent character design throughout.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Evening Gym Cardio Vibes POV
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10920.jpg" width="480" alt="SD2_10920"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/evening-gym-cardio-SD2_10920">🌐 Watch Online</a>

#### 📝 Prompt
```
CAMERA: DV 16mm handheld tape camera POV, shot by LISA [@图片1]. CHARACTER: Main LISA: [@图片1] SETTING: Evening gym cardio area, cardio equipment, music playing on phone, soft lighting. SCENES: 1.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

### 🎬 Cinematic Winter Cabin Retreat
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10918.jpg" width="480" alt="SD2_10918"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-winter-cabin-SD2_10918">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: Ultra-realistic, cinematic winter documentary, 4K HDR, natural lighting, shallow depth of field, smooth camera movement, soft colour grading, peaceful atmosphere. Maintain the same woman throughout every scene (mid-20s, natural appearance, long dark brown hair tied in a loose ponytail, cream knitted sweater, dark leggings, wool socks, no makeup-heavy look). Scene 1 (0–3s) Aerial drone shot of a small wooden cabin hidden deep inside a snow-covered pine forest. Heavy snow falls gently while warm golden lights glow from the windows. Thin smoke rises from the chimney as the camera slowly descends toward the cabin. Scene 2 (3–6s) Inside the cabin, the same woman sits beside a crackling stone fireplace wrapped in a soft wool blanket, reading a book. Steam rises naturally from a ceramic mug of hot chocolate on a rustic wooden table. Firelight flickers across the room, creating a warm contrast with the cold blue light outside. Scene 3 (6–10s) She opens the wooden front door and steps onto the snowy porch. Snowflakes land softly on her sweater and hair. She smiles, takes a slow deep breath, and looks across the silent forest while the camera gently circles around her. Scene 4 (10–13s) Close-up cinematic shots: boots leaving fresh footprints in untouched snow, her gloved hand brushing snow from pine branches, snowflakes settling on the warm cabin window, and smoke drifting into the crisp winter air. Scene 5 (13–15s) Wide cinematic pullback from the cabin at dusk. Snow continues falling as the glowing cabin becomes smaller among the vast white forest. The scene ends with a calm, peaceful atmosphere and the feeling of complete solitude. Camera Slow drone movements Smooth gimbal tracking Gentle push-ins Macro close-ups No fast cuts or shaky movement Audio Gentle wind Soft snowfall ambience Fireplace crackling Distant birds Quiet piano or acoustic instrumental Colour Grade Warm amber tones indoors, cool blue-white winter tones outdoors, creating a cosy contrast. End Text Sometimes the quietest places leave the strongest memories.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Cinematic Luxury Villa Lifestyle Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10916.jpg" width="480" alt="SD2_10916"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-luxury-villa-ad-SD2_10916">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-realistic cinematic luxury lifestyle ad of a fit blonde woman arriving in a premium electric car at a modern hillside villa during blue hour. She steps out confidently, walks through the elegant outdoor space, drinks from a stainless steel bottle, and enjoys a peaceful evening. Warm cinematic lighting, shallow depth of field, smooth gimbal tracking shots, soft bokeh, natural body movement, luxury atmosphere, 4K HDR, ARRI Alexa 35, premium commercial quality.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.04s`

---

### 🎬 Solo High Speed Train Travel Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10912.jpg" width="480" alt="SD2_10912"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/solo-train-travel-vlog-SD2_10912">🌐 Watch Online</a>

#### 📝 Prompt
```
A young woman (image = her face and hair) is seated by the window of a high-speed train, filming a realistic travel vlog from one fixed camera angle near the tray table. She smiles at the camera and says in Korean, "혼자 여행 시작!" As the train moves, beautiful countryside passes outside the window. She takes a sip of coffee, captures a photo of the scenery with her phone, then happily shows the photo to the camera. A few moments later she watches the sunset outside, smiles softly, and says, "정말 예쁘다." As the train arrives at the station, she picks up her backpack, waves warmly, and says, "도착! 다음에 또 만나요." She reaches toward the lens to stop the recording. Shot in live-action photorealism with a locked camera, natural train ambience, realistic skin texture, soft daylight, no background music, no subtitles, no logos, and no CGI or AI-plastic appearance.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Intense K-POP Girl Crush Solo Dance
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10908.jpg" width="480" alt="SD2_10908"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/kpop-girl-crush-solo-dance-SD2_10908">🌐 Watch Online</a>

#### 📝 Prompt
```
Exactly the same adult woman as in reference image 1—identical face, hairstyle, clothing, and body proportions. She performed an intense K-POP girl-crush solo with confident hip swings, deep body rolls, smooth body waves, thigh breaks, sharp waist movements, and natural hair tosses. Use dynamic multi-camera music and video settings. Starting with smooth 360° tracking shots, then switching between full-body dance shots, upper body close-ups, waist-to-hip close-ups, three-quarter angles from behind, and dramatic low-angle shots. Keep the choreography clear and continuous. Close-ups are used as short rhythmic inserts, while her full-body is shown throughout most of the dance. She ends with a slow, low-angle approach to the camera, turning to the camera with a confident expression. Warm skin tones, deep teal shadows, cinematic lighting, subtle film grain, realistic skin and fabric texture details, high-end K-POP MV and trendy advertising style, 24fps. Adapting the accompanying character images. Keep your face, clothing, and body proportions consistent throughout.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.13s`

---

### 🎬 Fresh Apple Lifestyle Beverage Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10904.jpg" width="480" alt="SD2_10904"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/fresh-apple-lifestyle-ad-SD2_10904">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a high-end lifestyle beverage ad that uses the same young East Asian woman throughout the entire sequence. Maintain the same facial features in every frame, smooth light brown wavy hair, glowing skin, body proportions, and clothing. She wore a fitted black ribbed cropped top, light blue ripped high-waisted jeans, white sneakers, silver round earrings, a multi-layered silver necklace, sunglasses perched on her head, and a small white shoulder bag. The modern downtown is filled with murals, cafes, boutiques, rooftop terraces, and upscale juice bars, a vibrant summer atmosphere, bright natural sunshine, luxurious commercial photography techniques, a fresh palette of green and white inspired by fresh apples. The video begins with her confidently smiling at the camera, standing outside a trendy juice bar. She noticed the chilled sparkling apple drink displayed on ice, excitedly picked it up, turned the bottle to her face, the droplets sparkling in the sunlight, then smiled and said, "Freshness starts here!" "A cinematic macro shot of the main character shows a chilled apple drink, surrounded by crisp green apples, ice cubes, sparkling droplets, and fresh mint leaves. She twisted open the bottle cap, producing a satisfying crisp pop. Slow-motion close-ups capture the moment when tiny bubbles surge upward as she sips, and her smile instantly brightens. She confidently walked through the colorful city center streets, adorned with murals, flowerpots, cafes, and boutique shops. A smooth handheld tracking camera followed her, with a gentle breeze naturally blowing through her hair. She casually browses fashion boutiques, tries on sunglasses, admires the display window, and continues to enjoy her apple drink. She met her friends at a stylish rooftop café overlooking the city skyline. They hug and greet each other, laugh together, order light meals, place chilled apple drinks on the table, and enjoy the warm afternoon sunshine. As the golden hour approached, the group walked across the rooftop terrace. Music performed on nearby streets sparked impromptu dancing and joyful moments. Handheld and stabilizer shots capture genuine laughter, hair swings, and energetic choreography, each holding their apple drink. The celebrations continued, gathering at the edge of the rooftop at sunset. Warm golden light illuminates the skyline as everyone raises their chilled apple drinks, laughing, and enjoying the scenery. Cinematic close-ups capture the sparkling droplets and the realistic flow of liquid inside the bottle. The final cinematic heroic shot: a young woman holding a chilled apple drink approaches the camera and is placed directly in front of the camera. The city skyline sparkled behind her, and she smiled warmly and said, "Keep it fresh." Stay energized. The camera slowly zooms in, showing the stunning rooftop skyline, sparkling sunsets, friends celebrating together, and the vibrant downtown atmosphere. Only natural ambient sounds are used: city ambiance, footsteps, café chatter, birdsong, gentle breeze, boutique doors opening, shopping bag rustling, bottle caps opening, bubble hissing, ice clinks, rooftop conversations, laughter, street performers in the distance, rustling leaves. No background music, no subtitles, no logos, no watermarks, and no screen text. High-end commercial-quality photography, ultra-realistic skin textures, realistic liquid physics, handheld and stabilized dynamic camera movement, physically precise lighting, shallow depth of field, vibrant green and crisp white palette, luxurious beverage advertising, 16:9 widescreen, 4K HDR.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Mysterious Black Box at Night
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10902.jpg" width="480" alt="SD2_10902"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/mysterious-black-box-night-SD2_10902">🌐 Watch Online</a>

#### 📝 Prompt
```
CHARACTER : [REFERENCE IMAGE] wearing casual home clothes, hair loose, relaxed expression LOCATION A small modern guesthouse room at night, clean minimalist interior with smooth neutral walls, simple contemporary furniture and a low platform bed with crisp linen sheets, a soft warm LED strip and a slim modern lamp giving dim light, a flush modern door across the room, and just outside that door an open-air walkway of a modern boutique guesthouse with clean concrete flooring, a sleek glass and metal railing, minimalist planters, and soft recessed downlights glowing along the ceiling, dark quiet night beyond STYLE Cinematic realistic horror short film, multishot with clean cuts between distinct camera setups, ARRI Alexa Mini LF, Cooke S7/i anamorphic prime, shallow cinematic depth, low-light night interior, desaturated cool palette with warm accents, Kodak Vision3 250D grade, fine natural 35mm grain, deep shadow falloff, photorealistic, unhurried naturalistic pacing SHOT Shot 1 Extreme close-up on the character's face lying sideways on the bed in the dark, eyes half-lidded and lazily scrolling, the cold blue phone glow flickering across their skin, calm and sleepy, then a doorbell suddenly rings offscreen and their eyes snap wide open with a startled flinch, they slowly push the blanket aside and sit up on the edge of the bed without hurrying, looking toward the door with a confused frown. Shot 2 Tracking shot following behind the character as they walk slowly and calmly across the dark room toward the door, and while still walking they speak uneasily "I didn't order anything, who is that". Shot 3 Close-up on the character's hand slowly turning the modern door handle and pulling the door open into the dark night outside. Shot 4 Shot from outside on the open-air walkway looking back at the character standing in the lit doorway facing outward, a plain black box clearly visible sitting on the concrete floor just outside the door at their feet, the character leans their head out past the doorframe and looks outward to the left along the empty walkway then turns and looks outward to the right, searching the dark night and finding nobody there, then finally lowers their gaze down to the black box at their feet. Shot 5 Low angle close-up on the plain black box sitting on the floor outside at the character's feet, then the character crouches down into frame, hesitates a moment, and picks it up with both hands. Shot 6 Medium shot inside the room as the character carries the black box to the bed and sets it down carefully on the mattress, then kneels beside it leaning over the box and reaches for the lid. Shot 7 The view from inside the box looking upward in total darkness, the lid lifting open to reveal the character's face peering down into the box from above lit from the side, first puzzled and frowning as they try t
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Relaxed Park Vlog Retro DV Style
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10900.jpg" width="480" alt="SD2_10900"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/relaxed-park-vlog-retro-dv-SD2_10900">🌐 Watch Online</a>

#### 📝 Prompt
```
CAMERA: DV 16mm tape camcorder handheld footage feel. Point of view of a beautiful young woman holding the camera directly in her hand. Maintain natural hand shake, slightly misaligned framing, delayed focus pulls, clumsy zoom in/out, occasional self-cam framing where part of her face gets cut off, and imperfect shots that briefly lose the subject. Every shot is filmed by her holding the camcorder herself in selfie-cam or first-person style. The camcorder itself never appears on screen. LOOK: DV 16mm tape camcorder footage look. Soft, slightly blurry digital tape quality, faint tape noise, subtle compression artifacts, highlights that bloom gently in bright daylight, auto-exposure that adjusts naturally while moving between sunlight and tree shade, muted color contrast, realistic skin tones. STYLE: Relaxed daytime park vlog with a calm, happy, low-energy vibe. Handheld throughout with authentic amateur camcorder filming. Natural pauses, occasional soft laughter, light breathing after walking, genuine unposed moments. Feels like a real personal home video rather than a cinematic production. Character: A beautiful cute young woman in her 20s with long naturally flowing dark hair, elegant facial features, expressive eyes, glowing healthy skin, and a warm genuine smile. fit build. Wearing a modest long-sleeve casual athletic top or lightweight sweatshirt, loose-fit joggers or comfortable pants, and sneakers. Fully covered arms and torso. No jewelry. Setting: A peaceful public park during daylight. Lush green trees, wide walking paths, neatly maintained grass, colorful flower beds, wooden benches, gentle breeze moving the leaves, birds occasionally flying by, soft natural sunlight filtering through the trees, distant park visitors, and a calm, relaxing atmosphere. Storyboard: (~2s, camera propped against a park bench, medium shot) She walks into frame with a relaxed smile after a leisurely walk, brushes a few loose strands of hair away from her face, and looks at the camera. WOMAN: ""It's such a beautiful day today."" (~2s, handheld, slow pan across the park) The camera slowly drifts across the green trees, walking paths, flowers, and open lawn before returning to her. WOMAN (off-screen, softly): ""Everything feels so peaceful out here."" (~2s, medium handheld, beside a bench) She picks up her reusable water bottle, takes a long refreshing sip, then smiles comfortably. WOMAN: ""I really needed that."" (~1.5s, macro insert, shallow DOF) Close-up of her hand brushing across the cool water bottle with tiny droplets of condensation sparkling in the sunlight. Leaves gently sway in the blurred background. No dialogue—only soft ambient park sounds and gentle breathing. (~2s, medium handheld, open grassy area) She p
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Sword Fairy Meets Bike Commuter
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10896.jpg" width="480" alt="SD2_10896"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sword-fairy-bike-reversal-SD2_10896">🌐 Watch Online</a>

#### 📝 Prompt
```
[Overall Style] A restrained comedy with cinematic realism and texture, using the elegant language of xianxia cinema, Jacques Tati's precise spatial management, and Buster Keaton's cold reactions; The humor comes from a sudden reversal of a character's status, no longer relying on falls, accidents, traffic penalties, or modern systems that slap people in the face. Designed for Seedance 2.0's features such as multi-reference character locking, multi-item coordinated movement, continuous spatial scheduling, fine performance control, and native audio-visual synchronization for Mandarin dialogue, ambient sound, music, and motion effects. [Characters] Role A The same East Asian sword fairy sister aged 25–30 from @图片 1 strictly maintains the same face as in the reference photo, with long black hair, makeup, tall and slender figure, white embroidered silk Hanfu, semi-transparent wide sleeves, jade hairpin, silver accessories, and white cloth boots. She appears fully from shoe to head in the frame, with a silver longsword controllingly circling her before stopping at her feet; She rose half a meter above the ground, hands behind her back, her expression calm and proud. Role B The same biker from @图片 2 strictly maintains the same identity, ponytail, clothing, body proportions, accessories, and bicycle; She pushed her bicycle into the frame, genuinely gazing at the Sword Immortal Sister in awe. [Lens 1 \| 0-5s \| Low-angle panoramic slow rail push] 16:9 landscape screen, sunlit modern Chinese city rooftop bicycle parking platforms, concrete floors, yellow parking lines, metal guardrails, distant tall buildings, clothes drying clothes fluttering in the wind, six neatly parked bicycles, and clear backlighting on a warm evening. Character A is the same 25–30 years old East Asian sword fairy from @图片 1, strictly maintaining the same face as in the reference image, long black hair, makeup, tall and slender figure, white embroidered silk Hanfu, semi-transparent wide sleeves, jade hairpin, silver accessories, and white cloth boots. She appears fully from shoe to head in the frame, with a silver longsword controllingly circling her before stopping at her feet; She rose half a meter above the ground, hands behind her back, her expression calm and proud. Character B is the same bike girl from @图片 2, strictly maintaining the same identity, ponytail, outfit, body proportions, accessories, and bicycle; She pushed her bicycle into the frame, genuinely gazing at the Sword Immortal Sister in awe. [Shot 2 \| 5-10s \| Double Medium Shot] The camera slowly pans horizontally: the same cyclist looks up and asks, "Sis, you really know how to ride a sword?" ” The same Sword Immortal Sister forced back her laughter, gently lifted her chin, and calmly replied, "I know a little." ” The same silver longsword elegantly traces a circle, her wide sleeves fluttering softly against the light. Bike Sister casually placed one hand on the bike bell, pressing it only once. In the background, the same six bicycles vibrate slightly, and the bike bells respond in precise rhythm one by one. [Shot 3 \| 10-15s \| Panoramic Reveal Gradually Moving into Close-up] Similarly, six bicycles rose smoothly from the ground, forming a huge circular "bicycle sword formation" behind the cyclist sister. The wheels slowly turned, resembling a glowing celestial aura. She stepped on the same bicycle she was floating on and casually said, "I usually use this for commuting." " Then smoothly glide into the distance. The only silver longsword beneath the same Sword Immortal sister's feet quietly retreated behind her legs to hide. Close-up: Sword Immortal Sister's proud smile froze instantly, one eyelid twitched slightly, and she silently lowered her spellcasting finger. The scene froze as she glanced sideways at the awkward longsword. [Technical Requirements] A strict total duration of 15 seconds, three clean shots, character faces and costumes are stable, characters always maintain clear movement directions, bicycle weight, wheel rotation, long hair, and silk fabric physical effects are realistic, Mandarin lip movements are accurate, the bell sequence is precisely synchronized, no subtitles are generated, no extra characters are added. [Negative Terms] blurry, bad quality, low quality, low resolution, noisy, jpeg artifacts, watermark, text, error; deformed, mutated, bad anatomy, poorly drawn hands, bad composition, out of frame, disfigured; inconsistent character, changing clothes, face morphing, background shift, glitching cuts, disappearing props
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Retro Film GRWM Style
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10894.jpg" width="480" alt="SD2_10894"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/retro-film-grwm-SD2_10894">🌐 Watch Online</a>

#### 📝 Prompt
```
A continuous 15 second retro styled cinematic Get Ready With Me video featuring an East Asian male with dreadlocks in a warm mid century apartment, shot on 35mm film with organic grain and natural color tones, 16:9 aspect ratio. [00:00 - 00:03] Static eye level shot. Central composition. A young man wearing a white ribbed tank top sits on a dark brown leather couch, pouring tea from a matte black kettle into a small vintage floral ceramic cup. Multiple hands rapidly extend from off screen edges, dangling various clothes like cardigans, vests, and sunglasses in front of him in a chaotic style. Warm afternoon sunlight pours in through side windows, illuminating lush houseplants and a wooden bookshelf behind him. [00:03 - 00:06] Rapid snap zoom to an extreme close-up macro shot of his hands buttoning light beige corduroy pants. Focus is razor sharp on the fabric texture, waistline, and brass button click, featuring micro handheld camera wobble. [00:06 - 00:09] Smooth whip pan upward to a medium shot as he pulls a oversized white crewneck tee over his head, immediately followed by tossing a green and cream horizontal striped knit cardigan toward the camera lens, creating a seamless dynamic fabric wipe transition. [00:09 - 00:12] Eye level medium close up shot. The subject slides on dark black retro sunglasses and adjusts a washed grey baseball cap over his dreadlocks. The lighting is warm, soft, and cozy, with a glowing paper lamp visible in the soft focus background. [00:12 - 00:15] The frame shifts into a circular fisheye lens perspective. The subject crouches low, bringing his hands up around the lens frame to inspect his look, smiling casually before leaning forward to tap the screen. Vintage 90s aesthetic, realistic skin texture, authentic film jitter, no plastic smooth look. Audio Track: 120 BPM smooth lo fi hip hop beat featuring relaxed sub bass, rhythmic vinyl crackle, subtle guitar licks, and crisp Foley sounds of tea pouring, cloth swishing and button snapping.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

<!-- STATS_END -->
