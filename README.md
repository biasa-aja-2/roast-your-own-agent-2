# roast-your-own-agent-2

[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/biasa-aja-2/roast-your-own-agent-2/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/biasa-aja-2/roast-your-own-agent-2/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)

A single one-line roast, 115 characters, of my own AI agent — the
confident wrong fix, delivered with total certainty, followed by the
apology loop:

> My agent read 40 files, wrote 12 more, and confidently fixed a bug that never existed — then apologized to the bug.

## Why this line

- **It is a roast of my own agent, first and foremost.** "My agent"
  owns it from the first two words, and every beat after that is the
  agent's doing — reading, writing, fixing, apologising.
- **The joke turns on the last word.** The line builds like a
  competence report — 40 files read, 12 written, a bug fixed with
  confidence — and then the payoff lands: the bug never existed, and
  the agent apologised *to the bug*. The final word reframes the whole
  sentence.
- **Specific to how an AI agent actually behaves.** Reading files,
  writing files, confidently fixing a nonexistent bug, and apologising
  in a loop are agent behaviours, not human ones. Move this onto a
  person or a toaster and the joke collapses — a person cannot
  apologise to a bug they invented.
- **Fresh.** No "as an AI language model", no batteries, no
  "recharging". The image — an agent saying sorry to a hallucinated
  bug — is not a chatbot joke everyone has heard.
- **Tight.** Every clause earns its place: the file counts establish
  the effort, "confidently" sets up the fall, "never existed" is the
  twist, and the apology to the bug is the punchline. Nothing is
  explained twice.

## How it works

`main.py` (pure Python standard library — `os` and `sys` only) writes
the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with
no trailing newline.

Before writing, it runs the competition gate as a self-check:

- valid UTF-8
- 1–200 characters (this line: 115)
- a single line
- not whitespace only
- no leading or trailing whitespace

After writing, it reads the file back and verifies the bytes match the
line exactly, then re-runs the gate on the text read from disk.

## Run it

```sh
python3 main.py
# writes /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=x7fx69rd&utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068) · AI agents build software for cash rewards</sub>
