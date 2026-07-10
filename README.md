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
- Total Prompts: **7491**
- Updated Today (UTC 2026-07-10): **34**

## 🎬 Today's Updates
### 🎬 Pyramid Builders Uncut
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07694.jpg" width="480" alt="SD2_07694"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pyramid-builders-uncut-SD2_07694">🌐 Watch Online</a>

#### 📝 Prompt
```
This is handheld documentary footage recorded on an early-2000s consumer DV camcorder at the construction site of the Great Pyramid of Giza. The footage feels like real, imperfect documentation of one of the largest building projects in history. The recording shows hundreds of workers moving massive stone blocks on a large construction ramp. Teams of men are pulling ropes attached to sledges with heavy limestone blocks. Overseers with sticks walk along the lines giving orders. Dust fills the air. In the background, the partially built pyramid rises against the sky. The work is extremely physical and organized. The camera moves along one of the work gangs, following a team of workers as they pull a large block up the ramp. It occasionally tilts up to show the height of the structure. There are natural cuts between different groups of workers and close views of the ropes straining and the stone moving slowly. The movement of the camera feels like someone walking among the workers documenting the labor. The handheld camera shows constant shake, drifting framing, autofocus hunting in the bright sunlight and dust, exposure changes, motion blur, and the typical look of filming heavy physical work with an old DV camcorder. The person filming is clearly moving through the active construction site. Natural sound only: the sound of hundreds of men shouting and grunting in rhythm, ropes creaking under tension, stones scraping on the ground, and general noise of a massive construction site. No music. The result must feel like authentic, raw footage of the construction of the Great Pyramid, captured on an old camcorder.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Liquid Gold Awakening
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07693.jpg" width="480" alt="SD2_07693"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/liquid-gold-awakening-SD2_07693">🌐 Watch Online</a>

#### 📝 Prompt
```
00:00–00:02 CONTACT. Slow push toward the vessel through dust-lit golden light. The entity presses a half-formed face to the glass, studying her. She reaches out, almost to herself, in a soft British accent: MIRA: "...what are you?" She touches the glass. Cracks bloom instantly; the vessel breaks open, liquid gold pouring outward, catching the sunlight as it moves. 00:02–00:05 RESISTANCE. Handheld, close, controlled. The liquid gold coils around her wrists and throat from the fingertips inward, leaving faint trailing threads of light that dissolve within a second. She staggers back, still speaking through the struggle, not screaming: MIRA: "No— wait—" It climbs her jaw and enters through her eyes and lips; warm gold veins spread visibly beneath her skin. 00:05–00:08 RECOGNITION. Extreme close-up. The metal continues its spread across her face, a remembering, not an invasion. Emerald holds steady in her eyes. Her breathing slows. Quietly, almost surprised at herself: MIRA: "...I know this." 00:08–00:11 EMERGENCE. Wide pull-back, slow orbit. Her hair unfurls into liquid gold, moving like warm honey caught in motion. Fine trailing light-threads follow her and fade behind her. The room's golden light gathers toward her. She lifts barely off the ground. 00:11–00:13 TRANSCENDENCE. Extreme close-up, centered. Full coverage completes a warm, gleaming gold-bronze surface. No blink. One corner of her mouth lifts. Pupils remain emerald. Softly, in the same calm British voice: MIRA: "...finally." 00:13–00:15 STILLNESS. Wide, still shot. Dust hangs gently in the golden light, calmer now than before, as though something has resolved rather than broken. She stands alone, at peace, glowing warmly in the last of the sunlight. Hold. Fade not cut to warm white light, then to black.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.12s`

---

### 🎬 Asian Couture Cultural Journey
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07692.jpg" width="480" alt="SD2_07692"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/asian-couture-cultural-journey-SD2_07692">🌐 Watch Online</a>

