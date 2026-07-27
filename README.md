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
- Total Prompts: **8382**
- Updated Today (UTC 2026-07-27): **32**

## 🎬 Today's Updates
### 🎬 Summer Resort Water Slide Vlog
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10781.jpg" width="480" alt="SD2_10781"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/summer-resort-water-slide-vlog-SD2_10781">🌐 Watch Online</a>

#### 📝 Prompt
```
: Female protagonist. In all the clips, her facial features must be perfectly preserved, including eye shape, nose, mouth shape, facial contours, and consistent hair color. Even if the shooting angle of each shot changes, it must clearly identify the person as the same person. Clothing is not fixed and references @ images; each outfit must strictly follow the corresponding text instructions. Ignore the background, pose of the person, and the text at the bottom of the screen in the @图片. (2) Subject and space Solo travel vlog at the Summer Resort. People pass by in order: Hotel rooms → balconies→ hotel water park→ large water slides→ and sinks. All scenes are located within the same resort hotel. From the guest room balcony, you can clearly see the outdoor water park downstairs. From the balcony's viewpoint, you must see a turquoise sink, shallow recreation area, sun umbrellas, and a prominent large open water slide. The water park, water slides, and sinks that are actually entered afterward must maintain the same spatial relationship and structural continuity as seen on the balcony. The season is summer. Clothing is divided into two stages: First half (0–4 seconds): Lightweight summer casual wear. Second half (4–15 seconds): Minimalist black bikini. Each segment can only wear the costume specified in the segment command; clothing within the same segment cannot be changed. During the 4–15 seconds, the female lead does not wear sunglasses, hats, or hold any props. (3) Timeline Total duration: 0–15 seconds, 7 segments. Each segment contains only one core action and may not be merged or omitted without authorization. 0–2 seconds [Arrival/Guest Room] The bright resort hotel rooms are mainly made of white linen, light-colored wood furniture, and off-white soft furnishings, with afternoon sunlight streaming into the interior from the balcony. The female lead walks into the room wearing a thin linen shirt and shorts, dragging her suitcase. The front-facing handheld wide-angle selfie starts with a close-up full-body shot, and the camera quickly zooms in on her. She said brightly and happily to the camera: "The summer vacation has finally begun!" 2–4 seconds [Display Scenery/Balcony] Keep up with the same summer casual outfits. First, a close-up shot of the hand pulling open the white curtains is taken, then the focus quickly shifts to the hotel water park downstairs outside the floor-to-ceiling glass window on the balcony. The image clearly shows the curved structure of the large open water slide and the connected sink. Then the camera quickly switched to her facial reaction as she turned away. When she saw the water slide, her eyes widened slightly, the corners of her mouth lifting into an expression of surprise, excitement, and eagerness to play. 4–6 seconds [Entering the water park/park trail] The female lead switched to a simple black bikini, went barefoot, and kept her hair dry. Handheld camera, she follows her into the hotel's water park. She quickly walked along the damp park trail toward the large water slide she'd just seen from the balcony. The scene naturally undulates and sways with her steps, with tropical plants, shallow water, umbrellas, and sparkling water in the background gliding behind her, and the waterslide always in the direction she is heading. 6–8 seconds [Climb to the slide/slide entrance] Keep the black bikini, your hair still dry. This segment is a fast, continuous montage, but the core move must be clear: climb the slide and sit at the entrance to prepare for departure. First, we filmed close-ups of her barefoot feet on the wet steps, then quickly switched to her gripping the railing as she climbed the steps, and then cut to the top entrance of the slide. After reaching the top, she turned and sat at the entrance of a large open water slide, legs naturally forward, hands at her sides, striking a stable and correct body skiing posture. A frontal close-up capturing her nervous yet excited expression. She looked at the camera and said clearly: "I'm going to slide down!" 8–11 seconds [High-speed slide / inside the waterslide] The female lead quickly slides down the same large open water slide. A waterproof wide-angle camera fixed in front of the slide, facing the female lead's upper body and face, was used to film the entire water skiing process, with the camera position consistent and not arbitrarily switching to other angles. She clearly shows her speeding down the slide. The slide passes one or two clear bends, with the character's body naturally tilting left and right along with the turns, their hair swayed by air and water, and their faces showing genuine, excited smiles and brief exclamations. Sunlight, shadows, and splashing droplets of water swiftly skimmed across the frame. Throughout the process, she must stay glued to the slide, not levitating, flipping, flying, or suddenly detaching from the slide. 11–13 seconds [Rush into the sink/slide exit] Keep the black bikini. The lens switches to a fixed, waterproof low camera position, directly in front of the slideway exit, near the water surface. She rushed from the slide exit into the sink at high speed, her body fully plunged into the water, splashing huge, real splashes. The front of the water splash covers the camera lens, with a few droplets left on the lens surface. After entering the water, she briefly disappears underwater, unable to stand up immediately after exiting the slide or come to a stop on the surface. 13–15 seconds [Ending / In the Sink] She naturally emerged from the water, her hair completely soaked by now. She first used both hands to comb her soaked hair back. Then quickly complete three consecutive shots: Close-up from the front: She closes her eyes and combs her wet hair back, with water droplets trickling down her face and shoulders. Close-up from the side: wet hair brushing her cheeks and neck, water droplets continuing to slide down, she slightly turns her head. Back to the close-up: she looks back at the camera and naturally smiles, the frame frozen in the final frame. The water droplets on the lens surface remain and do not disappear. (4) Cameras and audio Camera: Use a quick editing rhythm that switches shots every 0.5–1 second. Overall, it maintains the feel of handheld iPhone photography. 16:9 landscape format. Mix closer, zoom out, and tilt upward shots. Guest rooms, balconies, and water park walkways preserve natural handheld shaking, autofocus to find focus, and slight exposure fluctuations under direct outdoor sunlight. The inside and exit of the waterslide use real waterproof wide-angle camera positions, ensuring close contact with the water surface, strong speed, and a slight splash effect on the lens. Audio: No background music is added. Layered real environmental sounds include: The sound of the trunk wheels rolling The sound of the curtains being pulled open The sound of water park water drifting from outside the balcony The sound of cicadas The sound of barefoot stepping on damp ground The sound and echo of flowing water in the park environment The sound of footsteps climbing the steps The sound of water flowing continuously intensifies inside the waterslide The sound of wind and splashing water during high-speed descent The tremendous crash of water rushing into the sink Laughter naturally erupts after surfacing All dialogue must be in natural, clear Mandarin Chinese. Character lip movements, pronunciation rhythm, emotion, and Chinese lines must be accurately synchronized. Do not generate Korean, English, or other languages, nor add narration, explanatory dialogue, or irrelevant announcements yourself. (5) Style and Limitations The overall look features bright, vibrant natural summer light tones, with a subtle film texture to create an Instagram travel vlog vibe. Preserves the true texture of the skin, including pores, fine hairs, natural oily glow, and the real water droplets, wet hair, and moist skin in the latter half. The use of beauty filters is prohibited, and CGI or overly artificial skin textures are prohibited. Do not merge shots or omit any scenes without authorization. No need to change clothes. Between 4 and 11 seconds, hair must be kept dry and only exposed to wind; After 11 seconds, he rushed into the sink, his hair and body completely soaked. Water parks visible from the balcony, subsequent water parks, large water slides, and sinks must maintain complete spatial continuity and must not suddenly change venues or facility structures. The slide must always be a large open human slide and must not suddenly become a closed pipe, double slide, or other facilities. No text should be added to the screen.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

### 🎬 Mumbai Tsunami Emergency Evacuation Footage
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10780.jpg" width="480" alt="SD2_10780"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/mumbai-tsunami-evacuation-SD2_10780">🌐 Watch Online</a>

#### 📝 Prompt
```
Super casual real smartphone home video footage of the sudden tsunami emergency in Mumbai. Natural mobile phone camera recording with slight authentic handheld shake, normal frame rate with smooth natural motion, rapid-fire montage with constant quick jump cuts every 1–2 seconds like footage captured during a real emergency. Unpolished authentic phone recording of a mixed group urgently running together, warning one another, helping each other evacuate, and moving toward higher ground. Pure raw home video feel with no cinematic polish or heavy effects. Use the provided reference photo as the STRICT ONLY visual reference for the main woman. Maintain her exact appearance with zero deviation: [her described features]. Generate a mixed group of friends of all ages around her during the evacuation. 0–2.5s: Shaky handheld rapid cuts of the main woman suddenly running with friends away from the Mumbai shoreline after people begin shouting tsunami warnings. Wind blows through her hair. Quick flashes of feet splashing through shallow water and people rushing inland. 2.5–5s: Abrupt jump cuts showing a close-up of her looking back toward the ocean with concern, followed by the group running through crowded streets while warning others and checking on one another. 5–7.5s: Fast handheld footage of her helping a friend keep pace while everyone continues running toward higher ground. Natural daylight creates subtle lens reflections and realistic exposure changes as the phone moves naturally. 7.5–10s: Quick cut to a close-up of her giving a determined look toward the camera before turning back to continue running. The footage immediately jumps to the group climbing a staircase or elevated walkway together while people continue evacuating around them. 10–12.5s: Abrupt edit showing everyone reaching a safer elevated location, catching their breath and checking that everyone is safe. Friends point toward the distant shoreline while talking over one another. 12.5–15s: Final rapid transition showing the main woman standing safely among her friends, breathing heavily while quietly looking back toward the ocean. The video ends naturally with a gentle phone sway as if someone simply stopped recording. VISUAL STYLE: Natural smartphone video quality. Slight realistic handheld shake. Smooth normal frame-rate motion. Authentic casual interactions and physics. Realistic daylight and exposure adaptation. Stable main character consistency. Unpolished home phone recording aesthetics. No professional stabilization. No cinematic color grading. No beauty filters. No artificial effects. No AI artifacts or glitches. IMPORTANT GENERATION REQUIREMENTS: Consistent identity throughout the video. Realistic human anatomy and hand interactions. Natural running and body movement. Authentic Mumbai ambience with distant crowd voices, wind, rushing water, and city environmental audio. Physically correct lighting and shadows. Rapid mem
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Dreamy Resort Girl
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10779.jpg" width="480" alt="SD2_10779"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dreamy-resort-girl-SD2_10779">🌐 Watch Online</a>

