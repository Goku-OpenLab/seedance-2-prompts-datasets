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
- Total Prompts: **8105**
- Updated Today (UTC 2026-07-21): **78**

## 🎬 Today's Updates
### 🎬 Orbital Collapse Survival Run
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10509.jpg" width="480" alt="SD2_10509"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/orbital-collapse-survival-run-SD2_10509">🌐 Watch Online</a>

#### 📝 Prompt
```
Colossal orbital construction system, synchronized assembly breaks down, turning massive moving parts into lethal, unpredictable motion. Wide shot: perfectly timed mechanical arms moving huge segments into place. Micro-delay: one segment arrives early, barely noticeable at first. Collision: misaligned parts slam together, throwing off timing across the system. Cascade: surrounding arms react too late, desynchronizing the entire structure. Hard dive: small ship enters the assembly zone as motion becomes chaotic. Near-crush: two massive plates slam shut just after the ship passes through. Timing gamble: pilot commits to a gap that’s already closing. Whip movement: a mechanical arm swings unpredictably across the path. Close scrape: ship rolls sideways, barely avoiding full impact. Moving maze: structure still assembling, but incorrectly, paths shifting constantly. Critical moment: a full segment drops into the escape vector. Last-second slip: ship squeezes through a narrowing gap as components collide behind. Rhythm collapse = danger, everything still moving with force but no coordination.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Lighthouse Keeper Storm Rescue
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10508.jpg" width="480" alt="SD2_10508"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/lighthouse-storm-rescue-SD2_10508">🌐 Watch Online</a>

#### 📝 Prompt
```
Hyper-realistic cinematic action sequence, 15 seconds, aspect ratio 16:9. Night. On a remote rocky coast during a violent hurricane, a lighthouse keeper climbs the outside of a tall lighthouse to reach the emergency beacon at the top. The storm is brutal and the situation is urgent. Heavy rain lashes the tower, hurricane-force wind pushes hard against the keeper, and giant waves crash violently into the rocks and the base of the lighthouse. The exterior is simple and clear: wet stone walls, narrow metal ladder sections, exposed railings, a small exterior platform near the top, and the dark emergency beacon housing above. Wide opening shot: the lighthouse keeper steps out onto the exterior of the lighthouse in the middle of the hurricane and immediately begins climbing upward. Rain blasts sideways, wind whips clothing, and huge waves explode against the base of the tower below. Tracking shot: the keeper climbs higher along the outside ladder and narrow metal steps while the storm intensifies. The tower shakes from the force of the sea. Lightning flashes across the sky. The keeper nearly loses grip once, slams against the wall, recovers, and keeps climbing. The beacon above is dark, making the danger feel more urgent. Side shot: the keeper reaches the upper exterior section near the beacon platform. A massive gust hits hard. The keeper clings to the ladder, almost gets pulled away, then forces upward again. Water pours down the stone, the metal steps are slick, and another giant wave crashes into the lighthouse below, shaking the whole structure. Final 5 seconds: the action becomes extreme. The keeper pulls onto the tiny top platform while the hurricane is at full force. The platform rattles, the railing bends slightly under pressure, and the beacon housing swings or shakes in the wind. The keeper struggles across the platform, grabs the beacon assembly, and fights to secure or reconnect it while lightning flashes and spray blasts upward. At the last possible second, the beacon powers back on and cuts through the storm with a powerful beam. Final moment: the lighthouse beacon shines through the hurricane while the keeper clings to the top platform, waves smashing below and rain whipping across the frame. Style: hyper-realistic, cinematic, fast-paced, intense, stressful, clear readable action, strong sense of height and danger, violent hurricane, heavy rain, powerful wind, crashing waves, shaking lighthouse, dynamic but readable camera movement, no text, no logos, no cartoon style, no slow motion, no famous celebrity faces, no recognizable actors, no movie-star resemblance, no public-figure likenesses, no clear facial close-ups. Keep proportions. Keep style and features. Aspect ratio 16:9.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

### 🎬 Parrot Hunts Butterfly in One Shot
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10507.jpg" width="480" alt="SD2_10507"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/parrot-butterfly-bullet-time-SD2_10507">🌐 Watch Online</a>

