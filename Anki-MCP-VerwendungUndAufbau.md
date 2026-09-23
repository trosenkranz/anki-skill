# Anki-MCP: Verwendung und Aufbau

> **Dokumentstand:** 20.09.2026
>
> **Geltungsbereich:** Diese Datei dokumentiert nur, was in bisherigen Sessions tatsächlich beobachtet und verwendet wurde — sie erhebt keinen Anspruch auf Vollständigkeit der gesamten Sammlung.
>
> **Grundlegende Konventionen:**
> 1. **Decknamen:** Wird ein Deck nur mit Namen genannt (z. B. `10 - Kindheit`), ist — sofern nicht anders angegeben oder der vollständige Pfad genannt wird — immer das Subdeck von `#7 - Sprachcafé` gemeint (also z. B. `#7 - Sprachcafé::10 - Kindheit`).
> 2. **Sprachpaar:** Karten der Sprachcafé-Decks verwenden — sofern nicht explizit anders gefordert — immer **Deutsch + Ukrainisch** (Begriffe und Beispielsätze).
> 3. **Prompt-Sprache:** Anfragen können auf Deutsch oder Englisch gestellt werden.
> 4. **Sync:** Den AnkiWeb-Sync löst **der Nutzer manuell** aus — nicht selbstständig per `sync`-Tool synchronisieren.
> 5. **Duplikate:** Ob ein (sammlungsweites) Duplikat beim Anlegen erzwungen wird (`allow_duplicate: true`) oder übersprungen wird, entscheidet **der Nutzer im Einzelfall** (engl. *on a case-by-case basis*) — nicht selbstständig erzwingen.
>
> **Hinweise:**
> 1. Speicherort: Projekt-Root `~/Dokumente/anki/`.
> 2. Python-Skripte, die nur inline im Session-Verlauf existierten, werden hier im Quelltext konserviert, damit sie nicht verloren gehen.

---

## 1. Aufbau der Anki-Datenbank (bisher genutzter Teil)

### 1.1 Deck-Struktur

- Deck-Hierarchie mit `::` als Trenner; numerische Präfixe (`#7`, `01`) dienen der Sortierung. Subdecks von `#7 - Sprachcafé`:
  - `01 - Beruf`, `02 - Ausbildung & Studium`, `03 - Sport`, `04 - Musik & Kunst`, `07 - Tiere und Haustiere`, `08 - Familie und Generationen`, `09 - Wohnen`, `10 - Kindheit`, `11 - Landschaften`, `12 - Literatur`
- Auf den Sprachcafé-Standard normiert (UKR/DE-Beispielsätze, ukrainisches Genus, Notiztyp 1.2): `01 - Beruf`, `07 - Tiere und Haustiere` (seit 16.09.2026, siehe 1.2), `10 - Kindheit`, `11 - Landschaften`, `12 - Literatur` (seit 17.09.2026, siehe 1.2). In `03 - Sport` und `04 - Musik & Kunst` enthalten die `Example`-Felder bisher nur den deutschen Satz; Genus-Marker dort teils kyrillisch (`ж.`) — noch nicht normiert. In `02 - Ausbildung & Studium` fehlen Beispielsätze noch fast ganz (1 Ausnahme mit UKR-Satz + Audio). `08 - Familie und Generationen` und `09 - Wohnen` stehen noch auf Altbestand-Zwillingsnotizen (`Tandem Cafe Basic++` bzw. `Basic+++`, siehe 1.2): je Begriff 2 Notizen (je Richtung eine, je 1 Karte), `Beispielsatz` einsprachig pro Zwillingsnotiz.
- `11 - Landschaften`: `Front` enthält den Begriff ohne Plural-Endung; der ursprüngliche Altbestand (Notiztyp `Tandem Cafe Basic++++`, siehe 1.2) wurde auf Nutzerentscheidung gelöscht.

### 1.2 Notiztyp

Die untersuchten Notizen verwenden denselben Notiztyp:

**`Basic (with reversed card and example sentences)`**

