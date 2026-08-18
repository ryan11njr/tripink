# 优化 img/ 下的配图：缩放 + 转 JPG，输出同目录 .jpg 并删除原 .png
from PIL import Image
import os, glob
D = 'D:/DESK-D/202608甘肃宁夏青海/img/'
before = 0; after = 0
for f in sorted(glob.glob(D + '*.png')):
    if f.endswith('.png') and not os.path.basename(f).startswith('.'):
        im = Image.open(f).convert('RGB')
        w, h = im.size
        name = os.path.basename(f)
        maxd = 1800 if name == 'hero.png' else 1100
        if max(w, h) > maxd:
            im = im.resize((int(w*maxd/max(w, h)), int(h*maxd/max(w, h))), Image.LANCZOS)
        out = os.path.splitext(f)[0] + '.jpg'
        im.save(out, 'JPEG', quality=88, optimize=True, progressive=True)
        b = os.path.getsize(f); a = os.path.getsize(out)
        before += b; after += a
        os.remove(f)
        print(f"{name}  {w}x{h}  ->  {round(a/1024)} KB  (was {round(b/1024)} KB)")
print(f"\n合计：{round(before/1024/1024,1)} MB  ->  {round(after/1024/1024,1)} MB")