#### 📝 Prompt
```
High-quality animated footage. Refer to the characters in the source image and strictly maintain the same character throughout the entire story. Reference images are used only to maintain a character's face, contours, eye shapes, irises, hairstyles, hair color, hair volume, costumes, decorations, physique, body proportions, silhouette, atmosphere, and character colors. The background, room, furniture, poses, expressions, angles, and framing of the reference image itself are not reproduced. Only facial expressions, gazes, mouths, poses, breathing, and the natural swaying of hair and clothing can change. Mixing features, averaging faces, changing hairstyles, altering hair color, swapping outfits, losing decorations, changing body shapes, altering people, cloning, or adding unnecessary characters are all prohibited. Throughout, it consistently maintains high-quality animation expression best suited to the character in the reference image. The base is a delicate hand-drawn anime-style look, with thin lines, elegant and transparent colors, and the skin, hair, fabric, and decorations are applied softly to create a luxurious anime look. If the reference image has a bright atmosphere, lean toward a refreshing tone; if calm, lean toward an elegant and quiet tone. However, the art style itself remains consistent, avoiding bold lines, low-budget TV animation, semi-realistic adaptation, live-action adaptation, plastic CG production, excessive 3D effects, and mixed art styles. The location is fixed throughout the entire film in a bright, outdoor luxury resort space. The basic composition maintains white architecture, blue skies, open terraces, parasols, distant palm trees, and soft daytime natural light. The background is fresh and bright, with light bokeh and depth so that the characters appear to be the main characters. The structure of the location, the setting of an outdoor resort, white architecture, blue sky, terrace, parasols, and palm trees are maintained. Then, naturally adjust only the parasol, cushions, flowers, table accessories, decorative fabrics, reflected light, and background accent colors to match the character colors, costume color schemes, decorative motifs, and personality atmosphere of the reference image. The background is mainly used to enhance the character, making it less noticeable than the person. I don't do it anywhere else. This footage is not a strict reproduction of the original video, but rather redesigned into a social media-worthy camera work that makes the body look attractive while maintaining the same fresh atmosphere. Exact facial expressions are not required, but faces should be clearly readable throughout the entire story. Insert face rewards that clearly show the face, eyes, cheeks, and mouth multiple times. Facial expressions should match the character's natural mood, focusing on a natural, gentle gaze, a light smile, a hint of shyness, or a subtle, calm smile. The footage begins with a medium shot that shows up to the thighs. The character should be oriented slightly in four or three directions, with legs, waist, chest, shoulders, hair flow, and the main costume decorations all at once. From the start, the camera enters with a slightly forceful, smooth forward and diagonal movement, following the thighs, waist, chest, shoulders, and face with pleasure as if the gaze is flowing from below to the top. However, they must not leave their face behind; they must ensure that their face and eyes are clearly visible. The character naturally lifts both hands from below. Her hands don't cover her face, moving up along her thighs, waist, and chest. Her fingertips are gently open, without straining. The camera follows her movements by combining slightly faster slides, light push-ins, and shallow turns, showing body lines, costume structure, decorations, and hair flow one after another. When your hand passes near the lens, you may create a light foreground blur, but make sure the face, eyes, cheeks, and mouth are always readable. Do not hide your face with your hands for long. The camera is not fixed in front but quickly and shallow around left and right like licking in front of the character, showing the thighs, waistline, chest design, shoulders, neck, profile, flowing hair, and costume decorations at a fast pace. It has momentum but is not too rough, maintaining elegance. Sometimes, I look up from a slightly lower perspective, beautifully showing the length of my legs and the line that connects from my thighs to my waist. If necessary, you can instantly zoom in from a mid-range view up to your thighs to a close-up above your chest, then return to your thighs. Create a rhythm that stands out on social media by changing camera speed. In the middle section, the gaze flows from the chest to the hands, hands to hair, and hair to the face. Movable elements in the reference images—hair, skirt hems, coat hems, ribbons, lace, accessories—sway softly, half a beat behind body movement. The character slightly twists their shoulders, lightly shifts their center of gravity onto one leg, and stances that naturally and beautifully complement their body shape and costume silhouette. Rather than grand acts, he prioritizes a sophisticated body presentation like a fashion video. Somewhere in the middle, he takes a shot near his chest, clearly showing his face and eyes toward the front. In the final part, you can use a move where both arms are raised upward, but the camera is pulled away to avoid showing the whole body. While maintaining a range between mid-range and close-ups where the thighs are visible, slightly faster diagonal rises, light turns, and short turns make the shoulders, arms, chest, waist, thighs, hair spreads, and main decorations beautifully showcased. In the end, face rewards are the top priority. The camera naturally moves from above the chest to the bust up, with the character looking toward the front. In the final moment, the character looks directly at the camera, showing a natural, small smile typical of that person. Her eyes are bright, her cheeks are soft and relaxed, and her lips are smiling elegantly. Finally, the moment when that smile looking at the camera looks most attractive is cut. Overall, the camera doesn't move observantly slowly; instead, it chases people a bit faster, smoother, more tempo, and more pleasantly to capture them attractively. Refreshing and elegant, slightly like a fashion PV, bright and sophisticated to create SNS-worthy footage. No text, no subtitles, no logo, no watermark, no unnecessary characters, no clones, no face distortion, no changes in eye shape or iris color, no proliferation of hands, arms, or fingers, no costume alteration, no loss of decoration, no hairstyle modification, no hair color alteration, no body shape change, no full-body pull finish, no hand movements to hide the face for a long time, no camera stopping abruptly, no rigid standing pose, no background position change, no mixing of art styles.
```