| Feld | Inhalt | Konventionen |
|---|---|---|
| `Front` | Deutscher Begriff / Redewendung | Rein textuell, z. B. `der Chef / die Chefin` |
| `Back` | Ukrainische Übersetzung + Genus des **ukrainischen** Wortes in Klammern | Marker: `(m)`, `(f)`, `(n)`, `(pl)`; Doppelformen `найкращий друг / найкраща подруга (m/f)`; Synonyme mit unterschiedlichem Genus erhalten je Wort einen eigenen Marker (`жарт (m), витівка (f)`); bei Mehrwort-Übersetzungen zählt der Kopf-Begriff (`гра в хованки (f)`, `шведська стінка (f)`); Verben ohne Marker. Alle Sprachcafé-Decks folgen dieser Konvention (Deck `01 - Beruf` wurde deckweit umgestellt) |
| `Example` | Ukrainischer Beispielsatz + deutsche Übersetzung | Standard: `УКР.<br><br>DE.` — mit Audio wird ein `[sound:...]-Tag` **vorangestellt** (siehe 1.3) |

- Pro Notiz werden **2 Karten** erzeugt (Normal + Umgekehrt); `notes_info` liefert dazu das Array `cards` mit zwei Card-IDs.
- Beim Parsen des ukrainischen Satzes aus dem `Example`-Feld: Text **vor dem ersten** `<br>` nehmen und HTML-Tags strippen (robust auch bei Formatabweichungen in noch nicht normierten Decks).
- **Beispielsatz-Regel (ab 16.09.2026):** Der deutsche Satz im `Example` verwendet den Front-Begriff bzw. eine gebeugte Form davon; der ukrainische Satz entsprechend die Übersetzung aus dem Back bzw. eine gebeugte Form davon. Bei Qualitätsprüfungen (Phase 3) sind Satzvorschläge an dieser Regel zu messen.
- **Synonym-Varianten im `Example` (Konvention ab 16.09.2026):** Listet das `Back` zwei Synonyme, enthält das `Example` einen vollständigen UKR-Satz zur ersten Variante, dann ` <i>oder</i> `, dann einen vollständigen zweiten UKR-Satz mit der zweiten Variante; der gemeinsame DE-Satz folgt einmal danach (Muster: `Verantwortung übernehmen` in `10 - Kindheit`).
- Bewusste Strukturvarianten in `10 - Kindheit` (Nutzer-Entscheidung): zwei UKR/DE-Satzpaare in einem Feld (`die Unbeschwertheit/die Sorglosigkeit`; auch `aussterben` in `11 - Landschaften`), zwei UKR-Varianten, getrennt durch den Varianten-Trenner (siehe nächsten Punkt), kursive kulturelle Anmerkung nach dem DE-Satz (`die Schultüte`). Die Parse-Regel darüber bleibt unberührt (UKR-Text liegt vor dem ersten `<br>`). Audio: je Satzpaar ein eigenes `[sound:]`-Tag am Anfang des Paars (Reihenfolge im Feld: Tag → UKR → DE → Tag → UKR → DE).
- **Varianten-Trenner:** Konvention ab 15.09.2026: ` <i>oder</i> ` (deutsch, kursiv). Bestehende Karten trennen noch mit ` <i>або</i> ` (`Verantwortung übernehmen` in `10 - Kindheit`; `der Gletscher` in `11 - Landschaften`) — diese werden auf ` <i>oder</i> ` umgestellt, **sobald die jeweilige Karte aus anderem Anlass bearbeitet wird**; keine eigenständige Migration. Bis dahin Parsing/Audio-Split nur am getagten Trenner ausführen, nie am Klartext („або“/„oder“ können Teil von Wörtern sein, z. B. з**або**лочених).

