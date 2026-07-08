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
- Total Prompts: **5242**
- Updated Today (UTC 2026-07-08): **0**

## 🎬 Today's Updates
### 🎬 Green Bear Encourages Robot On Slide
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05264.jpg" width="480" alt="SD2_05264"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/green-bear-robot-slide-SD2_05264">🌐 Watch Online</a>

#### 📝 Prompt
```
montage, multi-shot 3D animated feature film, Don't use one camera angle or single cut, vibrant glossy CGI render, Pixar-quality stylized animation, expressive cartoon character performance, subsurface-scattered fur, soft cinematic lighting, sharp focus, high detail texture, depth of field mastery, warm sunny daylight, soft pastel playground palette In a sunny stylized playground full of pastel mushroom-houses, a colorful slide and leafy trees under a bright blue sky, a big chubby green fuzzy bear in a green t-shirt reading "Higgs" crouches beside a small rounded yellow retro robot with a single round eye-lens and a thin antenna topped by a little gold ball. The look is warm Pixar-quality stylized 3D animation — soft fur, glossy surfaces, playful expressive character performance, shallow depth of field, gentle golden daylight. Shot 1: Medium shot with a smooth playful push-in, the green bear crouches warmly beside the little yellow robot at the foot of a tall colorful slide and gives him a gentle reassuring pat. Beaming, he says: "Come on, little buddy — you've got this!" Shot 2: Close-up, the little yellow robot's round eye-lens widens and its antenna ball wobbles nervously as it cranes up at the towering slide. In a small wavering beep of a voice it says: "B-but it's so high..." Shot 3: Wide low-angle looking up the slide, the bear gently lifts the little robot to the very top where it peeks over the edge, the sunny pastel playground spread out far below. The bear calls up cheerfully: "I've got you. Ready? Three... two..." Shot 4: Tracking shot racing alongside, the little robot zips down the curving slide with a delighted whirring squeal, antenna flapping wildly and tiny arms flung in the air, sunlight flaring off its glossy yellow shell. Shot 5: Medium shot, the robot launches off the end of the slide and sails through the air in a little arc before landing with a soft poof straight into the big bear's outstretched fuzzy arms, both tumbling back onto the soft grass in a happy heap. Shot 6: Close-up two-shot, the bear and the little robot lie giggling in a pile on the grass, the robot's antenna spinning happily as its eye-lens sparkles. Bursting with joy it beeps: "Again! Let's go again!" Total: 15s / 6 shots / 16:9
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.04s`

---

