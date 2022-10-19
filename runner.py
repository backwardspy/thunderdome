import random
import subprocess
from pathlib import Path
from uuid import uuid4

snakes = [
    ("doctor strangle", 2000),
    ("david hisselhoff", 2001),
    ("marty the battlesnake", 2002),
    ("battlesnake galactica", 2003),
    ("johnny slitherhand", 2004),
    ("taipan no prisoners", 2005),
    ("calm snek", 2006),
    ("king kobra", 2007),
    ("serpentipity", 2008),
    ("battle boogie", 2009),
]

OUTPUT_PATH = Path("games/")

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
i = 0
while True:
    i += 1
    game_id = uuid4()
    combatants = random.sample(snakes, 2)
    print(
        f"running game #{i} - {combatants[0][0]} vs {combatants[1][0]} ({game_id})"
    )
    cmd = [
        "battlesnake",
        "play",
        "--output",
        str(OUTPUT_PATH / f"{game_id}.json"),
    ]

    for name, port in combatants:
        cmd.extend(("--name", name, "--url", f"http://localhost:{port}"))

    subprocess.run(cmd, stderr=subprocess.PIPE)
