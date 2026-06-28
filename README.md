# planets-game

## Workflow for creating Game Objects

Add a new prefab in `Game/content/prefabs`
Add a new custom controller in `Game/content/custom`
Add a the new custom controller to the prefab
All the logic in the custom content should already be applied
Now can use the new prefab in the scenes

## Adding a new display
1. In `window.py`
  - Create the new display in init
  - Add it to the `display_map`
  - Add to the `clear method`
  - Add to the `swap_buffers` method
2. In `game_state.py`
  - Add to `RenderGroup` enum
3. Use it in your prefab create method when adding a new renderer