### 🎬 Black Hole Devours Steam Truck
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05263.jpg" width="480" alt="SD2_05263"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/black-hole-steam-truck-SD2_05263">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: 8K cinematic. Photorealistic — no 3D render, no game engine, no game-cutscene aesthetic. Cinematography: high-velocity master cinematography. Extreme depth compression. Lighting: Blinding, violent accretion light. Pure, absolute dark of the singularity vs. the intense, searing golden-white light of the tearing accretion disk. Backlit dust and debris. Color: 60:30:10 — dominant pitch-black space and void 60% / secondary blinding golden-white and amber solar fire 30% / accent electric blue energy arcs from snapping tethers and dark soot 10%. Camera: Physical cine lens. 180° shutter motion blur. Intense handheld operator shake, violently reacting to gravitational micro-shocks. Physics: Gravity, inertia, and extreme tidal forces respected — debris accelerates exponentially as it nears the center, heavy vehicle weight distribution on the crumbling bridge. SUBJECTS: - @truck: a heavily armored, multi-wheeled steam-powered leviathan-hauler, built from riveted brass and dark iron, soot pouring from massive exhaust stacks, racing across a collapsing stone bridge. A lone operator is exposed on the rear platform, desperately cutting heavy mooring cables. - @singularity: a micro-black hole dominating the background, a perfect sphere of absolute blackness ringed by a violently spinning, chaotic accretion disk of crushed matter. LOCATION: A crumbling aerial archipelago of floating islands, connected by colossal, rusting iron chains. The environment is being actively torn apart and sucked into the horizon. ACTION — ONE CONTINUOUS TAKE, single unbroken handheld tracking shot from the truck’s rear, NO cuts. 15 seconds. - 0:00–0:05 — Tight medium shot on the rear of @truck: looking past the frantic operator as the vehicle violently bounces over snapping stone pavers. Massive, multi-ton iron chains behind the truck snap with violent whiplash, flying out of frame. - 0:05–0:10 — Slow, continuous zoom-in past the truck, tilting down into the abyss: the camera moves past the vehicle to lock onto the terrifying void of @singularity. Entire floating islands and ancient stone castles in the background are seen ripping apart like paper, their fragments aligning into glowing, white-hot spirals. - 0:10–0:15 — Extreme close-up telephoto view of the accretion edge: the frame is filled with a chaotic vortex of superheated metal, swirling space dust, and blinding friction fire. Huge chunks of rock are stretched into long, glowing threads before vanishing into the pitch-black center. Horizontal optical flares streak across the screen. CONSTRAINTS: 16:9 anamorphic widescreen scale. ONE CONTINUOUS SHOT — absolutely NO hard cuts. Telephoto lens compression. Default real-time. Dust, smoke, and debris obey gravitational pull and extreme speed vectors. Photoreal throughout. AUDIO: NO MUSIC. SFX ONLY — deafening, low-frequency gravitational hum, the screaming screech of tearing iron and snapping mega-chains, the violent chugging roar of the truck's steam piston engine, high-pressure steam venting, sonic cracks of breaking stone islands, and the terrifying, hollow wind-like roar of matter collapsing into the void.
```

#### 📌 Details
- Ratio: `2.33` | Duration: `15.04s`

---

### 🎬 Magical Barrier Shatters Under Dark Horde
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05262.jpg" width="480" alt="SD2_05262"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/magical-barrier-canyon-battle-SD2_05262">🌐 Watch Online</a>

#### 📝 Prompt
```
Sweeping wide shot of an immense magical barrier of glowing energy cracking apart across a canyon as armored defenders brace behind it and a dark horde surges on the far side. Handheld camera shakes along the line with an urgent jolt, snapping from the barrier splintering into shards of light to soldiers raising shields against the breach to mages straining to hold the failing wall. Fragments of energy rain down, dust erupts from the canyon floor, the horde pours through the gap. Cold stone grays and brilliant pale-gold light, vast desperate scale and chaos. 16:9, 10 seconds.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 Rooftop Hurricane Run
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05261.jpg" width="480" alt="SD2_05261"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rooftop-hurricane-run-SD2_05261">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: 8K cinematic. Photorealistic — no 3D render, no game engine. Cinematography: Rooftop chase handheld — camera operator running along the roof of a moving train at 200 km/h, the lens catching the @runner from behind and alongside as they sprint toward the front of the train against the direction of travel. The wind at 200 km/h makes the operator's movement specific — low, pressed against the train roof, moving in the specific crouch-sprint of someone in extreme wind. When the train passes through tunnels, the frame goes absolute black for the tunnel duration before emerging into the specific light of whatever environment the next section is in. Lighting: A fantasy train route through four distinct environments in 15 seconds — each environment has its own lighting character, and the transitions between them are hard, immediate cuts of light quality as the train passes through tunnels between sections. Section 1 (0:00-0:04): open desert at night, the specific dark of a desert sky with no light pollution, the train's own headlight the primary source creating a sharp forward cone. Section 2 (0:04-0:08): through a tunnel, absolute dark, the train's interior light visible through the roof hatches as amber-orange strips. Section 3 (0:08-0:12): emerging into a vast cavern lit by bioluminescent formations — the specific deep blue-green and violet of bioluminescent rock formations at scale, enormous, the train small within them. Section 4 (0:12-0:15): bridge over open void — the sky visible above and below, deep star-filled black on both sides. Color: Section 1 — dominant desert night-black and the sharp amber-gold of the train's headlight cone. Section 2 — absolute black and amber-orange interior light through hatches. Section 3 — deep blue-green and violet bioluminescent cavern, the train surfaces lit from every direction simultaneously. Section 4 — absolute star-black above and below, the train surface the only non-black element. Camera: Physical ultra-wide anamorphic cine lens (11mm). 180° shutter motion blur. Rooftop crouch-sprint handheld in extreme wind — every movement costs enormous effort against 200 km/h wind resistance. Speed-ramping (24fps to 240fps and back) at the moment the @runner reaches the front of the train and the obstacle they are running toward becomes fully visible. Tunnel transitions are physical — absolute darkness for the tunnel duration, the camera recovering each time the train emerges. Physics: Real 200 km/h rooftop physics — the wind pressure against a person on a train roof at 200 km/h is a continuous, total force equivalent to a category 3 hurricane. The specific body mechanics of moving against this force: the crouch-sprint, the center of gravity below the wind's maximum pressure, the specific grip required to maintain position. The train's vibration at speed — the specific high-frequency vibration of a train at 200 km/h transmitted through the roof surface into any contact point. SUBJECTS: @runner: A young woman — she is on the roof of this train because the interior of the train is no longer accessible to her, and the front of the train contains something that the train reaching its destination will destroy. She has four carriages to cover before the train reaches the tunnel at the end of Section 3. Her gear: nothing specific — she left wherever she was in a hurry. Her movement on the train roof: the specific physical problem of sprint-running against 200 km/h wind on a vibrating surface with no handholds, solved by the specific technique of someone who has calculated that the alternative is worse than the current physical difficulty. @train: A large, fast fantasy locomotive — its design the specific aesthetic of a train built for long-distance speed rather than passenger comfort, the roof profile low and smooth with the specific aerodynamic shaping of a vehicle designed to move through air at high speed. Its power system visible at the front as a deep, violet-blue energy emission from the locomotive's leading element — the power source that makes this train the fastest thing on these tracks and also, at the moment, the most dangerous. LOCATION: A fantasy rail route passing through four environments in rapid succession. The train is at maximum speed — 200 km/h. The @runner has the length of three carriages — approximately 75 meters — to cover in the time available before the train reaches the point of no return. ACTION — ONE CONTINUOUS TAKE, single unbroken handheld shot, NO cuts. 15 seconds. 0:00–0:04 — Desert night, full sprint (24fps): Camera running behind and alongside the @runner on the train roof — the desert night sky above, the desert floor visible far below on both sides as the train's headlight cone illuminates the track ahead, the sand and rock of the desert night passing at 200 km/h. The wind at this speed: the @runner's clothes and hair in the specific violent motion of 200 km/h wind, the camera operator experiencing the same force, the camera shake the compound shake of running-on-a-vibrating-surface plus wind resistance. The @runner's sprint: the specific low, driving movement of someone running against maximum wind resistance — not the upright sprint of a track athlete, the specific forward-angled, ground-hugging sprint of someone for whom the wind is a wall they are running through. Her hands: not pumping normally, pressed partially forward to cut through the wind, the specific adaptation of sprint mechanics to extreme wind resistance. First carriage covered. Two remaining. The tunnel mouth visible ahead as an absence of stars — the specific visual of a tunnel entrance seen at night at 200 km/h, the stars ending in a sharp line where the tunnel begins. 0:04–0:08 — Tunnel, absolute dark (24fps): The train enters the tunnel — the frame going absolute black in one frame, the desert night replaced by tunnel dark. The only light: amber-orange strips through the roof hatches of the train below — the interior light visible as lines in the black, the train's interior passing below the camera at 200 km/h, the hatch strips creating a stroboscopic effect as they pass. The @runner visible only in the amber-orange hatch light as she passes over each hatch — brief illuminations of her legs, her torso, her hands on the roof surface, then dark again. The wind unchanged — 200 km/h in the tunnel is 200 km/h in the dark, the camera shake unchanged, the operator running blind. The tunnel walls: invisible, implied by the echo character of the sound, the train in a tube of stone at 200 km/h. A light ahead: the tunnel exit. Growing. 0:08–0:12 — Bioluminescent cavern (24fps): The train exits the tunnel into the cavern — the frame going from tunnel-black to the specific deep blue-green and violet of bioluminescent rock formations at scale. The cavern: enormous, the train small within it, the bioluminescent formations covering the ceiling and walls at heights of hundreds of meters, their light omnidirectional and deep. The @runner in this light: the bioluminescence reaching every surface equally, the specific visual of a person lit from every direction simultaneously in blue-green and violet, the shadow situation extraordinary — multiple competing shadows in different colors from different light sources. The formations at train speed: the close formations blurring, the distant ones moving slowly, the specific depth parallax of a large space at 200 km/h. The train's violet-blue power emission visible ahead for the first time — the front of the train approaching, the power source's violet-blue competing with the cavern's bioluminescence. The third carriage behind them. One remaining. The tunnel at the far end of the cavern visible as the next absolute black — the exit. The @runner accelerating. 0:12–0:11 — Speed-Ramp: The train exits the cavern — the bioluminescent blue-green cut off by the tunnel, absolute black again, brief, then the tunnel exits onto the bridge. The bridge over the void: the sky above and below both absolute star-filled black, the bridge structure — narrow, the minimum material required — the only non-black element, the train on it a single object suspended between two darknesses. The @runner emerges onto the bridge section and sees, for the first time, what is at the front of the train — the locomotive's forward element, the violet-blue power emission at maximum output, and ahead of it, the bridge ending — not at a station, at a fracture point, the bridge ahead broken, the void below beginning 200 meters ahead, the train at 200 km/h with 200 meters to stop. In the exact millisecond she sees this and her body's sprint-run converts instantaneously to maximum-effort deceleration — from running toward to stopping as fast as possible — time freezes, ramping violently into extreme slow-motion. 0:11–0:15 — Ultra Slow-Motion (240fps) into Speed-Ramp Back: The bridge and the void in slow motion — the star-filled black above and below, the bridge structure, the train on it, the @runner on the train, the fracture point ahead. The @runner's deceleration, slowed: the specific biomechanics of maximum deceleration from sprint speed, the weight shifting backward, the feet going from propulsion to braking, the body's entire kinetic energy being managed through the feet and legs, the specific physics of a person stopping on a vibrating surface at 200 km/h wind resistance that was helping them brake but is now their enemy because they need to stop completely rather than be blown forward. The void below the bridge: visible between the bridge's structural elements as an absolute, total, star-filled black — not empty, the specific visual of open space below a structure at altitude, the stars present as a floor of light infinitely far below. The train's braking systems engaging: the specific visual of a train at 200 km/h beginning emergency braking — the brake system's friction visible as orange-white heat at the wheel contacts, the vibration of emergency braking conducting through the roof surface and into the camera and the @runner's feet simultaneously. The bridge fracture point ahead: 200 meters at 200 km/h is 3.6 seconds, and the train is braking, and the calculation is not yet resolved. The star-filled void above: identical to the void below, the bridge suspended between two identical darknesses. The @runner's hands finding the roof surface — gripping, the specific grip of someone making the calculation that if the train stops in time she needs to survive the deceleration, and if it does not stop in time she needs to not be on it. Blinding horizontal violet-blue and star-white anamorphic flares cross the full lens element slowly from the power emission and the void stars. Time snaps back: the train braking, the @runner braking, the fracture point approaching, the calculation still unresolved, the void on both sides, the stars above and below, the bridge structure between them, the speed decreasing, the distance decreasing, both decreasing, the outcome determined by which decreases faster, and the camera is still running, still on the roof, still catching the @runner's face as she watches the edge come, the speed dropping, the edge coming, the stars below absolute and patient. CONSTRAINTS: 16:9. ONE CONTINUOUS SHOT — NO cuts. Speed-ramp to 240fps at the moment the @runner sees the fractured bridge — the decision point, not the impact. The four environmental transitions must be hard and immediate — the tunnel entrances are one-frame cuts from one environment to absolute black, the exits one-frame cuts from black to the new environment. The wind physics must be consistent and visible throughout — the @runner's movement against 200 km/h wind is the constant physical challenge of every section. The bioluminescent cavern must be visually extraordinary — the specific deep blue-green and violet of real bioluminescence at architectural scale. The bridge section void must be genuinely vertiginous — star-filled black above and below, the bridge the only structure. Photoreal wind physics, tunnel acoustics, and train mechanics throughout. AUDIO: NO MUSIC. SFX ONLY — a train at 200 km/h experienced from the roof: the wind, which at 200 km/h is a total, continuous, high-pitched roar that is also a physical force, not weather but physics. The train's vibration conducted through the roof surface into the camera — the specific high-frequency vibration of a train at maximum speed, omnidirectional, continuous. The power emission: a deep, directional, violet-blue tone from the front of the train — the specific sound of the train's power system at maximum output, present throughout but growing as the @runner approaches it. Section 1 desert: the wind and the train, the desert acoustic below — thin, dry, the sound of a desert at night at high speed. Tunnel sections: the tunnel acoustic — the wind now reverberating off close walls, the echo character of a tube at 200 km/h, the train interior sounds visible through the hatches audible as a brief acoustic window each time the camera passes a hatch. The bioluminescent cavern: the cavern acoustic — the train's sound echoing off formations hundreds of meters away, the specific reverberation of an enormous biological-mineral space. The bridge section: the wind changes character above an open void — the specific acoustic of wind around a narrow bridge structure over open space, the sound of the void below as an absence of echo from below. Emergency braking: the specific sound of a large train's emergency brake system engaging — the high-pitched screech of braking metal conducted through the bridge structure, the vibration intensifying, the calculation in the sound. During slow-mo: the braking sound stretched — the brake friction a long, structured, escalating tone, the wind decreasing slightly as speed decreases, the power emission maintaining, the void silent, the stars silent, the outcome still unresolved.
```

#### 📌 Details
- Ratio: `2.33` | Duration: `15.04s`

---

### 🎬 Epic Microscopic War Inside Blood Vessel
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05259.jpg" width="480" alt="SD2_05259"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/blood-vessel-cell-warfare-SD2_05259">🌐 Watch Online</a>

#### 📝 Prompt
```
Sweeping wide shot of two colossal armies clashing inside a vast blood vessel, the curving translucent vessel wall arching across the frame like a ringed planet of living tissue. The combatants are organic and asymmetrical — immense amoeboid macrophages with rippling membranes and reaching pseudopod limbs, their cytoplasm threaded with bioluminescent seams that pulse as they engulf and strike, set against bristling viral swarms of spiky icosahedral capsids and crowned spike-proteins, all uneven spires and barbed fibers. Smaller craft are biconcave red blood cells — flattened ring-shaped discs that spin and bank, leaving spiral trails through a drifting debris field of cell fragments and fibrin strands. Handheld camera drifts and shakes amid the chaos, snapping from a giant infected cell's membrane cracking open under a concentrated viral assault to a swarm of red cells corkscrewing past a lysed husk. Plasma currents lash the frame, cells burst silently and collapse inward, fresh virions scatter like spores from a dying host cell. Deep crimson and slate-blue plasma, burning white antibody flares, vast cinematic scale and relentless motion. 16:9, 10 seconds.
```

#### 📌 Details
- Ratio: `2.33` | Duration: `10.04s`

---

### 🎬 Ice Titan Emerges From Glacier Battle
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05258.jpg" width="480" alt="SD2_05258"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ice-titan-glacier-battle-SD2_05258">🌐 Watch Online</a>

#### 📝 Prompt
```
Sweeping wide shot of a mountain-sized titan of ice and stone tearing itself free from a glacier as an army of armored warriors scrambles across the frozen valley below. Handheld camera shakes hard with each cracking movement, snapping from sheets of ice shattering off the titan's shoulders to soldiers diving from collapsing crevasses to a war-horn blaring across the field. Snow erupts in vast plumes, glowing runes flare along the titan's limbs, the whole glacier splinters apart. Stark whites and frozen blues, crushing primordial scale and chaos. 16:9, 10 seconds.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 Pandora Alien Ocean FPV Dive
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05257.jpg" width="480" alt="SD2_05257"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pandora-alien-ocean-fpv-dive-SD2_05257">🌐 Watch Online</a>

