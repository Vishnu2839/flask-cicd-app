from flask import Flask, render_template_string

app = Flask(__name__)

VERSION = "Version 2"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hello from CI/CD Pipeline</title>
<style>
:root{--bg:#f5f7fb;--card:#fff;--text:#1b2433;--muted:#5d6b82;--accent:#2f6fed;--ok:#1a9d5c}
@media (prefers-color-scheme:dark){
  :root{--bg:#0e1420;--card:#171f2f;--text:#e8edf6;--muted:#93a1ba;--accent:#6b9bff;--ok:#3ddc97}
}
html,body{height:100%;margin:0}
body{background:var(--bg);color:var(--text);font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
     display:flex;align-items:center;justify-content:center;padding:16px;box-sizing:border-box}
.card{background:var(--card);border-radius:16px;padding:40px 32px;max-width:520px;width:100%;
      box-shadow:0 8px 30px rgba(0,0,0,.12);text-align:center}
.badge{display:inline-flex;align-items:center;gap:8px;font-size:13px;color:var(--ok);font-weight:600}
.dot{width:9px;height:9px;border-radius:50%;background:var(--ok)}
h1{font-size:clamp(1.5rem,5vw,2.1rem);margin:18px 0 8px}
.ver{display:inline-block;background:var(--accent);color:#fff;border-radius:999px;padding:4px 14px;font-size:14px;font-weight:600}
p{color:var(--muted);margin:18px 0 0;font-size:15px}
.steps{display:flex;justify-content:center;gap:8px;flex-wrap:wrap;margin-top:24px;font-size:13px}
.steps span{border:1px solid var(--muted);color:var(--muted);border-radius:8px;padding:4px 10px}
</style>
</head>
<body>
<main class="card">
  <div class="badge"><span class="dot"></span>Pipeline passing</div>
  <h1>Hello from CI/CD Pipeline!</h1>
  <span class="ver">{{ version }}</span>
  <p>This page is deployed automatically on every push.</p>
  <div class="steps"><span>Commit</span><span>Build</span><span>Test</span><span>Deploy</span></div>
</main>
</body>
</html>"""


@app.route("/")
def home():
    return render_template_string(PAGE, version=VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
