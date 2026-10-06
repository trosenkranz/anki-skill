# Anki-Datenbankstand

> **Stand:** 06.10.2026
>
> **Pflege:** Nach jeder datenändernden Session aktualisieren (betroffene Deck-Blöcke, Zähler, Coverage, offene Punkte) und diesen Kopf datieren — Regeln: `Anki-MCP-Verwendung.md` §8. **Nur lesen, wenn Bestandsinformationen gebraucht werden** (Status-/Coverage-/Historie-Anfragen, deckweite Aktionen). Die lebenden Anki-Daten sind immer die Autorität; kein Changelog. Konventionen liegen nicht hier, sondern in der Regeldatei. — Nachfolgerin des früheren `Anki-MCP-VerwendungUndAufbau.md` (s. „Vorgeschichte“ im Kopf der Regeldatei).

## Deck-Übersicht `#7 - Sprachcafé`

Decks: `01 - Beruf`, `02 - Ausbildung & Studium`, `03 - Sport`, `04 - Musik & Kunst`, `07 - Tiere und Haustiere`, `08 - Familie und Generationen`, `09 - Wohnen`, `10 - Kindheit`, `11 - Landschaften`, `12 - Literatur`, `13 - Technologie`, `14 - Herbst` (Trenner `::`, numerische Präfixe sortieren).

| Deck | Format | Level-Tags | Beispiel-Audio | Offen |
|---|---|---|---|---|
| `01 - Beruf` | normiert | ✅ migriert | Bestand vorhanden, Vollständigkeit ungeprüft | Audio-Check |
| `02 - Ausbildung & Studium` | normiert | ✅ migriert | ✅ UKR-Beispiele + Audio vollständig seit 06.10.2026 (74 Dateien für 72 Karten) | — |
| `03 - Sport` | normiert | ✅ migriert | ✅ vollständig | — |
| `04 - Musik & Kunst` | ❌ nicht normiert | Altbestand | — | Normierung (nur DE-Beispiele, kyrillische Marker), Tag-Migration |
| `07 - Tiere und Haustiere` | normiert | Einzel-Tags | ✅ vollständig | — |
| `08 - Familie und Generationen` | ❌ Legacy (`Tandem Cafe Basic++`) | Altbestand | — | Transformation |
| `09 - Wohnen` | ❌ Legacy (`Tandem Cafe Basic+++`) | Altbestand | — | Transformation |
| `10 - Kindheit` | normiert | Kombi-Restbestand | ✅ vollständig | Tag-Migration, 1 × `або`-Trenner |
| `11 - Landschaften` | normiert | Kombi-Restbestand | nicht dokumentiert | Tag-Migration, 1 × `або`-Trenner, Audio-Check |
| `12 - Literatur` | normiert | Einzel-Tags | ✅ vollständig | — |
| `13 - Technologie` | normiert | Einzel-Tags | ✅ vollständig | — |
| `14 - Herbst` | normiert | Einzel-Tags | ✅ vollständig | 3 bewusste sammlungsweite Duplikate (s. u.) |

Außerhalb `#7`: Root-Bestand ohne Tags — Level-Tag-Migration geplant, nicht begonnen.

## Deck-Details

### `01 - Beruf`
- Normiert. Level-Tags migriert (20.09.2026, 46 Kombi-/Level-lose Notes): `A1/A2` → `A1`×13/`A2`×6, `B1/B2` → `B1`×13/`B2`×6, 8 `Redewendung`-Notes ohne Level → `B1`×4/`B2`×4. Ergebnis: `A1`×13, `A2`×6, `B1`×19, `B2`×10, `C1`×20.
- Audio: in einer frühen Session bestückt (erste Worklist `/tmp/beruf_audio.jsonl` — verfallen); **nicht** in der Liste der verifiziert vollständigen Decks → vor Audio-Arbeit Live-Check (`hasSound`).

