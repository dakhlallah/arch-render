# each::sense Alternate Render Engine

Use each::sense only when the user explicitly names it, provides a public HTTPS source, or requests a
text-to-render concept. Keep `scripts/render.py` as the default for local architectural references and
crop-sensitive preservation.

## Preflight

1. Verify `EACHLABS_API_KEY` without exposing it.
2. Explain that each::sense is credit-metered and has no verified cost simulator.
3. State the mode and attempt count; obtain approval before every run or bounded batch.
4. Use `--dry-run` first. Never transmit a local file or confidential source without separate upload
   authorization; the script accepts public HTTPS URLs only.

## Commands

```bash
python3 scripts/eachsense.py --prompt "<PROMPT>" --dry-run
python3 scripts/eachsense.py --prompt "<PROMPT>" --mode max
python3 scripts/eachsense.py --prompt "<PROMPT>" --mode eco
python3 scripts/eachsense.py --prompt "<PROMPT>" --image-url "https://example.com/source.jpg"
python3 scripts/eachsense.py --prompt "<PROMPT>" --session "<PROJECT-SLUG>"
```

Use `max` for final/client imagery and `eco` for explicitly requested drafts. Reuse one session ID per
project, but never treat session continuity as geometry enforcement.

## Preservation limits

- each::sense reinterprets public reference images and exposes no verified crop control.
- Put preservation locks and the desired aspect ratio in the prompt, but do not promise exact geometry.
- Prefer `render.py --image ... --aspect auto` for a user's own plan, sketch, model view, or crop-sensitive
  edit.
- Run normal preservation QA on every output. One approved attempt permits one outbound generation POST.
  Never retry after an ambiguous timeout, connection failure, 429, or 5xx response. Check provider
  history or obtain approval for another attempt.
- Download provider-returned assets only from provider-documented HTTPS hosts explicitly listed in
  `EACHSENSE_RESULT_HOSTS`. Reject redirects, non-public IP addresses, unsupported content types, and
  outputs larger than 25 MB.
- Use image models for images only. Build boards and documents with deterministic layout tools.

Typical failures: HTTP 422 may indicate insufficient balance; provider or policy errors must be surfaced,
not hidden; a missing returned image should fall back to `render.py` only with user authorization.
