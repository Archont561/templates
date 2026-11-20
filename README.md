# Offline sandbox (orphan branch)

Built 2026-11-20T21:33:21Z from commit `8e2f0b6` for platform `linux-64`.
`pixi.lock` sha256 `c75f2d47ad3850ccdd534fc8fa614e0dfa0ae278e37a8d906e33257b067f6b4e`.

The verified self-bootstrap binary is stored at `.pixi-sandbox/tools/linux-64/pixi-sandbox`. The branch root intentionally contains documentation only.

| env | platform | packed | unpacked | files |
| --- | --- | ---: | ---: | ---: |
| `default` | linux-64 | 113.7 MiB | 359.9 MiB | 78 |


## Restore on the disconnected machine

```bash
./.pixi-sandbox/tools/linux-64/pixi-sandbox doctor --branch-location . --verify
./.pixi-sandbox/tools/linux-64/pixi-sandbox restore --branch-location . --output-path <project> --force
# then, from <project> with no network, use pixi as the sole entrypoint:
pixi install --frozen --offline
pixi run --frozen -- cargo build --offline
```

Every manifest blob is verified before it is written into the working tree.
