# Anki-MCP: Verwendung — Regeln, Konventionen, Workflows

> **Dokumentstand:** 06.10.2026
>
> **Geltungsbereich:** Nur zeitlose Regeln, Konventionen und Werkzeuge — alles, was in bisherigen Sessions erprobt und als Norm etabliert wurde; kein Anspruch auf Vollständigkeit der AnkiMCP-Tools.
>
> **Trennung:** Der **Datenbankstand** (Deck-Status, Coverage-Zahlen, Historie, offene Punkte) liegt in `Anki-Datenbankstand.md` (Projekt-Root) und wird nur bei Bedarf gelesen. Diese Datei enthält keinen Bestand.
>
> **Vorgeschichte:** Nachfolgerin des früheren `Anki-MCP-VerwendungUndAufbau.md` (am 06.10.2026 in Regeln + Stand aufgeteilt — Regelinhalt hierher, Datenbankstand in `Anki-Datenbankstand.md`). Ältere Session-Notizen nennen noch den alten Dateinamen; deren §-Verweise beziehen sich auf das alte Gesamtdokument und sind grob so zu übersetzen: §1.1–§1.4 → §1–§3 dieser Datei bzw. `Anki-Datenbankstand.md`; §2 → §4; §3 → §5; §4 → §6; §5 → §7; §6 → §8.

**Grundlegende Konventionen:**
1. **Decknamen:** Wird ein Deck nur mit Namen genannt (z. B. `10 - Kindheit`), ist — sofern nicht anders angegeben oder der vollständige Pfad genannt wird — immer das Subdeck von `#7 - Sprachcafé` gemeint (also z. B. `#7 - Sprachcafé::10 - Kindheit`).
2. **Sprachpaar:** Karten der Sprachcafé-Decks verwenden — sofern nicht explizit anders gefordert — immer **Deutsch + Ukrainisch** (Begriffe und Beispielsätze).
3. **Prompt-Sprache:** Anfragen können auf Deutsch oder Englisch gestellt werden.
4. **Sync:** Den AnkiWeb-Sync löst **der Nutzer manuell** aus — nicht selbstständig per `sync`-Tool synchronisieren.
5. **Duplikate:** Ob ein (sammlungsweites) Duplikat beim Anlegen erzwungen wird (`allow_duplicate: true`) oder übersprungen wird, entscheidet **der Nutzer im Einzelfall** — nicht selbstständig erzwingen.

**Hinweise:**
1. Speicherort: Projekt-Root `~/Dokumente/anki/`.
2. Inline im Session-Verlauf entstandene Skripte werden konserviert, damit sie nicht verloren gehen. Das frühere Inline-Batch-TTS-Skript ist mittlerweile eine echte Datei: `bin/batch-tts.py` (§5.2).

---

## 1. Kartenformat (Notiztyp und Konventionen)

### 1.1 Notiztyp

**`Basic (with reversed card and example sentences)`**

| Feld | Inhalt | Konventionen |
|---|---|---|
| `Front` | Deutscher Begriff / Redewendung | Rein textuell, z. B. `der Chef / die Chefin` |
| `Back` | Ukrainische Übersetzung + Genus des **ukrainischen** Wortes in Klammern | Marker: `(m)`, `(f)`, `(n)`, `(pl)`; Doppelformen `найкращий друг / найкраща подруга (m/f)`; Synonyme mit unterschiedlichem Genus erhalten je Wort einen eigenen Marker (`жарт (m), витівка (f)`); bei Mehrwort-Übersetzungen zählt der Kopf-Begriff (`гра в хованки (f)`, `шведська стінка (f)`); Verben ohne Marker. Alle Sprachcafé-Decks folgen dieser Konvention |
| `Example` | Ukrainischer Beispielsatz + deutsche Übersetzung | Standard: `УКР.<br><br>DE.` — mit Audio wird ein `[sound:...]-Tag` **vorangestellt** (§2) |

- Pro Notiz **2 Karten** (Normal + Umgekehrt); `notes_info` liefert dazu das Array `cards` mit zwei Card-IDs.
- **Parse-Regel (UKR-Satz):** Text **vor dem ersten** `<br>` nehmen und HTML-Tags strippen — robust auch bei Formatabweichungen (z. B. `<div>`-Wrapper).

