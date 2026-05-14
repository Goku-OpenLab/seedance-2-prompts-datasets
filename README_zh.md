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
- 总 Prompt 数量：**2898**
- 今日更新（UTC 2026-05-14）：**163**

## 🎬 今日更新
### 🎬 霓虹魔幻时尚大片
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02917.jpg" width="480" alt="SD2_02917"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/turquoise-dream-catwalk-fantasy-SD2_02917">🌐 在线观看</a>

#### 📝 Prompt
```
制作一段15秒的奢华电影感竖屏奇幻视频（9:16比例）。一位魅力四射的西方女性，拥有深色长卷发、光泽肌肤与精致妆容，身着闪耀霓虹绿松石色亮片迷你裙。她怀抱一只祖母绿眼眸、佩戴同色珠宝蝴蝶结的蓬松波斯猫。二者置身于装饰繁复的绿松石水晶相框内，背景为深蓝绿色，点缀闪烁散景与漂浮亮片。0-3秒：静态肖像如活体画作。3-6秒：画作苏醒——她微笑抚猫，猫咪眨眼环顾。6-9秒：绿松石粒子迸发，她甩发跨出画框。9-12秒：快速时尚切换镜头——旋转、亮片裙特写、与猫俏皮互动。12-15秒：最终T台式英雄定格，旋转星尘环绕，身后相框流光溢彩。风格：照片级写实、魔幻奢华美学、高定时尚大片、电影级布光、真实毛绒与织物质感、35mm胶片效果、超精细8K画质。
```

#### 📌 Details
- Ratio: `0.56` | Duration: `15.0s`

---

### 🎬 女王骑士穿越战火
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02916.jpg" width="480" alt="SD2_02916"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/warrior-queen-dark-realm-SD2_02916">🌐 在线观看</a>

#### 📝 Prompt
```
一段极具电影感的15秒超现实奇幻片段，描绘了一位无畏的女王骑士骑着黑色战马穿越战火纷飞的黑暗领域。开场以宏大的航拍镜头展现暴风雨云下破碎的王国，闪电瞬间照亮了断裂的塔楼、燃烧的攻城器械、飘散的灰烬以及战场上如河流般涌动的硝烟。雨滴与火星在空中交织，远方的爆炸映红了天际。镜头快速切换为动态跟拍，战马全速冲过泥泞与火焰，铠甲叮当作响，女战士残破的斗篷在风中猛烈翻飞。闪电短暂映照在她雕刻般的铠甲与坚毅的面容上。画面切入戏剧性的低角度慢动作：战马跃过坍塌的废墟与燃烧的残骸，浓烟中浮现出 monstrous 的暗影生物。电影级特写捕捉到女战士拔出附魔长剑的瞬间，剑身萦绕着超自然能量，火焰的倒影在她眼中燃烧。配乐骤然激昂，快速动作镜头中她策马劈开黑暗实体，火花、魔法粒子与爆炸能量在风暴中四散，伴随超写实的动态模糊与电影冲击力。最终镜头拉升至史诗级航拍：她深入战场，四周涌动着恶魔大军。巨型闪电在她身后炸裂，戏剧性的闪光将混乱景象照得惨白。体积雾、变形镜头光晕、无缝镜头转换、电影级调色、逼真的环境物理效果，以及惊艳的4K电影级写实感，从头至尾营造出浓烈的黑暗奇幻氛围。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.23s`

---

### 🎬 保龄球馆惊魂夜
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02915.jpg" width="480" alt="SD2_02915"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/neon-nightmare-bowling-alley-horror-SD2_02915">🌐 在线观看</a>

