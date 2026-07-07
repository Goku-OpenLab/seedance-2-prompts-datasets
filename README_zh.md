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
- 总 Prompt 数量：**5187**
- 今日更新（UTC 2026-07-07）：**26**

## 🎬 今日更新
### 🎬 夕阳骑行踹飞半挂
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05207.jpg" width="480" alt="SD2_05207"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sunset-cyclist-kicks-truck-SD2_05207">🌐 在线观看</a>

#### 📝 Prompt
```
生成一个第一人称，我正在骑自行车，在一个呃阳光明媚的下午有夕阳的那种马路上，我正在骑自行车，然后一辆嗯大运这个商用半挂开过来，然后想差点撞到我，然后我一脚把它给踹踹飞了。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 单车踹飞半挂车
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05206.jpg" width="480" alt="SD2_05206"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/biker-kicks-semi-truck-SD2_05206">🌐 在线观看</a>

#### 📝 Prompt
```
生成一个第一人称，我正在骑自行车，在一个呃阳光明媚的下午有夕阳的那种马路上，我正在骑自行车，然后一辆嗯大运这个商用半挂开过来，然后想差点撞到我，然后我一脚把它给踹踹飞了。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

### 🎬 黄昏里的强颜欢笑
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05205.jpg" width="480" alt="SD2_05205"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/fading-smile-dusk-breeze-SD2_05205">🌐 在线观看</a>

#### 📝 Prompt
```
首先生成一张女生近景图。参考这张图：画面先完全保持图片开始的状态。女生近景，站在黄昏风里，脸微微侧着，发丝被风吹到脸前，眼神安静，表情没有明显情绪。镜头是手持近景，有很轻的呼吸晃动，像摄影机已经开机但演员还没进入表演。画外传来很轻的一句：“好，开始。”听到这句话后，女生才开始表演。她慢慢把视线转向镜头，先露出一个很甜、很自然的笑，像是在努力让人放心。笑容很干净，嘴角柔和上扬，眼睛也跟着弯起来，前两秒完全看不出难过。风继续吹，几缕头发贴到脸上，她没有整理。笑容保持着，但眼神开始慢慢空掉一点。不是悲伤爆发，而是笑得太久之后，脸部肌肉有一点撑不住。嘴角还在笑，眼睛里的光却慢慢弱下来。最后两秒，她依然看着镜头微笑。只是鼻翼轻轻动了一下，喉咙像咽了一口气，眼眶有一点点湿，但不落泪。嘴角努力维持住甜笑，眼神却露出疲惫。最后她轻轻低一下眼，再抬眼，像把情绪重新压回去，3:4
```

#### 📌 Details
- Ratio: `0.56` | Duration: `13.04s`

---

### 🎬 一镜到底变装秀
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05204.jpg" width="480" alt="SD2_05204"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/one-take-outfit-change-SD2_05204">🌐 在线观看</a>

#### 📝 Prompt
```
单次连续长镜头（0：00–0：15）——UGC自拍，无缝服装+场景过渡 ×3，单镜头，无剪辑。格式：9分16秒的肖像，15秒，100%实时。参考资料：@img1 = 照片中的黑发女性——聚焦她的脸，修长的深棕色
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.15s`

---

### 🎬 超能武者巅峰对决
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05203.jpg" width="480" alt="SD2_05203"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/supernatural-martial-arts-clash-SD2_05203">🌐 在线观看</a>

#### 📝 Prompt
```
@[character1 ref]和@[character2 ref]之间的超自然武术决斗，伴随着气场爆发和强烈的冲击效果。16拍。开场即时行动，保持不断升级的势头，最终以决定性的最终冲击收尾，没有缓慢的引入或冷却。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.03s`

---

### 🎬 机场货运生死时速
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05202.jpg" width="480" alt="SD2_05202"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cargo-terminal-escape-chase-SD2_05202">🌐 在线观看</a>

