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
- Total Prompts: **8484**
- Updated Today (UTC 2026-07-29): **88**

## 🎬 Today's Updates
### 🎬 Cat Flying On Sword
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10880.jpg" width="480" alt="SD2_10880"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cat-flying-on-sword-SD2_10880">🌐 Watch Online</a>

#### 📝 Prompt
```
[Style] Ultra-realistic mobile phone casual short videos. A first-person view inside a real sedan at the street corner of an ordinary Chinese city; A real cat floats and flies on a sword in a way that defies physical norms, but its fur, whiskers, pupils, tail, and body proportions all have the texture of real animals. Not anime, not cartoons, not low-poly 3D, not game CG. Vertical 9:16, 24fps, phone auto exposure, slight body bumps, handheld shake, focus breathing, no subtitles, no watermark. [Duration] 10 seconds [Scene] Guocheng Intersection. The camera is located in the front passenger seats of the sedan, showing a black-and-gray center console, air conditioning vents, A-pillars, window frames, and the left side mirror. At intersections, there are zebra crossings, traffic lights, utility poles, overhead wires, street trees, street-facing shops, and cars waiting to pass through; The streets are plain and authentic, with no cyber elements or ancient buildings. [Characters] Refer to the image of a cat. The cat stands in the anthropomorphic "Sword Master" pose: hind legs spread about one cat's shoulder-width apart, feet firmly placed on the middle of the sword, one front and one behind, knees slightly bent; The torso is vertically straight, with the chest slightly forward; Its two front paws fold and retract, tucked behind the waist, resembling a master of a sect; He lifted his head about 10 degrees, chin slightly raised, and looked straight ahead on the road, his expression calm and cold. Never open your mouth, wave your paws, or look at the camera the whole time; Only the tips of its ears, whiskers, and tail tips are moved by a very slight breeze. Flying Sword: A slender, narrow Chinese ancient-style flying sword, about 1.2 meters long and 8 centimeters wide, with the tip always pointing ahead of the road. The blade is a dark reddish-brown mix of wood and old metal, with fine wood grain, worn old paint, and narrow metal edging; The hilt features a round guard and a dark brown wrapped cord, with a yellow silk tassel hanging from the tail. The flying sword always remained level, about 40 centimeters above the ground, and slid forward at a constant speed; It does not breathe fire, emit light, drag its tail, or produce magical particles. Beneath the blade is a soft, realistic floating shadow; The yellow tassels and cattail sway slightly backward with the wind. [Voice] No character lines. It retains the deep engine sound of a sedan, subtle interior vibrations, road sounds, distant passing vehicles, and slight wind noises. [00:00-00:02] Scene 1: Found inside the car From the front passenger perspective of the sedan, first capture the overcast city intersection, crosswalk, vehicles ahead, and traffic lights outside the windshield; The center console and A-pillar occupy the lower and left sides of the screen. The phone naturally turns to the left window, and the left side mirror enters the foreground. A dark reddish-brown flying sword glides in from the low air on the left side of the image, its tip pointing ahead of the road, and the yellow tassel sways lightly backward at the tail. [00:02-00:05] Shot 2: Close-up of the Sword Cat The entire cat and flying sword entered the right car window intact. The flying sword floats horizontally about 40 centimeters above the crosswalk, with the cat's paws pressing one front and one back against the middle of the blade, the hind legs naturally bent slightly, the body straight, front paws folded behind the waist. The cat looked up into the distance, its expression cold, as if it were calmly riding a sword at a city intersection. The cat's tail naturally hangs down from behind, with the tip swaying gently in the wind; Yellow tassels fluttered at the tail of the sword. Cars and flying swords drive side by side, with background traffic lights, utility poles, and trees creating natural parallax. [00:05-00:07] Scene 3: Flying side by side across the intersection The intersection signal turned green, and the sedan and Flying Sword continued parallel to the road. The cat's body and flying sword remain stable throughout, with no vertical jumping on the blade; The cat slightly adjusted its hind leg balance, keeping both feet firmly planted on the sword. The flying sword skimmed across the crosswalk at a steady pace, its blade casting a gentle shadow beneath it. The side shots clearly show the cat's aloof profile, the front paws behind its folded back, the front and rear legs spread apart, the cat's tail, and the yellow sword tassel. [00:07-00:10] Shot 4: Pulling out to wrap things up The car gradually overtook the flying sword, while the cat maintained a perfectly consistent sword posture: feet stepping forward and backward, body upright, front paws behind the back, chin slightly raised, eyes looking forward. The flying sword smoothly led the cat through the intersection, the yellow tassels fluttering backward at the tail. The phone naturally returns to the windshield, and the cat and flying sword shrink to the absurd, floating figure at the front left of the car at the intersection; The vehicle ahead passes through the intersection normally, and the Sword Cat continues to fly smoothly along the road into the distance, ending the scene naturally.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `10.1s`

---

### 🎬 Immortal Falls for Truck Wind
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10879.jpg" width="480" alt="SD2_10879"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sword-immortal-truck-fail-SD2_10879">🌐 Watch Online</a>

#### 📝 Prompt
```
[Video Specifications] Duration: 10 seconds Format: 16:9 landscape format Genre: Comedy Twist Image quality: live-action shots, cinematic realistic texture, natural skin textures, and real urban environments [Core Contrast] The first half creates a grand, solemn, and oppressive atmosphere for a xianxia blockbuster. The second half suddenly shifts to a disheveled, quiet, and awkward reality comedy. The twist must happen suddenly, without hints in advance; the overall atmosphere is absurd but logically clear, maintaining a relaxed, harmless comedic atmosphere. [Scene] A main city road on a clear day. The road includes two-way motor vehicle lanes, roadside non-motorized lanes, and sidewalks. A large pile of loosely used cardboard boxes is stacked beside the sidewalk, varying in size and spreading out after the character falls, creating an exaggerated yet safe comedic effect. [Characters] Sword Immortal Sister: @图片1 Strictly maintain that the character's face, hairstyle, clothing, body type, and features match those shown in the reference images; no face changes or styling are allowed throughout the process. [Key Continuity] The silver longsword hovered at Sword Immortal Sister's feet throughout the first half. The blue truck only passes through the adjacent motor vehicle lane and must not touch or collide with anyone, swords, or bicycles. The Sword Immortal Sister's fall into a pile of cardboard boxes is a safe, exaggerated comedy performance, with no injuries, bleeding, pain, or real traffic accidents. All actions must be spatially continuous; characters and props must not teleport. ━━━━━━━━━━━━━━ [00:00-00:03] [Scene 1: Blockbuster Xianxia Film-Level Appearance] Ultra-low camera angle with a fast rear camera followed by the lens. Sword Immortal Sister stepped on a floating silver longsword and sped past the city road about two meters above the city. She clasped her hands behind her back, chin slightly raised, her gaze cold and her expression proud, as if overlooking the mortal world. Her long hair and skirt hem are blown behind her by the oncoming airflow, her movements steady, elegant, and full of pressure. Sunlight reflected sharply on the silver blade, leaving a faint silver sword aura trail as the long sword sliced through the air. Sound effects: grand xianxia music, whistling sounds, deep sword rings. Opening credits: "When the Sword Immortal first entered the modern transportation system" ━━━━━━━━━━━━━━ [00:03-00:07] [Scene 2: One compliment made her feel completely arrogant] Switch to non-motorized lane side tracking. Bike Sister entered the frame on her bicycle, looked up and saw Sword Immortal Sister in the air, her eyes widened instantly, then she excitedly accelerated and pedaled to catch up. Bike Sister sincerely admired and shouted: "Damn! Girl, you're just too handsome! ” Switch to close-up of Sword Immortal Sister's face. Upon hearing the praise, the Sword Immortal Sister's previously cold lips briefly lifted, but she immediately forced them back. She pretended to be calm as she raised her hand to tuck her hair, but her eyes secretly glanced at the bike girl below, clearly already feeling smug. The silver sword beneath his feet seemed to match his master's skill, drawing two smooth small S-shapes in the air. Sound effects: Xianxia music continues, adding a slightly triumphant "humming" sound and sparkling sound effects. ━━━━━━━━━━━━━━ [00:07-00:10] [Scene 3: The Real World Suddenly Takes Action] Switch to fixed side panorama. Sword Immortal Sister closed her eyes, slightly raised her chin, enjoying the admiration of Bike Sister. A huge blue truck suddenly sped past the adjacent motor vehicle lane. The truck did not hit any of the characters, but as it passed, it created an extremely exaggerated and strong crosswind. Sword Immortal Sister's hair, skirt, and facial expression were all messed up by the wind. The smug smile on her face vanished instantly; her eyes widened sharply, pupils trembling. The silver longsword beneath his feet began to swing violently from side to side. She tried to regain her mastery posture, but her hands frantically grabbed at the air twice. Then, her body floated like a piece of paper blown away by the wind, body and sword drifting sideways toward a pile of cardboard boxes by the roadside. Sound effects: low truck horn sound, fierce crosswind. The moment the truck passed, the grand xianxia music immediately stopped. ━━━━━━━━━━━━━━ [00:10-00:12] [Scene 4: Fairy Falls to the Mortal World] Quickly switch to the front machine position of the carton stack. Sword Immortal Sister plunged headfirst into a pile of old cardboard boxes in an exaggerated yet safe pose. The box instantly exploded in all directions. A large cardboard box wrapped around her upper body, and two small boxes slowly landed on her head and shoulders. The silver longsword spun uncontrollably twice in midair, its aura completely vanished, then fell to the side like an ordinary metal plate. "Bang!" The scene suddenly fell completely silent. Only the slow rolling of the cardboard box and the lonely call of a crow in the distance remain. ━━━━━━━━━━━━━━ [Performance Highlights] The first half of the Sword Immortal Sister must be extremely cool, elegant, and confident, exuding the imposing aura of a true xianxia master. When encountering crosswinds, facial expressions need to clearly complete four stage changes: Pride → doubt → terror → dumbfounded The first half of the Bicycle Sister must be genuinely admirable; after seeing Sword Immortal Sister fall, she was first stunned and petrified, then finally trying hard to hold back her laughter. Bike Sister can't show mockery or schadenfreude from the start. [Camera Pacing] Three seconds before the start, it quickly establishes the feel of a fantasy blockbuster. After the bike sister praises her, she keeps at least about a second of Sword Immortal Sister's facial reaction, letting the audience clearly see her secretly proud. Before the truck appears, you cannot use sound, shadow, camera movement, or character gaze to prompt you in advance. After the truck passes by, the xianxia music is immediately cut off, using sudden silence to reinforce the comedic contrast. The final line is immediately frozen after the line ends, with no delay or additional plot details. [Avoid] Don't let the blue van hit characters, bicycles, or longswords. Do not include realistic scenes of serious traffic accidents, injuries, bleeding, pain, or danger. Do not change the character's face, hairstyle, clothing, body type, or identity features. Don't let the silver longsword turn into a skateboard, broomstick, surfboard, or other object. Avoid cases of piercing the figure, distorted limbs, abnormal fingers, excess limbs, or reversed joints. Don't let characters or props teleport in the same shot. Do not use anime-style materialism, game CG textures, plastic skin, or obvious AI fake faces. Don't turn the twist into a disaster or thriller. Do not join in explosions, rollovers, collisions, rear-end collisions, or crowd panic. Overall, it maintains a safe, lighthearted, absurd, and harmless comedy atmosphere.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.08s`