**Altbestand-Familie `Tandem Cafe Basic` / `Basic+` / `Basic++` / `Basic+++` (nicht normiert):** Felder `Front`, `Back`, `Niveau`, `Grammatik`, `Beispielsatz` — Genus-Marker kyrillisch (z. B. `виховання (с.)`), `Beispielsatz` einsprachig; je Begriff 2 Zwillingsnotizen (UKR-Front + DE-Front), je 1 Karte. `Basic+` (früher komplett in `07 - Tiere und Haustiere`) wurde am 16.09.2026 transformiert: 65 normierte Notizen erstellt, 130 Alt-Notizen gelöscht; der Notiztyp bleibt ohne Notizen in der Collection (kein MCP-Delete-Tool für Notiztypen — manuelle Löschung über Anki-GUI möglich; Vorläufer: `Basic++++`); Legacy-`Grammatik`-Qualifier in `session-notizen/2026-09-16_07-tiere_legacy-grammatik.json` gesichert. Verbleibende Vorkommen: `Basic++` in `08 - Familie und Generationen`, `Basic+++` in `09 - Wohnen`. Der schlichte `Tandem Cafe Basic` (zuletzt nur in `12 - Literatur`; Zwillingsnotizen mit sprachspezifischer `Grammatik` — DE-Notiz deutsches Genus mit Zusätzen wie „kein Plural", „Eigenname", „Feste Wendung", UKR-Notiz der ukrainische рід; Back-Marker kyrillisch `(м.)/(ж.)/(ч.)/(с.)`; keine Tags, Niveau nur im Feld) wurde am 17.09.2026 transformiert: 29 normierte Notizen erstellt, 58 Alt-Notizen gelöscht; der Notiztyp bleibt ohne Notizen in der Collection (kein MCP-Delete-Tool für Notiztypen). Die sprachspezifischen Legacy-`Grammatik`-Qualifier sind in `session-notizen/2026-09-17_12-literatur_legacy-grammatik.json` gesichert. Duplikat-Entscheidung des Nutzers dabei: die leere normierte Alt-Notiz `die Bibliothek` in `07 - Tiere und Haustiere` wurde gelöscht; `12 - Literatur` führt den Begriff mit Beispielsatz.

**Transform-Rezept (erprobt bei 07):** Pro Begriffspaar 1 normierte Notiz: `Front` = DE-Zwillings-Front ohne Plural-Suffix (`, -e`-Muster und `(Pl.)` entfernt; inhaltliche Klammerzusätze wie `(für ein Tier)` bleiben); `Back` = UKR-Zwillings-Front mit kyrillischen Genus-Markern zu `(m)/(f)/(n)/(pl)` konvertiert und ans Ende gestellt (Mehrfachformen → kombiniert, z. B. `(m/f)`); `Example` = UKR-Satz + `<br><br>` + DE-Satz; `Niveau`-Wert als Level-Tag (Einzelnorm, siehe 1.4). ⚠️ Der sammlungsweite Duplikat-Check von `add_notes` greift **typübergreifend über das erste Feld**: Begriffe, deren neues Front identisch mit der Legacy-Zwillings-Front ist (kein Plural-Suffix, Verb, Klammerzusatz unverändert), kollidieren mit dem eigenen Altbestand → `allow_duplicate: true` ist gerechtfertigt, wenn per Query verifiziert wurde, dass die Kollision ausschließlich die ohnehin zu löschenden Legacy-Notizen betrifft.

**Variante `Tandem Cafe Basic++++` (ehem. Altbestand in `11 - Landschaften`; Notizen gelöscht, Notiztyp bleibt in der Collection):** gleiche Felder, aber: `Beispielsatz` einsprachig in der Sprache der jeweiligen Front-Seite (die Übersetzung des Satzes steht in der Zwillingsnotiz); die Umkehrrichtung ist je Begriff als **eigene Zwillingsnotiz** angelegt (1 Notiz = 1 Karte, kein Reverse-Template). `Grammatik` enthält Genus/Wortart des **Front-Begriffs**, teils mit Zusätzen wie „kein Plural" oder „Eigenname".

**Nutzer-Intention — Grammatik-Zusätze („kein Plural", „Eigenname"):** Der Nutzer möchte diese Zusätze möglicherweise künftig auch in den normierten Karten führen. Die konkrete Zuordnung je Begriff ist bei Bedarf **neu zu erheben** — mit der Löschung des Altbestands steht auch dessen `Grammatik`-Feld nicht mehr als Quelle zur Verfügung. Dieses Dokument speichert bewusst keine begriffsbezogenen Qualifier (also z. B. nicht, welches konkrete Wort ein Eigenname ist).

### 1.3 Audio-Einbettung (Beispielsatz-Audio)

Audio wird **nicht** in einem eigenen Feld gespeichert, sondern als `[sound:Datei.mp3]` am Anfang des `Example`-Feldes:

```
[sound:derberuf_bsp.mp3]<br><br>Моя професія — учитель.<br><br>Mein Beruf ist Lehrer.
```

**Media-Ordner:** Es gibt **einen einzigen Media-Ordner für alle Decks** der Collection (keine Deck-eigenen Ordner): `~/snap/anki-desktop/common/User 1/collection.media`. Damit sich Dateien verschiedener Decks nicht in die Quere kommen, trägt jede zukünftig erstellte Media-Datei ein **6-stelliges, alphanumerisches Zufalls-Suffix** (nur Kleinbuchstaben und Ziffern).

**Dateinamen-Konvention (ab 17.09.2026, durchgehend klein):** kleingeschriebener deutscher Begriff + `_bsp` + Zufalls-Suffix + `.mp3`:
- Muster: `begriff_bsp_<suffix>.mp3`, z. B. `dieentfremdung_bsp_t67afg.mp3`
- Basisname: Begriff kleingeschrieben; Satzzeichen werden entfernt (→ `derchefdiechefin`), Umlaute bleiben erhalten (→ `dasbüro`).

**Groß-/Kleinschreibung:** `store_media_file` legt Dateien **kleingeschrieben** ab. Karten und Dateien müssen **exakt übereinstimmen** — auf case-insensitive Auflösung ist kein Verlass: CamelCase-Referenzen (alte Konvention) funktionierten anfangs in der Anki-App, nach einem **Medien-Check** war die Verbindung Karte↔Datei jedoch gebrochen (Playback ohne Ton). Daher gilt ab sofort: Dateinamen **und** `[sound:...]-Referenzen` durchgehend kleingeschreiben, damit beide identisch sind.

**Projekt-Root:** Die generierten MP3s liegen zusätzlich lokal im Projekt-Root. Dort befinden sich auch ältere Vergleichsdateien anderer TTS-Anbieter (Suffixe wie `_MiniMaxSpeech2.8Turbo`, `_MAI-Voice-2_...`, `_gemini-...`) — diese sind **nicht** an Karten gebunden.

Die Decks `10 - Kindheit`, `07 - Tiere und Haustiere` (seit 16.09.2026) und `12 - Literatur` (seit 17.09.2026) sind vollständig mit Beispiel-Audio versehen (eine Datei pro UKR-Beispielsatz; bei `10 - Kindheit` hat die Karte mit zwei Satzpaaren zwei Dateien; bei `07` erhalten die vier ` <i>oder</i> `-Variantenkarten nur Audio der ersten Variante; bei `12` trägt die Aspektpaar-Karte `sich in ein Buch vertiefen` zwei Dateien, eines je Satzpaar).

### 1.4 Tags

| Tag | Bedeutung |
|---|---|
| `A1`, `A2`, `B1`, `B2`, `C1`, `C2` | Niveaustufe — Norm ab 16.09.2026 (Nutzer-Entscheidung, sammlungsweit): **genau ein Level-Tag je Notiz, nur Einzelwerte aus dieser Menge.** Altbestand mit Kombiwerten (`A1/A2`, `B1/B2` — Restbestand Stand 20.09.2026 in `02`, `10`, `11`) oder abweichenden Werten (`A2/B1`, `B2/C1` in `02`) wird bei Bearbeitung der jeweiligen Karte abgeleitet (Einzelnorm als Basis, Ableitung kontextabhängig im Einzelfall) und ersetzt; migriert bislang: `03 - Sport` (Rescan 20.09.2026: 67/67 Einzel-Tags, Literal-Tag `Niveau` entfernt) sowie `01 - Beruf` (20.09.2026, 46 Notes abgeleitet: `A1/A2` → `A1`×13/`A2`×6, `B1/B2` → `B1`×13/`B2`×6, 8 `Redewendung`-Notes ohne Level → `B1`×4/`B2`×4; Ergebnis: `A1`×13, `A2`×6, `B1`×19, `B2`×10, `C1`×20); die Migration der übrigen Bestandsdecks ist geplant, aber noch nicht umgesetzt |
| `Redewendung` | Idiom |
| `BadTranslation` | Übersetzung verworfen/mangelhaft — bei Suchen standardmäßig ausschließen (`-tag:BadTranslation`) |
| `NoExample` | Kein ukrainischer Beispielsatz vorhanden (Karte hat ggf. nur einen deutschen Beispielsatz im `Example`-Feld) |

---

## 2. Effektives Finden und Editieren über AnkiMCP

### 2.1 Relevante MCP-Tools

| Tool | Zweck | Wichtige Parameter |
|---|---|---|
| `find_notes` | Notizen per Anki-Query finden | `query`; liefert `noteIds[]` |
| `notes_info` | Details zu Notizen (Felder, Tags, Cards) | **`notes`** (nicht `noteIds`!), optional `include_fields` / `exclude_fields` / `excerpt_chars` |
| `update_notes` | Felder mehrerer Notizen in einem Batch ändern | `notes: [{ id, fields: { Feld: Wert } }]` (**`id`**, nicht `noteId`; Felder unter **`fields`** verschachteln!), `dry_run` |
| `update_note_fields` | Felder einer einzelnen Notiz ändern | |
| `add_notes` / `add_note` | Neue Notizen anlegen (Batch/einzeln) | `deck_name`, `model_name`, `notes: [{ fields: { Front, Back, Example }, tags: [...] }]` — Tags je Notiz im Item; `allow_duplicate` (Default `false`), Duplikatsprüfung **sammlungsweit** |
| `delete_notes` | Notizen **endgültig** löschen (inkl. aller zugehörigen Karten) | `notes: id[]`, `confirmDeletion: true` (Schutz — ohne ihn schlägt der Call fehl); `dry_run: true` für Vorschau |
| `store_media_file` | Datei nach `collection.media` kopieren | `{ filename, path }` — Pfad im Projekt-Root funktioniert (Snap kann `/tmp` nicht lesen); auch eine bestehende Datei im Media-Ordner selbst geht als Quelle (z. B. für Umbenennungen: unter neuem Namen speichern, alte löschen); Dateiname wird zu Kleinbuchstaben normalisiert (siehe 1.3) |
| `get_media_files_names` / `delete_media_file` | Media-Verwaltung | `pattern` für Glob-Filter; löschen verschiebt in Anki's Papierkorb |
| `tag_management` | Tags/Karten organisieren | Alle Parameter unter **`params: { action, ... }`** wrapper! |
| `card_management` | Karten organisieren | |

### 2.2 Suchen (Query-Beispiele)

```
deck:"#7 - Sprachcafé::01 - Beruf" -tag:BadTranslation      # Ziel-Deck ohne Ausschuss
deck:"#7 - Sprachcafé::01 - Beruf" tag:BadTranslation       # nur die verworfenen
```

- Decknamen mit Leerzeichen/Sonderzeichen in **doppelte Anführungszeichen**.
- `find_notes` liefert standardmäßig max. 100 Notizen (`limit`/`offset` Parameter vorhanden) — bei kleinen Decks unkritisch.

### 2.3 Bewährter Workflow: Audio an Karten hängen

1. **Selektieren:** `find_notes` mit Deck- + Tag-Filter.
2. **Analyse:** `notes_info` → prüfen: `Example` gefüllt? Enthält ein Feld bereits `[sound:`? (`hasSound`-Check über alle Felder).
3. **Audio erzeugen:** `bin/tts-cartesia.py` (siehe Abschnitt 3).
4. **Media speichern:** Dateinamen **kleingeschrieben** mit Zufalls-Suffix bilden (Konvention 1.3) und per `store_media_file` speichern; der `[sound:]`-Tag im Feld muss den Dateinamen exakt übernehmen.
5. **Feld aktualisieren:** `update_notes` mit `[sound:DATEI]<br><br>` + **Originalwert** des `Example`-Feldes (vorher `.trim()`en). Vorher `dry_run: true` — verifiziert alle Einträge ohne zu schreiben.
6. **Verifizieren:** Stichproben per `notes_info` + Zählabfrage (wie viele ohne `[sound:` übrig).

`update_notes` akzeptiert Batches bis `max_notes_per_batch: 100`. Fehler betreffen immer nur die jeweilige Notiz (`per-note results`), nicht den ganzen Batch.

### 2.4 Direktaufruf vs. mcpScript

- **Einzelne MCP-Calls:** Namespace-Proxy `mcp__anki_mcp` — liefert das Ergebnis **direkt geparst** zurück (z. B. `{ noteIds, count, total }`).
- **Mehrere Calls mit Logik** (Schleifen, Chunks, Fan-out): `mcpScript` mit `tools.anki_mcp_*`. Wichtig: Das Ergebnis ist dort **doppelt verpackt**:

```javascript
const res = await tools.anki_mcp_notes_info({ notes: [/*...*/] });
const parsed = JSON.parse(res.data.content[0].text);   // → { notes: [...] }
```

---

### 2.5 Bewährter Workflow: Vokabeln aus Tandem-Café-Arbeitsblatt (PDF) übernehmen

1. **PDF extrahieren:** `pdftotext -layout <datei>.pdf <ausgabe>.txt`; Diskussionsfragen/Satzanfänge am Ende nur aufnehmen, wenn der Nutzer es verlangt.
2. **Bestand abgleichen:** `find_notes` auf das Zieldeck (`-tag:BadTranslation`) + `notes_info` mit `include_fields: ["Front"]` in Chunks; Abgleich über die `Front`-Felder.
3. **Vorschlag mit Freigabe:** Kandidaten als Tabelle (Front/Back/Example/Tags) präsentieren, inkl. eigener Anmerkungen zur Übersetzungsqualität; Zwischenentscheidungen des Nutzers abwarten (Übersetzungsvarianten, Grundform-Kanonisierung wie `das Vorbild` statt `die Vorbilder`).
4. **Anlegen:** `add_notes`, Notiztyp `Basic (with reversed card and example sentences)`; Level- und `Redewendung`-Tags je Notiz im Item.
5. **Verifizieren:** Deck-Zählabfrage + Stichproben per `notes_info`; dabei auch die selbst ins Skript übertragenen Texte gegenlesen (Tippfehler-Gefahr, siehe Abschnitt 5).

⚠️ Die Duplikatsprüfung von `add_notes` läuft **sammlungsweit** über alle Decks, nicht nur im Zieldeck: `die Erziehung` für `10 - Kindheit` kollidierte mit einer Alt-Notiz in `08 - Familie und Generationen` → `skipped/duplicate`. Vorgehen nach Nutzerentscheidung (Konvention 5 im Kopf): Überspringen oder `allow_duplicate: true`.

---

## 3. Python-Skripte

### 3.1 `bin/tts-cartesia.py` (vorhanden, nicht Teil dieser Sessions erstellt)

Erzeugt MP3/WAV über die Cartesia-API (Modell Sonic 3.6, Standardsprache `uk`, aktuelle Stimme: „Oleh" — die einzige native ukrainische Stimme der Bibliothek).

```bash
bin/.venv/bin/python bin/tts-cartesia.py -i 'УКРАЇНСЬКИЙ РЕЧЕННЯ' -o 'Ausgabe_bsp.mp3'
# weitere Optionen: --list-voices, --save-voice <id>, --voice <id>, --language uk|de|en
```

- Muss mit dem **venv-Interpreter** `bin/.venv/bin/python` laufen (Abhängigkeiten: `bin/requirements.txt`).
- API-Key: ausschließlich über die Umgebungsvariable `CARTESIA_API_KEY` — `bin/.env` enthält **keinen** API-Key (dort steht nur `CARTESIA_VOICE_ID`).
- Exit-Code 0 + vorhandene, nicht-leere Ausgabedatei = Erfolg.

### 3.2 Batch-TTS-Skript (inline erstellt, hier konserviert)

Läuft die Worklist (JSONL) sequenziell ab, ruft je Zeile das TTS-Script auf und prüft das Ergebnis. Features: **Resume** (existierende Dateien > 1000 B werden übersprungen), **Fehlerprotokoll** nach `/tmp/beruf_tts_failures.json` (wird nur bei Fehlern angelegt), **keine Shell-Quoting-Probleme** (subprocess mit Argumentliste statt Shell-String — wichtig wegen ukrainischer Apostrophe `’`).

```python
import json, subprocess, os

os.chdir(os.path.expanduser("~/Dokumente/anki"))  # ~ wird in Python nicht automatisch expandiert
rows = [json.loads(l) for l in open("/tmp/beruf_audio.jsonl", encoding="utf-8") if l.strip()]
print(f"total rows: {len(rows)}", flush=True)

ok, fail = [], []
for i, r in enumerate(rows, 1):
    out = r["file"]
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        ok.append(out); print(f"[{i:02d}/{len(rows)}] SKIP (exists) {out}", flush=True); continue
    p = subprocess.run(
        ["bin/.venv/bin/python", "bin/tts-cartesia.py", "-i", r["uk"], "-o", out],
        capture_output=True, text=True, timeout=120
    )
    if p.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > 1000:
        ok.append(out); print(f"[{i:02d}/{len(rows)}] OK   {out} ({os.path.getsize(out)} B)", flush=True)
    else:
        fail.append((r["id"], out, (p.stderr or p.stdout).strip()[:200]))
        print(f"[{i:02d}/{len(rows)}] FAIL {out}: {(p.stderr or p.stdout).strip()[:150]}", flush=True)

print(f"\nDONE ok={len(ok)} fail={len(fail)}")
if fail:
    json.dump(fail, open("/tmp/beruf_tts_failures.json", "w"), ensure_ascii=False)
```

**Worklist-Format** (eine JSON-Zeile pro Karte; `uk` = exakter ukrainischer Satz aus dem `Example`-Feld, `file` = Zielname nach Konvention 1.3):

```json
{"id":1784060732221,"file":"derberuf_bsp.mp3","uk":"Моя професія — учитель."}
```

⚠️ Die Worklist lag in `/tmp/beruf_audio.jsonl` — **nicht persistent** (bei Bedarf neu erzeugen, siehe Workflow 2.3, Schritte 1–2).

### 3.3 Ukrainian-Satz aus `Example` extrahieren (JS/Python-Logik)

Robust gegen die Strukturvariante aus 1.2 (hier als JS aus dem mcpScript):

```javascript
const uk = exampleFieldValue
  .split(/<br\s*\/?>/i)[0]        // alles vor dem ersten <br>
  .replace(/<[^>]+>/g, " ")       // HTML-Tags entfernen (<div> … )
  .replace(/\s+/g, " ")
  .trim();
```

---

## 4. Limitierungen des Zugriffs über AnkiMCP

1. **Response-Größenlimits:** Große Antworten (z. B. `list_decks`) werden gekürzt/ausgelassen und stattdessen in eine temporäre Datei geschrieben (Pfad steht im `omitted`-Hinweis). Auch `notes_info` mit allen Feldern vieler Notizen kann das Limit erreichen — der Inhalt wird dann durch eine Zusammenfassung ersetzt.
2. **Kein Dateisystem-Zugriff in `mcpScript`:** `require("fs")` steht nicht zur Verfügung — mcpScript kann rechnen und MCP-Calls orchestrieren, aber **keine Dateien schreiben/lesen**. Datei-I/O muss über `bash`/`write`-Tools erfolgen.
3. **Kein direkter SQL-Zugriff** auf die Collection — alles läuft über die ~48 MCP-Tools.
4. **Kein automatischer AnkiWeb-Sync:** Media-Dateien landen nur lokal im Media-Ordner. Für andere Geräte muss der Medien-Sync in Anki manuell angestoßen werden.
5. **Snap-Sandbox:** Der MCP-Server (Anki-Desktop-Snap) kann **nicht aus `/tmp` lesen** („File not found", obwohl die Datei existiert) — Staging-Dateien immer im Projekt-Root ablegen.
6. **Inkonsistente Parameternamen über Tools hinweg:** `notes_info` will `notes`, `update_notes`-Einträge wollen `id` (und `fields`), `tag_management` will alles unter `params` — naiv geratene Namen erzeugen Validierungsfehler.

---

## 5. Beobachtete Probleme und bewährte Gegenmittel

| # | Problem | Gegenmittel (erprobt) |
|---|---|---|
| 1 | `ValidationError: Field required` bei falschen Parameternamen (`noteIds` statt `notes`, `noteId` statt `id`), fehlendem `fields`-Wrapper bei `update_notes`-Einträgen oder fehlendem `params`-Wrapper bei `tag_management` | Fehlermeldung lesen (nennt das erwartete Feld) oder Tool vorab mit `mcp describe` inspizieren |
| 2 | Größenlimit: Große Antworten verworfen; eine `find_notes`-Auswertung in mcpScript brach mit `content[0] undefined` ab | a) Gezielt `find_notes` statt `list_decks` nutzen; b) `notes_info` **in Chunks** von 8–16 Notizen abrufen; c) bei sporadischem Limit: einfachen Retry — das Limit greift nicht deterministisch |
| 3 | Doppelte Verpackung in mcpScript (`res.data.content[0].text` ist JSON-String) | Festes Parse-Muster: `JSON.parse(res.data.content[0].text)` (siehe 2.4) |
| 4 | `require is not defined` in mcpScript | Daten per `emit()` ausgeben und per `bash`/`write`-Tool in Datei sichern |
| 5 | Ukrainische Apostrophe (`’`, `'`) in Sätzen → Shell-Quoting-Risiko | Python `subprocess.run` mit **Argumentliste** statt Shell-String; single-quote-Regel `'\''` nur bei direkten Bash-Aufrufen nötig |
| 6 | Strukturvarianten im `Example`-Feld (`<div>…</div>` bei `der Burnout`) | Extraktion immer: Text vor erstem `<br>`, Tags strippen (3.3); vor Feld-Update Originalwert `.trim()`en und unverändert wieder einfügen |
| 7 | `store_media_file` normalisiert Dateinamen zu Kleinbuchstaben — CamelCase-Referenzen im `[sound:]`-Tag liefen nur über case-insensitive Auflösung; ein Medien-Check brach die Karte↔Datei-Verbindung (kein Playback mehr) | Konvention geändert (17.09.2026): Dateinamen **und** `[sound:]`-Referenzen durchgehend kleingeschrieben (siehe 1.3), damit beide exakt übereinstimmen; Eindeutigkeit über Zufalls-Suffix |
| 8 | Erwartungsabgleich Nutzer vs. Datenlage (zählbare Abweichungen bei Bulk-Operationen) | Vor Bulk-Operationen Zähler abfragen und Diskrepanz **inkl. Begründung** melden — erst nach Freigabe handeln |
| 9 | Übertragungsfehler beim Zusammenbauen langer Feldinhalte im Add-Skript (hier: DE/UKR-Text in einem Satz vermischt) | Nach Bulk-`add_notes` Stichproben per `notes_info` **gegenlesen**; Fehler gezielt per `update_notes` korrigieren |
| 10 | Inkonsistente Schlüssel in `notes_info`-Antworten: dieselbe Notiz teils unter `id`, teils unter `noteId` (je nach Aufrufkontext) — Naivzugriff auf `n.id` liefert dann `undefined` | Beim Parsen immer `n.noteId ?? n.id` abfragen; vor Bulk-Updates auf 0 gemappte Notizen prüfen und bei Problemen abbrechen (dry run schützt die Feldinhalte, nicht das Mapping) |

---

## 6. Diese Datei aktuell halten

Diese Datei ist ein **lebendes Dokument** und wird nach jeder Session fortgeschrieben, die Anki-Daten verändert oder neue Erkenntnisse über Struktur/Tools/Workflows liefert:

1. Nur die betroffenen Abschnitte ändern; flüchtige Angaben (Zahlen, „Stand …"-Hinweise) dabei entfernen, statt sie zu pflegen.
2. Annahmen, die nicht direkt aus Nutzerinstruktionen ableitbar sind, sind explizit zu benennen (Kopf der Datei bzw. im Text) — keine stillen Annahmen.
3. **Es wird kein Changelog geführt** — nur der Dokumentstand im Kopf wird auf das Datum der letzten Änderung aktualisiert.
