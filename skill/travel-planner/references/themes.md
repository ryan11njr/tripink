# UI 主题库（六套预设）

用法：选定主题后，替换 template.html 中 `:root` 的调色与字体变量、`body` 背景渐变（两团 radial-gradient 用主题浅色）、强度点配色（.dot/.tag 三档）、海拔剖面 `elevArea` 渐变主色、以及"高原反应区"色块（高原线路才保留，平原线路删除该 band 与图例）。
所有主题：标题字体优先**系统字体**（零下载、国内秒开）；数字/眉题统一 `Cormorant Garamond`（font.im CDN，回退 Georgia）。中文显示字体按主题换。

---

## 1. silk-mineral · 丝路矿物料（默认，demo 同款）
适用：历史文化深度 / 大西北 / 石窟关隘 / 紧凑多看
- `--paper:#f2e7cb; --paper2:#ead9b0; --card:#fbf3da; --card2:#f6ead0; --ink:#1b1815`
- 强调：石青 `--azur:#2b5d86`（主/水系）、石绿 `--mal:#4d8a55`（自然）、朱砂 `--cin:#b23a2e`（警示/峰值）、赭石 `--och:#c98a3e`、泥金 `--gold:#9a7730`
- 显示字体：楷体 `"STKaiti","KaiTi","楷体",serif`；签名元素：海拔剖面（矿物料手卷感）
- 背景渐变：赭石 + 石青两团极浅 radial

## 2. alpine-fresh · 高原清冽
适用：自然风光 / 雪山湖泊 / 慢节奏感受自然
- `--paper:#eef3f2; --paper2:#dde8e6; --card:#f7faf9; --card2:#edf3f1; --ink:#1a2a2e`
- 强调：冰川蓝 `#2f6f8f`、冷杉绿 `#3f7d5c`、晨雾灰 `#7d8f96`、日照金 `#c99a4b`、雪线红（警示）`#b5544b`
- 显示字体：`"Songti SC","SimSun","宋体",serif`（清瘦宋体）；签名元素：海拔剖面 + 山脊虚线装饰
- 背景渐变：冰川蓝 + 冷杉绿极浅 radial；整体留白比 mineral 多 10%

## 3. urban-pop · 都市霓虹
适用：网红打卡 / 都市美食 / 出片为主
- `--paper:#141419; --card:#1d1d24; --card2:#23232c; --ink:#f2f0ea`（**深底**）
- 强调：洋红 `#e8467c`、电光蓝 `#2fd4e0`、荧光黄绿 `#c8f04a`、暖橙 `#ff9f43`；警示用洋红
- 显示字体：`"PingFang SC","Microsoft YaHei",sans-serif` 加粗 900 + 大字号（标题 clamp 上调 1.3×）；签名元素：打卡点大字徽章 + 门票价签样式
- 卡片描边 1px 半透明强调色、hover 发光 `box-shadow:0 0 18px <accent>55`；地图默认高德矢量（夜间观感更稳）

## 4. seaside-breeze · 海滨假日
适用：海岛海滩 / 亲子友好
- `--paper:#f3f7f4; --paper2:#e3eef7; --card:#fbfdff; --card2:#eef6fb; --ink:#20323e`
- 强调：海盐青 `#2a9d8f`、珊瑚橙 `#f4772e`、沙金 `#e9c46a`、浪花蓝 `#4a9fd8`
- 显示字体：`"Yuanti SC","Microsoft YaHei",sans-serif`（圆体感，缺则黑体）；圆角整体上调（卡片 18px、标签 999px）；签名元素：每日页头波浪分隔线（SVG path）
- 强度色改为：轻松=海盐青 / 中等=沙金 / 硬日=珊瑚橙；亲子行程在 KPI 增加"儿童友好度"标签

## 5. ink-wash · 水墨留白
适用：江南 / 古镇园林 / 人文静线
- `--paper:#f7f5f0; --paper2:#eceae3; --card:#fcfbf7; --card2:#f3f1ea; --ink:#22211f`
- 强调：仅一个主色 墨青 `#33525c` + 印章红 `#a63d2f`（只用于峰值/警示/落款）；其余全灰阶（`#6b6a66/#98968f`）
- 显示字体：楷体或仿宋 `"STKaiti","KaiTi","FangSong",serif`；签名元素：章节号用竖排中文数字 + 印章式落款方块
- 卡片去阴影、边框改 0.5px 灰；剖面渐变淡至 0.25 不透明度

## 6. forest-warm · 山野暖木
适用：徒步 / 露营 / 森线自驾
- `--paper:#f1ede3; --paper2:#e4ddcc; --card:#faf7ef; --card2:#f0ebdd; --ink:#26221a`
- 强调：深林绿 `#3d5a3e`、苔藓 `#6a8a5f`、暖木褐 `#8a6b4a`、篝火橙 `#c96f33`、赤土 `#a6552e`（警示）
- 显示字体：`"Kaiti SC","KaiTi",serif`；签名元素：步道虚线路径线 + 徒步段爬升小剖面；KPI 增加"累计爬升/徒步 km"
- 背景加极淡织物噪点（`radial-gradient` 叠两层即可，勿用图片）