---

### 🎬 Wakeboard Trick Fails Dramatically
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10878.jpg" width="480" alt="SD2_10878"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/wakeboard-trick-fail-SD2_10878">🌐 Watch Online</a>

#### 📝 Prompt
```
15 seconds, 16:9 aspect ratio, live-action photorealistic. Authentic wakeboarding competition footage. A vast lake in midsummer, strong sunlight, blue sky, light reflecting off the water&#39;s surface. Towed by a speeding motorboat, an adult wakeboarder glides across the water at breakneck speed. [0-3 seconds] Low-profile camera just above the water&#39;s surface. The wakeboarder pulls hard on the rope, bending his knees deeply as he crosses the boat&#39;s wake. The edge of the board cuts sharply through the water, sending large splashes flying to the left and right. Telephoto compression with a sense of speed, natural camera vibration. [3-7 seconds] Using the slope of the wake like a jump ramp, he leaps high into the air. The camera tilts up from the water&#39;s surface into the sky. A spectacular trick where he tilts his body sideways in mid-air and rotates the board at high speed. A dynamic acrobatics that combines a back roll and a side spin. The horizon in the background rotates dramatically, and sunlight reflects off the underside of the board. [7-10 seconds] Towards the end of his aerial rotation, he attempts to enter a landing position, but the rotation is slightly insufficient. The tip of the board catches on the water&#39;s surface, and only his body is thrown forward. Here, there is a brief moment of super slow motion. The athlete&#39;s surprised expression, the taut rope, and his body approaching the water&#39;s surface are shown from multiple angles. [10-13 seconds] He abruptly returns to normal speed. The athlete&#39;s back and shoulder area are slammed into the water&#39;s surface with great force, and a huge white column of water explodes. Water droplets fly onto the camera lens, and the entire screen is covered in splashes for a moment. There is a strong camera shake and a low splashing sound in accordance with the impact. However, there are no grotesque depictions of bleeding, fractures, or bodily deformities. [13-15 seconds] The splashes subside, and the athlete floats to the surface in his life jacket. He raises one hand, looking slightly dazed, to signal that he is safe. The boat moves away, the water&#39;s surface is choppy, and the wakeboard drifts. The video ends with a realistic sports broadcast-style shot from a telephoto camera with water droplets on it. Camera setup: A camera that follows the boat just above the water&#39;s surface, a camera behind the boat, a super-telephoto camera from the shore, a side-orbit camera that tracks the aerial rotation, and a waterproof camera at the landing point. The direction of travel and the relative position of the body are maintained in every shot. Visual expression: Sharp water droplets, strong water pressure, realistic gravity and inertia, and natural body movements, all captured with a high-speed shutter. Slow motion is used only just before the failed landing, and the speed is immediately returned to normal upon impact. The composition shifts from refreshing sports footage to shocking footage of failure in an instant. Sound: The sound of water being cut at high speed, the boat engine, the sound of ropes tightening, and the sound of wind. Ambient sounds are muted in the air, with a moment of silence just before landing. At the moment of impact with the water&#39;s surface, there is a heavy, sharp &quot;splash&quot; sound and the sound of a large amount of water. No background music, narration, subtitles, logos, or legible text are included. Unacceptable actions include: the disappearance of boards or ropes, the addition of limbs, unnatural twisting of the body, instantaneous teleportation in mid-air, reversal of the relative position to the boat, depiction of splashes before landing, light landings, overly comical falls, bleeding, and depictions of serious injuries.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.07s`