#### 📌 Details
- Ratio: `1.34` | Duration: `6.25s`

---

### 🎬 Live Stock Market Crash Report
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10778.jpg" width="480" alt="SD2_10778"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/live-stock-market-crash-SD2_10778">🌐 Watch Online</a>

#### 📝 Prompt
```
BROADCAST TYPE: Live business news report covering a sudden stock market crash during trading hours. ON-AIR REPORTER: Female journalist, early 30s. Sharp blazer, earpiece, handheld mic with financial network logo. Composed but visibly tense. LIVE BROADCAST TIME: 11:20 AM. Bright daylight, glass-walled trading floor visible behind glass partition. REPORT LOCATION: Outside a stock exchange building. Digital ticker boards flashing red numbers. Traders visible through windows, gesturing anxiously. Passersby stopping to check phones. BROADCAST CAMERA: Steady tripod-mounted main shot with a secondary handheld cutaway camera. Occasional quick zoom to ticker board numbers dropping. Reflections of red digital numbers on glass. LIVE SEGMENTS: Opening: Reporter explains the sudden index drop and market panic. Update: Camera cuts to trading floor screens showing plunging graphs. Eyewitness Moment: A trader stepping outside briefly comments on the chaos. Situation Change: Ticker shows a fresh plunge, reporter reacts live to the number. Closing: Reporter signs off, noting market will be watched closely into afternoon. LIVE AUDIO: Muffled trading floor shouting, city traffic, notification pings from nearby phones, reporter's controlled voice, no music. BROADCAST REALISM: Genuine tension, traders ignoring camera, real-time number changes driving reactions, natural interruptions from passersby glancing at screens.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Cinematic Dragon Bond On Alpine Peak
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10776.jpg" width="480" alt="SD2_10776"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alpine-dragon-bond-SD2_10776">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 15-second hyper-realistic live-action cinematic video in 16:9 with fast-paced, emotionally warm storytelling, spectacular action, and seamless multi-shot transitions. Absolute photorealism with feature-film quality, shot on anamorphic 35mm lenses, realistic camera physics, subtle handheld movement, natural lens breathing, cinematic motion blur, restrained film grain, and physically accurate lighting. The scene takes place entirely on a rugged alpine mountain summit with jagged gray metamorphic rocks, loose gravel, exposed cliff edges, dry golden alpine grass, distant mountain ranges, a deep blue sky with thin cirrus clouds and low white cumulus clouds, illuminated by crisp late-morning sunlight. Maintain perfect environmental continuity throughout every shot. The main character is a beautiful woman, approximately 25 years old, with long thick naturally wavy blonde hair, fair skin, bright blue eyes, and an athletic feminine build. She wears a weathered brown leather medieval explorer outfit consisting of a fitted leather tunic, dark trousers, tall leather boots, leather bracers, a travel satchel, a belt, and a medieval sword. Preserve her exact facial features, hairstyle, clothing, body proportions, and identity consistently throughout the entire video. Her companion is a gigantic biologically realistic pink-red dragon with dusty reptilian scales, amber eyes, curved horns, muscular limbs, powerful claws, a long tail, and large translucent wing membranes with visible veins. The dragon behaves like a real undiscovered animal, with subtle breathing, shifting muscles beneath its scales, moist reflective eyes, realistic weight, and physically accurate interactions with the environment. The dragon always remains vastly larger than the woman. A powerful alpine crosswind acts as a third character throughout the sequence, constantly influencing the woman's flowing blonde hair, clothing, satchel straps, grass, dust, loose gravel, and the dragon's wing membranes and neck spines. Every gust behaves naturally according to the terrain and camera angle, with believable delayed secondary motion. The sequence begins with an extreme ground-level camera hidden between dry grass and sharp rocks. Wind drives dust and gravel across the lens while the woman stands confidently on the exposed ridge. A gigantic dragon shadow sweeps rapidly across the landscape before one enormous wing passes overhead, dramatically darkening the frame and creating a violent pressure gust. Cut to a dynamic forward-moving perspective traveling low toward the woman as the dragon approaches at high speed. The mountain rocks rush past with strong parallax while her long blonde hair and leather clothing whip dramatically in the wind. The dragon's heavy breathing creates subtle camera movement. Transition into a fast lateral tracking shot racing parallel to the rocky ridge. Foreground boulders repeatedly hide and reveal the action while the dragon runs beside the woman with tremendous weight. Massive claws strike loose gravel, sending rocks toward the camera as dust trails behind. The dragon suddenly brakes beside her, carving deep tracks into the rocky ground while a sweeping cloud of dust fills the frame. Move into a close reverse circular orbit around both characters as the dragon gently lowers its enormous head. The woman smiles warmly, steps closer, and softly places one hand against the dragon's snout. Their foreheads gently touch in an intimate emotional moment as the dragon's folded wing temporarily shelters them from the wind. Focus shifts naturally from her fingers resting on the scales to the dragon's amber eye and finally to her genuine smile. Cut to an unusual snout-mounted close-up beside the dragon's muzzle. The dragon gives a playful snort, blasting a gust of wind that sends the woman's long wavy blonde hair, clothing, and satchel flying backward. Laughing naturally, she briefly loses her balance before affectionately pushing the dragon's muzzle away with both hands. The dragon playfully nudges her again while the camera receives a subtle physical bump, creating an authentic documentary feel. Transition to a perfectly vertical top-down aerial shot directly above the rocky clearing. The dragon unfolds its enormous wings around the woman, nearly filling the frame. A single powerful wingbeat creates a visible expanding pressure wave across the terrain, pushing dust, grass, gravel, and clothing outward in physically accurate concentric motion. The woman crouches, shielding her face while laughing as the dragon begins its powerful takeoff run. Finish with a dramatic cliff-edge aerial shot as the dragon launches directly over the camera. Loose stones fall past the lens while one translucent wing passes overhead, revealing veins, scars, and stretched organic membranes illuminated by sunlight. The camera dives backward along the cliff before stabilizing into a sweeping cinematic reveal of the mountain summit and expansive valley. The dragon performs one fast, low fly-by above the woman, whose hair and clothing are once again swept by the powerful wake. End with a wide composition of the woman standing alone on the exposed ridge as the dragon gracefully glides across the open sky above the vast mountain landscape. Maintain absolute live-action realism throughout with consistent lighting, geography, scale, anatomy, wind direction, environmental continuity, and character identity. Negative Prompt: CGI, animation, cartoon, stylized fantasy, magical effects, glowing eyes, fire breathing, supernatural particles, unrealistic physics, weightless movement, plastic textures, synthetic skin, morphing, duplicated characters, anatomy changes, inconsistent scale, extra limbs, deformed wings, inconsistent lighting, random landscape changes, HDR look, oversaturated colors, text, captions, subtitles, logos, watermarks, interface elements, low quality, blur, noise, artifacts.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Morning Latte Dreams
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10773.jpg" width="480" alt="SD2_10773"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/morning-latte-dreams-SD2_10773">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 35-second anime/Ghibli-inspired 2D commercial for Starbucks Bottled Coffee featuring a young man enjoying a bright morning in the city. He picks up a Starbucks Caffè Latte from a convenience store, takes a refreshing sip, then works and socializes with friends in a cozy café while using his laptop and notebook. Warm sunlight, soft colors, expressive character animation, and upbeat acoustic music create a cheerful, inspiring atmosphere. End with a close-up of the Starbucks Caffè Latte bottles.
```