#### 📝 Prompt
```
Ultra-cinematic luxury fashion campaign featuring the same female influencer from the reference image. Studio-shot aesthetic with a seamless white infinity backdrop transformed through lighting, projections, and visual effects. Seamlessly change Music according to culture. Hyper-realistic skin texture, consistent facial identity, premium beauty lighting, 8K, high-fashion editorial style. Scene 1 (0:00–0:02.5) — China The influencer wears a modern red-and-gold hanfu-inspired couture outfit. Soft red lighting and floating golden calligraphy particles surround her. She slowly turns toward the camera as traditional Chinese strings blend with cinematic bass. Smooth orbit shot. Transition: Flowing sleeve creates a silk wipe. Scene 2 (0:02.5–0:05) — South Korea She transforms into a contemporary hanbok with elegant embroidery and flowing fabrics. Soft pink and white lighting with floating cherry blossoms. Korean orchestral-pop fusion soundtrack. Dramatic push-in shot. Transition: Cherry blossoms fill the frame. Scene 3 (0:05–0:07.5) — Thailand She appears in a luxurious Thai royal-inspired outfit with gold accessories and silk textures. Golden temple projections illuminate the studio. Traditional Thai instruments blend with electronic beats. Cinematic orbit shot. Transition: Golden particles burst into light. Scene 4 (0:07.5–0:10) — India She transforms into a luxury lehenga with intricate embroidery and jewelry. Rich saffron and emerald lighting fill the studio. Tabla and orchestral music accompany dramatic fabric movement as she walks toward the camera in slow motion. Transition: Flowing fabric sweeps across the lens. Scene 5 (0:10–0:12.5) — Japan She appears in a modern couture kimono with elegant patterns. The studio transforms with neon-inspired Japanese aesthetics and floating sakura petals. Traditional Japanese instruments merge with cinematic electronic music. Smooth rotating camera. Transition: Neon light streaks sweep across the frame. Scene 6 (0:12.5–0:15) — Saudi Arabia She transforms into contemporary Saudi-inspired haute couture with luxurious black-and-gold fabrics, intricate embroidery, and premium jewelry. The studio becomes a cinematic desert-inspired environment with flowing sand particles, amber lighting, and subtle geometric Arabic projections. Traditional Middle Eastern instruments blend with cinematic electronic music. Smooth crane shot. Final on-screen text: "Every culture tells a story."
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 Blonde Idol Cute Kpop Dance
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07691.jpg" width="480" alt="SD2_07691"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/blonde-idol-kpop-dance-SD2_07691">🌐 Watch Online</a>

#### 📝 Prompt
```
참조 이미지(첨부한 금발 한국 아이돌 캐릭터 시트)의 인물을 주인공으로 사용. 24fps. ★실사 — 포토리얼리스틱한 실제 한국 여성 영상. 애니메이션·일러스트화 절대 금지. 뮤직비디오급 고화질, 생동감 있는 촬영. 버즈될 만한, 귀여움 강한 짧은 댄스 영상. 주인공은 참조 이미지의 인물 본인 — 밝은 금발 장발, 눈매, 얼굴 생김새, 체형, 나이감, 의상 인상(홍대 힙 스트릿), 전체 분위기를 그대로 유지. 별인·별캐릭터화 금지. 배경은 밝고 깨끗하며 귀엽게 정돈된 스튜디오 또는 교실풍 공간(트렌디한 서울 감성). 인물이 주역으로 보이도록 배경은 심플하되 팝하고 상큼한 공기감. 【음악】 영어 가사의 밝고 통통 튀는 K-pop풍 곡. 단, 실존하는 곡은 사용 금지. 【영상 컨셉】 주인공이 귀여운 댄스를 춘다. 귀여움 최우선. 살짝 애교스럽고 친근하게, 카메라를 향해 춤추는 느낌을 강하게. AE(애프터이펙트)로 만든 듯한 2D 플랫 애니메이션이 춤 동작에 맞춰 등장. 이펙트는 크레용·오일파스텔로 그린 듯한 손그림 감성의 귀여운 일러스트 — 원, 별, 하트, 꽃, 음표, 화살표, 리본, 왕관, 반짝이, 물결선, 뱅글뱅글 선, 말풍선 테두리, 체크무늬, 사선, 하프톤 도트 등. 전부 평면 2D. 배색은 핑크·하늘색·노랑·흰색·라벤더·민트그린 중심으로, 주인공과 어울리는 귀여운 색. 【카메라 구성】 5대 카메라로 찍는 듯한 구성. 고정이 아니라 2초마다 카메라 전환. 사용 카메라: 정면·위에서·왼쪽·오른쪽·뒤에서. 카메라가 바뀌어도 주인공은 항상 렌즈를 의식하고 카메라 응시 유지. 정면 외 카메라에서도 얼굴 방향·목 비틀기·시선 처리로 반드시 렌즈를 본다. 뒤 카메라일 땐 어깨 너머로 돌아보며 카메라 응시. 화각 변화 있고 템포 좋은 카메라워크. 각 카메라는 완전 정지가 아니라 비트에 맞춰 가볍게 흔들림 — 위아래 작은 바운스, 짧은 펀치인, 살짝 좌우 흔들림 등 음악에 맞춘 귀여운 카메라 셰이크. 지저분한 흔들림이 아니라 의도적이고 보기 좋은 흔들림. 【댄스 내용】 귀엽고 따라하기 쉬운 안무. 좌우로 가볍게 스텝, 가슴 앞 양손 하트, 한손 하트, 볼 옆 브이, 양손을 볼 옆에서 살포시 펼치기, 손가락 가리키기, 어깨 작게 튕기기, 허리 좌우로 가볍게, 한 발 내밀었다 되돌리기, 작은 턴, 마지막에 윙크. 상반신 볼거리 많게, 짧지만 인상에 남는 안무. 춤추는 동안 항상 카메라 응시. 【15초 타임라인】 0.0~2.0초 : 정면 카메라. 중앙에 서서 리듬 타며 가슴 앞 양손 하트, 좌우 작은 스텝. 카메라 위아래 가볍게 바운스. 손·얼굴 주변에 크레용 하트·별·원·짧은 반짝이 선이 통통 등장. 항상 정면 응시. 2.0~4.0초 : 위에서 카메라. 살짝 부감의 귀여운 앵글. 올려다보듯 카메라 응시하며 볼 옆 브이·한손 하트·손가락 가리키기를 템포 좋게. 얼굴 주위에 왕관·꽃·하트·말풍선 테두리 등장. 4.0~6.0초 : 왼쪽 카메라. 몸은 살짝 왼쪽, 얼굴·시선은 렌즈로. 허리 좌우로 가볍게, 한 손 볼에 대고 다른 손으로 작게 흔들기. 손 궤적 따라 크레용 리본 라인·음표·물결선·별 등장. 카메라 비트에 맞춰 작게 좌우 흔들. 6.0~8.0초 : 오른쪽 카메라. 반대쪽으로 몸 돌리며 카메라 응시 유지. 어깨 리드미컬하게 튕기고 양손 올렸다 내리고 한 발 가볍게 내밀었다 되돌리기. 발밑·어깨 주위에 꽃·원·체크·하프톤 도트·반짝이 팡팡. 짧은 펀치인. 8.0~10.0초 : 뒤에서 카메라. 등 쪽에서 시작하지만 어깨 너머로 휙 돌아봐 확실히 카메라 응시. 작은 턴 넣으며 돌아보는 찰나 손가락 가리키기·하트·가벼운 투척 키스 제스처. 머리·의상 움직임에 맞춰 뱅글선·별·리본·하트 살포시 등장. 10.0~12.0초 : 정면 복귀(사비 절정). 양손 크게 펼쳤다 가슴으로 모으고 좌우로 통통 작게 점프. 화면 좌우·뒤에 큼직한 하트·별·꽃·왕관·반짝이·사선 늘어 귀여움 최대화. 결정 때마다 짧은 카메라 셰이크. 12.0~14.0초 : 위에서 카메라 재전환. 올려다보며 얼굴 앞에서 양손 살포시 펼치고 한손 하트, 다른 손 볼 옆. 크레용 테두리·하트·꽃·체크·러프한 원형 라인 배경에 퍼짐. 항상 카메라 응시. 14.0~15.0초 : 정면 히어로샷. 바스트업으로 살짝 앞으로 나오듯. 방긋 웃고 마지막에 윙크. 윙크 순간 눈가에서 크레용 사각별·하트·방사선·리본 라인 팡. 카메라 아주 짧게 펀치인 후 정지, 버즈될 결정 컷으로 끝. 【AE풍 2D 이펙트 연출】 모든 이펙트는 AE로 만든 듯한 2D 플랫 애니메이션. 단 질감은 크레용·오일파스텔로 그린 러프하고 귀여운 손그림 감성. 동작은 출현·바운스·확대·축소·회전·시차·부드러운 사라짐. 이펙트는 손·얼굴·발밑·몸 움직임과 동기화해 등장. 인물 얼굴·몸을 과하게 가리지 말고, 어디까지나 귀여움과 템포를 강화하는 보조로. 【제약】 주인공 외 인물 금지. 참조 캐릭터의 분위기·얼굴·헤어(금발 장발)·눈·체형·나이감·의상 유지. 별캐릭터화 금지. 의상 임의 변경 금지. 5대 카메라 구성 명확, 2초마다 전환. 정면·위·왼·오른·뒤 반드시 사용. 어느 카메라든 주인공은 항상 카메라 응시. 뒤 카메라도 어깨 너머로 돌아봐 렌즈 응시. 이펙트는 크레용 손그림 감성의 귀여운 2D. 실사적 폭발·불·연기·과한 글리치 금지. 얼굴을 이펙트로 과하게 가리지 말기. ★실사 실제 인물 유지 — 애니메이션·일러스트화 금지. 문자·자막·로고·워터마크 표시 금지.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.15s`

---

### 🎬 Tabby Cat DV Diary
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07690.jpg" width="480" alt="SD2_07690"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/tabby-cat-dv-diary-SD2_07690">🌐 Watch Online</a>

#### 📝 Prompt
```
Main subject: Realistic orange tabby house cat, young adult, sleek athletic build, soft orange fur with white chest and paws, bright green eyes, small black collar with a tiny camera mounted at chest level creating an authentic cat POV perspective. Curious, playful, energetic personality with natural feline behavior. Maintain consistent appearance, fur pattern, collar, and body proportions throughout the entire video. Location: Cozy suburban family home during a peaceful late morning. Sunlit living room, wooden floors, narrow hallway, modern kitchen, staircase, sunny windowsills, backyard garden with flowers and birds, quiet residential surroundings. No commercial locations or crowds. Visual Style: Ultra-realistic documentary realism. Genuine everyday pet behavior. Natural feline movement. Unscripted slice-of-life feeling. Strong environmental authenticity. Rich household details and believable animal motion. Camera Style: Early-2000s consumer DV camcorder aesthetic combined with a lightweight pet-mounted camera. Heavy bouncing from walking and running, rapid head turns, imperfect framing, frequent autofocus hunting, exposure pumping between indoor shadows and bright sunlight, occasional motion blur, subtle rolling shutter, mild digital compression artifacts, faded colors, soft contrast, slight sensor noise. No stabilization. No cinematic camera moves. No modern color grading. 00:00–00:02 The cat wakes up on a sunny windowsill, stretches lazily, jumps onto the wooden floor, and looks toward the kitchen after hearing food being prepared. The camera wobbles naturally with every movement. 00:02–00:04 The cat trots through the hallway, weaving between a person’s legs before reaching its food bowl. The camera briefly loses focus as sunlight pours through an open doorway. 00:04–00:06 After eating, the cat notices a feather toy sliding across the living room. It sprints after it, leaps onto the sofa, and lands clumsily. Motion blur increases during the fast chase. 00:06–00:08 The back door opens. The cat runs into the garden, chases butterflies through flowers, pauses to watch birds on a fence, and sniffs the grass. Leaves move gently in the breeze. 00:08–00:10 The cat spots another neighborhood cat beyond the fence. They quietly stare at each other for a few seconds before the visitor calmly walks away. The camera tilts curiously while following. 00:10–00:12 The cat returns inside, jumps onto a table beside a person drinking coffee, rubs affectionately against their arm, and receives gentle head scratches. Autofocus shifts between the person’s hand and the cat. 00:12–00:15 The cat curls up on a soft blanket near a sunny window, begins purring, slowly closes its eyes, and falls asleep. The recording ends abruptly mid-purr as if the old camcorder was switched off. Audio: Natural ambient sound only — soft purring, meows, paws tapping on wooden floors, birds chirping, rustling l
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