#### 📝 Prompt
```
超现实的电影动作场面 晚安。在一个巨大的未来机场货运航站楼内，两名特工，一男一女，在高速行李和货物处理区飞驰而过，而安保团队紧随其后。环境宽敞明亮且工业化：巨大的移动行李输送带、不同高度的货物传送带、机器人装卸臂、滚动集装箱、金属平台、闪烁的警示灯以及自动关闭的大型货舱门。两名特工都穿着深色合身战术服装，没有兜帽、头盔、面具，头发可见，没有明星相似之处。 宽广开场镜头：两名特工全速冲进货运区，保安紧随其后。传送带向不同方向移动，行李和货物箱滑过，机械臂在头顶摆动。 跟踪镜头：特工们沿着移动的传送带奔跑，然后跳到另一条高度不同的传送带上。他们穿梭于滚动的行李箱之间，躲过一只机械臂摆动到位。安保团队紧随其后，努力跟上移动的机械。 侧射：追逐变得更加激烈。一名特工滑过装满行李的传送带，另一名则翻越低矮的货物隔板。一只机械臂将一个货箱放到他们面前，迫使他们迅速改变方向。警告灯闪烁红光，远处一个大型货舱出口开始关闭。 最后5秒：节奏急剧加快。特工们冲过最后一组移动传送带，跳过传送带间的狭窄缝隙，穿过最后一个机械臂，并在货舱门关闭前迅速穿过狭窄的通道。随着安全队在传送带上耽搁，行李和货物箱在他们身后翻滚。 最后一刻：两名特工重重落在货舱门的另一侧，转身一瞬间，机械仍在密封门后运转。 风格：超写实、电影感、节奏明快、紧张、清晰易读的动作，强烈的运动感和紧迫感，机场货运航站楼，移动的传送带，机械臂，闪烁的警示灯，动态但清晰的镜头运动，无文字，无标志，无卡通风格。保持比例。保持风格和特征。宽高比为16：9。
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

### 🎬 拉面女侠战忍者
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05201.jpg" width="480" alt="SD2_05201"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ramen-warrior-ninjas-SD2_05201">🌐 在线观看</a>

#### 📝 Prompt
```
第一部分（0：00–0：15） 剪辑1（0：00–0：05）——偷偷穿过市场 1920年代大阪市场，Betamax胶片风格。雪悄悄踮着脚穿过拥挤的摊位，袖子遮住嘴，眼睛扫视着。她看到一家拉面店，咧嘴一笑，冲过了可伦帘子。 剪辑2（0：05–0：10）——拉面终于 在热气腾腾的拉面店里，雪兴奋地点了一份加了猪肉和鸡蛋的巨型豚骨拉面。当热腾腾的碗端上来时，她坐下，微笑着举起筷子，像挥剑一样。 第三节剪辑（0：10–0：15）——忍者伏击 三名魁梧的忍者状恶棍注意到她，戴上面具，突然发动攻击。桌子在他们跳跃时四散飞落。雪一边保护拉面一边翻身，正吸着拉面，脸上带着恼怒的怒视。 第二部分（0：15–0：30） 第四节剪辑（0：15–0：20）——面条辩护 忍者投掷手里剑。雪立刻用筷子拉开一根拉面接住了它，然后轻松以武术般的敏捷闪避忍者的攻击。 第五节剪辑（0：20–0：25）——人之术 雪站稳脚步，念道：“男之术！”发光的拉面从碗中升起，呼啸穿过店铺，缠绕着三名忍者，将他们绑在一起。 切入6（0：25–0：30）— 碗赛结束 纠缠的忍者们踉跄着，撞成一团。雪高高跃起，三重撞击地把空拉面碗砸在他们头上。定格在她那凶狠的撅嘴脸上，金红相间的发簪在灯笼光下闪闪发光。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.13s`

---

### 🎬 巨鳄袭车火箭歼灭
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05200.jpg" width="480" alt="SD2_05200"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/giant-crocodile-rocket-blast-SD2_05200">🌐 在线观看</a>

#### 📝 Prompt
```
一条明亮的白天村路，两侧都是小房子。一辆大型水罐车正沿路行驶。一只巨大的鳄鱼，像卡车一样大，咬住水罐车后部，猛地拉扯。在附近一栋建筑的屋顶上，一名士兵手持火箭发射器。声音：卡车引擎轰鸣，金属撞击声，人群喊叫，鳄鱼咆哮。 镜头1（0–3秒）——THE HOOK：我们看到水罐车剧烈摇晃。这只超级鳄鱼嘴巴紧咬卡车后部，左右拉扯着它。水花四溅。司机害怕，在无线电里喊道：“它抓住我的卡车了！” 镜头2（3–6秒）：在附近一栋建筑的屋顶，士兵准备拿起火箭筒。他仔细观察，但还没开枪——司机还太近了。他在广播里说：“跳出来！快跑！” 镜头3（6–9秒）：司机打开车门跳下卡车。他沿着路飞快地跑。鳄鱼松开卡车，驶上开阔的道路，追赶他。现在鳄鱼独自一人在开阔地带。 镜头4（9–13秒）——慢速时刻：鳄鱼现在出现在开阔的道路上。士兵从屋顶发射火箭筒。我们看到慢动作——烟雾冒出，火箭飞向鳄鱼。 第五镜头（13–15秒）：一切恢复正常速度。砰！火焰和烟雾从鳄鱼所在处喷涌而出。卡车静静地停着，安全无虞。司机从远处回头看，安全无虞。烟雾升上天空。停。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.88s`

---

### 🎬 巨蛇缠船惊魂记
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05199.jpg" width="480" alt="SD2_05199"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/giant-snake-boat-attack-SD2_05199">🌐 在线观看</a>

#### 📝 Prompt
```
一条两岸都是绿色树木的河流，阳光明媚。一艘小船在水面上移动。一条巨蛇缠绕着船，紧紧夹住。河岸上，一名士兵正在装填枪支。声音：水花声、船引擎声、蛇嘶嘶声、人们喊叫声。 第一枪（0–3秒）——钩子：巨蛇紧紧缠绕着船。船身左右倾斜。司机抓紧，在无线电上喊道：“它在挤我们！” 第二枪（3–6秒）：在河岸上，士兵手持枪械，准备就绪。他等待——还不能开枪，蛇离船太近了。他说：“割断网！现在就去！” 第三镜头（6–9秒）：船夫拿起刀割断绑着大而沉重网的绳索。网落下——蛇也随之落下！它从船上掉下来，落在了开阔的水域。现在蛇孤身一人，暴露在外。 第四次镜头（9–13秒）——大慢速时刻：蛇现在进入了开阔水域。士兵从银行开枪。我们看到它缓慢——烟雾冒出，子弹迅速飞过水面，直击蛇身。 第五镜头（13–15秒）：一切恢复正常速度。砰！水花溅起，蛇被击中的地方高处溅起。船只在水面上安全漂浮。司机回望着他，既开心又安全。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `11.88s`

