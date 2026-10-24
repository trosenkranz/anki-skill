# Anki-Datenbankstand

> **Stand:** 09.10.2026
>
> **Pflege:** Nach jeder datenändernden Session aktualisieren (betroffene Deck-Blöcke, Zähler, Coverage, offene Punkte) und diesen Kopf datieren — Regeln: `Anki-MCP-Verwendung.md` §8. **Nur lesen, wenn Bestandsinformationen gebraucht werden** (Status-/Coverage-/Historie-Anfragen, deckweite Aktionen). Die lebenden Anki-Daten sind immer die Autorität; kein Changelog. Konventionen liegen nicht hier, sondern in der Regeldatei. — Nachfolgerin des früheren `Anki-MCP-VerwendungUndAufbau.md` (s. „Vorgeschichte“ im Kopf der Regeldatei).

## Deck-Übersicht `#7 - Sprachcafé`

Decks: `01 - Beruf`, `02 - Ausbildung & Studium`, `03 - Sport`, `04 - Musik & Kunst`, `07 - Tiere und Haustiere`, `08 - Familie und Generationen`, `09 - Wohnen`, `10 - Kindheit`, `11 - Landschaften`, `12 - Literatur`, `13 - Technologie`, `14 - Herbst`, `15 - Ernährung und Soulfood` (Trenner `::`, numerische Präfixe sortieren).

| Deck | Format | Level-Tags | Beispiel-Audio | Offen |
|---|---|---|---|---|
| `01 - Beruf` | normiert | ✅ migriert | Bestand vorhanden, Vollständigkeit ungeprüft | Audio-Check |
| `02 - Ausbildung & Studium` | normiert | ✅ migriert | ✅ UKR-Beispiele + Audio vollständig seit 06.10.2026 (74 Dateien für 72 Karten) | — |
| `03 - Sport` | normiert | ✅ migriert | ✅ vollständig | — |
| `04 - Musik & Kunst` | normiert | ✅ Einzel-Tags | ✅ vollständig | — |
| `07 - Tiere und Haustiere` | normiert | Einzel-Tags | ✅ vollständig | — |
| `08 - Familie und Generationen` | ❌ Legacy (`Tandem Cafe Basic++`) | Altbestand | — | Transformation |
| `09 - Wohnen` | ❌ Legacy (`Tandem Cafe Basic+++`) | Altbestand | — | Transformation |
| `10 - Kindheit` | normiert | Kombi-Restbestand | ✅ vollständig | Tag-Migration, 1 × `або`-Trenner |
| `11 - Landschaften` | normiert | Kombi-Restbestand | nicht dokumentiert | Tag-Migration, 1 × `або`-Trenner, Audio-Check |
| `12 - Literatur` | normiert | Einzel-Tags | ✅ vollständig | — |
| `13 - Technologie` | normiert | Einzel-Tags | ✅ vollständig | — |
| `14 - Herbst` | normiert | Einzel-Tags | ✅ vollständig | 3 bewusste sammlungsweite Duplikate (s. u.) |
| `15 - Ernährung und Soulfood` | normiert (PDF-Import 09.10.2026) | Einzel-Tags (A1×13, A2×35, B1×54, B2×32) | ✅ vollständig seit 09.10.2026 (143 Dateien für 134 Karten; 9 Zwei-Paar-Karten × 2) | — |

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
- в/у-Audit 09.10.2026 (§ 23, Report: `session-notizen/2026-10-09_sprachnorm-vwu-pruefung.md`): 2 Fixes umgesetzt (Dry-Run → Execute → Voll-Read-back ok) — `die Umkleidekabine` „…зустрічаються в роздягальні.“, `die Mitgliedschaft` „Членство в спортивному клубі…“; dazu Tippfehler-Fix `die Yoga` „займається йогою“ (statt „егою“). Audio je Karte neu generiert (Cartesia/Oleh) unter **Wiederverwendung der bestehenden Dateinamen** (Nutzerentscheid: `[sound:]`-Tags unverändert); Dateien in `mp3/` und `collection.media` ersetzt (MD5-Gegenprobe ok).

