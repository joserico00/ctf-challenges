# Forensics

Hashing, encryption, metadata and binary-analysis challenges I built for beginner workshops. Several include the script used to build them.

| Path | Concept | Build script | Difficulty |
|---|---|---|---|
| `aes/` | AES-CBC encryption (key, IV, padding, Base64) | `aes.py` prints the ciphertext | Medium |
| `dictionary/` | Wordlist attack on an unsalted SHA-256 hash | `dic.py` generates `dictionary.txt` and `hashed_password.txt` (not committed) | Easy-Medium |
| `md5sum/` | Matching a file to a given MD5 digest | `md.py` regenerates `cybercamphashes/file1.txt` to `file10.txt` (a sample set is committed) and prints the target hash | Easy |
| `forensic photos/` | EXIF metadata and GPS geolocation from photos | Static images | Easy-Medium |
| `geocodes/` | Turning a coordinate pair into a place | Static file | Easy |
| `stri.c` | Extracting strings from a compiled binary | Compile it yourself, e.g. `cc stri.c -o flag_finder` (no binary is committed) | Easy |
| `strings/` | Empty placeholder | — | — |

The flags in `aes.py` and `stri.c`, and the password in `dic.py`, are placeholders: set your own values first, then run the build scripts and compile `stri.c`. Once set, the build scripts and `stri.c` contain answers in plain text, so give players only the generated artifacts. Solutions are intentionally not included. See the [main README](../README.md) for build and hosting notes.
