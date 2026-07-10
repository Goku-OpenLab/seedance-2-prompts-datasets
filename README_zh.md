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
- 总 Prompt 数量：**7013**
- 今日更新（UTC 2026-07-10）：**13**

## 🎬 今日更新
### 🎬 世界杯绝杀与重逢悬念
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07673.jpg" width="480" alt="SD2_07673"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/world-cup-bicycle-kick-cliffhanger-SD2_07673">🌐 在线观看</a>

#### 📝 Prompt
```
第一部分（0–15秒） 剪辑1（0–5秒）——更衣室回忆 马特奥独自坐在空荡荡的更衣室里，比赛开始前。慢慢推入。《Match》切入一段冷调的闪回，Elena站在门口。埃琳娜：“我受够你了。”她走开了。Hard切回现在，Mateo拿起队长的臂章，朝隧道走去。第二轮（5–10秒）——决赛开始 马特奥独自走出隧道，走向喧嚣的世界杯决赛。起重机镜头显示了拥挤的体育场，随后降至场地水平。他接到一个轻松传球后犹豫，最终失去控球权。第三回合（10–15秒）——LookA防守球员在Mateo慢跑时嘲讽他。后卫：“雷耶斯，你今天脑子怎么了？”人群摄像头在巨型大屏幕上找到了埃琳娜。她双手捧起，喊道，埃琳娜：“打得像你是认真的！”马特奥抬头。随着时间流逝，他们的目光在体育场上交汇。第二部分（15–30秒）切入4（15–19秒）——转折点 马特奥截球并带球突破两名防守球员，进行低角度追踪射门。画面切换到埃琳娜焦急地在看台上观看。第五轮（19–24秒）——球门侧跟踪摄像机全程跟随马特奥。完美的十字架传到了。马特奥在镜头环绕他旋转时完成了精彩的倒钩踢。让马特奥在踢球过程中完全可见。画面切到球飞入球门上角。进球后立刻硬切。没有庆祝。没有射门。切入6（24–30秒）——重聚与悬念马特奥已开始冲向观众护栏。埃琳娜冲上前。马特奥：“你回来了。”埃琳娜：“我必须告诉你一件事。”就在他们的手即将接触时，一个穿着深色大衣的神秘男子走到埃琳娜身后，坚定地抓住了她的肩膀。他的身体可见，但脸部依然隐藏着。埃琳娜惊恐地转过身。马特奥僵住了。画面切换到黑。结尾卡 第一集即将上线
```

#### 📌 Details
- Ratio: `0.56` | Duration: `29.47s`

---

### 🎬 冰原极速生死赛
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07671.jpg" width="480" alt="SD2_07671"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/arctic-ice-racer-survival-SD2_07671">🌐 在线观看</a>

#### 📝 Prompt
```
“一个危险的摩托冰上赛车手，穿着覆盖着霜冻的黑色赛车装备，头盔面罩是反光，头盔大灯能穿透暴风雪。蓝色时分暮光下的冰冻北极工业废土。冰路、废弃的钻井平台、冰桥、坍塌的隧道、被积雪覆盖的集装箱和暴风雪的能见度。黑暗电影感的电子舞曲，配以深沉的次低音脉冲。冰摩擦、引擎轰鸣、链条振动、雪地撞击和刺骨寒风主导了整个音景。超逼真的赛车摄影与生存惊悚美学和高端冬季广告相结合。射击1：超低速前轮跟踪镜头以危险速度穿越厚厚的冰尘。镜头2：快速转向接近撞击的漂移，绕过冰冻的工业残骸。照片3：宽景航拍，展示摩托车在巨大的冰冻海面上飞驰，穿梭于废弃建筑之间。镜头4：长镜头跳拍，飞越破碎的冰面，雪花在摩托车后方爆裂。第五击：在悬崖边缘几英寸处长时间横向漂移时的圆形侧向跟踪镜头。第六幕：在白茫茫情况下穿越坍塌的冰冻隧道，完成最后不可能的跳跃。骑手剧烈着地，在黑冰上甩尾，随后缓缓停在闪烁的工业灯光下，暴风雪般的风将画面吞噬。音乐瞬间切断。”
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.17s`

---

### 🎬 黑人滑手扶手杆绝技
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07669.jpg" width="480" alt="SD2_07669"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/skater-handrail-grind-kickflip-SD2_07669">🌐 在线观看</a>

