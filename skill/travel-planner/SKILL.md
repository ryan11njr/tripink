---
name: travel-planner
description: 规划旅行并生成高审美互动行程网页（含实时天气/导航路线/导游讲解/预算仪表盘，支持杂志纸刊/手账拼贴/针织暖物等展示模式）。Use when the user wants to plan a trip, 自驾游, 旅游攻略, 行程规划, research destinations (weather/tickets/小红书经验帖), iterate an itinerary, or generate a travel-plan HTML site/PDF. Triggers: 旅行计划、旅游攻略、自驾游、行程规划、trip planner、itinerary、去XX玩.
---

# Travel Planner · 旅行规划 → 高审美互动网页（v2）

> 项目代号 **TripInk**——Your trip, in ink. 把旅行写进墨里：读懂你 → 查证世界 → 把行程印成可交互的旅行杂志。
> **适用任何支持 SKILL.md 约定的智能体**（Claude Code、Codex 等）。文中工具名按平台替换：Claude Code 用 MCP 搜索/阅读工具，Codex 用内置 browsing / web search，其余平台同理。

产出物：单文件互动 `index.html`（海拔剖面 + 真实导航路线 + 每日分页 + 导游级讲解 + 按到达日期实时天气 + 美食住宿 + 预算仪表盘），可选 `行程手册.md/.pdf` 与 GitHub Pages 发布。

**总原则**
1. 用户往往不了解目的地——一切事实（票价/预约规则/天气/油价/店名）必须联网查证，**每个数字标注 [来源+日期]，查不到就标"未核实"，绝不编造**。
2. 先读懂人、再查世界、再谈方案；**用户点头后才写完整 HTML**。
3. 预算口径全程一致（人数×门票、人均=总计÷人数）；隐私项（如住宿花费）先问是否展示。
4. 呈现即内容的一半：**先读行程的性格，再选主题与展示模式**（参考 references/zine-modes.md）。

---

## Phase 1 · 问卷（用所在平台的交互提问机制，如 Claude Code 的 AskUserQuestion；无此机制则对话逐批提问。每批 ≤4 问）

**第一批（必问）**：出发地 / 目的地（可模糊）· 出发日期与天数 · 人数（大人+小孩）· 出行方式（自驾/高铁+租车/飞机+租车/包车/公共交通）。
**第二批（必问）**：消费习惯（经济/舒适/轻奢）· 旅行风格（紧凑多看/网红出片/随性体验/慢节奏自然/历史深度/亲子）· 节奏容忍（≤5h / 6–8h / 10h+ 硬日可接受）· 必去清单 & 雷区。
**第三批（按需）**：自驾→车型油耗/司机数/油号；亲子→孩子年龄；预算上限；是否发布上网。

## Phase 1.5 · 读懂这趟旅行（隐性需求探测）

从问卷与闲聊中主动识别并**复述确认**（"我理解你们更想要 X，对吗"）：

| 信号 | 隐性需求 | 主动做法 |
|---|---|---|
| 带老人/小孩 | 节奏要松、医疗近、少换乘 | 每日压缩一个锚点、备减负方案 |
| 纪念日/生日/蜜月 | 要仪式感 | 推荐日落机位、纪念餐厅、惊喜环节 |
| 反复问价格 | 预算敏感 | 给省钱替代矩阵 + 每项 ± 区间 |
| 反复问出片 | 拍照优先 | 机位/时段/穿搭色建议进 TIPS |
| 时间卡死（请假难） | 容错低 | 每天给"来不及就砍 X"的优先级 |
| 只说"随便/你定" | 决策疲劳 | 直接给 2 个成稿方案二选一，别再追问 |
| 目的地含糊（"想去西北"） | 需要被启发 | 先给 3 条风格化路线概念再收敛 |

## Phase 2 · 研究（多源交叉验证）

工具：用你可用的联网搜索与网页阅读工具（Claude Code：`mcp__web-search-prime__web_search_prime(location:"cn")` → `mcp__web-reader__webReader` / `WebFetch`，GitHub 项目用 zread MCP；Codex：内置 browsing / web search）。

**交叉验证矩阵**（关键事实至少两源，单源须标注"单源"）：
官方（景区公众号/官网/研究院）→ OTA（携程/美团门票页）→ UGC（小红书/马蜂窝/大众点评）→ 短视频（抖音经验）→ 结构化数据（Open-Meteo 天气、OSRM 路线、qiyoujiage 油价）。
**时效规则**：票价 ≤1 年内来源；油价 ≤1 次调价周期；**预约规则（莫高窟类热门窟/馆）出发前必查**，预约窗口是硬约束、先查再排期。