#### 📝 Prompt
```
深夜霓虹灯下的保龄球馆内，一场高度紧张的恐怖场景。复古街机灯光、反光的保龄球道、五彩LED光芒、逼真的实景照明。镜头1（0-3秒）：一名年轻女子僵立在球道旁，手中握着保龄球，呼吸变得急促。她突然看到周围保龄球馆的墙壁和天花板上爬满了巨大的昆虫状生物——巨型蜘蛛在霓虹灯牌和吊灯间穿梭。附近的人显得扭曲且毫无察觉。镜头2（3-5秒）：一只昆虫迅速爬过球道向她冲来。她惊慌失措——然后猛地回过神来。一切恢复正常。只是个普通的保龄球馆。身后的朋友们笑着向她挥手。镜头3（5-8秒）：她仍心有余悸，缓缓上前将保龄球沿球道滚出。镜头低角度跟随旋转的球向球瓶逼近。镜头4（8-11秒）：当球接近球瓶时，她突然再次听到令人不安的昆虫咔嗒声。笑容凝固。旁边空荡荡的球道——黑暗中有什么东西在快速移动。镜头5（11-15秒）：一只巨大的昆虫生物突然从侧道冲出，在抛光地板上疯狂爬行扑向人群。所有人尖叫着踉跄后退。那生物径直朝女子扑去。
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.08s`

---

### 🎬 洗衣店惊魂夜
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02914.jpg" width="480" alt="SD2_02914"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/laundromat-horror-creature-attack-SD2_02914">🌐 在线观看</a>

#### 📝 Prompt
```
深夜，一间灯火通明的24小时自助洗衣店内上演着高度紧张的恐怖场景。成排的工业洗衣机、荧光灯管、反光瓷砖地面、低声嗡鸣的自动售货机。声音：洗衣机的嗡鸣声、远处街道的车流声、手机滑动点击声，突然被暴力的金属撞击声打断。镜头1（0-3秒）：一名年轻女子独自坐在洗衣店内刷手机，身后几台洗衣机正在运转。突然——所有机器同时开始不自然地剧烈震动。硬币哗啦作响。灯光微微闪烁。她缓缓抬起头。镜头2（3-6秒）：震动升级为机器内部传出的巨大金属撞击声。一台洗衣机猛烈左右摇晃。接着是另一台。泛着绿光的水突然从机门下方渗出，在地板上蔓延开来。她紧张地站起身：“这……这是怎么回事？”镜头3（6-9秒）：摄像机缓缓环绕她移动，更多机器开始从内部剧烈撞击。洗衣店内回荡着扭曲的尖叫声与撞击声交织的噪音。绿色液体漫过瓷砖。镜头4（9-12秒）：一台洗衣机的门突然弹开。一只畸形的湿漉漉生物爬了出来。接着另一台机器打开。又一台。更多怪物从她周围不同的机器中一只接一只地钻出，滴落着绿色黏液。她惊恐地缓缓后退，摄像机继续环绕拍摄。镜头5（12-15秒）：所有怪物突然静止不动。半秒寂静。接着所有怪物同时尖叫着从洗衣店各个方向朝她冲来。她惊慌失措地踉跄后退——怪物们纵身扑来——画面切至黑屏。
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.08s`

---

### 🎬 雨夜屋顶狂奔
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02913.jpg" width="480" alt="SD2_02913"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/neon-rooftop-chase-action-sequence-SD2_02913">🌐 在线观看</a>

#### 📝 Prompt
```
超写实电影级动作片段，时长15秒，快速剪辑。一位身着旧风衣的坚毅女子在雨夜中狂奔于40层高楼的屋顶，脚下是霓虹闪烁的城市。镜头1[0-2秒]：极微距特写——她猛然睁眼，瞳孔扩张，红色应急灯光倒映其中，额间汗珠，浅景深，手持微颤。镜头2[2-4秒]：超广角低空无人机视角——她从通风井跃下，风衣在慢镜头中翻飞，下方浓雾弥漫，城市光斑虚化，变形镜头光晕。镜头3[4-6秒]：快速横向跟拍，斜角镜头——她转身冲向屋顶边缘，三名武装人员出现在身后，浅焦处理，背景中敌人模糊。镜头4[6-8秒]：120帧幻影慢镜头特写——她徒手抓住磨损的钢缆，指节泛白，子弹火花擦过缆绳，金色实用光爆裂，电影级动态模糊。镜头5[8-10秒]：空中眩晕俯冲——她荡出边缘，在两座玻璃摩天楼间自由坠落，下方城市网格闪烁，戏剧性拉远镜头，纯粹电影眩晕感。镜头6[10-12秒]：侧面中景——她撞上玻璃天窗，蛛网状裂纹实时扩散，她翻滚起身不停歇，实用碎裂特效，尘埃粒子。镜头7[12-14秒]：缓慢推进过肩镜头——她回头一瞥，下颌紧绷，眼神冰冷而坚定，城市雾气飘过画面。镜头8[14-15秒]：骤黑切镜——她进入黑暗楼梯间，门砰然关闭。照片级真实，8K分辨率，变形宽银幕2.39:1画幅，青橙色调，暗部压黑，高光褪色，实用霓虹反射光，红色应急灯，杜比视界HDR，全程雨景特效，湿滑表面镜面反射，电影级音效设计。
```