---

### 🎬 Spring Han River Bike Ride
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10877.jpg" width="480" alt="SD2_10877"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/han-river-spring-bike-ride-SD2_10877">🌐 Watch Online</a>

#### 📝 Prompt
```
Main Subject: Young Korean woman, 22, natural appearance, shoulder-length dark brown hair tied in a loose ponytail with wispy bangs. Wearing a light blue oversized hoodie, black cycling shorts, white sneakers, and a small grey crossbody bag. Minimal makeup, realistic skin texture, warm personality. Maintain consistent identity, clothing, hairstyle, and appearance throughout. Location: Quiet bicycle path beside the Han River during a sunny spring afternoon. Cherry trees, green grass, wooden benches, cyclists, joggers, gentle river breeze, distant city skyline, peaceful atmosphere. Visual Style: Ultra-realistic documentary realism. Genuine candid behavior, natural body language, authentic everyday life. Camera Style: Early-2000s Sony MiniDV camcorder. Heavy handheld shake, imperfect framing, autofocus hunting, exposure pumping, faded colours, soft contrast, slight motion blur, DV compression artifacts, no stabilization. 00:00–00:03 She unlocks a silver city bicycle beside a wooden bench, smiling as wind moves loose strands of hair. Camera briefly focuses on the handlebars before correcting. 00:03–00:06 She rides slowly along the riverside path. The camera jogs behind, shaking naturally while struggling to keep her centred. 00:06–00:09 She stops beside the river, parking the bike. Resting both hands on the handlebars, she quietly watches the water while cherry blossom petals drift past. 00:09–00:12 She drinks from a small bottled water, brushes hair behind her ear, and laughs softly after noticing the camera. 00:12–00:15 She gets back on the bicycle, waves casually toward the camcorder, and rides away as the operator lowers the camera. Recording cuts abruptly to black. Audio: Natural ambience only—birds, bicycle wheels, wind, distant conversations, footsteps, leaves rustling, flowing river, occasional bicycle bell. No music or narration. Goal: A forgotten MiniDV home video from 2004 capturing a peaceful afternoon bicycle ride along the Han River, warm, imperfect, nostalgic, and completely believable.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Flying Inside Nested Hollow Worlds
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10876.jpg" width="480" alt="SD2_10876"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/nested-hollow-worlds-SD2_10876">🌐 Watch Online</a>

#### 📝 Prompt
```
The camera races low over rolling terrain that bends upward at the edges instead of falling away, rivers climb the walls, forests hang overhead, and mountains grow downward from a ceiling of land. Two traversal craft fly the inside of a hollow world while the camera struggles to keep up with the inverted geometry. They climb toward the central sun and emerge into a sky filled with hundreds of nested hollow worlds, each one visible through the next.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Retro VHS Fitness Diary Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10875.jpg" width="480" alt="SD2_10875"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/retro-vhs-fitness-diary-SD2_10875">🌐 Watch Online</a>