#### 📝 Prompt
```
Photorealistic cinematic, one single continuous unbroken shot from start to finish — absolutely no cuts, no edits, no transitions, one fluid uninterrupted camera move, 16:9. Bright daylight in a lush green forest, sunlight filtering through the canopy, leaves and tree trunks softly blurred. The shot begins directly behind a vivid colorful butterfly fluttering fast and dynamically through the forest, the camera chasing close behind its wings as it weaves between trees, shafts of light and foliage — erratic, lively and kinetic. Without any cut, in the same fluid motion, the camera keeps racing with the darting butterfly deeper through the trees. Then, at the midpoint, a parrot suddenly bursts in from the side and snatches the butterfly out of the air, biting down and clamping onto the edge of one of its wings in its beak — and the camera sweeps with the strike in one continuous move. Still unbroken, the camera drives in onto the moment of capture and explodes into a dramatic bullet-time effect: time nearly freezes as the parrot's beak bites and clamps onto the butterfly's wing in an extreme macro close-up, the wing bending and creasing in the beak's grip, and the camera sweeps slowly around the frozen instant — shimmering powder and tiny iridescent scales scattering off the pinched wing and hanging suspended motionless in mid-air, the delicate wing membranes and veins razor-sharp, the parrot's beak texture and eye in crisp detail, the butterfly caught mid-flutter — hyper-detailed. One seamless continuous camera move — chase from behind, racing through the forest, into the parrot's strike, ending in a bullet-time orbit around the catch. Flowing and dynamic, collapsing into near-frozen bullet time only at the macro catch. Shallow depth of field, strong motion blur on the chase resolving into crisp frozen detail, bright natural daylight, dappled forest light, high dynamic range, ultra-detailed photorealistic textures — wing scales, powder, feathers, foliage — 4K, high-end wildlife documentary look. Pacing over 10 seconds: about 4–5 seconds of dynamic butterfly flight, the parrot striking around the midpoint, then the rest in bullet-time macro of the parrot biting the wing. 10 seconds, single continuous take.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.0s`

---

### 🎬 Steel Fans Shatter Stone Hammer
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10506.jpg" width="480" alt="SD2_10506"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/steel-fans-vs-stone-hammer-SD2_10506">🌐 Watch Online</a>

