[English](./README.MD) | [简体中文](./README_zh.md)

# 🎞️ Seedance-2-prompts-datasets

[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) [![Dataset Size](https://img.shields.io/badge/Size-12GB%2B-blue)](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets) [![Format](https://img.shields.io/badge/Format-JSONL%20%2F%20MP4-green)](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets)

> 🎞️ The ultimate Seedance-2 video prompt dataset (12GB+). 2000+ video generation prompts with full metadata and preview frames. Truly open source: No login, no ads, no redirection. Just pure data for AI video creators.

这个项目储存了海量字节跳动 Seedance 2.0 的提示词（Prompts）和由它们生成的预览视频。

整体数据集大小超过 **12GB**，包含 **2000+ 个视频及 Metadata**，且已进行完全结构化处理。由于 GitHub 不适合存储大批量文件，完整数据文件托管在 Hugging Face 平台上。在 Hugging Face 仓库中，主要包含了 **生成的视频（.mp4）**、**视频封面（.jpg）** 以及一个完全结构化并包含详细元数据的 **.jsonl 提示词文件**。

**下载完整数据集体验：**  
[https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets](https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets)

![huggingface](img/huggingface.jpg)

## 🌐 在线观看体验
无需登录，无广告，极速响应。  
👉 **[在线观看入口](https://prompthub.gokuscraper.com/)**

![website](img/website.jpg)

## 📖 项目介绍
**seedance-2-prompts-datasets** 由 **GokuOpenLab** 发起，是一个面向开发者与研究者的 Prompt 数据基础设施项目。

在当前 AI 生态中，Prompt 已经成为新的“生产力接口”，但现实情况往往是：
- Prompt 数据高度分散
- 缺乏统一结构标准
- 难以检索与批量复用
- 不适合工程化集成

本项目的目标不是“简单地展示 Prompt”，而是：
> 将互联网或生成社区中的 Prompt 转化为**可结构化、可计算、可二次开发的数据资产**

## 🚫 我们反对什么？(Our Manifesto)
在构建这个项目之前，我们看透了目前开源社区的种种乱象，并坚决说“不”：
- **反对黑盒式 Prompt 分发：** 不提供结构化数据、不支持二次使用的封闭系统
- **反对流量导向的伪开源：** 将 GitHub 作为引流入口，却将核心数据隐藏在私有平台强制登录获取
- **反对不可计算的数据形态：** 仅提供纯文本展示、无法被程序解析或训练使用的松散 Prompt 集合

## ✨ 项目优势（Goku Prompt Hub）

### 1️⃣ 全量数据开放
所有收录数据均可完整获取，不存在“试看内容”或“核心数据锁定”。
- 支持 Huggingface 直接全量下载
- 支持通过网站无门槛观看与检索

### 2️⃣ 结构化数据体系 (.jsonl)
我们的提示词数据被统一存储在 .jsonl 格式的文件中。每条 Prompt 均经过严格的标准化解析，并将视频实体、封面图片与参数完美关联。

*JSONL 结构化数据单条示例：*
`json
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
`

### 3️⃣ 开发者友好设计
- **统一 JSON Schema**: JSONL 格式能够完美地将数据逐行格式化为独立的 JSON 对象。
- **开箱即用支持数据库**: 极佳的数据集成度，支持一键无缝存入 SQLite、Supabase 或你的本地 AI 工具链。
- **一行 Python 代码即可加载**: 只需 1 秒即可将整个数据集直接加载为 Pandas DataFrame：

```python
import pandas as pd

# 极速加载数据集！
url = "https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/raw/main/metadata.jsonl"
df = pd.read_json(url, lines=True)
print(f"✅ 成功加载 {len(df)} 条结构化视频提示词！")
```

### 4️⃣ 开放许可（CC BY 4.0）
所有数据均采用 **CC BY 4.0 协议** 共享：
- ✔ 可自由使用
- ✔ 支持商业化
- ✔ 允许二次加工
- ✔ 允许再分发
- ❗ 仅需保留来源标注

## 📊 数据概览
- **总 Prompt 数量：** 2110+
- **覆盖语言：** 英文 / 中文
- **适用模型：** 字节涵盖核心（Seedance）及 Midjourney / Stable Diffusion / DALL·E 3 / Flux 等
- **数据更新：** 持续自动化同步解析

## 🛡️ 数据来源与免责声明
本仓库中的 Prompt 及相关元数据来源于互联网公开社区，仅用于学习研究与数据结构化处理用途。原始内容的版权及相关权益归原作者所有。

本项目仅提供：
- 杂项数据整理
- 结构化与规范化处理
- 标签分类与快速索引

我们不主张对原始创作内容拥有版权。如权利人认为内容存在问题，可通过 Issue 或邮件联系我们处理。同时，本项目不隶属于 Bytedance、OpenAI、Google、Midjourney 等任何模型开发实体或平台。

## 🤝 参与贡献
欢迎参与 Goku Prompt Hub 一同建设大模型时代的基础设施：
- **提交 Issue：** 反馈低质量、失效或重复解析的 Prompt
- **提交 PR：** 贡献你的高质量 Prompt 结构化数据集
- **Star 支持：** 给个🌟，推动 Prompt 数据开源生态真正落地！

---
*Happy Prompting!*



<!-- STATS_START -->

## 📊 数据统计
- 总 Prompt 数量：**8720**
- 今日更新（UTC 2026-08-18）：**25**

## 🎬 今日更新
### 🎬 古园旅拍
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11511.jpg" width="480" alt="SD2_11511"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-garden-vlog-SD2_11511">🌐 在线观看</a>

#### 📝 Prompt
```
请使用提供的图片作为拍摄地点参考，制作一段14秒的电影级旅行vlog。视频中，一位时尚的年轻女孩漫步于这座美丽的古朴花园，并拍摄vlog。拍摄时需保留参考图片中宏伟的历史建筑、五彩缤纷的花朵、湿润的小径、葱郁的绿植、摇曳的棕榈树以及整体氛围。视频开头需拍摄一个展现拍摄地点的全景镜头，然后女孩对着镜头自然地微笑和说话，并转动镜头展现周围美丽的景色。拍摄时需包含流畅的行走镜头、花朵和建筑的特写、自然的反应以及一个欢快的旋转镜头。使用温暖的金色阳光、真实的人物、电影级的景深、流畅的手持/云台拍摄、自然的城市环境音效以及超高清4K画质。视频结尾需拍摄一个展现同一地点的美丽全景镜头。视频中不得出现任何文字、标志或人工元素，并需准确还原参考地点。
```

#### 📌 Details
- Ratio: `1.51` | Duration: `14.7s`

---

### 🎬 粉笔日语演示
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11509.jpg" width="480" alt="SD2_11509"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/chalkboard-japanese-demo-SD2_11509">🌐 在线观看</a>

#### 📝 Prompt
```
[语音规则 - 首先阅读] 该女士只讲日语。她从不说中文、英语或任何其他语言。在整个剪辑中，她几乎一直在说话。她准确地说出了这句话，分成四个短语，按这个顺序，没有别的：「种子舞2.5なら」「黒板に日本语の文字を」「书くことができます。」「とても便利ですね」她以老师在黑板上写字的不紧不慢的速度说：她的声音减慢到她自己粉笔的速度，因此在她的手形成同一个短语的同时说出每个短语。声音和粉笔一起前进。只有短暂的自然呼吸将一个短语与下一个短语分开——任何地方都没有长时间的停顿。整个演讲时间大约占 15 秒中的 13 秒。唯一静默的时刻是最后0.8秒，她写完后只是微笑点头。全程禁止：即兴对话、填充词、重复短语、读两遍句子、哼唱、大笑、叹息，以及任何无声的哼唱，例如“んっ”、“うん”、“ふふ”、“啊”、“嗯”、“嗯”。她只说这四个短语各一次，仅此而已。“Seedance 2.5”的发音为英文“seedance two point five”。[参考] @Image1 = 关键帧：一位身穿白大褂的女子站在一块完全空白的绿色黑板旁，手中拿着一根细长的木制指示棒。严格保留 @Image1 的面部、头发、眼镜、白大褂、黑板的位置和大小、画架、背景书架以及画面构图。画面中除了她的手臂、上半身、面部以及她用粉笔画的痕迹之外，没有任何物体移动。 【一句话概括】15秒。一位笑容可掬的演讲者进行简短的讲解，一边用木制教鞭的尖端在绿色黑板上写下四行日语，一边大声朗读。皮克斯风格的3D动画。固定镜头。【整体设定】环境：温暖的室内书房，柔和的暖色调天花板灯光，浅景深，背景书架保持虚化。粉笔灰和画架的木质纹理高度逼真。视觉风格：皮克斯风格的3D动画，暖色调，柔和的阴影。镜头语言：中景，平视，正面镜头。镜头完全固定——无平移、无倾斜、无缩放、无推拉、无手持抖动。镜头行为：无。角色：与@Image1相同。保持眼镜、头发轮廓和外套一致。保持逼真的皮肤阴影和精细的表面细节——不要让她看起来像个塑料人。表演核心：一位热情自信、乐于展示的老师。 ***书写规则——她亲自书写，并边说边写。*** 每一条粉笔线都由她自己的手部动作产生，与她的声音节奏一致。每句话的书写过程如下：1. 她的肩膀和手肘将笔尖抬至笔画的起点。她的躯干微微转向黑板，目光首先落在该点上。2. 笔尖轻触黑板，沿着每一笔的轨迹移动。粉笔线出现在移动的笔尖正后方，与笔尖完全一致，绝不会超出笔尖的轨迹，也不会出现在笔尖未触及的地方。3. 字迹一笔一划地形成，遵循正确的日语笔顺，从左至右。笔尖扬起淡淡的粉笔灰，并伴有轻微的刮擦声。4. 笔画之间，笔尖抬起几厘米，然后在下一笔的起点落下。 5. 她说出的音节与她书写的汉字同步——当她的声音唱到某个词时，她的手就写出了那个词。声音和粉笔的书写节奏完全一致。6. 每写完一行，她都会略微降低笔尖，轻轻吸一口气，瞥一眼镜头，然后移到下一行。她的手臂引领笔画，笔迹跟随——手臂的移动和笔迹的出现必须逐帧同步。笔迹绝不会像一个完整的词那样逐渐显现。当她的手臂静止不动或笔尖离开黑板时，笔迹绝不会出现。没有隐形的手，也没有魔法般的书写。手臂的动作流畅自然：手腕弯曲，肘部张开闭合，肩膀带动笔尖越过黑板，身体重心随着笔尖的移动而略微移动。一行写完后，在接下来的镜头中，它都会留在黑板上保持不变。日语书写规则（重要）：每个汉字都要按照正确的笔画结构和笔画数书写——黒板 日 本 語 文 字 書 便 利。必须使用清晰易读的日文字符，而非自造字符或简体中文字符。书写时字号要大一些，笔画之间要保持间距。“Seedance 2.5”必须用拉丁字母和数字精确书写：Seedance，空格，2，句号，5。粉笔颜色——只能用两种：黄色粉笔仅用于书写“Seedance 2.5”，其他所有内容均使用白色粉笔。布局规则（重要）：四行，左对齐至共同的左边距，从上到下均匀排列，直至填满整个板面。使用大号、欢快的粉笔手写字体，笔画略微不均匀。确切的内容，从上到下： Seedance 2.5なら 黒板に日本语の文字を 书くことができます。 とても便利ですね 永远不要将线居中。永远不要写小。每行都写得尽可能大，同时仍然适合：完成的行几乎跨越了板的整个可写宽度，从左边距几乎到了板的右边缘，并且四行一起从上到下填充了板。字符宽且间距宽，因此密集的汉字（例如“黒板语”书便利）可以保持笔划分开且清晰易读。如果一行不适合，请使字符的高度更窄而不是更短 - 切勿缩小一行，使其仅占据板宽度的一部分。请勿添加任何其他文字、符号、箭头、下划线或绘图。禁止：无字幕、无隐藏说明、无屏幕用户界面、无水印、无背景音乐、无镜头移动、无切换到其他镜头、无其他人物、无第二只手进入画面、无空闲手中拿着粉笔、无已写线条的变形。[时间戳分镜脚本] 0.0-3.6秒 第1行 动作：她将指示棒举到空白黑板的左上角，用黄色粉笔写下“Seedance 2.5なら”——先写拉丁字母和数字，再写假名“なら”——笔尖移动时留下的痕迹。语音（与书写同步）「Seedance 2.5なら」 意图：看到品牌名称时，她微微扬起眉毛，带着一丝骄傲。这就是她要炫耀的东西。镜头：锁定。无字幕。无背景音乐。仅限日语。 3.6-7.2s 第2行动作：她跳到下一行，用白色粉笔一笔一笔地写下“黒板に日本语の文字を”。她的目光追随着自己的指尖。言语（与写作同步）：「黒板に日本语の文字を」 意图：就事论事，句子的设置一半。保持手臂稳定、均匀。相机：锁定。没有字幕。没有背景音乐。仅限日语。 7.2-11.0s 第3行动作：她跳到第三行，用白色粉笔一笔一画地写下“书くことができます。”，以坚定的点结尾。 言语（与书写同步）：「书くことができます。」 意图：这就是这句话的结果——她的声音在“ます”上稍微变硬，最后一个点被果断地轻轻敲击了一下。相机：锁定。没有字幕。没有背景音乐。仅限日语。 11.0-15.0s 第 4 行 — 结束动作：她用白色粉笔在底线上写下“とても便利ですね”，然后将指针降低到她的一侧，将脸完全转向镜头，露出一个开放的温暖微笑，并明确地点点头。她保持这个姿势，静默地持续了最后0.8秒。旁白（与文字同步，在14.2秒结束）：“とても便利ですね”。意图：点头表示结束。温暖，略带俏皮，仿佛在分享一个美好的发现。镜头：固定。无字幕。无背景音乐。仅日语。[结束限制——适用于整个片段]
```

#### 📌 Details
- Ratio: `0.56` | Duration: `13.0s`

---

### 🎬 皮克斯风沙龙护发
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11505.jpg" width="480" alt="SD2_11505"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pixar-salon-asmr-hair-care-SD2_11505">🌐 在线观看</a>

#### 📝 Prompt
```
3D皮克斯风格动画，8K分辨率，竖屏格式，3:4宽高比。一段温馨奢华的沙龙ASMR美发护理视频。一位可爱的年轻动画女郎，拥有一头柔顺的黑色长发，身着柔软的白色浴袍，舒适地斜倚在光滑的白色洗发池旁。一位笑容可掬的发型师，梳着随意的发髻，系着围裙，轻柔地为她清洗、涂抹洗发水并按摩头发。视频特写展现了金色水龙头流出的水流、丰富的白色泡沫、木质头皮按摩刷在柔软泡沫中轻柔按摩、几滴护发油按摩头皮、顺滑的木质梳子以及用白色毛巾擦干头发的细节。最后，女郎坐起身来，对着镜头露出灿烂的笑容，展现出她闪亮、蓬松、柔软的秀发。温馨的氛围，温暖的烛光、大理石台面、白色兰花和金色点缀，营造出舒适惬意的视觉效果。电影级的灯光效果、柔和的景深、极其流畅的镜头运动、逼真的流体物理效果，营造出轻松舒缓的氛围。——ar 3:4
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.08s`

---

### 🎬 废墟机械奔袭
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11503.jpg" width="480" alt="SD2_11503"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rusted-automaton-radioactive-ruins-SD2_11503">🌐 在线观看</a>

#### 📝 Prompt
```
镜头持续追踪拍摄一座坍塌的巨型城市，城市已被放射性丛林覆盖。主体是一个三英尺高的锈迹斑斑的自动装置，它有着破碎的玻璃面罩、裸露的铜线头发和活塞驱动的四肢。它飞奔过倾斜的摩天大楼梁柱，跃过破碎的窗户，滑过坠落的单轨列车车厢，攀爬缠绕在输电塔上的藤蔓，并在两座即将倒塌的建筑物之间跳跃，丛林实时地吞噬着混凝土。尘埃微粒、穿过树冠的光束、锈迹颗粒、体积雾。电影级8K画质，逼真的腐朽纹理。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 蓝底跑鞋创意广告
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11499.jpg" width="480" alt="SD2_11499"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/blue-running-shoe-ad-SD2_11499">🌐 在线观看</a>

#### 📝 Prompt
```
真人拍摄的跑鞋广告，时长20秒，无剪辑。背景始终保持单一的亮蓝色，没有渐变、纹理、地板或阴影。鞋子从画面顶部连续向下落下。画面中同时出现数十双跑鞋。它们都是同一型号，区别仅在于颜色：轻薄的跑鞋，鞋面采用亮色针织网布，鞋底为厚实的白色泡沫材质，鞋跟处有一个银色小标签。所有配色的标签颜色都相同，鞋子上没有任何金色或黑色金属元素。颜色依次为橙色、柠檬绿、珊瑚色、深灰色、白色和浅蓝色。每双鞋都从上往下落，落下的方向相同；不同之处在于每双鞋的翻转角度不同，因此在同一个画面中，有些鞋底会露出，有些鞋侧会露出，有些鞋则会从上方俯视。任何靠近镜头的鞋子都从画面顶部进入，从底部离开。它们既不在画面中央出现，也不在画面中央消失。近处的物体清晰锐利，远处的物体则只呈现出模糊的小色块。焦点始终集中在一个平面上，其前后的一切物体都柔和地消散开来。相机保持着它的位置，仿佛呼吸般微微颤动。画面的主体是那双鞋。画面进行到一半时，撕开的纸边掠过画面，撕开了下面的纸层。沿着每一道撕裂，纸张的白色芯材都变得参差不齐、纤维状，柔和的阴影投射到下面的纸层上。无论她出现在哪里，相机都始终在她前方。它从不跟随她的背部或后脑勺；她的脸始终面向镜头。纸层下的照片是黑白的：高调，天空过曝成白色，带有粗糙的暗房冲印颗粒。即使在黑白画面中，鞋子依然保持着原有的色彩。画面中出现了一位女性，她始终是同一个人：一位二十岁出头的韩国女性，五官轮廓分明，眼睛细长，下颌线条分明。她一头深红褐色的长发，如波浪般垂至腰间，几缕细小的辫子从头顶垂下。跑步时，她将头发扎成一条马尾。她身着三件衣物：内搭一件浅蓝色露脐吊带背心，外罩一件深灰色薄纱短款外套，长袖带拇指孔，遮住了手背，下身是深灰色束脚运动裤，裤腰处系着浅蓝色抽绳。跑步时，她始终穿着这三件衣物，它们从未变成跑步背心或运动短裤。脚上穿着前面提到的那双白色泡沫中底跑鞋。（0:00–0:03）影片以一只珊瑚色跑鞋的侧面镜头开始，占据了画面左上方，近到可以清晰地看到鞋面针织纹理、中底纹路和缝线。镜头沿着轴线向右下方倾斜，直到露出鞋子的内部。在它身后，数十只大小不一的跑鞋依次出现。 （0:03–0:05）一双浅绿色的鞋子卡在框架的顶部边缘，只有脚趾顶着，距离近到可以清晰地看到针织网的纹理和中底的质感。框架的其余部分是蓝色的，只有几只小鞋子从远处落下。（0:05–0:07.5）“LAND LIGHT”几个字以白色衬线大写字母的形式出现在框架中央，字母间距非常宽，位置固定。这些字母印在纸上，笔画内部可以看到水平的印刷线。一只鞋子落在字母前面，另一只落在字母后面。从右下角，撕开的纸边斜向上翘起，剥落了蓝色的纸层。（0:07.5–0:13）在纸边剥落的地方，出现了一张明亮的黑白照片。相机低低地放在她正前方的聚氨酯跑道上，镜头正对着她，随着她跑向相机，镜头也随之后退。白色的泡沫中底向前延伸，触地后压缩，然后弹回。只有鞋子保留着珊瑚色；其他一切都是黑白的。镜头从她的脚向上移动到她的脸，从正面框住她，胸部以上，画面宽阔。她的目光直视前方，脸上汗水浸湿，深褐色的头发飘动，一切都清晰可见。她身后的看台和天空逐渐虚化，天空被过曝成白色。（0:13–0:16）撕裂的边缘从画面底部升起，蓝色图层再次出现。一双珊瑚色的鞋子从画面正中央落下，一只鞋搭在另一只鞋上，镜头拉远，整只鞋都清晰可见。一道高光掠过鞋跟上的银色小标签。（0:16–0:17.5）一张电光蓝的纸从顶部落下，覆盖了整个画面。它的下边缘撕裂，露出白色的纸芯。（0:17.5–0:20）一片明亮的米白色纸面。画面中央是两行细长的字母：LAND LIGHT，RUN LONG。除此之外，没有其他文字或符号。画面下方边缘有一条撕裂的痕迹，角度很浅。最后一帧画面正好落在这个撕裂处。这显然是一部商业影片。胶片颗粒感仅体现在黑白图层上；蓝色图层清晰锐利。文字只出现在两个地方：0:05–0:07.5 处的 LAND LIGHT 以及最后一帧画面上的两行文字。没有任何品牌名称或标志出现。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `20.08s`

---

### 🎬 韩女市集自拍
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11493.jpg" width="480" alt="SD2_11493"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-girl-market-selfie-vlog-SD2_11493">🌐 在线观看</a>

#### 📝 Prompt
```
&lt;&lt;<image_1> &gt;&gt; = 仅保留女性的面部特征和发型，不包含其服装、姿势、背景或光线。全程使用手持前置手机自拍vlog，始终以她自己的视角拍摄，手机握在她手中，手臂伸直——不使用第三人称或外置摄像头，不使用三脚架，也不使用电影化的移动镜头。呈现真实的现代智能手机画面：轻微的手持抖动、行走时的轻微晃动、偶尔的自动对焦尝试、轻微的曝光偏移、轻微的构图瑕疵、自然的前置镜头畸变；柔和温暖的自然日光逐渐过渡到傍晚，手机色彩未经校正，没有进行任何色彩校正、美颜滤镜或磨皮处理。始终是同一位女性，保持相同的面部和发型，每次拍摄都由她本人手持手机。仅使用两套休闲时尚的服装，造型自然流畅——一套是从市场入口到礼品店的造型，另一套是从照相亭开始的明显不同的造型，每套服装的同一部分都完全相同，面部和发型在更换服装的过程中保持不变。没有字幕、屏幕文字、logo或水印；不使用任何品牌或角色名称。绝不使用参考图或重复任何主题。仅使用叙事性声音，不使用背景音乐：市场熙熙攘攘的人群和交谈声、脚步声、滋滋作响的街头小吃摊、安静的商店环境音、咖啡馆氛围、照相亭快门声、观景台的风声、公交车引擎声和街道声；所有台词均正面拍摄，嘴唇清晰可见。一位二十出头的韩国年轻女性，拥有自然的日常美，在休息日走进一个热闹的传统街市，她已经举起手机自拍；她用手机扫过熙熙攘攘的摊位，然后又回到自己灿烂的脸上，兴高采烈地说：“我在市场！”她继续在熙熙攘攘的市场中穿行，手机随着步伐自然地晃动，她瞥了一眼色彩缤纷的摊位，并短暂地将镜头转向有趣的食物和人群，然后又回到自己微笑的脸上；她轻声笑着，继续走着，没有一句台词。她停在一家热气腾腾的路边小吃摊前，拿起一串热乎乎的烤肉串，举到自拍镜头前，仔细端详着它的诱人模样，然后欣喜地说：“哇，这看起来太棒了！”尝了一口后，她高兴地笑了笑，然后继续拿着手机在市场里漫步。她走进一家摆满了可爱小玩意儿的小型礼品文具店，笑容满面地浏览着货架；她拿起一件小东西，看了看，又对着镜头露出一个略带担忧的表情，说道：“我觉得我的钱包可能要遭殃了。”离开商店后，她又在一家温馨的小咖啡馆或饮料摊前稍作停留，拿着一杯简单的外带饮料靠近自拍镜头，抿了一口，对着镜头露出满足的笑容，然后继续前行，周围只有咖啡馆和街头的自然氛围。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.08s`

---

### 🎬 血月传送门惊魂
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11487.jpg" width="480" alt="SD2_11487"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/blood-moon-portal-eclipse-SD2_11487">🌐 在线观看</a>

#### 📝 Prompt
```
{ &quot;duration&quot;: &quot;20 秒&quot;, &quot;aspect_ratio&quot;: &quot;9:16&quot;, &quot;style&quot;: &quot;超逼真，手持智能手机拍摄的原始视频，自然光照，数字噪点，逼真的运动模糊，伪纪录片风格&quot;, &quot;camera&quot;: { &quot;type&quot;: &quot;手持智能手机&quot;, &quot;movement&quot;: &quot;手部抖动，恐慌性抖动加剧，突然倾斜和抖动&quot;, &quot;perspective&quot;: &quot;第一人称视角，来自拥挤人群内部&quot;, &quot;lens&quot;: &quot;广角手机镜头，自然畸变，镜头光晕&quot; }, &quot;scene&quot;: &quot;2026 年 8 月 12 日日全食期间，西班牙北部悬崖上聚集着一大群兴奋的人群。傍晚时分。&quot;, &quot;sequence&quot;: [ { &quot;time&quot;: &quot;0-5 秒&quot;, &quot;action&quot;: &quot;日全食开始。正常的黑色月亮，带有明亮的白色日冕。人们欢呼并拍摄。镜头扫过人群。&quot; } }, { &quot;时间&quot;: &quot;5-9秒&quot;, &quot;动作&quot;: &quot;出乎意料的是，黑色的月亮开始变成深血红色。日冕变成闪耀的深红色。人群从欢呼声转为困惑的喘息声。&quot; }, { &quot;时间&quot;: &quot;9-14秒&quot;, &quot;动作&quot;: &quot;一个圆形发光传送门在红色月亮周围撕裂开来，向外扩散，伴随着旋转的能量和光芒。人群中的一些人开始缓缓向上飘向传送门。&quot; }, { &quot;时间&quot;: &quot;14-20秒&quot;, &quot;动作&quot;: &quot;一片混乱。人们尖叫着四处奔逃。更多的人被拉向空中，朝着红色传送门飞去。拍摄者惊慌失措，一边试图逃跑，一边拍摄红色月亮和传送门，摄像机变得极度不稳定。&quot; } ], &quot;audio_cues&quot;: &quot;兴奋的人群噪音 → 困惑的喘息声 → 大声尖叫、风声、奔跑声、沉重的呼吸声、手机麦克风失真和削波&quot;, &quot;negative_prompt&quot;: &quot;流畅的镜头、电影级的色彩调校、CGI 效果、文字、水印、完美对焦、专业电影、卡通&quot; }
```

#### 📌 Details
- Ratio: `0.56` | Duration: `20.13s`

---

### 🎬 废仓丝线凌空舞
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11485.jpg" width="480" alt="SD2_11485"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/aerial-thread-dance-warehouse-SD2_11485">🌐 在线观看</a>

#### 📝 Prompt
```
真机 iPhone 15 Pro Max，9:16 竖屏，一镜到底的固定镜头——相机置于地面，无移动、无变焦、无剪辑、无调色，真实颗粒感，日光。视角：相机即为置于地面的手机——始终不可见：不在手中，不在画面中，也不以反射形式出现。仓库：15 米高的锈蚀横梁，尘土飞扬的空气中弥漫着光束，涂鸦墙，龟裂的混凝土。线：每次她张开手掌，一根半透明的白色细线便从掌心射向横梁，然后她抓住细线并摆动——细线从未预先连接；被点燃的细线会保持悬挂状态。她走进去，蹲下，手触地，站起，从左侧离开。跑回来——手掌指向右上方的横梁，细线射出，连接，向上摆动；在最高点，她缓慢地翻了个跟头，足尖鞋尖绷直。她腾空而起，另一只手掌击向左上方的光束，摆向左侧墙壁，双脚蹬地，一个干净利落的后空翻，低蹲着落地。她走到我们面前，蹲下，双手伸向镜头，脸朝上——微微一笑。轻轻呼气。保持。停。
```

#### 📌 Details
- Ratio: `0.56` | Duration: `12.07s`

---

### 🎬 温馨晨间早餐
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11479.jpg" width="480" alt="SD2_11479"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cozy-morning-breakfast-SD2_11479">🌐 在线观看</a>

#### 📝 Prompt
```
使用提供的参考图片作为人物参考，制作一段15秒的超逼真16:9横屏生活方式视频。视频中要保持人物的面部特征、身份、发型、身材比例、肤色和整体外貌的一致性。不要改变人物的身份。0-3秒——厨房：中景镜头。他兴高采烈地走进厨房，将鸡蛋打入碗中，开始准备早餐，动作充满活力但自然流畅。3-6秒——烹饪：侧四分之三镜头。他将鸡蛋倒入平底锅中煎熟，脸上带着轻松的微笑。视频中要展现逼真的蒸汽、厨具、手部动作和烹饪物理效果。6-9秒——电视：他短暂地走进隔壁的客厅，拿起遥控器打开电视，带着一丝微笑瞥了一眼屏幕，然后返回厨房。9-12秒——完成早餐：回到厨房。他检查并搅拌/翻动食物，看起来很满意，然后将做好的早餐装盘。 12-15秒——用餐：餐桌前四分之三侧面镜头。他坐下，开心地看着早餐，微笑着，咬下第一口。风格：写实休闲的日常生活vlog，真实的居家环境，快乐活泼的氛围，自然的表演，真实的人体动作，轻柔的手机手持拍摄，自然的自动对焦，逼真的景深，24帧/秒。光线：柔和的自然晨光与真实的室内灯光混合。保持：面部和服装的一致性，真实的手部/手指，准确的物体互动，一致的厨房/客厅布局。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 老人与鸽的温馨时光
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11475.jpg" width="480" alt="SD2_11475"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/old-man-pigeon-warmth-SD2_11475">🌐 在线观看</a>

#### 📝 Prompt
```
【场景设定】温暖的晨光洒在舒适的老公寓阳台上，五彩缤纷的花盆、木椅、晾晒的衣物、摆放着鸟食的小桌子，构成了一幅温馨的画面。3D风格化动画，人物形象圆润可爱，表情丰富，充满趣味的肢体喜剧元素，传递出真挚的温暖。【角色1：古怪的老人】75岁以上，圆滚滚的肚子，稀疏的白发，褪色的开襟羊毛衫，宽松的裤子，破旧的拖鞋，眼镜滑落鼻梁。很少说话，主要通过面部表情和肢体语言交流。始终穿着同样的开襟羊毛衫。【角色2：调皮的鸽子】一只羽毛闪亮的胖乎乎的灰色鸽子，好奇的眼神和傲娇的性格。大部分时间保持沉默，通过头部动作、表情和肢体语言进行交流。【开场，0-6秒】老人坐在阳台的椅子上，将一小堆葵花籽放在手掌上。他微笑着对鸽子说：“来吧，小家伙。”鸽子缓缓靠近，狐疑地盯着他。[搞笑片段，6-14秒] 鸽子突然叼起种子，跳到老人头上。老人愣住了，瞪大了眼睛。他缓缓抬头，而鸽子则一脸得意地俯视着他。老人叹了口气，摇了摇头。[温馨片段，14-23秒] 老人小心翼翼地把鸽子从头上抱下来，轻轻地搂在胸前。鸽子放松下来，依偎着他。老人微笑着轻声说：“你赢了，小家伙。” 他轻轻抚摸着鸽子的羽毛。[结尾，23-30秒] 老人静静地坐在金色的阳光下，鸽子依偎在他身边。鸽子舒服地闭上了眼睛。老人微笑着，闭上眼睛，轻轻地笑了。镜头缓缓拉远，展现出温馨的阳台。 【一致性】一位老人，一只灰鸽，始终穿着同样的衣服，站在同一个阳台上，灯光也保持一致。全程无剪辑，无场景切换，无角色重复。无字幕或文字。【配音】温暖自然的老年男性嗓音，温和而略带幽默。仅有两句简短的台词。自然的鸽子咕咕声、轻柔的翅膀拍动声、清晨鸟鸣、微风拂面，在搞笑桥段配以轻柔的喜剧音乐，在结尾处营造出温馨怀旧的氛围。
```

#### 📌 Details
- Ratio: `0.56` | Duration: `20.04s`

---

### 🎬 京都少女漫步
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11473.jpg" width="480" alt="SD2_11473"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/kyoto-solo-date-walk-SD2_11473">🌐 在线观看</a>

#### 📝 Prompt
```
创作一段15秒的超写实旅行短片，场景设定在日本京都，跟随一位年轻的金发女郎，记录她独自一人在京都传统街道上享受宁静约会的时光。0-2秒：正面中景镜头，女子站在一栋传统的京都町屋外，深色木格门。她面带自然微笑，对着镜头俏皮地做了个手势。温暖的午后阳光，逼真的肌肤和头发动态，浅景深。2-4秒：镜头切换到她身后的流畅手持追踪镜头，她正走过一条狭窄的传统京都小巷。木质建筑、纹理丰富的墙壁、小植物和温暖的阳光营造出美丽的自然景深。镜头紧随其后，呈现微妙而真实的运动。4-6秒：广角后方追踪镜头，她继续沿着一条安静的石板路前行，路两旁是传统的木屋和盆栽绿植。柔和的黄金时段阳光投射出长长的影子和淡淡的镜头光晕。6-8秒：她走到一条小运河边，在石墙旁驻足。一只友善的橙白相间的猫沿着运河边漫步。她面带微笑地望着运河。水面映照着自然的倒影，微风轻拂着她的头发和衣衫。8-10秒：镜头切换到一台日式自动售货机旁的特写镜头。她买了一小罐红色饮料，抿了一口，脸上带着自然的微笑。逼真的手部动作，真实的自动售货机细节，浅景深。10-12秒：黄金时段的街景。她站在京都的一条小路旁，随意地环顾四周，一辆传统的黄色出租车从她身后驶过。强烈的阳光，真实的交通流线，电影般的逆光。12-15秒：镜头回到狭窄的木巷。她拿着饮料走向镜头，然后短暂地转身，带着柔和的微笑回头望去。镜头缓缓拉远，展现出美丽的京都传统建筑，画面自然淡出。整体风格：逼真的日本旅行电影，真实的京都氛围，自然的人体动作，真实的行走物理效果，微妙的呼吸和眨眼，细致的头发和衣物飘动，温暖的黄金时段光线，柔和的电影镜头光晕，浅景深，自然的手持/云台摄像机运动，逼真的阴影和反射，纪录片风格的摄影，35毫米胶片质感，高端旅行广告，高度精细，无缝过渡，没有不自然的CGI，没有扭曲的手部或面部，人物形象始终保持一致。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 史诗奇幻世界树
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11467.jpg" width="480" alt="SD2_11467"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/epic-fantasy-world-tree-SD2_11467">🌐 在线观看</a>

#### 📝 Prompt
```
超史诗级电影级3D CGI奇幻世界，纯粹的原创想象，超精细的逼真3D渲染，虚幻引擎5 + Octane品质，体积光晕，精巧的晶体几何结构，鲜活的魔法能量，8K分辨率，流畅的连续镜头运动，30秒。场景：0-7秒：一个悬浮在虚空中的奇幻世界，展现出一个宏伟的开场镜头。一棵大陆般大小的古老世界树从一块破碎的漂浮大陆上倒置生长，它的根系形成闪耀的琥珀色水晶活桥，横跨天际。液态星光如河流般向上倾泻，而非坠落。镜头缓慢而庄严地环绕拍摄，两颗日食的太阳投射出戏剧性的双色光芒（深金色和电光紫罗兰色）。7-15秒：镜头戏剧性地穿过闪耀的根系，直达世界树的核心。内部，巨大的空心空间充满了漂浮的发光球体，每个球体都包含着完整的微型星系。由活石和星象图案构成的巨大空灵泰坦缓缓苏醒，沿着内壁行走。纯粹魔法的能量风暴以慢动作翻腾。强烈的体积光和粒子系统。15-23秒：镜头从树干向外猛然拉开，进入开阔的天空。一头由半透明水晶和星云气体构成的巨型天鲸滑过，其身躯蕴藏着风暴和闪电。下方，一个由螺旋状水晶城市组成的文明如同活体生物般从漂浮的陆地上有机生长。巨大的符文石碑升起并在空中旋转，释放出金色的能量波。史诗般的广角追踪镜头，展现出极强的景深和规模。23-30秒：最后，镜头强力拉远，展现出整个原创奇幻宇宙：世界树位于中心，周围环绕着环绕的岛屿、天鲸和星光河流，构成一个鲜活的曼荼罗。双日完全合相，释放出一股巨大的纯净魔法光芒，席卷整个场景。电影般的慢镜头最终定格在世界树闪耀的轮廓上，映衬着浩瀚的宇宙虚空​​。风格：纯粹的3D想象，无2D元素，超写实材质，极致的比例对比，戏剧性的光影效果，浓郁的氛围薄雾，前所未见的精妙原创设计，史诗般的震撼氛围，浑然一体的画面感。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 仙侠师姐定力挑战
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11463.jpg" width="480" alt="SD2_11463"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/xianxia-stoic-challenge-SD2_11463">🌐 在线观看</a>

#### 📝 Prompt
```
电影级写实质感，纯古风中国仙侠美学，克制冷面的喜剧表演，观察式电影摄影，真实微表情、身体重量、真丝材质、细腻胶片颗粒、体积空气纵深、真实三维摄影机位移，以及一个从第一帧到最后一帧始终持续生活的参考图世界。控制协议——三条轨道必须同时运行，但三者绝不能互相抢夺叙事权限。主角剧情轨拥有100%编剧权。环境生命轨拥有持续运动权，但拥有0%编剧权。背景人物轨拥有独立生活权，但拥有0%主角互动权。环境不得制造、触发、解释、打断、解决、改变、强调或卡点任何人物剧情。风、云、雾、光线、反射、建筑、远景人物、植被和水体不得因为对白、眼神、喜剧包袱或者主角动作而产生特殊反应。摄影机为什么运动，只能由主角剧情和人物调度决定。但是与此同时：所有非主角区域绝不能冻结。将当前上传的全部参考图理解为世界DNA，而不是被冻结的像素，也不是一张需要保护的静态背景板。正式生成前，先综合理解参考图里的地貌逻辑、建筑语汇、尺度关系、材质、天气、云层体系、植被、反光表面、通行动线、主要光线方向、前景—中景—远景关系以及画外空间延伸，然后重新构建成一个真实连通的三维地点。保留参考世界的身份和逻辑，但允许重新规划空间排列和摄影机进入方向，不机械复制任何一张参考图原本的二维构图。整个10秒中，每一个大约2秒的时间窗口，都需要让不同空间层级存在多个清楚可见的非主角运动源。这些运动不能同时开始。也不能以完全相同的速度一起移动。极远景：当前世界中合理存在的一整层巨大云层或空气层，从开场以前就已经以缓慢、稳定的速度持续迁移，穿过宏大的远景结构。深中景：安排4–6名尺寸很小的远景环境人物作为独立群众演员。其中一人沿远处真实通道连续行走数秒。另一人沿现有台阶或路径上行或下行。另外一人停顿整理衣袖、携带物或者自身服装，然后继续。另外两人可以自然擦肩而过，各走各路。他们的所有行为与两位主角毫无关系。不得看主角。不得因为主角停步而停步。不得因为主角说话而转身。不得为了笑点同步动作。任何一个可见背景人物都不能整段10秒完全被冻结。中景空气层：薄雾、低云或其他当前参考世界合理存在的空气体积，持续绕过真实建筑和地形运动。雾气必须能够被实体建筑遮挡。进入建筑后方以后短暂看不见。随后根据真实空间关系从另一侧重新出现。绝不能直接穿过实体结构。近景层：摄影机真实移动过程中，让一个符合当前参考世界的近景元素——雾层、植物、布幡、建筑边缘或其他合理物体——短暂从镜头近处经过。让观众明确感觉摄影机位于空间内部。如果参考环境中存在水、湿润石材、金属、玉石或者其他反光表面，其反射必须随着摄影机位置和观察角度持续变化，不能像画在背景图上一样固定。所有环境运动共享同一套天气体系和统一风向。角色A剑仙师姐：25–30岁东亚女性，椭圆脸，白皙自然肤色，深色杏眼，黑色长发半挽，以白玉簪固定，高挑纤细，白色刺绣真丝汉服、半透明分层宽袖、银色腰封、玉佩、白色布靴。角色B小师妹：20–25岁东亚女性，圆润灵动脸型，黑发编辫，身形娇小，青绿色亚麻汉服、深色腰带、木簪、黑色布鞋。0-5s 全景或远景——主角剧情轨：摄影机从经过重新构建的三维世界内部开始一次真实的向前并略带横向推轨。近景空间或者空气层从镜头附近短暂经过。中景建筑相对于极远背景产生清楚的视差位移。两个人并肩正常向前走。同一个剑仙师姐突然非常认真地说道：\“今日练定心。\”同一个小师妹略微转头看她。剑仙师姐继续说道：\“谁先笑，谁输。\”小师妹立刻收起所有表情。两个人同时停下。然后转身面对彼此。这一整段剧情只来自剑仙师姐主动提出练习定力。绝不能由任何背景变化触发。0-5s 环境生命轨同时独立运行：两人说话时，远处巨大云层继续按照原本方向缓慢迁移。一名远景人物继续横向穿过远处平台。另一名人物继续沿真实道路或台阶移动。中景雾气继续以原来的速度流动。局部稳定风场继续产生细小衣料、植被或悬挂物运动。对白开始时背景不能突然动起来。两个人停下时背景也不能跟着停。5-10s 中景双人镜头 / 牛仔景——主角剧情轨：两个人面对面，相距约一个半手臂。双方努力保持完全没有表情。没有法术。不拔剑。环境不参与原因。小师妹为了破坏师姐定力，只做一个极小的动作：其中一侧脸颊非常轻微地鼓起来大约半秒。随后立刻恢复正常。剑仙师姐差一点有反应，但强行保持镇定。她只用极小幅度挑高一侧眉毛。小师妹嘴角差一点上扬。她立刻压下去。剑仙师姐的嘴唇也开始出现极难察觉的颤动。这一段两个人都不能真正笑出来。摄影机围绕两个人进行约15–20度的缓慢真实小弧形移动。摄影机必须真的换位置。不能使用数字变焦模拟环绕。背景近中远层因此产生不同速度的真实视差。喜剧只来自两个人的微表情和克制。5-10s 环境生命轨与背景人物轨继续独立运行：人物进入中近景之后，绝不能因为画面开始强调脸部，就把后方世界变成静态景片。不同纵深仍然必须保留多个清楚运动源。一名远景人物继续向前行走，并在行进过程中被原本存在的建筑自然遮住。另一名背景人物从另一个原本存在的空间遮挡后自然出现，然后继续自己的路线。空气体积继续在建筑后方和之间移动。摄影机做弧形运动时，中景结构和远景空间继续产生不同视差。云层、雾、反光和远景人物绝不能因为主角正在表演微表情而停止运动。所有背景运动都与主角节奏保持不同步。结尾续接状态：9.5-10s，两名主角身体尽量稳定，便于扩展续接。但只能稳定人物，不能冻结世界。剑仙师姐和小师妹仍然面对彼此。两个人都处于明显快要憋不住笑、但仍在强行保持严肃的状态。人物重心、视线和表情清楚。摄影机逐渐稳定。此时极远云层仍然能看到持续迁移。至少有一名远景人物正在行走过程之中，而不是站成静态人形贴纸。中景空气仍在运动。至少一个反光或光影状态仍然在连续演化。这个“人物稳定、世界仍运动”的准确状态作为第2段的时间续接状态。16:9横屏，原生同步普通话对白，配乐克制，真实脚步声、衣料声、远景脚步、风声与空间环境声。画面存在两名主要女性角色，同时允许出现尺寸较小、完全独立生活的远景环境人物。不生成字幕，不出现现代元素。Negative（第1段独立）：blurry, bad quality, low quality, low resolution, noisy, jpeg artifacts, watermark, text, subtitles, error; deformed, mutated, bad anatomy, poorly drawn hands, bad composition, out of frame, disfigured; inconsistent protagonist identity, changing clothes, face morphing, hairstyle change; static background plate, frozen scenery, frozen background people, background people standing motionless for the whole clip, living people rendered as landscape texture, duplicated background extras, background extras staring at protagonists, background extras synchronizing with protagonists, background extras reacting to dialogue, background extras reacting to comedy; flat 2D reference image, animated wallpaper, camera sliding over a photograph, fake digital zoom, fake parallax, foreground midground and background moving at identical speed, no occlusion, no object permanence, fixed cloud texture, static cloud sea, frozen mist, static reflections, painted reflections, static distant people, lifeless architecture surroundings, environment stopping during dialogue, environment stopping during close-up, environment freezing when protagonists stop, all environmental movement beginning at the same moment, all environmental movement synchronized to plot beats, dramatic wind caused by dialogue, cloud change caused by laughter, lighting change used as punchline, environment creating or solving story, camera following weather instead of protagonists, random new landmarks, impossible geometry, background replacement, teleporting extras, modern elements, glitching cuts 第2段作为独立扩展视频生成。如果当前 Seedance 工作流允许视频续接或视频参考，优先把第1段完整视频本身作为时间运动参考，同时把第1段最终一帧作为第2段开场视觉状态。绝不能只重新生成一个“长得差不多”的地点。必须让同一个世界沿着第1段已经建立的时间继续向前运行。完整继承同一个剑仙师姐和同一个小师妹，包括完全一致的面部、发型、身体比例、服装、准确站位、上一段结尾的憋笑表情、视线、摄影机高度、摄影机轴线和镜头透视。同时必须继承活世界本身的运动相位。第1段结束时正在行走的背景人物，从他们当时所在的位置和行进方向继续走。不能重新站回起点。云层保持之前已经建立的方向和速度继续迁移。正在流动的雾从上一段结束时的实际空间状态继续运行。反光继续演化。不能突然恢复成第1段开场时的样子。三条轨道权限保持完全不变：主角剧情轨 = 100%编剧权。环境生命轨 = 持续物理运动权，0%编剧权。背景人物轨 = 独立生活权，0%主角互动权。背景不能导致两个人笑。环境不能替她们决定输赢。远景人物不能帮助完成包袱。10-15s 双人特写 / 克制弧形运动——主角剧情轨：直接从第1段结束时两个人正在憋笑的准确表情开始。双方继续努力不笑。同一个小师妹改变策略。她突然把站姿调整得极其端庄，然后非常认真地模仿剑仙师姐平时那种高冷、平静、一本正经的表情。同一个剑仙师姐立即看出她在模仿自己。鼻翼出现一次极轻微变化。她忍住。小师妹看见这一点细小反应以后，自己的嘴唇开始更加明显地轻颤。剑仙师姐又看见小师妹正在努力憋住。于是现在变成：两个人都在努力不对“对方努力不笑的样子”产生反应。只使用非常小的微动作逐渐升级：一次挑眉。一次压住呼吸。一次下唇轻颤。一次几乎看不见的肩膀震动。不要夸张扮丑。不要大幅喜剧动作。环境完全不参与笑点。大约14.5秒，两个人终于在完全相同的瞬间破功，同时发出一声短促而真实的笑。这个笑只能来自两个人相互反馈的表情。10-15s 环境生命轨同时继续：即使镜头进入人物近景，人物后面的空间仍然必须拥有清楚可见的生命运动。第1段里已经在走的一名背景人物继续自己的路线，然后被原本存在的建筑自然遮挡。另一名背景人物在更深一层空间沿不同路线经过。第三名背景人物完成一个非常小的、与主角无关的生活动作，然后继续行走。远景云层继续迁移。雾继续流动。反光随着摄影机角度微变继续变化。两个人笑出来的瞬间：不能突然起风。不能突然亮灯。不能让背景人物转头。不能让云雾突然加速。不能出现任何背景同步反应。15-20s 中远景收尾——主角剧情轨：短暂笑完以后，两个人马上重新恢复严肃。小师妹问：\“平局？\”剑仙师姐思考半拍：\“重来。\”小师妹认真点头。两个人一本正经地把脸重新恢复成极其正式的状态。然后同时转回前方。继续并肩正常向前走。走出两步以后：小师妹非常随意地侧眼偷看师姐。没想到同一个剑仙师姐此刻已经在侧眼看她。两个人视线正好撞上。双方嘴角再次出现极细微的要笑趋势。但这次谁都不说话。不要再追加第三个包袱。最后保持观察式余味。15-20s 摄影机轨与环境生命轨：摄影机因为两个人重新开始走路，转换成柔和的四分之三侧向跟拍。摄影机移动原因仍然只来自人物走路。但是摄影机必须真实产生空间位移。一个符合参考世界的近景层从画面一侧自然掠过。两名主角位于中景。更深的空间中至少仍然有两名自主背景人物保持活动。其中一人穿过薄雾区域，身体被空气层部分遮住，然后继续移动。另一人在不同深度以明显不同的画面速度经过。极远巨大景观相对移动非常缓慢。云和雾完全继承第1段原本的运动方向，不重新开始。如果场景存在反光表面，亮部随着摄影机横向位置改变而连续滑动。人物最后一个眼神笑点结束以后，背景运动仍然继续。最后0.5秒：两名主角仍然向前走。同时观众仍然可以清楚看到多个彼此独立的非主角运动源。笑点结束了，但世界没有结束。16:9横屏，原生同步普通话对白与真实短笑，精准口型，与第1段时间状态无缝连续，真实摄影机视差，自主运动的远景背景人物，持续空气运动，物理合理的动态反光和环境空间声。两名主要女性角色，同时允许存在尺寸很小的远景环境人物。不生成字幕，不出现现代元素。Negative（第2段独立）：blurry, bad quality, low quality, low resolution, noisy, jpeg artifacts, watermark, text, subtitles, error; deformed, mutated, bad anatomy, poorly drawn hands, bad composition, out of frame, disfigured; inconsistent protagonist identity, changing clothes, face morphing, hairstyle change; background reset between clips, background motion restarting from zero, background extras returning to starting positions, frozen background extras, static distant people, living people rendered as scenery texture, duplicated extras, disappearing extras without occlusion, background extras watching protagonists, background extras reacting to laughter, background extras laughing with protagonists, synchronized background choreography; flat background plate, static reference image, animated wallpaper, fixed cloud sea, frozen cloud structure, frozen mist, static reflections, painted reflections, fake parallax, digital zoom instead of camera translation, foreground midground background moving at identical speed, environment freezing in close-up, environment freezing during dialogue, environment freezing when protagonists laugh, environment freezing after punchline, environmental event causing laughter, wind gust synchronized with laugh, cloud burst synchronized with joke, sunlight burst at punchline, mist revealing something at story beat, background solving the contest, camera following environmental motion instead of protagonists, new random architecture, scenery replacement, impossible geometry, extra foreground protagonists, modern elements, glitching cuts
```

#### 📌 Details
- Ratio: `1.78` | Duration: `20.07s`

---

### 🎬 顶层刺杀反杀
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11459.jpg" width="480" alt="SD2_11459"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/penthouse-assassin-takedown-SD2_11459">🌐 在线观看</a>

#### 📝 Prompt
```
0-3秒：行动启动：她站在一间超豪华的玻璃幕墙顶层休息室的吧台旁，俯瞰着霓虹闪烁的城市景观。听觉：舒缓的爵士乐被香槟酒瓶塞清脆的弹出声和高档水晶玻璃杯突然破碎的声音所干扰。视觉：她察觉到一名隐藏的刺客正从天鹅绒外套中拔出一把消音手枪；她立即抓起一个沉重的水晶醒酒器，将其扔过吧台，砸在他的脸上。3-6秒：近身格斗突袭 目标A：被玻璃碎片击中后踉跄了一下 → 她跃过抛光的红木吧台，扫倒他的支撑腿，将他的头猛地撞向硬木地板。目标B：手持伸缩电击棒逼近 → 她从落地窗帘上扯下一条丝绸窗帘带，在电击棒挥舞到一半时将其缠住他的脖子，将他勒到自己肩后。音效：低音强劲的休闲音乐、玻璃破碎声、身体撞击硬木地板的沉闷声响以及高压电火花噼啪作响的声音。6-8秒：服装及氛围细节：一件由祖母绿丝绸制成的露背晚礼服，开衩至大腿，佩戴厚重的金色手镯，涂着红色唇膏。环境：顶层公寓的天花板喷淋系统启动，温暖的雾气弥漫整个房间，在蓝紫色LED氛围灯的映衬下闪闪发光。8-11秒：擒抱目标C：用指节铜套拳击向她→她流畅地进入他的防御，抓住他挥拳的手臂，并用湿漉漉的丝绸窗帘绳将他的手臂绑在躯干上。目标D：从背后接近，手持电击枪→她迅速转身，将目标C被绑住的身体扭到目标D的攻击路线上，使电击枪的电极刺入目标C的夹克。 11-13秒：终结动作：她从架子上抓起一个沉重的黄铜香槟桶→旋转着像掷锤一样把它扔向守卫身后的落地玻璃墙。视觉效果：强化玻璃瞬间被风吹得四散开来，形成巨大的真空气流，将失去方向感的守卫们拉向敞开的窗台。13-15秒：余波氛围：上流社会的优雅被暴力摧毁，取而代之的是狂风肆虐的高空环境。动作：房间里充满了呼啸的狂风和雾气。她从吧台拿起手包，走过惊慌失措、手脚并用地逃跑的袭击者，镇定地走进私人服务电梯。音效：狂风呼啸着穿过破碎的玻璃框架的声音，随着沉重的黄铜电梯门滑关而瞬间消失。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 贵族少爷的误会
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11457.jpg" width="480" alt="SD2_11457"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/noble-master-misunderstanding-SD2_11457">🌐 在线观看</a>

#### 📝 Prompt
```
日式全彩动画风格。日式电视动画风格。赛璐珞风格动画。主要采用平涂色彩的动画风格截图。0-2秒：背景是18世纪的法国小镇。图1中戴着高顶礼帽的长发金发男子正在行走，似乎发现了什么，便躲到一栋建筑后面。2-4秒：图1中戴着高顶礼帽的长发金发男子从建筑后探出头的特写镜头，拍摄角度为斜侧。4-6秒：图2中黑发女仆面带微笑地与一位年轻的蔬菜商贩交谈。6-8秒：图2中黑发女仆的特写镜头，拍摄角度为斜侧。她闭着眼睛微笑，拳头放在嘴边，拳头背面朝向镜头。背景闪闪发光✨✨。 8-10秒：图1中戴着高顶礼帽、留着长发的金发贵族男性角色，脸上露出震惊的卡通式表情。糟糕。10-14秒：从这里开始，场景转移到宅邸内部。图3中的角色身处一个房间，因此穿着这样的衣服。图3中这位金发长发的贵族震惊得仿佛要吐出一个白色的灵魂。他疲惫地坐在沙发上，表情卡通，眼睛圆圆的，一片惨白。图2中的黑发女仆从屏幕右侧出现。黑发女仆问道：“少爷，怎么了？” 14-18秒：图3中金发长发男性角色低垂着脸的特写镜头，视角从下方斜角拍摄。“艾尔莎刚才和一个笑容灿烂的男人说话。”他掩饰不住自己的震惊。 18-22秒：图2中黑发女仆角色的斜侧视图。“如果你对她好，她会给你西红柿作为奖励。” 22-25秒：图3中的金发男角色抬起头，带着灿烂的笑容，从上方俯视。“什么，就这些？哦，我还以为……” 25-30秒：两人正面的合影。图3中的金发长发男角色坐在沙发上，抬头看着图2中的黑发女仆角色，而图2中的黑发女仆角色则站在他对面。图2中的黑发女仆角色：“我就知道？” 图3中的金发长发男角色：“不，没什么。” 他迅速转过脸去。
```

#### 📌 Details
- Ratio: `1.34` | Duration: `29.7s`

---

<!-- STATS_END -->