### `04 - Musik & Kunst`
- Normiert seit 08.10.2026 (in-place-Transformation — Notiztyp `Basic (with reversed card and example sentences)` war bereits etabliert, keine Legacy-Zwillinge): 70 Notizen. `Front` von Plural-/Paar-Suffixen und Verb-Klammerzusätzen befreit (`das Pysanka (Pl. Pysanky)` → `das Pysanka`; inhaltliche Klammerzusätze bleiben: `die Ausbildung (künstlerisch)`, Back `малювати (олівцем)`); kyrillische Genus-Marker `(ж.)/(ч.)/(с.)` → `(f)/(m)/(n)`; 70 UKR-Beispielsätze ergänzt (`УКР.<br><br>DE.`, DE-Sätze unverändert). Verifikation: Voll-Read-back aller 70 Notizen + Tag-Zählabfragen.
- Genus-Korrektur bei `die Aufführung`: Alt-Back `вистава / виступ (ч.)` — вистава ist feminin → `вистава (f) / виступ (m)`.
- Phase 3 abgeschlossen (08.10.2026): Split `die Aufführung` in 2 Karten — `die Aufführung` → `вистава (f)` (Satz unverändert) + neu `der Auftritt` → `виступ (m)` („Її перший виступ мав великий успіх. / Ihr erster Auftritt war ein großer Erfolg.“); Alt-Notiz gelöscht (Dry-Run → 1 Notiz + 2 Karten). Rechtschreib-Fix `das Volkslied` („В Німеччині“ → „У Німеччині“, Satzanfang + Konsonant). QS-Freigaben: `die Ausstellung` UKR „показує“ statt „представляє“; `die Trachtenkleidung` Back → `народний костюм (m)` (UKR-Satz angepasst); Qualifier `die Note (Musik)`; ` <i>oder</i> `-Zweitvarianten bei `kreativ`/`gestalten`; Zwei-Paar-Examples (ohne (m/f)-Marker, Präzedenz `der/die Auszubildende`) bei `der Musiker / die Musikerin`, `der Künstler / die Künstlerin`, `der Komponist / die Komponistin`. Bestand: **71 Notizen** (A1×6, A2×19, B1×36, B2×10).
- Audio vollständig seit 08.10.2026: 74 Dateien für 71 Karten — 3 Zwei-Paar-Karten × 2 Dateien (`_bsp2`: `der Musiker / die Musikerin`, `der Künstler / die Künstlerin`, `der Komponist / die Komponistin`), 2 ` <i>oder</i> `-Variantenkarten (`kreativ`, `gestalten`) nur erste Variante. Worklist: `session-notizen/2026-10-08_04-musik-kunst_audio-worklist.jsonl` (Builder: `…_build-worklist.py`, Payloads: `…_audio-payloads.json`). Verifikation: `Example:*sound*` = 71/71, Voll-Read-back aller Example-Felder.

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
- в/у-Audit 09.10.2026 (§ 23): 1 Fix umgesetzt (Read-back ok) — `die Schultüte` „В Німеччині в перший день школи…“ (statt „у перший“); Audio neu generiert unter gleichem Dateinamen `dieschultüte_bsp_hq4wzc.mp3` (Nutzerentscheid Wiederverwendung); fehlende lokale Kopie in `mp3/` ergänzt.

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
- в/у-Audit 09.10.2026 (§ 23): 2 Fixes umgesetzt (Read-back ok) — `das Halloween` „…переодягаються в костюми…“, `der Regenmantel` „В осінній дощ…“ (Satzanfang vor Vokal); Audio neu generiert unter gleichen Dateinamen (Nutzerentscheid Wiederverwendung).