#### 📝 Prompt
```
主题：黑人男性，长长的深色脏辫，黑色针织毛线帽，素黑色圆领T恤，黑色袖口牛仔裤，黑色胶底滑板鞋。从楼梯顶开始，奥利跳到扶手上，磨蹭整条扶手到底部，干净着陆，短暂滚出，然后踢翻并平稳落地。 地点：加州户外广场——浅灰色混凝土楼梯，钢制中央扶手，极简建筑，棕榈树投下长长的阴影，明亮温暖的正午阳光，自然的镜头光晕。 视觉风格：干净且逼真的滑板视频风格——自然肤色，逼真的面料和头发动作，灰色混凝土与黑色服装之间的清晰日光对比。快速移动时有细微的运动模糊，全程对骑手的清晰聚焦。 摄像头：楼梯顶端安装低角度跟踪摄像头进行奥利-on，然后沿滑轨跟踪，高度与下降速度匹配。每个动作顶点（奥利-昂、踢翻）处有短暂的慢动作保持。结尾是他滚动离开时稳定的跟踪镜头。 时间戳： 00：00–00：01 设置：滑冰者站在楼梯顶端，滑板斜向栏杆，低角度凸轮轴面向他，准备推地。 00：01–00：02 奥利-奥：板子弹出，~35%慢动作保持顶点，转向架在轨道顶上方排列，凸轮随弹跳向上移动。 00：02–00：02.5 轨道接触：卡车着陆在轨道顶部，全速撞击，微妙的凸轮抖动以传递接触。 00：02.5–00：05 滑轨下降：滑板轨道沿着轨道滑行，滑板者在楼梯上平滑，双臂张开保持平衡，楼梯略微模糊过凸轮。 00：05–00：05.5 着陆：从轨道底部弹出，干净利落地在平地上，凸轮保持稳定在地面水平。 00：05.5–00：06.5 滑行：以正常速度短暂前滚，凸轮轨道在稍远处并排行驶。 00：06.5–00：08 踢翻：板子在空中翻转，~35%慢动作保持在峰值显示旋转，侧面轮廓摄像头在板高处。 00：08–00：09 踢翻着地：旋转完成，正好落在握把胶带上，全速恢复，撞击时凸轮轻微抖动。 00：09–00：10 分辨率：摄像机拉远，稳定地跟踪广角镜头，同时滚动离开画面中干净的自然阳光。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.13s`

---

### 🎬 最终回放：冠军的秘密
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07667.jpg" width="480" alt="SD2_07667"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/final-replay-champions-secret-SD2_07667">🌐 在线观看</a>

#### 📝 Prompt
```
标题：“最终重赛”** **持续时间：** 15秒 **风格：** 电影般的体育剧情，高级电影风格，逼真的灯光，浅景深，情感丰富的表演，极其细致的写实，戏剧性的管弦乐配乐，伴随着远处观众氛围。 --- ### 第一场 — 背叛揭晓（0–5秒） 极近的特写，金发女子手中颤抖的智能手机。 手机屏幕上显示着冠军庆典的照片：足球明星骄傲地站在世界杯奖杯旁，一位优雅的黑发女子微笑着站在他身旁，佩戴着他的冠军奖牌。 一滴泪水落在屏幕上，模糊了画面。 画面切换到一位亲密的金发女子悲痛的表情，远处回荡着舞厅音乐。 她轻声低语： **“你答应过我今晚是属于我们的......”** 镜头从背后跟随她独自站在高耸舞厅门之间，凝视着外面的庆典。 舞厅内部： * 世界杯奖杯展示柜在聚光灯下闪耀。 * 国旗悬挂在天花板上。 * 巨型回放屏幕显示锦标赛决赛的精彩集锦。 * 宾客们在金色吊灯下庆祝。 情绪：心碎、难以置信、孤立。 --- ### 第二场 — 秘密（5–12秒） 画面切换到这位足球冠军穿着黑色西装外套，外面是敞领白衬衫，冠军奖牌挂在脖子上。 他突然僵住，仿佛察觉到有什么不对劲。 黑发女子自信地穿过人群走近。 她轻轻地把一只手放在他的手臂上。 片刻后，她的手指轻轻触碰到他胸前的奖牌。 近距离面对面构图。 庆祝的声音在低沉戏剧性的配乐下渐渐消退。 她靠近，轻声说道： **“秘密也能赢得奖杯。”** 那人一言不发。 他的表情从困惑转为担忧。 情绪：紧张、操控、内心冲突。 --- ###场景3 — 最终重播（12–18秒） 那女人后退一步，举起酒杯，带着会心的微笑。 她瞥向舞厅地板上方巨大的回放屏幕。 足球精彩片段继续在头顶播放，宾客们在下方庆祝，却浑然不觉附近正在紧张气氛的发生。 她慢慢把酒杯举到嘴边。 她没有看他，轻声说道： **“等他们看到最终回放。”** 她慢慢抿了一口酒。 镜头对准这位足球冠军的脸，他的表情变得严肃，充满担忧。 切入现场
```