#### 📌 Details
- Ratio: `1.77` | Duration: `15.1s`

---

### 🎬 深夜外星追杀惊魂
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02912.jpg" width="480" alt="SD2_02912"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alien-home-invasion-horror-chase-SD2_02912">🌐 在线观看</a>

#### 📝 Prompt
```
深夜现代住宅内上演的高张力科幻恐怖场景。昏暗暖色灯光下，狭长走廊映着抛光地板，窗外细雨绵绵。大幅半透明窗帘随风轻摆。镜头1（0-3秒）：客厅中一男一女僵立原地。男人紧握手枪，死死盯着被薄纱窗帘遮蔽的落地窗——帘外，一个扭曲的巨型黑影正缓缓移动。镜头2（3-5秒）：窗帘猛然向内爆裂。巨型外星生物撞碎玻璃冲入室内。男人本能开枪，却被冲击波掀翻在地。女人尖叫着奔逃。镜头3（5-9秒）：生物沿房屋疯狂追逐女人。她冲过走廊，急转绕过拐角，跌撞冲下楼梯，而生物如壁虎般在墙壁与天花板间快速攀爬紧追不舍。沿途家具被撞得支离破碎。镜头4（9-12秒）：女人跌入楼下房间——死路。她背抵墙壁瘫坐在地。生物缓缓爬过地板逼近，庞然身躯笼罩着她。狰狞面孔凑至咫尺。她吓得浑身僵直。镜头5（12-15秒）：震耳枪响。生物剧烈抽搐，轰然倒在她身侧。门口硝烟弥漫。持枪男人喘息着立于烟雾中。
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.08s`

---

### 🎬 机械恐龙夜袭赛博城
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02911.jpg" width="480" alt="SD2_02911"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/robotic-dinosaur-attacks-cyberpunk-city-SD2_02911">🌐 在线观看</a>

#### 📝 Prompt
```
午夜时分，巨型机械恐龙袭击赛博朋克城市，霓虹全息影像遍布各处，未来军队奋起反击，科幻电影般的场景，火花四溅，爆炸连连，戏剧性光影，超写实金属质感，史诗级动作氛围
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.1s`

---

### 🎬 孤星漫步废船
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02910.jpg" width="480" alt="SD2_02910"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/lone-soldier-destroyed-spaceship-SD2_02910">🌐 在线观看</a>

#### 📝 Prompt
```
孤独的太空士兵行走在毁坏未来飞船内部，红色应急灯闪烁，电影级科幻氛围，零重力漂浮的碎片，超写实，黑暗电影场景，戏剧性镜头运动，充满情感的未来感
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.1s`

---

### 🎬 实验室惊魂逃生
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02909.jpg" width="480" alt="SD2_02909"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/alien-lab-escape-sci-fi-horror-SD2_02909">🌐 在线观看</a>

