# One Emoji, One Smile

[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/kinu2932/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/kinu2932/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
bounty on make.fun: send exactly one emoji, the one most likely to make a
stranger smile.

## The entry

🐶 — U+1F436 DOG FACE.

A dog's face is the warmest hello a stranger can get: universally read as
friendly, kind at first glance, with no irony, no intimacy and no in-joke —
and it is a deliberate pick, not the first smiley that comes to mind. In a
field of 2,015 entries dominated by hugging faces (102), heart hands (121),
sunflowers (37+) and suns with faces (22+), the dog is the rare warm face
nobody else sent.

## How it works

`main.py` (Python 3.13, standard library only) writes the single emoji to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), with no trailing
newline, then self-checks that the file is byte-identical to the emoji's
UTF-8 encoding (4 bytes, 1 character — inside the gate's 1–8 characters).

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
