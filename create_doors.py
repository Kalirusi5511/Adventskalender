from pathlib import Path

BASE = Path("adventskalender")
DOORS = BASE / "doors"
DOORS.mkdir(parents=True, exist_ok=True)

# Rätsel 1–24
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

for day, (frage, antwort) in RIDDLES.items():
    html = f"""<h2>🎁 Türchen {day}</h2>
<p><strong>Rätsel:</strong></p>
<p>{frage}</p>
<details>
<summary>🧠 Lösung anzeigen</summary>
{antwort}
</details>
"""
    file_path = DOORS / f"door{day:02}.html"
    file_path.write_text(html, encoding="utf-8")

print("✅ Türchen 1–24 erstellt. Tür 25 bleibt für das besondere Geschenk.")
