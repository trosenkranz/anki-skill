# Anki-Datenbankstand

> **Stand:** 02.11.2026
>
> **Pflege:** Nach jeder datenändernden Session aktualisieren (betroffene Deck-Blöcke, Zähler, Coverage, offene Punkte) und diesen Kopf datieren — Regeln: `Anki-MCP-Verwendung.md` §8. **Nur lesen, wenn Bestandsinformationen gebraucht werden** (Status-/Coverage-/Historie-Anfragen, deckweite Aktionen). Die lebenden Anki-Daten sind immer die Autorität; kein Changelog. Konventionen liegen nicht hier, sondern in der Regeldatei. — Nachfolgerin des früheren `Anki-MCP-VerwendungUndAufbau.md` (s. „Vorgeschichte“ im Kopf der Regeldatei).

## Deck-Übersicht `#7 - Sprachcafé`

Decks: `01 - Beruf`, `02 - Ausbildung & Studium`, `03 - Sport`, `04 - Musik & Kunst`, `07 - Tiere und Haustiere`, `08 - Familie und Generationen`, `09 - Wohnen`, `10 - Kindheit`, `11 - Landschaften`, `12 - Literatur`, `13 - Technologie`, `14 - Herbst`, `15 - Ernährung und Soulfood`, `16 - Feste und Bräuche` (Trenner `::`, numerische Präfixe sortieren).

**✅ fertig** = normiert, Einzel-Tags, UKR-Beispiele + Audio vollständig, Deck vollständig durch die Pipeline (Zähler, Tag-Verteilung, Audio-Coverage per Live-Query nachprüfbar; hier nur noch Abweichungen).

| Deck | Format | Level-Tags | Beispiel-Audio | Offen |
|---|---|---|---|---|
| `01 - Beruf` | normiert | ✅ migriert | vorhanden, Vollständigkeit **ungeprüft** | Audio-Check |
| `02 - Ausbildung & Studium` | ✅ fertig | ✅ | ✅ | — |
| `03 - Sport` | ✅ fertig | ✅ | ✅ | — |
| `04 - Musik & Kunst` | ✅ fertig | ✅ | ✅ | — |
| `07 - Tiere und Haustiere` | ✅ fertig | ✅ | ✅ | — |
| `08 - Familie und Generationen` | ❌ Legacy (`Tandem Cafe Basic++`) | Altbestand | — | Transformation |
| `09 - Wohnen` | ❌ Legacy (`Tandem Cafe Basic+++`) | Altbestand | — | Transformation |
| `10 - Kindheit` | normiert | ⚠️ Kombi-Restbestand | ✅ | 1 × `або`-Trenner |
| `11 - Landschaften` | normiert | ⚠️ Kombi-Restbestand | ✅ | 1 × `або`-Trenner |
| `12 - Literatur` | ✅ fertig | ✅ | ✅ | — |
| `13 - Technologie` | ✅ fertig | ✅ | ✅ | — |
| `14 - Herbst` | ✅ fertig | ✅ | ✅ | bewusste Duplikate (s. u.) |
| `15 - Ernährung und Soulfood` | ✅ fertig | ✅ | ✅ | — |
| `16 - Feste und Bräuche` | ✅ fertig | ✅ | ✅ | optional: Notiztyp-Löschung |

## Deck-Details

Nur Abweichungen von der Norm und bewusste Nutzerentscheidungen; alles Übrige steht in Anki bzw. ist per Live-Query rekonstruierbar.

### `01 - Beruf`
- Audio: in einer frühen Session bestückt, **Vollständigkeit nie verifiziert** → vor Audio-Arbeit Live-Check (`hasSound`).

### `02 - Ausbildung & Studium`
- ✅ Fertig (Abschluss 06.10.2026).
- Alter Back der umgebauten Karte `ablegen (eine Prüfung)` gesichert: `session-notizen/2026-10-06_02-ablegen-alt-back.md`.

### `03 - Sport`
- ✅ Fertig (26.09.2026).

### `04 - Musik & Kunst`
- ✅ Fertig (08.10.2026; in-place-Transformation — Notiztyp war bereits etabliert, keine Legacy-Zwillinge, daher keine Grammatik-Sicherung).

### `07 - Tiere und Haustiere`
- ✅ Fertig (16.09.2026). Legacy-`Grammatik` gesichert: `session-notizen/2026-09-16_07-tiere_legacy-grammatik.json`.
- ⚠️ `der Heimtiermarkt` „…тварин **у** Європі.“ bewusst so gelassen (Nutzerentscheid 09.10.2026: [j]-Anlaut von Є; keine Regel in §1.9) — künftige в/у-Sweeps dürfen nicht „korrigieren“.

### `08 - Familie und Generationen`
- Legacy-Zwillinge `Tandem Cafe Basic++`: je Begriff 2 Notizen (je Richtung eine, je 1 Karte), `Beispielsatz` einsprachig pro Zwillingsnotiz.
- Enthält den von `14` bewusst geduldeten sammlungsweiten Duplikat-Zwilling `die Tradition`.

### `09 - Wohnen`
- Legacy-Zwillinge `Tandem Cafe Basic+++` (gleiche Anatomie wie `08`).