#### 📝 Prompt
```
FPV underwater flight through Pandora-like alien ocean, using the reference image. Smooth cinematic camera gliding between glowing coral reefs, translucent jellyfish, colorful alien fish, massive rock arches and sun rays in turquoise water. The camera dives through a canyon, passes under bioluminescent plants, then emerges into a majestic underwater valley. Photorealistic, magical, immersive, ultra wide angle, volumetric light, realistic water physics, 4K cinematic, dreamlike alien world, no recognizable characters.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.04s`

---

### 🎬 Exosuit Pilot Battles Alien Dreadnought
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05256.jpg" width="480" alt="SD2_05256"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/exosuit-dreadnought-battle-SD2_05256">🌐 Watch Online</a>

#### 📝 Prompt
```
STYLE: 8K photorealistic, anamorphic widescreen, original sci-fi blockbuster grade, fine film grain, hyperdetailed. Photorealistic — no 3D render, no game engine, no game-cutscene aesthetic. CINEMATOGRAPHY: naturalistic master cinematography, kinetic aerial-combat coverage, handheld operator energy motivated by concussive blasts. LIGHTING: cold neon-cyan key from the exosuit's glow; blinding fiery orange-red from explosions; hard electrical-blue energy arcs; volumetric smoke and beam-light; lens catching sparks and ember-streaks. COLOR: 60:30:10 — dominant deep space-indigo and steel-blue (sky & warship hull) 60% / secondary fiery orange-red (explosions & engine cores) 30% / accent electric exosuit-cyan and weapon-blue 10%. Vibrant, high-contrast. CAMERA: physical cine lens, 180° shutter motion blur, continuous handheld shake motivated by shockwaves; a fast tracking dodge, a hard zoom on the shield flare, a rack-focus, a crane-back to scale. Never static. MATERIAL: material-level realism — scratched battle-scarred exosuit alloy plating, a rippling translucent energy shield, molten twisting warship debris, glowing thruster vents streaking, sparks and ash raining and clinging to the lens. PHYSICS: gravity and inertia respected — the pilot's evasion carries real G-force weight, debris falls and tumbles with immense mass, the energy shield ripples and distorts on impact, shockwaves warp the smoke with aerodynamic drag, thruster-wash streaks with velocity. ACTING: the pilot twists and rolls through the chaos with desperate precision, head snapping to track incoming fire, body bracing as the shield takes a hit, then powering upward clear of the blast with locked focus. CHARACTER DESIGN (original, not based on any franchise): - PILOT: a lean figure in a sleek battle-scarred exosuit, glowing cyan energy lines, a reflective glowing helmet visor, thruster packs venting blue flame. - WARSHIP: a colossal alien dreadnought, dark riveted alloy lattice, glowing red-orange power-cores, massive energy-beam emitters, shedding fire and debris as it's hit. CONTINUITY: SAME pilot, SAME warship, SAME sky across all cuts. The warship firing in CUT 1 is the exact one that detonates in CUT 4. The battle stays in the same airspace from start to finish. TECHNICAL: 24fps real-time, slow-motion on the opening dodge and the final detonation only, ultra high detail, motion accelerating from a violent evasion into a scale-revealing pull-back. AUDIO (diegetic only, NO MUSIC): the deep thruster roar, concussive layered explosions, the electrical crackle and hum of the shield, a sharp warning klaxon, debris pinging and screeching off the suit, the subsonic groan of the breaking warship. SCENE CONTEXT A lone exosuit pilot weaves through a storm of fire and falling wreckage as a colossal alien warship fires energy beams overhead; the pilot dodges a blast, the shield flaring, then rockets clear as a beam detonates a chunk of the dreadnought. LOCATION MAP Foreground: the pilot's exosuit and rippling shield, streaking sparks. Midground: falling molten wreckage and energy beams. Background: the colossal warship firing, a vast burning fleet in deep space-sky. Camera: tracking dodge with the pilot → zoom on the shield-flare → rack-focus to the visor → crane-back to the fleet. FIRST FRAME / BLOCKING The exosuit pilot blasting upward across frame, an explosion erupting a hair behind, debris and fire streaking toward the lens, the warship's glowing emitters flaring in the background. FORMAT MODE Sequence of 4 cuts, no timecodes in output. Cuts only at the specified points; the camera does not cut on its own. OPTICS CUT 1 — MS tracking, the pilot's upward blast. CUT 2 — WS tracking through wreckage. CUT 3 — CU rack-focus to the visor. CUT 4 — EWS crane-back on the fleet. No drift mid-segment. CAMERA (per cut) A fast tracking dodge following the pilot, a weaving track through falling debris, a rack-focus from shield to face, then a wide crane-back revealing the fleet. ACTION (per cut) CUT 1 (~3s, slow-motion dodge): IN-MEDIAS-RES the pilot BLASTS upward across frame as an explosion erupts a hair behind, debris and fire blasting toward the lens, thruster-wash streaking. CUT 2 (~5s, real-time weave): slow tracking shot following the pilot weaving through falling molten wreckage, deep focus holding the battered suit plating in foreground AND the colossal warship firing energy beams huge in the background at once, embers and ash streaking. CUT 3 (~3s, rack-focus): the camera rack-focuses from a rippling shield-flare to the pilot's tense face inside the glowing helmet, micro-detail on the cracked visor and skin razor-sharp. CUT 4 (~4s, slow-motion payoff): a colossal beam detonates a chunk of the warship, the pilot rocketing clear as the camera cranes back to reveal the immense burning fleet in deep layered Star-Wars-scale spectacle. Hold. Hard cut to black. PHYSICS The dodge carries real G-force inertia; debris falls with mass and tumbles; the shield ripples and distorts on impact; the detonation throws molten wreckage with drag; thruster-wash streaks with velocity. The fight stays in the same airspace — no ground transition, no scene change. LIGHTING Cold cyan exosuit key, blinding orange explosion fill, electrical-blue arcs, volumetric beam-smoke; WB cool-vs-warm. No flat light, no clean color. POSITIVE LOCKS SAME pilot, SAME warship, SAME sky every cut. CRITICAL: the warship firing in CUT 1 is the exact one that detonates in CUT 4 — hold its design and glowing cores. The battle STAYS in the airspace — the pilot dodges, the shield flares, the warship is hit, but the action NEVER changes location. Space-indigo dominant; the cyan-lit pilot and fiery explosions are the saturated subjects. Total: 15s / 4 cuts / 16:9
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.04s`