#### 📝 Prompt
```
PART 1 — CLASH BEGINS (0:00–0:15) Cut 1 (0:00–0:05) — Fast drone-in, both students already squared off, empty hands raised, wind gusting. Quick alternating close-ups on their eyes, no dialogue yet. Cut 2 (0:05–0:08) — ACTION STARTS. Both sprint toward each other, shouting in sync: Girl: "STEEL—!" Boy: "—OR STONE!" Fast handheld push-in, dust kicking up under their feet. Cut 3 (0:08–0:11) — Both rip weapons from behind their bodies mid-sprint — girl's twin steel war-fans snap open (metallic RING), boy's massive stone-headed hammer swings into frame. Whip-pan cuts between them, full speed. Cut 4 (0:11–0:15) — Boy laughs, hammer cocked back: Boy: "Stone crushes steel, sweetheart!" Girl smirks, doesn't slow down: Girl: "Not today." Low tracking shot chasing her sprint. PART 2 — THE STRIKE (0:15–0:30) Cut 5 (0:15–0:18) — Boy swings the stone hammer down in a massive overhead arc, roaring with effort: Boy: "HAAAH!" Handheld shake with the swing's force. Cut 6 (0:18–0:22) — SLOW-MOTION STRIKE #1: Girl pivots low, both steel fan-blades scissor together and clash directly into the stone hammer-head. Sparks and rock dust erupt. Camera orbits the impact 180° in slow motion. No dialogue — just the grinding stone-on-steel shriek. Cut 7 (0:22–0:25) — Full speed: the stone head cracks and shatters into flying rock shards. Boy's eyes go wide: Boy: "WHAT—" Cut 8 (0:25–0:30) — Shockwave sends him flying backward, tumbling through dirt and stone fragments. Fast cuts: tumble — dust — skid to a stop. Girl stalks forward, fans still crossed, unshaken. PART 3 — FINISH (0:30–0:45) Cut 9 (0:30–0:33) — Boy pushes up on one elbow, dazed, blazer torn, dust on his face: Boy: (coughing, defiant) "...Not bad." Cut 10 (0:33–0:36) — Girl closes the distance fast, plants one fan-blade in the dirt beside his head — SLOW-MOTION STRIKE #2: blade sinks into the earth, wind blast throws his hair back, dust ring bursts outward around the impact point. Cut 11 (0:36–0:40) — Full speed. Girl straightens, fans crossed over her shoulders, hair whipping, staring down at him with total control. Boy: (smirking despite himself) "...Guess I lost." Cut 12 (0:40–0:45) — Low-angle hero shot, wind roaring, girl's eyes locked on camera: Girl: "K.O." Hard cut to black on final syllable.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `45.13s`

---

### 🎬 Deli Counter Queen Bars
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10505.jpg" width="480" alt="SD2_10505"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/deli-counter-queen-SD2_10505">🌐 Watch Online</a>

#### 📝 Prompt
```
@[Image 1](image_1) is the performer — preserve her exact identity: cornrow braids into long dark curls, silver chain-drop earring, gold pendant necklace, washed-green denim corset top, glossy lips. @[Audio 1](audio_1) is the finished master track — the only audio; no invented music, no new vocals. SHE RAPS THE VOCAL ON CAMERA — PRECISE LIPSYNC IS THE TOP PRIORITY. Mouth articulates every syllable of @[Audio 1](audio_1) exactly on time; face visible and sharp through every vocal line, no cutaways mid-word. LIPSYNC MAP: 0.0–0.5 instrumental. 0.5–2.8 "I'm standing on the edge / Say it with your chest / Or keep it on the deck" + "Hey!" 3.2–6.7 "I walk in, whole room gets tense / I don't need luck, I'm the consequence / If you really want to test my intent / Come correct, come correct or get bent" + "Woo!" 7.5–13.7 same hook verbatim second time, escalated. 14.5–15.0 instrumental hold. Music-video route: performance, NYC deli counter + street hybrid. Director thesis: corner-store cash-out — she raps from the bulletproof-glass deli counter out to the curb where her girls hold court on a double-parked old-school sedan. Black girlie hustle vibe. Visual world: classic uptown NYC corner deli at dusk — plexiglass counter carousel, snack racks, lotto machine glow, storefront plastered with faded posters; outside, a burgundy 90s sedan double-parked at the curb, streetlight just flicking on, brownstone corner behind. 3 background dancers: Black girls in uptown glam — fur bucket hat with a puffer vest and hoops, long braids under a fitted cap worn backwards with a cropped jersey, trench worn open over a matching knit set; all with name rings and gold chains. Palette: deli warm yellow, dusk blue street, burgundy car paint, denim green, gold. No neon effects, no particles. Shot flow (crash zooms stitching inside and outside): 0–0.5s static frame through the deli's plexiglass at her face lit by lotto-machine glow, waiting. 0.5s CRASH ZOOM IN through the plexiglass to her mouth on the first word — she raps through the carousel window, tapping the counter. 2.8–3.2s on "Hey!" hard cut outside: the three girls sit up in unison on the sedan — hood, roof, trunk. 3.2–6.7s she shoulders out the deli door rapping, bell jingling, camera pulling back to the curb; CRASH ZOOM punches on "tense" and "consequence"; the girls slide off the car and fall in step, hitting synchronized hip-cock freezes on every snare along the fender line; finger to lens on "come correct". 7.5s CRASH ZOOM IN on the kick to a tight close-up leaning back against the sedan door — second hook doubled, streetlight warm on her cheekbones, jaw snapping consonants. 10–13.7s slow orbital around the car: she raps from the hood while
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.04s`

---

### 🎬 Toddler Trapped in Whiteout Terror
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10503.jpg" width="480" alt="SD2_10503"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/toddler-whiteout-wolf-howls-SD2_10503">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: 8K IMAX, traditional hand-drawn 2D animation, animated on twos at 12 frames per second — each drawing held for two frames then replaced, choppy stepped motion cadence, hand-painted oil-brush texture, brushstrokes shifting and redrawn from frame to frame, line jitter, no 3D render, no game engine, no CGI smoothness. DIRECTOR'S NOTES — non-negotiable for every frame and every cut: 1. CHARACTER REFERENCE IS ABSOLUTE — face from <<<image_3>>> and wolf design from <<<image_4>>> exactly 1-to-1, no deviation, reference always overrides text. 2. MICRO-ACTING ON TODDLER FACE — every frame of her close-up shows constant micro-expressions: involuntary blinks as distinct held closed-eye frames on twos, sustained hard squints under gusts, eyelid flutter between blinks, brow gathering, chin quivering, lip pressed and trembling, jaw small and tight, nostrils flaring with shallow breath, tiny scared saccades searching the white air, eyes welling but no tears fall. When the first wolf howl rises offscreen, her eyes snap open wide for a single held frame in pure shock, eyelids freeze, breath catches in her small throat, lip parts slightly. 3. WOLVES NEVER APPROACH — they appear ONLY as a distant dark cloud creeping along the far horizon, never close, never as individual animals, only an undulating dark band of forms — appearing and vanishing as the buran sweeps across the lens. 4. BURAN NEVER PAUSES — rolling white-out waves continuously in every frame. CHARACTER TAGS: - THE TODDLER = small girl from <<<image_3>>>. - THE WOLVES = animals from <<<image_4>>>. - THE FOREST = location from <<<image_1>>>. Cinematography Lubezki / Deakins, fully handheld in human hands breathing with operator, anamorphic wide lens, shallow depth, never tripod never dolly never crane never aerial, eye level or below. The 12 principles of animation throughout: anticipation, follow-through and overlapping, slow in slow out on head turns, arcs, secondary action, exaggeration, solid drawing. Lighting: night, no light source, no moon, no stars, no rim, no contre-jour, no key light. Flat dim diffuse ambient grey glow only, no direction. Flat painted shapes, no gradient shading. Atmosphere — violent buran continuous: hurricane gusts driving snow horizontally, visibility roughly 3 meters around the camera, rolling waves of denser blizzard sweeping the lens, snow piled on the toddler's cap and shoulders, wind never drops. Audio: roaring buran wind continuously as dominant bed, crunching snow, shallow ragged child's breathing, plus two long wolf howls rising from offscreen distance — one howl in the first half of the scene, a pause, then a second howl from a different point along the horizon answering the first in the second half. Distant low growls and panting from the dark mass barely audible under the wind. No dialogue. No music. No subtitles. SHOT 2A — TIGHT CLOSE-UP handheld on THE TODDLER's face, exact face from <<<image_3>>>, every feature 1-to-1, identical features identical hair identical cap. Camera very close at her eye level, breathing with operator, vertical sway, her small face filling the frame off-center, negative space of white-out, focus locked on her eyes, background dissolved into pure white-out blur. Flat painted shadow only, no light direction. Snowflakes catch on her dark lashes and on the fur of her cap, snow piling on her shoulder. MICRO-ACTING in this shot, drawn frame by frame on twos as held poses: she squints hard against the wind, eyelids fluttering, then a held closed-eye frame for two frames, then snapping open, then a sustained hard squint when a gust hits held for three frames, anticipation as her tiny brow gathers before each squint, slow in slow out on every eye closure. Chin quivers visibly between beats, lower lip pressed and trembling, jaw small and tight, nostrils flaring with each shallow ragged breath, eyes welling at the corners but no tears fall. Then the first wolf howl rises from offscreen — her eyes snap wide open for a single held frame in pure shock, eyelids freeze in that wide pose for two frames, breath catches in her small throat (visible by held still chest), lip parts slightly. Her gaze then shifts in tiny scared saccades searching the white air on arcs, head turns a fraction toward the sound on a slow arc. The second howl answers from a different direction — she flinches, brow tightens, another sharp involuntary blink as a held closed-eye frame. A wave of buran sweeps across the lens partly obscuring her face, she does not move. Painting style identical to references. Animated on twos. HARD CUT to SHOT 2B — VERY WIDE LOW handheld looking out across the snowy expanse beyond THE FOREST treeline, the operator crouched in snow at knee height looking out toward the far horizon, camera in their hands with visible breath sway, the nearest dark pine trunks framing the edges as flat silhouettes. Far in the distance at the very edge of visibility along the horizon, THE WOLVES move as a single body — a dark moving mass like a black cloud creeping along the snowline, never approaching, never resolving into individual animals, only an undulating dark band of forms — exact wolf design from <<<image_4>>> readable only as silhouettes, exact coal-black fur with cold steel-blue sheen, faint pale yellow eye pinpricks barely visible. A rolling wave of buran sweeps across the lens — the dark cloud of wolves vanishes completely into white-out, holds white for two beats, then ghosts back into view as a faint dark band shifting along the horizon. The second wolf howl rises from a different point along the horizon, the dark band shifts in response stretching laterally. Another wave of buran swallows them again. The camera stays low and still, operator only breathing. Painting style identical to references. Animated on twos. Constraints: two distinct shots with hard cut between them not one continuous take, TIGHT CLOSE-UP on toddler then HARD CUT to VERY WIDE on wolves, THE TODDLER's face matches <<<image_3>>> exactly 1-to-1 with constant frame-by-frame micro-acting drawn as held poses on twos, THE WOLVES remain a distant dark cloud along the horizon throughout and never approach or resolve into individual close animals, reference always overrides text, buran rolling waves present in every frame, no dialogue, camera handheld eye level or below, no light source, flat painted shadow only, no 3D look.
```