### `02 - Ausbildung & Studium`
- Normiert; Bestand: 72 Notizen (06.10.2026: +3 neue, −1 aufgeteilt). **UKR-Beispielsätze vollständig seit 06.10.2026** (Phase 4, 67 ergänzt; Verifikation: Batch-Read-backs + leer-`Example`-Abfrage = 0). Struktur: 53 Einzel-Sätze, 13 Karten mit Synonym-Varianten (` <i>oder</i> `): das Zeugnis, die Hochschule, der Studiengang, das Studienfach, die Ausbildung, die Klausur, der Abschluss, die Promotion, durchfallen, das Stipendium, die Zulassung, der Lebenslauf, die Voraussetzung; 1 Karte mit Zwei-Paar-Muster: `der/die Auszubildende`. `die Frist` mit älterem Audio (`diefrist_bsp_e9uyhw.mp3`). Deck bewusst **ohne** `NoExample`-Tags (Nutzerentscheid 06.10.2026: nicht vorbeugend setzen, wenn Ergänzung ansteht — Regeldatei §3).
- Audio 06.10.2026 (Phase 5, deckweit): **vollständig** — 73 neue Dateien via `bin/batch-tts.py` (0 Fehler), danach `store_media_file` (absolute Pfade nötig, s. Regeldatei §7) und Feld-Updates in 10 Batches (Dry-Run → Execute → Read-back). Zwei-Paar-Karten `ablegen` und `der/die Auszubildende` je 2 Dateien (`_bsp`/`_bsp2`); 13 ` <i>oder</i> `-Variantenkarten nur Audio der ersten Variante. Verifikation: `Example:*sound*` = 72/72 Karten, Stichproben der Dateinamen in `collection.media` exakt. Worklist: `session-notizen/2026-10-06_02-ausbildung_audio-worklist.jsonl`.
- Nutzerkorrekturen bei der Freigabe: durchfallen-DE „… beim ersten Mal durchgefallen“ (statt „gleich beim“), Aufnahmeprüfung-DE „Auf die Aufnahmeprüfung …“ (statt „Für die“), Fachuniversität-DE „… für den Beruf“ (statt „für einen Beruf“).
- QS 06.10.2026 (Nutzerfreigabe, umgesetzt + Read-back): Schreibfehler in `die Schulpflicht` (`обов'язкова` → `обов’язкова`); `der Geselle / die Gesellin` → Back `підмайстер / підмайстеркa (m/f)`; `der/die Auszubildende (Azubi)` → Back `учень на виробництві / учениця на виробництві (m/f), стажер / стажерка (m/f)`; `die Fachuniversität / die spezialisierte Hochschule` (Artikel ergänzt).
- `ablegen (eine Prüfung)` (B1): Front normalisiert; Back → `скласти (іспит)`; Zwei-Paar-Aspekt-Example (`склав`/`складає`, Marker `(perf.)`/`(imperf.)`) + kursive Anmerkung zu „bestehen“ (Tippfehler „im Ukrainischem“ korrigiert). Alter Back (Konjugationszeile + Anmerkung) gesichert: `session-notizen/2026-10-06_02-ablegen-alt-back.md`.
- Aufteilung 06.10.2026: `das Ansehen / das Prestige` (Back `престиж (m), визнання (n)`) ersetzt durch drei Karten je B2 mit Beispiel: `das Ansehen` → `авторитет (m)`, `das Prestige` → `престиж (m)`, `die Anerkennung` → `визнання (n)`; alte kombinierte Notiz gelöscht (Dry-Run, 1 Notiz + 2 Karten).
- Level-Tags migriert (24.09.2026, 28 Kombi-Notes): `A1/A2` → `A1`×3, `A2/B1` → `A2`×7/`B1`×1, `B1/B2` → `B1`×8/`B2`×1, `B2/C1` → `B2`×3/`C1`×5. Ergebnis: `A1`×4, `A2`×10, `B1`×28, `B2`×17, `C1`×11.

### `03 - Sport`
- Normiert seit 26.09.2026 (UKR-Beispielsätze ergänzt, kyrillische Genus-Marker konvertiert, `Front` von Plural-Suffixen, Paar-Suffixen wie `, -nen` und Verb-Klammerzusätzen befreit).
- Tags: 67/67 Einzel-Tags; Literal-Tag `Niveau` entfernt.
- Audio vollständig seit 26.09.2026: 69 Dateien für 67 Karten — 2 Aspektpaar-Karten × 2 Dateien (`_bsp2`), 8 ` <i>oder</i> `-Variantenkarten nur erste Variante. Worklist: `session-notizen/2026-09-26_03-sport_audio-worklist.jsonl`.

