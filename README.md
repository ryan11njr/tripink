<p align="center">
  <img src="assets/brand/readme-header.png" alt="TripInk" width="100%">
</p>

# TripInk · Your trip, in ink.

> **跨智能体开源旅行规划技能**（Claude Code · Codex · 任何支持 SKILL.md 约定的智能体）：读懂你 → 查证世界 → 把你的行程**印成一本可交互的旅行杂志**。
> 不是又一份 AI 文字攻略——是海拔剖面、真实导航路线、实时天气、导游级讲解、预算仪表盘，全部装进一个双击就开的网页。

[![License: MIT](https://img.shields.io/badge/License-MIT-1b1815.svg)](LICENSE)
[![Homepage](https://img.shields.io/badge/HomePage-tripink-2b5d86.svg)](https://ryan11njr.github.io/tripink/)

## 为什么叫 TripInk

古人出嘉峪关，要领一份"关照"——它既是通行凭证，也意味着一路有人照应。后来我们有了护照、导航和无数攻略，却仍常在出发前面对一堆互相矛盾的数字。TripInk 想重新做一份属于今天的"关照"：先读懂谁要出发、为何出发，再查证门票、天气与路线，把结果印成一本可以点开的旅行杂志。让地图之外的顾虑也被看见，让抵达之前的每次选择都有依据。它不替你旅行，只让每一步更明白，也更像你。

## Why TripInk

Travelers once leaving Jiayuguan carried a *guanzhao*—a passage document, but also a promise of being looked after on the road. We now have passports, maps, and endless travel posts, yet planning can still leave us with scattered notes and numbers that no longer agree. TripInk is a modern take on that old idea of care. It first learns who is traveling, why the journey matters, and what pace feels right. Then it verifies tickets, weather, routes, and practical experience before shaping everything into an interactive travel magazine. The result can travel as a single HTML file, or be kept as PDF, Word, or Markdown. TripInk does not book the trip or replace your judgment. It gives the journey a form you can understand, check, carry, and remember—researched from the world, but designed around you.

## 它不一样在哪

- **最懂你** — 先读懂这趟旅行：谁同行、什么纪念日、什么节奏；连你没说出口的需求（隐性需求探测 + 每轮主动推荐：隐藏玩法 / 省钱点 / 风险预警 / 仪式感）都替你想好。
- **最靠谱** — 每个数字有来源、有日期：门票与预约规则、天气、油价、经验帖，多源交叉查证；生成的网页在旅途中持续拉取**当天的真实天气与导航路线**；查不到就明确标"未核实"。
- **随身行** — 输出 **HTML（按旅行风格定制审美）/ PDF / Word / MD**；HTML 单文件双击即开，一路出行随时查。

## 项目主页与 Demo

- **项目主页**（推荐从这里进）：<https://ryan11njr.github.io/tripink/>
- **Demo · 大西北自驾 8 天**（聊城东昌府区 ⇄ 敦煌 · 3 人 · "敦煌矿物料"画册风格）：<https://ryan11njr.github.io/tripink/demo/northwest/>
- Demo 配套 PDF 手册：<https://ryan11njr.github.io/tripink/demo/northwest/行程手册.pdf>

Demo 含麦积山 / 青海湖 / 茶卡 / 莫高窟 / 鸣沙山 / 嘉峪关 / 丹霞 / 西夏王陵的导游级讲解（附参考文献）、OSRM 真实导航路线、按到达日期的 Open-Meteo 实时天气与预算仪表盘。

## 安装（选你的智能体）

**Claude Code** — 复制到个人技能目录：

```bash
git clone https://github.com/ryan11njr/tripink.git
# Windows
xcopy /E /I tripink\skill\travel-planner "%USERPROFILE%\.claude\skills\travel-planner"
# macOS / Linux
cp -r tripink/skill/travel-planner ~/.claude/skills/
```

**Codex** — 放入技能目录（SKILL.md 约定）：

```bash
cp -r tripink/skill/travel-planner ~/.codex/skills/
```

**其他智能体** — 任何支持 SKILL.md 约定的智能体：把 `skill/travel-planner` 放入其技能目录，或在 AGENTS.md / 系统提示中引用该 SKILL.md 的路径。

装好后说"**帮我规划一次旅行 / 自驾游**"即触发：问卷 → 联网研究 → 迭代确认 → 生成网页 → 可选一键发布 GitHub Pages。

## Skill 结构

| 文件 | 说明 |
|---|---|
| `skill/travel-planner/SKILL.md` | 全流程：隐性需求探测 · 五源交叉验证 · 主动推荐引擎 · 构建 QA · 发布 |
| `references/themes.md` | 六套配色主题（丝路矿物料 / 高原清冽 / 都市霓虹 / 海滨假日 / 水墨留白 / 山野暖木） |
| `references/zine-modes.md` | 四种展示模式（纸刊杂志 / 手账拼贴 / 针织暖物 / 极简档案），理念致敬 [gathered-scenes-zine](https://github.com/Zeejay0/gathered-scenes-zine-skill) 等 zine 系作品 |
| `references/data-schema.md` · `template.html` · `optimize_images.py` | 数据规范 / 完整模板 / 配图压缩工具 |

## License

[MIT](LICENSE) · 仅供个人行程规划参考，不提供订票等服务。

---
数据来源：Open-Meteo · OSRM · 高德瓦片 · 敦煌研究院 · 《中国国家地理》· 汽油价格网 · 小红书 / 马蜂窝 · 汽车之家。