#### 📌 Details
- Ratio: `2.33` | Duration: `15.08s`

---

### 🎬 Zeera Biscuits: Crispy Chai Perfection
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10501.jpg" width="480" alt="SD2_10501"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/zeera-biscuits-chai-morning-SD2_10501">🌐 Watch Online</a>

#### 📝 Prompt
```
(15 sec Ad Video – Zeera Biscuits) Scene 1 (0–3s): Close-up shot of crispy golden Zeera biscuits placed on a wooden table. Light steam tea cup beside it. Soft morning sunlight. 👉 Text on screen: “Subah ki perfect shuruaat…” Scene 2 (3–6s): Slow-motion biscuit break — crunch sound — zeera (cumin seeds) visible inside. Crumbs falling in cinematic style. 👉 Sound: Satisfying crispy crunch Scene 3 (6–10s): Young person dipping biscuit into chai ☕, smiling. Cozy home vibe. 👉 Text: “Har bite mein asli taste” Scene 4 (10–13s): Pack shot of Zeera Biscuits rotating with glowing light effect. 👉 Text: “Crispy • Tasty • Classic” Scene 5 (13–15s): Final frame: Family enjoying tea with biscuits together ❤️ 👉 Text: “Zeera Biscuits – Har chai ka best partner”
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

### 🎬 Premium Summer Berry Juice Commercial
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10500.jpg" width="480" alt="SD2_10500"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/premium-summer-berry-juice-commercial-SD2_10500">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a premium beverage commercial featuring the same young woman throughout the entire sequence. Maintain identical facial features, shoulder-length blonde beach-wave hair, glowing skin, natural makeup, and body proportions in every scene. She wears a stylish pastel pink crop top, matching pleated mini skirt, white sneakers, gold hoop earrings, and delicate bracelets. Bright summer atmosphere, luxury lifestyle aesthetic, vibrant pink color palette, premium commercial cinematography, ultra-realistic storytelling. The video opens with her smiling brightly into the camera while holding an ice-cold pink mixed berry juice bottle beside her face. She gently rotates the bottle as condensation sparkles in the sunlight. She playfully taps the bottle, winks, and says, "Ready for something refreshing?" A cinematic macro hero shot showcases the chilled bottle surrounded by fresh strawberries, raspberries, dragon fruit, and ice cubes. Tiny droplets glisten as sunlight reflects across the bottle. She twists the cap open with a satisfying pop, and slow-motion captures sparkling juice swirling inside before she takes a refreshing sip and smiles naturally. She strolls through a colorful flower market filled with blooming pink flowers, fruit stalls, cafés, and cheerful summer energy. Smooth tracking shots capture her laughter as she samples fresh fruit, greets friendly vendors, and carries the juice bottle in her hand. The scene transitions to a scenic rooftop picnic decorated with pastel cushions, flowers, fairy lights, and fresh fruit platters. Her friends arrive, everyone laughs, chats, and clinks their juice bottles together while enjoying the sunset. As upbeat energy builds, they dance together in an open garden surrounded by blooming flowers and fluttering petals. Handheld and gimbal shots capture authentic laughter, spinning movements, and joyful summer moments. Near golden hour, the group runs through a beautiful flower garden with sprinklers creating sparkling water droplets. Slow-motion shots capture sunlight shining through the mist as she raises her juice bottle toward the camera with a radiant smile. Final cinematic hero shot: she stands among blooming pink flowers with her friends behind her, holding the chilled juice bottle toward the viewer. She smiles warmly and says, "Taste the joy!" The camera slowly pulls back to reveal the vibrant summer garden, golden sunset, blooming flowers, and friends celebrating together. Premium beverage advertising, ultra-realistic commercial cinematography, dynamic camera movement, shallow depth of field, realistic liquid physics, vibrant pink fruit color palette, joyful storytelling, 4K HDR, 16:9 widescreen, natural ambient sounds only (birds, breeze, footsteps, laughter, bottle opening, ice clinking, water splashes), no background music, no subtitles, no logos, no watermarks, and no on-screen text.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 One Line Three Ways to Play
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10499.jpg" width="480" alt="SD2_10499"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/one-line-three-ways-SD2_10499">🌐 Watch Online</a>

#### 📝 Prompt
```
(1) Version without specified play No camera fixed, no cut. A woman looks at her partner and speaks. Line: "That's amazing. I would never have thought of something like that." (2) A Happy Version No camera fixed, no cut. The woman is genuinely impressed by the fact that she has just heard about the remarkable feat her best friend accomplished single-handedly. He said to his best friend standing in front of him. Line: "That's amazing. I would never have thought of something like that." (3) Ironic Version No camera fixed, no cut. The woman knew that her colleague had stolen her idea and took credit for it, and inwardly she was exasperated and contemptuous. He says this in front of the person himself, pretending to praise him on the surface. Line: "That's amazing. I would never have thought of something like that."
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

