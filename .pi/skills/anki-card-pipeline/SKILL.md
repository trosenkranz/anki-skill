---
name: anki-card-pipeline
description: Generate, normalize, quality-check, extend, and add audio to Ukrainian-learning Anki cards in the #7 - Sprachcafé decks, following the user's established card format. Use when importing vocabulary from a source (PDF, apkg-imported cards, …), converting legacy note types, checking or improving card quality, adding example sentences or tags, generating example audio, or when the user explicitly asks for a deck inventory/status report.
---

# Anki Card Pipeline

A multistep workflow for the Anki collection. The user names the deck and the task;
each phase can be entered individually — a full run is driven phase by phase with the
user deciding between phases, never in one automatic pass.

## Source of truth

`Anki-MCP-VerwendungUndAufbau.md` in the project root defines the established card
layout (note type, fields, gender markers, Example structure, tags), media/audio
naming, MCP tool usage, and known pitfalls.

- Read it at the start of every session, before touching Anki data.
- Keep its details out of this skill. If reality diverges from the doc, stop and
  reconcile with the user, then update the doc (living document, see its §6).

## Safety rules (all phases)

- Work only on decks the user named. A bare deck name means the subdeck of
  `#7 - Sprachcafé`.
- Never sync — the user triggers AnkiWeb sync manually. Remind at the end when data
  or media changed.
- Never force `allow_duplicate: true` without the user's per-case decision
  (duplicate check runs collection-wide).
- **Expectation reconciliation:** only when the user states an expectation (count,
  scope): if the actual numbers deviate, report the discrepancy with reasons and wait
  before acting.
- **Verification for bulk mutations:** `dry_run` where available → execute → verify by
  read-back (counts + spot samples, including reverse-card integrity: notes of the
  established type must yield exactly 2 cards) → only then report done. Single edits:
  read-back as well.

## Phase 1 — Import

Sources: e.g. a PDF worksheet, or vocabulary already in the collection (e.g. imported
from an apkg via AnkiDroid — those usually need Phase 2 next).

1. Extract the vocabulary (PDF: `pdftotext -layout`; skip discussion questions unless
   requested).
2. Match against the target deck (`-tag:BadTranslation`) to find what is genuinely new.
3. Present candidates as a table (Front/Back/Example/Tags) with remarks on the source's
   translation quality; wait for the user's per-item decisions.
4. Create the notes (`add_notes`, established note type, per-note tags); read back a
   sample — long field values are copy-error-prone.

## Phase 2 — Transform (legacy → established format)

For cards in the collection that use a legacy note type (e.g. `Tandem Cafe Basic++`,
`Tandem Cafe Basic++++`): changing the note type in place is not an option — copy to
new notes, delete the old ones.

1. Report how the deck deviates from the established format (note type, fields, gender
   markers, example structure, tags, audio).
2. Propose the mapping into the established format; wait for approval.
3. Create new notes by copying/merging content (legacy-twin duplicates may be intended —
   user decides per case). Verify counts, cards, tags, samples.
4. Capture legacy-only information (e.g. `Grammatik` qualifiers) as session notes —
   never as per-term facts in the doc.
5. Delete legacy notes only after explicit approval: dry-run, `confirmDeletion: true`,
   and check beforehand that the note type is unused elsewhere.

## Phase 3 — Quality check

Collect findings first; apply changes only after the user's decision. Exception: pure
spelling fixes and pure tag work (additions; hygiene removals after a fix) are applied
directly and reported afterwards. Order:

1. **Front/Back** — translation idiomaticity; gender markers (Ukrainian gender of the
   head noun, verbs without markers); synonym/variant handling.
2. **Example** — UKR sentence grammar/style (word order, в/у euphony, calques,
   pleonasms); DE sentence naturalness and spelling; structure (UKR before first
   `<br>`, DE after, final periods).
3. **Tags** — exactly one level tag; `Redewendung` / `NoExample` / `BadTranslation`
   where applicable; add missing tags.
4. **Tag hygiene** — when the underlying issue is fixed in the same run (example
   added, translation replaced), remove the stale `NoExample` / `BadTranslation` tag
   directly and report it.

Possible outcomes, each requiring a user decision: field corrections, a second variant
separated by ` <i>oder</i> `, an italic cultural note at the field end, spelling fixes,
new cards or additional example sentences (see Phase 4).

## Phase 4 — Extend

- New cards: proposal table → approval → create → verify (as Phase 1).
- Additional example sentences (synonyms, aspect variants): propose — for new sentence
  drafts show the German version first — then append using the established multi-variant
  patterns.
- Text variants are separated by ` <i>oder</i> ` (German, italic — current convention).
  Legacy cards still use ` <i>або</i> `; convert to ` <i>oder</i> ` whenever such a card
  is edited (no standalone migration — see doc §1.2).

## Phase 5 — Audio

- Single file: delegate to the `ukrainian-example-audio` skill.
- Whole deck: doc §2.3/§3.2 — build the worklist from live data, batch TTS with resume,
  `store_media_file`, dry-run field update, verify.
- Special cases: `<i>або</i>` variants → audio for the first variant only; two-pair
  pattern → one file per pair (tag → UKR → DE → tag → UKR → DE).
- Split variant text only on the tagged separator (` <i>oder</i> `, legacy
  ` <i>або</i> `), never on plain text — "oder"/"або" occur inside Ukrainian words
  (substring trap).

## Inventory mode

Runs **only on explicit request** ("inventory", "deck status"). Read-only overview of
the `#7 - Sprachcafé` decks, e.g. as a table: format status (normed / legacy mix),
example-sentence coverage (UKR present?), tag coverage, audio coverage, counts of
`NoExample` / `BadTranslation`. No changes, no doc update from it alone.

## Wrap-up

- Report what changed and what remains open; remind about manual media/sync.
- Update `Anki-MCP-VerwendungUndAufbau.md` when the session changed data or revealed
  new conventions/tools/problems (§6: no changelog, no per-term facts, update the
  document date). Apply the doc changes first, then present them — no prior approval.
