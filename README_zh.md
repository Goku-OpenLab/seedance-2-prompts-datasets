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
- 总 Prompt 数量：**8679**
- 今日更新（UTC 2026-08-12）：**4**

## 🎬 今日更新
### 🎬 冰火双侠樱花决战
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11340.jpg" width="480" alt="SD2_11340"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/ice-fire-cherry-blossom-duel-SD2_11340">🌐 在线观看</a>

#### 📝 Prompt
```
【30秒最终精简版｜冰水女侠 vs 烈火男侠】 准确30秒，Seedance 2.5，保持参考图原始画幅。超写实高预算真人武侠玄幻电影，ARRI Alexa 35，自然亚洲演员、真实皮肤与衣料、长发物理、电影景深、自然运动模糊、克制胶片颗粒；禁止动漫、游戏感和廉价CG。 严格锁定@Image1成年女侠的脸、发型、白玉绿色服装与身材；@Image2成年男侠的脸、长发、黑深红服装与体型；@Image3同一巨大樱花树、古琴、石台、水池、古建筑、远山、光线和空间关系，全程不漂移。女侠开场无武器，受袭后才以池水凝成唯一半透明玉蓝冰剑；男侠始终只持一把黑色实体长剑，深红金火焰紧贴剑锋。禁止复制、换手、消失或变形。 【绝对时间线】 0–3秒古琴；3–6秒背后火剑突袭；6–8秒聚水成冰剑；8–20秒不间断高速实体剑斗；20–24秒“水龍”觉醒并召唤水龙；24–27秒“火鳳”觉醒并召唤凤凰；27–30秒终极对撞。20秒前严禁铭文、法阵、龙、凤凰或任何召唤预兆；召唤后不得返回剑斗。 人物必须有真实表情：弹琴平静；察觉偷袭时瞳孔转动、眉头收紧、呼吸骤停；Near-Miss时眼神锐利、下颌紧绷；决斗中目光追踪对手与剑刃，险避时惊险反应，撞击时咬牙、皱眉、呼气；召唤时愤怒、疲惫、承受巨力。动作非人类般高速凶猛，以脚步、腰胯、肩膀、Body Spin、空翻、轻功滑行和借力换向驱动，禁止站桩挥臂。90%保持高速，仅3厘米Near-Miss与撞剑使用0.12–0.18秒Speed Ramp。摄影机如第三位战士：Partial Cam、Whip Pan、离地20厘米Low-Level Track、快速环绕、Top Down、Dolly Zoom；狂野但清晰，每3–4秒换位，面部特写仅0.2–0.35秒，动作不停。 【0–3秒】 50mm贴近琴弦横移，女侠独自在樱花树下真实拨弦，花瓣飘落；镜头经过手指与平静侧脸后快速Dolly Out揭示庭院、水池和古建筑。男侠不得提前出现。 【3–6秒】 硬切女侠后侧。男侠从正后方十米外贴地疾冲，双手持唯一火剑，以冲刺、肩腰力量近距离垂直下劈，绝非火球或剑气。剑距她后脑3厘米时，她瞳孔侧转、扭腰向画面右侧闪开；镜头受风压向左震一次，立刻Whip Pan追右。火剑砸中石台，形成笔直燃烧裂痕、碎石、火星和飞散樱花，琴声骤停。 【6–8秒】 她滑至池边抬手，透明水带由剑柄至剑尖凝成唯一水剑，外层迅速冻结为玉蓝冰刃，内部水纹流动。男侠追到；她在成剑瞬间360°转身格挡，双剑撞出短促蒸汽、火星、碎冰和冲击环。 【8–14秒】 18mm低机位高速倒退跟拍。男侠连续下劈、反手横斩、低扫、旋身回斩；女侠侧头Near-Miss、低身滑步、反挑、剑背格挡、360°旋入内线。男侠收腹避开冰刃，单手撑地扫腿；她跃过并脚点剑背升空翻转反斩，他旋身挡下并将她震向樱花树。穿插鞋底碎石、握剑手、火刃擦眼3厘米、冰刃削过衣袖的瞬间特写。 【14–20秒】 女侠后仰避开横扫，踏树干三步垂直奔跑并弹射升空；男侠踏碎地面追上。两人沿树枝与屋檐疾跑起跳，以环境和剑刃借力连续换向：下劈、侧挡、反向Body Spin、空翻反刺、旋身格挡回踢、屋檐再跃、空中交叉换位，绝不悬浮摆姿势。火轨短且贴刃，冰剑仅留短暂水带、寒雾、冰晶；严禁远程剑气。最后空中撞剑形成蒸汽冲击环，两人被推向庭院两端，空翻落地怒视，剑斗结束。 【20–24秒｜水龍】 硬切女侠单人中近景，急促呼吸。冰剑内部浮现稳定古篆“水龍”，不是字幕或漂浮文字；“水”至“龍”沿笔画依次亮起，蓝光映脸。她双手持剑以全身360°旋转后猛烈上挑，剑尖展开三层水系法阵；水池巨量水流依次塑成龙角、头、须、鳞、长身与尾。她咬牙向前刺剑，铭文爆亮，引导完整东方水龙咆哮冲出；剑仅解除封印，绝不变成龙。 【24–27秒｜火鳳】 硬切男侠单人超低机位，逼近水压吹动长发衣袖。他咬牙怒视，黑剑内部古篆“火鳳”沿笔画依次赤金点燃，透视稳定。双手持剑全身回旋斩后垂直上挑，剑尖展开多层火阵，火焰依次构成凤凰头、羽毛、完整双翼与长尾。他向前压剑，铭文爆亮，引导巨大凤凰迎击；剑不得变成凤凰。 【27–30秒】 24mm侧面超广角：女侠左、男侠右，均以动态剑姿控制神兽，咬牙呼吸、双脚受反作用力后滑。完整水龙与火凤凰在中央正撞，水火持续推压，蒸汽、冰晶、火羽、符光和樱花旋转；核心禁止白色过曝，龙头龙身、凤头双翼长尾始终清晰。最后0.3秒“极速→10%→恢复”，两把铭文同时爆亮，双方全身推剑，释放蓝红环形冲击波并切黑。 无BGM、无旁白；仅古琴、风、呼吸、脚步、衣料、破风、火焰、冰裂、水流、撞剑、蒸汽、符文低鸣、龙吼、凤鸣、终极低频。禁止乱码、浮字、人物/武器/神兽复制、额外肢体、穿模、瞬移、僵硬重复、表情空洞、身份服装场景漂移及明显AI感。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `36.9s`

---

### 🎬 白兔怀表奇境追逐
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11320.jpg" width="480" alt="SD2_11320"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/white-rabbit-watch-chase-SD2_11320">🌐 在线观看</a>

#### 📝 Prompt
```
一段15秒的快速动作镜头，没有对白。镜头以中等宽度的平视构图开始：屏幕左侧的女孩刚刚从草丛中起身，而白兔则停在屏幕右侧的树篱旁。保持兔子身后树根下的黑暗洞口可见，但不要让它进入。镜头小心翼翼地快速推进到女孩的视线中，兔子伸手从马甲口袋里掏出一块小手表。镜头切换到兔子手中拿着手表的特写：表壳是实心金属的，表盘符合时代特征，但显然不可能转动，因为一只穿着正式的兔子正像人类一样惊慌地查看它。温暖的阳光掠过表盘。镜头立即切换到女孩的中近景；她不由自主地向前迈了一步，屏住呼吸，目光在手表和兔子的脸上来回移动。镜头拉远，兔子合上手表，转身看向树根下的洞口。镜头向右移动，将洞口纳入画面，并保留了清晰可见的因果链：手表证明了异常，异常使得追逐不可避免。女孩迈出第一步，草丛沙沙作响；树篱的叶子在微风中颤动；洞口内部阴冷漆黑，与琥珀色的洞岸形成鲜明对比。画面结尾，兔子开始向洞口奔去，女孩则笔直地站在左侧中景，蓄势待发，准备追赶。不要出现妹妹的镜头。不要让女孩触碰兔子，也不要让她叙述内心想法。情感的转折点是顿悟，而非恐惧：女孩已经看到了足够多的东西，足以做出行动的选择。使用简洁的剪辑，但要保持物理空间的连贯性：女孩始终在兔子的左侧，兔子始终在右侧，并且更靠近树篱。
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.08s`

---

### 🎬 剑仙单车互换
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11316.jpg" width="480" alt="SD2_11316"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sword-fairy-bike-swap-SD2_11316">🌐 在线观看</a>

#### 📝 Prompt
```
【视频规格】 严格总时长 10 秒 16:9 横屏 24fps 严格两个干净镜头 10.0 秒必须准确结束，不生成 10–15 秒内容 【整体风格】 电影级写实质感，采用优雅动作喜剧节奏、高级商业广告灯光、清晰的港式动作片空间关系、克制冷面反应，以及全新的“技能互换”机制。 没有任何一方被打脸或失败，而是让两个人发现：自身熟练的骑行经验，只能部分迁移到另一种完全不同的“坐骑”上。 喜剧核心来自： 熟练习惯 → 错误迁移 → 对方提醒 → 同时修正 → 意外建立默契。 【场景设定】 清晨空旷的高架滨河广场。 淡金色阳光、修长建筑阴影、拉丝混凝土地面、玻璃护栏、远处城市天际线、轻微晨雾和自然吹动衣料的风。 一条约二十米长的训练路线清楚可见。 空间必须开阔、简单、可读，确保两名角色、自行车、飞剑以及后续左右运动轨迹始终清楚。 【角色锁定】 角色 ID A｜剑仙姐 同一个来自 @图片 1 的 25–30 岁东亚剑仙姐。 严格保持参考图中的： 同一张脸 锐利深棕色眼睛 黑色长直发 高挑纤细身材比例 白色布靴 白色刺绣真丝汉服 半透明层叠宽袖 银色腰饰 玉簪 同一柄银色飞剑 角色 ID B｜单车姐 同一个来自 @图片 2 的 25–30 岁东亚单车姐。 严格保持参考图中的： 同一张脸 棕色马尾 同一身材比例 黄色外套 蓝色牛仔裤 白色运动鞋 饰品 同一辆自行车 【核心道具】 同一柄银色飞剑 同一辆自行车 不得复制、替换、消失或临时生成第二辆自行车、第二柄飞剑。 【镜头 1｜0–5s｜低角度全景缓慢推轨】 摄影机低角度全景缓慢推轨，先完整建立清晨高架滨河广场和约二十米长的训练路线。 同一个剑仙姐与同一个单车姐面对面站立。 同一辆自行车和同一柄悬浮飞剑位于两人中间。 单车姐伸手指向飞剑。 剑仙姐同时指向自行车。 单车姐问： “换？” 剑仙姐回答： “换。” 两个人保持无比严肃、像进行正式交接仪式一样的表情，随后交换位置： 单车姐走向飞剑 剑仙姐走向自行车 动作直接、克制、清楚，不加入额外笑料。 【镜头 2｜5–10s｜牛仔景中景侧面跟拍】 摄影机切换至牛仔景中景侧面跟拍。 两名角色分别使用对方原本熟悉的坐骑，并沿相反方向运动，最终在画面中交错经过。 单车姐｜骑飞剑 同一个单车姐踩上同一柄银色飞剑。 因为长期骑自行车形成的肌肉记忆，她本能地： 屈膝 压低身体 双脚做出踩踏动作 试图踩动根本不存在的脚踏板 她不是踩在剑身上行走，而是双脚已经站稳在飞剑上，却下意识做出骑自行车式踩踏动作。 飞剑受到身体动作影响，立刻向前加速。 剑仙姐｜骑自行车 与此同时，同一个穿白色刺绣真丝汉服的剑仙姐骑上同一辆自行车。 因为长期御剑形成的动作习惯，她本能地松开一只手，并用御剑时的双指指诀试图操控自行车。 自行车并不会响应指诀，因此前轮出现一次轻微偏移。 她仍坐稳车身，不摔倒、不失控，只是必须重新理解车把的实际作用。 【交错与对白】 两人沿相反方向继续前进，并在同一条训练路线中交错经过。 剑仙姐大喊： “脚别蹬剑！” 单车姐立刻回喊： “手要扶把！” 【同步修正】 两人在同一瞬间理解对方提醒，并同步修正动作。 单车姐： 停止踩踏动作 双脚稳定站在飞剑上 调整重心 恢复平稳御剑姿态 剑仙姐： 立即重新双手稳定扶住车把 修正前轮方向 保持正常骑行平衡 两个人都没有失败，也没有任何一方占绝对上风。 她们只是发现： 对方的坐骑不能完全按照自己的旧习惯来控制。 【10秒结束构图】 修正完成后，两人继续稳定前进。 她们一边保持各自新的稳定驾驶状态，一边侧头互相看向对方，以一种克制、意外认可的眼神完成确认。 画面必须在 10.0 秒准确结束于一个干净的平行运动构图： 两名角色同时处于稳定运动状态 同一辆自行车正常前进 同一柄飞剑平稳滑行 两人已经能够自信控制交换后的坐骑 两人的运动方向与摄影机轴线清楚 不发生停顿、摔倒、撞击或额外反转 10.0 秒直接结束。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.08s`

---

### 🎬 韩式夜间护肤
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11310.jpg" width="480" alt="SD2_11310"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/korean-night-skincare-vlog-SD2_11310">🌐 在线观看</a>

#### 📝 Prompt
```
超逼真竖屏视频，10秒。一位美丽的年轻韩国女性在舒适的卧室里享受着宁静的夜间护肤时光。她全程穿着同一件宽松的米白色T恤。温暖的床头灯光与透过窗户洒进来的柔和月光自然交融。房间布置温馨，充满韩式卧室的舒适感，配有全身镜、柔软的床品、柔和的串灯和小巧的床头柜。整个视频采用真实的手机自拍拍摄，如同个人夜间vlog。动作自然流畅，面部表情逼真，呼吸轻柔，眨眼自然，头发飘动逼真，肌肤纹理真实，没有任何刻意摆拍。镜头1（0-2秒）：在全身镜前进行正面自拍。她轻轻地将头发撩到肩后，短暂地看了看自己，然后将目光转向手机摄像头，露出一个温柔自然的微笑。手机轻微晃动，呈现出真实的手持效果。镜头2（2-4秒）：她舒适地坐在床边，从略高的角度自拍。她拿起一小瓶护肤霜，用指尖自然地涂抹在脸上，然后对着镜头露出俏皮的表情。镜头3（4-6秒）：对着镜子自拍。她靠近镜子，一边看着镜中的自己，一边轻轻地整理几缕散落的头发。片刻后，她看向手机屏幕，自然地笑了。镜头4（6-8秒）：在床头柜旁，她手持手机，侧脸自拍。她拿起一个透明水瓶，自然地抿了一小口，放下瓶子，带着轻松柔和的微笑看向镜头。她转身时，头发自然地飘动着。镜头5（8-10秒）：正面特写自拍。她舒适地靠在枕头上，盖着柔软的毯子，直视镜头，在镜头前比出一个小小的爱心手势，然后镜头缓缓后移，她露出温暖真挚的笑容。风格：超写实韩式美颜，真实智能手机相机画质，自然手持自拍动作，逼真的肌肤毛孔和纹理，自然的眨眼和呼吸，栩栩如生的头发模拟，逼真的手部和手指动作，柔和温暖的床头灯光与清冷的月光交相辉映，微妙的卧室阴影，电影级浅景深，自然的镜头表现，高级电影级色彩调校，温馨舒适的夜晚氛围，24帧/秒，8K分辨率，竖屏9:16。无文字，无字幕，无水印，无不自然的身体动作，无过度美颜滤镜。
```

#### 📌 Details
- Ratio: `0.75` | Duration: `10.08s`

---

### 🎬 时尚电影感蒙太奇
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11303.jpg" width="480" alt="SD2_11303"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cinematic-fashion-montage-SD2_11303">🌐 在线观看</a>

#### 📝 Prompt
```
一段节奏明快的电影式时尚蒙太奇，展现了一位身着黑色皮夹克、宽松浅蓝色牛仔裤、白色露脐上衣和深色太阳镜的时尚年轻女子。视频以一个快速追踪镜头开始，她奔跑在冷色调混凝土停车场的金属购物车旁。镜头快速切换，运用了快速摇摄和桶滚等技巧。一个极低角度的鱼眼镜头镜头展现了她站在一栋高耸的混凝土建筑前，头顶是明亮的阴天。镜头立即切换到一个高角度无人机镜头，俯瞰着她在空旷的停车场旋转的画面。在镜头切换之间，短暂地出现了数字故障效果和视觉扭曲。该序列中还运用了动态的手部过渡，展现了人物伸手去够镜头的画面。最后，以一个低角度追踪镜头结束，展现了她自信地向前走去的姿态。灯光在昏暗的荧光停车场灯光和明亮的阴天日光之间切换。高度逼真的运动模糊、电影级的色彩分级、自然的皮肤纹理和真实的服装物理效果。背景音乐是​​欢快的电子乐。画面比例为16:9，时长12秒。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `12.07s`