### 1.2 Beispielsatz-Regel

- Der deutsche Satz im `Example` verwendet den Front-Begriff bzw. eine gebeugte Form davon; der ukrainische Satz entsprechend die Übersetzung aus dem Back bzw. eine gebeugte Form davon. Qualitätsprüfung misst Satzvorschläge an dieser Regel.
- **Synonym-Varianten:** Listet das `Back` zwei Synonyme, enthält das `Example` einen vollständigen UKR-Satz zur ersten Variante, dann den Varianten-Trenner (1.3), dann einen vollständigen zweiten UKR-Satz mit der zweiten Variante; der gemeinsame DE-Satz folgt einmal danach.

### 1.3 Varianten-Trenner

` <i>oder</i> ` (deutsch, kursiv). Legacy-Karten noch mit ` <i>або</i> ` → Umstellung, sobald die jeweilige Karte aus anderem Anlass bearbeitet wird; keine eigenständige Migration (Restbestand: Standsdatei).

⚠️ Parsing/Audio-Split **nur am getaggten Trenner** ausführen, nie am Klartext — „або“/„oder“ können Teil ukrainischer Wörter sein (z. B. з**або**лочених).

### 1.4 Gebilligte Strukturvarianten im `Example`

(Bewusste Nutzer-Entscheidung.)

- **Zwei vollständige UKR/DE-Satzpaare** in einem Feld; Feld-Aufbau: `Tag → UKR → DE → Tag → UKR → DE` — je Satzpaar eine eigene Audio-Datei (`_bsp2`, §2). Genutzt für Synonyme mit je eigenem Satz, für Aspektpaare (1.5) und für Höflichkeits-/Numerus-Paare (z. B. formale vs. singulare Imperativform).
- Zwei UKR-Varianten, getrennt durch den Varianten-Trenner (1.3).
- Kursive kulturelle Anmerkung am Feldende (nach dem DE-Satz).

Die Parse-Regel (1.1, UKR vor dem ersten `<br>`) bleibt bei allen Varianten unberührt.

### 1.5 Aspektpaare

Zwei-Paar-Muster (1.4) für Verbaspekte: erster Satz mit perfektiver Used-Form (natürliche Umgebung, z. B. nach `можна`/`треба`), zweiter Satz mit dem imperfektiven Back-Verb; die Reihenfolge der Paare (perf. zuerst oder umgekehrt) ist bewusst frei. Der DE-Satz jedes Pairs endet mit dem kursiven Marker ` <i>(perf.)</i>` bzw. ` <i>(imperf.)</i>`. Der Marker gehört **nicht** zum UKR-Satz (Parse-Regel bleibt sauber) und ist für TTS irrelevant, da nur UKR vorgelesen wird.

### 1.6 Normform in Klammern (`багато`)

Bei `багато`-Konstruktionen steht im Satz die natürliche Plural-Verbform, dahinter die Singular-Normform in Klammern — `використовують (використовує)`. Audio liest nur die Pluralform ohne Klammerzusatz (Klammerzusatz beim TTS strippen).

### 1.7 Altbestand-Familie `Tandem Cafe Basic*` (Anatomie für Transformationen)

Gemeinsam: Felder `Front`, `Back`, `Niveau`, `Grammatik`, `Beispielsatz`; Genus-Marker kyrillisch (z. B. `виховання (с.)`); `Beispielsatz` einsprachig; je Begriff 2 Zwillingsnotizen (UKR-Front + DE-Front), je 1 Karte.

- `Basic+`: `Niveau` gefüllt (Einzelwerte → direkte Level-Tags, §3); `Beispielsatz`-Paare der Zwillingsnotiz zueinander passend (DE + UKR), sodass die `Example` ohne Neudraft zusammensetzbar sind.
- `Basic++` / `Basic+++`: gleiche Anatomie; verbleibende Vorkommen: Standsdatei.
- Schlichtes `Basic`: `Grammatik` sprachspezifisch je Zwillingsnotiz — DE-Notiz deutsches Genus mit Zusätzen wie „kein Plural", „Eigenname", „Feste Wendung"; UKR-Notiz der ukrainische рід; Back-Marker kyrillisch `(м.)/(ж.)/(ч.)/(с.)`; keine Tags, Niveau nur im Feld.
- `Basic++++` (aufgelöst): `Beispielsatz` einsprachig in der Sprache der jeweiligen Front-Seite (die Übersetzung des Satzes steht in der Zwillingsnotiz); die Umkehrrichtung ist je Begriff eine **eigene** Zwillingsnotiz (1 Notiz = 1 Karte, kein Reverse-Template); `Grammatik` enthält Genus/Wortart des **Front-Begriffs**, teils mit Zusätzen wie „kein Plural" oder „Eigenname".

