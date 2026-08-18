# Travel Planner Skill · 旅行规划 → 高审美互动网页

一个可复用的 **Claude skill**：问卷收集需求 → 联网研究实时信息（天气 / 门票 / 小红书经验帖 / 油价过路费）→ 与用户迭代行程 → 按旅行风格选 UI 主题 → 生成单文件互动网页（可选 md/PDF、可一键发布 GitHub Pages）。
本仓库同时是它的 **Demo 展示**：一次真实的 8 天 7 晚大西北自驾（聊城东昌府区 ⇄ 敦煌，3 人）。

## Demo 在线体验
- 互动网页：<https://ryan11njr.github.io/xibei-roadtrip/>
- 高审美 PDF 手册：<https://ryan11njr.github.io/xibei-roadtrip/行程手册.pdf>

网页包含：全程**海拔剖面**（签名设计，朱砂标峰值与 3000m+ 高反区）· 高德卫星底图 + **OSRM 真实导航路线** · 每日分页（时间轴 / 导游级景点讲解·含参考文献 / **按到达日期实时天气**（Open-Meteo）/ 美食住宿 / 当日花销）· **预算仪表盘**（每日堆叠柱 + 类目占比）。

## 安装 Skill

```bash
git clone https://github.com/ryan11njr/xibei-roadtrip.git
# Claude Code 个人技能目录（Windows 示例）
xcopy /E /I xibei-roadtrip\skill\travel-planner "%USERPROFILE%\.claude\skills\travel-planner"
# macOS / Linux
cp -r xibei-roadtrip/skill/travel-planner ~/.claude/skills/
```
装好后对 Claude 说"**帮我规划一次旅行 / 自驾游**"即可触发；它会先问卷（出发地 / 目的地 / 人数 / 天数 / 方式 / 预算习惯 / 旅行风格…），再研究、迭代、选主题、生成网页。

## Skill 结构
| 文件 | 说明 |
|---|---|
| `SKILL.md` | 全流程：问卷 → 研究（含 Open-Meteo / OSRM 免 key 端点、查证纪律）→ 迭代 → 六套 UI 主题 → 构建 QA 清单 → 发布命令 |
| `references/themes.md` | 六套预设主题 tokens：丝路矿物料 / 高原清冽 / 都市霓虹 / 海滨假日 / 水墨留白 / 山野暖木 |
| `references/data-schema.md` | `ELEV / DAYS / TIPS / GSRC / GIMG / CATS` 数据规范 |
| `references/template.html` | 完整可运行的网页模板（即本 Demo，换数据+主题即新行程） |

## 本地使用 Demo
双击 `index.html`（需联网：地图瓦片 / 天气 / 导航 API；断网时天气回落常年气候值、路线回落直线示意）。

## 更新本仓库
根目录（Git Bash）：`bash deploy.sh` —— 重新生成 md/PDF、同步 index/img/skill 并推送，Pages 约 1–2 分钟生效。

---
数据来源：Open-Meteo · OSRM · 高德瓦片 · 敦煌研究院 · 《中国国家地理》· 汽油价格网 · 小红书 / 马蜂窝 · 汽车之家。仅供个人行程规划参考。
