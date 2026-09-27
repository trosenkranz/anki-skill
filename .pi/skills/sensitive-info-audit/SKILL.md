---
name: sensitive-info-audit
description: Audit files, directories, or git changes for sensitive information (credentials, tokens, identifying data, personal content) before publishing or committing. Use when the user asks to check files for sensitive/private information, passwords, keys, or tokens, asks whether something is safe to share/publish/commit, or asks to re-check changed or new files after edits.
---

# Sensitive Info Audit

Check whether target files contain material that must not become public: credentials,
identifying details, or personal content. Run it as sweep → classify → report; fix
only on the user's decision, then re-verify.

## 1. Scope

- Named files/directories: list them (`ls -la` — include hidden files; `.env` and
  dot-directories are the classic carriers).
- "Check what changed": run `git status --porcelain`. Then
  - modified files → read the diff (`git diff <file>`; for large diffs scan only the
    added lines: `git diff <file> | grep -E '^\+[^+]'`),
  - untracked files → inspect them directly like any new file.
  State which commit/branch state the verdict refers to.
- Skip generated dependency trees (`.venv`, `node_modules`) for content, but flag them
  as publish-blockers by size and check them only for stray secret files
  (`find <dir> -name '*.env*' -o -name '*key*'`).

## 2. Sweep

Run every sweep as a `grep -nEi` over all targets, one combined pattern per group.
Completion criterion: every group below has run over every target file, and every hit
is either classified or dismissed as a false positive.

1. **Credentials:** `api[_-]?key|token|secret|password|passwort|pwd|authorization|bearer|--key[ =]|sk-[A-Za-z0-9]{10,}|AKIA[0-9A-Z]{16}|ey[A-Za-z0-9_-]{10,}\.ey`
2. **Identifying:** `/home/[A-Za-z0-9_-]+` (absolute paths leak the account name), email pattern `[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}`, phone patterns (`\+49`, `\+380`)
3. **Project-specific names:** grep for the local username and hostname found in the
   environment (`whoami`, `hostname`) — catches refs that pattern 2 misses.

For any file that *is* a secret store (`.env` etc.): list key names only
(`cut -d= -f1`), never values. If a value must be inspected, **mask it**:
`sed -E 's/=(.{4}).*/=\1***MASKED***/'`. Never paste an unmasked secret value into the
conversation, even on the user's own machine — transcripts travel.

Then **read** a sample of each file (head, plus any hit's surroundings). Sweeps miss
what reads catch: stale doc claims, session UUIDs, personal context, infra hints.

## 3. Classify

A hit is a **pointer** or a **value** — the distinction decides everything:

- **Pointer** (safe): the *name* of an env var (`CARTESIA_API_KEY`), the *location*
  where a secret is stored (`bin/.env`), a tool name. Report only as an infra hint.
- **Value** (critical): the secret itself — key strings, passwords, tokens, private
  keys. Any hit of group 1 that resolves to an actual value is a blocker.

Scale for the report:

- ❌ **Critical** — credential values, private keys. Must be removed/rotated.
- ⚠️ **Identifying / infra** — usernames in paths, emails, phone numbers, secret
  storage locations, sandbox/infra quirks. Genericize or accept consciously.
- ⚪ **Personal context** — learning content, progress data, notes. Rarely a blocker;
  name it so the user decides with eyes open.

Also check, and report as findings:

- **Claim-vs-reality:** does documentation claim a secret lives somewhere it doesn't
  (or vice versa)? Fix stale claims — future agents otherwise hunt for or restore keys.
- **Permissions:** secret stores should be `600` (`ls -la`).
- **Ignore coverage:** are `.env`, `.venv/`, generated media gitignored? (`git check-ignore -v <path>`)

## 4. Report

Per-file table: file → finding → classification. Close with a verdict (safe to
publish/commit or not) and concrete remediation offers. Keep masked values masked.

## 5. Fix and re-verify

Apply fixes only after the user approves them. Established fixes from this project:

- Absolute paths → `~` in prose, `~`-based paths in code only via
  `os.path.expanduser("~/…")` (Python does not expand a bare `~` — say so in a comment).
- Stale secret-storage claims → rewrite to the verified reality ("only via env var,
  `<file>` contains no key").
- After every fix: re-run the full sweep on the touched files. Completion criterion:
  zero remaining hits (or only classified-and-accepted ones), confirmed by grep output
  in the report.