### `15 - Ernährung und Soulfood`
- Neu 09.10.2026 per PDF-Import (`UA-Tandem_2026-10-14 - Ernährung_Soulfood.pdf`, „Ukrainische und deutsche Kochtraditionen“), direkt im Normformat erstellt; **134 Notizen** (je 2 Karten; 133 Import + 1 QS-Karte `pikant`). PDF-Diskussionsfragen nicht importiert.
- Nutzerentscheidungen: `der Fisch` (Duplikat in `07`) und `der Apfel` (Duplikat in `14`) **übersprungen**; 6 PDF-interne Duplikate (`das Lorbeerblatt`, `der Kümmel`, `kneten`, `schälen`, `schneiden`, `reiben`) zu je 1 Karte gemerged — 2. Beispiele gesichert in `session-notizen/2026-10-09_15-ernaehrung-import-offenpunkte.md` (Phase 4).
- Genus-Fixes gegenüber PDF: `die Nudel` `локшина (f) / макаронний виріб (m)`, `der Kuchen` `пиріг (f) / торт (m)`, `der Eintopf` `густа страва (f) / рагу в одному горщику (n)`, `die Spezialität` Kopf `страва (f)`; `по- різному` → `по-різному`; Apostrophe normalisiert (`м’ясо`).
- Level-Tags einzeln vergeben: A1×13, A2×35, B1×54, B2×32.
- Verifikation: Deck-Zählabfrage, Tag-Verteilung per Query, Voll-Read-back Batch 1 + Stichproben aller Batches; 2 Übertragungsfehler (`kneten`, `köcheln lassen` — „десять“ im DE-Satz) gefunden, gepatcht, Read-back ok.
- QS-Runde 09.10.2026 (Nutzerfreigabe, umgesetzt + Read-back): `herzhaft` Back → `ситний` (2. Variante entfernt); `überbacken` Back → `запікати під сиром`; `das Pampuschky` → Sg./Pl.-Karte `die Pampuschka / die Pampuschky` mit Back `пампушка (f) / пампушки (pl)` und Zwei-Paar-`Example` (Marker `<i>(Sg.)</i>`/`<i>(Pl.)</i>`); `die Bratwurst` Back + `братвурст (f)`, `der Sauerbraten` Back + `зауербратен (m)` (Beispiele bewusst unverändert — Transliteration im Satz deckungsgleich mit der 2. Back-Variante); `ein Schuss` und `der Eintopf` bewusst so gelassen; `einlegen` bewusst so gelassen (2. Runde) — Disambiguierung über kursive Anmerkung am Example-Ende von `marinieren` („маринувати meint auch ‚einlegen‘…“). Neu: `pikant` → `пікантний` (B1) mit kursiver Anmerkung zur übertragenen Bedeutung.
- `konservieren`: 2. Satzpaar ergänzt (DE-Satz bewusst mit „einlegen“, UKR mit `консервують`) — Karte hat jetzt 2 Satzpaare → Audio später je Paar eine Datei (`_bsp`/`_bsp2`).
- Phase 3 abgeschlossen (09.10.2026): Sweep über alle 134 Karten (в/у, Kalken, Pleonasmen, Genus-Marker, Struktur, Tags). 4 stilistische Befunde auf Nutzerfreigabe umgesetzt (Read-back): `der Knoblauch` „гарного супу“, `die Spezialität` „власні традиційні страви“, `der Kuchen` „кавового столу“, `zerlassen` „на повільному вогні“.
- ⚠️ в/у-Lektion (09.10.2026): Zwei zunächst direkt umgesetzte „Euphonie-Fixe“ (Zucker, schmelzen → „у“) erwiesen sich nach Prüfung des **Український правопис 2019, § 23** als falsch — normgerecht ist **в** nach Vokalbuchstabe vor einfachem Konsonanten (amtliches Bsp. „Пішла в садок“). Beide Karten zurückgesetzt („цукру в тісто“, „масло в каструлі“, Read-back ok); Regel + Bookmarks dauerhaft in der **Regeldatei §1.9** (Deck-unabhängige Norm); Session-Details in `session-notizen/2026-10-09_15-ernaehrung-import-offenpunkte.md`, Abschn. 3c/3d. Faustregel „у nach Vokal“ gilt normativ **nicht** — künftige в/у-Prüfungen nur noch gegen § 23.
- Phase 4 abgeschlossen (09.10.2026, Nutzerfreigabe A+B+C+D1): 6 Merged-Karten mit 2. PDF-Satzpaar (Lorbeerblatt, Kümmel, kneten, schälen, schneiden, reiben); `der Kuchen` Synonym-Muster („шматок пирога. <i>oder</i> шматок торта.“, DE-Satz gemeinsam); `hinzufügen` Aspektpaar §1.5 („<i>(perf.)</i>“ / „<i>(imperf.)</i>“, neuer UKR-Satz „Я додаю сіль у салат.“); `die Nudel` Back → `локшина (f) / макарони (pl)` + Synonym-Muster. Voll-Read-back aller 9 Notizen ok.
- Phase-3-Nachprüfung der Phase-4-Beispiele (09.10.2026): 2 Aspekt-Befunde umgesetzt — `kneten` und `schälen` sind jetzt Aspektpaar-Karten mit §1.5-Markern („<i>(imperf.)</i>“/„<i>(perf.)</i>“); `schälen` zusätzlich очищати-oder-Variante (§1.2; erste Karte mit oder-Muster + Zwei-Paar-Muster kombiniert). Против указанного: в/у (§ 23) и з/із (§ 25) в den neuen Sätzen normkonform („із супу“ korrekt).
- Phase 5 Audio abgeschlossen (09.10.2026): **143/143 TTS OK** (`bin/batch-tts.py`, 0 Fehler), Worklist `session-notizen/2026-10-09_15-ernaehrung_audio-worklist.jsonl`; 143 Dateien per `cp` in `collection.media` (verifiziert); Feld-Updates im Patch-Modus (143/143, lauter Abbruch bei Feldabweichung); Verifikation: `Example:*sound*` = 134/134, `Example:*_bsp2*` = 9, Stichproben ok. ⚠️ Batch-TTS schreibt relativ zum Aufrufverzeichnis (Projekt-Root) — Dateien nachträglich nach `mp3/` verschoben.
- Deck `15` damit vollständig durch die Pipeline (Phase 1–5); keine offenen Punkte mehr.