#### 📌 Details
- Ratio: `0.56` | Duration: `29.2s`

---

### 🎬 动画师的灵感时刻
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07666.jpg" width="480" alt="SD2_07666"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/animator-character-inspiration-SD2_07666">🌐 在线观看</a>

#### 📝 Prompt
```
第一部分： “动画师在挣扎着想出点子。这让他变得疯狂。他把画扔了。又试了一次。拉了拉他的胡须。重新开始。纸张被扔进垃圾桶。 喜剧。动画风格。多场景。高端动画。” 第二部分（附上第一部分视频作为参考） “继续这个视频。 在努力构思角色概念后，艺术家深吸一口气，对自己说要集中注意力。 然后他画了一个美丽又酷炫的公主，手持枪械。他骄傲地举起它，低声说：就是这样。 喜剧。动画风格。多场景。高端动画。”
```

#### 📌 Details
- Ratio: `1.78` | Duration: `35.29s`

---

### 🎬 雨停时刻
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07665.jpg" width="480" alt="SD2_07665"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/the-day-time-stuttered-SD2_07665">🌐 在线观看</a>

#### 📝 Prompt
```
变形宽银幕21：9电影，超现实心理惊悚片。白天的时光断断续续。0-4：一个极度忙碌的[设定]。突然间，所有声音归零，所有人、车辆和坠落物体在移动中瞬间僵住。镜头缓缓掠过静止的身影。4-8镜头：变形宽银幕低角度跟踪镜头。一个孤独的[角色]缓缓穿过冰冷的人群，穿梭于悬浮的雨滴和冰冷的水花之间。椭圆形散景在静止的水面上闪烁。8-12秒：极端眩晕旋转——摄像机围绕一处冻结的[粒子/水]爆炸旋转360度，展现不可能的冻结物理。水平的霓虹灯光芒穿透画面。12-15秒：角色伸手触摸一滴冰冻的水滴。时间瞬间倒流——声音的海洋回归，水流倾泻而下，人们快速同步移动。镜头迅速向天空退去，21：9的辉煌画面。照片级写实的8K，大卫·芬奇风格的摄影精准，变形宽银幕定焦镜头，体积雨，时间锁定物理。变形宽银幕21：9电影，超现实心理惊悚片。白天的时光断断续续。0-4：纽约一条被雨水打湿、交通繁忙的人行横道。突然间，所有声音归零，每个人、车辆和落下的雨滴都瞬间僵住。镜头缓缓掠过静止的身影。4-8镜头：变形宽银幕低角度跟踪镜头。一位身穿黄色大衣的孤独女子缓缓穿过冰冷的人群，穿梭于悬浮的雨滴和冻结的黄色出租车水花之间。椭圆形散景在静止的水面上闪烁。8-12秒：极度眩晕旋转——摄像机围绕水坑的冰水环绕360度旋转，展现不可能的冻结物理效果。水平的霓虹灯光芒穿透画面。12-15秒：女子伸手触摸一滴冰冻的水滴。时间瞬间倒流——声音的海洋回归，水流倾泻而下，人们快速同步移动。镜头迅速向天空退去，21：9的辉煌画面。照片级写实的8K，大卫·芬奇风格的摄影精准，变形宽银幕定焦镜头，体积雨，时间锁定物理。
```

#### 📌 Details
- Ratio: `1.74` | Duration: `15.13s`

---

### 🎬 亮片裙变装秀
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07664.jpg" width="480" alt="SD2_07664"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/sequin-dress-glow-up-SD2_07664">🌐 在线观看</a>