### 🎬 Crimson Roots High Fashion Surreal
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10498.jpg" width="480" alt="SD2_10498"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/crimson-roots-fashion-SD2_10498">🌐 Watch Online</a>

#### 📝 Prompt
```
A cinematic, high-fashion close-up and medium shot of an elegant East Asian woman wearing a striking white and red abstract-patterned cloak with a high, ruffled collar, standing in a barren, desolate landscape under a dim, overcast sky. She interacts with a massive, ancient tree with dark, gnarled bark and deep crimson, leaf-covered branches. The ground is dry and cracked, and suddenly, thick, vein-like crimson roots or tendrils erupt from the earth, surrounding her and growing upward towards the sky in a dramatic, surreal sequence
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.13s`

---

### 🎬 Japanese Announcer Summer Weather Report
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10497.jpg" width="480" alt="SD2_10497"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/japanese-announcer-summer-weather-SD2_10497">🌐 Watch Online</a>

#### 📝 Prompt
```
Clean broadcast audio. Soft studio ambience. Dialogue is clear and prominent. Background music is very low. She smiles warmly, briefly glances toward the weather map, then looks back into the camera and speaks in a cheerful, calm, professional voice: "Hello everyone. Today, the weather is clear nationwide, with summery blue skies spreading out. In some places, the highest temperature can reach around 35 degrees Celsius, so please stay hydrated frequently and be careful not to suffer from heatstroke. " Natural conversational pacing with small pauses between sentences. Slight smile throughout. Authentic Japanese TV announcer delivery. The woman speaks to the camera. "Hello everyone. Today, the weather is clear nationwide, with summery blue skies spreading out. In some places, the highest temperature can reach around 35 degrees Celsius, so please stay hydrated frequently and be careful not to suffer from heatstroke. "
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.12s`