## Altbestand & Transformationen (Historie)

- Verbleibende Legacy-Vorkommen: `Basic++` in `08`, `Basic+++` in `09` (Anatomie & Rezept: Regeldatei §1.7/§1.8).
- Die notizleeren Altbestand-Notiztypen `Tandem Cafe Basic`, `Tandem Cafe Basic+` und `Tandem Cafe Basic++++` wurden am 24.09.2026 manuell über die Anki-GUI gelöscht (kein MCP-Delete-Tool für Notiztypen).
- Abgesicherte Legacy-Infos: `session-notizen/2026-09-16_07-tiere_legacy-grammatik.json`, `session-notizen/2026-09-17_12-literatur_legacy-grammatik.json`, `session-notizen/2026-09-24_13-technologie_legacy-grammatik.json`.

## Offene Punkte

- Transformation `08 - Familie und Generationen` (`Basic++`) und `09 - Wohnen` (`Basic+++`).
- `02 - Ausbildung & Studium`: Audio für 71 Beispielkarten ergänzen (deckweiter TTS-Lauf, Workflow 4.3/§5.2).
- Level-Tag-Migration: `10`, `11` (Kombi-Restbestand), Root ohne Tags.
- `або`-Restkarten: `Verantwortung übernehmen` (`10`), `der Gletscher` (`11`) — bei nächster Bearbeitung umstellen.
- Audio-Vollständigkeit prüfen: `01 - Beruf` (frühe Bestückung), `11 - Landschaften` (nicht dokumentiert).
- **Nutzer-Intention Grammatik-Zusätze** („kein Plural", „Eigenname"): ggf. künftig auch in normierten Karten führen. Die konkrete Zuordnung je Begriff müsste **neu erhoben** werden — mit dem Altbestand ist das Legacy-`Grammatik`-Feld als Quelle weg; nur die drei JSON-Sicherungen oben. In diesen Dokumenten werden bewusst **keine** begriffsbezogenen Qualifier gespeichert.