#### 📝 Prompt
```
[全球视野与基调]电影感十足的15秒片段，快节奏的抖音“抓着擦拭”爆发镜头。核心特效：物体捕捉、镜头擦除匹配剪辑、慢动作走秀和吸引目光的背景群众演员。音频教学：严格禁止背景音乐。纯粹的ASMR音效设计（布料卡住声、厚重擦拭镜头、湿滑沥青上高跟鞋清脆的敲击声、闷闷的城市街道氛围）。真人真人（女性面部基础input_file_0.png）。高端时尚、前卫且充满魅力的美学。 [镜头分解][0.0-5.0秒] 现实（镜头1）：明亮现代房间的静态中景。主角（input_file_0.png）自信地穿着休闲时尚的极简服装（时尚的夏季无袖上衣和牛仔短裤）。突然，一件华丽且高度反光的白色亮片迷你裙（高级定制）从画面外飞入画面。她一只手轻松接住了它。她自信地微笑，迈出有力的步伐，粗暴地将闪亮的白色连衣裙直接推向镜头，屏幕被遮蔽。ASMR布料捕捉和厚重布擦拭。 [5.0-15.0秒] 街头超级巨星揭晓（5次快速射击）： [5.0-6.5秒] 镜头2（比赛剪裁揭示）：布料被猛烈拉开！爆炸性的火柴切割。夜晚，房间变成了一条充满活力、霓虹灯闪烁的城市街道。主角现在完全变身，穿着她捕捉到的那件令人屏息的白色亮片高级迷你裙。这件裙子在路灯下闪闪发光。 [6.5-8.5秒] 镜头3（动态走秀）：中等跟踪镜头，后退移动。她在湿漉漉的柏油路上展现出强劲自信的高潮T台步伐。她那锋利优雅的造型在阴暗的城市背景中格外突出。 [8.5-10.5秒] 镜头4（吸引头角者）：慢动作广角跟踪镜头。当她自信地走过时，背景模糊的群众演员（路人）明显停下脚步，转头惊叹，完全被她的气场迷住。 [10.5-12.5秒] 镜头5（低角度细节）：低角度跟踪镜头，聚焦于她极其修长的双腿和闪亮的钻石高跟鞋在霓虹灯下有节奏地敲击。ASMR尖锐的脚跟咔嗒声。 [12.5-15.0秒] 镜头6（最终定格）：她脸部极近特写。完美抖音风格妆容（光泽唇部，光泽玻璃肌肤V10.2）。电影般的城市风吹拂着她完美造型的头发。她直视镜头，带着锋利、魅力且傲慢的笑容，知道自己掌控了这条街。画面渐渐变黑。柯达Vision3 500T胶片画面，漂亮的变形镜头光晕。
```

#### 📌 Details
- Ratio: `0.56` | Duration: `10.13s`

---

### 🎬 萌妹高速达摩变脸秀
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07663.jpg" width="480" alt="SD2_07663"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/cute-daruma-pose-switch-SD2_07663">🌐 在线观看</a>

#### 📝 Prompt
```
だるまを見てこちらを見てまただるまを見てこちらを見てを繰り返す。こっちを見た瞬間はカワイイポーズ、高速で何回も繰り返す、こちらを見る時は頬にだるまをくっつけて「キラーン」とつぶやく。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `8.0s`

---

### 🎬 红黑魅影舞台
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07662.jpg" width="480" alt="SD2_07662"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/moody-red-black-kpop-stage-SD2_07662">🌐 在线观看</a>

#### 📝 Prompt
```
风格：情绪浓郁，高对比的K-pop，单色饱和布景（深红/深红配黑色），戏剧性聚光灯，慢节奏落下渐进 主题：女偶像，结构化的红黑服装，带有透视/金属面板细节 [0：00-0：03] 特写，表演者的手从黑暗中出现，形成单一聚光灯，节拍缓慢揭示面部，镜头拉远至红色环幕前的完整剪影。[0：03-0：07] 广角镜头，锐利的编舞，红色背景下有强烈的阴影效果，镜头缓慢横向移动，戏剧性的聚光灯追逐她的动作。[0：07-0：11] 中景，表演者坐在极简王座上的钩子台词，场景快速切换到戏剧性的红色雾气舞台背景。[0：11-0：15] 三重剪辑的强力姿势分别从不同角度（侧面、顶部、背面）照明，定格英雄姿势配红色雾霾爆发，打孔，淡入标志。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `14.13s`

