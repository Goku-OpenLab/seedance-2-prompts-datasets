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
- 总 Prompt 数量：**2735**
- 今日更新（UTC 2026-05-11）：**243**

## 🎬 今日更新
### 🎬 篮球攻防全流程电影级故事板
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02754.jpg" width="480" alt="SD2_02754"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/defense-to-dominance-basketball-storyboard-SD2_02754">🌐 在线观看</a>

#### 📝 Prompt
```
打造一支高质量4K电影级篮球故事板，完整呈现从防守到强力得分的全流程，运用动态场馆灯光、戏剧性观众氛围和专业体育转播风格。开场聚焦半场激烈对抗：防守者干净利落地完成抢断或封盖，篮球被精准拍飞，慢镜头捕捉汗水与运动粒子。随即切入快攻：球员夺回球权，运球疾驰中保持速度与掌控，通过快速变向和脚步动作甩开防守者。特写镜头展现球鞋抓地细节、篮球有节奏的弹跳以及专注的面部表情，穿插球场空间开阔的全景画面。关键助攻时刻：篮球在防守队员间犀利传递，随后球员冲向篮筐，观众席随之沸腾。慢镜头逼近油漆区，最终以强力终结——高冲击力扣篮、流畅上篮或干净跳投收尾。篮球应声入网或篮筐剧烈震颤，同时捕捉防守方与观众的反应。全程融入真实背景音效：硬木地板上球鞋的摩擦声、运球回响、球员呼喊、裁判哨音、观众低语渐变为震耳欢呼、解说员式远景激情解说，以及关键节点（抢断、快攻、绝杀球）不断强化的场馆混响。结尾以情感爆发收束：得分者回跑、握拳怒吼或高举双臂，队友簇拥而至，场馆灯光闪耀，观众彻底沸腾。运用多角度镜头（全景、跟拍、特写、第一人称、慢动作），强化动态模糊与真实物理效果（篮球弹跳、球鞋摩擦、身体动作），突出从防守掌控到进攻统治的胜利蜕变。
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.07s`

---

### 🎬 玻璃唇精华秒变
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02753.jpg" width="480" alt="SD2_02753"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/lumiera-seoul-glass-glow-lip-elixir-ad-SD2_02753">🌐 在线观看</a>

#### 📝 Prompt
```
基础设定：“高端化妆品店内超写实快节奏TikTok风格美妆广告。明亮灯光、镜面反光、潮流美学。一位皮肤透亮、身着现代服饰的时尚韩国女孩。快速剪辑、动态运镜、病毒式编辑风格、4K画质。” ⏱️ 0:00 – 0:02（钩子——吸引眼球）——女孩进店时快速推近镜头——彩色美妆货架闪切 🎙️ 屏幕文字：“等等——这改变了一切 💄✨” 🎧 音效：热门TikTok节拍骤降 ⏱️ 0:02 – 0:05（快速购物蒙太奇）——快速剪辑：• 抓取产品 • 将商品扔进购物车 • 手扫过货架的特写 🎙️ 文字：“试遍所有产品…” ⏱️ 0:05 – 0:07（发现时刻）——突然慢动作对比——聚光灯打在唇彩上——产品标签清晰可见：“LUMIÉRA Seoul – 玻璃光泽唇部精华” 👩 女孩（兴奋低语）：“等等……这个？” ⏱️ 0:07 – 0:10（转变上妆）——快速镜子转场——唇彩涂抹的快速特写——瞬间呈现光滑光泽 🎙️ 文字：“天哪 😳” 👩 女孩：“好吧……哇哦。” ⏱️ 0:10 – 0:13（效果+美妆镜头）——快速美学剪辑：• 嘴唇发光 • 甩发 • 自信表情 🎙️ 文字：“几秒打造玻璃唇 ✨” ⏱️ 0:13 – 0:15（产品特写+行动号召）——快速推近产品——干净奢华的产品镜头 🎙️ 画外音：“LUMIÉRA Seoul – 玻璃光泽唇部精华。” 🎙️ 屏幕文字：“立即入手 🔥”——节拍骤降结束 剪辑风格：快速剪辑、跳跃转场、速度渐变、推近镜头、闪光转场 运镜风格：手持拍摄+快速推近+微距美妆镜头 音效：热门TikTok音频，节拍骤降与剪辑同步 氛围与风格：潮流、上瘾、高能量、病毒式美妆广告 现代Z世代美学，极致精致，4K画质
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.2s`

