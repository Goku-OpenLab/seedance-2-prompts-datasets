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
- Total Prompts: **7539**
- Updated Today (UTC 2026-07-11): **0**

## 🎬 Today's Updates
### 🎬 Birds Morph and Dissolve
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10084.jpg" width="480" alt="SD2_10084"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/birds-morph-dissolve-SD2_10084">🌐 Watch Online</a>

#### 📝 Prompt
```
The birds from &lt;video&gt; loosely form the imperfect shape of a bird based on &lt;image&gt;. They move to the music from &lt;audio&gt; and dissipate as they fly
```

#### 📌 Details
- Ratio: `1.78` | Duration: `8.25s`

---

### 🎬 Apartment Lights Dance to Music
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10083.jpg" width="480" alt="SD2_10083"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/apartment-lights-music-sync-SD2_10083">🌐 Watch Online</a>

#### 📝 Prompt
```
The lights of the apartments start turning on in sync with the music.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 Bee Transforms Into Fireflies
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10082.jpg" width="480" alt="SD2_10082"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/bee-to-fireflies-SD2_10082">🌐 Watch Online</a>

#### 📝 Prompt
```
Change the bee into a small swarm of fireflies.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 Violinist Over-Shoulder Shot
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10080.jpg" width="480" alt="SD2_10080"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/violinist-over-shoulder-SD2_10080">🌐 Watch Online</a>

#### 📝 Prompt
```
Change the camera angle to be over the violinist’s shoulder.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 Making the Violin Invisible
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10079.jpg" width="480" alt="SD2_10079"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/invisible-violin-SD2_10079">🌐 Watch Online</a>

#### 📝 Prompt
```
Make the violin invisible
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 Violinist Image Environment Transport
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10078.jpg" width="480" alt="SD2_10078"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/violinist-image-transport-SD2_10078">🌐 Watch Online</a>

#### 📝 Prompt
```
Transport the violinist to the image environment
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.0s`

---

### 🎬 Armored Heroine Soars Above Golden Clouds
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10077.jpg" width="480" alt="SD2_10077"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/armored-heroine-golden-clouds-SD2_10077">🌐 Watch Online</a>

#### 📝 Prompt
```
Shot 1 (8 seconds) shows a strong female character. Cinematic wide-angle shots, she soars above golden sea of clouds, the warm orange glow of the sunset illuminating the mist, creating a spectacular and dramatic scene. The wind brushes her hair and clothes, creating a strong sense of physical realism. Futuristic, streamlined mechanical armor components came from all directions—breastplates, shoulder armor, arm armor, leg armor, and a glowing helmet—flying in at high speed, trailing vivid light trails and cyan engine exhaust. Every part is...
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 Red Dragon Storm Fury
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10076.jpg" width="480" alt="SD2_10076"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/red-dragon-storm-fury-SD2_10076">🌐 Watch Online</a>

#### 📝 Prompt
```
A raging red dragon (elemental) soared from the sea, swirling and dancing above the ship at incredible speed, stirring up massive waves. Dynamic footage follows the dragon through the storm, tumbling and receding in the waves.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 Ramadan Paper Cut Zoom Lapse
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10075.jpg" width="480" alt="SD2_10075"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ramadan-paper-cut-zoom-lapse-SD2_10075">🌐 Watch Online</a>

#### 📝 Prompt
```
Through highly detailed paper-cutting art and seamless infinite zoom ultra-lapse photography, capture the journey from Ramadan to Eid celebrations. The scene begins during the fasting meal, when a bright crescent moon hangs above the tranquil street, with soft lantern light flickering. The camera zooms in to a window, showing a family preparing a fast-ending meal, then smoothly transitioning into the fast-paced daily fasting moment—ultra-lapse photography—people working, praying, and waiting for the break of the fast. The camera zooms in, and at sunset, the streets are packed with street vendors and crowds...
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 Office Dragon Fires Employee
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10074.jpg" width="480" alt="SD2_10074"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/office-dragon-fires-employee-SD2_10074">🌐 Watch Online</a>

#### 📝 Prompt
```
Quick editing: An ultra-realistic "office dragon" flies through multiple office rooms, weaving through crowds, over desks, around people, in a busy cubicle office. It landed on a table in front of a man, spraying flames at the man. The dragon said, "You were fired." ”
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 Global Female Armor Transformations
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10073.jpg" width="480" alt="SD2_10073"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/global-female-armor-transformations-SD2_10073">🌐 Watch Online</a>

#### 📝 Prompt
```
Core scene prompt @94d74b42-17ec-45d3-ab60-487c3a1700cb Complete 10 sets of global female armor transformations within 12 seconds. No glasses throughout, full armor helmet + weapon, pure female general look. All transitions include glowing particle effects. The style is unified as high-end, realistic, and impactful. Scenes by time period: 0-1 second: Chinese red-gold bright armor + gilded battle helmet, wielding a gilded spear, lifting...
```

#### 📌 Details
- Ratio: `0.56` | Duration: `5.04s`

---

### 🎬 Vibrant Orange Soda Splash
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10072.jpg" width="480" alt="SD2_10072"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/orange-soda-splash-SD2_10072">🌐 Watch Online</a>

#### 📝 Prompt
```
A vibrant orange soda can surrounded by splashing citrus slices and sparkling water droplets, presented in slow motion, with bright and vibrant lighting and high-detail commercial photography.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 Giant Cat Invades Chongqing
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10070.jpg" width="480" alt="SD2_10070"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/giant-cat-chongqing-SD2_10070">🌐 Watch Online</a>

#### 📝 Prompt
```
[Style] Mockumentary, mobile vlog perspective, surreal CG combined with real scenes, 8K quality, perfect physical simulation of hair. [Duration] 15 seconds [Scene] Chongqing Hongyadong or busy interchange intersections (with magical 8D). Urban feel). [00:00-00:05] Shot 1: Visual Spectacle (Reveal). The footage shows a bustling city street. The camera lifts to show a white tabby cat the size of **Godzilla...
```

#### 📌 Details
- Ratio: `0.56` | Duration: `5.04s`

---

### 🎬 Armored Baboon Destroys Marseille Village
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10069.jpg" width="480" alt="SD2_10069"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/armored-baboon-marseille-village-SD2_10069">🌐 Watch Online</a>

#### 📝 Prompt
```
A giant armored baboon charged through a burning Marseille village, grabbed a Marseille warrior, and threw him into a burning hut. The Marseille soldiers scattered in terror amid the sea of fire and ruins.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 Cozy Hollow at Golden Dusk
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10068.jpg" width="480" alt="SD2_10068"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cozy-hollow-golden-dusk-SD2_10068">🌐 Watch Online</a>

#### 📝 Prompt
```
Format: 15 seconds / 6 shots / Heartwarming forest comedy / Short dialogues Style: Surreal, cinematic forest animation; warm golden sunset rays stream through cracks in tree bark, moss grows inside tree hollows, creating a cozy and comfortable atmosphere.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

<!-- STATS_END -->
