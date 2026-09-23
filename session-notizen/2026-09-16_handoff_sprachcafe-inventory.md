# Handoff — Inventory `#7 - Sprachcafé` + Normalisierung von `07 - Tiere und Haustiere` und `12 - Literatur`

> **Quell-Sessions:** `01a0a6f6-b470-738c-97ae-7a29b2bffbda` (15.–16.09.2026) · weitere Session 17.09.2026 (`12 - Literatur`)
> **Dokumentstand:** **20.09.2026** — §1/§2 historischer Stand, §3 = Updates 17.09., §4 = **frischer Read-only-Rescan vom 20.09.2026** (alle Zahlen in §4/§5 live erhoben, nichts dabei verändert)
> **Skill:** `anki-card-pipeline` · **Notiztyp (normed):** `Basic (with reversed card and example sentences)` — 2 Karten pro Notiz (Normal + Umgekehrt)

---

## 1. Inventory (erhoben 15.–16.09.2026, read-only — historischer Snapshot, überholt durch §4)

**Scope:** `#7 - Sprachcafé` mit den 9 damaligen Subdecks plus Root-Deck. **Damals: 792 Notizen / 1178 Karten.**

| Deck | Notes | Note type | UKR example | Audio | Level tags | `NoExample` | `BadTranslation` |
|---|---|---|---|---|---|---|---|
| 01 - Beruf | 68 | normed | 67/68 | 62/68 | 60/68 (8 untagged) | 1 | 6 |
| 02 - Ausbildung & Studium | 71 | normed | 1/71 | 1/71 | alle, aber 21 non-standard (`A1`,`A2`,`A2/B1`,`B2/C1`) | 0 | 0 |
| 03 - Sport | 68 | normed | 0/68 (DE only) | 0 | 39 std, 29 non-standard (u. a. Literal-Tag `Niveau`) | 0 | 0 |
| 04 - Musik & Kunst | 70 | normed | 0/70 (DE only) | 0 | **0 — keine Tags** | 0 | 0 |
| 07 - Tiere und Haustiere | 130 = 65 Begriffspaare | **legacy `Tandem Cafe Basic+`** | 65 UKR / 65 DE (Twin-Notes) | 0 | keine (Level im `Niveau`-Feld) | 0 | 0 |
| 08 - Familie und Generationen | 136 = 68 Paare | **legacy `Tandem Cafe Basic++`** | 68 UKR / 68 DE | 0 | keine | 0 | 0 |
| 09 - Wohnen | 140 = 70 Paare | **legacy `Tandem Cafe Basic+++`** | 70 UKR / 70 DE | 0 | keine | 0 | 0 |
| 10 - Kindheit | 56 | normed | 56/56 ✅ | 56/56 ✅ | alle ✅ | 0 | 0 |
| 11 - Landschaften | 31 | normed | 31/31 ✅ | 31/31 ✅ | alle ✅ | 0 | 0 |
| **Root-Deck (direkt)** | **22** | normed | 1/22 | 0 | **0 — alle untagged** | – | – |

### Notable findings (Stand Inventory)