### `04 - Musik & Kunst`
- Nicht normiert: `Example`-Felder bisher nur mit deutschem Satz; Genus-Marker teils kyrillisch (`ж.`).

### `07 - Tiere und Haustiere`
- Normiert seit 16.09.2026 (Transform `Basic+`: 65 normierte Notizen erstellt, 130 Alt-Notizen gelöscht). Legacy-`Grammatik` gesichert: `session-notizen/2026-09-16_07-tiere_legacy-grammatik.json`.
- Audio vollständig seit 16.09.2026; vier ` <i>oder</i> `-Variantenkarten nur Audio der ersten Variante. Worklist: `session-notizen/2026-09-16_07-tiere_audio-worklist.jsonl`.
- Historie: die leere normierte Alt-Notiz `die Bibliothek` wurde bei der 12-er-Transformation auf Nutzerentscheidung gelöscht (Begriff steht jetzt in `12` mit Beispielsatz).

### `08 - Familie und Generationen`
- Legacy-Zwillinge `Tandem Cafe Basic++`: je Begriff 2 Notizen (je Richtung eine, je 1 Karte), `Beispielsatz` einsprachig pro Zwillingsnotiz.
- Enthält den von `14 - Herbst` bewusst geduldeten sammlungsweiten Duplikat-Zwilling `die Tradition`.

### `09 - Wohnen`
- Legacy-Zwillinge `Tandem Cafe Basic+++` (gleiche Anatomie wie `08`).

### `10 - Kindheit`
- Normiert; Strukturvarianten (Nutzer-Entscheidung): `die Unbeschwertheit/die Sorglosigkeit` mit zwei Satzpaaren; kursive kulturelle Anmerkung bei `die Schultüte`.
- ⚠️ `Verantwortung übernehmen` noch mit Legacy-Trenner ` <i>або</i> ` (Umstellung bei nächster Bearbeitung).
- Audio vollständig seit 16.09.2026 (die Zwei-Paar-Karte hat 2 Dateien).
- Tags: Kombi-Restbestand (`A1/A2` etc.) — Ableitung bei Kartenbearbeitung.

### `11 - Landschaften`
- Normiert; `Front` enthält den Begriff ohne Plural-Endung. Zwei-Paar-Karte: `aussterben`.
- ⚠️ `der Gletscher` noch mit ` <i>або</i> `-Trenner (Umstellung bei nächster Bearbeitung).
- Audio: nicht dokumentiert → vor Audio-Arbeit Live-Check (`hasSound`).
- Tags: Kombi-Restbestand — Ableitung bei Kartenbearbeitung.
- Historie: Altbestand `Tandem Cafe Basic++++` auf Nutzerentscheidung gelöscht (Notiztyp ebenfalls, s. u.).

### `12 - Literatur`
- Normiert seit 17.09.2026 (Transform schlichtes `Tandem Cafe Basic`: 29 normierte Notizen erstellt, 58 Alt-Notizen gelöscht). Legacy-`Grammatik` gesichert: `session-notizen/2026-09-17_12-literatur_legacy-grammatik.json`.
- Audio vollständig seit 17.09.2026; Aspektpaar-Karte `sich in ein Buch vertiefen` mit 2 Dateien (eines je Satzpaar).