### 1.8 Transform-Rezept

Pro Begriffspaar 1 normierte Notiz:

- `Front` = DE-Zwillings-Front **ohne Plural-Suffix** (`, -e`-Muster und `(Pl.)` entfernt; inhaltliche Klammerzusätze wie `(für ein Tier)` bleiben)
- `Back` = UKR-Zwillings-Front, kyrillische Genus-Marker zu `(m)/(f)/(n)/(pl)` konvertiert und ans Ende gestellt; Mehrfachformen kombiniert (z. B. `(m/f)`)
- `Example` = UKR-Satz + `<br><br>` + DE-Satz
- `Niveau`-Wert als Level-Tag (Einzelnorm, §3)

⚠️ Der sammlungsweite Duplikat-Check von `add_notes` greift **typübergreifend über das erste Feld**: Begriffe, deren neues Front identisch mit der Legacy-Zwillings-Front ist (kein Plural-Suffix, Verb, Klammerzusatz unverändert), kollidieren mit dem eigenen Altbestand → `allow_duplicate: true` ist gerechtfertigt, wenn per Query verifiziert wurde, dass die Kollision ausschließlich die ohnehin zu löschenden Legacy-Notizen betrifft.

Legacy-only-Informationen (z. B. `Grammatik`-Qualifiers) als JSON in `session-notizen/` sichern — **nie** als begriffsbezogene Fakten in eines der beiden Dokumente (zur Nutzer-Intention „Grammatik-Zusätze": Standsdatei, Offene Punkte).

---

## 2. Audio-Norm (Beispielsatz-Audio)

Audio wird **nicht** in einem eigenen Feld gespeichert, sondern als `[sound:Datei.mp3]` am **Anfang** des `Example`-Feldes:

```
[sound:derberuf_bsp.mp3]<br><br>Моя професія — учитель.<br><br>Mein Beruf ist Lehrer.
```

- **Media-Ordner:** Es gibt **einen einzigen Media-Ordner für alle Decks** der Collection (keine Deck-eigenen Ordner): `~/snap/anki-desktop/common/User 1/collection.media`. Damit sich Dateien verschiedener Decks nicht in die Quere kommen, trägt jede neu erstellte Media-Datei ein **6-stelliges, alphanumerisches Zufalls-Suffix** (nur Kleinbuchstaben und Ziffern).
- **Dateinamen:** kleingeschriebener deutscher Begriff + `_bsp` + Zufalls-Suffix + `.mp3` → Muster `begriff_bsp_<suffix>.mp3`, z. B. `dieentfremdung_bsp_t67afg.mp3`. Basisname: Begriff kleingeschrieben, Satzzeichen entfernt (→ `derchefdiechefin`), Umlaute bleiben erhalten (→ `dasbüro`). Bei Karten mit zwei Satzpaaren erhält die zweite Datei `_bsp2` vor dem Suffix: `begriff_bsp2_<suffix>.mp3`.
- ⚠️ `store_media_file` legt Dateien **kleingeschrieben** ab. Karten und Dateien müssen **exakt übereinstimmen** — auf case-insensitive Auflösung ist kein Verlass: CamelCase-Referenzen (alte Konvention) funktionierten anfangs in der Anki-App, nach einem **Medien-Check** war die Verbindung Karte↔Datei jedoch gebrochen (Playback ohne Ton). Daher: Dateinamen **und** `[sound:...]`-Referenzen durchgehend kleinschreiben (s. auch §7).
- **Projekt-Root:** Die generierten MP3s liegen zusätzlich lokal im Projekt (Unterordner `mp3/`). Dort befinden sich auch ältere Vergleichsdateien anderer TTS-Anbieter (Suffixe wie `_MiniMaxSpeech2.8Turbo`, `_MAI-Voice-2_...`, `_gemini-...`) — diese sind **nicht** an Karten gebunden.

---

## 3. Tags

| Tag | Bedeutung |
|---|---|
| `A1`, `A2`, `B1`, `B2`, `C1`, `C2` | Niveaustufe — Norm: **genau ein Level-Tag je Notiz, nur Einzelwerte aus dieser Menge.** Altbestand mit Kombiwerten (`A1/A2`, `A2/B1`, `B1/B2`, `B2/C1`) wird bei Bearbeitung der jeweiligen Karte abgeleitet (Einzelnorm als Basis, Ableitung kontextabhängig im Einzelfall) und ersetzt; Migrationsstand: Standsdatei |
| `Redewendung` | Idiom |
| `BadTranslation` | Übersetzung verworfen/mangelhaft — bei Suchen standardmäßig ausschließen (`-tag:BadTranslation`) |
| `NoExample` | Kein ukrainischer Beispielsatz vorhanden (Karte hat ggf. nur einen deutschen Beispielsatz im `Example`-Feld). **Nicht** vorbeugend massenweise setzen, wenn die Beispiel-Ergänzung ohnehin unmittelbar ansteht — Setzung nur auf Nutzeranfrage (Nutzerentscheid 06.10.2026) |

---

## 4. Effektives Finden und Editieren über AnkiMCP

### 4.1 Relevante MCP-Tools

| Tool | Zweck | Wichtige Parameter |
|---|---|---|
| `find_notes` | Notizen per Anki-Query finden | `query`; liefert `noteIds[]` |
| `notes_info` | Details zu Notizen (Felder, Tags, Cards) | **`notes`** (nicht `noteIds`!), optional `include_fields` / `exclude_fields` / `excerpt_chars` |
| `update_notes` | Felder mehrerer Notizen in einem Batch ändern | `notes: [{ id, fields: { Feld: Wert } }]` (**`id`**, nicht `noteId`; Felder unter **`fields`** verschachteln!), `dry_run` |
| `update_note_fields` | Felder einer einzelnen Notiz ändern | |
| `add_notes` / `add_note` | Neue Notizen anlegen (Batch/einzeln) | `deck_name`, `model_name`, `notes: [{ fields: { Front, Back, Example }, tags: [...] }]` — Tags je Notiz im Item; `allow_duplicate` (Default `false`) ist ein **Batch-Parameter** (gilt für alle Notizen des Aufrufs — bei gemischten Kollisionsfällen den Batch splitten), Duplikatsprüfung **sammlungsweit** |
| `delete_notes` | Notizen **endgültig** löschen (inkl. aller zugehörigen Karten) | `notes: id[]`, `confirmDeletion: true` (Schutz — ohne ihn schlägt der Call fehl); `dry_run: true` für Vorschau |
| `store_media_file` | Datei nach `collection.media` kopieren (**nur absoluter Pfad**, §7 #13; für viele Dateien stattdessen `cp`, Workflow 4.3 Schritt 4) | `{ filename, path }` — Pfad im Projekt-Root funktioniert (Snap kann `/tmp` nicht lesen); auch eine bestehende Datei im Media-Ordner selbst geht als Quelle (z. B. für Umbenennungen: unter neuem Namen speichern, alte löschen); Dateiname wird zu Kleinbuchstaben normalisiert (§2) |
| `get_media_files_names` / `delete_media_file` | Media-Verwaltung | `pattern` für Glob-Filter; löschen verschiebt in Anki's Papierkorb |
| `tag_management` | Tags/Karten organisieren | Alle Parameter unter **`params: { action, ... }`** wrapper! |
| `card_management` | Karten organisieren | |

### 4.2 Suchen (Query-Beispiele)

```
deck:"#7 - Sprachcafé::01 - Beruf" -tag:BadTranslation      # Ziel-Deck ohne Ausschuss
deck:"#7 - Sprachcafé::01 - Beruf" tag:BadTranslation       # nur die verworfenen
```

- Decknamen mit Leerzeichen/Sonderzeichen in **doppelte Anführungszeichen**.
- `find_notes` liefert standardmäßig max. 100 Notizen (`limit`/`offset` Parameter vorhanden) — bei kleinen Decks unkritisch.

### 4.3 Bewährter Workflow: Audio an Karten hängen

1. **Selektieren:** `find_notes` mit Deck- + Tag-Filter.
2. **Analyse:** `notes_info` → prüfen: `Example` gefüllt? Enthält ein Feld bereits `[sound:`? (`hasSound`-Check über alle Felder).
3. **Audio erzeugen:** `bin/tts-cartesia.py` (§5.1), bei mehreren Karten `bin/batch-tts.py` (§5.2).
4. **Media verteilen:** Dateinamen **kleingeschrieben** mit Zufalls-Suffix bilden (§2). Standard ab 06.10.2026: direktes `cp mp3/<name>.mp3 "$HOME/snap/anki-desktop/common/User 1/collection.media/"` — ein Bash-Call für beliebig viele Dateien (kein MCP-Limit, keine Pfad-Falle §7 #13). ⚠️ `cp` normalisiert **nicht** zu Kleinbuchstaben — Namen müssen bereits kleingeschrieben sein (§2-Generator). Extern eingefügte Dateien erfasst Anki beim nächsten Medien-Sync/Medien-Check automatisch. Einzel-/Sonderfälle weiterhin per `store_media_file` (absoluter Pfad!). Der `[sound:]`-Tag im Feld muss den Dateinamen exakt übernehmen.
5. **Feld aktualisieren:** `update_notes` mit `[sound:DATEI]<br><br>` + **Originalwert** des `Example`-Feldes (vorher `.trim()`en). Vorher `dry_run: true` — verifiziert alle Einträge ohne zu schreiben.
6. **Verifizieren:** Stichproben per `notes_info` + Zählabfrage (wie viele ohne `[sound:` übrig).

`update_notes` akzeptiert Batches bis `max_notes_per_batch: 100`. Fehler betreffen immer nur die jeweilige Notiz (`per-note results`), nicht den ganzen Batch.

### 4.4 Direktaufruf vs. mcpScript

- **Einzelne MCP-Calls:** Namespace-Proxy `mcp__anki_mcp` — liefert das Ergebnis **direkt geparst** zurück (z. B. `{ noteIds, count, total }`).
- **Mehrere Calls mit Logik** (Schleifen, Chunks, Fan-out): `mcpScript` mit `tools.anki_mcp_*`. Wichtig: Das Ergebnis ist dort **doppelt verpackt**:

⚠️ **Beobachtung (06.10.2026):** In der aktuellen anki-mcp-Server-Version ist `mcpScript` nicht mehr auffindbar (Tool-Suche leer). Mehrstufige Logik läuft stattdessen als direkte Einzelaufrufe über den Namespace-Proxy (ggf. mehrere Calls parallel pro Nachricht).

```javascript
const res = await tools.anki_mcp_notes_info({ notes: [/*...*/] });
const parsed = JSON.parse(res.data.content[0].text);   // → { notes: [...] }
```

### 4.5 Bewährter Workflow: Vokabeln aus Tandem-Café-Arbeitsblatt (PDF) übernehmen

1. **PDF extrahieren:** `pdftotext -layout <datei>.pdf <ausgabe>.txt`; Diskussionsfragen/Satzanfänge am Ende nur aufnehmen, wenn der Nutzer es verlangt.
2. **Bestand abgleichen:** `find_notes` auf das Zieldeck (`-tag:BadTranslation`) + `notes_info` mit `include_fields: ["Front"]` in Chunks; Abgleich über die `Front`-Felder.
3. **Vorschlag mit Freigabe:** Kandidaten als Tabelle (Front/Back/Example/Tags) präsentieren, inkl. eigener Anmerkungen zur Übersetzungsqualität; Zwischenentscheidungen des Nutzers abwarten (Übersetzungsvarianten, Grundform-Kanonisierung wie `das Vorbild` statt `die Vorbilder`).
4. **Anlegen:** `add_notes`, Notiztyp `Basic (with reversed card and example sentences)`; Level- und `Redewendung`-Tags je Notiz im Item.
5. **Verifizieren:** Deck-Zählabfrage + Stichproben per `notes_info`; dabei auch die selbst ins Skript übertragenen Texte gegenlesen (Tippfehler-Gefahr, siehe §7).

⚠️ Die Duplikatsprüfung von `add_notes` läuft **sammlungsweit** über alle Decks, nicht nur im Zieldeck: `die Erziehung` für `10 - Kindheit` kollidierte mit einer Alt-Notiz in `08 - Familie und Generationen` → `skipped/duplicate`. Vorgehen nach Nutzerentscheidung (Konvention 5 im Kopf): Überspringen oder `allow_duplicate: true`.

---

## 5. Python-Skripte

### 5.1 `bin/tts-cartesia.py` (vorhanden, nicht Teil dieser Sessions erstellt)

Erzeugt MP3/WAV über die Cartesia-API (Modell Sonic 3.6, Standardsprache `uk`, aktuelle Stimme: „Oleh" — die einzige native ukrainische Stimme der Bibliothek).

```bash
bin/.venv/bin/python bin/tts-cartesia.py -i 'УКРАЇНСЬКИЙ РЕЧЕННЯ' -o 'Ausgabe_bsp.mp3'
# weitere Optionen: --list-voices, --save-voice <id>, --voice <id>, --language uk|de|en
```

- Muss mit dem **venv-Interpreter** `bin/.venv/bin/python` laufen (Abhängigkeiten: `bin/requirements.txt`).
- API-Key: ausschließlich über die Umgebungsvariable `CARTESIA_API_KEY` — `bin/.env` enthält **keinen** API-Key (dort steht nur `CARTESIA_VOICE_ID`).
- Exit-Code 0 + vorhandene, nicht-leere Ausgabedatei = Erfolg.

### 5.2 `bin/batch-tts.py` (Batch-TTS mit Resume)

Echte Datei; arbeitet eine Worklist (JSONL, eine Zeile je Karte) sequenziell über §5.1 ab:

```bash
bin/.venv/bin/python bin/batch-tts.py <worklist.jsonl> [--failures /tmp/tts_failures.json]
```

- **Worklist-Format:** `uk` = exakter ukrainischer Satz aus dem `Example` (nach Parse-Regel 1.1; Aspekt-Marker 1.5 und `багато`-Klammerzusatz 1.6 strippen); `file` = Zielname nach §2, Pfade relativ zum Aufrufverzeichnis (Projekt-Root empfohlen):

  ```json
  {"id":1784060732221,"file":"derberuf_bsp.mp3","uk":"Моя професія — учитель."}
  ```

- **Resume:** existierende Dateien > 1000 B werden übersprungen; **Fehlerprotokoll** nur bei Fehlern; **keine Shell-Quoting-Probleme** (subprocess mit Argumentliste — ukrainische Apostrophe `’` harmlos); Exit-Code 1 bei Fehlern.
- ⚠️ Worklists in `/tmp` sind **nicht persistent** — bei Bedarf aus Live-Daten neu erzeugen (Workflow 4.3, Schritte 1–2) oder dauerhaft in `session-notizen/` ablegen (Stand der deckweiten Läufe: Standsdatei).

### 5.3 Ukrainian-Satz aus `Example` extrahieren (JS/Python-Logik)

Robust gegen die Strukturvarianten aus §1.4 (hier als JS):

```javascript
const uk = exampleFieldValue
  .split(/<br\s*\/?>/i)[0]        // alles vor dem ersten <br>
  .replace(/<[^>]+>/g, " ")       // HTML-Tags entfernen (<div> … )
  .replace(/\s+/g, " ")
  .trim();
```

---

## 6. Limitierungen des Zugriffs über AnkiMCP

1. **Response-Größenlimits:** Große Antworten (z. B. `list_decks`) werden gekürzt/ausgelassen und stattdessen in eine temporäre Datei geschrieben (Pfad steht im `omitted`-Hinweis). Auch `notes_info` mit allen Feldern vieler Notizen kann das Limit erreichen — der Inhalt wird dann durch eine Zusammenfassung ersetzt.
2. **Kein Dateisystem-Zugriff in `mcpScript`:** `require("fs")` steht nicht zur Verfügung — mcpScript kann rechnen und MCP-Calls orchestrieren, aber **keine Dateien schreiben/lesen**. Datei-I/O muss über `bash`/`write`-Tools erfolgen.
3. **Kein direkter SQL-Zugriff** auf die Collection — alles läuft über die ~48 MCP-Tools.
4. **Kein automatischer AnkiWeb-Sync:** Media-Dateien landen nur lokal im Media-Ordner. Für andere Geräte muss der Medien-Sync in Anki manuell angestoßen werden.
5. **Snap-Sandbox:** Der MCP-Server (Anki-Desktop-Snap) kann **nicht aus `/tmp` lesen** („File not found", obwohl die Datei existiert) — Staging-Dateien immer im Projekt-Root ablegen.
6. **Kein Delete-Tool für Notiztypen** — leergelaufene Altbestand-Typen können nur manuell über die Anki-GUI gelöscht werden.

---

## 7. Beobachtete Probleme und bewährte Gegenmittel

| # | Problem | Gegenmittel (erprobt) |
|---|---|---|
| 1 | `ValidationError: Field required` bei falschen Parameternamen (`noteIds` statt `notes`, `noteId` statt `id`), fehlendem `fields`-Wrapper bei `update_notes`-Einträgen oder fehlendem `params`-Wrapper bei `tag_management`; bei `add_notes` gehören `deck_name`/`model_name` auf **Batch-Ebene**, nicht ins Notiz-Item | Fehlermeldung lesen (nennt das erwartete Feld) oder Tool vorab mit `mcp describe` inspizieren |
| 2 | Größenlimit: Große Antworten verworfen; eine `find_notes`-Auswertung in mcpScript brach mit `content[0] undefined` ab | a) Gezielt `find_notes` statt `list_decks` nutzen; b) `notes_info` **in Chunks** von 8–16 Notizen abrufen; c) bei sporadischem Limit: einfachen Retry — das Limit greift nicht deterministisch |
| 3 | Doppelte Verpackung in mcpScript (`res.data.content[0].text` ist JSON-String) | Festes Parse-Muster: `JSON.parse(res.data.content[0].text)` (siehe 4.4) |
| 4 | `require is not defined` in mcpScript | Daten per `emit()` ausgeben und per `bash`/`write`-Tool in Datei sichern |
| 5 | Ukrainische Apostrophe (`’`, `'`) in Sätzen → Shell-Quoting-Risiko | Python `subprocess.run` mit **Argumentliste** statt Shell-String (`bin/batch-tts.py` macht das fertig); single-quote-Regel `'\''` nur bei direkten Bash-Aufrufen nötig |
| 6 | Strukturvarianten im `Example`-Feld (`<div>…</div>` bei `der Burnout`) | Extraktion immer: Text vor erstem `<br>`, Tags strippen (5.3); vor Feld-Update Originalwert `.trim()`en und unverändert wieder einfügen |
| 7 | `store_media_file` normalisiert Dateinamen zu Kleinbuchstaben — CamelCase-Referenzen im `[sound:]`-Tag liefen nur über case-insensitive Auflösung; ein Medien-Check brach die Karte↔Datei-Verbindung (kein Playback mehr) | Dateinamen **und** `[sound:]`-Referenzen durchgehend kleingeschrieben (§2), damit beide exakt übereinstimmen; Eindeutigkeit über Zufalls-Suffix |
| 8 | Erwartungsabgleich Nutzer vs. Datenlage (zählbare Abweichungen bei Bulk-Operationen) | Vor Bulk-Operationen Zähler abfragen und Diskrepanz **inkl. Begründung** melden — erst nach Freigabe handeln |
| 9 | Übertragungsfehler beim Zusammenbauen langer Feldinhalte im Add-Skript (hier: DE/UKR-Text in einem Satz vermischt) | Nach Bulk-`add_notes` Stichproben per `notes_info` **gegenlesen**; Fehler gezielt per `update_notes` korrigieren |
| 10 | Inkonsistente Schlüssel in `notes_info`-Antworten: dieselbe Notiz teils unter `id`, teils unter `noteId` (je nach Aufrufkontext) — Naivzugriff auf `n.id` liefert dann `undefined` | Beim Parsen immer `n.noteId ?? n.id` abfragen; vor Bulk-Updates auf 0 gemappte Notizen prüfen und bei Problemen abbrechen (dry run schützt die Feldinhalte, nicht das Mapping) |
| 11 | Manuelles Zusammenbauen großer `update_notes`-Payloads (hier: 66 Einträge mit `[sound:]`-Präfix) produziert **Übertragungsfehler im eigenen Text** (UKR-Wörter im DE-Satz), die der Dry-Run **nicht** findet — er validiert nur serverseitig, nicht gegen den Originalinhalt | Payloads in **kleinen Batches (≤ 8 Notizen)** schreiben; nach jedem Execute Read-back **aller** Notizen des Batches und Zeilenvergleich gegen den bekannten Originalwert (`[sound:Tag] + Original`); Abweichungen gezielt per Einzel-Update (`update_note_fields`) korrigieren und erneut read-backen |
| 12 | Feldsuche mit `:` im Suchbegriff schlägt lautlos fehl (`Example:sound:` → 0 Treffer, obwohl `[sound:...]` vorhanden) | Wildcard-Form nutzen: `Example:*sound*`; für belastbare Checks zusätzlich `notes_info` + `hasSound` über alle Felder (Workflow 4.3, Schritt 2) |
| 13 | `store_media_file` mit **relativem** Pfad → „File not found“, obwohl die Datei existiert (Server löst relativ zu seinem eigenen Arbeitsverzeichnis auf, nicht zum Projekt-Root) | Absoluten Pfad im Projekt-Root angeben (z. B. `/home/<user>/Dokumente/anki/mp3/…`); Vorhandensein über `get_media_files_names` mit Glob-Muster verifizieren |

---

## 8. Diese Dokumente aktuell halten

- **Regeldatei (diese Datei):** Lebendes Dokument — ändern, wenn sich Konventionen, Tools, Workflows oder Gegenmittel ändern. **Kein DB-Stand hier:** Zahlen, Deck-Statusdaten und „Stand …"-Hinweise gehören in die Standsdatei, nicht in den Regeltext. Neue Konvention → Datum in die Konventions-Timeline (Anhang) eintragen.
- **Standsdatei (`Anki-Datenbankstand.md`):** Nach **jeder** datenändernden Session aktualisieren (betroffene Deck-Blöcke, Zähler, Coverage, offene Punkte) und den „Stand"-Kopf datieren. Die lebenden Anki-Daten bleiben die Autorität; die Standsdatei ist das aufgezeichnete Bild davon.
- **Beide:** Annahmen, die nicht direkt aus Nutzerinstruktionen ableitbar sind, sind explizit zu benennen — keine stillen Annahmen. **Es wird kein Changelog geführt** — nur der Dokumentstand im Kopf wird auf das Datum der letzten Änderung aktualisiert. Änderungen zuerst anwenden, dann präsentieren — keine vorherige Freigabe nötig.

---

## Anhang A: Konventions-Timeline

| Datum | Eingeführt |
|---|---|
| 15.09.2026 | Varianten-Trenner ` <i>oder</i> ` |
| 16.09.2026 | Level-Tag-Einzelwert-Norm; Beispielsatz-Regel; Synonym-Varianten-Muster im `Example` |
| 17.09.2026 | Audio-Namenskonvention durchgehend kleingeschrieben (CamelCase-Referenzen nach Medien-Check gebrochen) |
| 24.09.2026 | Normform in Klammern (`багато`); Zwei-Paar-Muster für Aspektpaare; Altbestand-Typen `Basic`/`Basic+`/`Basic++++` manuell gelöscht (vgl. §6.6) |
| 06.10.2026 | Aspekt-Marker `(perf.)`/`(imperf.)`; Höflichkeits-/Numerus-Zweipaar; `mcpScript` in aktueller Server-Version nicht mehr auffindbar → Einzelaufrufe über den Namespace-Proxy |
| 06.10.2026 | `NoExample` nur auf Nutzeranfrage setzen — nicht massenweise, wenn die Beispiel-Ergänzung (Phase 4) unmittelbar geplant ist (Nutzerentscheid) |
| 06.10.2026 | `store_media_file` nur mit absoluten Pfaden (relativ → „File not found“); Verifikation über `get_media_files_names` |
| 06.10.2026 | Media-Verteilung bevorzugt per `cp` in `collection.media` (Menge ×1 statt N MCP-Calls; `cp` normalisiert nicht — Namen bereits kleingeschreiben); `store_media_file` für Einzel-/Sonderfälle |
