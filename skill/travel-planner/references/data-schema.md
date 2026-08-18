# 数据结构规范（template.html 顶层 JS 常量）

生成新行程 = 重写以下常量 + 主题 tokens。其余函数勿动。

## ELEV · 海拔剖面节点
`['地名', 累计公里数, 海拔m, '归属日标签']`
- 数组按行程顺序；公里数**单调递增**，末项=总里程；起终点同名不同标签（'起' / 'D8'）
- 平原/无高反线路：删除 3000m band 相关渲染（altBand 变量）与图例"高原反应区"
- 高原线路：海拔 ≥3600m 的点自动标朱砂数字（模板逻辑）

## DAYS · 每日数据（核心）
```
{n:1, date:'2026-08-08', wk:'周六', from:'A', to:'B',
 dist:'900 km', drive:'约 10.5 h', intensity:'hard|mid|easy', tag:'四字主题',
 lat:34.58, lon:105.72,            // 当晚住宿点坐标（天气取数点）
 altM:1100, altLabel:'1,100 m',
 route:'高速名 · 途经',
 timeline:[['06:30','事件'],...],
 attractions:[{cat:'his|geo|cul', name:'景点 · 副题', hook:'一句话钩子',
   facts:[['标签','值'],...],
   secs:[['沿革|地质|看点|贴士','正文（可含<b>）'],...],
   anec:'典故一段（可空）'}],
 food:[{dish:'菜名', shop:'店名（地址）', note:'一句话+人均', src:'来源'}],
 hotel:{area:'住宿分区建议', recs:[{n:'店名', p:'~280/间', note:'一句'}], budget:'500–600'},
 cost:{fuel:0,toll:0,hotel:0,food:0,tickets:0,other:0},   // 当日全队合计
 climate:{tmax:'32',tmin:'22',humid:'60',uv:'8',sunrise:'06:12',sunset:'19:53',note:'一句'}}
```
- `intensity` 三档映射 INMAP（hard/mid/easy → 硬日/中等/轻松 + 圆点色）
- 景点讲解是"导游底本"：每景点 facts 3–4 条 + secs 3–5 节 + 典故，史实必须有 GSRC 来源
- `cost` 各键为**全队当日合计**；仪表盘总计 = Σ(每日 CATS 各键)；首页大数字须与它一致（手写，改数据后同步）
- 隐私口径：不想展示的花费类目从 CATS 与 costTable 行中同时移除，并在文案注明"不含 XX"

## TIPS · 每日小贴士 `{1:['...','...'],...}`
来自小红书/马蜂窝经验帖的实操点（几点进园、错峰、装备、安全），3–5 条/天，可含 `<b>`。

## GSRC · 景点来源 `{ '景点名(须与 attractions.name 完全一致)':'文献/机构;文献' }`
显示在讲解卡底部。机构/志书/经典文献优先，宁缺毋滥。

## GIMG · 配图映射 `{ '景点名':'文件名(无扩展名)' }`
- 图片放 `img/<名>.jpg`（1:1、≤1100px、≤400KB，可用 optimize_images.py 压缩）
- 无配图就 `GIMG={}`；模板 `onerror` 自动隐藏，不破版

## CATS · 预算类目 `[['fuel','油费','#色'],...]`
顺序即图例顺序；色值取主题强调色。增删类目会同时影响：仪表盘堆叠图、类目表、md 生成器（若用仓库脚本需同步改）。

## 其他勿动
hash 路由（`#/day/N`、`#/budget`）、Open-Meteo 取数（按 date+lat/lon）、OSRM fetchRoute（按 LL 坐标折线取真实道路）、LL 坐标表（新行程需重写：`'地名':[lat,lon]`）。
