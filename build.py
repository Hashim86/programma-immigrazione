import json, sys, pathlib
here = pathlib.Path(__file__).parent
data = json.loads((here / "data.json").read_text(encoding="utf-8"))
ids = {p["id"] for p in data["permessi"]}
err = []
for p in data["permessi"]:
    for k in ["nome", "categoria", "sintesi", "norme", "requisiti", "durata", "lavoro", "rinnovo", "alias"]:
        if k not in p: err.append(f"{p['id']}: manca {k}")
    for c in p.get("conversioni", []):
        if c["a"] not in ids: err.append(f"{p['id']}: conversione verso id sconosciuto {c['a']}")
        if c["esito"] not in ("si", "no", "cond"): err.append(f"{p['id']}->{c['a']}: esito {c['esito']}")
if err:
    print("\n".join(err)); sys.exit(1)
tpl = (here / "template.html").read_text(encoding="utf-8")
out = tpl.replace("/*__DATA__*/", "const DATA_INTEGRATA = " + json.dumps(data, ensure_ascii=False) + ";")
dest = here / "dist" / "Programma Immigrazione.html"
dest.parent.mkdir(exist_ok=True)
dest.write_text(out, encoding="utf-8")
print("ok", dest, len(out) // 1024, "KB,", len(data["permessi"]), "permessi,", sum(len(p.get("conversioni", [])) for p in data["permessi"]), "conversioni,", len(data["faq"]), "faq")