---

### 🎬 Sky Pirate Leviathan Duel
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05255.jpg" width="480" alt="SD2_05255"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sky-pirate-leviathan-duel-SD2_05255">🌐 Watch Online</a>

#### 📝 Prompt
```
A boundless sky of towering sunset thunderhead canyons, two colossal whale-like sky-leviathans gliding between clouds, lightning within. HERO: a sky-pirate in a long coat and goggles standing on the back of a flying skiff. (0-5s) sweeping aerial through a cloud canyon revealing the skiff racing alongside a leviathan. (5-10s) tight close-up: the hero leaps from the skiff onto the leviathan's back, draws a cutlass and clashes with a rival boarder, sparks flying. (10-15s) the duel as the leviathan rolls; the hero parries, kicks the rival off, and rides the leviathan up through a shaft of sunset light, coat streaming. Camera: sweeping aerial then handheld duel close-ups with a controlled orbit on the clash, anamorphic lens. Smooth fluid 24fps cinematic motion, motion-blurred but smooth, no stutter, no strobing. Lighting: warm sunset key, cool cloud shadow, creature glow, lightning glints. Epic amber-and-teal grade, fine grain, halation, anamorphic flare. Audio: soaring score, deep leviathan song, clashing steel, wind, distant thunder.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.04s`