---

### 🎬 冰火女战士激战
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11299.jpg" width="480" alt="SD2_11299"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/elemental-warriors-clash-SD2_11299">🌐 在线观看</a>

#### 📝 Prompt
```
一段气势磅礴、精彩纷呈的3D奇幻动作场景，两位元素女战士展开激战。左侧，一位身着红色皮甲、黑发凌厉的女战士，手臂上缠绕着炽热的火焰和燃烧的余烬。右侧，一位身着白冰蓝相间长袍、长发飘逸的女战士，挥舞着闪耀着蓝色光芒的冰玫瑰鞭剑。她们在荒凉的远古石柱林立、暴风雨般的夕阳下，冲锋陷阵，跃向彼此。当她们在空中相撞时，炽热的橙色魔法光环与明亮的蓝色冰晶能量正面碰撞，迸发出巨大的光芒、余烬、蓝色玫瑰花瓣和飞溅的碎片，场面震撼人心。动态镜头平移、慢动作冲击、超逼真的8K CGI、虚幻引擎5渲染风格、戏剧性的光影效果，共同打造出这段精彩绝伦的视觉盛宴。
```

#### 📌 Details
- Ratio: `2.35` | Duration: `15.19s`

---

### 🎬 夜滩双猫萌舞
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11298.jpg" width="480" alt="SD2_11298"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/kittens-dancing-night-beach-SD2_11298">🌐 在线观看</a>

