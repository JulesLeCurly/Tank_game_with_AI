**Tank Game With AI**

A small 2D tank game built with Pygame. The project implements terrain generation, tanks, shooting, explosions (particles), basic hit/damage, sound, and simple UI elements. It is designed as a learning / hobby project and can be extended with AI players.

**Features**
- **Terrain**: Procedurally generated and editable terrain saved to `Images/Terrains/Terrain.png`.
- **Tanks**: Multiple tanks with independent controls, angle and power settings.
- **Project elements**: Projectile physics, collision detection, particles for explosions, simple sound effects.

**Requirements**
- **Python**: 3.8+ recommended.
- **Python packages**: `pygame`, `numpy`, `pillow` (PIL), `colorama`.

Install dependencies (PowerShell):

```
python -m pip install --upgrade pip
pip install pygame numpy pillow colorama
```

**Run**
- From the project root run:

```
python Main.py
```

or run the game loop directly (development):

```
python Function/core/Game_env.py
```

**Controls (default two-player keyboard)**
- **Red tank**:
  - Rotate turret: `A` (left) / `E` (right)
  - Power: `Z` (increase) / `S` (decrease)
  - Move: `Q` (left) / `D` (right)
  - Shoot: `F`
- **Blue tank**:
  - Rotate turret: `I` (left) / `P` (right)
  - Power: `O` (increase) / `L` (decrease)
  - Move: `K` (left) / `M` (right)
  - Shoot: `J`

**Project structure**
- `Main.py` and `test.py`: entry/test scripts.
- `Function/core/`: game modules
  - `Game_env.py`: main Pygame loop, input handling and game orchestration.
  - `Terrain.py`: terrain generation, image export, and terrain modification (destruction).
  - `Tank.py`, `Balle.py`, `Particule.py`, `Cible.py`, `Life.py`, `son.py`, `Cloud.py`: game objects and helpers.
- `Images/`: game images (terrain image is produced here).
- `Sounds/`: audio files used by `son.py`.

**Notes & Tips**
- The terrain generator writes `Images/Terrains/Terrain.png`. If the directory or the image is missing, run the game — the generator will create the image.
- To change the number of tanks, edit the `nb_tank` variable in `Function/core/Game_env.py`.
- If you modify terrain via explosions, the code updates `self.array_terrain` and re-saves the terrain image.

**Troubleshooting**
- If Pygame fails to initialize audio on Windows, ensure your audio drivers are installed and try running the script from a normal (non-WSL) Python environment.
- If you get missing module errors, re-run the `pip install` command above.

**Extending the project**
- Add AI agents by creating a controller class that chooses moves and shots and plug it in place of keyboard input in `Game_env.py`.
- Add networked multiplayer, new weapons, or smoother physics.

**License & Contribution**
- This project currently has no license feel free to use the code the way you want.