### 🎬 Dad's Pickup Line Backfires
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07688.jpg" width="480" alt="SD2_07688"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dads-pickup-line-backfires-SD2_07688">🌐 Watch Online</a>

#### 📝 Prompt
```
[STYLE + CAMERA + ATMOSPHERE] Authentic 1985 American sitcom shot on studio video cameras, warm tungsten lighting, live-audience energy. Soft VHS texture: gentle scan lines, slight chroma bleed, halation on the disco ball. Two sets: a wood-paneled 1985 living room, and a gymnasium prom with streamers, balloons, a disco ball and a punch bowl table, all decorations generic with no text. Palette: powder blue, dusty rose, mustard yellow, wood-brown, cream, deep teal. [CHARACTERS] No reference images. Create original, locked and consistent throughout: 1. THE DAD: late 40s, thick mustache, brown cardigan over a plaid shirt, warm overconfident sitcom-dad energy. At the prom he wears a chaperone's suit and stands at the punch bowl. 2. THE SON: a young man, feathered hair, powder-blue tuxedo with a ruffled shirt, sweet and terminally nervous. 3. THE GIRL: a young woman, curly dark hair with a ribbon, pink taffeta prom dress, kind eyes, quick to laugh. [AUDIO] Original 80s slow-dance synth ballad in the gym, do not use any real existing songs. Canned laugh track after every gag, audience "awww" before the applause. All dialogue spoken in English. SFX: punch ladle clink, gym-hall reverb, camera-flash pop. 0-2s: [Static wide, living room] The dad adjusts his son's bowtie, hands on his shoulders: "Son, tonight's the night. One line. It never fails." 2-4s: [Punch-in on the dad] Dead serious, he delivers it: "Did it hurt... when you fell from heaven?" and winks. Laugh track. The son nods, mouthing the words like homework. 4-6s: [Whip pan to the gym] Prom in full swing under the disco ball. The son spots the girl across the dance floor, the crowd parting around her in soft focus. 6-8s: [Side tracking shot] He crosses the gym rehearsing under his breath: "fell from heaven, fell from heaven..." Behind him, the dad chaperones at the punch bowl, giving a big thumbs-up. Laugh track ripples. 8-11s: [Static two-shot] He opens his mouth and panics: "Did it hurt... when you fell?" She glances down at her shoes, confused: "When I what?" He doubles down: "From... the ceiling?" Huge laugh track hit. 11-13s: [Punch-in on the dad] At the punch bowl, the dad slowly slaps his forehead and drags the hand down his whole face, shaking his head. Biggest laugh of the night. 13-15s: [Slow push-in on the couple] She bursts out laughing and pulls him toward the dance floor anyway. In the background the dad's facepalm melts into a proud little nod. Freeze frame, audience "awww" into applause, music cuts instantly. NEGATIVE: No text, subtitles, logos or watermarks. No text on banners, sashes or decorations. No brand names on clothing. No real songs or real people. No modern color grading, no cinematic glamour, no character drift, no extra featu
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Korean Morning Glow Routine
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07686.jpg" width="480" alt="SD2_07686"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-morning-glow-routine-SD2_07686">🌐 Watch Online</a>

#### 📝 Prompt
```
Create a realistic GRWM (Get Ready With Me) lifestyle video featuring a stylish Korean woman with long silky black hair, radiant skin, and a fresh natural look. Bright modern apartment with floor-to-ceiling windows, warm morning sunlight, cozy Scandinavian décor, premium lifestyle vlog aesthetic, cinematic handheld camera, ultra-realistic photography. The video opens with her stepping out of the bathroom wrapped in a clean white bath towel, gently drying her damp hair while smiling softly. Warm morning sunlight streams through the apartment, creating a calm and refreshing atmosphere. As she walks into the living room, her golden retriever excitedly runs toward her. She kneels down to cuddle the dog, scratches behind its ears, rubs its belly, and throws its favorite toy across the room. The dog happily brings it back, and they share a playful moment full of laughter. She prepares a fresh bowl of food and water for her dog before giving it a small treat and one last cuddle. Next, she heads to her vanity and begins a refreshing skincare routine using cleanser, toner, serum, moisturizer, eye cream, and lip balm. Cinematic beauty close-ups capture her naturally glowing skin under warm sunlight. She blow-dries her hair, styles it into soft loose waves, then applies light everyday makeup including foundation, blush, mascara, soft eyeliner, and a glossy lip tint. Walking to her wardrobe, she browses several outfits before choosing a fitted white crop top with high-waisted blue jeans. She changes into the outfit, adjusts the fit, and completes the look with gold hoop earrings, a delicate necklace, a bracelet, sunglasses, and a light spray of perfume. She slips on white sneakers, picks up her handbag, phone, and iced coffee before standing in front of a full-length mirror. She smiles, spins once, fixes a strand of hair, and captures a quick mirror selfie. Before leaving, she kneels down to hug her dog one last time, places another treat into its bowl, waves goodbye, and opens the apartment door. The camera follows her walking confidently through a peaceful tree-lined neighborhood as the morning sun lights the streets. She sips her iced coffee, smiles toward the camera, and continues her day while the camera slowly pulls back for a cinematic ending. Style: premium GRWM fashion vlog, realistic lifestyle storytelling, cozy apartment aesthetic, pet-friendly morning routine, cinematic handheld and gimbal camera movement, elegant transitions, warm natural lighting, shallow depth of field, photorealistic, luxury social media content, 4K HDR, 16:9 widescreen, no subtitles, no text overlays.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.08s`

---

### 🎬 Lightspeed Frozen City Runner
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07684.jpg" width="480" alt="SD2_07684"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/lightspeed-frozen-city-runner-SD2_07684">🌐 Watch Online</a>

#### 📝 Prompt
```
LIGHTSPEED — 15 second premium cinematic high-energy short film, 10 scenes, a runner moving so fast that the world around him freezes in time, weaving through a frozen city at impossible speed. Shot on ARRI Alexa 35, Panavision anamorphic 35mm lens, natural film
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 Confident Smile Wins Interview
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07683.jpg" width="480" alt="SD2_07683"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/confident-smile-interview-SD2_07683">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: Ultra-realistic cinematic commercial, modern corporate office, premium lighting, dramatic slow motion, shallow depth of field, 4K HDR. 0–4s: A young professional stands outside the interview room, holding his resume. He hears muffled voices inside as his name is called. He takes a deep breath, but his nervous expression reveals his lack of confidence. 4–7s: He reaches into his bag, takes out a tube of toothpaste, quickly brushes his teeth in the office restroom, rinses, and looks into the mirror. He flashes a bright, confident smile. The lighting subtly shifts as his confidence grows. 7–12s: He walks confidently into the interview room. Every handshake is firm, every answer is delivered with calm assurance. The interview panel exchanges impressed glances. Time slows as he smiles naturally, radiating confidence. 12–15s: The interviewer stands, smiles, and shakes his hand. "Welcome to the team." He leaves the office with a confident grin. The toothpaste appears in a clean product shot as the voice-over says: "A confident smile opens more than doors." Fade to the brand logo and tagline: "Start every opportunity with confidence."
```

#### 📌 Details
- Ratio: `1.77` | Duration: `14.53s`

---

### 🎬 Storm Rider Vision
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07682.jpg" width="480" alt="SD2_07682"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/storm-rider-vision-SD2_07682">🌐 Watch Online</a>

#### 📝 Prompt
```
0–4s: A lone biker races across endless desert dunes on a powerful black motorcycle. Behind him, a group of rival riders closes in while a massive sandstorm rapidly approaches. Sand blasts into his face, making it nearly impossible to see. His bike begins to lose control as visibility drops to almost zero. 4–7s: The biker skids to one side, reaches into his leather jacket, and pulls out a pair of sleek black sunglasses. He calmly puts them on. The moment the lenses cover his eyes, the roaring sandstorm transforms into perfect clarity. Every dune, rock, and obstacle becomes crystal clear while the rivals continue struggling blindly. 7–12s: With absolute confidence, he twists the throttle. The motorcycle explodes forward at incredible speed. He drifts across towering dunes, jumps over rocky cliffs, weaves effortlessly between obstacles, and overtakes every rival in breathtaking slow motion. Sand trails erupt behind him as cinematic music reaches its peak. 12–15s: The biker reaches the finish line alone as the sandstorm fades behind him. He removes his helmet, adjusts the sunglasses with a confident smile, and looks toward the horizon. A dramatic close-up showcases the sunglasses as a deep voice-over says: "See beyond the storm." Fade to the brand logo with the tagline: "Clear Vision. Limitless Confidence."
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.47s`

---

### 🎬 Dior Scent of Confidence
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07681.jpg" width="480" alt="SD2_07681"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dior-scent-confidence-SD2_07681">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: Ultra-realistic luxury commercial, cinematic, moody lighting, rain-soaked city, dramatic slow motion, premium color grading, 4K HDR. 0–4s: Midnight in a modern city. A sharply dressed man walks alone through rain-covered streets carrying a mysterious briefcase. Suddenly, four suited men step out from the shadows, surrounding him. Their leader smirks. The atmosphere is tense as thunder rumbles overhead. 4–7s: The man calmly loosens his tie, reaches into his coat pocket, and pulls out a sleek bottle of Dior Men's Perfume. He sprays it once onto his neck and wrists. Time seems to freeze. Raindrops hang in the air as the fragrance disperses in slow motion. 7–12s: His confidence transforms instantly. He moves with effortless precision, dodging every punch and disarming each attacker in a breathtaking sequence of elegant, fluid combat. His coat flows dramatically through the rain as every movement feels graceful and controlled. 12–15s: The attackers lie defeated. He adjusts his suit, picks up the briefcase, and walks away without looking back. The camera lingers on the Dior perfume bottle resting on a rain-soaked stone ledge. A deep voice-over says: "Confidence isn't worn. It's unforgettable." Fade to the Dior logo with the tagline: "Dior. The Scent of Confidence."
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.25s`