#### 📝 Prompt
```
一段10秒的逼真手持视频，拍摄于夜晚湿润的沙滩上。一只头部带有灰色斑纹的白色小猫，后腿直立在浅水中，前爪抬起，仿佛在跳舞或保持平衡，好奇地看着镜头。一只浅棕色（姜黄色）的小猫向它走来，然后也站了起来，与白色小猫并肩而立。两只猫并排站着，爪子抬起，摆出一个俏皮可爱、近乎人类的姿势。柔和的海浪在黑暗的背景中翻滚，湿润的沙滩在柔和的夜光下闪闪发光。这段略带抖动的可爱手持视频，营造出一种温馨而奇幻的氛围。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `9.97s`

---

### 🎬 超写实电影分镜
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11296.jpg" width="480" alt="SD2_11296"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/hyper-realistic-cinematic-storyboard-SD2_11296">🌐 在线观看</a>

#### 📝 Prompt
```
使用 @[Image] 作为电影序列的分镜参考。用作第一镜头 01。一段 15 秒的恢弘电影序列，严格按照时间顺序流畅地过渡到所有 8 个分镜。视觉风格：超写实。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 奢华智能手表演示
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11293.jpg" width="480" alt="SD2_11293"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/luxury-smartwatch-demo-SD2_11293">🌐 在线观看</a>