#### 📌 Details
- Ratio: `0.89` | Duration: `31.22s`

---

### 🎬 Korean Youth Riverside Walk After Rain
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10772.jpg" width="480" alt="SD2_10772"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-youth-riverside-walk-SD2_10772">🌐 Watch Online</a>

#### 📝 Prompt
```
Main subject: Young Korean man, early 20s, natural everyday appearance, oversized cream knit sweater with sleeves slightly covering his hands, relaxed dark olive cargo pants, white worn sneakers, simple silver bracelet on left wrist, medium-length black hair with soft natural waves. Realistic skin texture, minimal styling, calm and thoughtful personality. Maintain identical face, hairstyle, clothing, body proportions, and appearance throughout the entire video.

Location: Quiet Korean riverside walking path after a light rain. Wet stone pavement reflecting soft daylight, wooden benches, willow trees, bicycle lane, shallow puddles, small bridge in the distance, green riverbank, gentle breeze moving leaves. Peaceful environment with no crowds, shops, advertisements, or tourist activity.

Visual Style: Hyper-realistic documentary footage. Ordinary daily life with spontaneous human behavior. Natural movement, subtle facial expressions, believable environmental interaction. Nothing staged or cinematic.

Camera Style: Mid-2000s MiniDV handheld camcorder. Friend casually filming. Constant handheld shake, imperfect framing, slow autofocus hunting, exposure fluctuations from cloudy skies, occasional rolling shutter, soft image quality, mild digital compression, slight color fading, visible sensor grain, subtle motion blur. No stabilization, no cinematic tracking, no modern grading.

00:00–00:02
The recording starts unexpectedly while he stands beside a puddle looking at the reflections. He lightly nudges the water with his sneaker, creating ripples. Camera briefly loses focus.

00:02–00:04
He walks along the riverside path carrying a transparent umbrella even though the rain has stopped. The camera trails behind while struggling to keep him centered.

00:04–00:06
He pauses beside a wooden railing, watching ducks glide across the river. Wind moves his hair naturally while autofocus shifts between the railing and his face.

00:06–00:08
He notices a small fallen maple leaf stuck on his sweater, laughs quietly, removes it, and lets it drift away. The camera zooms slightly by accident before correcting.

00:08–00:10
Passing beneath willow branches, he reaches up and brushes the hanging leaves with his fingertips while continuing to walk. Sunlight briefly breaks through clouds, causing exposure pumping.

00:10–00:12
He sits on a damp wooden bench sipping from a small convenience-store coffee cup. He glances toward the camera with a relaxed smile before looking back at the river.

00:12–00:15
As he walks away toward the bridge, he casually turns over his shoulder, gives a small wave, and quietly says, “Gaja.” The operator lowers the camcorder too early, cutting off the top of the frame before the recording abruptly ends.

Audio: Natural ambience only. Light wind, distant flowing river, birds, bicycle passing occasionally, soft footsteps on wet pavement, leaves rustling, ducks spl
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

### 🎬 Photorealistic Latiao Rooftop Commercial
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10770.jpg" width="480" alt="SD2_10770"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/latiao-rooftop-commercial-SD2_10770">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a 15-second photorealistic Chinese latiao commercial using @image1 only as a visual reference for the adult female model, study room, snack package, rooftop gathering, food appearance, and scene progression. Convert it into continuous full-screen live-action
```