### `10 - Kindheit`
- Normiert; Tags: Kombi-Restbestand — Ableitung bei Kartenbearbeitung.
- ⚠️ `Verantwortung übernehmen` noch mit Legacy-Trenner ` <i>або</i> ` (Umstellung bei nächster Bearbeitung).

### `11 - Landschaften`
- Normiert; Tags: Kombi-Restbestand — Ableitung bei Kartenbearbeitung.
- ⚠️ `der Gletscher` noch mit ` <i>або</i> `-Trenner (Umstellung bei nächster Bearbeitung).
- з/із-Audit 25.10.2026: 0 Verletzungen; 1 UNCERTAIN (`die annektierte Halbinsel`, Ziffern-Jahr — offene Normfrage §1.10).

### `12 - Literatur`
- ✅ Fertig (17.09.2026). Legacy-`Grammatik` gesichert: `session-notizen/2026-09-17_12-literatur_legacy-grammatik.json`.

### `13 - Technologie`
- ✅ Fertig (24.09.2026). Legacy-`Grammatik` gesichert: `session-notizen/2026-09-24_13-technologie_legacy-grammatik.json`.
- ⚠️ `das E-Government` „…лідером **у** Європі.“ — gleiche bewusste Ausnahme wie `der Heimtiermarkt` in `07`.

### `14 - Herbst`
- ✅ Fertig (PDF-Import 04.10.2026, Abschluss 06.10.2026).
- Bewusste sammlungsweite Duplikate (Nutzer-Entscheidung): `wandern` → `03`, `der Feiertag` → `01`, `die Tradition` → `08` (dort als Legacy-Zwilling).

### `15 - Ernährung und Soulfood`
- ✅ Fertig (PDF-Import 09.10.2026, Pipeline Phase 1–5).

### `16 - Feste und Bräuche`
- ✅ Fertig (Transform 24.10.2026 aus 192 Legacy-Zwillingen `Tandem Cafe Basic`; Audio abgeschlossen 01.11.2026).
- Bewusste Auslagerungen (sammlungsweite Duplikate übersprungen, Nutzerentscheid): `die Tradition`, `das Erntedankfest`, `die Erinnerung`, `Allerheiligen` → `14`; `die Schultüte` → `10`; `das Familienrezept` → `15`.
- Legacy-`Grammatik` gesichert: `session-notizen/2026-10-24_16-feste-und-braeuche_legacy-source.json`. `незм.`-Fälle bewusst ohne Genus-Marker im Back: `олів'є (m)`, `Івана Купала`.
- Optional offen (GUI): leeren Notiztyp `Tandem Cafe Basic` löschen (§6.6).

## Legacy-Restbestand & gesicherte Altbestände

- Verbleibende Legacy-Notiztypen: `Tandem Cafe Basic++` in `08`, `Tandem Cafe Basic+++` in `09` (Anatomie & Rezept: Regeldatei §1.7/§1.8).
- Die notizleeren Altbestand-Notiztypen `Tandem Cafe Basic`, `Tandem Cafe Basic+` und `Tandem Cafe Basic++++` wurden am 24.09.2026 manuell über die Anki-GUI gelöscht; durch den 16-Import existiert `Tandem Cafe Basic` erneut und ist nach der Transformation wieder notizleer (Löschung optional offen, §6.6).
- Abgesicherte Legacy-Infos (bewusst nur hier, nicht in Karten): die vier JSON-Sicherungen der Decks 07, 12, 13 und 16 (Pfade s. Deck-Blöcke).

## Sprachnorm-Audit-Coverage

- в/у (§ 23, 09.10.2026, Report: `session-notizen/2026-10-09_sprachnorm-vwu-pruefung.md`): geprüft `02, 03, 04, 07, 10, 12, 13, 14`; `15`/`16` über die jeweiligen Phase-3-Sweeps abgedeckt. **Nicht geprüft: `01`, `11`** (und Legacy `08`/`09`).
- з/із (§ 25/§1.10, 25.10.2026): Fixes in `01`, `02`, `03`, `14`; `11` geprüft ohne Verstoß (1 UNCERTAIN, s. Deck-Block).

## Offene Punkte

- Transformation `08 - Familie und Generationen` (`Basic++`) und `09 - Wohnen` (`Basic+++`).
- Level-Tag-Migration: `10`, `11` (Kombi-Restbestand), Root außerhalb `#7` ohne Tags.
- `або`-Restkarten: `Verantwortung übernehmen` (`10`), `der Gletscher` (`11`) — bei nächster Bearbeitung umstellen.
- Audio-Vollständigkeit prüfen: `01 - Beruf` (frühe Bestückung, nie verifiziert).
- в/у-§23-Sweep noch offen: `01`, `11` (Legacy `08`/`09` erst nach Transformation).
- Optional (GUI): leeren Notiztyp `Tandem Cafe Basic` löschen (§6.6).
- **Nutzer-Intention Grammatik-Zusätze** („kein Plural", „Eigenname"): ggf. künftig auch in normierten Karten führen. Die konkrete Zuordnung je Begriff müsste **neu erhoben** werden — das Legacy-`Grammatik`-Feld ist als Quelle weg; nur die vier JSON-Sicherungen. In diesen Dokumenten werden bewusst **keine** begriffsbezogenen Qualifier gespeichert.