#### 📝 Prompt
```
深夜，未来感十足的地下实验室中上演了一场高张力科幻恐怖戏码。惨白的照明与闪烁的红色应急灯交织，反光地板、玻璃隔离墙、电脑显示器、散落的科研设备随处可见。音效：低沉的电流嗡鸣、远处警报声、玻璃吱嘎作响、生物低吼。镜头1（0-2秒）：实验室走廊内，一名持手枪的紧张保安站在一位穿白大褂的女科学家身旁。巨大的半透明玻璃隔离墙后，一个扭曲的庞大生物轮廓缓缓移动。科学家紧张地凝视着，低声说：“我想……它醒了。”镜头2（2-5秒）：突然，隔离玻璃猛烈向内爆裂。巨大的外星生物在火花四溅和玻璃碎片中冲了出来。保安开了一枪，却被猛地撞倒在地。科学家尖叫着逃跑。镜头3（5-9秒）：生物在实验室中疯狂追逐她。她飞奔过闪烁的显示器和翻倒的设备，身后生物撞碎玻璃隔断。警报响起。生物冲过实验室，标本罐纷纷碎裂。镜头4（9-12秒）：她跑进一个小实验室隔间——死路一条。她背靠操作台，无路可逃。生物沿着地板和墙壁缓缓爬向她，居高临下。它将脸凑到她面前几英寸处，张开血盆大口。镜头5（12-15秒）：一声响亮的枪声回荡。生物猛地抽搐，倒在她身旁。门口烟雾弥漫。保安站在那里，双手颤抖地握着手枪。科学家如释重负地长舒一口气，红色应急灯在毁坏的实验室中闪烁。
```

#### 📌 Details
- Ratio: `1.33` | Duration: `15.08s`

---

### 🎬 山巅龙啸惊天地
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02908.jpg" width="480" alt="SD2_02908"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/dragon-roar-mountain-summit-SD2_02908">🌐 在线观看</a>

#### 📝 Prompt
```
单镜头静态构图，黎明时分山巅之上呈现宽银幕电影感画面，起初镜头稍近对准男子上半身——一名身着白色登山夹克的男子[图1]居中面向镜头站立，微风轻拂衣摆与发丝，清冷晨光映照面庞，身后层叠的蓝色山脉与远处雪峰在戏剧性的云天下延展，薄雾在山谷间飘移。镜头启动时，摄影机缓慢而微妙地向后移动（慢速后拉），逐渐拓宽视野，展现身后更广阔的山峦景致。男子随即缓缓将双臂向外向上抬起，仅至肩部高度，未完全展开成V形，动作克制而沉稳。当双手抬至半空时，远处山峦骤然爆发无形冲击波——一场无火焰的剧烈爆炸，只有尘土、岩石与气压狂暴向外扩散，碎石与浓烟冲天而起，镜头因冲击力产生细微震颤，强化了紧张氛围。在扩散的尘云中，两条巨龙赫然显现，巨大剪影穿透烟尘与光线，鳞甲细节在冷冽天光下清晰可见，它们稳稳盘踞于山巅，利爪紧扣岩壁，双翼半展却未扇动，纹丝不动。男子保持双臂悬停姿态，岿然不动。首条巨龙昂首发出震天咆哮，第二条巨龙随即以更响亮的吼声应和，每次咆哮都引发可见的环境震动——尘土簌簌、云层翻涌——镜头随吼声震颤加剧。突然，在更深的尘雾与崩裂的山体中，第三条体型更为庞大的巨龙赫然现身，其压迫感铺天盖地，即刻爆发出最具统治力的咆哮，引发更剧烈的镜头晃动与大气扭曲。三条巨龙始终固守山巅，巍然不动，尘雾缭绕其间，男子在前景中保持双臂微张的姿势，疾风与碎屑环绕周身，画面定格于这充满戏剧张力的瞬间。无配乐
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.1s`

---

### 🎬 母亲节温馨短片
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02907.jpg" width="480" alt="SD2_02907"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/mothers-day-heartwarming-surprise-SD2_02907">🌐 在线观看</a>

#### 📝 Prompt
```
一部温馨的电影感母亲节短片。清晨，母亲早早起床准备早餐，温柔唤醒孩子，帮忙整理校服，临别前深情拥抱。画面切换至长大后的孩子，手捧鲜花与手写贺卡给母亲惊喜。柔和的晨光、动人的背景音乐、慢动作拥抱、温暖的家居氛围、真实细腻的表情、电影级运镜。字幕浮现：“母爱永不褪色。母亲节快乐❤️” 4K画质，情感叙事，9:16竖屏格式，时长15秒。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.0s`