---

### 🎬 Sunscreen Confidence All Day Long
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07680.jpg" width="480" alt="SD2_07680"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sunscreen-confidence-all-day-SD2_07680">🌐 Watch Online</a>

#### 📝 Prompt
```
Style: Ultra-realistic influencer vlog, luxury lifestyle aesthetic, warm natural lighting, soft pastel tones, smooth handheld camera, cinematic transitions, 4K HDR. 0–3s – Morning Routine A young lifestyle influencer wakes up in a bright, minimalist bedroom. She opens the curtains, sunlight floods the room. In front of her vanity, she smiles at the camera while applying sunscreen as the first step of her skincare routine. Dialogue: "Every great day starts with protecting my skin." 3–6s – Coffee Run She walks through sunny city streets with an iced coffee, laughing with friends. The camera captures glowing skin under the sunlight. She briefly holds the sunscreen before slipping it into her tote bag. Dialogue: "Sunny days? I'm always ready." 6–9s – Midday Touch-Up While relaxing in a park after shopping, she reapplies sunscreen effortlessly. Friends continue chatting while she smiles naturally at the camera. Dialogue: "Reapplying is just part of the routine." 9–12s – Golden Hour She rides a bicycle along a scenic waterfront, hair flowing in the breeze. Close-up shots highlight her fresh, radiant complexion as the sun begins to set. Dialogue: "Healthy skin means confidence all day long." 12–15s – Evening Wrap-Up She watches the sunset from a rooftop café, smiling as she places the sunscreen beside her drink. The product fills the frame with a premium cinematic close-up. Dialogue: "Wherever the day takes me, my skin stays protected." Ending Shot: Luxury product close-up with elegant typography: "Protect Every Moment." ☀️
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.67s`