---

### 🎬 超写实变身战斗
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02752.jpg" width="480" alt="SD2_02752"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/golden-lightning-impact-strike-SD2_02752">🌐 在线观看</a>

#### 📝 Prompt
```
超写实电影级动作，物理真实感，IMAX电影质感，4K-8K HDR，高对比度，深邃阴影，自然皮肤纹理，细微胶片颗粒，35mm变形镜头（f/2.8）。无过度光晕，无多余辉光。能量表现为气压扭曲+细密金色电光（锐利、间歇性）。镜头：动态手持跟拍，快速追踪，甩镜，冲击震动，自然动态模糊。场景（连续10秒）：一名身穿白色背心与黑色长裤的瘦削男子立于龟裂地面。0-2秒：手持镜头快速推进。身体绷紧，青筋浮现，呼吸沉重。双手与肩部浮现细小金色电火花。尘土开始震颤。2-4秒（快速变身）：肌肉逐渐膨胀至运动员体格（非瞬间切换）。发丝竖起并转为金色。地面裂纹呈放射状扩展，碎石浮起四散。空气产生微妙扭曲。一道短促微型冲击波将尘土向外推散。镜头：快速环绕+轻微抖动。4-6秒（锁定目标）：前方显现一只人形触手怪物。触手沉重地猛烈挥舞。角色凝聚力量，身体微向前倾，随即爆发高速冲刺（真实动态模糊）。镜头：极致甩镜，几乎丢失主体。6-8秒（冲击打击）：角色瞬间闪现至怪物面前。一记重拳击中躯干/头部。特效：沉重打击感（血肉+质量感），接触点短暂金色电光爆发，气压冲击，脚下尘土炸开。镜头：冲击变焦+剧烈抖动+接触帧轻微慢动作。8-10秒（击飞→撞山）：怪物被远远击飞，拖曳一道尘迹。切至远景：怪物撞入山壁，岩石崩塌，大块碎石坠落（真实落石效果，无能量爆炸）。切回近景：角色静立，运动员体格，金色发丝。细微残余电光闪烁。尘埃落定。撞击后的寂静。
```

#### 📌 Details
- Ratio: `2.34` | Duration: `15.13s`

---

### 🎬 女战士能量箭炸裂
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02751.jpg" width="480" alt="SD2_02751"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/fierce-warrior-unleashes-energy-arrow-SD2_02751">🌐 在线观看</a>

#### 📝 Prompt
```
一段电影感十足的快节奏动作场景，起始于一位黑发、面部带有银色金属纹路的凶猛女战士特写，她正瞄准一把发着蓝光的能量弓与箭。镜头切换至她棕色眼眸的极端特写，一个未来风格的橙色数字瞄准准星在她的瞳孔上激活。接着，画面切至过肩广角镜头，展现她立于高耸岩石悬崖之上，俯瞰着阳光照耀的沙漠峡谷，那里有一支由黑暗怪物组成的大军正在行进。她松开那支发光的蓝箭，箭矢在半空中分裂成数道耀眼的能量光束。镜头迅速追踪着主蓝色光束，它沿着峡谷疾速飞向怪物群，最终在怪物中引发了一场由厚重尘土与碎片构成的巨大爆炸冲击。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.23s`

---

### 🎬 日本女摔角冠军决战
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02750.jpg" width="480" alt="SD2_02750"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/japanese-women-wwe-championship-finale-SD2_02750">🌐 在线观看</a>