---

### 🎬 猩红执法者登场
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07661.jpg" width="480" alt="SD2_07661"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/borus-cyber-jungle-enforcer-SD2_07661">🌐 在线观看</a>

#### 📝 Prompt
```
请使用@[Borus角色表]作为Borus的权威角色参考：红色猿猴状网络丛林执法者，黑色面部毛发，黄色眼睛，灰色战术背心配徽章，超大机械护臂，深色工装裤，白色靴子，长长的红色尾巴。
```

#### 📌 Details
- Ratio: `0.75` | Duration: `12.07s`

---

### 🎬 闪光灯恶作剧
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07659.jpg" width="480" alt="SD2_07659"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/flash-prank-friend-SD2_07659">🌐 在线观看</a>

#### 📝 Prompt
```
【角色身份锁定】使用参考图像作为严格的恒等参考。年轻女性必须在整个视频中保持与参考完全相同的面部结构、面部特征、比例、肤色和整体外观。无论场景、灯光、面部表情或语言如何，她的身份和族裔都必须完全不变。制作一部超逼真的手持智能手机抓拍视频，拍摄在夜晚或昏暗室内环境中。相机非常靠近主体，但避免极端的面部裁剪。画面中保持头顶、部分肩膀和举起的手可见。这张照片应该让人感觉像是亲密朋友手里拿着手机，突然打开闪光灯逗她。一道刺眼的智能手机闪光直接射向她的脸，使灯光突然变得异常明亮。她本能地举起一只手挡住额头和眼睛，挡住光线。她的手掌和手指自然进入前景，营造出逼真的部分遮挡效果，但又不完全遮住她的脸或面部特征。她微微歪头，自然地眯起眼睛，轻轻皱起眉头，微微皱起鼻子。她的表情中带着轻微的恼怒，夹杂着调皮的尴尬和好笑，仿佛在回应亲密朋友的调侃。她不应该显得愤怒、冷漠或过于戏剧化。相反，捕捉当朋友的恶作剧打断他时，他真实的表情。她一边遮住眼睛，一边自然地说：“别这样。”说出这句话时要轻柔随意，就像本能反应不经思考地脱口而出。她的口型同步应当精准自然，口型和说话节奏都真实，绝不夸张。说完后，她的表情渐渐放松，露出一抹不情愿的微笑，暗示虽然有些恼火，但最终还是觉得这件事很有趣。保持高度逼真的皮肤细节，包括可见毛孔、细微瑕疵、淡淡的痤疮标记、自然肌肤质地、柔和的面部光泽、脸颊纹理以及鼻梁上的真实挑染。她的嘴唇应有自然的水润和柔和的反光，但不会显得光泽或浓妆。避免任何美貌过滤的外观。她的头发自然垂落，额头上有几缕松散的发丝。几缕发丝贴着她的皮肤，自然地轻轻摆动。背景应高度模糊，采用柔和的深蓝和紫色夜间环境光，搭配散景散景灯。整体画面应当像是真实的智能手机闪光视频，而非广告、时尚拍摄或摆拍制作。强调日常真实感、真实互动、细腻的微表情、自然的语言表达以及略显不完美的构图。手持手机的感觉应该很明显，有轻微的自然晃动和轻微的呼吸动作，就像随意用智能手机录制的那种感觉。时间线 0–2秒 一个朋友突然打开了手机闪烁。明亮的闪光从正面照亮了她的脸。镜头非常近，手持移动很细微。她短暂地被吓了一跳。2–4秒 她本能地举手挡住光线，微微转头，眯眼，轻轻皱眉，自然反应。4到6秒，她仍在遮挡灯光，轻声说：“停下。”她的对嘴动作清晰自然，节奏真实，语调真实，仿佛在回应一位调皮的朋友。6–8秒 她继续部分遮挡光线，同时短暂移开视线。她的表情逐渐从轻微的恼怒转为勉强的好笑。8–10秒 她稍微放松了。她的手依然在前景，但不再挡住那么多光线。她嘴角浮现出一丝微笑，显然被这个玩笑打动了。视频结束时保持着近距离手持智能手机的自然风格。负面提示：请勿使用极端的面部裁剪。不要让手完全遮住脸部。避免畸形的手、多余的手指、僵硬的表情、无神的眼神、缺失的眨眼、错误的口型同步、说话时僵硬的口型动作、音频和唇形不匹配、夸张的表演、冷漠或无感情的表情、AI风格的塑料皮肤、过度的皮肤平滑、美妆滤镜、网红风格滤镜、浓妆、假摄影、商业或电影广告美学、摄影棚灯光、漂移的面部特征、杂乱的背景， 字幕、文字、标志、水印、手机状态栏、播放控制、屏幕闪烁、突然切换或突然切换镜头。无论如何都不要更改受试者的族裔。不要亚洲化、西化或以其他方式改变面部特征。角色的身份必须在整个视频中忠实地与参考图像保持一致。
```