---

### 🎬 Realistic Dunhuang Apsaras Portrait
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10496.jpg" width="480" alt="SD2_10496"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dunhuang-apsaras-portrait-SD2_10496">🌐 Watch Online</a>

#### 📝 Prompt
```
Realistic portrait photography: iPhone 16 Pro close-up style, with no phone in the frame. A young adult East Asian woman sits half-seated on a flying apsaras music and dance carpet with Western Region flair, set against a background of mottled Dunhuang murals, earthy sandstone, swaying lotus candlesticks, pipas, and colorful ribbons. The atmosphere is magnificent, exotic, mysterious, yet authentic and natural.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.08s`

---

### 🎬 Spear vs Axe City Clash
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10495.jpg" width="480" alt="SD2_10495"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/spear-axe-city-clash-SD2_10495">🌐 Watch Online</a>

#### 📝 Prompt
```
[Genre] High-density 3D toon/cel look. In the same square of a vast open-world city, @1の槍使いと@2の大型救援斧使いが never lose fighting spirit, launching rapid attacks, evasions, parries, and continuous counterattacks. Like in-game event scenes, you can simultaneously read the city's depth, weapon weight, speed, contact points, and recoil against your body. [Reference Images] @1は槍使いの顔, eye shape, iris color, hairstyle, hair color, costume, decoration, physique, silhouette, native color, actual physical features such as horns, tail, wings, and spear shapes and color schemes are the top priorities. @2は斧使いの顔, eye shape, irise, hairstyle, hair color, costume, decoration, physique, silhouette, unique color, and the shape and color scheme of the large rescue axe are the top priorities. Reference images are used only for people and equipment information; backgrounds, rooms, furniture, text, settings table UI, white background, poses, angles of view, framing, and split layouts are not reproduced. Both are maintained as the same people as in the reference image. The only things you can change are the natural movements of facial expressions, gazes, mouth, fighting posture, breathing, hair, costumes, and decorations. Averaging faces, mixing features, hair color swapping, costume swapping, weapon swapping, altering persons, cloning, and adding characters are all prohibited. [Character Adaptation] Backgrounds, props, architectural decorations, light, particles, reflections, color temperature, and sense of air are adjusted according to @1と@2の世界観, costume design, unique colors, and atmosphere. However, the unique colors of the two are not mixed; instead, they are kept distinguishable by the left and right lights and outline light. The city naturally integrates into the same world within the two settings, preventing bias toward one world. @1に尻尾がある場合は一本だけを腰後方へ連続接続し, synchronize your body rotation from the base to the tip. If there is no tail, do not add it; instead, the tail-using movements are replaced with spear hilts, hip rotations, stepping, and aerial posture control. Horns, wings, animal ears, and mechanical parts are only maintained as shown in the reference images, and do not multiply, move, detach, or become separate creatures. [Fixed Art Style] Movie-class key animation, high-quality composites, transparent lighting, and dense background art. Maintain a fine, delicate dark contour, two- to three-tier cel shading, soft mid-tones, multi-layered iris and jewel-like catchlight, and fine highlights along the hair strands. Draw cloth, embroidery, leather, metal, translucent blades, stone paving, and glass by varying reflections, roughness, and transparency. The main light is based on the evening slanting light, and the color temperature is adjusted to match the reference character. Generic 3D beautiful girl faces, thick black outlines, single-layer cel shadows, smooth plastic CG, low-density backgrounds, realistic or semi-realistic, mixed art styles, and muted colors are prohibited. [Weapon Locked] There is only one spear. He treats a single hard long shaft, spearhead, and stone tip as a single solid body, while both hands grip only the hilt. Only one axe. It consists of a single long handle, an axe fixed at the upper end, a large blade, a rear mechanism, and a stone protrusion at the bottom, maintaining the same closed shape throughout. I don't switch to a typical lumberjack axe, spear, halberd, or two-axe setup. Weapon transformation, deployment, launch, proliferation, fusion, softening, and switching weapons are prohibited. A short hit stop of about 0.1 seconds is applied at the moment of contact, synchronizing contact points, sparks, material sounds, and recoil from the body and the entire weapon. [Stage] Central Square in the same open-world city. Wide stone pavement, a main street lined with shops, steps, stairs, glass and stone buildings, metal arches, elevated walkways, panoramic towers, flags, street trees, and stopped traffic equipment are arranged. Architectural design, paving patterns, decorations, plants, sky colors, and lighting should match the character traits of @1 and @2. Maintain the positional relationships of light sources, buildings, stairs, paved lines, and distant towers, and avoid teleportation, background loss, or switching to another plaza. Readable signs, crowds, third-party fighters, text, subtitles, logos, and watermarks are all prohibited. [Camera and Combat Principles] All 8 cuts. Low over-shoulder medium shot, low side following, diagonal forward wide, short upward tilt following a jump, reverse side following after position swap, and finally a symmetrical two-person medium shot, all passed according to the cause and effect of the movement. Purposeless omni-orbit orbits are prohibited. The entire show is fast-paced in real time. Attack, physical reactions to the opponent, parry or evade, and use the recoil to connect counterattacks without interruption. Repositioning, long pushes, mid-air stops, long slow motion, and waiting at long distances are prohibited. [Action] Cut 1 @2が斧刃を床から完全に浮かせて低く沈み, rotate it wide diagonally and vertically just once. At the end of the lower half-circle, strike the outer base of the blade to a point on the stone pavement, producing sparks and stone fragments. With the momentum, he bounced the entire axe upward and connected it to the initial horizontal sweep. Don't drag the floor. Cut 2 @1が横薙ぎの内側へ踏み込み, a high-speed mid-level thrust with a spear. @2は斧頭外縁と柄上部で槍頭を外へ流し, connect to a lower horizontal sweep in the opposite direction. @1は槍柄で斧柄を一度だけ受け, transfer the momentum to the next body rotation. Cut 3 @2が斧全体を床すれすれへ大きく薙ぐ. @1は低い開脚スライドで刃の下を抜け, he touched the spear's stone tip to the floor and lifted his body with the recoil. Without letting go of the spear, he spun forward once, crossed over @2's head, landed on both feet on the opposite side, and absorbed the impact with his knees. If a tail is present, a continuous arc is drawn from the base to the tip to balance the rotation. Cut 4 @1は着地反動から背後へ槍を水平に振る. @2は振り返りながら斧柄中央で受ける. @1に尻尾がある場合は, from a reverse rotation, the tail strikes the center of the axe handle once, then releases immediately without wrapping around it. If it has no tail, it is replaced with a short follow-up attack using a spear thrust. @2は横反動へ逆らわず, connect the entire weapon diagonally upward to the reverse. Cut 5 @1は斜め上の斧を槍頭側面で外へ弾き, jump sideways. Rotate the body and spear around a single center of gravity, performing a single side somersault without a pivot. At the moment of upward flipping, the spearhead side is briefly pressed inward of the axe blade to derail the path and land on both feet. Do not rotate only the spearhead independently. Cut 6 @2が頭上から斜め下へ斧全体を叩き込む. @1は斜め前へ低くスライドして回避する. If a tail is present, it is flicked low along the stone pavement to @2の前足首外側へ一度だけ当てる. If it has no tail, it uses the spear's stone prongs to keep its feet in check. @2は後脚と斧の石突で重心を支え, from the landing recoil, the entire axe returns to a horizontal sweep. @1は槍を両手で水平に構えて受け流す. Cut 7 @1が中段突きから槍を引き戻し, he connects with a two-stage attack aimed at the chest with a stone thrust. @2は第一撃を斧刃内側で払い, he receives the second strike at the center of the axe handle, pushing back and sweeping it wide in the opposite direction. @1は上体を低く沈めて刃の下を抜け, I thrust the spearhead back to the side of @2. @2は半歩だけ軸足を滑らせ, he flicked the spearhead outward with the axe handle. The two maintained close range and fixed their gaze on each other, entering their final simultaneous steps without making a long pause. Cut 8 The two of them stepped deeply from both sides at the same time. @1
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.12s`

