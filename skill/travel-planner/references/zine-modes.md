# 展示模式（版式语言）· 四式

> 理念源自 zine 系开源作品的共识：**先读素材的性格，再决定呈现**——不把行程当模板套，而是辨认这趟旅程的主体（人）、空间（地貌）、色彩（目的地色谱）与没说出口的情绪，再选择保留真实（照片锚点）或转译为插画。
> 致敬与参考：[Zeejay0/gathered-scenes-zine-skill（拾景纸刊）](https://github.com/Zeejay0/gathered-scenes-zine-skill)、photo-to-zine-postcard、photo-to-organic-knit 等 GitHub 技能。

选择规则：主题管"颜色与字体"，模式管"版式与质感"。先定模式骨架，再套主题 tokens。

---

## M1 · 纸刊杂志（editorial zine）
**适用**：历史文化深度 / 慢节奏 / 出片为主 —— 想让网页"像一本被认真编辑过的画册"。
**版式语言**：
- 每日页改为 **3:5 竖版海报卡**（`aspect-ratio:3/5`，或每屏一页横向翻阅），一天=一页，页码用衬线数字
- **大留白**：正文区左右留白 ≥18%，每页只放一个视觉锚点（一张配图或海拔剖面）
- 标题用大号衬线（楷体/宋体 900），正文小而疏（行高 2.0），克制用色（全页 ≤2 个强调色）
- 图片四周出血留 8px 纸边；说明文字用细线上引（`border-top` + 小字号）
**CSS 配方**：`.poster{aspect-ratio:3/5;padding:9% 12%;break-inside:avoid}`；页脚页码 `font-variant-numeric:oldstyle-nums`

## M2 · 手账拼贴（journal / washi tape）
**适用**：随性体验 / 亲子 / 网红打卡 —— 要"手作的温度"。
**版式语言**：
- **拍立得相框**：配图 `background:#fff;padding:10px 10px 42px;box-shadow:2px 4px 10px rgba(0,0,0,.15);transform:rotate(-1.5deg)`，底部手写体图注
- **纸胶带**：卡片顶部一条 24px 半透明色带斜贴 `background:<accent>55;transform:rotate(-2deg);width:110%`，两端锯齿（`mask-image` 或 clip-path）
- **邮戳/印章**：SVG 圆形章（`border:2px dashed`+内圈文字沿圆 `textPath`），盖在卡片角上表示"到此一游"
- **手写标注**：关键数字/箭头用楷体斜放；和纸纹理：`<filter><feTurbulence baseFrequency="0.8"/><feColorMatrix values="0 0 0 0 0.93 ..."/></filter>` 叠 5% 透明度
**CSS 配方**：噪点 `body::after{content:"";position:fixed;inset:0;pointer-events:none;opacity:.05;background-image:url("data:image/svg+xml,...feTurbulence...")}`

## M3 · 针织暖物（organic knit）
**适用**：山野徒步 / 露营 / 秋冬温泉线 —— 要"裹起来的暖"。
**版式语言**：
- **织纹底**：整页极淡十字织纹（SVG `<pattern>` 8px 交叉线，透明度 4–6%），卡片如**织物吊牌**（打孔+穿绳：伪元素圆孔+一条斜线）
- **缝线边框**：`border:2px dashed`（虚线间距 6 8）模拟走线，圆角 6px（织物没有锐角）
- **毛线色板**：低饱和暖色系（主题 tokens 选 forest-warm/seaside 的暖色带），强调色像"换线"般只出现在标题与按钮
- 标题可配一行编织纹分隔线（`repeating-linear-gradient` 交叉编织 12px 高）
**CSS 配方**：吊牌孔 `.tag::before{content:"";width:10px;height:10px;border-radius:50%;background:var(--paper);border:2px solid var(--ink3)}`

## M4 · 极简档案（minimal archive）
**适用**：紧凑多看 / 数据控 / 长途硬核自驾 —— demo 默认风格更冷峻的变体。
**版式语言**：单色+唯一强调色；等宽数字（`font-variant-numeric:tabular-nums`）做里程/预算；卡片带档案标签（左上角小号编号 `D-03`）；细分隔线（1px 30% 透明）；无圆角或 2px。
**CSS 配方**：`--radius:0`；标签 `.tag-no{font-family:var(--fnum);letter-spacing:.15em;font-size:10px;color:var(--ink3)}`

---

### 组合速查
| 旅行风格 | 推荐主题 × 模式 |
|---|---|
| 历史文化深度 | silk-mineral × M1 纸刊（demo 同款气质） |
| 网红打卡/出片 | urban-pop × M2 手账（或 seaside-breeze × M2） |
| 慢节奏自然 | alpine-fresh × M1 / M4 |
| 亲子海滨 | seaside-breeze × M2 |
| 江南人文 | ink-wash × M1 |
| 徒步露营 | forest-warm × M3 针织 |
| 硬核自驾 | silk-mineral × M4 档案 |

实现提示：模式只动 CSS 与卡片外壳（.poster/.polaroid/.tag 等包装类），数据结构与 JS 一概不动；先做一页样张给用户确认再铺全站。
