# TripInk · Your trip, in ink.

> 一个 Claude 技能：读懂你 → 查证世界 → 把你的行程**印成一本可交互的旅行杂志**。
> 不是又一份 AI 文字攻略——是海拔剖面、真实导航路线、实时天气、导游级讲解、预算仪表盘，全部装进一个双击就开的网页。

**最懂你** — 先读懂这趟旅行（谁同行、什么纪念日、什么节奏），连你没说出口的需求都替你想好，每轮主动推荐隐藏玩法与风险预警。
**最靠谱** — 每个数字有来源、有日期：门票与预约规则、天气、油价、小红书经验帖，实时查证、多源交叉；生成的网页在你旅途中持续拉取**当天的真实天气与导航路线**。
**随身行** — 输出 **HTML（按旅行风格定制审美）/ PDF / Word / MD**；HTML 双击即开，一路出行随时查。

## 在线 Demo（真实行程生成）
- 互动网页：<https://ryan11njr.github.io/tripink/>
- 高审美 PDF 手册：<https://ryan11njr.github.io/tripink/行程手册.pdf>

一次 8 天 7 晚大西北自驾（聊城东昌府区 ⇄ 敦煌，3 人）：矿物料"敦煌画册"风格，含麦积山/青海湖/茶卡/莫高窟/鸣沙山/嘉峪关/丹霞/西夏王陵的导游级讲解（附参考文献）、OSRM 真实导航路线、按到达日期的 Open-Meteo 实时天气与预算仪表盘。

## 安装 Skill

```bash
git clone https://github.com/ryan11njr/tripink.git
# Claude Code 个人技能目录（Windows 示例）
xcopy /E /I tripink\skill\travel-planner "%USERPROFILE%\.claude\skills\travel-planner"
# macOS / Linux
cp -r tripink/skill/travel-planner ~/.claude/skills/
```
装好后对 Claude 说"**帮我规划一次旅行 / 自驾游**"即触发：问卷（出发地/人数/风格/预算…）→ 联网研究 → 迭代确认 → 六套主题 × 四种展示模式（纸刊杂志 / 手账拼贴 / 针织暖物 / 极简档案）→ 生成网页 → 可选一键发布 GitHub Pages。

## Skill 结构
| 文件 | 说明 |
|---|---|
| `skill/travel-planner/SKILL.md` | 全流程：隐性需求探测 · 五源交叉验证 · 主动推荐引擎 · 构建 QA · 发布命令 |
| `references/themes.md` | 六套配色主题（丝路矿物料/高原清冽/都市霓虹/海滨假日/水墨留白/山野暖木） |
| `references/zine-modes.md` | 四种展示模式（纸刊/手账/针织/档案），理念致敬 [gathered-scenes-zine](https://github.com/Zeejay0/gathered-scenes-zine-skill) 等 zine 系作品 |
| `references/data-schema.md` · `template.html` · `optimize_images.py` | 数据规范 / 完整模板 / 配图压缩工具 |

## 品牌与传播
- [交接文档（写给 GPT 协作者）](docs/HANDOVER.md) —— 项目全貌 + 任务清单 + 防幻觉事实表
- [品牌定稿与 Logo Prompt](docs/命名与Logo.md)（6 个扁平字标方向，含 OG 图）
- [爆款传播方案](docs/PROMOTION.md)（抖音/小红书/GitHub 三平台打法 + 冷启动 72h 清单）

## 本地使用 Demo
双击 `index.html`（需联网加载瓦片/天气/导航 API；断网自动降级）。更新仓库：根目录 `bash deploy.sh`。

---
数据来源：Open-Meteo · OSRM · 高德瓦片 · 敦煌研究院 · 《中国国家地理》· 汽油价格网 · 小红书/马蜂窝 · 汽车之家。MIT License · 仅供个人行程规划参考。