---

### 🎬 Headlights Rap Queen
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10493.jpg" width="480" alt="SD2_10493"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/headlights-rap-queen-SD2_10493">🌐 Watch Online</a>

#### 📝 Prompt
```
@Image1 is the performer — preserve her exact identity: cornrow braids, septum ring, statement earrings, sculptural white designer top, dark indigo denim. @Audio1 is the finished master track — the only audio; no invented music, no new vocals. SHE RAPS THE VOCAL ON CAMERA — PRECISE LIPSYNC IS THE TOP PRIORITY. Mouth articulates every syllable of @Audio1 exactly on time; face visible and sharp through every vocal line, no cutaways mid-word. LIPSYNC MAP: 0.0–0.5 instrumental. 0.5–2.8 "I'm standing on the edge / Say it with your chest / Or keep it on the deck" + "Hey!" 3.2–6.7 "I walk in, whole room gets tense / I don't need luck, I'm the consequence / If you really want to test my intent / Come correct, come correct or get bent" + "Woo!" 7.5–13.7 same hook verbatim second time, escalated. 14.5–15.0 instrumental hold. Music-video route: performance, night drive exterior. Director thesis: she raps in the beams of a single car's headlights on an empty wet asphalt lot — minimal, cinematic, all attitude. Visual world: empty asphalt lot at night after rain, one matte black sedan parked with headlights on, wet ground mirroring the beams, distant sodium streetlights, light steam rising off the asphalt. Palette: headlight white, sodium amber, wet black, bone white top blazing in the beams, indigo. No neon signage, no particles. Shot flow: 0–2.8s she leans against the car hood in silhouette; on the first word she pushes off and steps into the beams — medium shot, she raps straight down the lens, double shadows fanning behind her. 2.8–3.2s on "Hey!" hard cut to a low wide: her figure blazing between the headlights. 3.2–6.7s backward-dollying medium as she stalks toward camera through the beams rapping, each snare hitting with a sharp head isolation, wet ground doubling her figure; finger to lens on "come correct". 7.5–10s cut on the kick to a tight close-up lit only by headlight glow: second hook with bared teeth intensity, breath faintly visible in the cold air, jaw snapping every consonant. 10–13.7s slow orbital around her in the beams, steam drifting through the light, she raps while carving angular vogue lines with one hand, earrings flaring. 13.7–15s on "Woo!" she stops dead center of the beams, arm high, frozen; the headlights flick to high-beam for the final frame, hold. Performance rules: cold, cocky, unbothered; articulation crisp and readable; never smiles. Continuity: same woman, same wardrobe, same lot and car. Audio intent: @Audio1 only, mouth locked to it; faint idle engine and wet-ground foley under the track. Quality bar: expensive cinematic rap video, no AI gloss, no glow effects.
```

#### 📌 Details
- Ratio: `1.82` | Duration: `14.97s`

---

### 🎬 Authentic Handheld Selfie Style
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10492.jpg" width="480" alt="SD2_10492"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/authentic-handheld-selfie-SD2_10492">🌐 Watch Online</a>

#### 📝 Prompt
```
Handheld self-filming with an iPhone, or occasionally leaning the camera against a dressing mirror. Only selfies / first-person perspective. Natural hand shake, imperfect framing, delayed focusing, awkward zoom, slight subject loss, and occasional cropping of faces. The camera itself never appears. Natural light, high-definition pixel quality, soft contrast, and lifelike skin tones. Style: Casual
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.08s`

---

<!-- STATS_END -->