---

### 🎬 暴风雨中的致命特工
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02906.jpg" width="480" alt="SD2_02906"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/storm-assault-tactical-covert-op-SD2_02906">🌐 在线观看</a>

#### 📝 Prompt
```
时长：15秒 风格：超高速电影级动作 • 未来主义间谍惊悚 • 暗黑战术时装 格式：竖屏9:16 • 超高清8K • IMAX手持摄影 • 杜比全景声 • 极致真实 一段超写实的军事动作场景，发生在夜间穿越猛烈雷暴的赫尔克里士运输机内。极端湍流以逼真的物理效果摇晃着飞机。红色应急灯快速闪烁。体积烟雾充满机舱。蓝橙色调的电影级照明营造出高对比度的未来主义战场氛围。超精细视觉特效、动态模糊、镜头畸变以及动态IMAX手持摄影机运动，增强了紧张感和混乱程度。 主要角色： 一名训练有素的女特工，身着黑色战术时装，冷静专注，是极其敏捷的近身格斗专家，执行快速精准的战术战斗。 0–2秒：赫尔克里士飞机在暴风雨中剧烈摇晃。红色应急灯闪烁。特写镜头对准踩在金属地板上的靴子，镜头向上倾斜，露出她冰冷专注的脸。武装特工慢慢包围了她。 2–4秒：第一次攻击开始。她以超高速移动。镜头快速摇摄跟随。旋转脚跟踢将第一名特工撞到墙上。火花和碎片以慢动作呈现。 4–6秒：快速近身格斗。她施展咏春拳加赛博忍者打击。多名敌人以电影化的快速连击被击败。镜头在狭窄的走廊中剧烈旋转。 6–8秒：枪声响起。她以超慢动作躲开子弹，解除攻击者武装，用膝盖撞击，将他扔向货舱门。警报加剧，混乱升级。 8–10秒：后货舱门猛烈打开。暴风雨涌入舱内。她在敞开的边缘附近与最后几名特工搏斗。闪电照亮，形成戏剧性的剪影。 10–12秒：最后一名敌人被旋转踢击败，扔出飞机。她立即以史诗般的慢动作跳入暴风雨的夜空。 12–14秒：在云层上空自由落体。降落伞戏剧性地展开。她的服装在狂风中飘动。在闪电的天空下，表情冷静、克制、致命。 14–15秒：她向赫尔克里士飞机投掷一枚手榴弹。巨大的空中爆炸摧毁了飞机。 最终镜头：她在降落伞下漂浮，身后是火球和闪电风暴，呈现电影般的刺客终局。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.14s`

---

### 🎬 印尼冰咖啡牛奶制作
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02905.jpg" width="480" alt="SD2_02905"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/iced-kopi-susu-harvestside-diamond-SD2_02905">🌐 在线观看</a>

#### 📝 Prompt
```
在印尼家庭书桌场景中拍摄的UGC手持视频，采用仅露手部的休闲创作者风格。人物将一包白色Harvestside Arabica速溶咖啡和一瓶Diamond鲜奶盒清晰展示在镜头前，严格参照提供的产品图片还原咖啡袋和牛奶盒的外观。在透明玻璃杯中制作冰咖啡牛奶，杯中可见冰块，置于温馨书桌上。自然晨光，真实手机摄像头，轻微手持晃动，背景为舒适书架，呈现地道印尼UGC风格，无影棚感，无商业级抛光灯光。为8秒9:16比例Seedance 2.0视频设计的流程：前1.5秒：双手将两款产品靠近镜头，标签清晰可读。接下来2秒：Harvestside咖啡袋直立放在桌上，顶部自封拉链整齐打开。小勺从袋内舀取速溶咖啡粉，加入装有冰块的透明玻璃杯。禁止直接从袋中倒咖啡，禁止撕扯或破坏袋子，禁止将袋子作为饮品容器。再接下来2秒：从Diamond鲜奶盒中倒出牛奶入杯，形成奶油色咖啡漩涡。最后2.5秒：特写完成后的冰咖啡牛奶置于桌上，两款产品包装放在玻璃杯旁。背景为轻柔欢快的晨间低保真音乐，自然居家氛围，干净健康的饮品制作过程。产品标签需严格参照参考图片。
```