1. **22 stray notes direkt im Root-Deck** (UKR Front → DE Back, z. B. *прикол*, *пропонува́ти*, *Червона шапочка*), untagged, fast ohne Beispiele → die 44 Root-Level-Karten.
2. **Junk-Platzhalter in 03 - Sport**: `Front="Front"`, `Back="Back"`, `Example="Beispielsatz"`, Tag `Niveau` → Löschkandidat. *(seitdem erledigt, s. §2.1)*
3. **Doc-Divergenz**: Doc behauptete, 02/07/08/09 hätten komplett keine Beispielsätze — real hatte **jede** Note in 07/08/09 einen einsprachigen `Beispielsatz` (UKR + DE als Twin-Notes), 02 sogar 1 UKR-Beispiel + Audio. Doc erwähnte `Basic+`/`Basic+++` nicht. *(seitdem korrigiert, s. §2.5)*
4. **Non-standard Level-Tags**: 02 (`A1`,`A2`,`A2/B1`,`B2/C1`), 03 (separate `A1`/`A2` + Literal-Tag `Niveau`), 04 und alle drei Legacy-Decks ganz ohne Tags. *(Einordnung §4.2: die Kombi-Tags in 01/10/11 sind das ursprüngliche Nutzerschema und wurden im Handoff-Stand 16.09. nicht als „non-standard" geführt.)*
5. **Audio-Lücken**: 01 - Beruf fehlen 6/68; alle normierten Decks ohne Audio außer 10 und 11.

---

## 2. Updates nach der Normalisierung von `07 - Tiere und Haustiere` (16.09.2026)

### 2.1 Junk-Karte in 03 - Sport gelöscht
- Note `1784668521886` (2 Karten) permanent gelöscht, 0 Platzhalter verbleibend. **03 - Sport jetzt 67 Notizen.**

### 2.2 Phase 2 — Normalisierung `07 - Tiere und Haustiere` ✅
- **Analyse:** 130 Legacy-Notes (`Tandem Cafe Basic+`, nur in diesem Deck) = exakt 65 saubere DE↔UKR-Twin-Paare, kein Orphan.
- **Mapping:** Front ← DE-Twin ohne Plural-Suffix (semantische Klammern behalten) · Back ← UKR-Twin, Marker lateinisch ans Ende (`(ж.)`→`(f)`, `кіт / кішка` → `(m/f)`, `(мн.)`→`(pl)`) · Example ← UKR-Satz + `<br><br>` + DE-Satz.
- **Tag-Norm (neue userspezifische Norm, im Doc §1.4 festgehalten):** **genau ein** Level-Tag pro Note, nur `A1`/`A2`/`B1`/`B2`/`C1`/`C2`; nicht konforme Werte werden beim Anfassen pro Karte abgeleitet. Ergebnis: `A1`×6, `A2`×16, `B1`×30, `B2`×13 · zusätzlich `Redewendung`×3 (`Gassi gehen`, `artgemäß halten`, `die Gesellschaft leisten`).
- **Ergebnis (verifiziert):** 65/65 normierte Notes erstellt (Read-back-Diff: 0 Feldabweichungen, 65/65 mit exakt 2 Karten = 130 Karten). 35 „Duplicates" kollidierten nur mit den eigenen Legacy-Twins (Cross-Type-Dupe-Check!) → mit `allow_duplicate` erstellt, Kollision nach Löschung behoben.
- **Legacy gelöscht:** 130/130 (Batches 100+30, je Dry-Run), **0 verbleibend collection-weit**. Legacy-`Grammatik`-Infos vorher gesichert: `session-notizen/2026-09-16_07-tiere_legacy-grammatik.json`.
- **⚠️ Manueller Rest:** Note type `Tandem Cafe Basic+` hat 0 Notes mehr, aber der MCP-Server kann Note types nicht löschen → optional manuell: *Anki → Tools → Manage Note Types → `Tandem Cafe Basic+` → Delete* (harmlos, gleicher Status wie `Basic++++`).

### 2.3 Phase 3 — Quality-Check `07` ✅
- **Green:** Struktur 65/65 (UKR vor erstem `<br>`, DE danach, Endpunkte), Geschlechtsmarker alle gegen tatsächliche UKR-Genera verifiziert, Tags 65/65 genau ein Level-Tag (+ `Redewendung`×3), в/у-Euphonie ohne Befund.
- **5 Content-Fixes angewendet & per Read-back verifiziert:**
  1. `die Fürsorgepflicht` — Komma-Germanismus entfernt („Як власник ти маєш…")
  2. `die Tierversicherung` — fehlendes Prädikat ergänzt (…abschließen)
  3. `die Notunterkunft (für Tiere)` — Pleonasmus behoben: „…тимчасовий притулок" / „kurzfristige Notunterkunft"
  4. `erziehen (ein Tier)` — Beispiel neu: „Щоб правильно виховати молодого собаку, потрібне терпіння."
  5. `der Tierschutzverein` — „**безпритульних** котів і собак" / „**herrenlose** Katzen und Hunde" (Users-Wortwahl)
- **Konventionen geklärt & im Doc §1.2 verankert:**
  - **Beispielsatz-Regel:** der Front-Begriff steht im DE-Satz, seine Back-Übersetzung im UKR-Satz.
  - **Synonym-Varianten:** bei Synonymen im Back wird **ein vollständiger zweiter UKR-Satz** gebildet und per ` <i>oder</i> ` angehängt, danach der eine gemeinsame DE-Satz (Muster `Verantwortung übernehmen`). Auf 4 Karten angewendet: `adoptieren`, `impfen`, `kastrieren`, `erziehen (ein Tier)`. Gender-Paare wie `кіт / кішка (m/f)` bleiben bei ` / `.
  - Optional-Polish (die Katze, das Fell, die Anschaffung, Freigänger/Katzenklappe, erziehen-Komma) wurde auf Users-Anweisung **verworfen** — nicht geändert.

### 2.4 Phase 5 — Audio `07` ✅
- Worklist aus Live-Daten (65 Zeilen, bei den 4 `oder`-Karten nur die erste Variante): `session-notizen/2026-09-16_07-tiere_audio-worklist.jsonl`
- TTS Cartesia (Stimme „Oleh"): **65/65 OK, 0 Fehler** · `store_media_file` 65/65 · Feld-Update (Dry-Run clean → ausgeführt): **65/65 Notes mit `[sound:]`-Präfix verifiziert.**

### 2.5 Doc-Updates (`Anki-MCP-VerwendungUndAufbau.md`, Stand 16.09.2026)
- **§1.4 neu:** Eine-Level-Tag-Norm (s. o.), Migration der Bestandsdecks geplant, noch nicht ausgeführt.
- **§1.1 korrigiert:** 07 jetzt normed; Falschbehauptung entfernt, 08/09 hätten keine Beispiele (sie haben einsprachige pro Twin-Note).
- **§1.2:** Legacy-Familie `Basic+`/`++`/`+++` dokumentiert + erprobtes Transform-Rezept inkl. Cross-Type-Duplicate-Check-Falle · Beispielsatz-Regel · Synonym-Varianten-Muster.
- **§1.3:** 07 als vollständig audio-abgedeckt eingetragen (neben 10 - Kindheit).

---

## 3. Updates der Session 17.09.2026 — Normalisierung `12 - Literatur` ✅

*(laut Doc-Updates vom 17.09. + Session-Artefakten; alle Zahlen durch den Rescan 20.09. verifiziert)*

- **Phase 2 — Transform:** `12 - Literatur` stand komplett auf schlichtem `Tandem Cafe Basic` (Zwillingsnotizen mit **sprachspezifischer** `Grammatik`: DE-Notiz deutsches Genus mit Zusätzen wie „kein Plural", „Eigenname", „Feste Wendung"; UKR-Notiz der ukrainische рід; Marker kyrillisch `(м.)/(ж.)/(ч.)/(с.)`; keine Tags, Niveau nur im Feld). **29 normierte Notes erstellt, 58 Alt-Notizen gelöscht**, `Tandem Cafe Basic` damit collection-weit bei 0 Notes (Rescan-verifiziert). Legacy-`Grammatik` gesichert: `session-notizen/2026-09-17_12-literatur_legacy-grammatik.json`.
- **Duplikat-Entscheidung des Nutzers:** die leere normierte Alt-Notiz `die Bibliothek` wurde gelöscht; `12 - Literatur` führt den Begriff mit Beispielsatz. *(Rescan 20.09.: `die Bibliothek` existiert genau 1× collection-weit, normiert, mit Beispiel; `07` weiter bei 65 Notes, keine leeren Examples.)*
- **Phase 5 — Audio:** **29/29 Notes** mit `[sound:]`-Präfix verifiziert (Rescan bestätigt). Die Aspektpaar-Karte `sich in ein Buch vertiefen` trägt zwei Dateien, eines je Satzpaar. Worklist: `session-notizen/2026-09-17_12-literatur_audio-worklist.jsonl`.
- **Tags:** 29/29 mit **genau einem** normkonformen Level-Tag (`A1`×1, `A2`×8, `B1`×13, `B2`×7).
- **Doc-Updates 17.09.:** §1.1 (12 normiert), §1.2 (`Tandem Cafe Basic` dokumentiert + Duplikat-Entscheidung), §1.3 (Dateinamen-Konvention ab 17.09. durchgehend klein; 12 audio-vollständig), §1.4 (Kombiwerte-Bestand eingeordnet).
- *(Nachtrag 20.09.: die in §1.3 bis heute gegenteilige Bemerkung „12 noch ohne Beispiel-Audio" war ein vergessener Reststand — Rescan widerspricht ihr; im Doc entfernt. Ebenso die 03-Betreffende Stelle in §1.4, s. §4.2.)*

---

## 4. Deck-Status NUN — Rescan 20.09.2026 (read-only, frisch erhoben)

**Gesamt: 754 Notizen / 1232 Karten** (ggü. 16.09.-Stand 726/1176: +29 `12 - Literatur`, −1 Note in `02` ⚠️ siehe §4.2; Karten −2 Junk, −130+−58 Legacy, +65+29 normiert).

| Deck | Notes | Karten | Format | UKR example | Audio | Level tags |
|---|---|---|---|---|---|---|
| 01 - Beruf | 68 | 136 | normed | 67/68 | 62/68 ⚠️ 6 fehlen | **✅ genau ein Level-Tag** (`A1`×13, `A2`×6, `B1`×19, `B2`×10, `C1`×20) · `Redewendung`×8 · `NoExample`×1, `BadTranslation`×6 *(Einzelnorm seit 20.09.2026, s. §4.3)* |
| 02 - Ausbildung & Studium | **70 ⚠️** | 140 | normed | 1/70 | 1/70 | 42 normkonform (`A1`×1, `A2`×3, `B1`×19, `B2`×13, `C1`×6) + 28 Kombi (`A1/A2`×3, `A2/B1`×8, `B1/B2`×9, `B2/C1`×8) |
| 03 - Sport | 67 | 134 | normed | 0/67 (DE only) | 0 | **✅ 67/67 normkonform** (`A1`×9, `A2`×19, `B1`×30, `B2`×9) — Literal-Tag `Niveau` entfernt, Migration vollzogen |
| 04 - Musik & Kunst | 70 | 140 | normed | 0/70 (DE only) | 0 | **0 — keine Tags** |
| 07 - Tiere und Haustiere | 65 | 130 | normed ✅ | 65/65 ✅ | 65/65 ✅ | ✅ genau ein Level-Tag (`A1`×6, `A2`×16, `B1`×30, `B2`×13) + `Redewendung`×3 |
| 08 - Familie und Generationen | 136 | 136 | legacy `Basic++` | 68 (Zwillings-`Beispielsatz`) | 0 | keine |
| 09 - Wohnen | 140 | 140 | legacy `Basic+++` | 70 (Zwillings-`Beispielsatz`) | 0 | keine |
| 10 - Kindheit | 56 | 112 | normed | 56/56 ✅ | 56/56 ✅ | Nutzerschema: `A1/A2`×17, `B1`×15, `B1/B2`×9, `C1`×15 (26 Kombi) + `Redewendung`×3 |
| 11 - Landschaften | 31 | 62 | normed | 31/31 ✅ | 31/31 ✅ | Nutzerschema: `A1/A2`×11, `B1`×11, `B2`×9 (11 Kombi) |
| **12 - Literatur** | **29** | **58** | **normed ✅** | **29/29 ✅** | **29/29 ✅** | **✅ genau ein Level-Tag** (`A1`×1, `A2`×8, `B1`×13, `B2`×7) |
| Root-Deck (direkt) | 22 | 44 | normed | 1/22 | 0 | keine; 21/22 ohne Example |

### 4.1 Integrität (Rescan)

- **478 normierte Notes, ausnahmslos exakt 2 Karten** ✅ (Normal + Umgekehrt). Legacy-Twins (08/09): 1 Karte/Note ✅.
- Note types **`Tandem Cafe Basic`, `Basic+`, `Basic++++`: je 0 Notes collection-weit** (nur noch manuell per GUI löschbar); aktiv bleiben nur `Basic++` (08) und `Basic+++` (09).

### 4.2 Abweichungen des Rescans gegen den Handoff-Stand 16.09.

1. **`02 - Ausbildung & Studium`: 71 → 70 Notes** — eine Note wurde irgendwann zwischen 16.09. und 20.09. gelöscht (nicht dokumentiert; Begriff unbekannt). ⚠️ Zur Klärung mit dem Nutzer: bekannt/beabsichtigt?
2. **`03 - Sport` vollständig auf Einzelnorm migriert**: war 39 std + 29 non-standard (u. a. `Niveau`) → jetzt 67/67 einzelne, normkonforme Level-Tags ohne `Niveau`. Im Handoff nicht dokumentiert; Doc §1.4 (Stand 17.09.) führte 03 noch als nicht migriert → dort nachgetragen (20.09.).
3. **`01 - Beruf`**: die ehemals 8 untagged Notes tragen `Redewendung`. Die 60 Level-Tags waren das ursprüngliche **Nutzerschema mit Kombiwerten** (`A1/A2`, `B1/B2`, `C1`) — unter der Eine-Level-Norm von 16.09. nicht normkonform, war im Handoff-Stand 16.09. so nicht ausgewiesen. Gleiches Muster in `10` (26 Kombi) und `11` (11 Kombi). **→ `01` wurde am 20.09.2026 auf die Einzelnorm migriert, s. §4.3.**
4. **Kleinigkeit Root-Deck:** eine Stray-Note hat ein leeres `<i></i>` am Front-Anfang (`<i></i>відві́дувати`) — Formatierungsrest.
5. Sonst unverändert gegenüber 16.09.: `04`, `08`, `09`, Root (22 Strays, 1 UKR-Beispiel), `01`-Audio-Lücke (6), `NoExample`=`die Fluktuation`, `BadTranslation`×6.

### 4.3 Nachtrag 20.09.2026 — Migration `01 - Beruf` auf die Einzelnorm ✅

- **46 Notes per `tag_management`/`batch_tags`** (6 Operationen, Pre-Check gegen Live-Stand, danach Read-back-Verifikation 68/68):
  - `A1/A2`×19 → `A1`×13 (`der Beruf`, `die Arbeit`, `der Chef/die Chefin`, `der Kollege/die Kollegin`, `das Büro`, `die Firma`, `der Termin`, `die Pause`, `der Urlaub`, `die Aufgabe`, `der Computer`, `das Team`, `der Feiertag`) · `A2`×6 (`der Lohn`, `das Gehalt`, `der Feierabend`, `das Vorstellungsgespräch`, `der Arbeitsplatz`, `die Schicht`)
  - `B1/B2`×19 → `B1`×13 (`die Karriere`, `die Beförderung`, `die Kündigung`, `die Weiterbildung`, `die Teilzeit`, `die Vollzeit`, `das Homeoffice`, `die Work-Life-Balance`, `die Verantwortung`, `die Zusammenarbeit`, `die Gehaltserhöhung`, `das Feedbackgespräch`, `die Flexibilität`) · `B2`×6 (`der Arbeitsvertrag`, `der Arbeitsdruck`, `die Führungskraft`, `der Betriebsrat`, `das Networking`, `die Selbstständigkeit`)
  - 8 `Redewendung`-Notes ohne Level → `B1`×4 (`den Nagel auf den Kopf treffen`, `ins kalte Wasser springen`, `Land in Sicht`, `am Ball bleiben`) · `B2`×4 (`die Ärmel hochkrempeln`, `ein Rädchen im Getriebe sein`, `auf dem Holzweg sein`, `sich ins Zeug legen`)
- **Ergebnis (verifiziert):** `A1`×13, `A2`×6, `B1`×19, `B2`×10, `C1`×20 = 68/68 mit genau einem Level-Tag; 0 Kombiwerte; `Redewendung`×8, `BadTranslation`×6, `NoExample`×1 unverändert. Nur Tags geändert — keine Notizen/Karten/Felder/Measurement-Daten angefasst.

---

## 5. Offene Punkte / nächste Schritte

1. **⚠️ Manueller AnkiWeb-Sync** — zwingend: durch 16.09. **und** 17.09. wurden Notizen gelöscht/erstellt/geändert und **94 neue Media-Dateien** (65 × `07`, 29 × `12`) erzeugt; Media-Sync in Anki nötig. *(Niemals selbst synchronisieren — Nutzer löst aus.)*
2. **Phase 2 für `08 - Familie und Generationen` und `09 - Wohnen`** — gleiches Rezept, im Doc §1.2 dokumentiert (inkl. Cross-Type-Dupe-Falle). Letzte beiden Legacy-Decks (`Basic++`/`Basic+++`).
3. **Audio `01 - Beruf`** — 6 fehlende.
4. **Level-Tag-Migration Restbestände** (Einzelnorm, Doc §1.4): `02` (28 Kombi), `10` (26 Kombi), `11` (11 Kombi), `04` (gar keine Tags), Root (gar keine). **`01` ✅ und `03` ✅ erledigt**, `07`/`12` ✅.
5. **04 - Musik & Kunst** — keine Tags, 0 UKR-Beispiele, 0 Audio (Phase 3/4/5-Kandidat).
6. **22 Root-Stray-Notes** — untagged, 21 ohne Example, einsortieren oder verwerfen (Entscheidung offen).
7. **Manuell (GUI):** Note types `Tandem Cafe Basic`, `Tandem Cafe Basic+`, `Tandem Cafe Basic++++` löschen (je 0 Notes).
8. **Klären:** gelöschte Note in `02` (71 → 70, s. §4.2.1).

## 6. Session-Artefakte

- `session-notizen/2026-09-16_07-tiere_legacy-grammatik.json` — Legacy-`Grammatik`-Dump der 130 gelöschten Notes (kein Plural ×16, feste Wendungen, Umgangssprache, Etymologien, Hundesteuer-Note)
- `session-notizen/2026-09-16_07-tiere_audio-worklist.jsonl` — Audio-Worklist `07` (65 Zeilen, id + Dateiname + UKR-Satz)
- `session-notizen/2026-09-17_12-literatur_legacy-grammatik.json` — sprachspezifische Legacy-`Grammatik` der 58 gelöschten `12`-Zwillingsnotizen (deutsches Genus + Zusätze wie „kein Plural", „Eigenname"; ukrainischer рід)
- `session-notizen/2026-09-17_12-literatur_audio-worklist.jsonl` + `…-worklist-source.json` — Audio-Worklist `12` (29 Notes)
