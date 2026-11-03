"""Assemble the single-file review page: template.html + data.json + the T&I logo  ->  index.html

  python dashboard/build.py            (writes dashboard/index.html)
"""
import base64, io, os
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
data = open(os.path.join(HERE, "data.json"), encoding="utf-8").read().replace("</", "<\\/")
im = Image.open(os.path.join(ROOT, "brand", "TI_Logo.png")).convert("RGB"); w = 560; im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
buf = io.BytesIO(); im.save(buf, "PNG", optimize=True); logo = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
out = os.path.join(HERE, "index.html")
open(out, "w", encoding="utf-8").write(tpl.replace("/*DATA*/", data).replace("/*LOGO*/", logo))
print("wrote", out, os.path.getsize(out) // 1024, "KB")
