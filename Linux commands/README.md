# Linux commands

Terminal challenges I built so first-time Linux users could practice `find`, hidden files, `grep`, `file` and `tar`.

| Path | Concept | Build script | Difficulty |
|---|---|---|---|
| `ctfmaker.py` | Three-flag hunt: find by name, search file contents, count files including hidden ones | `ctfmaker.py` generates `ctf_challenge/` | Easy |
| `find/` (Level 1) | `find` across 100 directories | `find/generate.py` with `base_dir = 'ctf_challenge'` and a non-hidden flag file name | Easy |
| `find/` (Level 2) | Hidden dotfile across 100 directories | `find/generate.py` as written, generates `ctf_challengelevel2/` | Easy |
| `grep/` | Finding one token in about 780 KB of filler words. `workshop2.txt` is a small warm-up file. | `grep/generategrep.py` generates `challenge.txt` | Easy |
| `file/` | Checking a file's real type instead of its extension | `echo 'cybercamp{your_flag_here}' > cat.png` | Easy |
| `tar/` | Extracting a `.tar.gz` archive | `echo 'cybercamp{your_flag_here}' > flag.txt && tar -czf flag.tar.gz flag.txt && rm flag.txt` | Easy |

Notes:
- **Set your own flags first, then build.** The flags in `ctfmaker.py`, `find/generate.py` and `grep/generategrep.py` are placeholders. For `file/` and `tar/`, put your flag in the commands above.
- None of the generated files (`ctf_challenge/`, both `find` mazes, `grep/challenge.txt`, `file/cat.png`, `tar/flag.tar.gz`) are committed.
- Run the builders and commands from their own folders; create `file/` and `tar/` with `mkdir -p` if your clone doesn't have them. `ctfmaker.py` and `generate.py` delete their previous output directory before rebuilding.
- `find/level/` and `find/2/` are empty placeholders.

Solutions are intentionally not included. See the [main README](../README.md) for details.
