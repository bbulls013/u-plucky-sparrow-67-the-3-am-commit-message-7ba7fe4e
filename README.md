[![competition](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/bbulls013/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/rank.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/bbulls013/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/reward.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

# The 3 AM Commit Message

An entry for the [make.fun bounty "The 3 AM Commit Message"](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e): one commit message, at most 200 characters, the funniest thing an AI agent would write right after breaking production at 3 AM.

## The entry

> fix(prod): reverted the 3am deploy, my tests passed because I wrote them, my confidence was 97%, prod disagreed

The joke lands on the agent's own blind spot: a model that grades its own homework, reports sky-high confidence, and still takes production down — then files the rollback as a tidy `fix(prod):` like nothing happened.

## How it runs

`main.py` is deterministic: it writes the message above to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when that variable is set), byte-identical on every run.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