---

### 🎬 Abyssal Leviathan Awakens In Deep Trench
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05254.jpg" width="480" alt="SD2_05254"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/abyssal-leviathan-awakens-SD2_05254">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: 8K cinematic. Photorealistic — no 3D render, no game engine, no game-cutscene aesthetic. Cinematography: naturalistic deep-sea master cinematography. Underwater particle drag. Lighting: High-contrast abyssal murk. Cold, piercing bio-plasma light from the creature vs. weak, warm halogen lights of the vehicle. Heavy volumetric marine snow and silt haze. Color: 60:30:10 — dominant pitch-black and deep navy abyssal water 60% / secondary eerie bioluminescent cyan and electric blue 30% / accent warning-red strobes of the rover 10%. Camera: Physical cine lens. 180° shutter motion blur. Handheld operator micro-shake, shifting dynamically with underwater shockwaves and currents. Physics: Hydrodynamics and inertia strictly respected — heavy silt displacement, slow-moving massive currents, correct contact shadows on the seabed. No floating props without buoyancy physics. SUBJECTS: - @rover: a heavy, industrial multi-treaded deep-sea drilling rover, rusted and covered in oceanic grime, fighting immense water drag as it crawls over a pitch-black trench floor, its halogen headlights cutting weak cones into the silt. - @leviathan: a colossal, planetary-scale biomechanical marine entity forming the literal tectonic ridge behind the rover, its ancient skin a texture of volcanic rock and chitin. LOCATION: The absolute bottom of an alien ocean trench. Massive hydrothermal vents emitting black smoke on the right. The ground is covered in carpets of faint phosphorescent filaments that crush under the treads. ACTION — ONE CONTINUOUS TAKE, single unbroken handheld tracking shot, NO cuts. 15 seconds. - 0:00–0:05 — Medium shot tracking alongside @rover: the heavy machine struggles against a powerful bottom current, its treads throwing up massive clouds of dark silt. Behind it, the abyssal trench floor suddenly buckles and rises. - 0:05–0:10 — Slow continuous zoom-out and tilt-up: the camera pulls back, revealing that the rising ridge is the shifting armor of @leviathan. A town-sized slit snaps open on the creature’s side, revealing a massive, pulsing bioluminescent cyan eye. The water around it warps from extreme heat. - 0:10–0:15 — Settles into a compressed telephoto wide view: the frame is dominated by the giant glowing eye, within which the tiny silhouette of the fleeing rover is sharply reflected. Kilometrous vents around the eye erupt with blinding blue bio-plasma, spinning the water into massive underwater tornados that rip past the camera lens. CONSTRAINTS: 16:9 anamorphic widescreen scale. ONE CONTINUOUS SHOT — absolutely NO hard cuts. Telephoto compression. Default real-time. Volumetric water, marine snow, and silt obey fluid dynamics. No eye glow on the vehicle. Photoreal throughout. AUDIO: NO MUSIC. SFX ONLY — deep, bone-rattling low-frequency underwater groans, the heavy mechanical clanking and high-torque whine of the rover's engines, underwater turbulence roaring, violent volcanic rumbling, and the high-pitched hiss of superheated water boiling against the deep-sea hull.
```

#### 📌 Details
- Ratio: `2.33` | Duration: `15.04s`

---

### 🎬 Dragon Hunter's Last Stand
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05253.jpg" width="480" alt="SD2_05253"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dragon-hunter-last-stand-SD2_05253">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: 8K cinematic. Photorealistic — no 3D render, no game engine, no game-cutscene aesthetic. Cinematography: Aggressive, desperate handheld master shot. Camera operator physically running and diving for cover, lens constantly buffeted by shockwaves, reactive dutch tilts under stress, focus breathing on every impact. Never locked, never clean — a war correspondent in a fantasy battlefield. Lighting: Catastrophic bioluminescent jungle twilight. The dense alien canopy filters the dying red sun into deep amber-crimson god-rays. The @dragon's acid breath illuminates the entire scene from below in violent, sickly neon-green — casting upward shadows on every surface, inverting the natural lighting logic and making every figure look wrong. Color: 60:30:10 — dominant deep blood-red and shadow-black jungle canopy 60% / secondary violent neon-green acid light from dragon breath 30% / accent blinding white sparks from shattered enchanted armor and bone-white lightning arcs 10%. Camera: Physical wide anamorphic cine lens (18mm). 180° shutter motion blur. Masterfully executed speed-ramping (24fps to 240fps and back). Severe horizontal neon-green anamorphic lens flares from every acid burst. Physics: Gravity, mass, and fluid dynamics strictly respected — acid splashes behave with real surface tension and viscosity, dragon limbs move with immense reptilian inertia, shockwaves from wingbeats flatten the jungle canopy in visible pressure rings. SUBJECTS: @hunter: A lone, battered female dragon hunter — tall, lean, wearing scorched leather armor reinforced with salvaged dragon-scale plates still faintly glowing at the edges. No fantasy embellishment — her gear is practical, damaged, functional. Face streaked with soot and luminous green acid burns on her left forearm. Moves with desperate precision, not heroic grace. @dragon: A massive, low-profile ambush predator — not a classic European dragon. Its body is long and sinuous, built like a 30-meter saltwater crocodile with six limbs and a broad, flat skull. Its scales are matte black with hairline cracks between each one leaking constant sickly neon-green acid light. It moves fast, low, and intelligent — a hunting animal, not a monster. LOCATION: A vast alien jungle on a dying world — the trees are enormous, hundreds of meters tall, their bark deep arterial red, their canopy so thick it creates a false twilight at ground level. The jungle floor is carpeted with enormous bioluminescent fungi that pulse dim violet and amber underfoot. Ancient, collapsed ruins of an unknown civilization are overgrown and barely visible — cracked stone columns, half-buried archways. The air is thick with glowing acid vapor from the dragon's prior attacks. ACTION — ONE CONTINUOUS TAKE, single unbroken handheld tracking shot, NO cuts. 15 seconds. 0:00–0:05 — Medium tracking shot on @hunter (24fps): Camera runs alongside her at chest height as she sprints low through the ruins, the @dragon's mass visible as a fast, terrifying shape between the tree trunks to her right — closing. She dives behind a collapsed stone column. The dragon's acid spray hits the column she just vacated, and the stone dissolves instantly in a boiling neon-green splash. Camera shakes violently from the shockwave, lens catching a direct hit of acidic vapor — the glass element briefly hazes over before clearing. 0:05–0:06 — Speed-Ramp: She rises from cover, draws a heavy iron-tipped lance from her back, and plants her feet in the mud. In the exact millisecond the dragon lunges directly at her — its jaw opening into a gape of pure green fire — time freezes, ramping violently into extreme slow-motion. 0:06–0:12 — Ultra Slow-Motion (240fps): The dragon's lunge hangs suspended mid-air. Its six limbs are caught fully extended, individual claws hyper-visible, each scale hairline crack pulsing with trapped green light. The acid beginning to pour from its open jaw has frozen into a slow, glowing river of neon-green liquid catching the crimson god-rays from above and refracting them. The hunter's lance tip is extended toward the incoming mass. Violent horizontal neon-green anamorphic flares streak slowly across the full lens element. Bioluminescent fungi spores from the shattered jungle floor drift upward in slow golden clouds. Every detail hyper-sharp — the micro-texture of ruined stone, the individual scales, the hunter's knuckles white on the lance. 0:12–0:15 — Speed-Ramp Back (24fps): Time snaps violently back. The dragon's full mass slams into her position — the camera is thrown sideways by the shockwave, spinning and reorienting. Through the chaos, a single moment: her lance buried deep, green fire erupting in all directions, and the dragon's shriek shaking the entire frame. The camera settles, low, in the acid mist — outcome unclear, both figures lost in the neon-green haze. CONSTRAINTS: 16:9 anamorphic widescreen. ONE CONTINUOUS SHOT — NO cuts. Speed-ramp to 240fps and back. Handheld never stabilized — constant motivated shake. Neon-green acid light must compete with and frequently overpower the ambient red. Photoreal throughout. AUDIO: NO MUSIC. SFX ONLY — the deafening wet roar of the dragon's movement through dense jungle, snapping ancient trees like dry wood. The hiss and sizzle of acid dissolving stone. The hunter's ragged, controlled breathing. At 0:05, the dragon's lunge produces a colossal wingbeat shockwave — a deep infrasonic thud. During slow-mo (0:06–0:12), all ambient sound drops into a thick muffled vacuum, replaced by a deep, resonant hum from the acid energy and the hunter's own amplified heartbeat. At 0:12, a world-ending reptilian shriek and the wet, catastrophic impact — followed by the hiss of expanding acid steam swallowing the frame.
```