免 key 端点（模板已内置，规划期可先测通）：
- 天气 `api.open-meteo.com/v1/forecast?latitude=..&longitude=..&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,relative_humidity_2m_mean,uv_index_max,sunrise,sunset,precipitation_sum,wind_speed_10m_max&timezone=Asia/Shanghai&start_date=..&end_date=..`
- 真实道路 `router.project-osrm.org/route/v1/driving/{lon,lat;...}?overview=full&geometries=geojson`
- 油价 `qiyoujiage.com/92|95.shtml`；过路费≈0.4–0.5 元/km（一类客车，用游记交叉验证）；里程优先地图口径，直线×1.25 须标"估算"。

每站清单：天气 → 门票/预约 → 必吃+具体店+人均 → 住宿分区 → 3–5 条经验帖 tips → 里程驾时 →（自驾）加油/限速/垭口。

## Phase 2.5 · 主动推荐引擎（每轮迭代必须附）

不是等用户问，而是每轮主动给出（标注"建议，可拒绝"，附理由与来源）：
1. **一个隐藏玩法**：小众替代（"人多可去 X，小红书反馈更好"）
2. **一个省钱点**（"A 类票→应急票省 414/3 人"）
3. **一个风险预警**（海拔/预约/天气窗口/连续硬日）
4. **一个仪式感彩蛋**（日出机位、纪念日餐厅、给同行者的讲解梗）

## Phase 3 · 迭代（先纸面后代码）

给：① 总览表（日/城市/里程/驾时/强度/亮点）② 预算框架（类目+人均+区间，注明假设）③ 关键风险。连续硬日主动给减负备选。通常 2–3 轮，用户明确确认后才构建。

## Phase 4 · 主题 × 展示模式（二维选择）

- **主题（配色/字体）**：见 `references/themes.md` 六套（丝路矿物料/高原清冽/都市霓虹/海滨假日/水墨留白/山野暖木）。
- **展示模式（版式语言）**：见 `references/zine-modes.md` 四式（纸刊杂志/手账拼贴/针织暖物/极简档案）。
向用户报"主题+模式"组合与一句效果描述确认（如"矿物料 × 纸刊杂志：像一本敦煌画册"）。

## Phase 5 · 构建

1. 复制 `references/template.html`；2. 换主题 tokens；3. 按模式套版式（zine-modes 的 CSS 配方）；4. 换数据 `ELEV/DAYS/TIPS/GSRC/GIMG`（规范见 `references/data-schema.md`）；5. 换标题/brand/Latin 副标；6. 无配图则 `GIMG={}`（onerror 自动隐藏）。
**QA 必做**：零 JS 报错；逐日渲染；天气 API 真实返回；预算自洽（每日小计和=仪表盘=首页大数字）；375px 移动端；PDF 输出（若需）背景色完整。
手册（可选）：仓库 `gen_handbook.js`/`render_pdf.js` 出 md+pdf；Word 可按 `gen_docs.js` 先例（docx-js）生成；或手写等价 MD。

## Phase 6 · 发布（可选，先问）

有 `gh` CLI 则用下列命令；无则在 GitHub 网页手动建仓库并开启 Pages（Settings → Pages → main / root），且根目录加空文件 `.nojekyll`：

```bash
mkdir -p publish/img && cp index.html 行程手册.* publish/ && cp -r img/. publish/img/
cd publish && git init -b main && git add -A && git commit -m "trip site"
gh repo create <name> --public --source=. --remote=origin --push
gh api --method POST repos/<owner>/<name>/pages -f "source[branch]=main" -f "source[path]=/"
touch .nojekyll && git add -A && git commit -m nojekyll && git push   # 防 Jekyll 吞 .md
```
curl 200 验证后再交付链接。

## 反模式
❌ 未查证就写票价/天气/店名；❌ 用户没确认就产出全量 HTML；❌ 只答不荐（缺主动推荐四件套）；❌ 口径漂移（门票 4 人预算 3 人）；❌ 网页引本地依赖（须单文件自洽，仅 img/）；❌ 忽略预约硬约束；❌ 高原/长下坡/儿童座椅等安全提醒缺失；❌ 拿模板硬套——先读行程性格再选呈现。