#### 📌 Details
- Ratio: `0.8` | Duration: `15.04s`

---

### 🎬 Tokyo Tower Parkour Queen
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10769.jpg" width="480" alt="SD2_10769"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/tokyo-tower-parkour-queen-SD2_10769">🌐 Watch Online</a>

#### 📝 Prompt
```
Main subject: A young Japanese woman, confident, with a delicate face, long black hair and high ponytail, a white sports tank top, a white tennis sports skirt, and white and blue sneakers. At night, she parked at Tokyo Tower in downtown Tokyo. She greeted the camera, then immediately ran across Tokyo Bridge, jumped on the roof of a car, then quickly jumped onto the balcony of Tokyo Tower, then onto a huge supermarket billboard, and finally to the balcony on the third floor of Tokyo Tower. She looked up at the tower's tall, flashing rainbow lights, and charged up for a run, quickly running up the outer wall of Tokyo Tower. Her body was almost perpendicular to the tower's facade, and in 3 seconds, she ran from the base of the tower all the way to the top, with close-ups of her feet. She made the final leap to leap past Tokyo Tower, then steadily landed from the air and stood atop the tower. The camera quickly panted around, overlooking Tokyo's brightly lit night scene. The movements were dazzling and thrilling, with low-angle follow-up shots, high-difficulty sports photography, heroic perspective, and shaky moments. ，16:9
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.08s`

