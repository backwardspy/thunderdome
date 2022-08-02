# thunderdome

## dependencies

requires the [battlesnake CLI](https://github.com/BattlesnakeOfficial/rules),
docker (recent enough for compose support), and python.

## usage

```bash
git submodule init --recursive --init --remote
docker compose build
docker compose up -d
python runner.py
```
