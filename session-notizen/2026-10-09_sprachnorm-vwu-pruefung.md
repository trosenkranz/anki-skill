# QS-Prüfung Sprachnorm в/у (§ 23) — vollständig durchgelaufene Decks

> **Datum:** 09.10.2026 · **Art:** Read-only-Audit (keine Daten geändert) · **Anlass:** Neufixierung der Sprachnorm в/у in `Anki-MCP-Verwendung.md` §1.9 (Правопис 2019 § 23) am selben Tag; Prüfung der bereits fertigen Decks gegen die neue Norm.
>
> **Scope:** 8 Decks (`02, 03, 04, 07, 10, 12, 13, 14`) — 471 Notizen, 494 UKR-Sätze (inkl. aller `oder`-/Zwei-Paar-Varianten), 192 eigenständige в/у-Präpositionsverwendungen. `15 - Ernährung und Soulfood` auf ausdrückliche Nutzeraussage übersprungen (Phase-3-Sweep 09.10.2026 inkl. в/у mit §-23-korrigiertem Rollback gilt als geprüft). `01`/`11` (Audio-Status ungeprüft) und Legacy `08`/`09` nicht im Scope.
>
> **Methode:** Example-Felder live extrahiert (MCP + verifizierter Read-only-DB-Zugriff, identische Werte), UKR-Sätze nach Parse-Regel §5.3 getrennt; 9 Fresh-Context-Subagenten prüften je ein Deck gegen § 23 (inkl. Amtstext slovnyk.ua); alle gemeldeten Treffer per MCP-Read-back gegen Live-Daten verifiziert. Falle „в nach Vokal" (§7.14) explizit als Nicht-Befund kontrolliert.

## Befunde — klare Verstöße (5)

| # | Deck | Note | Front | Fundstelle | Normgerecht |
|---|---|---|---|---|---|
| 1 | `03 - Sport` | 1784668521981 | die Umkleidekabine | „…зустрічаються **у** роздягальні." (−я → р) | „…зустрічаються **в** роздягальні." |
| 2 | `03 - Sport` | 1784668522003 | die Mitgliedschaft | „Членство **у** спортивному клубі…" (−о → с) | „Членство **в** спортивному клубі…" |
| 3 | `10 - Kindheit` | 1789335249962 | die Schultüte | „В Німеччині **у** перший день…" (−і → п) | „В Німеччині **в** перший день…" |
| 4 | `14 - Herbst` | 1791151233287 | das Halloween | „…переодягаються **у** костюми…" (−я → к) | „…переодягаються **в** костюми…" |
| 5 | `14 - Herbst` | 1791241223103 | der Regenmantel | „**У** осінній дощ…" (Satzanfang + Vokal о) | „**В** осінній дощ…" (§23.2.2) |

⚠️ Alle 5 Karten haben Beispielsatz-Audio → Fix je Karte = Feld-Update + Re-TTS (Workflow §4.3/§5.1).

## Befunde — grenzwertig nach Buchstabenregel (2, Nutzerentscheid)

| # | Deck | Note | Front | Fundstelle | Anmerkung |
|---|---|---|---|---|---|
| 6 | `13 - Technologie` | 1790279669060 | das E-Government | „лідером **у** Європі" (Konsonant м → Є) | §1.9-Buchstabenregel: „в Європі"; aber Є/я/ю/ї haben [j]-Anlaut → „у" davor mid-sentence verbreitet; Правопис regelt „у" vor я/є/ю/ї nur für Satzanfang (§23.1.3) |
| 7 | `07 - Tiere und Haustiere` | 1789509975838 | der Heimtiermarkt | „…тварин **у** Європі." (Konsonant н → Є) | identischer Musterfall wie #6 |

## Entkräftete Review-Meldungen (normkonform, keine Aktion)

- `02`: „Яке **в** тебе…", „Завтра **в** мене…" — в nach Vokal vor einfachem Konsonanten ✓ (dokumentierte Falle)
- `04`: „грає **в** джазовому гурті" — дж nicht in der Cluster-Liste (льв/зв/св/дв/тв/гв/хв) ✓
- `12`: „розгортається **в** XIX столітті" — в nach Vokal ✓

## Nebenfund (außerhalb в/у-Scope)

- `03 - Sport`, 1784668521922 (`die Yoga`): „займається **егою**" — mutmaßlich Tippfehler, gemeint **„йогою"** (Instrumental von йога). Karte hat Audio.

## Statistik

| Deck | Notizen | Sätze | в/у-Verwendungen | Verstöße | Grenzfälle |
|---|---|---|---|---|---|
| 02 - Ausbildung & Studium | 72 | 74 | 47 | 0 | 0 |
| 03 - Sport | 67 | 69 | 27 | 2 | 0 |
| 04 - Musik & Kunst | 71 | 74 | 28 | 0 | 0 |
| 07 - Tiere und Haustiere | 65 | 65 | 23 | 0 | 1 |
| 10 - Kindheit | 56 | 58 | 19 | 1 | 0 |
| 12 - Literatur | 29 | 30 | 10 | 0 | 0 |
| 13 - Technologie | 45 | 51 | 13 | 0 | 1 |
| 14 - Herbst | 66 | 73 | 25 | 2 | 0 |
| **Σ** | **471** | **494** | **192** | **5** | **2** |

Normkonformität: 185/192 Verwendungen (≈ 96 %); Fehlkorrektur-Falle („в" nach Vokal) **0 falsche Fixes** in allen Decks.

## Offene Punkte — Status (Nachtrag 09.10.2026)

1. ✅ Die 5 klaren Fixes umgesetzt (Dry-Run → Execute → Voll-Read-back ok) + Audio unter **Wiederverwendung der bestehenden Dateinamen** neu generiert (`mp3/` + `collection.media`, MD5-Gegenprobe ok) — Nutzerentscheid: `[sound:]`-Tags bleiben unverändert.
2. ✅/ℹ️ Die 2 „у Європі“-Grenzfälle bleiben **bewusst unverändert** (Nutzerentscheid 09.10.2026; **keine permanente Regel** in §1.9). ⚠️ Künftige в/у-Sweeps dürfen diese beiden Karten nicht automatisch „korrigieren“: `07` 1789509975838 (`der Heimtiermarkt`, „тварин у Європі“) und `13` 1790279669060 (`das E-Government`, „лідером у Європі“).
3. ✅ Tippfehler-Fix „йогою“ (`03`, `die Yoga`, 1784668521922) umgesetzt + Audio neu generiert (gleicher Dateiname).