#### 📝 Prompt
```
80s/90s retro home videotape-style fitness vlog. DV / VHS / Old DVD texture, low definition, 4:3 format, as if the footage was recorded by a home camera from the late 1980s to the 1990s. Overall, it presents a distinct retro tape aesthetic: slight noise, scan lines, tape grain, slight frame drop, warm colors with slight fading, slight blur, low resolution, softened edges, occasional auto exposure drift, delayed focusing, unstable white balance, soft vignetting in highlights, preserving the authentic, rough old video feel. The visuals resemble old DVDs/home tapes that have been re-recorded several times, carrying a bit of a sense of vintage and a sense of everyday life. Shooting method: POV first-person perspective, shot by CHASE himself. She occasionally shoots handheld and sometimes places the camera on the treadmill console or on a nearby stool. Natural image shake, unstable framing, awkward composition, occasional zooming in and out of skill, and the camera itself should never appear in the frame. Character Settings: An Asian woman in her twenties, with the aura of a Korean idol. Long black ponytail, delicate features, lively eyes, sweat from slight exercise, slim, well-proportioned, and sporty build. She wore a simple and understated long-sleeved sports top, loose jogging pants, white sneakers, and a towel draped around her neck. The overall look is authentic—no over-retouching, no blockbuster-style looks—just like a casual personal fitness diary from that era. Scene: Modern indoor gym, but with vintage VCR graphics, it gives off a retro feel. The environment features treadmills, rowing machines, mirrors, and soft indoor lighting for evenings. The background should be authentic and natural, not overly clean or commercialized, with a bit of everyday clutter and signs of use. Overall tone: A lighthearted, playful, authentic, slightly tiring aerobic challenge vlog. Not an advertisement, not a movie, not a high-quality blockbuster, but an old-fashioned personal video full of everyday life and humor. Characters react naturally, with real breathing, breathing, pauses, and small expressions. Footage: At the start of the selfie, she stood in front of the treadmill and said to the camera, "Let's see if I can make it past twenty minutes." ” The camera was set up on the treadmill console, and she began to jog naturally. Holding the close-up, she panted and said helplessly, "Why does it feel faster every minute?" ” A close-up of her finger pressing the treadmill stop button. She slowly stepped down from the treadmill, smiling as she wiped the sweat from her forehead. She picked up the water bottle and took a deep breath. She gave a tired but amusing thumbs-up to the camera and said, "Today, cardio officially beat me." ” Finally, she picked up her gym bag, smiled warmly, waved goodbye to the camera, and said, "See you next time!" ” Additional requirements: Maintains the feel of vintage home VCRs / VHS / vintage DVDs Don't want a modern, high-definition look, don't be too sharp, don't overdo beauty filters Retain real sweat, breathing, tired expressions, and natural small mistakes Overall, it looks like a family fitness day documentary from the 80s/90s
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Cinematic Morning GRWM Workout Routine
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10874.jpg" width="480" alt="SD2_10874"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/morning-grwm-workout-SD2_10874">🌐 Watch Online</a>

#### 📝 Prompt
```
Using the attached character reference, create a 15-second ultra-realistic cinematic GRWM (Get Ready With Me) video featuring the exact same young Korean East Asian woman with consistent facial features, hairstyle, glowing skin, body proportions, and identity throughout the sequence. She wears a white fitted athletic crop top, high-waisted red leggings, white running sneakers, a lightweight smartwatch, and a high ponytail throughout the outdoor workout. The video opens with her peacefully waking up in a bright modern bedroom as soft sunrise light streams through the curtains. She smiles, stretches naturally, washes her face, brushes her teeth, completes a quick skincare routine, and changes into her white crop top and red leggings. She ties her hair into a neat high ponytail, fastens her smartwatch, laces her sneakers, picks up a yoga mat, reusable water bottle, and wireless earbuds, then heads outside. She steps onto a lush green lawn surrounded by blooming flowers and tall trees glowing in the golden morning light. She begins with gentle stretching, yoga poses, squats, lunges, planks, push-ups, jumping jacks, and light jogging across the grass. Cinematic tracking shots capture realistic hair movement, natural breathing, and dew sparkling beneath her shoes. Macro shots highlight her smartwatch tracking heart rate, shoes brushing fresh grass, hands reaching toward the sky, and sunlight illuminating her face. After finishing her workout, she drinks water, sits cross-legged on the yoga mat for mindful breathing, smiles peacefully, then returns home. She prepares a fresh strawberry smoothie in a modern kitchen, pours it into a glass, walks to a sunlit window, notices the camera, smiles warmly, raises the smoothie toward the viewer in a friendly toast, and enjoys the peaceful morning as the camera slowly pulls back. Use smooth cinematic transitions, seamless match cuts, gentle handheld and gimbal camera movement, shallow depth of field, premium lifestyle cinematography, realistic skin texture, natural hair physics, physically accurate sunrise lighting, warm golden-hour atmosphere, glossy commercial-quality color grading, 4K HDR, 16:9, with natural ambient audio only (birds chirping, gentle breeze, rustling leaves, footsteps on grass, breathing, water bottle opening, smoothie blending), no background music, subtitles, logos, watermarks, or on-screen text.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `14.18s`