#### 📌 Details
- Ratio: `0.56` | Duration: `10.06s`

---

### 🎬 尼罗河畔古埃及日常
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07657.jpg" width="480" alt="SD2_07657"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/nile-farmer-ancient-egypt-SD2_07657">🌐 在线观看</a>

#### 📝 Prompt
```
这是一部手持纪录片，使用2000年代初的消费级DV摄像机拍摄，跟踪一名年轻人穿过尼罗河沿岸的一个农村。这些录像应当像真实、不完美的古埃及日常生活家庭录像。 那人二十出头。他留着短短的深色头发，皮肤温暖的棕色，带有户外工作带来的自然质感，穿着简单的白色亚麻短裙，系着腰带。他的身体状况显示出从事重度农业和建筑劳动的特征。 环境是靠近河流的简朴埃及村庄：泥砖房屋、麦田和亚麻田、灌溉渠道、棕榈树，以及几头穿梭的驴和牛。 录像跟随他开始一天的开始，他用两头牛拉的木犁在田间工作，引导动物沿着灌溉渠道前进。然后他走到其中一个水道，用木制工具清理泥土和杂物。后来他提着一个大篮子走向河边，加入了将收获作物装上小木船的男子。回村途中，他停下来帮忙用泥砖修复一段灌溉渠道。他最终在家附近完成，坐在地上用石头磨着木制工具。 镜头跟随他，手持手感自然，构图漂移，弯腰或快速移动时自动对焦问题，明场与阴影区的曝光变化，偶尔出现运动模糊。 只有自然的声音：水流在水道中流淌，远处动物的叫声，工具敲击泥土和木头的声音，其他工人的声音，还有轻微的风声。没有音乐。 结果必须像是用一台老式摄像机拍摄的古埃及日常农业生活的真实、抓拍画面。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `15.08s`

---

### 🎬 天穹闭合
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07655.jpg" width="480" alt="SD2_07655"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/planetary-shutters-closing-SD2_07655">🌐 在线观看</a>

#### 📝 Prompt
```
10秒的电影科幻动作戏，16：9，超写实，规模惊艳，物理物理逼真，没有露脸。 一架战斗机飞越了一个巨大的人工世界。 内陆包含大陆、城市和海洋。 突然，行星防御系统启动。 巨大的装甲板开始在天空中滑动。 每个板块宽达数百公里。 世界实际上正在关闭。 阳光会一点点消失。 飞行员穿梭在逐渐狭窄的光走廊中。 整个景观被移动的盔甲掩盖。 剩余的开口越来越小。 战斗机俯冲向最后一个可见的空隙。 行星的百叶窗在他身后相撞。 停。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.13s`

---

### 🎬 飞鸟随乐消散
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07654.jpg" width="480" alt="SD2_07654"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/birds-dissipate-music-SD2_07654">🌐 在线观看</a>

#### 📝 Prompt
```
&lt;视频&gt;中的鸟类松散地基于&lt;图像&gt;形成了鸟类不完美的形状。它们随着&lt;音频&gt;的音乐移动，飞行时逐渐消散
```

#### 📌 Details
- Ratio: `1.78` | Duration: `8.25s`

---

### 🎬 公寓灯光随乐起舞
<img src="https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main/seedance-2/covers/1/SD2_07653.jpg" width="480" alt="SD2_07653"><br>
<a href="https://prompthub.gokuscraper.com/en/seeddance2/prompt/apartment-lights-music-sync-SD2_07653">🌐 在线观看</a>

#### 📝 Prompt
```
公寓的灯光随着音乐同步亮起。
```

#### 📌 Details
- Ratio: `1.78` | Duration: `10.04s`

---

<!-- STATS_END -->