#### 📌 Details
- Ratio: `0.56` | Duration: `8.08s`

---

### 🎬 永夜破晓：第一缕阳光
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02904.jpg" width="480" alt="SD2_02904"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/first-dawn-after-eternal-night-SD2_02904">🌐 在线观看</a>

#### 📝 Prompt
```
一部电影级情感科幻短片，设定在一个永夜笼罩的世界。0-3秒：寂静无声，城市在永恒的黑暗中冻结。路灯微弱闪烁，雪一般的灰烬缓缓飘落在空荡的街道上。人们站在屋顶，凝视着漆黑的地平线。3-6秒：特写镜头对准疲惫的面孔——人们相互依偎，静静等待。收音机里传来静电的嘶嘶声。空气中掠过一阵微弱的、无法解释的震颤。6-9秒：天空在多年后首次开始变化。地平线上出现一道细薄、不可思议的温暖橙色光线。鸟儿突然振翅起飞。风势渐起。9-12秒：情绪升级——人们跪倒在地，哭泣、欢笑、遮住眼睛。第一缕阳光冲破黑暗，触及那些多年未见光明的建筑。12-15秒：最终宽幅电影镜头。太阳完全升起，金色光芒淹没整个世界。冰雪融化，阴影退却，城市在寂静与敬畏中缓缓苏醒。风格：极致电影写实主义，情感基调，柔和金色体积光，慢动作人类反应，高细节环境，电影级调色，充满希望与变革的氛围。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.07s`

---

### 🎬 深夜厨房情感对峙
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/SD2_02903.jpg" width="480" alt="SD2_02903"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/emotional-confrontation-dim-kitchen-SD2_02903">🌐 在线观看</a>

#### 📝 Prompt
```
15秒，电影级情感对峙。深夜，狭小公寓厨房内，两位角色@[角色表参考]面对面站立。房间仅由一盏暖色顶灯和窗外透进的柔和城市灯光照亮。气氛充满情感疲惫、紧张且痛苦地亲密，仿佛一场积压多年的争吵。现代电影现实主义风格，微妙的手持摄影机运动，浅景深，柔和胶片颗粒，情感克制的表演，对话间隙中真实的沉默。节拍1：情绪状态保持高唤醒度和中低效价。镜头：缓慢的手持侧拍，环绕两位角色，紧贴肩膀的特写镜头，短暂的平视双人镜头展现情感距离。FACS角色A：AU4 + AU7 + AU17。对话A：/juː ˈnev.ɚ ˈriː.ə .li lʊkt æt miː/ /juː wɚ ɔːlˌweɪz ˈsʌmˌwɛɹ ɛls/。声音：紧绷克制的声音，压抑的愤怒，呼吸不均匀。角色A试图保持冷静，同时压抑多年的怨恨。节拍2：情绪状态逐渐转向极低效价和中高唤醒度。镜头：缓慢推进至角色B，极度特写颤抖的眼睛和嘴巴，静态广角镜头展现争吵高潮后的沉默。FACS角色B：AU1 + AU4 + AU15 + AU25。对话B：/aɪ wəz ˈtɹaɪ.ɪŋ maɪ bɛst/ /aɪ dɪdnt noʊ haʊ tə fɪks ˈɛv.ɹiˌθɪŋ/。声音：破碎的声音，呼吸不稳，情感崩溃的表演。节拍3：情绪状态保持极低效价和中低唤醒度。镜头：锁定广角镜头，两人之间沉默，缓慢特写两位角色避免眼神接触，微妙的焦点切换在面孔之间。FACS角色A：AU1 + AU15 + AU17。对话A：/ˈmeɪ.bi wiː stɑpt ˈlɪs.ən.ɪŋ ə lɔŋ taɪm əˈgoʊ/。声音：情感疲惫，声音更轻，愤怒被悲伤取代。没有夸张的尖叫，没有暴力，没有喜剧，没有文字叠加，没有水印。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.03s`

---

<!-- STATS_END -->
