#!/usr/bin/env python3
"""Download, validate, and locally host real SaaS screenshots before publishing."""
import io, json, pathlib, shutil, urllib.request, urllib.parse, hashlib, sys
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parent.parent
source=json.loads((ROOT/"catalog-source.json").read_text(encoding="utf-8"))
dist=ROOT/"dist"
assets=dist/"assets"
assets.mkdir(parents=True,exist_ok=True)
for name in ["index.html","ionta.html","ionta-competitors.json","ionta-deep-dive.html","ionta-competitive-deep-dive.json","IONTA_COMPETITIVE_RESEARCH_RU.md","style.css","app.js","AGENTS.md","llms.txt","robots.txt",".nojekyll"]:
 if (ROOT/name).exists():shutil.copyfile(ROOT/name,dist/name)
verified,errors,hashes=[],[],set()
for p in source["patterns"]:
 try:
  candidate=p["image_url"]
  u=urllib.parse.urlsplit(candidate)
  if "/_next/image" in u.path:
   url=urllib.parse.parse_qs(u.query).get("url",[""])[0]
   if url.startswith("https://"):candidate=url
  for attempt in range(2):
   try:
    req=urllib.request.Request(candidate,headers={"User-Agent":"Mozilla/5.0 (compatible; SaaS-Atlas-Research/1.0)","Accept":"image/avif,image/webp,image/png,image/jpeg,image/*"})
    with urllib.request.urlopen(req,timeout=25) as resp:raw=resp.read(12*1024*1024+1)
    if len(raw)>12*1024*1024:raise ValueError("over 12MB")
    im=Image.open(io.BytesIO(raw));im.load()
    if im.width<350 or im.height<180:raise ValueError("too small")
    break
   except Exception:
    if attempt==0 and candidate!=p["image_url"]:candidate=p["image_url"];continue
    raise
  digest=hashlib.sha256(raw).hexdigest()
  if digest in hashes:raise ValueError("duplicate screenshot bytes")
  hashes.add(digest)
  im.thumbnail((2600,1800))
  target=assets/(p["id"]+".jpg")
  im.convert("RGB").save(target,format="JPEG",quality=86,optimize=True)
  with Image.open(target) as check:check.verify()
  verified.append(p)
  print("VERIFIED",p["id"],len(raw))
 except Exception as exc:
  errors.append({"id":p["id"],"reason":str(exc)[:250]})
  print("EXCLUDED",p["id"],str(exc)[:180])
ids={p["id"] for p in verified}
products=[]
for product in source["products"]:
 item=dict(product)
 item["pattern_ids"]=[p for p in item["pattern_ids"] if p in ids]
 if item["pattern_ids"]:products.append(item)
published=dict(source,patterns=verified,products=products,images_verified=True)
(dist/"catalog.json").write_text(json.dumps(published,ensure_ascii=False,indent=2),encoding="utf-8")
(dist/"catalog.js").write_text("window.SAAS_ATLAS="+json.dumps(published,ensure_ascii=False,separators=(",",":"))+";",encoding="utf-8")
(dist/"validation-report.json").write_text(json.dumps({"verified":len(verified),"products":len(products),"excluded":errors},ensure_ascii=False,indent=2),encoding="utf-8")
if len(verified)<8 or len(products)<4:
 print("PUBLICATION BLOCKED: too few verified screenshots",file=sys.stderr)
 sys.exit(2)
print("BUILD VALIDATED",len(verified),"screens",len(products),"products")