---

### 🎬 动漫少女闯关竞技场
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05198.jpg" width="480" alt="SD2_05198"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/anime-girl-retro-arena-SD2_05198">🌐 在线观看</a>

#### 📝 Prompt
```
{ “风格”：“真实的1990年代初英国周六晚ITV播出风格，对《角斗士》竞技场画面的真实还原，巨大的室内体育馆配备霓虹灯具和泡沫挥舞的观众，广播视频质感带有轻微晕花，充满电力般的氛围。” “main_character”：“Q版动漫贴纸角色，平面2D贴纸纹理，粗体卡通轮廓，纸剪手感。她有一头金色长发，刘海直垂，眼睛是大大的紫色圆眼睛。她穿着一套简单的红白运动服，配有白色头盔和护膝。她的动作在与真实环境互动时，仍保留了略显夸张的贴纸感。” “shots”： [ { “时间”：“0-3秒”， “镜头”：“广角场馆镜头”， “描述”：“Q版动漫贴纸女孩冲向旅行者——一条陡峭向上的传送带，快速向下冲刺。观众欢呼，霓虹竞技场灯光扫过舞台。” }, { “时间”：“3-6”， “摄像机”：“低角度跟踪镜头”， “描述”：“她跳上腰带，全速冲刺攻击。她一度领先，长长的金发飘扬，随着皮带在脚下发出哀鸣声，她向前推进。 }, { “时间”：“6-9”， “camera”：“侧中镜头”， “描述”：“她的步伐变短——腰带获胜。她拼尽全力奔跑，缓缓向后滑行，双臂乱挥，紫色的大眼睛从专注转为惊慌。” }, { “时间”：“9-12秒”， “摄像机”：“带动态模糊的特写镜头” “描述”：“她四肢着地，爪子抓着橡胶表面，拼命爬行，最后被拖下去，吐到防撞垫上，成堆了。” }, { “时间”：“12-15秒”， “camera”：“手持跟拍镜头”， “描述”：“她躺在垫子上，胸口起伏，一只手臂无助地竖起大拇指，铃声响起，暂停声响起。旅行者在她身后得意地嗡嗡作响。框架稳住。” } ], “technical_details”：“高保真逼真的真人画面，风格类似90年代初英国竞技场竞技节目。精准的传送带跑步机物理效果、霓虹竞技场灯光和连贯的角色动作。主角保持平面2D动漫贴纸风格，环境和物理效果保持真实。” “negative_prompt”：“模糊、低质量、变形角色、额外肢体、文字、水印、标志、过曝、欠曝、现代伪影、3D渲染角色” }
```