---

### 🎬 Golden Hour Girl's Dream
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10873.jpg" width="480" alt="SD2_10873"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/golden-hour-girl-dream-SD2_10873">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 15-second ultra-photorealistic cinematic coming-of-age short film set in a peaceful rural Japanese town during late golden hour. The entire film should feel nostalgic, elegant, timeless, warm, and emotionally peaceful, with a rich vintage yellow colour palette inspired by classic Japanese cinema. The environment is bathed in glowing amber sunlight, soft golden haze, creamy highlights, matte shadows, subtle film grain, dreamy bloom, and warm nostalgic tones similar to Kodak Gold 200 and Kodak Portra 400 film photography. Every frame should look premium, artistic, and cinematic. Main Character: A beautiful Japanese teenage schoolgirl wearing a traditional navy-and-white sailor school uniform with a navy pleated skirt, white socks, black loafers, long black hair tied in a low ponytail with a small white flower hair clip. Keep her face, hairstyle, clothing, proportions, and identity perfectly consistent throughout every shot. Scene 1 (0:00–0:02) A wide establishing shot of a quiet old Japanese street lined with traditional wooden houses. The road glows with warm yellow sunset reflections as the girl walks peacefully toward the distant sun. Long cinematic shadows stretch across the street while the camera slowly pushes forward. Scene 2 (0:02–0:04) A smooth tracking shot from behind follows her walking. Her ponytail gently moves in the breeze. Warm sunlight wraps around her silhouette creating soft rim lighting and beautiful lens flare. Every movement feels calm and natural. Scene 3 (0:04–0:06) She arrives at an old railway crossing and quietly watches a train passing in the distance. The sun shines directly behind the tracks, creating a glowing silhouette and an emotional nostalgic atmosphere. Slow cinematic camera movement. Scene 4 (0:06–0:08) A close-up side profile as she slowly turns her face toward the golden light. Her expression is peaceful and thoughtful. Warm rim light outlines her face while the background melts into soft creamy bokeh. Scene 5 (0:08–0:10) She walks beside a quiet canal, lightly running her fingertips along the railing while looking at the shimmering water reflecting the sunset. Leaves sway gently in the breeze. The camera slowly circles around her with elegant movement. Scene 6 (0:10–0:12) Transition into a glowing field of white daisies. She walks slowly through the flowers, brushing the petals with both hands. Tiny pollen particles float through the warm sunlight. The atmosphere feels dreamy and magical. Scene 7 (0:12–0:14) Extreme close-up as she gently picks a single white daisy and playfully holds it over one eye. She slowly lowers the flower and smiles naturally toward the camera. Wind softly moves loose strands of hair, creating an intimate emotional moment. Scene 8 (0:14–0:15) An ultra-wide final shot reveals the endless flower field beneath a breathtaking golden sunset sky. She stands peacefully facing the horizon while the camera slowly pulls back and rises
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 Quiet Urban Earphone Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10872.jpg" width="480" alt="SD2_10872"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/quiet-urban-earphone-ad-SD2_10872">🌐 Watch Online</a>

#### 📝 Prompt
```
Generate 15-second, 9:16, hyper-realistic original true wireless earphone ads. Restraint, quietness, and urban breath. Protagonist: 28-year-old East Asian female graphic designer, short black hair, natural skin tone, charcoal shirt + white tank top + dark straight-leg pants + low-top canvas shoes. The entire face, hairstyle, clothing, and body shape must be consistent.
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.13s`

---

### 🎬 Alien Terror in Emergency Room
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10871.jpg" width="480" alt="SD2_10871"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alien-terror-emergency-room-SD2_10871">🌐 Watch Online</a>

#### 📝 Prompt
```
Cinematic sci-fi horror scene in a dimly lit, high-tech hospital emergency room during a heavy storm. An eerie, slender alien entity with dark, symbiotic armor and glowing accents stands tall in the center of the room, surrounded by terrified medical staff in scrubs and white coats. Moody, desaturated teal and charcoal color grading with harsh emergency lighting, dramatic backlighting, volumetric smoke and haze, high-contrast shadows, photorealistic textures, shot on 35mm lens, anamorphic depth of field, suspenseful and chilling atmosphere, 8k resolution. negative_prompt: cartoon, illustration, low resolution, bright cheerful lighting, poorly rendered faces, extra limbs, blurry aspect_ratio: 16:9
```

#### 📌 Details
- Ratio: `1.78` | Duration: `28.1s`

---

### 🎬 Futuristic School Sword Fight Animation
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10870.jpg" width="480" alt="SD2_10870"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/futuristic-school-sword-fight-SD2_10870">🌐 Watch Online</a>

