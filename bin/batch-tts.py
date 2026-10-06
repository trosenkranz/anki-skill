#!/usr/bin/env python3
"""Batch-TTS für ukrainische Beispielsätze (Worklist als JSONL).

Läuft eine Worklist zeilenweise ab und erzeugt je Zeile eine MP3 über
bin/tts-cartesia.py (Cartesia Sonic, Sprache uk, Voice „Oleh").

Worklist-Format — eine JSON-Zeile je Karte:
    {"id": 1784060732221, "file": "derberuf_bsp.mp3", "uk": "Моя професія — учитель."}
- `uk`   = exakter ukrainischer Satz aus dem `Example`-Feld (Aspekt-Marker und
           `багато`-Klammerzusätze vorher strippen, siehe Anki-MCP-Verwendung.md §1.5/§1.6)
- `file` = Zieldateiname nach Namenskonvention (Anki-MCP-Verwendung.md §2);
           Pfade werden relativ zum aktuellen Arbeitsverzeichnis aufgelöst
           (Projekt-Root `~/Dokumente/anki` empfohlen).

Features:
- Resume: existierende Dateien > 1000 B werden übersprungen.
- Fehlerprotokoll: JSON-Liste [id, file, stderr/stdout-Auszug], wird nur bei
  Fehlern geschrieben (Default /tmp/tts_failures.json).
- Keine Shell-Quoting-Probleme: subprocess mit Argumentliste statt Shell-String
  (ukrainische Apostrophe `’` sind dadurch harmlos).

Aufruf (aus dem Projekt-Root):
    bin/.venv/bin/python bin/batch-tts.py WORKLIST.jsonl [--failures PFAD]
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser(description="Batch-TTS über eine JSONL-Worklist abarbeiten.")
    ap.add_argument("worklist", help="JSONL-Datei mit {id, file, uk} je Zeile")
    ap.add_argument("--failures", default="/tmp/tts_failures.json",
                    help="Pfad für das Fehlerprotokoll (nur bei Fehlern geschrieben)")
    args = ap.parse_args()

    rows = [json.loads(l) for l in open(args.worklist, encoding="utf-8") if l.strip()]
    print(f"total rows: {len(rows)}", flush=True)

    ok, fail = [], []
    for i, r in enumerate(rows, 1):
        out = r["file"]
        if os.path.exists(out) and os.path.getsize(out) > 1000:
            ok.append(out)
            print(f"[{i:02d}/{len(rows)}] SKIP (exists) {out}", flush=True)
            continue
        p = subprocess.run(
            [str(ROOT / "bin" / ".venv" / "bin" / "python"),
             str(ROOT / "bin" / "tts-cartesia.py"),
             "-i", r["uk"], "-o", out],
            capture_output=True, text=True, timeout=120,
        )
        if p.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > 1000:
            ok.append(out)
            print(f"[{i:02d}/{len(rows)}] OK   {out} ({os.path.getsize(out)} B)", flush=True)
        else:
            fail.append((r["id"], out, (p.stderr or p.stdout).strip()[:200]))
            print(f"[{i:02d}/{len(rows)}] FAIL {out}: {(p.stderr or p.stdout).strip()[:150]}", flush=True)

    print(f"\nDONE ok={len(ok)} fail={len(fail)}")
    if fail:
        json.dump(fail, open(args.failures, "w", encoding="utf-8"), ensure_ascii=False)
        print(f"failures -> {args.failures}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