#### 📝 Prompt
```
一段奢华智能手表产品演示视频。开头以微距镜头突出展示屏幕、高级材质、流畅的镜头运动、引人注目的光影效果以及产品功能，最后呈现最终使用场景。超逼真的商业广告风格，4K 超高清画质。一段奢华智能手表产品演示视频。开头展示最终的广告片，呈现智能手表在运动中的使用效果。在揭示最终效果后，过渡到工作流程和特写镜头，运用高级灯光、流畅的电影级镜头运动，呈现超逼真的商业广告风格，4K 超高清画质。
```

#### 📌 Details
- Ratio: `0.63` | Duration: `20.03s`

---

### 🎬 超写实人偶渲染
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11289.jpg" width="480" alt="SD2_11289"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/hyper-realistic-cgi-figurine-render-SD2_11289">🌐 在线观看</a>

#### 📝 Prompt
```
电影级超写实3D CGI收藏人偶渲染，如同真人大片的特效镜头：基于物理的渲染（PBR）、媲美Octane渲染器的光照和材质，织物纹理清晰可见，垂坠自然，金属部件磨损痕迹逼真。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `13.97s`

---

### 🎬 雨夜逃亡
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11287.jpg" width="480" alt="SD2_11287"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/rainy-night-alien-chase-SD2_11287">🌐 在线观看</a>

#### 📝 Prompt
```
一个绝望的低角度追踪镜头，跟随image_1.png中的男子，保持着他的容貌和蓝色眼睛，如今他身着黑色战术装备，在夜色中一条被雨水浸透、混乱不堪的市中心街道上飞奔。在他身后，一辆双层城市公交车被卷入一场巨大的爆炸，碎片和橙色的火焰冲天而起。在燃烧的城市上空，一艘巨大的、金属结构精巧的生物机械外星母舰穿过暴风云缓缓降落，蓝色的灯光闪烁不定。在右侧，一个身形矫健的异形掠食者从阴影和残骸中现身，紧追不舍。镜头动态地后退并摇摄，展现了破坏的规模，最终定格在全景画面上。戏剧性的光线对比鲜明，火光与冷冽的夜色交相辉映。大雨倾盆而下，在水面上形成倒映着光芒的水洼。无文字说明。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.04s`

---

### 🎬 故事板视觉控制指南
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11285.jpg" width="480" alt="SD2_11285"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/storyboard-visual-control-SD2_11285">🌐 在线观看</a>

#### 📝 Prompt
```
【参考控制】使用上传的故事板图像作为故事结构、角色设计、服装设计、环境、情感发展和镜头顺序的主要视觉参考。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 巧克力芒果干广告
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11283.jpg" width="480" alt="SD2_11283"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/chocolate-mango-snack-commercial-SD2_11283">🌐 在线观看</a>