#### 📝 Prompt
```
High-quality animated footage. A high-density 3D toon/cel-look cinematic action RPG featuring high-speed sword-fighting in a near-future school city. Movie-class key animation, high-quality composites, transparent lighting, and dense background art. @1は冷静で圧倒的な格上. @2は速度と手数で挑む挑戦者. Seamlessly connect attacks, parries, counterattacks with recoil, and maximum collisions. [Reference Image and Fixed Person] @1参照画像と**@2参照画像を each is interpreted as a different person. Reference images are used only for maintaining face, eye shape, iris color, hairstyle, hair color, costume, decorations, physique, silhouette, atmosphere, character color, and existing weapon designs. Backgrounds, rooms, furniture, text, split layouts, poses, compositions, angles, and framing from reference images are not reproduced. Throughout the story, the two are the same person, the same person, the same character identity. Only facial expressions, gazes, mouths, postures, breathing, and natural hair and clothing movements can change. Face averaging, feature mixing, hair color swapping, costume swapping, weapon swapping, altering humans, cloning, clones, and adding unnecessary characters are all prohibited. From the reference images, the main color, secondary color, accent color, texture, decorative motif, and worldview of each character are extracted, and thereafter used as the @1 unique color and @2固有色**. Colors are not exchanged between the two of them. Backgrounds, props, illuminated guide lines, floor reflections, air, steam, lighting, and effects are all redesigned to harmonize with the two characters' costumes, decorations, personalities, and worlds while maintaining the fixed stage structure. However, the flow of battle, positional relationships, contact points, and camera order remain unchanged. [Fixed Style] Fine, delicate colored outlines. Clear two- to three-tier celshading and transparent intermediate shadows on faces, hair, costumes, and equipment. Using the natural colors of reference images with clear high saturation, with multi-layered highlights for eyes and hair. Faces, hair bundles, embroidery, decorations, metals, jewelry, and even weapon equipment are densely packed. Draw cloth, leather, metal, jewelry, wet floors, and glass with different reflections and roughness. Each character's unique color is used for key lights and shadow colors, with the background set one shade darker than the character. Thick black outlines, flat single-layer cel shadows, simplified TV animation, universal 3D beautiful girl faces, mature, smooth plastic CG, semi-realistic, realistic, low-density backgrounds, dull colors, and no mixing of art styles. [Setting & Atmosphere] A near-future academy city after the rain, a wet rooftop training ground at dusk. Luminous induction lines, colored reflections on the floor, high-rise school buildings, glass walls, urban skyline, thin steam. Except for the two of them, no one is around. Architectural decorations, floor patterns, handrails, lighting fixtures, training equipment, and abstract patterns in long-distance advertisements match the motifs of reference figures, but text, logos, and UI are not included. [Camera] Instead of a fixed horizontal view, use a low-angle camera that approaches the final collision in sequence with about 60-degree rotation around the @2を追う床すれすれの低い三分の四, @1の胸上の斜め前, @1の肩越し, and contact points. The camera and background rotate, preventing people from spinning meaninglessly. [Weapon Locked] Each of them carries only one sword, totaling two. If the reference image includes a weapon, its shape, length, decoration, and color scheme are preserved; if it is not a sword, it is redesigned as a single sword that inherits that design. All cuts fix the number of blades, blade, tsuba, hilt, scabbard, and tassel connection. The hand grips only the handle behind the tsuba. The blade, tsuba, and hilt are used as a single weapon, moving from the shoulder, elbow, waist, and supporting leg, without rotating only the blade or tip. @1は弾きの瞬間だけ右手で柄を腰近くに保持し, use your left index finger. @2は刀を両手で保持する. [Movement] Cut 1: The @1固有色の水平斬撃光がレンズ前を横切る瞬間から開始 at the end of the preceding clip. The light is a curved afterglow closely attached to the sweeping surface of the sword, not an independent laser. When the light escapes, the camera connects to the left rear of @2, at the lower four-thirds position just above the floor. @2は左足で濡れた床を蹴り, he struck @1's right shoulder with both swords and delivered a diagonal downward swing from the upper right to the lower left. Water droplets, hair, and fabric flutter in the opposite direction of acceleration. @2固有色** blade light covers the lens, acting as a shielding wipe for the next close-range shot. Cut 2: @2の刀光が抜けると**@1の胸上を斜め前から映す. @1は一歩も退かず無表情. Hold the sword low with your right hand and form a single thin hexagonal defensive surface with @1 unique color in front of your left index finger. @2の斬撃が防御面中央の単一接触点へ当たり, local flash, hexagonal ripples, @2固有色の火花が同期する. @1が指と手首を数センチ外側へ弾くと, the entire defensive surface tilts and @2の軌道が@1の肩外側から約45度上方へ偏向される. The opposite reaction force returns to @2**'s arms, shoulders, and hips, and the supporting leg steps back down. The camera follows the deviated trajectory with a whip pan. Cut 3: @1の肩越しへ入る at the end of the whip pan. @2は返った反力を使い, he rotated his hips once using his left foot as the pivot for a low counter slash. @1は左手を柄へ戻し, the center of the blade is hit at a single point, and immediately after a short hit stop, the contact surface slides to deflect the @2 blade upward and outward. @1 then stepped into his pocket and returned a rising slash in @1's unique color from the lower left to the upper right. The camera rotates about 60 degrees around the contact point, causing significant movement between the railing and floor reflections. @2は斜め後方へ押され, he spins half a circle in midair, lands with his right foot, and slides briefly. @1は止まらず前進する. @2だけが押し戻される**Asymmetric movement. The splash of water from the landing covers the bottom of the screen. Cut 4: Beyond the splash, @1を左手前に大きく, @2を右奥に置く斜め低空構図. Don't put the two side by side. @2は滑りの終端で右足を踏み直し, without stopping, @2固有色の振り下ろし from the upper right to the center. @1も前進を止めず, from the lower left to the center, @1 unique color ascending slash. From beneath and behind them, massive flame-like auras of their unique colors erupted, accompanied by glowing cracks in the floor, thin electric flashes, and upward currents. The two colors do not mix. For the brief moment when the two swords enter the same contact point, the shape is read, and after contact, it is hidden in the glow. Using the same contact point as the source, @1の直線軌道と@2の湾曲軌道が巨大なX字を形成する. Only the narrow incandescent center is pure white, leaving the two unique colors outside it. It maintains a large area of highly saturated color fields, radiating shock waves, concentric pressure waves, vertical flame-like aura, volumetric light, electric light, and sparks from the same impact core. Floor water, steam, dust, debris, hair, and costumes are blown outward, and colored effects occupy most of the screen. @1の圧力で@2の防御姿勢が崩壊する. ** The camera briefly rushes to the contact point, is pushed back slightly by the shockwave, and tilts several degrees. Do not make the entire screen white. [Major NG] Fixed horizontal fighting game perspective, symmetrical full-body composition, re-partitioning to separate two people to the left and right edges, simultaneous reversals, simultaneous mirror dashes, long run-ups, long sword clashes, meaningless continuous spins, independent laser, third beam, two-color fusion, full-screen blank display, no text, subtitles, logo, watermark, UI, or sound generation. [Terminals] @1のエネルギーが接触点を**@2側へ押し, @2側の水煙と砂塵が後方へ膨む. @2のシルエットが斜め後方へ崩れ始め, @1** keeps pushing forward with a low center of gravity. The massive two-colored X-shaped light expands to its maximum, and at the moment the person and blade conceal themselves in the light, the frame captures the start of collapse and immediately cuts through the frame. Actions continue.
```