#### 📝 Prompt
```
制作一段超写实、电影感的15秒连续镜头，展现一场WWE风格的冠军决赛，由两位体能出众的日本女摔跤手在座无虚席的体育馆中对决。遵循精确的比赛进程：疲惫对峙→爆发式晾衣绳攻击→降服技缠斗→DDT反击→近身压制→德式背摔→上绳月面宙返终结技→干净利落的三秒压制→冠军庆祝（腰带、彩纸、角落烟火）。保持角色形象一致，并匹配擂台服装。强调真实的汗水、冲击物理效果、观众能量，以及关键动作的戏剧性慢动作。结尾以升起的吊臂镜头捕捉胜利者的姿态。输出应如同WWE直播现场——照片级真实、高对比度、60帧每秒。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.13s`

---

### 🎬 15秒奢华美容霜广告
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02749.jpg" width="480" alt="SD2_02749"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/luxury-beauty-cream-ad-SD2_02749">🌐 在线观看</a>

#### 📝 Prompt
```
Seedance 2.0 – 15秒美容霜广告视频提示 制作一段15秒竖屏（9:16）超写实电影级美容霜广告视频。 场景：一位年轻女性身处整洁现代的梳妆台或柔和工作室风格的浴室中。环境明亮优雅、简约，采用柔和粉彩色调，营造奢华护肤氛围。 风格：高端护肤品广告，超写实，流畅的电影级布光，柔焦效果，高端美妆品牌美学。 快速剪辑序列： 0–4秒：特写女性在柔和自然光下洁净透亮的肌肤 4–8秒：她以流畅动作将美容霜轻柔涂抹于面部 8–12秒：肌肤更显光彩焕新，镜中浮现自信微笑 12–15秒：产品罐置于洁净台面的主角镜头，背景泛光 旁白（轻柔舒缓语调）： “唤醒你的自然光泽……以纯净轻盈的日常呵护。” 灯光：柔和漫射白光，肌肤上呈现细腻高光，温暖洁净色调。 音乐：轻柔舒缓的美容广告配乐，轻钢琴搭配空灵环境音。 氛围：清新、优雅、自信，奢华护肤质感。 结尾文字（可选）： “光泽始于呵护。”
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.05s`

---

### 🎬 独行杂货店
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02748.jpg" width="480" alt="SD2_02748"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/grocery-aisle-memories-SD2_02748">🌐 在线观看</a>

