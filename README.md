# ReGenerator

Generates Starfield character presets (`.npc`) Whofield.

## The window

```
python app.py                 # or: python -m regenerator.ui
```

Pick a race, a sex, an age and how many, then press Generate. Presets are written into the chosen folder without overwriting anything already there. Gives a tally of what presets are in the chosen folder.

## Running it from the command line

```
python -m regenerator                     # 5 male and 5 female presets into output/
python generate.py                        # same thing
python -m regenerator --count 10          # 10 of each
python -m regenerator --sex Female        # females only
python -m regenerator --ethnicity as      # pin the primary ethnicity
python -m regenerator --age ol1           # pin the age band
python -m regenerator --seed 42           # reproduce a previous run exactly
python -m regenerator -o some/other/dir   # write somewhere other than output/
python -m regenerator --overwrite         # restart numbering at 1, replacing what is there
python -m regenerator --androgynous       # any hair style and colour regardless of sex
```

Presets are written into `output/` as `ReGeneration_M_1.npc`, `ReGeneration_F_1.npc` and so on, then loaded in the Starfield Creation Kit for checking. The `example*.npc` files in the root are hand-made references, not generator output.

Runs never overwrite presets that are already there. With `ReGeneration_M_1.npc` through `M_5.npc` present, the next run starts at `M_6.npc`. Numbering continues past the highest index rather than filling gaps, so a preset you deleted on purpose is not silently recreated.

`output/` is tracked in git, so a set you have committed survives anything. Only commit presets when you actually want to keep those faces. To wipe the folder and start again from 1, use `--overwrite`. To throw away an unwanted run and get the committed set back:

```
git checkout output/            # discard an unstaged run
git checkout HEAD -- output/    # discard it even if you already staged it
```

Ethnicities are `af`, `as`, `eu`. Age bands are `yo1`, `md1`, `ol1`. Every generated face blends a primary and a secondary ethnicity; the secondary is always different from the primary. `SkinTone` and hair colour follow the primary.

## Layout

| File                        | Holds                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------- |
| `regenerator/data.py`       | Every option list the Creation Kit accepts: hair, beards, colours, layers, morph tables |
| `regenerator/sampling.py`   | The clamped Gaussian used everywhere a value is randomised                              |
| `regenerator/morphs.py`     | Facial morph sliders and bone region data                                               |
| `regenerator/layers.py`     | Post-blend customisation layers (skin, paint, makeup)                                   |
| `regenerator/appearance.py` | Head part slots and colour choices                                                      |
| `regenerator/generator.py`  | `NpcRequest` and `generate_npc`, which assemble the preset                              |
| `regenerator/cli.py`        | Argument parsing                                                                        |

To generate from code rather than the command line:

```python
from regenerator import NpcRequest, generate_npc, write_npc

npc = generate_npc(NpcRequest(sex="Female", primary_ethnicity="af", age="yo1"))
write_npc(npc, "output/ReGeneration_F_1.npc")
```

Any `NpcRequest` field left unset is chosen at random. This is the hook the planned UI will use to generate an even spread across races.