#### 📌 Details
- Ratio: `1.78` | Duration: `30.03s`

---

### 🎬 韩系晨间精致出门准备
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05197.jpg" width="480" alt="SD2_05197"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-morning-grwm-routine-SD2_05197">🌐 在线观看</a>

#### 📝 Prompt
```
制作一段逼真的GRWM（与我一起准备）生活方式视频，展现一位时尚的韩国女性，拥有长长的柔顺黑发、光彩照人的肌肤和清新自然的外貌。明亮现代公寓，落地窗，温暖的晨光，斯堪的纳维亚风格的装饰，高端时尚Vlog美学，电影感十足的手持摄像机，超写实摄影。 视频开场，她坐在床边。她轻轻一笑，伸了个懒腰，走向窗户，拉开窗帘，温暖的金色阳光洒满房间。她整理好床铺，然后走向梳妆台。 她开始使用洁面乳、爽肤水、精华液、保湿霜和润唇膏进行清爽护肤程序。特写美妆照突出光泽肌肤，自然阳光透过房间反射。 接着，她用卷发棒将头发梳成柔软松散的波浪，轻柔地梳理卷发，使其妆效顺滑。她会化轻盈的日常妆容，包括粉底、腮红、睫毛膏、柔和眼线和光泽粉色唇彩，自然地对着镜子微笑。 她走向衣柜，打开衣柜，比较了几套衣服，然后选了一件粉色合身短款上衣和高腰蓝色牛仔裤。她换上衣服，调整合身度，还戴上了小巧的金色圈耳环、一条精致的项链、一块手表和太阳镜。 她喷上最喜欢的香水，穿上白色运动鞋，拿起一个小单肩包，从厨房台面拿了一杯冰咖啡。 站在全身镜前，她从不同角度检查自己的穿着，带着微笑转了一圈，然后快速拍了张镜子自拍。 视频结束时，她打开公寓门，走到明亮的晨光中。镜头跟随她，她自信地走在宁静的树荫大道上，手里拿着冰咖啡，最后以电影般的拉回镜头收尾。 风格：高端GRWM时尚视频，奢华生活内容，温暖自然光，温馨公寓美学，真实手持和云台摄影，柔和电影色彩分级，照片级真实优雅的过渡，浅景深，4K HDR，16：9宽屏，无字幕，无文字叠加。
```

#### 📌 Details
- Ratio: `1.73` | Duration: `15.07s`

---

### 🎬 巨鳄袭车狙击救援
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05196.jpg" width="480" alt="SD2_05196"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/soldier-saves-bus-crocodile-SD2_05196">🌐 在线观看</a>