#### 📌 Details
- Ratio: `1.74` | Duration: `8.21s`

---

### 🎬 Ultimate Sword Skill Chops Scallions
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10869.jpg" width="480" alt="SD2_10869"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sword-immortal-chops-scallions-SD2_10869">🌐 Watch Online</a>

#### 📝 Prompt
```
[Style] A pure ancient-style xianxia cold comedy with a cinematic sense of realism, exquisite commercial cinematic visuals, and a fast-paced short video narrative, but overall performance is restrained and not exaggerated. The first half creates a solemn xianxia atmosphere of "profound swordsmanship," while the second half reveals the results to create a cold, twisted comedy. Drawing on classic physical comedy staging techniques, the humor relies on clear spatial relationships, foreshadowing, character reactions, and a calm finishing line at the end. The entire film strictly maintains the context of ancient China, avoiding any modern objects, clothing, architecture, language, or sound effects. Each shot preserves only one clear main action, without stacking complex behaviors. [Duration] 10 seconds, three-shot structure, 2 people on camera, 16:9 landscape mode. [Scene] Quiet morning in the kitchen courtyard behind the mountain gate. Bamboo shadows fall on the gray stone floor, and the scene retains only a clay stove, a wooden counter, a steaming iron pot, a bundle of fresh green onions, hanging dried herbs, and neatly stacked firewood. All shots consistently maintain the same courtyard, clay stove, counter, iron pot, and bundle of green onions, with stable and clear spatial orientation. [Characters] Character A: Sword Immortal Sister @图片1. East Asian women aged 25–30, oval face, fair natural skin, dark almond eyes, long black hair half-tied up with a jade hairpin; Tall and slender. Face, hairstyle, makeup, body proportions, full outfit, shoes, accessories, and clothing colors must strictly match the reference images. Wear a white embroidered silk Hanfu, layered wide sleeves, light-colored waistband, silver waist ornaments, and white cloth boots. Her temperament is cool, confident, and restrained, with a hint of pretentious composure and profundity. Character B: Junior Sister @图片2. East Asian women aged 20–25, with a round, lively face, braided black hair, and petite figure. Face, hairstyle, body proportions, clothing, shoes, and accessories must strictly match the reference images. Wear a teal linen hanfu, dark cloth belt, plain headband, and black cloth shoes. She is sincere and admires her senior sister, but expresses calmness and naturalness, with a cool, comedic touch at the end. [Lens 1] 0–3s, panoramic shot, stable and slow track push. In the quiet kitchen courtyard behind the mountain gate in the morning, bamboo shadows fall on the gray stone floor. Only the clay stove, wooden table, hot iron pot, green onions, dried herbs, and firewood remain in the painting. The same Sword Immortal Sister @图片1 stood fully from her shoes to her head on a slightly elevated stone platform, hands behind her back, chin slightly raised, posture calm. The same silver flying sword gracefully traced a full arc around her, leaving only restrained pale blue sword light shadows. The same junior sister @图片2 stood beside the desk, looking up sincerely and admiringly. Accompanied by a solemn guqin, distant birdsong, and a faint hum of sword energy. This shot shows only one main action: a flying sword winding through a full arc. [Lens 2] 3–6s, 50mm medium scene dialogue shot. The same junior sister @图片2 looked up and asked, her Mandarin mouth movements accurate and natural, as she replied: "Senior sister, what kind of sword technique is this?" The same Sword Immortal Sister @图片1 raised two fingers and calmly replied: "Ten thousand swords return to the sect." As soon as he finished speaking, the same silver flying sword suddenly accelerated toward the same wooden desk. Only layered sword light and trailing shadows are allowed to express sword intent bursts; no duplicates of multiple physical flying swords are allowed; only the same flying sword is always allowed. The background always maintains the same courtyard, the same counter, the same iron pot, and the same bundle of green onions. This shot shows only one main action: the flying sword suddenly accelerates toward the table. [Shot 3] 6–10s, close-ups revealed, followed by extreme close-ups, clean and hard cuts. The same flying sword quickly and precisely cuts the same bundle of green onions into evenly sized rings, all neatly placed into the same steaming iron pot. The physical effects of flying swords, scallions, steam, and sword light trails must be realistic and natural. The grand xianxia music stopped instantly. The same junior sister, @图片2, looked down at the pot, expressionless, and calmly finished off: "Enough scallions, but the dough isn't done yet." Then I forced myself to a close-up of the same Sword Immortal sister @图片1. She still tried hard to maintain her refined demeanor, but one eyebrow twitched slightly, and the once smug smile slowly faded, replaced by a brief and awkward quiet pause. Finally, it ends with a crisp wooden fish strike. [Performance Requirements] The first half must truly convey the solemnity of a master performing superior sword techniques; the Sword Immortal Sister must not show any comical side too early. The twist and humor comes from "Ten Thousand Swords Return to the Sect," but in the end, it's just chopping scallions. The junior's finishing blow must be natural, calm, and restrained, creating a cold, comedic effect. Sword Immortal Sister's awkwardness is handled by micro-expressions, focusing on her slightly twitching eyebrows and the fading smile at the corners of her mouth—avoid exaggerating or making her expression too large. [Technical Requirements] Seedance 2.0 prioritizes optimized reference image consistency, dual-role stability, spatial continuity, Mandarin lip-sync synchronization, and clear movement execution. The entire film is in 16:9 landscape mode, with a strict total length of 10 seconds, realistic and live-action with cinematic natural morning lighting, no subtitles generated, and clean hard cuts. Character facial stability is required, costumes are consistent throughout, movement relationships are clearly defined, and teleportation, background drift, and prop disappearance are prohibited. [Sound Effects] The solemn guqin, distant birdsong, faint hum of sword energy, the crisp sound of scallions being sliced by flying swords, the soft crunch of scallions falling into the pot, the faint steam of iron pots, the last half second of awkward and quiet pause, and finally wrapped up with a crisp wooden fish strike. [Negative words] blurry, bad quality, low quality, low resolution, noisy, jpeg artifacts, watermark, text, subtitles, caption, error; deformed, mutated, bad anatomy, poorly drawn hands, bad composition, out of frame, disfigured; inconsistent character, changing clothes, changing hairstyle, face morphing, unstable face, background shift, glitching cuts, disappearing props; duplicated sword, extra swords, multiple entity flying sword, broken spatial continuity, wrong lip sync, modern objects, modern clothes, modern architecture, modern sound effects
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.08s`

