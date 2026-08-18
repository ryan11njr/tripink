---
name: travel-planner
description: 规划旅行并生成高审美互动行程网页（含实时天气/导航路线/导游讲解/预算仪表盘）。Use when the user wants to plan a trip, 自驾游, 旅游攻略, 行程规划, research destinations (weather/tickets/小红书经验帖), iterate an itinerary, or generate a travel-plan HTML site/PDF. Triggers: 旅行计划、旅游攻略、自驾游、行程规划、trip planner、itinerary、去XX玩.
---

# Travel Planner · 旅行规划 → 高审美互动网页

产出物：单文件互动 `index.html`（海拔剖面 + 真实导航路线 + 每日分页 + 导游级景点讲解 + 按到达日期实时天气 + 美食住宿 + 预算仪表盘），可选配套 `行程手册.md/.pdf` 与 GitHub Pages 发布。

**总原则**
1. 用户往往不了解目的地——一切事实（票价/预约规则/天气/油价/店名）必须联网查证，**每个数字要有来源 URL；查不到就标"未核实"，绝不编造**。
2. 先问卷、再研究、再和用户迭代确认行程，**用户点头后才写完整 HTML**。
3. 预算口径全程一致：人数、门票按人数、人均 = 总计 ÷ 人数；涉及隐私（如住宿花费）先问用户是否展示。

---

## Phase 1 · 问卷（AskUserQuestion，每批 ≤4 问）

**第一批（必问）**
1. 出发地 / 目的地（目的地可模糊，如"大西北"，由你建议路线）
2. 出发日期与天数（含往返交通时间）
3. 人数：大人几位、小孩几位（小孩影响门票/行程强度）
4. 出行方式：自驾 / 高铁+当地租车 / 飞机+租车 / 包车 / 纯公共交通

**第二批（必问）**
5. 消费习惯：经济（快捷/青旅）· 舒适（连锁中端）· 轻奢（四星+/特色民宿）
6. 旅行风格（决定景点取舍与 UI 主题）：紧凑多看景点 / 网红打卡出片 / 随性体验 / 慢节奏自然 / 历史文化深度 / 亲子友好
7. 节奏容忍：轻松（≤5h/天）· 适中（6–8h）· 紧凑（可接受 10h+ 硬日）
8. 必去清单 & 雷区（去过不想再去的、忌口、恐高/高反等）

**第三批（按需）**：自驾→车型与油耗、几位司机、是否加 95/92 号；亲子→孩子年龄；预算上限；是否需要发布上网。

## Phase 2 · 研究（实时信息，缺一不可）

工具与端点（中国内容优先 `mcp__web-search-prime__web_search_prime`，参数 `location:"cn"`；读页用 `mcp__web-reader__webReader` / `WebFetch`）：

| 需求 | 做法 |
|---|---|
| 小红书/马蜂窝经验帖（美食、避坑、tips） | 搜"XX 小红书 必吃/避坑/攻略"，取具体店名与人均 |
| 门票 + 预约规则 | 搜"XX 门票 2026 预约 提前几天 官方"；**热门窟/馆类（莫高窟、陕历博等）预约窗口常是硬约束，先查再排期** |
| 天气 | Open-Meteo 免费无 key：`https://api.open-meteo.com/v1/forecast?latitude=..&longitude=..&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,relative_humidity_2m_mean,uv_index_max,sunrise,sunset,precipitation_sum,wind_speed_10m_max&timezone=Asia/Shanghai&start_date=..&end_date=..`（生成的网页会按"到达日期"自动实时取数，模板已内置；断网回落常年气候值，需填 DAYS[].climate） |
| 真实导航路线 | OSRM 免费无 key：`https://router.project-osrm.org/route/v1/driving/{lon,lat;lon,lat;...}?overview=full&geometries=geojson`（模板已内置，规划期可先测通连通性） |
| 油价 | qiyoujiage.com/92.shtml / 95.shtml（分省价，注明调价日期）；过路费≈0.4–0.5 元/km（一类客车），用游记交叉验证 |
| 里程 | 优先地图口径；无则直线 ×1.25 并标注"估算" |
| 日出日落/海拔 | Open-Meteo 返回；海拔用行政区划常识并复核 |

每站研究清单：天气 → 门票/预约 → 必吃+具体店 → 住宿区域建议 → 3–5 条经验帖 tips → 里程与驾时 → （自驾）加油/限速/垭口提醒。

## Phase 3 · 迭代（先纸面后代码）

给出：① 总览表（日/城市/里程/驾时/强度/亮点）；② 预算框架（类目合计+人均+区间，注明假设）；③ 关键风险（预约窗口、高原、连续硬日、季节闭园）。
- 连续硬日主动给"减负备选"（换住宿点平衡里程）。
- 通常 2–3 轮修改；用户明确说"可以/就这样"才进入构建。

## Phase 4 · UI 主题（按旅行风格选，见 references/themes.md）

紧凑多看/历史文化→`silk-mineral`；自然/雪山湖泊/慢节奏→`alpine-fresh`；网红打卡/都市美食→`urban-pop`；海滨/亲子→`seaside-breeze`；江南古镇人文→`ink-wash`；徒步露营山野→`forest-warm`。向用户报主题名+一句配色描述确认。

## Phase 5 · 构建

1. 复制本 skill `references/template.html`（即 demo，含全部交互逻辑）。
2. 换 **主题 tokens**（`:root` 调色板/字体、body 背景渐变、强度色、海拔剖面渐变色）。
3. 换 **数据**：`ELEV / DAYS / TIPS / GSRC / GIMG`，字段规范见 `references/data-schema.md`。
4. 换标题/brand/hero 文案与 Latin 副标（拼音大写）。
5. 配图可选：无图则 `GIMG={}`（模板 onerror 自动隐藏，不破版）。
6. **QA 必做**：无 JS 报错；逐日可渲染；天气 API 真实返回；预算自洽（每日小计之和 = 仪表盘总计 = 首页大数字）；移动端 375px 可用。
7. 手册（可选）：同仓库有 `gen_handbook.js`/`render_pdf.js` 可生成 md+pdf；不在仓库时手写等价 MD。

## Phase 6 · 发布（可选，先问）

```bash
mkdir -p publish/img && cp index.html 行程手册.* publish/ && cp -r img/. publish/img/
cd publish && git init -b main && git add -A && git commit -m "trip site"
gh repo create <name> --public --source=. --remote=origin --push
gh api --method POST repos/<owner>/<name>/pages -f "source[branch]=main" -f "source[path]=/"
```
1–2 分钟后 `https://<owner>.github.io/<name>/` 生效（curl 200 验证）。

## 反模式
- ❌ 未查证就写票价/天气/店名；❌ 用户没确认就产出全量 HTML；❌ 门票按 4 人、预算按 3 人这类口径漂移；❌ 网页引入本地依赖（必须单文件自洽，仅 `img/` 相对路径）；❌ 忽略预约硬约束把热门窟排进不可能的日期；❌ 高原/长下坡/儿童座椅等安全提醒缺失。
