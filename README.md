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
- Total Prompts: **2735**
- Updated Today (UTC 2026-05-11): **243**

## 🎬 Today's Updates
### 🎬 ID: SD2_02754
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02754.jpg" width="480" alt="SD2_02754">

- **Prompt**: Create a high-quality 4K cinematic basketball storyboard showing a full sequence from defense to a powerful score, using dynamic arena lighting, dramatic crowd atmosphere, and professional sports broadcast style. The scene begins with an intense h...
- **Specs**: Ratio: `1.33` | Duration: `15.07s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02754.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02754)

---

### 🎬 ID: SD2_02753
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02753.jpg" width="480" alt="SD2_02753">

- **Prompt**: Base Setup: “Ultra-realistic fast-paced TikTok-style beauty ad inside a luxury cosmetics store. Bright lighting, glossy reflections, trendy aesthetic. A stylish Korean girl with glowing skin and modern outfit. Fast cuts, dynamic camera movement, v...
- **Specs**: Ratio: `1.78` | Duration: `15.2s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02753.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02753)

---

### 🎬 ID: SD2_02752
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02752.jpg" width="480" alt="SD2_02752">

- **Prompt**: Ultra-realistic cinematic action, grounded physics, IMAX film look, 4K–8K HDR, high contrast, deep shadows, natural skin texture, subtle film grain, anamorphic lens 35mm (f/2.8). No over-glow, no excessive aura. Energy as air pressure distortion +...
- **Specs**: Ratio: `2.34` | Duration: `15.13s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02752.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02752)

---

### 🎬 ID: SD2_02751
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02751.jpg" width="480" alt="SD2_02751">

- **Prompt**: A cinematic, fast-paced action sequence starting with a close-up of a fierce female warrior with dark hair and silver metallic facial markings, aiming a glowing blue energy bow and arrow. Transition to an extreme close-up of her brown eye as a fut...
- **Specs**: Ratio: `1.78` | Duration: `15.23s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02751.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02751)

---

### 🎬 ID: SD2_02750
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02750.jpg" width="480" alt="SD2_02750">

- **Prompt**: Create a hyper-realistic, cinematic 15-second continuous sequence depicting a WWE-style championship finale between two highly athletic Japanese female wrestlers in a packed arena. Follow a precise match progression: fatigued staredown → explosive...
- **Specs**: Ratio: `1.78` | Duration: `15.13s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02750.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02750)

---

### 🎬 ID: SD2_02749
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02749.jpg" width="480" alt="SD2_02749">

- **Prompt**: Seedance 2.0 – 15 Beauty Cream Advertisement Video Prompt Create a 15-second vertical (9:16) ultra-realistic cinematic advertisement video for a beauty cream. Scene: A young woman in a clean, modern vanity or soft studio bathroom setting. The envi...
- **Specs**: Ratio: `1.78` | Duration: `15.05s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02749.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02749)

---

### 🎬 ID: SD2_02748
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02748.jpg" width="480" alt="SD2_02748">

- **Prompt**: Create a 15-second cinematic short video with a unique emotional storyline. Scene starts inside a softly lit modern grocery store. A young woman (mid-20s, natural look, casual outfit) walks slowly through the aisles, picking up everyday items like...
- **Specs**: Ratio: `1.78` | Duration: `15.17s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02748.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02748)

---

### 🎬 ID: SD2_02747
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02747.jpg" width="480" alt="SD2_02747">

- **Prompt**: Create a cinematic fantasy movie sequence based on this 16-panel storyboard poster. A young royal princess is performing an elegant ballroom dance inside a luxurious European palace ballroom at night. Warm golden chandelier light and candlelight g...
- **Specs**: Ratio: `0.56` | Duration: `9.65s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02747.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02747)

---

### 🎬 ID: SD2_02746
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02746.jpg" width="480" alt="SD2_02746">

- **Prompt**: Style: Cinematic thriller, handheld camera energy, high contrast lighting, teal-orange grading, shallow depth of field, fast rhythmic cuts, realistic motion blur. 0–2s — The Heist Breaks Loose Interior bank vault corridor. Red alarm lights flashin...
- **Specs**: Ratio: `1.78` | Duration: `14.1s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02746.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02746)

---

### 🎬 ID: SD2_02745
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02745.jpg" width="480" alt="SD2_02745">

- **Prompt**: 0–3s (VIRAL HOOK): Extreme macro close-up of a gourmet cheeseburger being lifted slowly. Melted cheese stretches dramatically between bun and patty—thick, glossy, elastic strands. Juices glisten on the patty, steam rises naturally. Slow-motion eff...
- **Specs**: Ratio: `1.78` | Duration: `11.73s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02745.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02745)

---

### 🎬 ID: SD2_02744
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02744.jpg" width="480" alt="SD2_02744">

- **Prompt**: Read IMG_1 as the sole main character reference. Read IMG_2 as an abstract storyboard reference. The faceless mannequins in IMG_2 are not characters but symbols indicating position, pose, and composition.
- **Specs**: Ratio: `1.78` | Duration: `15.08s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02744.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02744)

---

### 🎬 ID: SD2_02743
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02743.jpg" width="480" alt="SD2_02743">

- **Prompt**: Style: Cinematic samurai drama, ultra-realistic, muted color palette, natural dusk lighting, slow-motion emphasis, wind-swept atmosphere, shallow depth of field, minimal dialogue, emotional tension, Kurosawa-inspired framing. 0–3s — Silent Approac...
- **Specs**: Ratio: `1.78` | Duration: `15.07s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02743.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02743)

---

### 🎬 ID: SD2_02742
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02742.jpg" width="480" alt="SD2_02742">

- **Prompt**: A packed city bus tears through rainy streets at night. Suddenly the entire floor dents upward beneath passengers’ feet with a metallic BOOM. People scream as scraping sounds race underneath the bus at impossible speed. Sparks blast past the windo...
- **Specs**: Ratio: `1.0` | Duration: `12.17s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02742.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02742)

---

### 🎬 ID: SD2_02741
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02741.jpg" width="480" alt="SD2_02741">

- **Prompt**: A vast ancient forest, towering trees thousands of years old, their bark carved with glowing runes, mist curling through the roots like living creatures. Dead silence. Then — a crack of golden light splits the sky. Thick storm clouds part and a bl...
- **Specs**: Ratio: `0.75` | Duration: `15.21s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02741.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02741)

---

### 🎬 ID: SD2_02740
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02740.jpg" width="480" alt="SD2_02740">

- **Prompt**: 0–4s Soft morning light spills over Venice. A young girl steps out of a narrow alley wearing a pastel cotton floral dress, light and breathable, flowing gently with every step. The canals shimmer as gondolas pass quietly in the background. 4–8s Sh...
- **Specs**: Ratio: `1.78` | Duration: `15.17s`
- **Links**: [🎬 Watch Video](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/videos/SD2_02740.mp4) | [🌐 View on Prompt Hub](https://prompthub.gokuscraper.com/?q=SD2_02740)

---

<!-- STATS_END -->
