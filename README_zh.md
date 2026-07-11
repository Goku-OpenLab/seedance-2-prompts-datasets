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
- 总 Prompt 数量：**7539**
- 今日更新（UTC 2026-07-11）：**0**

## 🎬 今日更新
### 🎬 飞鸟幻形
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10084.jpg" width="480" alt="SD2_10084"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/birds-morph-dissolve-SD2_10084">🌐 在线观看</a>

#### 📝 Prompt
```
视频中的鸟儿们根据图片中的图像，大致组成了一个并不完美的鸟形。它们随着音频中的音乐舞动，并在飞翔中消散。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `8.25s`

---

### 🎬 公寓灯光随音乐起舞
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10083.jpg" width="480" alt="SD2_10083"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/apartment-lights-music-sync-SD2_10083">🌐 在线观看</a>

#### 📝 Prompt
```
公寓的灯光随着音乐同步亮起。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 蜜蜂化萤火
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10082.jpg" width="480" alt="SD2_10082"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/bee-to-fireflies-SD2_10082">🌐 在线观看</a>

#### 📝 Prompt
```
把蜜蜂变成一小群萤火虫。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 小提琴肩后视角
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10080.jpg" width="480" alt="SD2_10080"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/violinist-over-shoulder-SD2_10080">🌐 在线观看</a>

#### 📝 Prompt
```
把摄像机角度改成小提琴手肩膀后方。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 隐形小提琴
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10079.jpg" width="480" alt="SD2_10079"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/invisible-violin-SD2_10079">🌐 在线观看</a>

#### 📝 Prompt
```
让小提琴隐形
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 小提琴手影像穿越
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10078.jpg" width="480" alt="SD2_10078"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/violinist-image-transport-SD2_10078">🌐 在线观看</a>

#### 📝 Prompt
```
将小提琴手带入影像环境
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.0s`

---

### 🎬 机甲女神翱翔云海
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10077.jpg" width="480" alt="SD2_10077"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/armored-heroine-golden-clouds-SD2_10077">🌐 在线观看</a>

#### 📝 Prompt
```
镜头 1（8 秒）一位强大的女性角色。电影级广角镜头，她翱翔在金黄色云海之上，夕阳的暖橙色光线映照着薄雾，场面壮观而富有戏剧性。风吹拂着她的头发和衣物，展现出高度的物理真实感。来自四面八方的未来感十足的流线型机械装甲部件——胸甲、肩甲、臂铠、腿甲和一顶发光的头盔——高速飞来，拖曳着鲜艳的光迹和青色的引擎尾气。每个部件都...
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 赤龙出海风暴狂舞
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10076.jpg" width="480" alt="SD2_10076"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/red-dragon-storm-fury-SD2_10076">🌐 在线观看</a>

#### 📝 Prompt
```
一头狂暴的红色巨龙（元素）从海中腾空而起，以极快的速度在船上方盘旋飞舞，激起巨大的海浪。 动态镜头跟随巨龙穿过风暴，在巨浪中翻腾远去。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 剪纸斋月延时
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10075.jpg" width="480" alt="SD2_10075"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ramadan-paper-cut-zoom-lapse-SD2_10075">🌐 在线观看</a>

#### 📝 Prompt
```
通过高度精细的剪纸艺术，无缝无限变焦超延时摄影，捕捉从斋月到开斋节庆祝的旅程。场景始于封斋饭时间，宁静的街区上空悬挂着一轮皎洁的弯月，柔和的灯笼光影摇曳。镜头拉近一扇屋窗，一家人正在准备封斋饭，随后平稳过渡到快节奏的日常斋戒时刻超延时摄影——人们工作、祈祷，等待开斋。 镜头继续拉近，日落时分，街道上挤满了小吃摊贩和人群...
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 办公室巨龙喷火解雇员工
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10074.jpg" width="480" alt="SD2_10074"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/office-dragon-fires-employee-SD2_10074">🌐 在线观看</a>

#### 📝 Prompt
```
快速剪辑：一条超逼真的“办公室巨龙”在多个办公室房间里高速飞过，穿梭于人群之间、越过办公桌、绕着人们，在一个繁忙的格子间办公室里。它降落在一个人面前的桌子上，向那名男子喷射火焰。巨龙说：“你被解雇了。”
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 全球女将铠甲变身
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10073.jpg" width="480" alt="SD2_10073"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/global-female-armor-transformations-SD2_10073">🌐 在线观看</a>

#### 📝 Prompt
```
核心场景提示词 @94d74b42-17ec-45d3-ab60-487c3a1700cb 12 秒内完成 10 套全球女性盔甲变身。全程无眼镜，全盔甲头盔 + 武器，纯女性将军造型。所有转场均包含发光粒子特效。风格统一为高端、写实、震撼。按时间段划分的场景： 0-1 秒：中国红金明光铠 + 鎏金战盔，手持鎏金长矛，抬...
```

#### 📌 Details
- Ratio: `0.56` | Duration: `5.04s`

---

### 🎬 橙色汽水活力飞溅
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10072.jpg" width="480" alt="SD2_10072"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/orange-soda-splash-SD2_10072">🌐 在线观看</a>

#### 📝 Prompt
```
一个充满活力的橙色汽水罐，周围环绕着飞溅的柑橘切片和闪闪发光的水滴，慢动作呈现，明亮而充满活力的灯光，高细节商业摄影。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 巨猫降临重庆城
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10070.jpg" width="480" alt="SD2_10070"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/giant-cat-chongqing-SD2_10070">🌐 在线观看</a>

#### 📝 Prompt
```
【风格】伪纪录片，手机 Vlog 视角，超现实 CG 结合真实场景，8K 画质，完美的毛发物理模拟。 【时长】15 秒 【场景】重庆洪崖洞或繁忙的立交桥路口（具有魔幻 8D 城市感）。 [00:00-00:05] 镜头 1：视觉奇观（揭示）。 画面显示一条熙熙攘攘的城市街道。镜头抬升，展现一只**哥斯拉大小的白色虎斑猫...
```

#### 📌 Details
- Ratio: `0.56` | Duration: `5.04s`

---

### 🎬 装甲狒狒血洗马赛村
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10069.jpg" width="480" alt="SD2_10069"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/armored-baboon-marseille-village-SD2_10069">🌐 在线观看</a>

#### 📝 Prompt
```
一只身披盔甲的巨大狒狒冲过一个燃烧的马赛村庄，它抓起一名马赛战士，将其扔进一间着火的茅屋，马赛战士们在一片火海和废墟中惊恐地四散奔逃。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

### 🎬 树洞里的暖心黄昏
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_10068.jpg" width="480" alt="SD2_10068"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cozy-hollow-golden-dusk-SD2_10068">🌐 在线观看</a>

#### 📝 Prompt
```
格式：15 秒 / 6 镜头 / 暖心森林喜剧 / 简短对话 风格：超现实电影级森林动画，温暖的金色夕阳透过树皮裂缝洒下，树洞内长满苔藓，温馨舒适
```

#### 📌 Details
- Ratio: `1.78` | Duration: `5.04s`

---

<!-- STATS_END -->
