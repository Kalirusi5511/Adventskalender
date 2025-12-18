from pathlib import Path
import base64

BASE = Path("adventskalender")

# -----------------------------
# Rätsel 1–24 (DE)
# -----------------------------
RIDDLES = {
    1: ("Ich habe Städte ohne Häuser, Flüsse ohne Wasser und Länder ohne Menschen. Was bin ich?", "Eine Landkarte"),
    2: ("Was wird größer, je mehr man davon wegnimmt?", "Ein Loch"),
    3: ("Was gehört dir, wird aber häufiger von anderen benutzt?", "Dein Name"),
    4: ("Ich spreche ohne Mund und höre ohne Ohren. Was bin ich?", "Ein Echo"),
    5: ("Was kann reisen um die Welt, bleibt aber immer am selben Ort?", "Eine Briefmarke"),
    6: ("Was hat einen Schlüssel, aber keine Tür?", "Eine Tastatur"),
    7: ("Was läuft, aber kommt nie ans Ziel?", "Die Zeit"),
    8: ("Was hat Beine, kann aber nicht laufen?", "Ein Tisch"),
    9: ("Was ist immer vor dir, aber nie zu sehen?", "Die Zukunft"),
    10: ("Was hat ein Auge, aber kann nicht sehen?", "Eine Nadel"),
    11: ("Was wird nass, während es trocknet?", "Ein Handtuch"),
    12: ("Was fällt, ohne sich zu verletzen?", "Der Schnee"),
    13: ("Was hat viele Zähne, aber kann nicht beißen?", "Ein Kamm"),
    14: ("Was geht hoch und runter, bleibt aber am selben Ort?", "Eine Treppe"),
    15: ("Was hat Hände, aber kann nichts greifen?", "Eine Uhr"),
    16: ("Was wird immer kürzer, je länger es dauert?", "Das Leben"),
    17: ("Was kann man brechen, ohne es anzufassen?", "Ein Versprechen"),
    18: ("Was hat ein Herz, aber keine Gefühle?", "Eine Artischocke"),
    19: ("Was ist leicht wie eine Feder, aber niemand kann es lange halten?", "Den Atem"),
    20: ("Was sieht man einmal im Jahr, zweimal im Monat, aber nie in der Woche?", "Den Buchstaben M"),
    21: ("Was ist voll, auch wenn es leer ist?", "Ein Kalender"),
    22: ("Was wird größer, je mehr Licht man darauf wirft?", "Ein Schatten"),
    23: ("Was kann man hören, aber nicht sehen?", "Geräusche"),
    24: ("Was endet immer mit einem Anfang?", "Ein Kreis"),
}

# -----------------------------
# Verschlüsselung (STABIL)
# -----------------------------
def encrypt(text: str, key: str) -> str:
    out = ""
    for i, ch in enumerate(text):
        out += chr(ord(ch) ^ ord(key[i % len(key)]))
    return base64.b64encode(out.encode("utf-8")).decode("utf-8")

# -----------------------------
# Dateien
# -----------------------------
FILES = {
    "index.html": """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>🎄 Adventskalender</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

<h1>🎄 Rätsel-Adventskalender</h1>
<p>24 Rätsel + ein besonderes Geschenk 🎁</p>

<div id="calendar" class="calendar"></div>
<div id="content" class="content"></div>

<script src="js/crypto.js"></script>
<script src="js/calendar.js"></script>
</body>
</html>
""",

    "css/style.css": """body {
  font-family: Arial, sans-serif;
  background: linear-gradient(#081821, #0b2a38);
  color: white;
  text-align: center;
}

.calendar {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
  max-width: 420px;
  margin: 30px auto;
}

button {
  padding: 15px;
  font-size: 18px;
  background: #b22222;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  color: white;
}

button:hover {
  background: #dc143c;
}

.content {
  margin: 30px auto;
  max-width: 500px;
  background: rgba(0,0,0,0.4);
  padding: 20px;
  border-radius: 12px;
}
""",

    "js/crypto.js": """function decrypt(data, key) {
  try {
    const decoded = atob(data);
    let out = "";
    for (let i = 0; i < decoded.length; i++) {
      out += String.fromCharCode(
        decoded.charCodeAt(i) ^ key.charCodeAt(i % key.length)
      );
    }
    return out;
  } catch {
    return null;
  }
}
""",

    "js/calendar.js": """const cal = document.getElementById("calendar");

// Buttons erzeugen
for (let i = 1; i <= 25; i++) {
  const btn = document.createElement("button");
  btn.textContent = i;
  btn.onclick = () => openDoor(i);
  cal.appendChild(btn);
}

// TEST-FREUNDLICH: kein Jahres-Key mehr
function canOpenDoor(n) {
  const today = new Date();
  return today.getMonth() === 11 && today.getDate() >= n;
}

async function openDoor(n) {
  if (!canOpenDoor(n)) {
    alert("🎄 Dieses Türchen ist noch geschlossen!");
    return;
  }

  const res = await fetch(`data/door${String(n).padStart(2,'0')}.enc`);
  const encrypted = await res.text();

  const key = `DOOR-${n}`;
  const content = decrypt(encrypted, key);

  if (!content || !content.includes("<h2>")) {
    alert("❌ Entschlüsselung fehlgeschlagen");
    return;
  }

  document.getElementById("content").innerHTML = content;
}
""",

    "README.md": """🎄 Rätsel-Adventskalender
🌍 GitHub Pages
📜 Lizenz: MIT

25 Türchen – fair play 🙂
""",

    "LICENSE": """MIT License

Copyright (c) 2025 Kalirusi5511
"""
}

# -----------------------------
# Build
# -----------------------------
def main():
    (BASE / "css").mkdir(parents=True, exist_ok=True)
    (BASE / "js").mkdir(parents=True, exist_ok=True)
    (BASE / "data").mkdir(parents=True, exist_ok=True)

    for path, content in FILES.items():
        p = BASE / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    # Tür 1–24
    for day, (question, answer) in RIDDLES.items():
        html = f"""
<h2>🎁 Türchen {day}</h2>
<p><strong>Rätsel:</strong></p>
<p>{question}</p>
<details>
<summary>🧠 Lösung anzeigen</summary>
{answer}
</details>
"""
        key = f"DOOR-{day}"
        enc = encrypt(html, key)
        (BASE / "data" / f"door{day:02}.enc").write_text(enc, encoding="utf-8")

    # Tür 25 – Geschenk
    gift_html = """
<h2>🎄 Türchen 25</h2>
<p>🎁 Glückwunsch!</p>
<p>Öffne jetzt die Datei <strong>GESCHENK.txt</strong>.</p>
<p>Frohe Weihnachten! 🎅</p>
"""
    enc = encrypt(gift_html, "DOOR-25")
    (BASE / "data" / "door25.enc").write_text(enc, encoding="utf-8")

    (BASE / "GESCHENK.txt").write_text(
        "🎁 Überraschung!\n\nHier kommt dein echtes Geschenk rein.\n",
        encoding="utf-8"
    )

    print("✅ Adventskalender FIXED & erstellt!")

if __name__ == "__main__":
    main()
