# Sun Tzu Hex Tactics - Modularized from your uploaded 8_suntzu_hex.py

Run:

```bash
pip install pygame
python main.py
```

The uploaded monolithic source is included as `8_suntzu_hex_original_uploaded.py` for reference.

Key modules:

- `main.py` - game loop
- `constants.py` - screen size, colors, terrain colors, UI rectangles
- `models.py` - dataclasses
- `state.py` - shared GameState object
- `scenarios.py` - principles, scenario list, maps, and unit setup
- `logic.py` - movement, combat, AI, victory rules, special actions
- `render.py` - drawing/UI/terrain decorations
- `input_handlers.py` - keyboard and mouse handling
- `assets.py` - scenario-specific unit image loading
- `hex_utils.py` - hex-grid math
