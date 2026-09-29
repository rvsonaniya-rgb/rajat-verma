# DNA Sequence Analyzer

**Author:** Rajat Verma (Integrated M.Tech, AI and Bioinformatics, VIT Bhopal)
**Project type:** VITyarthi - Build Your Own Project (Python)

---

## Overview

DNA Sequence Analyzer is a menu-driven Python program that does the basic analysis a biology student usually does by hand on a DNA strand. You give it a sequence, either by typing it or by loading it from a text/FASTA file, and it works out the base composition, GC content, reverse complement, RNA transcript and protein translation. It can also search for a motif and save everything into a report file.

I chose this project because it connects what we learned in the Python course (strings, dictionaries, loops, functions, file handling and exception handling) with my own field, bioinformatics. Doing these calculations by hand is slow and easy to get wrong, so this program does them in a second.

The full problem statement, scope and target users are in [statement.md](statement.md).

---

## Features

1. **Sequence input:** type a sequence or load it from a `.txt` / FASTA file
2. **Validation:** only `A`, `T`, `G`, `C` are accepted. Spaces and newlines are removed and lowercase is converted to uppercase automatically
3. **Base count and percentage** for A, T, G and C
4. **GC content** (in %)
5. **Reverse complement** of the strand
6. **Transcription:** DNA to RNA (T becomes U)
7. **Translation:** DNA to protein using the standard genetic code (stops at the first STOP codon)
8. **Motif search:** shows every 1-based start position where the motif appears, including overlapping matches
9. **Report:** saves the full analysis to `report.txt`
10. **Error handling:** invalid bases, empty input, missing files and wrong menu choices all give a clear message instead of crashing

---

## Technologies / Tools Used

- **Python 3.6 or above** (uses f-strings)
- **Python standard library only.** No external packages, so nothing extra to install
- **Git and GitHub** for version control

Python concepts used: functions, dictionaries, loops, string handling, file I/O, and `try / except` error handling.

---

## Steps to Install and Run

**1. Install Python 3.6 or newer** from [python.org](https://www.python.org/downloads/) and check it with:

```bash
python --version
```

**2. Get the project**

```bash
git clone <your-repository-link>
cd <repository-folder>
```

**3. Run the program**

```bash
python dna_analyzer.py
```

You will see this menu:

![Main menu](screenshots/menu.png)

Choose option **1** or **2** first to load a sequence. Options 3 to 9 all work on the sequence you loaded.

### Input file format

A plain text file or a FASTA file. Lines starting with `>` are skipped and all other lines are joined into one sequence:

```
>sample_sequence
ATGGCCATTGTAATGGG
CCGCTGA
```

---

## Instructions for Testing

The project is tested by running the program and comparing the output with the expected results below. All of these can be checked by hand.

### Test 1: Main example

Choose option 1 and enter `ATGGCCATTGTAATGGGCCGCTGA`.

| Option | Expected output |
|--------|-----------------|
| 3 - Base count | A: 5 (20.83%), T: 6 (25.0%), G: 8 (33.33%), C: 5 (20.83%) |
| 4 - GC content | 54.17 % |
| 5 - Reverse complement | `TCAGCGGCCCATTACAATGGCCAT` |
| 6 - Transcription | `AUGGCCAUUGUAAUGGGCCGCUGA` |
| 7 - Translation | `MAIVMGR` |
| 8 - Motif `ATG` | found 2 time(s) at positions: [1, 13] |

### Test 2: Input cleaning

| Input (option 1) | Expected result |
|------------------|-----------------|
| `atg gcc` | Sequence saved (6 bases). Lowercase and space are handled |
| `ATGXC` | Error: Invalid base 'X'. Only A, T, G, C are allowed. |
| (just press Enter) | Error: Sequence is empty. |

### Test 3: Edge cases

| Situation | Expected result |
|-----------|-----------------|
| Choose option 3 to 9 before loading a sequence | Please enter or load a sequence first (option 1 or 2). |
| Sequence `ATGTAA`, option 7 | `M` (translation stops at the STOP codon) |
| Sequence `TAA`, option 7 | (no protein produced) |
| Sequence `AAAA`, motif `AA` | found 3 time(s) at positions: [1, 2, 3] (overlaps counted) |
| Main example, motif `CCC` | 'CCC' not found. |
| Motif `ATX` | Error: motif must contain only A, T, G, C. |
| Option 2 with a wrong file name | Error: file not found. |
| Menu choice `12` | Invalid choice. Please enter a number from 0 to 9. |

### Test 4: File loading and report

1. Save the FASTA example above as `sample.txt` in the same folder
2. Choose option 2 and enter `sample.txt`. It should say the sequence was loaded (24 bases)
3. Choose option 9. A `report.txt` file should appear with the same results as Test 1

---

## Sample Report (`report.txt`)

```
==================================================
        DNA SEQUENCE ANALYSIS REPORT
==================================================
Sequence        : ATGGCCATTGTAATGGGCCGCTGA
Length          : 24 bases

Base composition:
  A :    5  (20.83%)
  T :    6  (25.0%)
  G :    8  (33.33%)
  C :    5  (20.83%)

GC content      : 54.17%
Reverse compl.  : TCAGCGGCCCATTACAATGGCCAT
RNA             : AUGGCCAUUGUAAUGGGCCGCUGA
Protein         : MAIVMGR
==================================================
```

---

## How It Works

- **Codon table:** instead of typing all 64 codons by hand, I generate them with nested loops from `BASES = "TCAG"` and a 64-letter amino acid string, where `*` means a STOP codon.
- **Translation:** starts at the first base, reads three letters at a time and stops at the first STOP codon.
- **Motif search:** slides a window across the sequence and records every match.

---

## Project Structure

```
dna_analyzer.py   # main program
README.md         # this file
statement.md      # problem statement, scope, target users, features
screenshots/      # screenshots used in this README
report.txt        # created when you choose option 9
```

---

## Limitations

- Only `A`, `T`, `G`, `C` are supported. Ambiguous bases like `N` are rejected.
- Translation always starts from the first base. It does not look for an `ATG` start codon or other reading frames.
- Only the standard genetic code is used.
- The report is always saved as `report.txt` and overwrites any existing file with that name.

---

## Future Improvements

- Translate all 6 reading frames and find ORFs
- Support IUPAC ambiguity codes
- Molecular weight and melting temperature calculation
- Let the user choose the report file name