#### 📝 Prompt
```
白天的一条路。一辆普通公交车开着车，车里有人。一只大鳄鱼咬了公交车的后部。附近的一座山丘上，一名士兵手持一把大枪。声音：公交车引擎声、人群喊叫、鳄鱼咆哮。 镜头1（0–3秒）——钩子：大鳄鱼咬住了公交车的后部。公交车剧烈晃动。里面的人尖叫。司机在无线电上喊道：“它咬着公交车了！” 第二枪（3–6秒）：在山丘上，士兵举起大枪准备。他仔细观察，但还没开枪。公交车离鳄鱼太近了。他说：“现在转身！走开！” 镜头3（6–9秒）：公交司机快速转动方向盘。公交车从鳄鱼嘴里逃脱了。大鳄鱼独自跑上开阔的道路，紧追不舍。 镜头4（9–13秒）——大缓慢时刻：鳄鱼现在独自一人在开阔的道路上。山上的士兵开枪。我们看到它很慢。冒烟。枪声飞向鳄鱼。 第五镜头（13–15秒）：一切恢复正常速度。砰！鳄鱼所在的地方起了大火。公交车安全，开走了。里面的人回头看，既快乐又安全。烟雾升上天空。停。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.88s`

---

### 🎬 本漫游纽约时代广场
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05195.jpg" width="480" alt="SD2_05195"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ben-nyc-times-square-vlog-SD2_05195">🌐 在线观看</a>

#### 📝 Prompt
```
请使用附图作为本的确切身份。保持相同的面部、发型、眼睛、下颌线、胡茬、皮肤质地、年龄、声音、体型、服装、个性和举止。没有表情滑动。身份没有变化。所有片段都是同一个人。现实的美国旅行视频博主。纪录现实主义。地道的纽约氛围。自然的人群行为。逼真的语音和对嘴。英语。自动字幕与语音对话匹配。高端旅游视频日志。频繁切换镜头角度。” 片段1（0：00–0：15） 0：00–0：03 自拍，时代广场，本身后。 本：“大家好，我叫本。欢迎回到另一个视频日志。” 0：03–0：06 镜头转向巨型屏幕。 本：“今天我就在纽约市中心，站在时代广场。” 0：06–0：09 观众镜头。 本：“这个地方我旅行清单上已经有好几年了。” 0：09–0：12 回到本。 Ben：“这里的能量真是难以置信。” 0：12–0：15 向前走。 本：“我们一起去探索一天吧。” 片段2（0：15–0：30） 0：15–0：18 视角行走。 本：“你首先注意到的是声音。” 0：18–0：21 出租车通过。 本：“汽车、音乐、对话。” 0：21–0：24 街头表演者可见。 本：“每隔几步就有点事发生。” 0：24–0：27 公告牌拍摄。 本：“你能感觉到城市在你周围流动。” 0：27–0：30 观众镜头。 本：“这里根本不会无聊。” 片段3（0：30–0：45） 0：30–0：33 仰望天空。 本：“看看这些屏幕。” 0：33–0：36 巨型LED广告。 本：“有些比整栋楼还高。” 0：36–0：39 下方交通情况。 本：“数百万人经过这里。” 0：39–0：42 游客拍照。 Ben：“每个人都在努力捕捉那一刻。” 0：42–0：45 全城镜头。 本：“我完全理解为什么。” 片段4（0：45–1：00） 0：45–0：48 步行镜头。 Ben：“我喜欢纽约的一点就是多样性。” 0：48–0：51 不同的人。 本：“来自世界各地的人们。” 0：51–0：54 街头小吃车。 本：“不同的文化。” 0：54–0：57 店面。 本：“不同的故事。” 0：57–1：00 本短暂出现。 本：“大家都住在同一条街上。” 片段5（1：00–1：15） 0：00–0：03 打开出租车门。 本：“我们去市中心吧。” 0：03–0：06 进入黄牌出租车。 本：“没有什么比这里更像纽约了。” 0：06–0：09 出租车移动。 本：“经典的黄色出租车。” 0：09–0：12 窗户视图。 本：“这是参观城市的完美方式。” 0：12–0：15 街道经过。 本：“让我们好好享受这段旅程吧。” 片段6（1：15–1：30） 出租车内部。 Ben 谈到了建筑、老建筑、摩天大楼，以及曼哈顿如何将历史与现代设计相结合。 片段7（1：30–1：45） 出租车窗户的视角。 本谈到人们匆忙赶往工作岗位，以及城市似乎从未放慢脚步。 第8段（1：45–2：00） 出租车到达目的地。 本走出去，说尽管在同一个城市，每个社区感觉完全不同。 片段9（2：00–2：15） 走过一个小公园。 本注意到一只友善的猫。 本：“你好啊，小家伙。”
```