### `13 - Technologie`
- Normiert seit 24.09.2026 (erneuter `Basic+`-Import: 88 Zwillingsnotizen mit gefülltem `Niveau` — nur Einzelwerte → direkte Level-Tags — und zueinander passenden DE/UKR-`Beispielsatz`-Paaren; 44 normierte Notizen erstellt, 88 Alt-Notizen gelöscht). Legacy-`Grammatik` gesichert: `session-notizen/2026-09-24_13-technologie_legacy-grammatik.json`.
- Bestand: 45 Notizen (seit 06.10.2026; Zuwachs: `der Kopfhörer` mit Höflichkeits-Zweipaar — formale/plurale vs. singulare Imperativform).
- Audio vollständig seit 24.09.2026: 51 Dateien für 45 Karten — 6 Zwei-Paar-Karten × 2 Dateien (`_bsp2`; Aspektpaare `herunterladen`, `aufladen`, `installieren`, `teilen`, `generieren` + Höflichkeits-Paar `der Kopfhörer`), ` <i>oder</i> `-Karten nur erste Variante, 4 `багато`-Karten mit Pluralform ohne Klammerzusatz. Worklist: `session-notizen/2026-09-24_13-technologie_audio-worklist.jsonl`.

### `14 - Herbst`
- Seit 04.10.2026 per PDF-Import (`UA-Tandem_0710206_Herbst.pdf`), direkt im Normformat erstellt; 66 Notizen. Die PDF-Diskussionsfragen wurden nicht importiert.
- Bewusste sammlungsweite Duplikate (Nutzer-Entscheidung): `wandern` → `03 - Sport`, `der Feiertag` → `01 - Beruf`, `die Tradition` → Legacy-Zwilling in `08`.
- 06.10.2026 erweitert: 6 neue Karten; ` <i>oder</i> `-Zweitvarianten bei 5 Synonym-Karten; Zwei-Paar-`Example` für `die Gemütlichkeit / die Behaglichkeit` (das beim Merge nicht übernommene PDF-`Behaglichkeit`-Beispiel nachgetragen); 6 Aspektpaar-Karten mit Markern.
- Audio vollständig seit 06.10.2026: 73 Dateien für 66 Karten — 7 Zwei-Paar-Karten × 2 Dateien (`_bsp2`; davon 6 Aspektpaar-Karten, Audio nur der UKR-Satz ohne den DE-Marker), 5 ` <i>oder</i> `-Variantenkarten nur erste Variante. Worklist: `session-notizen/2026-10-06_14-herbst_audio-worklist.jsonl`.

## Altbestand & Transformationen (Historie)

- Verbleibende Legacy-Vorkommen: `Basic++` in `08`, `Basic+++` in `09` (Anatomie & Rezept: Regeldatei §1.7/§1.8).
- Die notizleeren Altbestand-Notiztypen `Tandem Cafe Basic`, `Tandem Cafe Basic+` und `Tandem Cafe Basic++++` wurden am 24.09.2026 manuell über die Anki-GUI gelöscht (kein MCP-Delete-Tool für Notiztypen).
- Abgesicherte Legacy-Infos: `session-notizen/2026-09-16_07-tiere_legacy-grammatik.json`, `session-notizen/2026-09-17_12-literatur_legacy-grammatik.json`, `session-notizen/2026-09-24_13-technologie_legacy-grammatik.json`.

## Offene Punkte

- Transformation `08 - Familie und Generationen` (`Basic++`) und `09 - Wohnen` (`Basic+++`).
- `02 - Ausbildung & Studium`: Audio für 71 Beispielkarten ergänzen (deckweiter TTS-Lauf, Workflow 4.3/§5.2); `04 - Musik & Kunst`: Normierung (UKR-Beispiele, Genus-Marker).
- Level-Tag-Migration: `10`, `11` (Kombi-Restbestand), `04`, Root ohne Tags.
- `або`-Restkarten: `Verantwortung übernehmen` (`10`), `der Gletscher` (`11`) — bei nächster Bearbeitung umstellen.
- Audio-Vollständigkeit prüfen: `01 - Beruf` (frühe Bestückung), `11 - Landschaften` (nicht dokumentiert).
- **Nutzer-Intention Grammatik-Zusätze** („kein Plural", „Eigenname"): ggf. künftig auch in normierten Karten führen. Die konkrete Zuordnung je Begriff müsste **neu erhoben** werden — mit dem Altbestand ist das Legacy-`Grammatik`-Feld als Quelle weg; nur die drei JSON-Sicherungen oben. In diesen Dokumenten werden bewusst **keine** begriffsbezogenen Qualifier gespeichert.