#### 📌 Details
- Ratio: `2.33` | Duration: `15.04s`

---

### 🎬 Bone Dragon Awakens
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05252.jpg" width="480" alt="SD2_05252"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/bone-dragon-awakens-SD2_05252">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: 8K cinematic. Photorealistic — no 3D render, no game engine, no game-cutscene aesthetic. Naturalistic master cinematography of a swarm of colossal armored insects in mass combat. Cinematography: Naturalistic master cinematography. Physical cine lens, ultra-wide 21:9 anamorphic framing. Macro-scale realism applied to titan-scale creatures. Lighting: Surrealistic, vibrant alien twilight. High-contrast dramatic light. (single continuous take — "phases" = beats within one unbroken camera move) PHASE 1 (00:00–00:02) — Dead Wasteland / Entering Frame EFFECT: slow low-height dolly-in + subtle handheld drift + drifting snow (ground spindrift) A lifeless icy wasteland, low overcast light, desaturated grey-blue grade, mist hugging the ground. Camera at knee height creeps slowly forward across the snow. The hero's legs in dark spiked armor enter frame from above; camera holds the low angle. Speed: ~85% (slightly slowed, heavy footfalls). Transition out: camera begins a smooth crane-up along the body. PHASE 2 (00:02–00:04) — Hero Reveal EFFECT: vertical crane-up (tilt-reveal) + wind animation on hair/cloak Camera rises from legs to torso to head: horned helmet, rune-etched sword glowing cold blue in hand. Long white hair and torn cloak whip in the headwind. Camera settles to a three-quarter/over-the-shoulder framing, holding the hero in the right third. Speed: normal. Transition: the hero stops — camera freezes (micro-hold). PHASE 3 (00:04–00:05) — The Wind-Up EFFECT: slight push-in + speed ramp (brief deceleration at the peak of the swing) The hero raises the sword high overhead, muscles and armor straining, the blade's runes flaring brighter. Camera tilts slightly (low Dutch ~10°) to add weight to the strike. Speed: accelerates to ~120% on the wind-up, then brakes just before impact. Transition: sharp downward acceleration. PHASE 4 (00:05–00:06) — SWORD INTO THE ICE EFFECT: impact frame + camera shake (high-frequency vibration) + ice-shard burst + blue light flash from the point of impact The sword drives into the ice with full force. From the strike point — a burst of shards and frost, a short blue flash racing up the blade. Camera takes a sharp jolt (whip-shake), motion blur. Speed: moment of contact ~30% (snappy slow-mo), then instant return to normal. Transition: camera dives down toward the ice surface, following the fracture. PHASE 5 (00:06–00:09) — The Crack Race ← SIGNATURE VISUAL EFFECT EFFECT: high-speed ground-tracking (camera races over the ice chasing the crack) + motion blur + branching fracture The crack rips across the ice away from the hero, branching like a web. The camera flies over it at speed, blue light pulsing deep within the chasm. Low height, aggressive forward dolly, ice flashing past beneath the lens. Speed: ~130–140% (accelerated chase). Transition: the crack hits the base of the massive ice mountain — camera tilts up onto the wall. PHASE 6 (00:09–00:11) — The Mountain Fractures EFFECT: tilt-up reveal + slow speed ramp + spreading fracture network + rising internal glow The gigantic ice mountain begins to crack entirely: fractures crawl through the whole mass. From the depths, a cold blue light kindles through the splits. Camera pulls back and rises (crane-back + up), revealing the mountain's scale. Speed: ~70% (heavy, inevitable deceleration before the reveal). Transition: the light focuses into two points — the eyes. PHASE 7 (00:11–00:13) — The Dragon Awakens EFFECT: glow ignition (eye flash) + ice destruction (debris sim) + slight push-in on the skull The blue light in the fractures ignites — the eyes of a colossal bone dragon that slept for thousands of years. With its sheer might it splits the mountain and casts off slabs of ice; debris hurtles toward the camera. Camera nudges in toward the skull-face, then begins to recoil from the scale. Speed: normal, with short micro-slows as the large slabs tear free. Transition: the dragon throws its head toward the sky. PHASE 8 (00:13–00:15) — Blue Flame to the Sky EFFECT: blue fire breath (volumetric flame) + bloom/glow + final crane-out (reveal of scale) The dragon arches its skull back and erupts a column of bright blue flame into the sky, lighting the whole scene in cold light, frost and steam billowing around it. A wide crane-out/rise reveals the dragon's full silhouette over the shattered mountain and the tiny figure of the hero below. Speed: normal, final frame "breathing" slightly (~95%). Resolution: flame and glow — the energy resolves on scale. MASTER EFFECTS INVENTORY DOLLY / FORWARD TRACKING (used 3x) — Phases 1, 5, 7 — the engine of the "single take," carrying the viewer through the scene. CRANE MOVE — up & back (used 3x) — Phases 2, 6, 8 — vertical reveals (hero's body, mountain, final scale). SPEED RAMP (used 4x) — Phases 3, 4, 5, 6 — accel/decel on the wind-up, the strike, the crack chase, and the fracture. CAMERA SHAKE / VIBRATION (used 1x) — Phase 4 — camera jolt at the sword impact. MOTION BLUR (used 2x) — Phases 4, 5 — smear on impact and during the high-speed chase. GLOW IGNITION / BLOOM (used 3x) — Phases 4 (impact point), 6 (light in the mountain), 7–8 (eyes + flame) — blue light as a through-line motif. DEBRIS / SHATTER SIM (used 2x) — Phases 4 (ice shards), 7 (mountain split and ice shed). CRACK PROPAGATION (used 2x) — Phases 5, 6 — branching fracture across the ice and through the mountain, the narrative connective tissue. DUTCH ANGLE (used 1x) — Phase 3 — slight tilt to add weight to the wind-up. VOLUMETRIC FIRE (used 1x) — Phase 8 — blue dragon flame, the climactic effect. EFFECTS DENSITY MAP 00:00–00:04 = LOW DENSITY (dolly-in, crane-up, wind — 3 effects in 4s) 00:04–00:06 = HIGH DENSITY (wind-up ramp, impact, shake, motion blur, ice flash — 5 effects in 2s) 00:06–00:09 = HIGH DENSITY (high-speed tracking, motion blur, branching crack, ramp — 4 effects in 3s) 00:09–00:11 = MEDIUM DENSITY (tilt-up, ramp, rising glow — 3 effects in 2s) 00:11–00:15 = HIGH DENSITY (eye ignition, shatter, push-in, flame, bloom, crane-out — 6 effects in 4s) ENERGY ARC Act 1 (0–4s) — SILENCE AND ANTICIPATION. Minimal effects, a cold dead wasteland, slow camera approach and hero reveal. The viewer "banks" tension — the contrast that makes the strike land. Act 2 (4–9s) — DETONATION AND CHASE. The sword strike is the first peak: shake, flash, contact slow-mo. Immediately after comes the signature beat — the camera racing the crack across the ice. The most kinetic stretch. Act 3 (9–15s) — AWAKENING AND SCALE. Energy doesn't drop, it escalates into something larger: the mountain shatters, the dragon's eyes ignite, the final column of blue flame to the sky. Camera pulls out to reveal scale — the energy resolves not by fading but by unveiling the colossus.
```

#### 📌 Details
- Ratio: `2.33` | Duration: `15.04s`

---

### 🎬 Rider of the Emerald Sky
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05251.jpg" width="480" alt="SD2_05251"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/emerald-sky-rider-SD2_05251">🌐 Watch Online</a>

#### 📝 Prompt
```
A lone rider clings to the back of an immense translucent sky-creature soaring between mountain-sized crystalline spires that drift through an emerald sky. The camera sweeps alongside as one spire fractures and falls directly into their path — then the rider leans hard and the creature banks sharply, threading through the tumbling shards as veils of green light trail behind them. They break clear and accelerate toward the bright horizon. Handheld camera sweeps and shakes with the dive, motes of light streaming past. Vivid jade greens and luminous haze, a single figure navigating monumental spectacle. 21:9, 15 seconds.
```

#### 📌 Details
- Ratio: `2.33` | Duration: `15.04s`

---

### 🎬 Dragon Rider's Bioluminescent Flight
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05250.jpg" width="480" alt="SD2_05250"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dragon-rider-bioluminescent-flight-SD2_05250">🌐 Watch Online</a>

#### 📝 Prompt
```
A vast alien rainforest at night glowing with bioluminescence, spiral trees with pulsing pink and cyan veins, a glowing river. HERO: a young warrior-rider bonded to a large winged dragon-like beast, gripping its neck. (0-5s) low gliding shot through the glowing undergrowth, then a crane up as the rider and beast burst from the canopy. (5-10s) tight over-the-shoulder close-up on the rider banking the beast hard between glowing trees, leaves streaking past, fierce focus on the face. (10-15s) the beast dives toward the glowing river, the rider leaning low, then pulls up in a spray of luminous spores as the camera sweeps wide. Camera: smooth gliding aerial and banking follow, tight rider close-ups, anamorphic lens. Smooth fluid 24fps cinematic motion, motion-blurred but smooth, no stutter, no strobing. Lighting: bioluminescent pink, cyan, violet sources, deep shadows, glow haze. Magical teal-and-magenta grade, fine grain, halation, anamorphic flare. Audio: ethereal pads, beating wings, the rider's exhilarated shout, a soaring orchestral swell.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.04s`

---

### 🎬 Colossal Starfleet Clash
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05249.jpg" width="480" alt="SD2_05249"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/colossal-starfleet-clash-SD2_05249">🌐 Watch Online</a>

#### 📝 Prompt
```
Sweeping wide shot of two colossal starfleets clashing in the void above a ringed gas giant. The warships are organic and asymmetrical — vast curved hulls like blackened whale ribs and barnacled coral, bristling with uneven spires and bioluminescent seams that pulse as they fire. Smaller craft are flattened ring-shaped discs that spin and bank, leaving spiral trails through a drifting debris field. Handheld camera drifts and shakes amid the chaos, snapping from a capital ship's ribbed hull cracking open under a concentrated energy lance to a swarm of ring-craft corkscrewing past a shattered hulk. Plasma arcs lash the frame, explosions bloom silently and collapse inward, escape pods scatter like spores from a dying mothership. Deep slate blues and burning white flares, vast cinematic scale and relentless motion. 16:9, 10 seconds.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

<!-- STATS_END -->