---

### 🎬 Cozy Japanese Grocery Store Animation
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10768.jpg" width="480" alt="SD2_10768"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cozy-japanese-grocery-animation-SD2_10768">🌐 Watch Online</a>

#### 📝 Prompt
```
A first-person animated journey in Japan: Ride a bicycle through a sunny traditional residential area, head to a local grocery store called "Kimura Shoten," enter the store, select fresh ingredients like tomatoes, potatoes, milk, chicken, eggs, and canned goods, pay at the counter with friendly staff, and pack groceries into the reusable "KIMURA STORE ECO-BAG." A warm and cozy atmosphere, with detailed Japanese landscapes and smooth, cinematic animation.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 Premium Bitbyte Break Ad
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10766.jpg" width="480" alt="SD2_10766"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/bitbyte-break-ad-SD2_10766">🌐 Watch Online</a>

#### 📝 Prompt
```
premium UGC-style bitbyte ad showing a young professional taking a relaxing break from work in a warm golden-hour home office, naturally enjoying a bitbyte with realistic chocolate and wafer details, ending with the message: “Have a Break. Grab Your bitbyte.”
```

#### 📌 Details
- Ratio: `1.77` | Duration: `5.0s`

---

### 🎬 Tokyo Parkour Rivals
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10763.jpg" width="480" alt="SD2_10763"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/tokyo-parkour-rivals-SD2_10763">🌐 Watch Online</a>

#### 📝 Prompt
```
FORMAT: 15 seconds, 16:9, 1080p, 8-cut cinematic ultra-advanced parkour footage. CHARACTERS: Two realistic individuals from image_1 and image_2. Use the attached images as absolute character references, and fully maintain the facial features, hairstyles, hair colors, skin textures, body types, height differences, outfits, color schemes, and age appearances of each person across all cuts. No altering into different people, face swaps, outfit changes, hairstyle changes, or mixing of the two individuals' features. SETTING: A sunny modern Japanese city reminiscent of Tokyo, Shibuya, and Yokohama — rooftops, alleys, staircases, railings, pipes, concrete walls. The two protagonists, as equals, race through at high speed running side by side, following, crossing paths, and coordinating. CUTS: 1. (00:00–00:01.60) Low-angle rear tracking. Both accelerate side by side and simultaneously kong vault over separate obstacles. 2. (00:01.60–00:03.40) Front low-angle. One wall runs the left wall, the other the right, then tic-tac to cross in midair and land on opposite rooftops. 3. (00:03.40–00:05.20) Lateral tracking. Consecutive precision jumps, then cat leaps to grab and climb a high wall. 4. (00:05.20–00:07.20) Rooftop tracking. The leader dash vaults, the trailer websters over the gap, then they swap front and back positions. 5. (00:07.20–00:09.20) Overhead moving camera. Both dive roll, then run side by side to speed vault a long railing. 6. (00:09.20–00:11.30) Handheld retreating from the front. One underbars, the other side flips, conquering the obstacle simultaneously. 7. (00:11.30–00:13.20) Drone from diagonal rear above. Both palm spin off left and right walls, kong vault, accelerate into the final jump. 8. (00:13.20–00:15.00) Climax. Both leap a large rooftop gap, each doing a corkscrew, camera circling them in midair as they land on separate rooftop edges — then run side by side into the distance. QUALITY: Live-action film quality. World-championship-level smooth freerunning. Realistic center-of-gravity shifts, muscle movement, natural landing impacts, swaying hair and clothing. Sharp background, natural motion blur only during high-speed movement. PROHIBITED: Facial distortion, altering into different people, face or body swaps, outfit changes, hairstyle changes, body type changes, limb multiplication, duplicates, body fusion, penetration, warping, floating, unnatural landings, anime style, CG style.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.17s`