#### 📝 Prompt
```
一部电影级3D商业产品视频，宣传一款高档干果零食，采用9:16竖屏比例。视频以高清特写镜头开场，展现了枝头枝繁叶茂、绿叶葱茏的新鲜成熟黄芒果和红芒果，沐浴在温暖的金色阳光下。镜头流畅过渡，一颗成熟的芒果漂浮在温暖的背景光下，随后化作一片片金黄色的芒果干，轻盈地悬浮在空中。接着，一个新鲜的椰子裂开，浓郁顺滑的牛奶巧克力缓缓流淌而出。裹满黑巧克力的芒果干向上飘浮，细碎的白色椰丝如雪花般飘落。最后，画面中央漂浮着一个印有“MR. VIET 巧克力椰香芒果干”字样的黑色零食袋，周围环绕着裹满巧克力的芒果干和细碎的椰丝。该视频运用了动态物理效果、温暖的室内灯光、超精细的纹理、慢动作特效、8K渲染，呈现出逼真的画面效果，风格与食品广告片类似。
```

#### 📌 Details
- Ratio: `0.56` | Duration: `21.7s`

---

### 🎬 练习生千禧闪回
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11272.jpg" width="480" alt="SD2_11272"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/trainee-nostalgic-flashback-SD2_11272">🌐 在线观看</a>