#### 📌 Details
- Ratio: `1.78` | Duration: `205.03s`

---

### 🎬 金发少女走廊激战
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05194.jpg" width="480" alt="SD2_05194"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/blonde-schoolgirl-hallway-brawl-SD2_05194">🌐 在线观看</a>

#### 📝 Prompt
```
这是一场充满活力、充满活力的电影动作戏，发生在美国高中走廊里。一位强悍美丽的西部女子，留着长长的波浪金发，穿着印有校徽的浅粉色校服西装外套，白衬衫，条纹领带，百褶格子裙，黑色及膝袜和鞋子，她独自一人在激烈的走廊混战中与多名男性袭击者搏斗。 她动作极快、敏捷且具备武术技巧——旋转、施展强力高踢、拳击和流畅连击，将高大男子击飞进储物柜，撞击墙壁，最终摔倒在地。纸张散落在光滑的地板上。男人们一个接一个被击倒或击败，她则穿过走廊。 镜头极具动态感：低角度跟踪镜头、快速平移、她坚定面容和飘逸金发的戏剧性特写、混乱的广角镜头，以及紧张的肩膀后镜头。电影般的灯光和头顶荧光灯、快速动作时的真实运动模糊、戏剧性的甩发效果和强烈的面部表情。她看起来强大、自信，到最后略显气喘吁吁，站在倒下的对手中，目光专注地直视前方。 真实的真人演出风格，高细节，紧凑的编排类似动作电影打斗场面，时长14秒，16：9画面比例。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 竞技场时空裂隙巨龙现世
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_05193.jpg" width="480" alt="SD2_05193"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/arena-time-gate-dragon-invasion-SD2_05193">🌐 在线观看</a>

#### 📝 Prompt
```
请以@[参考图片]作为巨大圆形银色竞技场门、两尊巨型国王雕像、拥挤的观众、明亮的白天、高耸的白色塔楼，以及观众席内智能手机视角的主要参考。
一段连续水平的智能手机视频，来自一位惊恐的旁观者。镜头自然摇晃、平移、向上倾斜、向后踉跄、头部、手机、尘土、旗帜和奔跑的人群后方的构图丢失。没有剪辑，没有界面，没有时间戳，没有字幕，没有音乐。
在一个巨大的银白色未来竞技场中，圆形时间之门最初关闭，柔和地散发着蓝白色的能量。观众安静、紧张，正在拍摄。突然，城门周围的古老符文一个接一个地亮起。一阵低沉的嗡鸣震动了广场。尘埃升起，旗帜断裂，一个受控的蓝白色时间漩涡在封闭的门面形成。
漩涡旋转加速，压缩成一道垂直的光裂缝，随后伴随着剧烈冲击波撕裂。D1，一条宽角龙，直冲镜头飞来。人群尖叫着，陷入恐慌，人们躲避、跌倒、掉落手机、推搡、四处奔跑。镜头猛地向左转，D1低空飞越人群。长颈天空巨蛇D2从其后出现。镜头回到仍在发光的大门，D3——一只重甲龙龙——强行冲出开口，紧随其后的是D4，一条狭长翅膀的刀刃状巨龙，在空中划破。这扇门始终保持活跃、明亮且不稳定。
最后，最大的龙D5用发光的眼睛、巨大的爪子、装甲胸膛和巨大的翅膀填满了整个圆形大门。它冲向天空，蔓延得比大门还宽，在竞技场上方咆哮，然后喷出一道巨大的金橙色火焰，横扫天空。蓝白色的城门灯与橙色火光交织，照亮雕像、塔楼、旗帜、尘埃和逃散的人群。视频以D5主宰天空结束，时间之门仍在其后发光。
反提示：没有银河门户，没有太空隧道，没有可见的异世界，没有星门关闭，没有龙行走或降落，没有平静的人群，没有干净的电影镜头，没有无人机镜头，没有字幕，没有界面，没有时间戳，没有音乐。
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

<!-- STATS_END -->