#### 📝 Prompt
```
制作一段15秒的电影级短片，讲述一个独特的情感故事。开场场景设在一家灯光柔和的现代杂货店内。一位年轻女性（25岁左右，自然妆容，休闲装扮）缓步穿过货架间，拿起牛奶、面包、水果等日常用品。镜头以平滑的跟拍方式跟随她，聚焦于细微之处——她手指轻抚商品的动作，若有所思的神情。中段（5-10秒）：她拿起一块巧克力时突然停住，画面叠化出柔焦的闪回片段——她与某个特别的人欢笑的记忆（暗示怀旧或过往恋情）。结尾（10-15秒）：她轻轻将巧克力放回原处，露出温柔而感动的微笑，走向收银台。镜头停留片刻，目送她独自离开商店，虽形单影只却平静而坚强。风格：电影质感，浅景深，暖色调灯光，轻柔背景音乐，情感基调。镜头：慢动作，特写+平滑跟拍。氛围：怀旧，平和，略带感伤。画质：超写实，4K，胶片调色。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

### 🎬 公主月下舞殿华章
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02747.jpg" width="480" alt="SD2_02747"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/royal-princess-ballroom-dance-sequence-SD2_02747">🌐 在线观看</a>

#### 📝 Prompt
```
根据这幅16格故事板海报，创作一段电影般的奇幻舞蹈场景。深夜，一位年轻的皇室公主在奢华的欧式宫殿舞厅中优雅起舞。温暖的金色吊灯光芒与烛光交织，柔和的月光透过高大的拱形窗洒入室内。公主身着皇家蓝华服，裙摆层叠飘逸，缀满闪耀刺绣，头戴冠冕，佩戴精致珠宝。将舞蹈演绎为连贯的序列：她优雅入场，舒展双臂，开始缓慢旋转，流畅侧步，为回旋蓄势，继而加速旋转，裙摆如花绽放；在吊灯光晕下稍作停顿，完成低身屈膝扫掠，起身时后仰成弓形，最终以华丽的大回旋推向高潮；缓缓收势，转向月光笼罩的窗边，回眸一瞥诉说故事，定格于充满力量的最终姿态。镜头风格：电影级追踪运镜，流畅的慢动作瞬间，柔和的景深效果，逼真的布料物理，自然的发丝飘动，珠宝上微光闪烁，旋转时优雅的动态模糊。
```

#### 📌 Details
- Ratio: `0.56` | Duration: `9.65s`

---

### 🎬 银行劫案惊魂逃亡
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02746.jpg" width="480" alt="SD2_02746"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/neon-heist-chase-escape-SD2_02746">🌐 在线观看</a>

#### 📝 Prompt
```
风格：电影级惊悚片，手持摄影的动感，高对比度布光，青橙色调，浅景深，快节奏剪辑，逼真的动态模糊。0-2秒——劫案爆发。银行金库走廊内景。红色警报灯剧烈闪烁。安全门猛然弹开。远处警笛声开始鸣响。特写：戴手套的手抓起装满现金的行李袋。2-5秒——开始逃亡。蒙面劫匪撞碎玻璃门冲出。慢镜头中玻璃碎片向外飞溅，映出霓虹城市灯光。劫匪冲上街道时镜头轻微晃动。5-8秒——街头混乱。拥挤的城市市场街道广角镜头。人群惊慌四散。劫匪推开行人，快速穿梭。警笛声渐响，红蓝警灯扫过建筑。8-11秒——追捕升级。低角度跟拍镜头：劫匪横穿车流。车辆急刹。警车侧滑入画。快速切换：靴子踏击路面、急促喘息、甩动的钱袋。11-13秒——险些被捕。劫匪闪入狭窄小巷。一只手几乎从背后抓住他们。上方霓虹灯牌闪烁，细雨初降，湿漉漉的地面泛起反光。13-15秒——逃亡悬念。劫匪跃过护栏消失在地铁入口。镜头停留于涌入小巷的闪烁警灯，在警笛声最高潮时切至黑屏。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.1s`

---

### 🎬 芝士汉堡拉丝诱惑
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02745.jpg" width="480" alt="SD2_02745"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/gourmet-burger-asmr-slow-motion-hook-SD2_02745">🌐 在线观看</a>

#### 📝 Prompt
```
0–3秒（病毒式开场）：极致微距特写，一只美食芝士汉堡被缓缓抬起。融化的芝士在面包与肉饼之间拉出浓稠、油亮、富有弹性的长丝。肉饼上汁水闪烁，热气自然升腾。慢动作效果带来极致满足感。首帧略带颗粒感/低画质，随后逐渐锐化（以强化你的“前后对比”创意）。3–6秒：切至博主手持汉堡的镜头，采用自然手持UGC风格（手机拍摄感）。她露出兴奋反应：微微一笑，眉毛上扬。轻柔对话或口型同步：“好吧……这看起来太疯狂了。”6–10秒：手持Vlog风格镜头。她咬下一大口——芝士再次拉丝，酱汁微微滴落。真实无滤镜的反应：眼睛睁大，点头，轻声笑。自然的画面抖动增强真实感。10–13秒：极致微距ASMR镜头：酥脆烤面包的纹理、多汁肉饼的纤维、融化芝士拉丝+酱汁滴落。背景完全虚化，聚焦高级美食。13–15秒（病毒式结尾）：她看向镜头，自信微笑，轻轻竖起大拇指。汉堡定格画面，带有发光高光+轻微放大冲击。最终帧为超清晰4K HDR（清晰的“之后”画质时刻）。🎥 视觉风格（增强版）：超写实汉堡纹理（多汁肉饼、融化芝士、油亮面包）；UGC手持真实感+电影级精致；前5秒略软/低画质→过渡至清晰4K画质；温暖舒适灯光+霓虹反射；浅景深，主体突出；自然运动模糊+微相机抖动。🔊 音频风格：热门TikTok美食Vlog音效/舒缓低保真节拍；强烈ASMR层：咬碎声、酱汁滴落声、芝士拉丝声；首次芝士拉丝（钩子时刻）时加入轻微低音冲击；5秒后音频清晰度提升（与画质提升同步）
```

#### 📌 Details
- Ratio: `1.78` | Duration: `11.73s`

---

### 🎬 主角与抽象构图
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02744.jpg" width="480" alt="SD2_02744"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/faceless-mannequins-storyboard-composition-SD2_02744">🌐 在线观看</a>

#### 📝 Prompt
```
将IMG_1作为唯一的主角角色参考。将IMG_2作为抽象故事板参考。IMG_2中的无脸模特并非角色，而是表示位置、姿势和构图的符号。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 武士对决：风中的斩击
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02743.jpg" width="480" alt="SD2_02743"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/samurai-duel-at-dusk-SD2_02743">🌐 在线观看</a>