#### 📝 Prompt
```
@CHASE 始终保持同一角色形象。请严格保持面部、发型和外貌的一致性。

制作一段15秒的怀旧风格闪回，展现2000年代初练习生的成长历程，全部使用手持DV/16mm摄像机拍摄。呈现原始的个人影像美学：自然的镜头抖动、不完美的构图、缓慢的自动对焦、笨拙的微距变焦、轻微的模糊、磁带噪音、运动模糊、高光过曝以及偶尔的曝光闪烁。不使用任何现代的精修摄影技术。

故事：
0-2秒：日出前，她疲惫地从练习生宿舍醒来。“没有人看到这一切是如何开始的。”
2-4秒：她走进空荡荡的舞蹈室，打开灯，准备练习。
4-6秒：在声乐室里，她唱错一个高音，叹了口气，再次尝试。 “有些时候，我觉得自己不够好。”
6-9秒：反复练习舞蹈，犯错，然后继续练习。
9-11秒：快速的DV特写镜头，展现磨损的运动鞋、疲惫的双手、汗水，以及一个动作最终完美落地。
11-13秒：筋疲力尽地站在走廊里，她轻轻一笑，听到练习音乐，又站了起来。“但不知怎的……我还是坚持了下来。”
13-15秒：她走向一间灯光明亮的评估室，停顿片刻，深吸一口气，走了进去。“也许这就足够了。”画面切黑。
真实、私密、充满情感。细腻的表演，真实的疲惫和决心。硬剪辑，真实的房间氛围，脚步声和呼吸声。柔和的情感音乐逐渐响起。营造出一种被遗忘的私人教练录像的感觉，而不是音乐录影带。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 粉发少女墨舞
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/2/SD2_11271.jpg" width="480" alt="SD2_11271"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/pink-hair-ink-action-SD2_11271">🌐 在线观看</a>

#### 📝 Prompt
```
P1 [0:00–0:01.25] 使用提供的故事板帧、角色参考图和 Higgsfield 标志参考图。保持角色外观的精确性：粉色头发、橄榄绿工装裤、白色露脐上衣、绿色帽子、手臂上的纹身。保持 Higgsfield 标志和“Higgsfield”字样在整个场景中自然可见，作为环境品牌标识。实景拍摄，低角度镜头，一位身穿橄榄绿工装裤的年轻女子，粉色头发，低蹲着，黑色墨水在她拳头击打地面时爆炸，高速摄影，戏剧性的影棚灯光，墨水飞溅物理效果，超精细的皮肤纹理，佳能 R5，85mm f/1.4 镜头。P2 [0:01.25–0:02.50] 照片级写实，动态模糊，一位身穿粉色头发的运动型女子使出旋踢，黑色墨水轨迹在空中划过，电影级灯光，浅景深，粗糙的混凝土环境，运动摄影风格，尼康 Z9 相机。保持角色形象的精准还原，并确保Higgsfield品牌标识清晰可见。P3 [0:02.50–0:03.75] 逼真的低角度仰拍镜头，粉色头发的女子垂直跃起，周围环绕着巨大的黑色墨水漩涡，戏剧性的轮廓光，上升压力造成的扭曲，高速快门，逼真的织物运动，动态的姿态，24mm广角镜头。P4 [0:03.75–0:05.00] 平面上旋转的黑色墨水漩涡的微距摄影，螺旋状结构，高对比度的黑白色调，影棚灯光，超清晰的焦点，逼真的流体动力学。角色出现在边缘或倒映在墨水漩涡中。P5 [0:05.00–0:06.25] 逼真的动态动作镜头，粉色头发的女子低身闪避，黑色墨水带在她周围飞舞，动态模糊，强烈的戏剧性光线，粗粝的都市背景，运动服，电影级调色。 P6 [0:06.25–0:07.50] 真实摄影，一位粉色头发的女子朝镜头疾驰而来，黑色墨迹在她身边飞驰，头发随风飘扬，面部清晰对焦，背景虚化，戏剧性的逆光轮廓。P7 [0:07.50–0:08.75] 电影级写实镜头，一位粉色头发的女子冲破破碎的表面，沾满墨水的碎片悬浮在空中，她以动感的落地姿势，爆炸性的逆光，尘土和墨水颗粒，深景深，IMAX风格的戏剧效果。P8 [0:08.75–0:10.00] 电影级写实中景镜头，一位粉色头发的年轻女子直立面对镜头，目光直视，黑色墨水从她的双拳中滴落，衣服上沾满了墨水，表情坚定，戏剧性的逆光，墨雾在她脚边弥漫，浅景深，营造出粗粝的氛围，佳能R5，85mm f/1.4镜头。全球通用说明：请完全按照提供的 Higgsfield 标志参考图使用。请勿更改标志设计或“Higgsfield”字样。请确保品牌标识在每一帧画面中清晰可见，直至最后一帧。
```

#### 📌 Details
- Ratio: `1.77` | Duration: `10.08s`

---

<!-- STATS_END -->