---

### 🎬 Fashion Duo at African Opera House
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10762.jpg" width="480" alt="SD2_10762"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/fashion-duo-african-opera-house-SD2_10762">🌐 Watch Online</a>

#### 📝 Prompt
```
Main subjects: Two young East Asian women in their twenties, confident in temperament and delicate features. Figure 1 shows a woman in white, Figure 2 shows a woman in black Scene: Clear daytime, main venue of the African Opera House, with clear views of the Red Sea harbor bridge in the distance, bright and bright daylight
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.17s`

---

### 🎬 Anime Campside Beef Pho
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10761.jpg" width="480" alt="SD2_10761"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/anime-campside-beef-pho-SD2_10761">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a cinematic anime-style cooking video showing the outdoor preparation of authentic beef pho at a peaceful riverside campsite. Begin with slicing marbled beef, preparing ginger, onions, whole spices, fresh Thai basil, bean sprouts, and lime, then simmer beef bones, aromatics, and spices in a cast-iron pot over a crackling campfire to create a rich broth. Finally, place rice noodles in a ceramic bowl, top with thin beef slices, pour steaming broth to gently cook the meat, and finish with herbs, chili, red onion, and lime. Capture warm golden lighting, cozy camping vibes, detailed food close-ups, smooth transitions, and beautiful anime-inspired visuals.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.5s`

---

### 🎬 Sassy Luxury Skincare ASMR Routine
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10760.jpg" width="480" alt="SD2_10760"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sassy-luxury-skincare-asmr-SD2_10760">🌐 Watch Online</a>

#### 📝 Prompt
```
High-maintenance luxury beauty/skincare routine with sassy, condescending ASMR elements CAMERA / LOOK: Propped iPhone/Mini DV camcorder footage on a sleek vanity mirror stand. Soft diffuse lighting, delicate lens flare, gentle zoom adjustments, subtle tape
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.18s`

---

<!-- STATS_END -->