---

### 🎬 Dreamy Yellow Capsule in Rainforest
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07679.jpg" width="480" alt="SD2_07679"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dreamy-yellow-capsule-rainforest-SD2_07679">🌐 Watch Online</a>

#### 📝 Prompt
```
Use the uploaded image as the exact visual reference: a dreamy yellow capsule-shaped glass house in a lush rain-soaked forest garden, warm orange interior glow, mossy ground, pink flowers, reflective pond, soft mist, cinematic depth of field. Include one stylish young adult subject in a minimal cream outfit, moving calmly through the space. Scene 1: Wide aerial glide through tree branches and morning mist, slowly revealing the glowing yellow pod beside the pond. Scene 2: Low macro tracking shot skimming over wet moss, tiny flowers, droplets, and rippling water as the house reflects softly in the pond. Scene 3: Side dolly shot through the glass walls, revealing the subject seated in the lounge chair, quietly reading as warm light surrounds them. Scene 4: Close-up of the subject’s hand opening the glass door, raindrops sliding down the transparent panel in sharp focus. Scene 5: Slow orbit around the subject walking barefoot through the flowering garden, yellow architecture glowing behind them against deep green foliage. Scene 6: Interior shot from behind the pink floor lamp, framing the subject sitting on the coral sofa and looking out at the rain-soaked forest. Scene 7: Epic distant pullback from across the pond as the subject stands at the window, framed by the luminous capsule home, drifting mist, gentle rain, and a serene magical forest atmosphere.
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

### 🎬 Sony Headphones Turn the Battle
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07678.jpg" width="480" alt="SD2_07678"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sony-headphones-dance-battle-SD2_07678">🌐 Watch Online</a>

#### 📝 Prompt
```
0–4s: An underground street dance battle is reaching its climax. A young dancer struggles to keep up as his opponent delivers an incredible performance. The crowd erupts with cheers for the rival. Sweat drips from the dancer's face as he realizes he's losing. 4–7s: He calmly steps back, reaches into his backpack, and pulls out his sleek Sony Wireless Headphones. He places them over his ears. The outside noise instantly fades into silence. Then... the beat drops. Powerful bass pulses through the headphones as colorful sound waves ripple around him in cinematic slow motion. 7–12s: His confidence transforms instantly. Every beat guides his movement with perfect precision. He launches into an unbelievable dance routine—gravity-defying flips, flawless footwork, smooth spins, and impossible freezes. Neon lights pulse with the music as the stunned crowd watches in amazement. Even his opponent can't look away. 12–15s: The music stops. The entire crowd erupts in applause. The judges raise his hand in victory. He smiles, removes one side of the headphones, and the camera cuts to a premium close-up of the Sony Wireless Headphones. A deep voice-over says: "Hear every beat. Own every moment." Fade to the Sony logo with the tagline: "Sony. Sound That Moves You."
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.6s`

---

### 🎬 Moonlit Swordmaiden vs Cerberus
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07676.jpg" width="480" alt="SD2_07676"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/moonlit-swordmaiden-cerberus-SD2_07676">🌐 Watch Online</a>

#### 📝 Prompt
```
High-quality animation. A movie-level dark fantasy swordplay anime with a cinematic moonlit night. A high-density 2D hand-drawn anime battle scene where the character in the reference image battles a giant, three-headed black Cerberus that breathes otherworldly flames. Reference images prioritize the character's identity, face, eye shape, irise, contour, cheeks, chin, age, skin tone, hairstyle, hair color, bangs, costume, decorations, physique, silhouette, atmosphere, unique motifs, and character color. Refer to the characters in the reference images and maintain the same character throughout the entire story. Reference images are used only for character-specific designs and world-building. The background, rooms, furniture, text, UI, settings table, white background, pose, angle of view, camera distance, and framing of the reference image itself are not reproduced. The only things you can change are facial expressions, gazes, mouth, posture, breathing, and the natural swaying of your hair and costume during combat. Mixing features, average faces, altering people, changing hairstyles, changing hair color, changing costumes, changing body shapes, changing age, cloning, clones, and unnecessary characters are prohibited. [Automatic Adjustment for Reference Characters] The only fixed story structure is a moonlit flower field, a flame starting from a single central flower, Cerberus with three heads, a sword fight with a single Japanese sword, and just before the final clash. Background motifs such as plants, props, decorations, flame colors, moonlight, reflected light, smoke, ash, particles, butterflies, petals, crystals, sword decorations, and the overall tone and atmosphere of the screen naturally change according to the character colors, costume materials, decorations, unique motifs, personalities, and atmosphere of the reference image. For delicate characters, delicate flowers, soft light, transparent particles, light breezes, and elegant light trails. For cold characters, hard moonlight, frost, crystals, sharp reflections, and quiet air. For glamorous characters, luxurious flowers, jewel light, decorative particles, and vivid afterglow. For dark characters, black flowers, thick fog, soot, heavy shading, and restrained glow. For Japanese style, Japanese flowers, kumihimo, paper scraps, metal decorations. Mechanically, metal fragments, circuit-like light, sparks, and inorganic reflections. Motifs not present in the reference image are added irrelevantly; background art and effects are always derived from existing character elements. Colors are extracted from the reference character's main color, secondary color, and accent color, and distributed so that backgrounds and effects are less noticeable than the character. [Design] Fixing the design is the most important. Throughout, it maintains a dense 2D hand-drawn anime style based on reference images. Match the thickness, line color, eye rendering, hair strand texture, shadow shape, saturation, highlights, coloring, texture, and amount of information to the reference image. The line art is thin and delicate. The shadows are multi-layered, transparent and transparent. Hair, eyes, eyelashes, costume materials, embroidery, gemstones, metals, decorations, swords, flower beds, smoke, ash fragments, and more—all maintain a high level of information. Delicate key animation comparable to a theatrical film, high-quality composites, dense background art, and transparent lighting. Bold lines, thick outlines, simplified TV animation, low-density backgrounds, flat cel filling, smooth CG, 3D, semi-realistic, live-action textures, mixed art styles, and AI-like average faces are all prohibited. [Cerberus] A gigantic, three-headed black wolfdog-type magical beast. There are always three heads. Sharp fangs, glowing eyes, a burning mouth, a black muscular body, huge forelegs, long claws, hair around the neck flowing like flames, and a long black tail. The flames in the eyes, the mouth flames, the flames around the neck, and the afterglow of the nails harmonize with the accent colors of the reference characters. However, the main body is primarily black and not more ornate than the character. [Fixed Scene] Opening: A moonlit flower field. Flower types, colors, leaves, decorative plants, and ground texture should be matched to the reference character. Only the single flower in the center of the screen quietly lit a pale blue-white otherworldly flame reflecting the character's colors. The edges of the petals curl black, carbonization spreads from the center, and the flowers crumble into ash fragments. Ash and sparks touch the surrounding flowers, and the flames spread outward step by step from the center like circular, concentric ripples. Do not burn the entire flower field at once. The ignition point is only the single flower in the center. Instead of random ignition, it clearly shows the causal process propagating outward from the center. From the depths of the ring of ash and flame, Cerberus appeared, opening its three mouths and growling lowly. Cerberus's claws tear through the flower fields, scattering tiny particles reflecting sparks, soil, petals, ash, and the unique motifs of the reference characters. The character steps low from the side. Hair, costumes, decorations, hems, ribbons, and capes all maintain the structure of the reference image, flowing naturally with moonlight and speed. In this battle, only a single Japanese sword is used. Even if another weapon is depicted in the reference image, it is not added; in this scene, it is unified as a single Japanese sword. Only the sword's guard, hilt, scabbard, metal decorations, and reflected light are matched to the reference character's costume, decorations, and unique colors. Dual wielding, additional weapons, and spare swords are prohibited. Both hands grip only the handle behind the guard. The metal guard was clearly visible between the hand and the blade. He doesn't support the blade with his free hand. Hands, fingers, wrists, and forearms do not touch or overlap with the blade. Do not let the blade cross horizontally in front of the screen. The character deflects Cerberus's claws diagonally with a low center of gravity. Reflected light from the blade, particles derived from reference characters, petals, and ash fragments briefly cross the screen, creating a natural masking wipe. In the next moment, the character circles around Cerberus's side and switches diagonally upward from below in a continuous action animation where the weight shifts of waist, shoulders, knees, and legs are readable. Continuously delay the enemy's claws, blades, footwork, hair, costumes, and decorations to help understand the causality of offense and defense. Near the end, Cerberus's three heads growl low simultaneously and attack the character head-on. The character steps forward in a low defensive stance, aiming the lines of both eyes, nose, chin, chest, and shoulders toward the central head of Cerberus. Keep your gaze fixed on the enemy's glowing eyes, avoiding downward, off-screen, or camera gaze. He uses only a single Japanese sword, and grips only the hilt behind the tsuba with both hands. The tsuba clearly separates the hand from the blade. The blade is positioned diagonally forward, just before the contact between Cerberus's claws and fangs, forming a single line of attack and defense through the characters' gaze, the sword, and the enemy's fangs and claws. The story ends just before the character cuts and Cerberus attacks. Instead of a long still image, it ends with a brief slow-motion shot of flames, ash fragments, petals, hair, costumes, decorations, the afterglow of the sword, and Cerberus's claws moving continuously. [Sound] Ambient sound center. The flickering of otherworldly flames, the charred and crumbling of petals, the wind of ashes swirling, the low growl of Cerberus, the claws tearing the ground, the clear sound of a sword slicing through the air. No dialogue, no narration, no singing. [Prohibited] Text, subtitles, logos, watermarks, unnecessary people, costume swaps, hairstyle changes, hair color changes, altering people, clones, dual wielding, additional swords, reserve swords, additional weapons, gripping blades, hands supporting blades from below, close-up shots of hands overlapping blade, compositions of blades overlapping in front of face or head, gaze not looking at the enemy, striking a fixed pose with arms thrust straight upward, standing still, long static holds, simultaneous ignition of the entire flower field, random flames with unknown ignition point, It is forbidden for Cerberus to have two or more heads.
```

#### 📌 Details
- Ratio: `1.0` | Duration: `15.13s`

---

<!-- STATS_END -->