---

### 🎬 Clumsy Girl's Iced Coffee Quest
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10867.jpg" width="480" alt="SD2_10867"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/clumsy-coffee-quest-SD2_10867">🌐 Watch Online</a>

#### 📝 Prompt
```
POV MiniDV camcorder vlog filmed entirely by the main character herself. The camcorder is never visible. Authentic early-2000s DV tape aesthetic with soft analog blur, subtle tape grain, faint tape hiss, slight colour bleed, blooming highlights, autofocus hunting, exposure breathing, muted contrast, imperfect white balance, realistic skin texture, natural motion blur, handheld shake, crooked framing, delayed focus, accidental head crops, awkward zooms, and genuine human camera movement. Documentary style, not cinematic perfection. Main Character: The same recurring fictional Japanese woman for every episode. Early 20s, very fair porcelain skin, naturally beautiful, long dark brown-black hair in a loose ponytail with soft face-framing strands, expressive brown eyes, natural makeup, slim petite build, oversized cream hoodie, black leggings, white sneakers, warm smile, playful and slightly clumsy personality. Location: Quiet Japanese neighbourhood during golden hour, tree-lined sidewalks, small local café, soft evening sunlight, peaceful atmosphere. Scene 1 (0–2s) Handheld selfie while leaving home. "Okay... today's mission is simple. One iced coffee... then straight home." Scene 2 (2–5s) Walking down the street. She notices a fluffy dog, crouches to pet it, laughs. "...No, stay focused... coffee first." Scene 3 (5–8s) Camera propped on the café counter. She reaches for her pocket to pay and suddenly freezes. "...Wait... where's my wallet?" Scene 4 (8–11s) Quick panic. She checks another hoodie pocket, finds it instantly, bursts into genuine laughter. "Never mind... false alarm!" Scene 5 (11–15s) Walking outside with the iced coffee during golden hour. Takes the first sip, smiles at the camera. "Mission accomplished... see you in tomorrow's chaos." Audio: No background music. Only authentic ambient sounds: birds, footsteps, distant traffic, café ambience, doors opening, soft wind, clothing movement, breathing, laughter, and natural voice. Overall feeling: Cozy, wholesome, funny, spontaneous, highly realistic, authentic camcorder diary, social-media-friendly pacing, emotionally warm, subtly humorous, and designed to feel like viewers are spending 15 seconds with a real person rather than watching a scripted video.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 Idol Backstage Fitting Room Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10866.jpg" width="480" alt="SD2_10866"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/idol-backstage-fitting-vlog-SD2_10866">🌐 Watch Online</a>

#### 📝 Prompt
```
DV 16mm handheld camcorder POV, CHASE filming herself, occasionally propped against a fitting-room mirror. Natural hand shake, imperfect framing, delayed focus, clumsy zooms, tape blur/noise, bloomed vanity lights, flickering auto-exposure, muted contrast, realistic skin. Playful, energetic backstage fitting-room vlog with quick pacing. CHASE: Korean idol in her 20s, long straight black hair, dewy glass skin, coral lips, large eyes, slim. Wears two fully modest stage outfits (1: fitted long-sleeve top + tailored trousers, 2: high-neck dress over long-sleeve base layer), minimal jewelry. Backstage fitting room with mirror, garment rack, stylist off-camera, pins/fabric clips. Sequence: outfit 1 mirror turn ("Okay, first outfit—let's see."), smooths fabric ("I really like this fit."), stylist pins waist (ambient only), playful spin ("Moves pretty well!"), quick change to outfit 2 ("Now let's compare."), compares ("More elegant, but the first had better movement."), close-up thinking ("I genuinely can't decide."), selfie spin ending ("I'll let the team decide—see you on stage!"). Camcorder never visible.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Neon Graffiti Underpass
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10865.jpg" width="480" alt="SD2_10865"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/neon-graffiti-underpass-SD2_10865">🌐 Watch Online</a>

#### 📝 Prompt
```
Cinematic anime short film clip, 15 seconds. Underground street tunnel at night, long dark corridor, walls completely covered in colorful graffiti tags, wet glistening asphalt reflecting dim tunnel lights, raw illegal underground energy, nobody around.
```

#### 📌 Details
- Ratio: `0.89` | Duration: `14.43s`

---

<!-- STATS_END -->