#### 📝 Prompt
```
风格：电影级武士剧，超写实，低饱和色调，自然黄昏光线，慢动作强调，风拂过境的氛围，浅景深，极简对白，情感张力，黑泽明式构图。0-3秒——无声逼近 黄昏时分，雾气笼罩的田野广角定场镜头。两名武士相隔甚远，纹丝不动。高草在疾风中摇曳。远处寺庙的轮廓隐入薄雾。万籁俱寂——唯有风声。3-6秒——缓步启程 两名武士开始相向而行。交替的低角度跟拍镜头。平静而专注的眼神特写。手在刀柄附近微动。呼吸克制，步步紧逼，张力渐升。6-9秒——张力攀升 距离缩短，镜头缓缓环绕。衣袂与发丝在更猛烈的风中翻飞。脚步陷入湿土。无音乐，无对白——只有节奏分明的脚步声与凝滞空气中不断攀升的压力。9-11秒——最终对峙 他们在刀锋可及之处停步。手紧握刀柄的极端特写。一片落叶在两人之间缓缓飘落，慢动作中时间仿佛凝固。11-13秒——拔刀与斩击 瞬间切入超慢镜头：两人同时拔刀。尖锐的金属铮鸣回荡。半空中一次决定性的交错斩击。火花与动态模糊定格在碰撞瞬间。13-15秒——余寂 一名武士屹立不倒。另一人倒出画外。风继续吹过空旷的田野。镜头定格于静止，久久凝视飘摇的草叶，随后渐隐至黑。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 公交惊现外星生物
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02742.jpg" width="480" alt="SD2_02742"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alien-bus-attack-rainy-night-SD2_02742">🌐 在线观看</a>

#### 📝 Prompt
```
一辆拥挤的城市公交车在雨夜疾驰。突然，乘客脚下的整个地板伴随着金属的巨响向上隆起。刺耳的刮擦声以不可思议的速度在车底穿梭，人们尖叫声四起。火花从车窗旁飞溅而过。一名乘客低头望向窗外——一个外星生物正倒挂在底盘下疾速奔跑，在车轴间灵活穿梭。司机猛踩刹车。地板从下方撕裂开来，那生物猛地冲进过道。 镜头1（0-2秒）——悬念 在拥挤行驶的公交车内。站立乘客脚下的地板突然剧烈向上隆起，瞬间将人掀向两侧。金属发出刺耳的呻吟。紧接着第二次撞击袭来。火花从车窗旁飞掠而过。 镜头2（2-5秒） 公交车在车流中剧烈转向。乘客尖叫着抓住扶手。刺耳的金属刮擦声从车头到车尾在车底急速移动，仿佛有庞然大物在下方以极限速度爬行。整辆车随着沉重撞击有节奏地摇晃。 镜头3（5-8秒） 一名惊恐的乘客探向侧窗。窗外下方：一个外星生物倒挂在行驶的公交车底，用修长的肢体抓住金属，在车轴间疾速穿梭。它发光的眼睛瞬间向上盯住乘客。 镜头4（8-11秒） 司机猛踩刹车。所有人向前剧烈前倾。那生物从下方反复向上猛撞。地板一块接一块撕裂开来，沿着过道朝镜头方向如拉链般向上爆裂。乘客们惊慌地翻越座椅逃窜。 镜头5（11-15秒）——高潮 地板炸裂。那生物在火花与扭曲金属的暴雨中完全冲进过道，在半空中抓住一名尖叫的乘客。公交车侧向撞上隔离带。最终画面：透过碎裂的挡风玻璃，公交车滑行着，而那生物在侧翻的车厢内沿着天花板朝镜头爬来。
```

#### 📌 Details
- Ratio: `1.0` | Duration: `12.17s`

---

### 🎬 光明与阴影的末日之战
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02741.jpg" width="480" alt="SD2_02741"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ancient-forest-apocalyptic-fairy-demon-clash-SD2_02741">🌐 在线观看</a>

#### 📝 Prompt
```
一片广袤的远古森林，参天古树已有千年树龄，树皮上刻满发光的符文，雾气如活物般在树根间蜿蜒。死寂。突然——一道金色光芒撕裂天空。厚重的风暴云层向两侧分开，耀眼的光芒倾泻而下，成千上万的仙女列队降临，翅膀如彩色玻璃捕捉阳光般闪烁，铠甲由月光石和冻结星光锻造，长矛尖端燃烧着纯白火焰。她们如椋鸟群般移动——流畅、同步、势不可挡。与此同时——森林地面裂开。深红光芒从裂缝中渗出，大地自行撕裂。恶魔大军如火山喷发般涌出——高耸的角兽、熔岩之眼的鳞甲战士、如撕裂皮革般的暗黑翅膀遮蔽了残存的天空，战吼声撼动古树根基。两军隔着树冠对视，悬停一次呼吸——彻底寂静——然后以毁灭性的力量相撞。光明与阴影相遇。金色与红色碰撞。古树颤抖碎裂。魔法向四面八方引爆。森林地面燃起烈焰。天空进一步撕裂。镜头以惊心动魄的弧线横扫——展现碰撞的全貌——双方纵深数千——一场酝酿千年的末日之战，终于在这一刻以毁灭性的爆发释放。电影感。神话感。天崩地裂。场景分解：时间 场景 10–2秒 建立广角镜头：远古符文森林，死寂，雾气在树根间蜿蜒 22–4秒 天空裂开，金色光芒涌入风暴云层，仙女大军以发光阵型降临 34–6秒 特写：月光石铠甲的仙女战士，闪烁翅膀，白色火焰长矛，整齐划一 46–8秒 森林地面裂开，深红光芒渗出，恶魔大军从地底猛烈喷发 58–10秒 特写：高耸角兽，熔岩之眼，撕裂皮革翅膀，战吼撼动树木 610–12秒 两军隔树冠对视，悬停一次心跳的纯粹寂静 712–14秒 灾难性碰撞：光明与阴影相遇，金色与红色碰撞，魔法向四面八方引爆 814–15秒 广角弧线横扫：两军全面交战，森林燃起，天空撕裂
```

#### 📌 Details
- Ratio: `0.75` | Duration: `15.21s`

---

### 🎬 碎花裙女孩的意大利之旅
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02740.jpg" width="480" alt="SD2_02740"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pastel-floral-dress-through-italy-SD2_02740">🌐 在线观看</a>

#### 📝 Prompt
```
0–4秒 威尼斯清晨的柔光洒落。一位年轻女孩从狭窄小巷中走出，身着浅色棉质碎花连衣裙，轻盈透气，裙摆随步伐轻柔摆动。运河波光粼粼，贡多拉静静划过背景。4–8秒 她乘火车穿越意大利乡间。仍穿着那件浅色棉质碎花裙，外搭轻薄开衫，凝视窗外。起伏的山丘与葡萄园化作温暖梦幻的风景。8–12秒 佛罗伦萨以金色光芒迎接她。她身着柔软棉质碎花裙漫步历史街道，浅色系与城市土黄色建筑相映成趣。微风拂过裙摆，她在教堂前驻足。12–16秒 罗马日落时分，她伫立古遗迹旁，依然穿着那件优雅的浅色碎花裙。布料映着天空温暖的橘色余晖。城市灯火渐亮，她浅笑嫣然，定格成宁静的电影画面。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.17s`

---

<!-- STATS_END -->
