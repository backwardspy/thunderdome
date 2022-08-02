from uuid import uuid4
from pathlib import Path
import random
import subprocess

snakes = [
    ("doctor strangle", 2000),
    ("david hisselhoff", 2001),
    ("marty the battlesnake", 2002),
    ("battlesnake galactica", 2003),
    ("johnny slitherhand", 2004),
    ("taipan no prisoners", 2005),
    ("calm snek", 2006),
    ("king kobra", 2007),
    ("hangry", 2008),
]

RUNS = 1000
OUTPUT_PATH = Path("games/")

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
for i in range(RUNS):
    game_id = uuid4()
    combatants = random.sample(snakes, 2)
    print(
        f"running game #{i} of {RUNS} - {combatants[0][0]} vs {combatants[1][0]} ({game_id})"
    )
    cmd = [
        "battlesnake",
        "play",
        "--output",
        str(OUTPUT_PATH / f"{game_id}.json"),
    ]

    for name, port in combatants:
        cmd.append("--name")
        cmd.append(name)
        cmd.append("--url")
        cmd.append(f"http://localhost:{port}")

    subprocess.run(cmd, stderr=subprocess.PIPE)
